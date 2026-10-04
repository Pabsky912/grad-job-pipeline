"""Run with: python -m unittest discover tests"""
import contextlib
import csv
import io
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import pipeline  # noqa: E402


def run(*argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = pipeline.main(list(argv))
    return code, buf.getvalue()


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.ws = os.path.join(self.tmp, 'my-search')

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def rows(self, name='tracker.csv'):
        with open(os.path.join(self.ws, name), encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def test_init_creates_workspace(self):
        run('--workspace', self.ws, 'init')
        for f in ('profile.md', 'preferences.json', 'tracker.csv', 'contacts.csv', 'fact_bank.md', 'voice.md', 'log.md'):
            self.assertTrue(os.path.exists(os.path.join(self.ws, f)), f)
        json.load(open(os.path.join(self.ws, 'preferences.json')))

    def test_add_dedupes_and_keeps_status(self):
        run('--workspace', self.ws, 'init')
        item = {'org': 'Acme Bio', 'role': 'Research Assistant', 'link': 'https://example.com/1', 'why': ['a', 'b']}
        run('--workspace', self.ws, 'add', '--json', json.dumps(item))
        rows = self.rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['id'], 'acme-bio-research-assistant')
        self.assertEqual(rows[0]['why'], 'a ; b')
        self.assertEqual(rows[0]['status'], 'new')
        # person changes status; a re-add must not overwrite it
        rows[0]['status'] = 'applied'
        pipeline.write_csv(os.path.join(self.ws, 'tracker.csv'), rows, pipeline.TRACKER_COLS)
        run('--workspace', self.ws, 'add', '--json', json.dumps(dict(item, role='research assistant', status='new', score='4')))
        rows = self.rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['status'], 'applied')
        self.assertEqual(rows[0]['score'], '4')

    def test_check_flags_problems(self):
        run('--workspace', self.ws, 'init')
        run('--workspace', self.ws, 'add', '--json', json.dumps({'org': 'A', 'role': 'B', 'deadline': '31/12/2026', 'status': 'maybe'}))
        code, out = run('--workspace', self.ws, 'check')
        self.assertEqual(code, 1)
        self.assertIn('not YYYY-MM-DD', out)
        self.assertIn('unknown status', out)
        self.assertIn('TODO', out)

    def test_example_workspace_is_valid_and_builds(self):
        ex = os.path.join(self.tmp, 'example')
        shutil.copytree(os.path.join(ROOT, 'examples', 'sample-candidate'), ex)
        code, out = run('--workspace', ex, 'check')
        self.assertEqual(code, 0, out)
        run('--workspace', ex, 'today')
        run('--workspace', ex, 'dashboard')
        html = open(os.path.join(ex, 'dashboard.html'), encoding='utf-8').read()
        self.assertNotIn('/*__DATA__*/null', html)
        self.assertIn('Example Neuroscience Institute', html)
        run('--workspace', ex, 'calendar')
        ics = open(os.path.join(ex, 'deadlines.ics'), encoding='utf-8', newline='').read()
        self.assertTrue(ics.startswith('BEGIN:VCALENDAR'))
        self.assertIn('BEGIN:VEVENT', ics)
        self.assertNotIn('Commercial Graduate Scheme', ics)  # not-for-me rows are left out
        for line in ics.split('\r\n'):
            self.assertLessEqual(len(line.encode('utf-8')), 75)

    def test_import_changes_round_trip(self):
        ex = os.path.join(self.tmp, 'example')
        shutil.copytree(os.path.join(ROOT, 'examples', 'sample-candidate'), ex)
        changes = os.path.join(self.tmp, 'changes.csv')
        new_row = json.dumps({'id': 'own-beta-lab-ra', 'org': 'Beta Lab', 'role': 'RA', 'status': 'shortlist', 'source': 'own find'})
        with open(changes, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['kind', 'id', 'field', 'value', 'new_row'])
            w.writerow(['item', 'jobsacuk-EX1001', 'status', 'drafting', ''])
            w.writerow(['item', 'own-beta-lab-ra', 'status', 'shortlist', new_row])
            w.writerow(['contact', 'dr-a-example', 'status', 'sent', ''])
        run('--workspace', ex, 'import-changes', changes)
        with open(os.path.join(ex, 'tracker.csv'), encoding='utf-8') as f:
            rows = {r['id']: r for r in csv.DictReader(f)}
        self.assertEqual(rows['jobsacuk-EX1001']['status'], 'drafting')
        self.assertIn('own-beta-lab-ra', rows)
        with open(os.path.join(ex, 'contacts.csv'), encoding='utf-8') as f:
            self.assertEqual({r['id']: r for r in csv.DictReader(f)}['dr-a-example']['status'], 'sent')

    def test_cv_render(self):
        out = os.path.join(self.tmp, 'cv.html')
        run('cv', os.path.join(ROOT, 'examples', 'sample-candidate', 'cv.json'), '--out', out)
        html = open(out, encoding='utf-8').read()
        self.assertIn('Jordan Reyes', html)
        self.assertIn('<b>Grades: </b>', html)

    def test_fetch_parsers(self):
        fake = {
            'greenhouse': {'jobs': [{'id': 1, 'title': 'Graduate Scientist', 'absolute_url': 'https://x/1', 'location': {'name': 'London'}, 'updated_at': '2026-10-01T00:00:00Z', 'content': '&lt;p&gt;Hi&lt;/p&gt;'}]},
            'lever': [{'id': 'abcdef123', 'text': 'Research Assistant', 'hostedUrl': 'https://x/2', 'categories': {'location': 'Remote'}, 'createdAt': 1790000000000}],
            'ashby': {'jobs': [{'id': 'zz', 'title': 'Data Analyst', 'location': 'Berlin', 'isRemote': True, 'jobUrl': 'https://x/3', 'publishedAt': '2026-09-01', 'isListed': True}]},
            'workable': {'jobs': [{'title': 'Lab Tech', 'shortcode': 'AB1', 'url': 'https://x/4', 'city': 'Madrid', 'country': 'Spain'}]},
            'recruitee': {'offers': [{'id': 9, 'title': 'Intern', 'careers_url': 'https://x/5', 'location': 'Amsterdam'}]},
        }
        orig = pipeline.http_json
        try:
            for ats, payload in fake.items():
                pipeline.http_json = lambda url, timeout=25, p=payload: p
                jobs = pipeline.fetch_board(ats, 'acme')
                self.assertEqual(len(jobs), 1, ats)
                self.assertTrue(jobs[0]['link'].startswith('https://'), ats)
                self.assertTrue(jobs[0]['role'], ats)
        finally:
            pipeline.http_json = orig


if __name__ == '__main__':
    unittest.main()

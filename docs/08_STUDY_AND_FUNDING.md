# 08 · Master's, PhD and funding

Further study is a track like any other: rows go into `tracker.csv` with
`track` = `masters`, `phd` or `funding`, and Scout judges them the same way.
The differences are the sources, the calendar and the eligibility checks.

## What to collect per programme

Programme name, university, country, length, start date, tuition for the
person's fee status, the application window (opens and closes, and whether
there are rounds), entry requirements (degree class or GPA, subjects, language
tests), documents (statement, references, CV, transcript, portfolio, GRE),
whether interviews happen, and which scholarships are tied to the application
deadline. Put the essentials in the tracker row and the rest in `notes`.

## Fee status and eligibility (check every time, never assume)

- Tuition often depends on citizenship and residence (home, EU, international),
  and rules change. Quote the university's own fees page.
- Many scholarships have narrow rules: nationality, where the first degree was
  taken, field, age, or "must not already hold a Master's". Read the rules page
  and record exactly which rule makes the person eligible or not. Keep a
  "checked, not eligible" list in `notes` or in `log.md` so the same scheme isn't
  rechecked every run.
- PhD routes differ by country: direct entry after a bachelor's is common in
  some (for example integrated or "fast-track" programmes) and rare in others.

## Sources

- Programme search: FindAMasters, FindAPhD, Mastersportal and PhDportal,
  the DAAD programme database (Germany), Study in Holland, Study in Sweden,
  the university's own department pages.
- Structured doctoral programmes and graduate schools at research institutes
  (many have one main call a year, often between October and January).
- Funding: the university's own scholarships page (often the most useful),
  national agencies (for example DAAD in Germany, Fulbright for US exchange,
  research councils' doctoral training partnerships in the UK), Erasmus Mundus
  joint Master's scholarships, private foundations in the person's home country,
  and subject societies' travel or summer grants.
- Web search: `"<field>" master's scholarship <country> <year>`,
  `"<programme name>" deadline <year>`.

## Judging study options

Use the same verdicts, with study-specific factors: fit with the research or
career direction in `profile.md`, the entry requirements versus their grades,
total cost after any realistic funding, the quality of supervision or
placements, and where graduates go next. Be plain about cost: an unfunded
programme in an expensive city is a real watch-out.

## Calendar

Study deadlines are clustered and unforgiving. For every programme and
scholarship row, set `opens`, `deadline` and a `next_step` such as "ask Dr X for
a reference by <date>" (references need 3 to 4 weeks' notice). Run
`python tools/pipeline.py calendar` so the reminders reach their calendar.

## Statements of purpose

Same rules as cover letters ([`05_CV_AND_LETTERS.md`](05_CV_AND_LETTERS.md)):
facts from the fact bank only, one paragraph specific to that programme (named
modules, labs, people, and why), the person's own voice, and the exact word
limit the programme sets.

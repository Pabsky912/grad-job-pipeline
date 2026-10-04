# grad-job-pipeline

**A free job-search partner for students and graduates, run by the AI you already use.**

grad-job-pipeline turns Claude, ChatGPT, Codex, Gemini, Cursor, Copilot or any
similar assistant into a careful, honest job-search partner. It interviews you
to learn what you want, searches real job boards, judges every posting against
your profile with reasons, keeps your applications and deadlines in one place,
and drafts tailored CVs, cover letters, cold emails and LinkedIn notes in your
own voice.

No account, no subscription, no server. It's a method written for AI agents,
some templates, and a small optional Python script. Your details stay in a
private folder on your computer.

Built for early careers (research assistant roles, graduate schemes,
internships, entry-level jobs, Master's and PhD places, scholarships) in any
field and any country.

---

## Try it (2 minutes)

**If your AI can work with files** (Claude Code, Claude desktop app with a
folder, Codex, Cursor, Gemini CLI, Copilot in VS Code, Windsurf...), paste this:

```
Clone https://github.com/Pabsky912/grad-job-pipeline, open AGENTS.md and follow it to set me up.
```

or download the ZIP from the green **Code** button, unzip it, open the folder in
your AI tool and say **"set me up"**.

**If you use a plain chat window** (ChatGPT, Claude.ai, Gemini or Copilot on the
web), paste the prompt in [`prompts/chat_kickoff.md`](prompts/chat_kickoff.md),
ideally inside a Project / custom GPT / Gem with the `docs/` files uploaded. See
[`docs/10_CHAT_ONLY.md`](docs/10_CHAT_ONLY.md).

## What happens next

1. **Onboarding (20 to 30 min).** Your AI reads your CV, builds a *fact bank* of
   things you can actually claim, and interviews you a few questions at a time:
   what kinds of work, where, from when, right to work, what you enjoyed and what
   drained you, hard no's.
2. **Taste calibration.** It shows you 8 to 10 real, open postings that
   deliberately vary, and you answer yes / maybe / no with a few words. That
   teaches it your taste far better than abstract questions.
3. **Scout.** It searches job boards and employers' public job feeds, screens out
   what you can't apply for, opens every remaining posting, and judges it:
   **strong / worth a look / stretch / skip**, a 1 to 5 fit score, why it fits
   and what to watch out for.
4. **Pipeline.** Everything lands in one tracker (a CSV that opens in Excel or
   Google Sheets), with an offline dashboard and a calendar file of deadlines.
5. **Applying.** One-page tailored CVs from your fact bank (never invented),
   cover letters, form answers, cold emails to professors or teams, and LinkedIn
   connection notes under 200 characters, all in your voice. You send them.
6. **Routine.** Every few days: new finds, deadlines in the next two weeks,
   follow-ups owed. Five minutes of your time.

## What you can say to it

| | |
|---|---|
| "Set me up." | Runs onboarding |
| "Anything new today?" / "Run Scout." | Quick or full search, judged |
| "Is this one for me? *link*" | Judges a single posting |
| "Here's my LinkedIn job alert: *paste*" | Checks and judges a pasted list |
| "Tailor my CV for the Acme role." | One-page CV from your fact bank |
| "Write to Professor X about RA roles." | A cold email with a paragraph only they could receive |
| "Who should I contact on LinkedIn this week?" | A queue of people and notes |
| "I applied to Acme." / "Not for me: too much sales." | Updates the tracker and learns |
| "What's due?" / "Build my dashboard and calendar." | Digest, dashboard, `.ics` file |
| "Set up a routine every 3 days." | Scheduled check-ins, if your tool supports them |

More in [`prompts/quick_prompts.md`](prompts/quick_prompts.md).

## The dashboard

`python tools/pipeline.py dashboard` builds a single offline page (works in any
browser, light and dark mode, phone or laptop) with tabs for Scout finds,
your pipeline by track, deadlines, outreach and your profile. Click to shortlist,
dismiss with a reason, set statuses, copy messages, then **Export changes** and
your AI writes them back into the tracker.

See it with fictional data: build the example
(`python tools/pipeline.py --workspace examples/sample-candidate dashboard`) and
open `examples/sample-candidate/dashboard.html`.

## How it's organised

```
AGENTS.md              entry point for any AI agent (CLAUDE.md and GEMINI.md point here)
docs/
  01_ONBOARDING.md     the profile interview and taste calibration
  02_SCOUT.md          count, screen, pull and judge postings
  03_SOURCES.md        job boards and public employer job feeds, by region
  04_TRACKER.md        tracker columns, statuses, dashboard, calendar, Excel
  05_CV_AND_LETTERS.md tailored CVs and cover letters from verified facts
  06_OUTREACH_EMAILS.md cold emails that get read
  07_LINKEDIN.md       who to contact, notes under 200 characters, follow-ups
  08_STUDY_AND_FUNDING.md Master's, PhD and scholarships
  09_ROUTINE.md        the every-few-days loop and scheduling
  10_CHAT_ONLY.md      using it in a plain chat window
templates/             starting files for your workspace
prompts/               copy-paste prompts (chat kick-off, scheduled routine, examples)
tools/pipeline.py      optional helper: init, add, check, today, fetch, dashboard, calendar, cv, xlsx
tools/cv_docx.js       optional Word CV renderer (needs Node and `npm install docx`)
skills/                a skill file for assistants that support Agent Skills
examples/              a complete fictional workspace to look at
my-search/             YOUR workspace, created on first run, git-ignored
```

## The helper script (optional)

Python 3.9+, standard library only:

```bash
python tools/pipeline.py init          # create my-search/ from the templates
python tools/pipeline.py today         # what's due, what's new, who to follow up
python tools/pipeline.py fetch greenhouse <company-slug> --q "graduate,research"
python tools/pipeline.py dashboard     # my-search/dashboard.html
python tools/pipeline.py calendar      # my-search/deadlines.ics
python tools/pipeline.py check         # catch duplicates, bad dates, unverified emails
python tools/pipeline.py --help
```

Your AI runs these for you. If it can't run code, it edits the CSV and Markdown
files directly; everything still works.

## Principles

- **Never invent.** No made-up postings, deadlines, requirements, contacts or
  achievements. Every posting is opened before it's judged; every CV line traces
  to your own documents.
- **Honest verdicts.** A weak match is called weak, and eligibility problems are
  flagged up front.
- **You stay in control.** The AI drafts; you apply and send.
- **No bots on LinkedIn** or other sites that forbid them. Public pages and
  official job feeds only, robots.txt respected.
- **Private by default.** Your workspace never leaves your computer through this
  kit, and `my-search/` is git-ignored so a fork can't leak it.

## Privacy note

The kit itself sends nothing anywhere. Your AI provider sees what you share in
the conversation, as with any use of that assistant; check its data settings.
The only network calls the helper script makes are to public job-board feeds
you ask it to read.

## Contributing

Ideas, new sources that work, better prompts and fixes are welcome: open an
issue or a pull request. Please never include real personal data in examples.

## Credits

Inspired by agent-first job tools such as [Pinloop](https://github.com/pinloop-ai/pinloop-cli),
which showed how good a job board "for your coding agent" can feel. This project
takes a different route: free, file-based, and built around a student's whole
search, not just postings. Not affiliated with Pinloop or any AI provider.

MIT licence. See [LICENSE](LICENSE).

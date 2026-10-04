# 10 · Using the kit in a plain chat window

Some assistants can browse the web but can't read or write files on the
person's computer (for example the web versions of ChatGPT, Claude, Gemini or
Copilot). The kit still works: the person keeps the files, and you work from
what they paste or upload.

## Setting up

Best: a **project** (Claude Projects, ChatGPT Projects or a custom GPT, Gemini
Gems, or similar). Ask the person to:

1. Create a project called "Job search".
2. Paste the contents of `AGENTS.md` into the project's instructions (or upload
   it), and upload the `docs/` files and `templates/` as project knowledge.
   Shortcut: upload `prompts/chat_kickoff.md` and the whole `docs/` folder.
3. Start a chat in the project and say "set me up".

Without projects, paste [`../prompts/chat_kickoff.md`](../prompts/chat_kickoff.md)
at the start of a chat and attach the docs it asks for.

## How state is kept

Because you can't save files:

- At the end of onboarding, output each workspace file (`profile.md`,
  `preferences.json`, `fact_bank.md`, `voice.md`, `sources.md`) in its own code
  block with the filename above it, and ask the person to save them (or to add
  them to the project's knowledge, replacing older versions).
- Keep `tracker.csv` as a CSV code block they paste into a spreadsheet, or ask
  them to keep the tracker in Google Sheets or Excel and paste the open rows at
  the start of each session.
- At the end of every session, output a short `log.md` entry for them to add, and
  any changed rows in full.
- At the start of every session, ask for the latest `profile.md`, the open rows
  of the tracker and the last log entry, if they are not already in the project.

## What changes

- Run Scout with your browsing tool. If you can't browse, ask the person to run
  searches from [`03_SOURCES.md`](03_SOURCES.md) and paste results.
- Skip the Python tools. Produce Markdown tables instead of the dashboard, and
  write calendar events as an `.ics` code block the person saves as
  `deadlines.ics` (one `VEVENT` per deadline).
- Everything else (judging, CVs, letters, emails, LinkedIn notes) works the same.

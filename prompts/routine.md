# Routine prompt (for scheduled tasks)

A standalone prompt for a scheduled task or a terminal agent run every 2 to 3
days. Replace `<PATH>` with the folder that holds this repository.

---

Open the folder `<PATH>` (the grad-job-pipeline kit) and read `AGENTS.md`.
Then run the "Every few days" routine in `docs/09_ROUTINE.md` for the person
whose workspace is in `my-search/`:

1. Read `my-search/profile.md`, `preferences.json`, `sources.md`, the last three
   entries of `log.md`, and `tracker.csv`.
2. Run Scout in full mode (`docs/02_SCOUT.md`), judging every posting that passes
   the screen, and add results to `tracker.csv` with status `new`.
3. Re-check every open row with a deadline in the next 14 days.
4. List contacts in `contacts.csv` whose `next_date` is today or earlier.
5. If Python is available, run `python tools/pipeline.py dashboard` and
   `python tools/pipeline.py calendar`.
6. Add a dated entry at the top of `my-search/log.md`.
7. Reply in under 150 words: new strong and worth finds (with deadlines),
   anything closing within 14 days not yet applied to, follow-ups due, sources
   that failed. List the links you used.

Do not apply, send messages, or change `profile.md` or `preferences.json` in a
scheduled run. Never invent postings or dates.

---

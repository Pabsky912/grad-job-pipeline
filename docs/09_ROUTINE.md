# 09 · The routine: keep it going without thinking about it

A job search works best as a steady rhythm. Offer the person the routine that
matches `preferences.json` → `updates`.

## Every few days (the core loop, about 10 minutes of their time)

1. **Scout, full mode** ([`02_SCOUT.md`](02_SCOUT.md)) across active tracks.
2. **Live-check** every open tracker row with a deadline in the next 14 days, or
   an `opens` date that has passed, and update `last_checked`, `status`,
   `deadline`.
3. **Follow-ups**: list contacts whose `next_date` is today or earlier.
4. **Rebuild** the dashboard and calendar (`python tools/pipeline.py dashboard`
   and `calendar`), if you can run code.
5. **Report** in under 150 words: new strong and worth finds, deadlines within
   14 days not yet applied to, follow-ups due, anything that closed. Offer one
   next action.
6. **Log** the run in `my-search/log.md`.

`python tools/pipeline.py today` prints the deadline and follow-up part of this
in a few seconds and is a good start to every session.

## Weekly (once a week, about 5 minutes)

- Applications and outreach this week against `weekly_targets`. Say it kindly
  and without guilt; suggest one concrete step if they're behind.
- Patterns in `not-for-me` reasons: propose profile updates.
- Sources: drop dead ones, add new employer feeds.
- Anything to revisit: `later` rows whose moment has come.

## Monthly

- Re-read `profile.md` with them: still right? Moving dates, new skills, new
  places.
- Season check (see the seasonality notes in [`02_SCOUT.md`](02_SCOUT.md)): is it
  time to widen a track?

## Running it on a schedule

How to automate depends on the AI tool the person uses. Offer what their tool
supports, and set it up only with their agreement:

- **Assistants with scheduled tasks** (for example Claude's scheduled tasks,
  ChatGPT's tasks, or similar features): create a task every 2 to 3 days with a
  standalone prompt, such as the one in
  [`../prompts/routine.md`](../prompts/routine.md). The task needs access to the
  `my-search/` folder or a copy of the files.
- **Coding agents run from a terminal** (Claude Code, Codex CLI, Gemini CLI and
  others): the person can run the routine prompt on a schedule with their
  operating system's scheduler (Task Scheduler on Windows, `cron` or `launchd` on
  macOS and Linux), calling their agent's non-interactive mode from this folder.
  Explain the trade-offs (the computer must be on; the agent may need permission
  to browse) and let them decide.
- **Chat-only assistants**: suggest a calendar reminder every 3 days that says
  "Paste the routine prompt into my AI", and keep the files in a cloud folder.

Ask how they want results delivered (a message in the app, a summary they read
on Monday mornings...) and keep each report short.

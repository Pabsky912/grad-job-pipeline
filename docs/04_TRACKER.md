# 04 · Tracker, dashboard and calendar

One CSV file holds every opportunity on every track, so it opens in Excel,
Google Sheets or Numbers, and any agent can read and edit it.

## `my-search/tracker.csv`

| Column | Meaning |
|---|---|
| `id` | Unique, stable id (see [`02_SCOUT.md`](02_SCOUT.md)) |
| `track` | A track id from `preferences.json` (`research-assistant`, `masters`...) |
| `org` | Organisation |
| `role` | Job title or programme name |
| `location` | City, country |
| `remote` | `yes`, `hybrid`, `no` or empty |
| `link` | The posting itself, not a search page |
| `source` | Where it was found (`jobs.ac.uk`, `greenhouse`, `pasted`, `own find`...) |
| `found_on` | Date added, `YYYY-MM-DD` |
| `opens` | Date applications open, if not yet open |
| `deadline` | Closing date `YYYY-MM-DD`; empty if rolling or not stated |
| `deadline_note` | `rolling`, `not stated`, `closes early if enough applicants`, time zone... |
| `start` | Start date or season as the posting says |
| `salary` | As stated, or empty |
| `verdict` | `strong`, `worth`, `stretch`, `skip` |
| `score` | 1 to 5 |
| `summary` | One sentence |
| `why` | Reasons it fits, separated by ` ; ` |
| `watch_out` | Catches, separated by ` ; ` |
| `status` | See below |
| `applied_on` | Date applied |
| `next_step` | The very next action ("ask about June start", "prepare for interview") |
| `next_date` | When that action is due |
| `last_checked` | Last date someone confirmed the posting was still open |
| `notes` | Anything else |

Dates are always ISO (`2027-01-15`). Keep commas inside fields quoted (any CSV
library does this; when editing by hand, wrap the field in double quotes).

### Status values

`new` → found, not yet reviewed by the person
`shortlist` · `this-week` · `later` → the person's own lists
`drafting` → working on the application
`applied` · `interview` · `offer` · `rejected` → the outcome trail
`not-for-me` → dismissed (write the reason in `notes`; it teaches Scout)
`gone` → the posting closed or vanished

When the person tells you anything ("applied to Acme yesterday", "got an
interview!", "the Novo one isn't for me, too commercial"), update the row,
set `next_step` and `next_date` where useful, and, for a `not-for-me`, consider
whether the reason should become a dislike (see
[`01_ONBOARDING.md`](01_ONBOARDING.md), *Updating the profile*).

### Keeping it honest

- Before a deadline within 14 days, re-open the link and set `last_checked`. If
  it is gone, set `status` to `gone`.
- Never delete rows; status carries the history. Hide them in views instead.
- If the person already had a spreadsheet, import it: map their columns to these,
  keep their extra columns in `notes`, and tell them what you could not map.

## `my-search/contacts.csv`

For people: professors, researchers, alumni, recruiters, team members.

| Column | Meaning |
|---|---|
| `id` | Slug of name and organisation |
| `name`, `title`, `org` | Who they are |
| `channel` | `email` or `linkedin` |
| `contact_type` | `professor`, `researcher`, `alumni`, `recruiter`, `team-member`, `other` |
| `why` | Why them, in one line, and which tracker row it links to |
| `url` | Their public profile or staff page |
| `email` | Only from an official page; leave empty otherwise |
| `email_verified` | `yes` if copied from an official page, `no` if guessed (never send to `no`) |
| `linked_id` | `id` of the related tracker row, if any |
| `template` | Template used (see [`07_LINKEDIN.md`](07_LINKEDIN.md)) |
| `message` | The exact text sent |
| `status` | `to-send`, `sent`, `accepted`, `replied`, `meeting`, `no-reply`, `declined`, `closed` |
| `sent_on`, `accepted_on`, `follow_up_on` | Dates |
| `follow_up_stage` | `0`, `1` or `2` follow-ups sent |
| `reply` | What they said, briefly |
| `next_step`, `next_date` | The next action and when |
| `notes` | Anything else |

## Dashboard

`python tools/pipeline.py dashboard` builds `my-search/dashboard.html`: a single,
offline page that opens in any browser. It shows:

- tiles: strong finds, closing within 14 days, applications in progress,
  follow-ups due;
- **Scout**: new postings with verdict, score, why and watch-outs, filterable
  by verdict and track, with buttons to save to Shortlist, This week or Later,
  or dismiss with a reason;
- **Pipeline** by track, sorted by deadline, with a status menu on every row;
- **Deadlines**: everything with a date in the next 60 days;
- **Outreach**: contacts with follow-ups due, and a copy button for messages;
- **Profile**: the five-line summary, so the person can check what Scout is
  using.

Changes made on the page are saved in that browser. The **Export changes**
button downloads a small CSV; give it to the agent or run
`python tools/pipeline.py import-changes <file>` to write the changes into
`tracker.csv` and `contacts.csv`. Rebuild the dashboard after every Scout run
or tracker change.

If you cannot run Python, you can still produce a simple view: a Markdown table
of open rows sorted by deadline.

## Calendar

`python tools/pipeline.py calendar` writes `my-search/deadlines.ics` with:

- each `deadline` (all-day event, with reminders 7 days and 1 day before);
- each `opens` date for postings not yet open;
- each `next_date` in tracker and contacts, as a to-do style reminder.

Rows with status `not-for-me`, `gone`, `rejected` or `offer` are left out. The
person imports the file into Google Calendar (Settings → Import), Outlook (File →
Open & Export → Import) or Apple Calendar (File → Import). Each event has a
stable id, so importing an updated file again updates events instead of
duplicating them in most calendar apps.

## Excel

`python tools/pipeline.py xlsx` (needs `pip install openpyxl`) writes
`my-search/tracker.xlsx` with two sheets, filters, frozen headers, clickable
links and a "Days left" column. `tracker.csv` stays the master copy: edit the
CSV (or use the dashboard), not the export.

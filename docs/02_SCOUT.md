# 02 · Scout: find and judge postings

Scout is the search engine of the kit. It does what paid "job board for your
agent" services do (count, screen, pull, judge with reasons, save to lists),
using only public pages, official job-board APIs and your own reading.

Before a run, read `my-search/preferences.json`, `my-search/sources.md` and the
rows already in `my-search/tracker.csv` (so you don't add duplicates).

## Modes

- **Quick mode** (onboarding, or "anything new today?"): 2 to 4 sources, the top
  one or two tracks, stop after about 10 good candidates. 5 to 10 minutes.
- **Full mode** ("run Scout", the routine): every working source in
  `sources.md` for every active track, plus a few web searches. Judge
  everything that passes the screen.
- **Single posting** ("is this one for me?" plus a link): skip to *Judge*.
- **Pasted list** (from another tool, a newsletter, a friend): parse each line
  into organisation, role, place, deadline and link, open each link to confirm
  it is still live, then screen and judge as normal. Set `source` to where the
  list came from.

## The four stages

### 1. Count (cheap)

Read search-result pages and board listings, not full postings. For each
source, build the query from the track's `keywords` and `titles`, narrowed by
place where the source allows it. Note how many results each query returns. If
a query returns hundreds of mostly irrelevant results, tighten it (add a field
word, a place, "graduate" or "entry level") rather than wading through them; if
it returns nothing, loosen it once. Record per source: `ok`, `blocked`, or
`empty`.

For company boards on Greenhouse, Lever, Ashby, Workable or Recruitee, use the
JSON API (see [`03_SOURCES.md`](03_SOURCES.md)), or run
`python tools/pipeline.py fetch <ats> <slug> --q "keyword1,keyword2"` if you can
run code.

### 2. Screen (hard filters, from the listing alone)

Drop a result without opening it when the listing already shows that it:

- is senior, lead, manager, principal, or asks for years of experience they
  don't have;
- needs a qualification they won't have by the start date (PhD, completed
  Master's, professional registration);
- is only for students in a year they are not in (for example
  "penultimate-year students only");
- is in a place listed under `locations.never`, or outside every acceptable
  place, and is not remote;
- requires a language they don't work in;
- matches anything in `preferences.json` `ruleouts`;
- is already in `tracker.csv` (same id, or same organisation and role).

Keep borderline cases for the judge stage: if in doubt, open it.

### 3. Pull (open the full posting)

Open every posting that passed the screen. You cannot judge from a title.
Extract: title, organisation, place, remote or not, salary if stated, start date,
contract length, closing date (or "rolling", or "not stated"), when applications
open if not yet open, eligibility requirements, the three or four duties that
best describe the job, and the link. If the page is a dead end (expired, 404,
"no longer accepting applications"), drop it.

### 4. Judge

Score each posting from 1 to 5 using the person's weights (default:
interest 0.5, skills 0.25, eligibility 0.15, logistics 0.1):

- **Interest**: how close it is to their top tracks, likes and favourite
  organisations, and how far from their dislikes. A priority-1 track with two
  "likes" in the duties is a 5; a track they ranked last is a 2 to 3.
- **Skills**: how much of what the posting asks for appears in
  `fact_bank.md`. Count the essential criteria they clearly meet.
- **Eligibility**: degree level, timing, right to work, language. A clear
  blocker caps the score at 2.
- **Logistics**: place, start date, salary floor, contract length.

Then give a **verdict**:

| Verdict | Meaning |
|---|---|
| `strong` | Score 4 to 5, eligible, timing works. Apply. |
| `worth` | Score about 4 with one fixable issue (start date to ask about, a skill to evidence). Worth a look. |
| `stretch` | Score 3, real gaps, but interesting. Apply only if the pipeline is thin. |
| `skip` | Fails a hard rule. Keep only if it teaches something (for example, a role to revisit next year). |

Write for each judged posting:

- `summary`: one sentence on what the job is, in plain words.
- `why`: two or three short reasons it fits, each tied to something specific in
  their profile or fact bank ("you've done cryostat sectioning, which is in the
  essential criteria").
- `watch_out`: the honest catches ("closes in 6 days", "asks for a driving
  licence", "start date is March, before you graduate: ask if June works").

Quote the posting for requirements and dates. **Never guess a deadline.** If
none is stated, write "not stated" and set `deadline` empty.

## Save the results

Add each judged posting to `my-search/tracker.csv` (see
[`04_TRACKER.md`](04_TRACKER.md) for the columns), with `status` = `new`,
`found_on` = today, `source` = the board name, and an `id` made from a short
source prefix and the posting's own id where it has one (`gh-acme-4012345`,
`lever-acme-9f2c`, `jobsacuk-DTC631`). Without a posting id, use a slug of
organisation and role (`acme-research-assistant`). Postings judged `skip` go in
with `status` = `not-for-me` only if they are worth remembering.

If you can run code, `python tools/pipeline.py add --json '{...}'` handles ids
and dedupe; then `python tools/pipeline.py dashboard` refreshes the dashboard.

Update `my-search/sources.md`: mark sources that were blocked or empty, and add
any new employer board you discovered that works.

## Report back (keep it short)

In under about 150 words:

1. New `strong` and `worth` finds: title, organisation, deadline, one reason.
2. Anything closing within 14 days that they haven't applied to.
3. Sources that failed and need a manual check.
4. One suggested next action ("Want me to tailor your CV for the Acme role?").

End with a list of the links you used. Then write the session to `log.md`.

## Seasonality (useful defaults; check for the person's field and country)

- Large graduate schemes (pharma, consulting, banking, big tech, civil service)
  usually open in late summer or autumn for starts the following summer or
  autumn, and many close by December or January. Search these early.
- Research assistant, technician and many small-company roles usually start
  within weeks of being advertised, so a role advertised in October rarely waits
  until June. Before the final term, focus these searches on roles that are
  part-time, remote, or explicitly flexible on start; widen them in the last
  three to four months before the person can start.
- PhD and Master's calls, and their scholarships, often close between November
  and March for the following autumn. See [`08_STUDY_AND_FUNDING.md`](08_STUDY_AND_FUNDING.md).

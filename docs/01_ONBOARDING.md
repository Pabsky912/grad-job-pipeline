# 01 · Onboarding: get to know the person

Goal: in about 20 to 30 minutes of conversation, produce five files that every
other part of the kit relies on:

- `my-search/profile.md`: who they are and what they want, in plain language
- `my-search/preferences.json`: the same, machine-readable, with weights
- `my-search/fact_bank.md`: verified facts from their CV, quoted, nothing added
- `my-search/voice.md`: how they write
- `my-search/sources.md`: the boards and employer pages worth checking for them

The person can stop at any point. Save what you have after every round so
nothing is lost, and pick up from the first missing piece next time.

## How to host this conversation

- Be warm and brief. Ask **at most three or four questions per message**, and
  number them so they can answer quickly ("1. yes 2. London or remote 3. ...").
- **Infer before you ask.** If the CV already says they graduate in June 2027,
  don't ask when they graduate; confirm it in passing.
- Offer options when people are stuck ("For example: lab research, data,
  consulting, policy, product, teaching..."), but never push them toward one.
- Reflect back what you heard in one or two lines at the end of each round so
  they can correct you.
- Accept "I don't know" as an answer. Mark it as an open question in the
  profile; the taste calibration in Step 5 often answers it.

## Step 0 · Say what this is (one message, no questions yet)

Tell them, in your own words:

1. This is a free job-search kit. You'll interview them for a few minutes, read
   their CV, then search real job boards and judge each posting against what
   they told you, with reasons.
2. Their details are kept in a private folder on their computer (`my-search/`)
   that is never uploaded to GitHub.
3. They are in charge: you draft emails, CVs and messages, they send them.
4. They can stop at any time and continue later.

Then set up the workspace: run `python tools/pipeline.py init`. If you cannot run
code, create `my-search/` and copy every file from `templates/` into it, dropping
the `.template` from each name.

## Step 1 · Their materials

Ask for:

1. Their CV or résumé (a file, a link to a PDF, or pasted text). More than one
   version is welcome; older or tailored versions often hold extra facts.
2. Optional: LinkedIn "About" text, a transcript, a personal website, a cover
   letter they were happy with, or any email they wrote that sounded like them.

Then build `my-search/fact_bank.md` from `templates/fact_bank.template.md`:

- Copy every education entry, role, project, skill, language, award, grade and
  number **exactly as their documents state it**. Keep their own sentences
  verbatim where they are good; these are what CVs will reuse.
- Note the source file next to each fact.
- List conflicts (two different dates for the same role) and gaps (a role with
  no dates) under *To confirm*, and ask about them in Step 2.
- Do not add skills they "probably have". If they mention something in
  conversation that is not on the CV, add it marked `(said in onboarding,
  date)` so it is clear where it came from.

## Step 2 · Direction (what they want)

Ask, adapting to what the CV already shows:

1. What kinds of work are you looking for? List as many as feel right, and put
   them in order if you can. (Offer examples relevant to their degree: research
   or lab roles, graduate schemes, data or analytics, consulting, engineering,
   policy, product, teaching, start-ups, further study...)
2. Is there a field, problem or industry you'd most love to work on? Any
   organisations you'd be thrilled to join?
3. Of everything you've done (courses, projects, jobs, volunteering), what did
   you enjoy most, and what exactly about it? And what drained you?
4. Are you also considering a Master's or PhD, or a gap year or volunteering
   placement? (If yes, note it; [`08_STUDY_AND_FUNDING.md`](08_STUDY_AND_FUNDING.md) covers it.)

Turn their answers into **tracks**: named lines of search, each with a priority
(1 = most wanted). Examples: `research-assistant`, `grad-scheme-pharma`,
`data-health`, `consulting`, `masters`. A track has a short description,
keywords for searching, and the job titles that count.

## Step 3 · Constraints (what rules things in or out)

1. When can you start full-time? Are you finishing a degree first, and when
   exactly? Would you take something part-time or remote before then?
2. Where would you work? Cities or countries, in order. Remote OK? Would you
   relocate, and is anywhere a firm no?
3. Right to work: which countries can you work in without sponsorship, and what
   visa route (if any) would you be on? (Ask plainly and without judgement; it
   decides eligibility for many roles.)
4. Languages you can work in, and at what level.
5. Anything else that rules a job out: minimum salary, contract length, travel,
   shift work, sectors you won't work in (for example tobacco, defence,
   gambling), unpaid roles, roles needing a driving licence...

Record hard limits as **rule-outs** (the job is skipped) and softer ones as
**watch-outs** (the job is kept but flagged).

## Step 4 · How they like to work the search

1. How many applications a week feels realistic: 2, 5, 10 or more?
2. Are you comfortable with cold outreach (emailing professors or teams that
   haven't advertised, LinkedIn connection notes)? Roughly how many a week?
3. How do you want updates: a short summary every few days, a daily digest, or
   only when you ask? (Used by [`09_ROUTINE.md`](09_ROUTINE.md).)
4. Do you keep a spreadsheet already? If so, share it and I'll import it into
   `tracker.csv` rather than starting from scratch.

## Step 5 · Taste calibration (understand their likes)

People often can't say what they want in the abstract, but they react
immediately to real postings. Use that.

1. Run a **quick** Scout pass ([`02_SCOUT.md`](02_SCOUT.md), *Quick mode*) across
   their top two or three tracks and pick **8 to 10 real, open postings** that
   deliberately vary: different tracks, sizes of employer, places, seniority
   within entry level, research vs industry.
2. Show them as a numbered list, one line each: title, organisation, place, one
   phrase on what the job is, and the link.
3. Ask them to react quickly to each with **yes / maybe / no** plus a few words
   on why ("no: too sales-y", "yes: the imaging work", "maybe: love it but
   Leeds is far").
4. From the reactions, write down **likes** (themes that drew a yes), **dislikes**
   (themes behind the nos) and any new rule-outs. Ask one follow-up about any
   surprise ("You said yes to the policy role though it wasn't on your list:
   should policy be a track?").
5. Adjust track priorities and `preferences.json` weights. If the sample was
   mostly "no", say so, adjust, and run one more short round.

Add any posting they said yes to straight into `tracker.csv` (status
`shortlist`), so the calibration already produces something useful.

## Step 6 · Voice

If they shared something they wrote (an email, a cover letter, a personal
statement), study it and fill `my-search/voice.md` from
`templates/voice.template.md`: sentence length, formality, contractions or not,
British or American spelling, phrases they use, phrases to avoid. If they shared
nothing, ask: "Paste a short email you've sent that sounded like you, or tell me
three words that describe how you'd like to come across." Defaults when nothing
is known: plain, specific, friendly, no clichés, spelling from their country.

## Step 7 · Write the files and confirm

1. Fill `my-search/profile.md` from `templates/profile.template.md`. Keep it under
   about 120 lines and in plain language. Remove every `TODO`.
2. Fill `my-search/preferences.json` (format below).
3. Start `my-search/sources.md` from `templates/sources.template.md`, keeping the
   sections relevant to their tracks and places from
   [`03_SOURCES.md`](03_SOURCES.md), and adding career pages of any organisation
   they named.
4. Show a **five-line summary** ("You're looking for...; top places...; you can
   start...; hard no's...; I'll check these sources...") and ask them to correct
   anything.
5. Write the first entry in `my-search/log.md`.
6. Offer the next steps in one short list: run the first full Scout search, build
   the dashboard, set up a routine, tailor a CV for one of their "yes" postings.

## `preferences.json` format

```json
{
  "updated": "2026-10-04",
  "name": "Jordan",
  "spelling": "british",
  "start_from": "2027-07-01",
  "graduation": "2027-06-20",
  "part_time_before_start": true,
  "tracks": [
    {
      "id": "research-assistant",
      "label": "Research assistant (neuro and cell biology)",
      "priority": 1,
      "keywords": ["research assistant", "research technician", "lab technician"],
      "titles": ["Research Assistant", "Research Technician", "Junior Research Associate"],
      "fields": ["neuroscience", "cell biology", "imaging"]
    }
  ],
  "locations": {
    "preferred": ["London", "Cambridge", "Northbridge"],
    "acceptable": ["United Kingdom"],
    "remote_ok": true,
    "relocate": true,
    "never": []
  },
  "work_rights": "UK citizen",
  "languages": ["English (native)", "French (B1)"],
  "salary_min": null,
  "likes": ["microscopy and image analysis", "turning messy data into clear charts"],
  "dislikes": ["sales or business development targets", "pure data entry"],
  "ruleouts": ["requires a PhD", "requires a completed Master's", "penultimate-year students only"],
  "watchouts": ["fixed-term under 12 months", "animal work"],
  "weekly_targets": {"applications": 5, "outreach": 8},
  "updates": "every 3 days",
  "weights": {"interest": 0.5, "skills": 0.25, "eligibility": 0.15, "logistics": 0.1}
}
```

This is the fictional example in `examples/sample-candidate/` (shortened). `priority` 1 is the most wanted track. `weights` must add up to 1; leave the
defaults unless the person says, for example, that location matters more than
anything.

## Updating the profile

People change their minds, and every "no" teaches something. Whenever the
person says something that changes what they want ("no more consulting",
"actually I'd love Copenhagen", "I passed my driving test"):

1. Update `profile.md` and `preferences.json` (and `fact_bank.md` for new facts).
2. Add a dated line under *Change history* at the bottom of `profile.md`.
3. Say in one sentence what you changed and what it means for the next search.
4. If the change removes a track or adds a rule-out, offer to mark matching
   tracker rows `not-for-me`.

When the person dismisses a posting with a reason, check whether the reason
generalises. If it has come up twice, propose adding it as a dislike or rule-out.

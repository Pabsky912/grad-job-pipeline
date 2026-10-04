# 07 · LinkedIn outreach (manual, assisted)

You help the person decide **who** to contact, **what** to say and **when** to
follow up. The person does every click on LinkedIn themselves.

> **No automation.** Do not auto-connect, auto-message, auto-fill the note box,
> scrape profiles or search results, or drive LinkedIn with a browser tool.
> LinkedIn's User Agreement prohibits bots and automated access, and accounts get
> restricted for it. The kit only queues, drafts, copies and logs.

## Who to contact

For each employer or lab in the tracker with status `shortlist`, `this-week`,
`drafting` or `applied`, suggest up to three people, in this order:

1. **Alumni** of the person's university who work there (the person finds them
   with LinkedIn's alumni tool: their university's page → Alumni → filter by
   company). Warmest audience by far.
2. **Someone doing the job** they want, or did it one or two years ago (recent
   graduates on the same scheme, research assistants or PhD students in the lab).
3. **The recruiter** for early careers, or the hiring manager if named in the
   posting.

You can name people only from public pages you opened (a lab's team page, a
company's "meet the team" page, a conference programme). Otherwise give the
person a search recipe ("search: `<Company> graduate programme`, filter People,
Current company: <Company>, School: <their university>") and let them pick.

Add each person to `contacts.csv` with `channel` = `linkedin`, `status` =
`to-send`, `why` and `linked_id`.

## Connection notes (200 characters or fewer)

Free LinkedIn accounts have a monthly limit on personalised notes; paid ones
allow more. Keep every note within 200 characters, count them, and record the
count. One clear reason for connecting, one small, easy ask or none.

Templates to adapt (replace the brackets; never send a template unfilled):

| ID | For | Template |
|---|---|---|
| N1 | Alumni | Hi [Name], fellow [University] [subject] grad (finishing [year]) here. I'm applying to [Company]'s [programme] and would love to hear how you found it. Thanks! |
| N2 | Someone in the role | Hi [Name], I'm a final-year [subject] student at [University] and your path into [team/role] is close to what I'm aiming for. Would be glad to connect. |
| N3 | Researcher / lab member | Hi [Name], I enjoyed your [year] [journal] paper on [topic]. I'm a [subject] student at [University] hoping to work in [field], would be great to connect. |
| N4 | Recruiter | Hi [Name], I've applied for [role] ([ref]) at [Company] and am really keen on the [specific aspect]. Happy to share anything useful. Thank you! |
| N5 | After an event | Hi [Name], thanks for your talk at [event] on [topic]. The point about [detail] stuck with me. I'd be glad to stay in touch. |
| N6 | No note (when out of notes) | Connect without a note, then send M1 once accepted. |

## Follow-up messages (after they accept)

| ID | When | Template |
|---|---|---|
| M1 | Within a few days of accepting | Thanks for connecting, [Name]! If you ever had 15 minutes, I'd really value hearing how you got into [role/team] and what you'd do differently as a graduate now. Completely fine if not. |
| M2 | After a call or reply | Thank you so much for your time today. [One specific thing they said] was really useful, and I'll [action]. I'll let you know how it goes. |
| M3 | One gentle nudge, about 2 weeks after M1 with no reply | Hi [Name], just floating this up in case it got buried. No worries at all if you're busy! |

Never more than one nudge. Never ask a stranger for a referral in the first
message; that comes, if at all, after a real conversation.

## The daily queue

When asked "who should I contact today?":

1. Count how many notes the person has sent this week and their weekly target
   (`preferences.json` → `weekly_targets.outreach`).
2. List today's batch (default 5 to 8): name, organisation, why, the filled
   note with its character count, and the profile link or search recipe.
3. List follow-ups due: accepted with no M1 yet; M1 sent over 14 days ago with
   no reply (offer M3); replies that need an answer.
4. After the person says what they sent, update `contacts.csv`: `status`,
   `sent_on`, `message`, `follow_up_stage`, `next_date`.

The dashboard's Outreach section shows the same queue with copy buttons.

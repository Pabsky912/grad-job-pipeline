# 06 · Cold outreach emails

For writing to people who haven't advertised anything (yet): a professor whose
lab might take a research assistant, a team lead at a start-up, an alumna at a
company, a programme director. Done well, this is one of the most effective
things an early-career person can do. Done as a mail merge, it is spam.

## Before writing

1. **Find the right person.** The PI or group leader for a lab; the hiring
   manager or team lead for a company role; a programme coordinator for study
   questions. Use their official staff or lab page.
2. **Confirm the email address on an official page.** If you can only guess it
   from a pattern, record it in `contacts.csv` with `email_verified` = `no` and
   tell the person: never send to a guessed address without a second check.
3. **Check they are still there.** People move. Make sure the affiliation you
   name is current.
4. **Read their work.** For researchers: one foundational paper and one recent
   (last one or two years), and what connects them. For companies: a recent
   product, project, blog post or talk by that team. Note the specific finding or
   decision that genuinely connects to the person's interests.
5. Check `contacts.csv`: has the person written to them before?

## Structure (four short paragraphs, 200 to 350 words)

1. **Who they are and the ask.** Name, year and degree, university, and what
   they're asking for (a research assistant role, a summer placement, a short
   call, advice on a programme) and from when. One or two sentences.
2. **Why this person, specifically.** The paragraph that proves they did the
   reading. Name the paper (journal and year) or the project, say what was
   interesting about it in their own words, ideally the connection between the
   older and newer work. **Unique per recipient. Never reused.**
3. **What they'd bring.** Two or three facts from `fact_bank.md` that overlap
   most with the recipient's methods or questions. Specific, not a list of
   adjectives.
4. **The ask, and an easy way to say yes.** Acknowledge that positions are
   often advertised close to the start date; ask whether there might be an
   opening, or who else they'd suggest; offer CV, transcript and references;
   offer flexibility on timing.

Sign-off: "Best wishes," (or the person's usual sign-off from `voice.md`), full
name, degree, university, email, phone if they want it included.

**Subject line:** specific and short, for example
"Research assistant enquiry: sleep and memory consolidation (graduating June 2027)".

## Voice rules (defaults; `voice.md` overrides)

- Contractions are fine ("I'm", "I'd"): it reads as a person, not a form.
- Vary openings. Not every paragraph starts with "I am very interested in".
  Rotate: "What caught my attention was...", "I've been struck by...",
  "Your 2024 paper on X showed...".
- Specific beats vague: "your 2024 *Cerebral Cortex* paper showing X" beats
  "your recent work in this area".
- Don't oversell. Let the specificity of paragraph 2 persuade.
- Use the spelling convention in `voice.md` throughout.

## Batches without a mail-merge feel

When writing to several people in one sitting:

- Paragraph 2 is always written from scratch.
- Paragraphs 1, 3 and 4 can share a structure, but keep 3 or 4 phrasings of each
  and rotate them so consecutive emails don't open with the same sentence.
- Space sending out (the person sends; suggest a few a day, not 30 at once).

## Before handing it over

- Re-read paragraph 2: if it could go to another recipient unchanged, rewrite it.
- Check every fact against the fact bank, and every paper title and year against
  the source you opened.
- Flag unverified addresses.
- Save the draft as `my-search/emails/<date>_<surname>.md`, add or update the row
  in `contacts.csv` (`status` = `to-send`), and give the person the text to paste.
  Never send it yourself.

## Follow-ups

If no reply after about 10 to 14 days, one short, polite follow-up in the same
thread (two or three sentences: a gentle nudge, perhaps one new relevant detail).
After a second silence, close it (`status` = `no-reply`) and move on. Never more
than two follow-ups.

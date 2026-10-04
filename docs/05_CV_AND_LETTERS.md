# 05 · Tailored CVs and cover letters

A tailored CV is the same true facts, chosen and ordered for one reader. Never
a new set of facts.

## Non-negotiables

1. **Every fact comes from `my-search/fact_bank.md`.** Grades, dates, durations,
   counts, tools, outcomes. If the posting wants something the person has no
   evidence for, leave it out. Do not round up, stretch dates or upgrade
   "helped with" into "led".
2. **Reuse their own sentences.** Where the fact bank holds a good sentence in
   their words, keep its factual part verbatim and only adjust the short
   relevance clause at the end. The CV should still sound like them.
3. **Reframe, don't rewrite.** You may change which entries appear, their order,
   the bold lead-in labels and the closing relevance clause of a bullet. You may
   not change the fact inside the bullet.
4. **Lead with real numbers.** If a bullet has a verified number, put it early
   ("37/45 points: ...", "3 strains analysed..."). Never add a number to make a
   bullet look better.
5. **One page** for undergraduates and recent graduates unless the posting or
   the country's convention says otherwise (academic CVs in some countries, US
   federal résumés). Check the page count after rendering.
6. **Plain wording.** No slashes jamming two things together ("R and Python",
   not "R/Python"), no buzzword lists, no "results-driven".

## Procedure

1. **Read the target.** Open the posting (or the lab's page, or the programme).
   Note the field, the essential and desirable criteria, the methods or tools
   named, and the tone. Note any eligibility mismatch once, plainly, then carry
   on unless the person says stop.
2. **Map criteria to evidence.** Make a short table for yourself: each essential
   criterion → the fact-bank entries that evidence it, or "none". Share the
   "none" lines with the person: they may know something that isn't in the fact
   bank yet (add it, marked with today's date, if they confirm it).
3. **Select.** Education always. Then the 4 to 8 most relevant experience
   entries, most relevant first. Pick one register: research CVs and business
   CVs rarely mix well on one page; leadership and volunteering fit either.
4. **Reframe.** For each chosen bullet keep the factual clause and adjust only
   the relevance clause. Example of the same fact framed for three readers:
   - behaviour lab: "...built an unsupervised-learning pipeline on focal-sampling
     data, the same approach as quantifying naturalistic social behaviour."
   - data role: "...built an unsupervised-learning pipeline on focal-sampling
     data, finding structure in a large, messy dataset."
   - regulatory role: "...built an unsupervised-learning pipeline on
     focal-sampling data, the same pattern-detection approach used on safety
     datasets."
   If there is no honest connection, add no clause at all.
5. **Render.** Write the content as JSON in the format of
   [`../examples/sample-candidate/cv.json`](../examples/sample-candidate/cv.json), then run
   `python tools/pipeline.py cv my-search/cv/<target>.json`. It writes a
   one-page HTML CV next to the JSON; open it in a browser and print to PDF
   (A4 or Letter, margins "none", headers and footers off). For a Word file,
   `tools/cv_docx.js` renders the same JSON (`npm install docx`, then
   `node tools/cv_docx.js my-search/cv/<target>.json`).
   No code? Write the CV in Markdown with the same order and headings and let the
   person paste it into their own template.
6. **Check.** One page; nothing invented (compare each line with the fact bank);
   no orphan lines; dates aligned; their name and contact details correct.
7. **Save** as `my-search/cv/CV_<Org>_<Role>.<ext>` and add the path to the
   tracker row's `notes`. Tell the person in one or two sentences what you
   emphasised and why.

## Cover letters and motivation statements

Same fact rules. Structure that works for most entry-level roles (250 to 400
words, or the length the posting asks for):

1. **Opening (2 sentences):** who they are (degree, university, when they
   finish) and exactly what they're applying for.
2. **Why this organisation and this role (the paragraph that must be unique):**
   something specific: a product, a programme, a paper, a project, a value they
   act on, and the link between that and what the person wants to do. If it
   could be sent to another employer unchanged, it isn't specific enough.
3. **Evidence (1 to 2 paragraphs):** two or three essential criteria, each
   answered with a concrete fact-bank example: situation, what they did, what
   came of it.
4. **Close (2 sentences):** availability (start date, right to work if relevant),
   thanks. No "I am confident I would be an asset."

Follow `my-search/voice.md`. Save as `my-search/letters/Letter_<Org>_<Role>.md`
(or `.docx` if they need Word).

## Application form questions

For "Why do you want this role?" and competency questions with word limits:
draft in their voice from the fact bank, stay under the limit (count words or
characters exactly as the form does), and keep a copy in
`my-search/letters/` so answers can be reused and adapted later.

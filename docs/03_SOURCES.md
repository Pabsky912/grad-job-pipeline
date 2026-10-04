# 03 · Sources: where to look

A starting registry. Copy the relevant parts into the person's
`my-search/sources.md` during onboarding, then grow it: every time an employer
they care about appears, find its careers system and add it.

Status notes reflect what worked for automated reading in October 2026. Sites
change; trust what happens on the day and update `sources.md`.

## 1. Employer job boards with public JSON APIs (best: complete and structured)

Many companies post jobs through an applicant tracking system (ATS) with a
public, documented, read-only feed. Find the slug by opening the company's
careers page and looking at where the "Apply" links point.

| ATS | How to spot it | Feed |
|---|---|---|
| Greenhouse | links to `boards.greenhouse.io/<slug>` or `job-boards.greenhouse.io/<slug>` | `https://boards-api.greenhouse.io/v1/boards/<slug>/jobs?content=true` |
| Lever | links to `jobs.lever.co/<slug>` | `https://api.lever.co/v0/postings/<slug>?mode=json` |
| Ashby | links to `jobs.ashbyhq.com/<slug>` | `https://api.ashbyhq.com/posting-api/job-board/<slug>` |
| Workable | links to `apply.workable.com/<slug>` | `https://apply.workable.com/api/v1/widget/accounts/<slug>` |
| Recruitee | links to `<slug>.recruitee.com` | `https://<slug>.recruitee.com/api/offers/` |
| Personio | links to `<slug>.jobs.personio.de` | `https://<slug>.jobs.personio.de/xml` (XML) |

`python tools/pipeline.py fetch greenhouse <slug> --q "graduate,research"` reads
the first five of these and prints matching postings.

Workday, SuccessFactors, Taleo, iCIMS and SmartRecruiters are common at large
employers but are either script-heavy or disallow automated reading. List them
under "check by hand" with the direct search link.

## 2. Job boards by region (search pages)

Read the search-results page with your query in the URL, then open individual
postings. Use the person's track keywords.

**UK**
- jobs.ac.uk (universities, research institutes, research assistant and technician roles): `https://www.jobs.ac.uk/search/?keywords=<q>&sortOrder=1&pageSize=25` (add `&location=<city>`)
- Bright Network graduate deadlines by sector: `https://www.brightnetwork.co.uk/application-deadlines/`
- Prospects (graduate jobs, all sectors): `https://www.prospects.ac.uk/graduate-jobs`
- TARGETjobs: `https://targetjobs.co.uk/`
- Gradcracker (STEM and engineering): `https://www.gradcracker.com/`
- Civil Service Jobs: `https://www.civilservicejobs.service.gov.uk/`
- NHS Jobs: `https://www.jobs.nhs.uk/`
- Charity Job (non-profits): `https://www.charityjob.co.uk/`
- W4MP (parliamentary and policy): `https://w4mpjobs.org/`

**Europe**
- EURAXESS (research jobs across Europe): `https://euraxess.ec.europa.eu/jobs/search` (often blocks automated reading: check by hand)
- AcademicTransfer (Netherlands, academic): `https://www.academictransfer.com/en/jobs/?q=<q>`
- Varbi (Swedish universities, for example Karolinska `https://ki.varbi.com/en/`)
- EMBL, EMBO, CRG, Max Planck, Helmholtz, Pasteur and similar institutes: own vacancy pages (several are script-heavy or block bots: check by hand)
- EU Careers / EPSO traineeships: `https://eu-careers.europa.eu/`
- Country boards: StepStone (DE), InfoJobs (ES), Welcome to the Jungle (FR), Jobindex (DK), Finn (NO): check by hand if blocked

**United States**
- USAJOBS (federal, has an official API with a free key): `https://www.usajobs.gov/`
- HigherEdJobs (universities): `https://www.higheredjobs.com/`
- Science careers: `https://jobs.sciencecareers.org/`
- Idealist (non-profits): `https://www.idealist.org/`

**Worldwide / any field**
- Nature Careers (science): `https://www.nature.com/naturecareers/` (blocks bots: check by hand)
- Company careers pages of every organisation the person named
- Web search, for example: `"graduate programme" 2027 <field> <country>`,
  `"research assistant" <field> <city> site:ac.uk`, `<company> careers early careers 2027`

Sites that need a login (LinkedIn Jobs, Handshake, Indeed, Glassdoor, university
careers portals): do not log in or scrape them. Ask the person to run the search
themselves and paste the results, then process them as a pasted list (see
[`02_SCOUT.md`](02_SCOUT.md)). Job alerts by email from those sites can be
pasted in the same way.

## 3. Further study and funding

See [`08_STUDY_AND_FUNDING.md`](08_STUDY_AND_FUNDING.md).

## Keeping `sources.md` healthy

For each source keep one line: name, URL pattern, which tracks it serves,
status (`ok`, `blocked`, `empty`, `login`), and the date last checked. Remove
sources that were empty for three runs in a row for that person's tracks, and
add employers' ATS feeds as you find them.

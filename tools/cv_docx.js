/**
 * Render a one-page Word CV from the same JSON that `pipeline.py cv` uses.
 *
 *   npm install docx
 *   node tools/cv_docx.js my-search/cv/CV_Acme_ResearchAssistant.json [out.docx]
 *
 * Layout: right-aligned italic "Last updated", centred name and contact line,
 * bold section headings with a thin grey rule, bold title / right-aligned place,
 * italic subtitle / right-aligned dates, hollow "o" bullets, skills block,
 * small grey name signature. A4, tuned for 2 education + 6 to 8 experience
 * entries at 9.5pt. Convert to PDF and check it is one page before sending.
 *
 * JSON format: see examples/sample-candidate/cv.json. A bullet is either a
 * string or a list of [text, bold] pairs, e.g. [["Grades: ", true], ["First-class...", false]].
 */
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, TabStopType, ExternalHyperlink,
} = require("docx");

const inFile = process.argv[2];
if (!inFile) { console.error("Usage: node tools/cv_docx.js <cv.json> [out.docx]"); process.exit(1); }
const CV = JSON.parse(fs.readFileSync(inFile, "utf8"));
const outFile = process.argv[3] || inFile.replace(/\.json$/i, "") + ".docx";

const FONT = CV.font || "Garamond";
const PAGE_MARGIN = 500;            // DXA (~0.35in)
const BOTTOM_MARGIN = 320;          // DXA
const CONTENT_WIDTH = 11906 - PAGE_MARGIN * 2;
const RIGHT_COL_WIDTH = 2300;       // keeps date ranges on one line
const BODY_SIZE = CV.body_half_points || 19; // 9.5pt; never below 18 (9pt)

const HAIRLINE = { style: BorderStyle.SINGLE, size: 4, color: "999999" };
const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE };

const runsOf = (b) => (typeof b === "string" ? [[b, false]] : b);

function twoCol(left, right, bold, size) {
  const cell = (text, width, align) => new TableCell({
    width: { size: width, type: WidthType.DXA },
    margins: { top: 0, bottom: 0, left: 0, right: 0 },
    children: [new Paragraph({ alignment: align, spacing: { after: 0 },
      children: [new TextRun({ text: text || "", font: FONT, size, bold, italics: !bold })] })],
  });
  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA }, borders: noBorders,
    rows: [new TableRow({ children: [
      cell(left, CONTENT_WIDTH - RIGHT_COL_WIDTH, AlignmentType.LEFT),
      cell(right, RIGHT_COL_WIDTH, AlignmentType.RIGHT),
    ] })],
  });
}

function bullet(runs, size, after) {
  return new Paragraph({
    indent: { left: 260, hanging: 260 },
    spacing: { after, line: 240, lineRule: "auto" },
    tabStops: [{ type: TabStopType.LEFT, position: 260 }],
    children: [new TextRun({ text: "o\t", font: FONT, size }),
      ...runs.map(([text, bold]) => new TextRun({ text, font: FONT, size, bold: !!bold }))],
  });
}

function heading(text) {
  return new Paragraph({
    spacing: { before: 100, after: 30 },
    border: { bottom: { ...HAIRLINE, space: 4 } },
    children: [new TextRun({ text, font: FONT, size: 24, bold: true })],
  });
}

const children = [];
if (CV.last_updated) children.push(new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 120 },
  children: [new TextRun({ text: `Last updated ${CV.last_updated}`, font: FONT, size: 16, italics: true, color: "666666" })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
  children: [new TextRun({ text: CV.name || "", font: FONT, size: 36, bold: true })] }));

const c = CV.contact || {};
const contactRuns = [];
const plain = [c.location, c.email, c.phone].filter(Boolean).join("   •   ");
if (plain) contactRuns.push(new TextRun({ text: plain + (c.link ? "   •   " : ""), font: FONT, size: 18 }));
if (c.link) contactRuns.push(new ExternalHyperlink({ link: c.link,
  children: [new TextRun({ text: c.link_label || c.link, font: FONT, size: 18, style: "Hyperlink" })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: contactRuns }));

for (const sec of CV.sections || []) {
  children.push(heading(sec.heading || ""));
  for (const e of sec.entries || []) {
    children.push(twoCol(e.title, e.where, true, BODY_SIZE));
    if (e.subtitle || e.dates) children.push(twoCol(e.subtitle, e.dates, false, BODY_SIZE));
    const bs = e.bullets || [];
    bs.forEach((b, i) => children.push(bullet(runsOf(b), BODY_SIZE - 1, i === bs.length - 1 ? 120 : 20)));
  }
}
if ((CV.skills || []).length) {
  children.push(heading("Skills & Languages"));
  for (const [k, v] of CV.skills) children.push(new Paragraph({ spacing: { after: 20, line: 240, lineRule: "auto" },
    children: [new TextRun({ text: `${k}: `, font: FONT, size: BODY_SIZE - 1, bold: true }),
               new TextRun({ text: v, font: FONT, size: BODY_SIZE - 1 })] }));
}
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 40 },
  children: [new TextRun({ text: CV.name || "", font: FONT, size: 18, italics: true, color: "999999" })] }));

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: BODY_SIZE } } } },
  sections: [{ properties: { page: { size: { width: 11906, height: 16838 },
    margin: { top: PAGE_MARGIN, bottom: BOTTOM_MARGIN, left: PAGE_MARGIN, right: PAGE_MARGIN } } }, children }],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(outFile, buf); console.log("Wrote " + path.resolve(outFile)); });

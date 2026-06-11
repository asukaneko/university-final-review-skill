# DOCX Style Guide

Use this guide when the user asks to export the review material as a Word / DOCX document or says that the document should look polished, printable, or similar to a well-formatted study handout.

## Visual style goal

The document should look like a clean university review handout:

- White page background with generous margins.
- Deep blue as the primary academic accent color.
- Light blue section highlights for chapter summaries and main-thread notes.
- Pale yellow boxes for notices, cautions, and exam reminders.
- Pale red boxes for mistake-prone points.
- Dark blue table headers with white text.
- Light gray code / formula blocks.
- Clear page headers and footers.
- Compact but readable spacing for mobile and printed reading.

## Recommended color tokens

| Token | Use | Suggested value |
| --- | --- | --- |
| Primary blue | Main title, section heading, table header | `#1F5D8C` |
| Heading navy | Body headings | `#1E3A56` |
| Light blue fill | Chapter main thread / key idea box | `#EAF3FB` |
| Light yellow fill | Notice / reminder box | `#FFF6D9` |
| Light red fill | Mistake-prone point box | `#FDEBEC` |
| Light gray fill | Formula / code / example block | `#F4F6F8` |
| Border gray | Table borders and separators | `#D8DEE6` |

## Page layout

Recommended page settings:

- Paper size: A4.
- Margins: 2.0 cm left and right, 1.8-2.2 cm top and bottom.
- Body font: a readable CJK-compatible sans-serif for Chinese, or Calibri / Aptos for English.
- Body size: 10.5-11 pt.
- Line spacing: 1.15-1.25.
- Paragraph spacing: 4-6 pt after normal paragraphs.

## Cover / first page structure

Use a clear first page:

1. Small breadcrumb line, for example: `Course name | Chapter N | Topic`.
2. Main course title.
3. Chapter title.
4. Subtitle such as `Detailed Review Notes and Exam Focus`.
5. A highlighted main-thread box.
6. Learning objectives.
7. Table of contents.

## Section hierarchy

Recommended heading style:

- Title: centered, large, primary blue.
- Chapter title: centered, bold, dark navy.
- Level 1 heading: primary blue, bold, numbered.
- Level 2 heading: dark navy, bold, numbered.
- Important inline terms: bold.
- English keywords can be kept after Chinese terms when useful, for example `状态 state`.

## Callout boxes

Use callout boxes consistently:

### Main-thread box

Use for the chapter's core logic.

- Fill: light blue.
- Border: optional pale blue.
- Label: `Main thread` / `本章主线`.

### Notice box

Use for exam reminders, assumptions, and special conditions.

- Fill: light yellow.
- Label: `Notice` / `注意`.

### Mistake-prone box

Use for traps and misconceptions.

- Fill: light red.
- Label: `Mistake-prone point` / `易错点`.

### Formula / code / example block

Use for formulas, pseudocode, short code, or path examples.

- Fill: light gray.
- Monospace font when appropriate.
- Keep examples concise and separated from normal paragraphs.

## Tables

Tables should be easy to scan:

- Header row: primary blue background and white bold text.
- Body rows: white or very light gray alternating rows.
- Borders: light gray.
- Use compact cell padding.
- Prefer three columns for concept tables: `Concept`, `Meaning`, `Example`.
- Prefer three columns for exam tables: `Item`, `Key point`, `Exam interpretation`.

## Recommended recurring blocks

For each chapter, include these blocks when applicable:

1. Chapter main thread
2. Learning objectives
3. Table of contents
4. Concept table
5. Mechanism / process explanation
6. Formula / rule block
7. Worked example
8. Notice box
9. Mistake-prone box
10. Exam focus table
11. Quick review summary
12. Practice questions

## DOCX generation instruction

When creating a DOCX, preserve semantic structure rather than only plain text. Use real Word headings, tables, shaded paragraphs, page breaks, headers, and footers. Avoid producing one long unstyled document.

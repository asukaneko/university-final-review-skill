---
name: university-final-review
description: Generate comprehensive, cross-disciplinary university final-exam review materials from PPT slides, lecture notes, assignments, syllabi, screenshots, lab materials, case materials, or past papers. Use this skill when the user asks for final review notes, exam-point prediction, question banks, memorization outlines, mock exams, discipline-specific review plans, step-by-step problem/case/clinical/proof coaching, concept maps or mind maps, or polished DOCX/Word review handouts.
---

# University Final Review Skill

This skill turns university course materials from different disciplines into structured final-exam review resources.

Use this skill when the user wants to:

- Review uploaded PPT slides or lecture notes.
- Summarize chapters for final exams.
- Generate detailed study notes.
- Predict likely exam points.
- Generate practice questions and mock exams.
- Create memorization outlines.
- Generate active-recall test cards, flashcards, Anki-style CSV files, or interactive HTML review interfaces.
- Export polished Word / DOCX study handouts.
- Explain discipline-specific problem solving, such as calculation, proof, experiment analysis, case analysis, legal issue spotting, clinical reasoning, design critique, or essay planning.
- Get discipline-specific study strategy recommendations.
- Compare similar concepts, theories, diseases, or frameworks.
- Create concept maps, mind maps, comparison tables, and memory aids.
- Get error-prone point analysis and prevention strategies.

## Supported discipline categories

Use the most relevant category guide when generating the review package. Each category includes sub-discipline breakdowns, concrete examples, and discipline-specific templates:

- Computer Science / Engineering: `docs/en/categories/stem-engineering.md`, `docs/zh-CN/categories/stem-engineering.md`
- Natural Sciences / Mathematics: `docs/en/categories/natural-sciences.md`, `docs/zh-CN/categories/natural-sciences.md`
- Medicine / Health: `docs/en/categories/medicine-health.md`, `docs/zh-CN/categories/medicine-health.md`
- Law: `docs/en/categories/law.md`, `docs/zh-CN/categories/law.md`
- Humanities: `docs/en/categories/humanities.md`, `docs/zh-CN/categories/humanities.md`
- Social Sciences: `docs/en/categories/social-sciences.md`, `docs/zh-CN/categories/social-sciences.md`
- Business / Economics: `docs/en/categories/business-economics.md`, `docs/zh-CN/categories/business-economics.md`
- Education / Arts / Design: `docs/en/categories/education-arts.md`, `docs/zh-CN/categories/education-arts.md`

### Cross-disciplinary courses

When a course spans multiple disciplines, combine the relevant category guides. Examples:

- Medical Ethics: Medicine/Health + Law/Humanities
- Educational Psychology: Education + Social Sciences
- Business Law: Business/Economics + Law
- Technical Writing: CS/Engineering + Humanities
- Health Economics: Medicine/Health + Business/Economics

## Core workflow

1. Identify the course, chapters, discipline category, exam scope, and available materials.
2. Apply evidence-based study principles from `docs/en/learning-strategies.md` or `docs/zh-CN/learning-strategies.md`, then select the relevant discipline-specific review pattern.
3. Extract the chapter structure and major concepts from the user-provided files.
4. Build a material coverage map before writing: list the uploaded files, chapters, slide/section ranges, visible headings, diagrams, tables, examples, exercises, and teacher-emphasized cues that must be preserved.
5. Generate a course-level and chapter-level mind map from the material coverage map using `docs/en/mind-map.md` or `docs/zh-CN/mind-map.md`. The chapter overview must include a mind map before detailed notes.
6. In ChatGPT, when the user requests a mind-map image or a visual map would clearly improve the DOCX/complete review package, first create a verified Mermaid/outline version, then use GPT 图像模型 2 or ChatGPT's built-in visual tool to render an accurate, beautiful, readable mind-map image.
7. Generate deep lecture notes for each chapter with discipline-specific structure and source-grounded expansion.
8. Identify high-priority exam points and likely question types.
9. Generate a chapter-based question bank with answers and explanations across multiple difficulty levels.
10. Create comparison tables, concept maps, and memory aids for similar concepts.
11. Generate discipline-specific test cards using `docs/en/test-cards.md` or `docs/zh-CN/test-cards.md`.
12. If the user requests an interactive card-review tool, first generate a test-card CSV with columns `ID,Front,Back,Chapter,Topic,Difficulty,CardType,Tags`, then run `scripts/generate_test_cards_html.py` to create a standalone HTML review interface.
13. Produce memorization outlines with multiple memory techniques (keyword chains, mnemonics, acronyms, visual associations).
14. Provide discipline-specific worked examples and analysis templates using `docs/en/problem-solving-coach.md` or `docs/zh-CN/problem-solving-coach.md`.
15. Generate error-prone point analysis with prevention strategies.
16. Create study strategy recommendations adapted to the discipline.
17. If the user requests DOCX / Word output, apply the DOCX style guide instead of producing an unstyled plain document.
18. Generate a blueprint-driven precision mock exam using `docs/en/precision-mock-exam.md` or `docs/zh-CN/precision-mock-exam.md` if requested or when a complete package is requested.

## Grounding and information-preservation constraints

These constraints override brevity and generic summarization:

1. **Material-first, not template-first.** The lecture notes must be built from the actual uploaded files or explicitly mentioned course materials. Do not write generic textbook-style notes that could apply to any course without showing how the uploaded material shaped the content.
2. **Preserve source information.** Important definitions, formulas, processes, algorithms, diagrams, tables, examples, case names, experiment steps, code snippets, theorem conditions, teacher-emphasized points, and exercise patterns from the materials must be retained unless they are exact duplicates.
3. **No thin units.** A chapter, unit, or section must not be reduced to a few abstract bullets when the uploaded material contains substantial content. Each meaningful unit should include enough explanation, examples, exam use, and mistake-prone analysis to recover the original learning value of the material.
4. **Coverage before compression.** Compress repeated wording, but do not delete distinct concepts, boundary conditions, variants, steps, examples, or diagram/table information. If space is limited, prioritize structured tables and compact explanations over omission.
5. **Source labels are required.** Mark content sources with `来自上传资料`, `基于资料推测的考点`, or `补充背景知识` / `From uploaded materials`, `Exam points inferred from materials`, or `Supplementary background`.
6. **Mention evidence cues.** For key points, reference the evidence type from the material, such as PPT heading, repeated keyword, diagram, table, worked example, assignment question, past-paper pattern, or teacher-emphasis cue.
7. **Mind maps must be source-grounded.** Course and chapter mind maps must reflect the actual chapter headings, section hierarchy, diagrams, formulas, examples, and relationships from the uploaded materials. Do not generate decorative or generic mind maps that ignore the source structure.
8. **Mind-map images must be checked.** When a mind-map image is rendered, the structured Mermaid/outline version remains the source of truth. Check that the image preserves node text, hierarchy, relationships, exam tags, and readable layout; if it drops or distorts important content, provide the structured text version as the reliable source and render again or add a correction note.
9. **Flag missing or unclear material.** If the uploaded files are incomplete, low-resolution, truncated, or missing chapters, say what is missing and avoid silently filling the gap as if it came from the uploaded material.
10. **Quality check before final output.** Before delivering notes or DOCX content, verify that every uploaded chapter/section has corresponding notes, no obvious table/diagram/example was skipped, mind maps cover the real chapter structure, mind-map images match the structured map, and supplementary content is clearly labeled.

## Documentation

English documentation is in `docs/en/`.

Chinese documentation is in `docs/zh-CN/`.

### Core workflow docs

- `docs/en/overall-workflow.md` / `docs/zh-CN/overall-workflow.md` — Complete review generation workflow
- `docs/en/learning-strategies.md` / `docs/zh-CN/learning-strategies.md` — Evidence-based study strategies with discipline-specific adaptations

### Content generation docs

- `docs/en/deep-lecture-notes.md` / `docs/zh-CN/deep-lecture-notes.md` — Chapter-by-chapter deep notes
- `docs/en/mind-map.md` / `docs/zh-CN/mind-map.md` — Source-grounded course and chapter mind maps
- `docs/en/exam-point-predictor.md` / `docs/zh-CN/exam-point-predictor.md` — Exam point prediction
- `docs/en/question-bank-generator.md` / `docs/zh-CN/question-bank-generator.md` — Question bank generation
- `docs/en/test-cards.md` / `docs/zh-CN/test-cards.md` — Test cards and active recall
- `docs/en/memorization-outline.md` / `docs/zh-CN/memorization-outline.md` — Memorization outlines with memory techniques
- `docs/en/precision-mock-exam.md` / `docs/zh-CN/precision-mock-exam.md` — Blueprint-driven mock exams

### Discipline-specific docs

- `docs/en/categories/README.md` / `docs/zh-CN/categories/README.md` — Category overview and selection guide
- `docs/en/problem-solving-coach.md` / `docs/zh-CN/problem-solving-coach.md` — Discipline-specific problem-solving templates

### Output docs

- `docs/en/output-format.md` / `docs/zh-CN/output-format.md` — Output formatting guide
- `docs/en/docx-style-guide.md` / `docs/zh-CN/docx-style-guide.md` — DOCX styling guide

### Scripts

- `scripts/generate_test_cards_html.py` — Generate interactive HTML review interface from CSV
- `scripts/generate_styled_docx.py` — Generate styled DOCX documents

## Output principles

- Stay grounded in the uploaded materials.
- Do not produce vague summaries when the user asks for exam review.
- Do not let any unit become too thin: preserve the informational density of the uploaded materials and expand important points into study-ready explanations.
- Add a mind map in the course overview and in every chapter overview. Use Mermaid mindmap, Markdown tree, or DOCX-friendly hierarchy boxes depending on the requested output format.
- In ChatGPT, when a mind-map image is requested or clearly useful, first create a verified Mermaid / outline version, then use GPT 图像模型 2 or ChatGPT's built-in visual tool to produce an accurate, beautiful, readable mind-map image. The structured map remains the source of truth.
- Choose an output structure that fits the discipline.
- Make the output directly useful for studying, memorizing, analyzing, and solving questions.
- Use clear sectioning, tables, worked examples, concept maps, mind maps, timelines, case templates, test cards, and scoring rubrics when useful.
- For interactive test-card review, generate a clean CSV first, then create a standalone HTML interface with search, filters, flip cards, self-rating, weak-card review, progress tracking, and exportable study records.
- For DOCX output, use polished academic handout formatting: blue headings, callout boxes, readable tables, headers, footers, page breaks, printable spacing, and readable mind-map blocks or mind-map images when available.
- For medical, legal, financial, or other high-stakes subjects, frame outputs as study support, not professional advice.
- For Chinese users, produce exam-oriented Chinese explanations unless the user requests English.
- For English users, produce polished English study notes unless the user requests Chinese.
- Mark content sources: `来自上传资料`, `基于资料推测的考点`, `补充背景知识`.

## Default output package

When the user asks for a complete review package, include:

1. Course overview and exam scope
2. Discipline category and review strategy (with sub-discipline breakdown)
3. Evidence-based study plan with spaced repetition schedule
4. Course-level mind map and chapter-level overview mind maps
5. Chapter-by-chapter deep notes with discipline-specific structure
6. Exam point prediction with priority ranking (必考点 / 高频考点 / 低频易拿分)
7. Concept comparison tables, formula/rule summaries
8. Chapter-based question bank (4 difficulty levels: 基础 / 常考 / 综合 / 迁移)
9. Test cards for active recall, optionally exported as CSV and interactive HTML using `scripts/generate_test_cards_html.py`
10. Memorization outlines with multiple memory techniques (keyword chains, mnemonics, acronyms, visual associations)
11. Discipline-specific worked examples and analysis templates
12. Error-prone point analysis with prevention strategies
13. Error log and weak-point repair plan
14. Final sprint checklist with time allocation advice
15. Optional polished DOCX handout using the style guide
16. Blueprint-driven 100-point precision mock exam with answer key, partial-credit rubric, and post-exam diagnosis

Base directory for this skill: file:///C:/Users/ycssb/.claude/skills/university-final-review-skill-main

Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.

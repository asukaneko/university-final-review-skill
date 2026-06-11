---
name: university-final-review
description: Generate comprehensive, cross-disciplinary university final-exam review materials from PPT slides, lecture notes, assignments, syllabi, screenshots, lab materials, case materials, or past papers. Use this skill when the user asks for final review notes, exam-point prediction, question banks, memorization outlines, mock exams, discipline-specific review plans, step-by-step problem/case/clinical/proof coaching, or polished DOCX/Word review handouts.
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
- Export polished Word / DOCX study handouts.
- Explain discipline-specific problem solving, such as calculation, proof, experiment analysis, case analysis, legal issue spotting, clinical reasoning, design critique, or essay planning.

## Supported discipline categories

Use the most relevant category guide when generating the review package:

- Computer Science / Engineering: `docs/en/categories/stem-engineering.md`, `docs/zh-CN/categories/stem-engineering.md`
- Natural Sciences / Mathematics: `docs/en/categories/natural-sciences.md`, `docs/zh-CN/categories/natural-sciences.md`
- Medicine / Health: `docs/en/categories/medicine-health.md`, `docs/zh-CN/categories/medicine-health.md`
- Law: `docs/en/categories/law.md`, `docs/zh-CN/categories/law.md`
- Humanities: `docs/en/categories/humanities.md`, `docs/zh-CN/categories/humanities.md`
- Social Sciences: `docs/en/categories/social-sciences.md`, `docs/zh-CN/categories/social-sciences.md`
- Business / Economics: `docs/en/categories/business-economics.md`, `docs/zh-CN/categories/business-economics.md`
- Education / Arts / Design: `docs/en/categories/education-arts.md`, `docs/zh-CN/categories/education-arts.md`

## Core workflow

1. Identify the course, chapters, discipline category, exam scope, and available materials.
2. Apply evidence-based study principles from `docs/en/learning-strategies.md` or `docs/zh-CN/learning-strategies.md`, then select the relevant discipline-specific review pattern.
3. Extract the chapter structure and major concepts from the user-provided files.
4. Generate deep lecture notes for each chapter.
5. Identify high-priority exam points and likely question types.
6. Generate a chapter-based question bank with answers and explanations.
7. Produce memorization outlines and last-minute checklists.
8. Provide discipline-specific worked examples where relevant, using `docs/en/problem-solving-coach.md` or `docs/zh-CN/problem-solving-coach.md`:
   - calculation, proof, derivation, coding, or system design for STEM courses;
   - theorem, experiment, graph, or mechanism interpretation for natural sciences;
   - clinical reasoning and safety cautions for medical courses;
   - issue-rule-application-conclusion analysis for law;
   - thesis-evidence-analysis writing for humanities;
   - theory-method-case analysis for social sciences;
   - model-financial-case analysis for business and economics;
   - lesson-plan, critique, or portfolio review for education, arts, and design.
9. If the user requests DOCX / Word output, apply the DOCX style guide instead of producing an unstyled plain document.
10. Generate a complete mock exam if requested.

## Documentation

English documentation is in `docs/en/`.

Chinese documentation is in `docs/zh-CN/`.

Recommended references:

- `docs/en/overall-workflow.md`
- `docs/en/learning-strategies.md`
- `docs/en/categories/README.md`
- `docs/en/problem-solving-coach.md`
- `docs/en/docx-style-guide.md`
- `docs/en/deep-lecture-notes.md`
- `docs/en/exam-point-predictor.md`
- `docs/en/question-bank-generator.md`
- `docs/en/memorization-outline.md`
- `docs/en/output-format.md`
- `docs/zh-CN/overall-workflow.md`
- `docs/zh-CN/learning-strategies.md`
- `docs/zh-CN/categories/README.md`
- `docs/zh-CN/problem-solving-coach.md`
- `docs/zh-CN/docx-style-guide.md`
- `docs/zh-CN/deep-lecture-notes.md`
- `docs/zh-CN/exam-point-predictor.md`
- `docs/zh-CN/question-bank-generator.md`
- `docs/zh-CN/memorization-outline.md`
- `docs/zh-CN/output-format.md`

## Output principles

- Stay grounded in the uploaded materials.
- Do not produce vague summaries when the user asks for exam review.
- Choose an output structure that fits the discipline.
- Make the output directly useful for studying, memorizing, analyzing, and solving questions.
- Use clear sectioning, tables, worked examples, concept maps, timelines, case templates, and scoring rubrics when useful.
- For DOCX output, use polished academic handout formatting: blue headings, callout boxes, readable tables, headers, footers, page breaks, and printable spacing.
- For medical, legal, financial, or other high-stakes subjects, frame outputs as study support, not professional advice.
- For Chinese users, produce exam-oriented Chinese explanations unless the user requests English.
- For English users, produce polished English study notes unless the user requests Chinese.

## Default output package

When the user asks for a complete review package, include:

1. Course overview
2. Discipline category and review strategy
3. Chapter-by-chapter deep notes
4. Exam point prediction
5. Question bank
6. Memorization outline
7. Discipline-specific worked examples and analysis templates where applicable
8. Final sprint checklist
9. Optional polished DOCX handout using the style guide
10. 100-point mock exam with answer key and scoring rubric

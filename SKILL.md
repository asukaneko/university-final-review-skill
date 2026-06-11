---
name: university-final-review
description: Generate comprehensive university final-exam review materials from PPT slides, lecture notes, assignments, syllabi, screenshots, or past papers. Use this skill when the user asks for final review notes, exam-point prediction, question banks, memorization outlines, mock exams, or step-by-step calculation/algorithm problem coaching.
---

# University Final Review Skill

This skill turns university course materials into structured final-exam review resources.

Use this skill when the user wants to:

- Review uploaded PPT slides or lecture notes.
- Summarize chapters for final exams.
- Generate detailed study notes.
- Predict likely exam points.
- Generate practice questions and mock exams.
- Create memorization outlines.
- Explain calculation, scheduling, algorithm, database, or network problems step by step.

## Core workflow

1. Identify the course, chapters, exam scope, and available materials.
2. Extract the chapter structure and major concepts from the user-provided files.
3. Generate deep lecture notes for each chapter.
4. Identify high-priority exam points and likely question types.
5. Generate a chapter-based question bank with answers and explanations.
6. Produce memorization outlines and last-minute checklists.
7. For technical courses, provide formulas, derivations, pseudocode, C++ examples, or hand-calculation steps when relevant.
8. Generate a complete mock exam if requested.

## Documentation

English documentation is in `docs/en/`.

Chinese documentation is in `docs/zh-CN/`.

Recommended references:

- `docs/en/overall-workflow.md`
- `docs/en/deep-lecture-notes.md`
- `docs/en/exam-point-predictor.md`
- `docs/en/question-bank-generator.md`
- `docs/en/memorization-outline.md`
- `docs/en/calculation-algorithm-coach.md`
- `docs/en/output-format.md`
- `docs/zh-CN/overall-workflow.md`
- `docs/zh-CN/deep-lecture-notes.md`
- `docs/zh-CN/exam-point-predictor.md`
- `docs/zh-CN/question-bank-generator.md`
- `docs/zh-CN/memorization-outline.md`
- `docs/zh-CN/calculation-algorithm-coach.md`
- `docs/zh-CN/output-format.md`

## Output principles

- Stay grounded in the uploaded materials.
- Do not produce vague summaries when the user asks for exam review.
- Make the output directly useful for studying, memorizing, and solving questions.
- Use clear sectioning, tables, worked examples, and scoring rubrics when useful.
- For Chinese users, produce exam-oriented Chinese explanations unless the user requests English.
- For English users, produce polished English study notes unless the user requests Chinese.

## Default output package

When the user asks for a complete review package, include:

1. Course overview
2. Chapter-by-chapter deep notes
3. Exam point prediction
4. Question bank
5. Memorization outline
6. Calculation / algorithm coaching where applicable
7. Final sprint checklist
8. 100-point mock exam with answer key and scoring rubric

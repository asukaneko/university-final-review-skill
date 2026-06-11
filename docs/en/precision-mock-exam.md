# Precision Mock Exam Blueprint

Use this module to generate accurate, exam-like mock papers rather than generic practice sets. A precision mock exam should reflect the course materials, assessment style, topic weight, cognitive level, and marking logic.

## Required inputs

Use all available evidence:

- syllabus and official exam scope;
- lecture slides and notes;
- assignments, labs, tutorials, quizzes;
- past papers and model answers;
- instructor emphasis and repeated examples;
- user-stated exam format, duration, and total marks.

If the exam format is unknown, infer a reasonable default and clearly mark it as inferred.

## Exam blueprint table

Before writing questions, create a blueprint:

| Topic / chapter | Evidence source | Expected weight | Cognitive level | Question type | Marks |
| --- | --- | ---: | --- | --- | ---: |
| Chapter 1 | slides + assignment | 15% | recall + application | MCQ + short answer | 15 |

## Cognitive-level balance

Use a balanced distribution unless course evidence suggests otherwise:

- 20-30% recall and recognition;
- 25-35% explanation and conceptual understanding;
- 25-35% application, calculation, case, proof, or analysis;
- 10-20% integration, evaluation, design, or transfer.

## Question precision rules

Every question should specify:

- source topic or chapter;
- intended learning outcome;
- difficulty level;
- expected time;
- marks;
- answer format;
- scoring points;
- common traps.

Avoid vague questions such as “Discuss chapter 4”. Ask targeted, markable questions.

## Standard 100-point structure

When no format is provided, use:

1. **Section A: Fast recall and concept checks** — 20 points.
2. **Section B: Short-answer explanations** — 25 points.
3. **Section C: Applied problems / cases / calculations / analysis** — 35 points.
4. **Section D: Integrated high-value question** — 20 points.

Adjust the structure by discipline:

- STEM: include calculations, algorithms, derivations, debugging, or design.
- Natural sciences: include mechanism, data interpretation, proof, experiment design.
- Medicine: include case vignettes, lab interpretation, safety, clinical reasoning.
- Law: include issue-spotting hypotheticals, rule application, policy essay.
- Humanities: include evidence-based essays, close reading, comparison.
- Social sciences: include theory application, methods critique, data/case analysis.
- Business: include calculations, graphs, case recommendation, managerial memo.
- Education/arts/design: include critique, lesson/design task, reflection, portfolio rationale.

## Answer key requirements

The answer key must include:

- correct answer;
- reasoning steps;
- mark allocation;
- acceptable alternatives;
- common wrong answers and why they fail;
- source topic reference;
- grading notes for partial credit.

## Rubric format

```markdown
### Question X rubric: [marks]

| Criterion | Marks | Award when... |
| --- | ---: | --- |
| Correct rule/model selection | 2 | Student identifies ... |
| Application to facts/data | 4 | Student uses ... |
| Explanation/interpretation | 2 | Student explains ... |
```

## Mock exam variants

When useful, generate multiple versions:

- **Version A: likely exam style** — closest to expected format.
- **Version B: harder transfer version** — tests unfamiliar cases.
- **Version C: rapid diagnostic version** — shorter, identifies weak chapters.

## Calibration checklist

Before finalizing, check:

- Total marks add to 100.
- Time is realistic.
- Every major chapter is represented according to weight.
- Questions match the stated discipline and exam style.
- There are no answer leaks in the question text.
- The answer key is specific enough for self-marking.
- The mock exam includes at least one integrative question.

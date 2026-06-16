# Overall Workflow

Use this workflow when the user asks for a complete university final-review package.

## Input materials

The user may provide:

- PPT slides
- Lecture notes
- Textbook excerpts
- Assignment sheets
- Past papers
- Syllabus or exam scope
- Screenshots of class materials
- Lab reports
- Course video screenshots
- Handwritten notes

## Workflow

### Step 1: Confirm and plan

1. Confirm course name, chapter range, and exam scope.
2. Determine the discipline category, select the corresponding [`categories/`](categories/README.md) guide.
3. Assess completeness of available materials, marking missing, unreadable, duplicated, or out-of-scope sections.
4. Develop a review package generation plan.

### Step 2: Material inventory and structure extraction

Before writing the notes, build a material coverage map to avoid information loss and to provide the structure for mind maps.

1. Organize the materials by file, chapter, page/slide range, and heading hierarchy.
2. Extract core concepts, definitions, formulas, processes, algorithms, diagrams, tables, worked examples, experiment steps, cases, assignments, and past-paper clues.
3. Mark frequently occurring content, high-level headings, instructor-emphasized points, repeated keywords, and question-type clues.
4. Build a logical relationship map between chapters.
5. Extract mind-map nodes for the course overview and each chapter overview: chapter themes, primary modules, secondary concepts, key formulas/processes/algorithms/diagrams, typical examples, and high-yield exam points.
6. Mark information-dense units as "must expand" so they are not reduced to brief summaries.

### Step 3: Chapter-by-chapter deep generation

For each chapter, generate in this order:

1. Chapter overview and position in the course.
2. Material coverage map: uploaded files, material excerpts, diagrams, tables, formulas, worked examples, assignments, or user-mentioned content used for this chapter.
3. Chapter overview mind map: use Mermaid `mindmap`, an indented tree, or DOCX hierarchy boxes to show the chapter knowledge structure.
4. Mind-map reading guide: identify which trunks to review first, which branches correspond to exam question types, and which nodes require memorization or calculation.
5. Core concepts and definitions.
6. Key mechanisms, formulas, algorithms, structural diagrams, experiment steps, or case frameworks.
7. Exam-oriented explanations.
8. Common question types and problem-solving approaches.
9. Common errors and precautions.
10. Concept comparison tables.
11. One-page speed notes.
12. Practice problems and answers.

When generating chapter notes, follow these constraints:

- The notes must correspond to the uploaded materials or the user's explicitly mentioned material scope. Do not write generic disciplinary knowledge only.
- The chapter overview must include a mind map, and mind-map nodes must come from headings, diagrams, formulas, processes, algorithms, examples, assignments, or exam-point clues in the materials.
- Units must not be too thin. If a section has substantial source material, expand it into "definition/conclusion + mechanism/process + preserved material details + example/question type + mistake-prone points".
- Do not lose source information. Preserve or rewrite definitions, formulas, steps, diagrams, examples, classifications, conditions, advantages/disadvantages, case elements, and question-type clues as study tables or explanations.
- Compress repeated wording only; do not delete distinct concepts, conditions, variants, or examples.

### Step 4: Exam point analysis

1. Analyze high-yield exam points and likely question types.
2. Predict exam weight for each chapter.
3. Mark must-know points, high-frequency points, and low-frequency easy points.
4. Provide priority for "1 day left" and "3 hours left" scenarios.
5. For every important exam point, state the evidence cue: heading hierarchy, repetition, diagram/table/formula, assignment, past paper, worked example, or instructor-emphasis trace.
6. Add must-know, high-frequency, and mistake-prone markers to the corresponding mind-map nodes.

### Step 5: Question bank generation

1. Generate chapter practice questions with answer explanations.
2. Layer by difficulty (basic, standard, comprehensive, transfer).
3. Include multiple question types (MCQ, fill-in, short answer, calculation, case, etc.).
4. Each question with detailed explanation and common errors.
5. Prefer converting examples, assignments, past papers, and typical diagrams/tables from the materials into question prototypes.
6. Questions may reference corresponding mind-map branches to help students review structurally.

### Step 6: Active recall materials

1. Generate test cards (definition cards, comparison cards, process cards, application cards, etc.).
2. Organize memorization outlines and speed notes.
3. Provide keyword chain memory techniques and mnemonics.
4. Cards should cover key definitions, formulas, processes, diagrams, comparison points, example methods, and mistake-prone points from the materials.
5. Test cards may be grouped by chapter mind-map branches.

### Step 7: Problem-solving coach

1. Add step-by-step problem-solving for calculation, algorithm, case, and other discipline-specific problems.
2. Provide discipline-specific analysis templates.
3. Include worked examples and common variations.
4. Derive problem-solving templates primarily from examples, assignments, labs, or past papers in the uploaded materials.

### Step 8: Mock exam

1. Generate a precision 100-point mock exam based on the blueprint.
2. Include answer key, scoring rubric, and partial-credit notes.
3. Provide post-exam diagnosis analysis.
4. Match question coverage to the information volume, chapter weight, and exam scope reflected in the uploaded materials.

### Step 9: Output organization

1. Organize all content in a unified format.
2. If needed, generate a DOCX version.
3. If needed, generate an interactive test card HTML.
4. Before final delivery, run a material coverage check to ensure no important unit, diagram, formula, worked example, process, or question-type clue has been skipped.
5. Check that the course overview and every chapter overview include source-grounded mind maps rather than generic templates.

## Default complete output

A complete final-review package should include:

1. Course overview and exam scope
2. Discipline category and review strategy (with sub-discipline breakdown)
3. Chapter structure
4. Material coverage map
5. Course overview mind map
6. Chapter overview mind maps for each chapter
7. Chapter-by-chapter review notes
8. Exam priority ranking (must-know / high-frequency / low-frequency easy)
9. Key definitions and core concepts
10. Concept comparison tables, formula/rule summaries
11. Common question types
12. Common errors
13. Chapter question bank (4 difficulty levels: basic / standard / comprehensive / transfer)
14. Test cards (exportable as CSV and interactive HTML)
15. Memorization outlines with multiple memory techniques
16. Error log and weak-point repair plan
17. Final sprint checklist with time allocation advice
18. Precision mock exam (with scoring rubric and post-exam diagnosis)

## Grounding rule

Always prioritize the user's uploaded materials. If a concept is not present in the materials but is necessary background, mark it as supplementary.

Labeling rules:

- `来自上传资料` / `From uploaded materials`: Directly extracted from user-provided materials.
- `基于资料推测的考点` / `Exam points inferred from materials`: Exam priorities inferred from materials.
- `补充背景知识` / `Supplementary background`: Background information not in materials but necessary.

## Information-preservation rule

A complete review package is not a minimal summary; it is a structured rewrite of the materials. Follow these rules:

1. Cover every uploaded or mentioned chapter, unit, and major subsection.
2. Preserve definitions, formulas, processes, algorithms, diagrams, tables, examples, classifications, experiment steps, cases, assignments, and past-paper clues from the materials.
3. Do not mention diagrams, formulas, or examples only in passing; convert them into explanations, tables, steps, question templates, or mind-map nodes.
4. Units must not be too short. If a unit has substantial source material, the notes should increase in depth accordingly.
5. Compress repeated information only; do not delete independent information points.
6. If materials are missing or unreadable, clearly state the missing range.

## Mind-map rule

When generating course overview or chapter overview content, follow [`mind-map.md`](mind-map.md). Default requirements:

- The course overview mind map shows chapter relationships, main course logic, module grouping, and exam weight.
- Chapter overview mind maps show heading hierarchy, core concepts, formulas/processes/algorithms/diagrams, worked examples, and question-type clues.
- Nodes must come from the materials or be inferred from the material structure. Do not use generic templates.
- Markdown output should prefer Mermaid `mindmap`; DOCX output should use printable hierarchy boxes, indented trees, table blocks, or readable images.
- Mind maps should serve review rather than decoration; prioritize structure, relationships, exam points, and mistake-prone points.

## Output format

Choose output format based on user needs:

- **Markdown**: Default format, suitable for online viewing and editing; mind maps should prefer Mermaid `mindmap` or indented trees.
- **DOCX/Word**: Suitable for printing and sharing, see [`docx-style-guide.md`](docx-style-guide.md); mind maps should use hierarchy boxes, indented trees, table blocks, or readable images.
- **Interactive HTML**: Test cards only, see [`test-cards.md`](test-cards.md).

## Multi-disciplinary combinations

When a course spans multiple disciplines:

1. Identify primary and secondary disciplines.
2. Use the primary discipline's template as the base.
3. Supplement with secondary discipline-specific content.
4. Use combination templates at intersection points.

Examples:

- Medical Ethics: Medicine/Health + Law/Humanities
- Educational Psychology: Education + Social Sciences
- Business Law: Business/Economics + Law
- Technical Writing: Computer Science/Engineering + Humanities
- Health Economics: Medicine/Health + Business/Economics

## Quality checklist

After completing the review package, check:

- [ ] Chapter structure fully covers exam scope.
- [ ] A material coverage map has been created.
- [ ] A course overview mind map has been generated.
- [ ] Every chapter overview includes a mind map.
- [ ] Mind maps come from the material structure and cover major sections, diagrams, formulas, processes, examples, and exam-point clues.
- [ ] Every chapter and section corresponds to uploaded or user-mentioned materials.
- [ ] Concept definitions are accurate and clear.
- [ ] Formulas and theorems include applicable conditions.
- [ ] Diagrams, tables, formulas, processes, algorithms, examples, cases, and assignment clues from the materials are preserved.
- [ ] No section is too thin, generic, or detached from the materials.
- [ ] Question bank covers multiple difficulty levels and types.
- [ ] Answer explanations are sufficiently detailed.
- [ ] Common errors are clearly marked.
- [ ] Memorization outlines are ready to use.
- [ ] Mock exam matches the exam format.
- [ ] All content is grounded in uploaded materials.
- [ ] Supplementary content is labeled as "supplementary background."
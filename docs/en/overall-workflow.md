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
3. Assess completeness of available materials, mark missing parts.
4. Develop a review package generation plan.

### Step 2: Structure extraction

1. Build a chapter structure from the materials.
2. Extract core concepts, definitions, formulas, processes, algorithms, and diagrams.
3. Mark frequently occurring content and instructor-emphasized priorities.
4. Build a logical relationship map between chapters.

### Step 3: Chapter-by-chapter deep generation

For each chapter, generate in this order:

1. Chapter overview and position in the course.
2. Core concepts and definitions.
3. Key mechanisms, formulas, algorithms, or structural diagrams.
4. Exam-oriented explanations.
5. Common question types and problem-solving approaches.
6. Common errors and precautions.
7. Concept comparison tables.
8. One-page speed notes.
9. Practice problems and answers.

### Step 4: Exam point analysis

1. Analyze high-yield exam points and likely question types.
2. Predict exam weight for each chapter.
3. Mark must-know points, high-frequency points, and low-frequency easy points.
4. Provide priority for "1 day left" and "3 hours left" scenarios.

### Step 5: Question bank generation

1. Generate chapter practice questions with answer explanations.
2. Layer by difficulty (basic, standard, comprehensive, transfer).
3. Include multiple question types (MCQ, fill-in, short answer, calculation, case, etc.).
4. Each question with detailed explanation and common errors.

### Step 6: Active recall materials

1. Generate test cards (definition cards, comparison cards, process cards, application cards, etc.).
2. Organize memorization outlines and speed notes.
3. Provide keyword chain memory techniques and mnemonics.

### Step 7: Problem-solving coach

1. Add step-by-step problem-solving for calculation, algorithm, case, and other discipline-specific problems.
2. Provide discipline-specific analysis templates.
3. Include worked examples and common variations.

### Step 8: Mock exam

1. Generate a precision 100-point mock exam based on the blueprint.
2. Include answer key, scoring rubric, and partial-credit notes.
3. Provide post-exam diagnosis analysis.

### Step 9: Output organization

1. Organize all content in a unified format.
2. If needed, generate a DOCX version.
3. If needed, generate an interactive test card HTML.

## Default complete output

A complete final-review package should include:

1. Course overview and exam scope
2. Discipline category and review strategy (with sub-discipline breakdown)
3. Chapter structure
4. Chapter-by-chapter review notes
5. Exam priority ranking (must-know / high-frequency / low-frequency easy)
6. Key definitions and core concepts
7. Concept comparison tables, formula/rule summaries
8. Common question types
9. Common errors
10. Chapter question bank (4 difficulty levels: basic / standard / comprehensive / transfer)
11. Test cards (exportable as CSV and interactive HTML)
12. Memorization outlines with multiple memory techniques
13. Error log and weak-point repair plan
14. Final sprint checklist with time allocation advice
15. Precision mock exam (with scoring rubric and post-exam diagnosis)

## Grounding rule

Always prioritize the user's uploaded materials. If a concept is not present in the materials but is necessary background, mark it as supplementary.

Labeling rules:

- `来自上传资料` / `From uploaded materials`: Directly extracted from user-provided materials.
- `基于资料推测的考点` / `Exam points inferred from materials`: Exam priorities inferred from materials.
- `补充背景知识` / `Supplementary background`: Background information not in materials but necessary.

## Output format

Choose output format based on user needs:

- **Markdown**: Default format, suitable for online viewing and editing.
- **DOCX/Word**: Suitable for printing and sharing, see [`docx-style-guide.md`](docx-style-guide.md).
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
- Technical Writing: CS/Engineering + Humanities
- Health Economics: Medicine/Health + Business/Economics

## Quality checklist

After completing the review package, check:

- [ ] Chapter structure fully covers exam scope.
- [ ] Concept definitions are accurate and clear.
- [ ] Formulas and theorems include applicable conditions.
- [ ] Question bank covers multiple difficulty levels and types.
- [ ] Answer explanations are sufficiently detailed.
- [ ] Common errors are clearly marked.
- [ ] Memorization outlines are ready to use.
- [ ] Mock exam matches the exam format.
- [ ] All content is grounded in uploaded materials.
- [ ] Supplementary content is labeled as "supplementary background."

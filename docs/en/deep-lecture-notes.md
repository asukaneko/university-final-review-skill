# Deep Lecture Notes

Use this module to convert PPT slides, lecture notes, textbook excerpts, class screenshots, assignments, past papers, or explicitly mentioned course materials into detailed final-exam study notes. The output must be more than a simple summary or a generic textbook overview.

## Core principle: notes must be tied to the materials

Lecture notes must prioritize the user's uploaded or explicitly mentioned materials. Do not write broad discipline summaries that could apply to any course. Each chapter, section, and major concept should show how it is grounded in the materials, such as slide headings, subsections, diagrams, tables, formulas, worked examples, assignments, past-paper patterns, instructor-emphasized keywords, or the user's stated exam scope.

If a concept is not present in the materials but is necessary for understanding, label it as `Supplementary background`. Do not present it as if it came from the uploaded materials.

## Output structure per chapter

For each chapter, include:

1. Chapter role in the course
2. Material coverage map: corresponding files, page/slide ranges, headings, diagrams, tables, worked examples, assignments, or user-mentioned material points
3. Chapter overview mind map: generated from headings, knowledge structure, process relationships, formulas/algorithms/diagrams/examples in the materials
4. Core concepts
5. Important definitions from the PPT / notes / textbook excerpts
6. Key mechanisms, processes, formulas, models, algorithms, diagrams, experiment steps, or case explanations
7. Exam-oriented explanations
8. Common question types
9. Mistake-prone points
10. Concept comparison tables
11. One-page quick review

## Chapter overview mind map requirements

Every chapter overview must include a mind map. The mind map helps students build the structure first, then enter detailed review.

The mind map must follow these rules:

1. **Source-grounded nodes**: Nodes must come from chapter headings, section headings, diagrams, tables, processes, formulas, algorithms, worked examples, cases, assignments, or user-mentioned material points.
2. **Clear hierarchy**: Prefer 3–5 levels: chapter theme → primary modules → secondary concepts → key conditions/formulas/steps/question types.
3. **Coverage of key content**: Cover the main knowledge blocks of the chapter. Do not include only a few concept names.
4. **Relationship expression**: For processes, algorithms, causal chains, classification systems, comparison relationships, and input-output relationships, reflect the relationship in node wording, such as "leads to", "depends on", "classified into", "steps", "conditions", or "applies to".
5. **Exam orientation**: Mark high-yield points, mistake-prone points, and typical question types with tags such as `[Must-know]`, `[Mistake-prone]`, or `[Question type]`.
6. **No generic decoration**: Do not generate decorative branches unrelated to the material structure.

Recommended output forms:

- Markdown default: prefer Mermaid `mindmap` code blocks; if Mermaid is not supported, use an indented tree.
- DOCX output: use printable hierarchy boxes, nested indentation, or table blocks, and optionally preserve the Mermaid source.
- Image output: if the user explicitly asks for an image, generate a separate image from the Mermaid or tree structure.

After the mind map, add a short "how to read this map" note explaining which trunks to review first, which branches correspond to exam question types, and which nodes require memorization or calculation.

## Unit density requirements

Do not compress a unit into a few abstract conclusions. If the materials contain substantial content for a unit, expand it enough for review, memorization, and problem solving.

Each meaningful unit should cover at least:

- **Source cue**: the type of source evidence, such as heading, table, diagram, worked example, formula, flowchart, or instructor-emphasis cue.
- **Core definition / conclusion**: key wording and limiting conditions from the materials.
- **Expanded explanation**: why the concept exists, what problem it solves, and how its internal logic or process works.
- **Preserved material details**: categories, steps, conditions, advantages/disadvantages, comparison dimensions, examples, diagram/table information, formula variables, and applicable scope.
- **Exam transformation**: how it may appear as MCQ, fill-in, short-answer, calculation, analysis, drawing, proof, case, or comprehensive questions.
- **Mistake-prone points**: common confusions, missing keywords, calculation errors, or misuse scenarios.

If a subsection contains multiple concepts, diagrams, examples, or algorithmic steps, split them into separate subpoints instead of merging them into one sentence.

## Information-preservation rules

The goal is to turn materials into study-ready notes, not to delete information through summarization. Follow these rules:

1. Preserve all important definitions, formulas, algorithmic steps, processes, classifications, table fields, diagram meanings, worked-example methods, experiment steps, case elements, and instructor-emphasized points.
2. Compress repeated wording only; do not delete distinct concepts, conditions, variants, examples, or question-type clues.
3. Convert tables and diagrams into text explanations, review tables, or mind-map nodes. Do not merely write "as shown in the figure".
4. For formulas, explain variables, applicable conditions, common question types, and mistake-prone points.
5. For algorithms, processes, experiments, and case analysis, preserve step order and key decision conditions.
6. Treat examples from textbooks or slides as examples, application scenarios, or question prototypes whenever possible.
7. If the material is unclear, truncated, low-resolution, or missing context, explicitly mark the limitation. Do not invent missing content as if it came from the uploaded materials.

## Expansion rules

Do not only restate slide bullet points. For each major concept, explain:

- Why the concept exists
- What problem it solves
- How it works
- How it differs from similar concepts
- Which definitions, diagrams, tables, examples, formulas, processes, or emphasis cues appear in the materials
- Which branch of the chapter mind map it belongs to and which nodes it relates to
- How it may appear in exams
- Which keywords, steps, or formulas should appear in an answer

## Source-labeling rules

Label key content by source:

- `来自上传资料` / `From uploaded materials`: directly extracted or rewritten from user-provided materials.
- `基于资料推测的考点` / `Exam points inferred from materials`: inferred from frequency, heading hierarchy, examples, assignments, past papers, or emphasis cues.
- `补充背景知识` / `Supplementary background`: not directly present in the materials but necessary for understanding or problem solving.

Avoid overloading every sentence with labels. Use section openings, table columns, mind-map notes, or highlighted blocks when appropriate.

## Quality checklist

Before delivering notes, check:

- [ ] Every uploaded or mentioned chapter, unit, and major subsection is covered.
- [ ] Every chapter overview includes a mind map based on the material structure.
- [ ] Mind maps cover major headings, core concepts, formula/process/diagram/example clues, and high-yield exam points.
- [ ] No important diagram, table, formula, worked example, process, algorithm, case, or assignment pattern from the materials is skipped.
- [ ] No section reads like generic common knowledge without connection to the materials.
- [ ] No unit is too thin to support review or problem solving.
- [ ] Distinct concepts from the materials were not wrongly merged or over-compressed.
- [ ] Supplementary background is clearly labeled.
- [ ] Exam-oriented wording, question-type cues, and mistake-prone points are included.

## Style

The notes should be detailed, structured, and directly useful for university final-exam review. Prefer clear headings, compact tables, examples, step-by-step explanations, chapter overview mind maps, ready-to-memorize phrasing, and exam-oriented prompts. The output should preserve the informational value of the materials while making it clearer, not thinner or more generic.
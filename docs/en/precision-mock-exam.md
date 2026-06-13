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

Avoid vague questions such as "Discuss chapter 4". Ask targeted, markable questions.

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

## Standard exam paper template

When generating the mock exam, use the following unified template format. The output must be split into two independent parts: **Exam Paper** and **Answer Key with Scoring Rubric**.

### Exam paper template (Markdown format)

```markdown
---

# 【Course Name】Final Mock Examination

**Duration: 【X】 minutes &emsp; Total Marks: 100 &emsp; Mode: Closed-book / Open-book**

**Instructions:**
1. This paper contains 【X】 questions, totaling 100 marks. Complete within the time limit.
2. Read each question carefully before answering. Allocate your time wisely.
3. Write clearly and show all working. Calculation questions without shown steps may not receive marks.
4. This paper is for study purposes only and does not constitute an official examination.

---

## Section A: Multiple Choice (X marks each, X marks total)

**Instructions: Select the single best answer. Write the letter in the brackets.**

**1.** 【Question stem】（  ）

A. 【Option A】

B. 【Option B】

C. 【Option C】

D. 【Option D】

---

**2.** 【Question stem】（  ）

A. 【Option A】

B. 【Option B】

C. 【Option C】

D. 【Option D】

---

## Section B: Fill in the Blanks (X marks each, X marks total)

**Instructions: Write the correct answer on the line.**

**3.** 【Question stem with ______ blanks】.

**4.** 【Question stem with ______ blanks】.

---

## Section C: True or False (X marks each, X marks total)

**Instructions: Mark ✓ for correct, ✗ for incorrect and briefly explain why.**

**5.** 【Statement】（  ）

**6.** 【Statement】（  ）

---

## Section D: Define the Following Terms (X marks each, X marks total)

**7.** 【Term 1】

**8.** 【Term 2】

---

## Section E: Short Answer (X marks each, X marks total)

**9.** 【Question】

---

**10.** 【Question】

---

## Section F: Calculation / Analysis / Essay (X marks each, X marks total)

**11.** 【Question with specific data / case / material】

---

**12.** 【Question with specific data / case / material】

---

## Section G: Comprehensive Application (X marks total)

**13.** 【Question with full context / background material】

---

**【END OF EXAM】Please review all your answers carefully.**

---

# Answer Key and Scoring Rubric

**Course Name: 【Course Name】**

**Paper Version: A**

---

## Section A: Multiple Choice Answers

| Question | Answer | Explanation |
| --- | --- | --- |
| 1 | X | 【Brief explanation: why X is correct, why others are wrong】 |
| 2 | X | 【Brief explanation】 |

---

## Section B: Fill in the Blanks Answers

**3.** 【Standard answer】

**【Explanation】** 【Solution approach and key points】

---

**4.** 【Standard answer】

**【Explanation】** 【Solution approach and key points】

---

## Section C: True or False Answers

**5.** ✓ / ✗

**【Basis】** 【Reference to knowledge point or statute】

**【Explanation】** 【Why correct/incorrect】

---

## Section D: Term Definitions

**7.** 【Standard definition】

**【Scoring criteria】** Keyword "XX" (1 mark), core concept "XX" (1 mark), example (1 mark)

---

## Section E: Short Answer Solutions

### Question 9 (X marks)

**【Reference answer】**

【Point-by-point answer, each with marks】

**【Scoring rubric】**

| Criterion | Marks | Award when... |
| --- | ---: | --- |
| Point 1 | X | Accurately states... |
| Point 2 | X | Fully explains... |
| Point 3 | X | Correctly interprets... |

**【Common errors】**
- Error 1: ... (deduct X marks)
- Error 2: ... (deduct X marks)

---

## Section F: Calculation / Analysis / Essay Solutions

### Question 11 (X marks)

**【Solution process】**

1. 【Step 1】
   - Formula/basis: ...
   - Calculation/analysis: ...
   - Marks: X

2. 【Step 2】
   - ...

**【Final answer】** 【Result with units/format】

**【Scoring rubric】**

| Criterion | Marks | Award when... |
| --- | ---: | --- |
| Model/formula selection | X | Correctly identifies... |
| Calculation process | X | Complete steps, correct units... |
| Result interpretation | X | Reasonably explains meaning... |
| Answer presentation | X | Proper format, clear conclusion... |

**【Common errors】**
- Error 1: ... (deduct X marks)
- Error 2: ... (deduct X marks)

---

## Section G: Comprehensive Application Solutions

### Question 13 (X marks)

**【Reference answer】**

【Complete, structured answer】

**【Scoring rubric】**

| Criterion | Marks | Award when... |
| --- | ---: | --- |
| Analytical framework | X | Correctly applies... |
| Evidence use | X | Adequately cites... |
| Logical reasoning | X | Rigorous reasoning,充分 argumentation... |
| Conclusion quality | X | Reasonable conclusion, depth... |

**【Partial credit notes】**
- Partial points only: award proportionally
- Correct framework but incomplete content: award framework marks
- Creative but off-topic: award at discretion

---

## Post-Exam Diagnosis

### By chapter

| Chapter | Questions | Marks | Score suggestion | Mastery level |
| --- | --- | ---: | --- | --- |
| Ch 1 | Q1, Q3, Q9 | 15 | ... | Mastered / Review / Weak |
| Ch 2 | Q2, Q5, Q11 | 20 | ... | Mastered / Review / Weak |

### By cognitive level

| Level | Questions | Marks | Recommendation |
| --- | --- | ---: | --- |
| Recall/Recognition | Q1-Q4 | 15 | ... |
| Understanding | Q5-Q8 | 20 | ... |
| Application/Analysis | Q9-Q12 | 35 | ... |
| Synthesis/Evaluation | Q13 | 20 | ... |

### Weak-point repair suggestions

1. **【Weak point 1】**: Review 【specific chapter/knowledge】, redo 【related questions】.
2. **【Weak point 2】**: Create 【comparison table/flowchart】, strengthen 【specific skill】.
3. **【Weak point 3】**: Retest after 【X days】 interval.
```

## Discipline-specific exam adjustments

### Computer Science / Engineering

- MCQ: concept discrimination, algorithm complexity, protocol steps
- Fill-in: formula parameters, algorithm steps, data structure properties
- Calculation: time complexity, circuit analysis, SQL queries
- Code: complete code, debug errors, design algorithms
- Design: system architecture, database design, algorithm selection

### Natural Sciences / Mathematics

- MCQ: concept judgment, formula applicability conditions
- Fill-in: formula derivation, theorem conditions
- Proof: theorem proofs, inequality derivations
- Calculation: formula substitution, numerical computation
- Experiment: data interpretation, experiment design

### Medicine / Health

- MCQ: disease features, drug mechanisms, test selection
- Fill-in: anatomy structures, lab values, diagnostic criteria
- Case: full case analysis, clinical reasoning
- Mechanism: pathophysiological processes, drug action mechanisms
- Public health: epidemiological indicator calculation, interventions

### Law

- MCQ: legal concepts, element judgment
- Fill-in: statutory keywords, legal elements
- Case analysis: issue spotting, IRAC application
- Statute interpretation: provision meaning, scope of application
- Essay: legal principle evaluation, policy analysis

### Humanities

- MCQ: concept discrimination, background knowledge
- Fill-in: key terms, dates/figures
- Short answer: concept explanation, comparative analysis
- Close reading: text/image analysis
- Essay: argumentative essay, comparative study

### Social Sciences

- MCQ: theory judgment, concept discrimination
- Fill-in: theorists, core concepts
- Short answer: theory comparison, concept explanation
- Case analysis: theory application, policy analysis
- Methods: research design, validity analysis

### Business / Economics

- MCQ: concept judgment, framework applicability
- Fill-in: formulas, ratio definitions
- Calculation: NPV, ratios, elasticity
- Graph analysis: supply-demand curves, equilibrium changes
- Case analysis: business diagnosis, strategic recommendations

### Education / Arts / Design

- MCQ: theory judgment, principle application
- Fill-in: key terms, theorists
- Lesson plan analysis: instructional design evaluation
- Design critique: work analysis, improvement suggestions
- Reflection writing: experience → theory → improvement

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
- Exam format is unified and professional.
- Answer key question numbers match the exam paper one-to-one.
- Scoring criteria are operational and quantifiable.

## Generating DOCX mock exams

Use the following workflow to generate standardized mock exam DOCX files:

### Step 1: Generate JSON data

Organize the mock exam data in this format:

```json
{
  "metadata": {
    "course": "Course Name",
    "exam_title": "Final Mock Examination",
    "duration": "120 minutes",
    "total_marks": 100,
    "mode": "Closed-book",
    "orientation": "landscape",
    "version": "A",
    "header": "Header text",
    "footer": "Footer text",
    "instructions": ["Instruction 1", "Instruction 2"]
  },
  "sections": [
    {
      "title": "Section A: Multiple Choice",
      "description": "Select the single best answer",
      "total_marks": 20,
      "page_break_before": true,
      "questions": [...]
    }
  ],
  "answers": [...],
  "diagnosis": {...}
}
```

### metadata field reference

| Field | Required | Description |
| --- | --- | --- |
| course | Yes | Course name |
| exam_title | No | Exam title, default "Final Mock Examination" |
| duration | Yes | Exam duration |
| total_marks | Yes | Total marks |
| mode | No | Exam mode: Closed-book / Open-book |
| orientation | No | Page orientation: landscape or portrait, default landscape |
| version | No | Paper version, default A |
| header | No | Header text |
| footer | No | Footer text |
| instructions | No | List of instructions |

### sections field reference

Each section contains:

| Field | Required | Description |
| --- | --- | --- |
| title | Yes | Section title, e.g., "Section A: Multiple Choice" |
| description | No | Section instructions |
| total_marks | Yes | Total marks for this section |
| page_break_before | No | Page break before this section, default true |
| questions | Yes | List of questions |

### questions field reference

Each question contains:

| Field | Required | Description |
| --- | --- | --- |
| number | Yes | Question number |
| type | No | Question type: MCQ / Fill-in / True-false / Definition / Short answer / Calculation / Analysis / Comprehensive |
| text | Yes | Question stem |
| marks | Yes | Marks |
| time | No | Expected time |
| options | No | List of options for MCQ |
| sub_questions | No | List of sub-questions |
| answer_lines | No | Number of blank answer lines |
| page_break_before | No | Force page break before this question |

### Step 2: Run the script to generate DOCX

```bash
python scripts/generate_mock_exam_docx.py \
  --input examples/mock_exam_os.sample.json \
  --output output/mock_exam_os.docx
```

### Page layout

- **Landscape**: Page width 29.7cm, height 21.0cm. Suitable for exams with many MCQs and long question stems.
- **Portrait**: Page width 21.0cm, height 29.7cm. Suitable for exams with many short-answer and essay questions.

### Page break rules

- Automatic page break before each section.
- Question headers and stems use keep_with_next to prevent splitting across pages.
- Options use keep_with_next to keep them together.
- Answer section and diagnosis section have automatic page breaks.

### Sample files

- JSON example: `examples/mock_exam_os.sample.json`
- Generation script: `scripts/generate_mock_exam_docx.py`

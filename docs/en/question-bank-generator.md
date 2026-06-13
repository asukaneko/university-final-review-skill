# Question Bank Generator

Use this module to generate chapter practice questions, test cards, diagnostic exercises, and exam-style questions from course materials.

For active recall flashcards, also use [`test-cards.md`](test-cards.md). For complete mock exams, also use [`precision-mock-exam.md`](precision-mock-exam.md).

## Question bank layers

A complete question bank should contain four layers:

1. **Basic recall**: Definitions, terms, formulas, rules, dates, figures, components.
2. **Conceptual understanding**: Explain mechanisms, compare concepts, interpret diagrams, identify assumptions.
3. **Application and process**: Calculation, algorithm, case, proof, data interpretation, legal application, design critique.
4. **Synthesis and transfer**: Cross-chapter questions, unfamiliar scenarios, high-value comprehensive questions.

## Required question types

Each chapter should include appropriate question types based on the discipline:

- Single-choice MCQ;
- Multiple-choice when appropriate;
- True/false with correction;
- Fill-in-the-blank or cloze;
- Term definition and concept comparison;
- Short-answer explanation;
- Calculation, proof, algorithm, code, experiment, or data questions;
- Case, clinical, legal, business, policy, essay, design, or critique questions;
- Error-correction questions;
- Transfer questions.

## Standard question type formats

When generating the question bank, use the following unified format for each question type:

### Multiple choice format

```markdown
**QN-01** [Basic | 2 min | Topic | X marks]

【Question stem】（  ）

A. 【Option A】

B. 【Option B】

C. 【Option C】

D. 【Option D】

**Answer:** X

**Explanation:** 【Brief explanation: why X is correct, why others are wrong】

**Common errors:** 【Why students commonly choose wrong options】

**Review tip:** 【One-sentence memory aid】
```

### Fill-in-the-blank format

```markdown
**QN-02** [Basic | 1 min | Topic | X marks]

【Question stem with ______ blanks】.

**Answer:** 【Standard answer】

**Explanation:** 【Solution approach and key points】

**Common errors:** 【Common incorrect answers】

**Review tip:** 【One-sentence memory aid】
```

### True/false format

```markdown
**QN-03** [Basic | 1 min | Topic | X marks]

【Statement】（  ）

**Answer:** ✓ / ✗

**Basis:** 【Reference to knowledge point or statute】

**Explanation:** 【Why correct/incorrect】

**Common errors:** 【Common misjudgments and reasons】

**Review tip:** 【One-sentence memory aid】
```

### Term definition format

```markdown
**QN-04** [Basic | 3 min | Topic | X marks]

**【Term name】**

**Answer:** 【Standard definition, 2-4 sentences】

**Scoring criteria:** Keyword "XX" (X marks), core concept "XX" (X marks), example (X marks)

**Common errors:** 【Incomplete definition, missing key elements】

**Review tip:** 【Memory mnemonic or keywords】
```

### Short answer format

```markdown
**QN-05** [Standard | 5 min | Topic | X marks]

**【Question】**

**Reference answer:**

1. 【Point 1】 (X marks)
2. 【Point 2】 (X marks)
3. 【Point 3】 (X marks)

**Scoring rubric:**

| Criterion | Marks | Award when... |
| --- | ---: | --- |
| Point 1 | X | Accurately states... |
| Point 2 | X | Fully explains... |
| Point 3 | X | Correctly interprets... |

**Common errors:**
- Error 1: ... (deduct X marks)
- Error 2: ... (deduct X marks)

**Review tip:** 【Answer framework or keywords】
```

### Calculation/Analysis format

```markdown
**QN-06** [Comprehensive | 10 min | Topic | X marks]

**【Question with specific data / case / material】**

**Solution process:**

1. 【Step 1】
   - Formula/basis: ...
   - Calculation/analysis: ...
   - Marks: X

2. 【Step 2】
   - ...

**Final answer:** 【Result with units/format】

**Scoring rubric:**

| Criterion | Marks | Award when... |
| --- | ---: | --- |
| Model/formula selection | X | Correctly identifies... |
| Calculation process | X | Complete steps, correct units... |
| Result interpretation | X | Reasonably explains meaning... |
| Answer presentation | X | Proper format, clear conclusion... |

**Common errors:**
- Error 1: ... (deduct X marks)
- Error 2: ... (deduct X marks)

**Review tip:** 【Key problem-solving steps】
```

### Case/Essay format

```markdown
**QN-07** [Transfer | 15 min | Topic | X marks]

**【Full case / material context】**

**【Question requirements】**

**Reference answer:**

【Complete, structured answer】

**Scoring rubric:**

| Criterion | Marks | Award when... |
| --- | ---: | --- |
| Analytical framework | X | Correctly applies... |
| Evidence use | X | Adequately cites... |
| Logical reasoning | X | Rigorous reasoning... |
| Conclusion quality | X | Reasonable conclusion... |

**Partial credit notes:**
- Partial points only: award proportionally
- Correct framework but incomplete content: award framework marks
- Creative but off-topic: award at discretion

**Common errors:**
- Error 1: ... (deduct X marks)
- Error 2: ... (deduct X marks)

**Review tip:** 【Answer framework and key elements】
```

## Required metadata per question

Each question should include:

- Question ID;
- Chapter and topic;
- Intended learning outcome;
- Question type;
- Difficulty level (Basic / Standard / Comprehensive / Transfer);
- Expected time;
- Marks (for exam questions);
- Correct answer;
- Detailed explanation;
- Scoring rubric (for short-answer and above);
- Source basis: from uploaded materials / inferred from materials / supplementary background;
- Common errors;
- Review tip;
- Follow-up review card when appropriate.

## Difficulty levels

Use four tiers:

1. **Basic**: Direct recall or one-step recognition.
2. **Standard**: Standard explanation or routine application.
3. **Comprehensive**: Multi-step reasoning or cross-chapter connection.
4. **Transfer**: Unfamiliar scenario, condition change, or synthesis judgment.

## Per-chapter quantity suggestions

For a typical chapter, generate:

- 5-8 basic recall questions;
- 5-8 conceptual understanding questions;
- 4-6 application/process questions;
- 2-4 synthesis/transfer questions;
- 8-25 test cards, adjusted by chapter density.

Increase the ratio of application and transfer questions for exam-heavy chapters.

## Answer quality requirements

Answers should demonstrate:

- Final answer;
- Reasoning path;
- Why this method/rule applies;
- Why common alternative answers are wrong;
- Partial credit points when relevant;
- A one-sentence review tip for memorization.

## Output format

```markdown
## Chapter N Question Bank

### Blueprint

| Topic | Weight | Question type | Difficulty focus |
| --- | ---: | --- | --- |

### Basic recall questions

#### QN-01 [Basic | 2 min | Topic | X marks]

**Question type:** MCQ / Fill-in / True-false / Definition

【Question stem...】

**Answer:** ...

**Explanation:** ...

**Common errors:** ...

**Review tip:** ...

### Conceptual understanding questions

#### QN-06 [Standard | 5 min | Topic | X marks]

**Question type:** Short answer / Comparison / Explanation

【Question stem...】

**Reference answer:** ...

**Scoring rubric:** ...

**Common errors:** ...

**Review tip:** ...

### Application/process questions

#### QN-11 [Comprehensive | 10 min | Topic | X marks]

**Question type:** Calculation / Analysis / Proof / Case

【Question stem...】

**Solution process:** ...

**Final answer:** ...

**Scoring rubric:** ...

**Common errors:** ...

**Review tip:** ...

### Synthesis/transfer questions

#### QN-15 [Transfer | 15 min | Topic | X marks]

**Question type:** Comprehensive / Design / Essay

【Question stem...】

**Reference answer:** ...

**Scoring rubric:** ...

**Common errors:** ...

**Review tip:** ...
```

## Connection to mock exams

If the user requests a mock exam, do not randomly select questions. Follow [`precision-mock-exam.md`](precision-mock-exam.md) to first create a blueprint, then allocate marks by chapter weight, balance cognitive levels, and provide scoring rubrics.

Questions in the mock exam should be selected from the question bank according to the blueprint, or newly created following the question bank format standards. Ensure:
- Sequential question numbers with no gaps;
- Reasonable mark allocation;
- Comprehensive question type coverage;
- Appropriate difficulty gradient.

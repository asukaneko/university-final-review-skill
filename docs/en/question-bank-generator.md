# Question Bank Generator

Use this module to create chapter practice questions, test cards, diagnostic drills, and exam-style mock questions from course materials.

For active-recall flashcards, also use [`test-cards.md`](test-cards.md). For full mock exams, also use [`precision-mock-exam.md`](precision-mock-exam.md).

## Question-bank layers

A complete question bank should include four layers:

1. **Basic recall**: definitions, terms, formulas, rules, dates, people, components.
2. **Conceptual understanding**: explain mechanisms, compare concepts, interpret diagrams, identify assumptions.
3. **Application and procedure**: calculations, algorithms, cases, proofs, data interpretation, legal application, design critique.
4. **Integration and transfer**: mixed-topic questions, unfamiliar scenarios, high-value exam prompts.

## Required question types

For each chapter, choose question types that fit the discipline:

- single-choice questions;
- multiple-choice questions when appropriate;
- true / false with correction;
- fill-in-the-blank or cloze questions;
- definition and comparison questions;
- short-answer explanations;
- calculation, proof, algorithm, coding, lab, or data questions;
- case, clinical, legal, business, policy, essay, design, or critique questions;
- error-correction questions;
- transfer questions.

## Required metadata for each question

Each question should include:

- question ID;
- chapter and topic;
- related learning outcome;
- question type;
- difficulty level;
- expected time;
- marks if exam-style;
- correct answer;
- detailed explanation;
- source basis: uploaded material / inferred exam focus / supplementary background;
- common mistakes;
- follow-up review card when useful.

## Difficulty levels

Use four levels:

1. **Basic**: direct recall or one-step recognition.
2. **Common exam level**: standard explanation or routine application.
3. **Advanced / integrated**: multi-step reasoning or cross-chapter connection.
4. **Transfer**: unfamiliar case, changed condition, or synthesis.

## Chapter question mix

For a normal chapter, generate:

- 5-8 basic recall questions;
- 5-8 conceptual questions;
- 4-6 application/procedure questions;
- 2-4 integrated or transfer questions;
- 8-25 test cards depending on density.

For high-stakes or exam-heavy chapters, increase applied and transfer questions.

## Answer quality requirements

Answers should show:

- final answer;
- reasoning path;
- why the method/rule applies;
- why common alternatives are wrong;
- partial-credit points when relevant;
- a short review cue the student can remember.

## Output format

```markdown
## Chapter N Question Bank

### Blueprint

| Topic | Weight | Question types | Difficulty focus |
| --- | ---: | --- | --- |

### Questions

#### QN-01 [Basic | 2 min | Topic]
Question...

**Answer:** ...
**Explanation:** ...
**Common mistake:** ...
**Review cue:** ...
```

## Mock exam connection

When the user requests a mock exam, do not simply select random questions. Build the exam using [`precision-mock-exam.md`](precision-mock-exam.md): create a blueprint, assign marks by topic weight, balance cognitive level, and provide a marking rubric.

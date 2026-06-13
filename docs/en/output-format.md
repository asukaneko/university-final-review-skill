# Output Format

Output should use clear, study-friendly Markdown structure. If the user requests DOCX / Word output, also refer to the formatting guidelines in [`docx-style-guide.md`](docx-style-guide.md).

## Recommended chapter format

```markdown
## Chapter N: Title

### 1. Chapter Overview

### 2. Core Concepts

### 3. Key Mechanisms / Formulas / Algorithms

### 4. Exam Point Analysis

### 5. Common Question Types

### 6. Common Errors

### 7. One-Page Speed Notes

### 8. Practice Problems
```

## Table usage scenarios

The following content should use tables:

- Concept comparison
- Exam point priority ranking
- Question type mapping
- Formula summary
- Common error details
- Case analysis structure
- Clinical reasoning chains
- Legal elements
- Framework quick reference

## Mock exam format

A complete mock exam should include:

- Total score: 100 points
- Suggested time allocation
- Question type distribution
- Points per question
- Standard answers
- Scoring criteria

## DOCX output format

When generating DOCX, prefer these formatting elements:

- Centered course title and chapter title
- Header: course name, chapter name, or topic
- Footer: material type, page number, or "Study Notes & Exam Review"
- Light blue "Chapter Main Thread" box
- Learning objectives list
- Table of contents
- Dark blue header concept and exam point tables
- Light yellow "Note" box
- Light red "Common Errors" box
- Light gray formula, code, or example blocks
- Appropriate page breaks between chapters

See [`docx-style-guide.md`](docx-style-guide.md) for detailed visual specifications.

## Content labeling

When necessary, label content sources:

- `来自上传资料` / `From uploaded materials`
- `基于资料推测的考点` / `Exam points inferred from materials`
- `补充背景知识` / `Supplementary background`

## Complete review package

When the user requests "rich" or "complete" output, include:

1. Course and exam scope overview.
2. Discipline category and review strategy.
3. Evidence-based study plan with spaced repetition schedule.
4. Chapter-by-chapter deep notes.
5. High-yield exam point map.
6. Concept comparison tables, formula/rule summaries.
7. Chapter question bank with answers and explanations (4 difficulty levels).
8. Test cards for active recall, see [`test-cards.md`](test-cards.md).
9. Worked examples or model answers.
10. Error log and weak-point repair plan.
11. Precision 100-point mock exam, see [`precision-mock-exam.md`](precision-mock-exam.md).
12. Final sprint checklist with time allocation advice.

## Precision mock exam output

The mock exam should include:

- Exam blueprint table
- Total score and duration
- Section instructions
- Questions with points and estimated time
- Standard answers
- Detailed rubric
- Partial-credit notes
- Common traps
- Post-exam diagnosis by chapter and ability dimension

## Test card output

Test cards should be grouped by chapter and card type. Include ID, front, back, chapter, topic, difficulty, card type, and tags.

# Test Cards

Use test cards to turn review notes into compact, repeatable retrieval drills. A test card is not a summary card; it is a question-driven card that forces the student to recall, apply, compare, or explain.

## When to generate test cards

Generate test cards when the user asks for:

- flashcards;
- memory cards;
- active recall cards;
- Anki-style review material;
- quick review before an exam;
- a complete final-review package.

For a complete package, include test cards by default unless the user asks for a shorter output.

## Card types

Use a mix of the following card types.

### 1. Definition card

```markdown
**Front:** What is [concept]?
**Back:** [Precise definition] + [one example] + [one non-example or contrast].
**Tags:** chapter, concept, basic
```

### 2. Cloze deletion card

```markdown
**Prompt:** In [model/process], _____ causes _____ when _____.
**Answer:** [missing term or relation]
**Why it matters:** [exam relevance]
```

### 3. Compare-and-contrast card

```markdown
**Front:** Compare [A] and [B].
**Back:**
| Dimension | A | B |
| --- | --- | --- |
| Definition | ... | ... |
| Use case | ... | ... |
| Common exam trap | ... | ... |
```

### 4. Process / mechanism card

```markdown
**Front:** Explain the steps of [process/mechanism/algorithm].
**Back:**
1. ...
2. ...
3. ...
**Failure point:** [where students usually lose marks]
```

### 5. Formula / rule card

```markdown
**Front:** When and how do you use [formula/rule/test]?
**Back:**
- Formula/rule: ...
- Symbols/elements: ...
- Assumptions: ...
- Example use: ...
- Do not use when: ...
```

### 6. Application card

```markdown
**Front:** Given [mini case/problem], what should you do first and why?
**Back:** [Reasoned answer with first step, rule/model, and explanation]
```

### 7. Error-correction card

```markdown
**Front:** A student answered: "..." What is wrong?
**Back:** [Error diagnosis] → [correct reasoning] → [prevention cue]
```

### 8. Transfer card

```markdown
**Front:** How would [concept/method] change if [condition changes]?
**Back:** [Transfer reasoning and changed conclusion]
```

## Discipline-specific card guidance

- **STEM / engineering:** formula cards, algorithm tracing cards, debugging cards, unit-check cards, design trade-off cards.
- **Natural sciences / mathematics:** theorem-condition cards, proof-step cards, graph interpretation cards, experiment-control cards.
- **Medicine / health:** disease script cards, drug safety cards, red-flag cards, lab interpretation cards, clinical reasoning cards.
- **Law:** rule element cards, case holding cards, issue-trigger cards, IRAC application cards, counterargument cards.
- **Humanities:** thesis cards, evidence cards, quotation-analysis cards, chronology cards, interpretation debate cards.
- **Social sciences:** theory cards, method-validity cards, variable-measurement cards, case application cards, critique cards.
- **Business / economics:** framework selection cards, calculation setup cards, graph-shift cards, ratio interpretation cards, case recommendation cards.
- **Education / arts / design:** principle-example cards, critique vocabulary cards, lesson-plan cards, portfolio evidence cards, reflection cards.

## Card quality rules

A good test card should:

- test one main idea;
- be answerable without opening the notes;
- include a short explanation, not only a keyword;
- include contrast, example, or trap when useful;
- be tagged by chapter, topic, difficulty, and card type;
- avoid vague prompts such as “Explain chapter 3”.

## Recommended output format

```markdown
## Test Cards: Chapter N

### Basic recall cards

| ID | Front | Back | Tags |
| --- | --- | --- | --- |
| C1-01 | ... | ... | ch1;definition;basic |

### Application cards

| ID | Front | Back | Tags |
| --- | --- | --- | --- |
| C1-08 | ... | ... | ch1;application;exam |

### Error-correction cards

| ID | Front | Back | Tags |
| --- | --- | --- | --- |
| C1-13 | ... | ... | ch1;mistake;transfer |
```

## Quantity guidance

For each chapter:

- short chapter: 8-12 cards;
- normal chapter: 15-25 cards;
- dense exam-heavy chapter: 30-45 cards;
- final sprint set: 50-120 cards across the whole course, prioritized by exam likelihood and student weakness.

## Export guidance

When the user asks for Anki/CSV style output, use columns:

```text
ID,Front,Back,Chapter,Topic,Difficulty,CardType,Tags
```

## Generate an HTML review interface

The repository includes a zero-dependency script that converts a test-card CSV file into a standalone HTML review interface:

```bash
python scripts/generate_test_cards_html.py \
  --input examples/test_cards.sample.csv \
  --output output/test_cards.html \
  --title "University Final Review Test Cards" \
  --language en
```

The generated HTML works offline and can be shared directly with students.

### Supported CSV columns

Recommended columns:

```text
ID,Front,Back,Chapter,Topic,Difficulty,CardType,Tags
```

The script also supports common aliases, including lowercase headers and Chinese headers:

- `正面` → `Front`
- `背面` / `答案` / `解析` → `Back`
- `章节` → `Chapter`
- `主题` / `知识点` → `Topic`
- `难度` → `Difficulty`
- `卡片类型` / `类型` → `CardType`
- `标签` → `Tags`

### HTML interface features

- Search front, back, topic, and tags.
- Filter by chapter, difficulty, and card type.
- Flip cards to reveal answers.
- Use `1/2/3/4` to mark Again / Hard / Good / Easy; after rating, the current card shows the corresponding color, status badge, and selected button. Choosing Again stays on the current card and flips to the answer side for immediate review.
- Track reviews, mastery score, and last-reviewed time; the side list also shows each card's answer status.
- Weak-card-only review mode.
- Shuffle mode.
- Export progress as CSV.
- Save progress in browser `localStorage`.
- Keyboard shortcuts: space to flip, arrow keys to navigate.

### Recommended workflow

For a complete review package:

1. Generate chapter-based test cards as CSV.
2. Keep one main knowledge point per card.
3. Tag every card with chapter, topic, difficulty, type, and tags.
4. Generate the HTML interface with `generate_test_cards_html.py`.
5. Ask students to review all cards once, then use weak-card-only mode for the second round.

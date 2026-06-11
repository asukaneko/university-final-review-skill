# University Final Review Skill

A bilingual, cross-disciplinary AI skill for turning university course materials into structured final-exam review resources.

This repository provides a reusable skill workflow for students who need to transform PPT slides, lecture notes, assignments, syllabus documents, screenshots, lab materials, case materials, or past papers into exam-oriented study materials.

It is designed for a broad range of university disciplines:

- Computer Science and Engineering
- Natural Sciences and Mathematics
- Medicine, Nursing, Pharmacy, and Public Health
- Law and Legal Studies
- Humanities: history, philosophy, literature, languages
- Social Sciences: politics, sociology, psychology, communication
- Business, Economics, Accounting, and Management
- Education, Arts, Design, and General Education courses

## What it generates

The skill can generate:

- Deep chapter-by-chapter lecture notes
- Exam point prediction
- Question banks with answers and explanations
- Memorization outlines
- Discipline-specific problem-solving and analysis templates
- Calculation, proof, experiment, case-analysis, clinical-reasoning, essay-planning, or design-critique walkthroughs
- Polished DOCX / Word review handouts
- Final sprint checklists
- Full mock exams with scoring rubrics

## Repository layout

```text
.
├── SKILL.md
├── README.md
├── requirements.txt
├── docs/
│   ├── en/
│   │   ├── README.md
│   │   ├── categories/
│   │   │   ├── README.md
│   │   │   ├── stem-engineering.md
│   │   │   ├── natural-sciences.md
│   │   │   ├── medicine-health.md
│   │   │   ├── law.md
│   │   │   ├── humanities.md
│   │   │   ├── social-sciences.md
│   │   │   ├── business-economics.md
│   │   │   └── education-arts.md
│   │   ├── overall-workflow.md
│   │   ├── deep-lecture-notes.md
│   │   ├── exam-point-predictor.md
│   │   ├── question-bank-generator.md
│   │   ├── memorization-outline.md
│   │   ├── problem-solving-coach.md
│   │   ├── docx-style-guide.md
│   │   └── output-format.md
│   └── zh-CN/
│       ├── README.md
│       ├── categories/
│       │   ├── README.md
│       │   ├── stem-engineering.md
│       │   ├── natural-sciences.md
│       │   ├── medicine-health.md
│       │   ├── law.md
│       │   ├── humanities.md
│       │   ├── social-sciences.md
│       │   ├── business-economics.md
│       │   └── education-arts.md
│       ├── overall-workflow.md
│       ├── deep-lecture-notes.md
│       ├── exam-point-predictor.md
│       ├── question-bank-generator.md
│       ├── memorization-outline.md
│       ├── problem-solving-coach.md
│       ├── docx-style-guide.md
│       └── output-format.md
├── assets/templates/
│   └── final-review-request.md
├── examples/
│   └── review_content.sample.json
├── scripts/
│   ├── generate_styled_docx.py
│   ├── build_review_plan.py
│   ├── package_skill.py
│   └── validate_skill.py
└── .github/workflows/
    └── validate.yml
```

## Languages

- English documentation: [`docs/en/README.md`](docs/en/README.md)
- 中文文档：[`docs/zh-CN/README.md`](docs/zh-CN/README.md)

## Discipline categories

| Category | English | 中文 |
| --- | --- | --- |
| Computer Science / Engineering | [`docs/en/categories/stem-engineering.md`](docs/en/categories/stem-engineering.md) | [`docs/zh-CN/categories/stem-engineering.md`](docs/zh-CN/categories/stem-engineering.md) |
| Natural Sciences / Mathematics | [`docs/en/categories/natural-sciences.md`](docs/en/categories/natural-sciences.md) | [`docs/zh-CN/categories/natural-sciences.md`](docs/zh-CN/categories/natural-sciences.md) |
| Medicine / Health | [`docs/en/categories/medicine-health.md`](docs/en/categories/medicine-health.md) | [`docs/zh-CN/categories/medicine-health.md`](docs/zh-CN/categories/medicine-health.md) |
| Law | [`docs/en/categories/law.md`](docs/en/categories/law.md) | [`docs/zh-CN/categories/law.md`](docs/zh-CN/categories/law.md) |
| Humanities | [`docs/en/categories/humanities.md`](docs/en/categories/humanities.md) | [`docs/zh-CN/categories/humanities.md`](docs/zh-CN/categories/humanities.md) |
| Social Sciences | [`docs/en/categories/social-sciences.md`](docs/en/categories/social-sciences.md) | [`docs/zh-CN/categories/social-sciences.md`](docs/zh-CN/categories/social-sciences.md) |
| Business / Economics | [`docs/en/categories/business-economics.md`](docs/en/categories/business-economics.md) | [`docs/zh-CN/categories/business-economics.md`](docs/zh-CN/categories/business-economics.md) |
| Education / Arts / Design | [`docs/en/categories/education-arts.md`](docs/en/categories/education-arts.md) | [`docs/zh-CN/categories/education-arts.md`](docs/zh-CN/categories/education-arts.md) |

## Basic usage

Copy this repository into a supported skill directory, or keep it as a reusable prompt/skill library.

Example request:

```text
Use the university final review skill. Identify the discipline category from the uploaded Chapter 1-5 materials and generate detailed final-exam review notes, exam points, a question bank, memorization outlines, discipline-specific problem-solving templates, a polished DOCX handout, and a 100-point mock exam.
```

For Chinese courses:

```text
请使用大学期末复习 Skill，查看我上传的第 1-5 章资料，先判断学科大类，再生成详细复习资料，包括逐章讲义、考点预测、题库、背诵提纲、学科专属解题/分析模板、一份排版美观的 DOCX 文档和一套 100 分模拟卷。
```

## Skill modules

| Module | Purpose |
| --- | --- |
| Overall Workflow | Converts raw course materials into a complete review pipeline. |
| Discipline Categories | Applies discipline-specific review patterns. |
| Deep Lecture Notes | Produces detailed chapter-by-chapter notes. |
| Exam Point Predictor | Estimates likely exam topics and question forms. |
| Question Bank Generator | Creates questions, answers, explanations, and rubrics. |
| Memorization Outline | Produces compact material for recitation and last-minute review. |
| Problem-Solving Coach | Provides discipline-specific reasoning templates for calculation, proof, experiment analysis, legal cases, clinical reasoning, essays, business cases, and design critique. |
| DOCX Style Guide | Defines polished Word-document formatting for printable review handouts. |
| Styled DOCX Generator | Converts structured review JSON into a styled Word handout using `python-docx`. |

## Scripts

Install the DOCX generator dependency:

```bash
pip install -r requirements.txt
```

Generate a styled DOCX handout from the sample JSON:

```bash
python scripts/generate_styled_docx.py --input examples/review_content.sample.json --output output/final_review.docx
```

Validate the repository structure:

```bash
python scripts/validate_skill.py
```

Build a simple review plan:

```bash
python scripts/build_review_plan.py --course "Operating Systems" --chapters "1-5" --language zh-CN
```

Package the skill into a zip file:

```bash
python scripts/package_skill.py
```

## License

MIT License.

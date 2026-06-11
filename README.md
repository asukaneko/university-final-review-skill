# University Final Review Skill

A bilingual AI skill for turning university course materials into structured final-exam review resources.

This repository provides a reusable skill workflow for students who need to transform PPT slides, lecture notes, assignments, syllabus documents, screenshots, or past papers into exam-oriented study materials.

It is designed for courses such as:

- Computer Science fundamentals
- Operating Systems
- Algorithms and Data Structures
- Database Systems
- Computer Networks
- Software Engineering
- Political theory / history / general education courses
- Any lecture-based university course with slides or notes

## What it generates

The skill can generate:

- Deep chapter-by-chapter lecture notes
- Exam point prediction
- Question banks with answers and explanations
- Memorization outlines
- Calculation / algorithm problem walkthroughs
- Final sprint checklists
- Full mock exams with scoring rubrics

## Repository layout

```text
.
├── SKILL.md
├── README.md
├── docs/
│   ├── en/
│   │   ├── README.md
│   │   ├── overall-workflow.md
│   │   ├── deep-lecture-notes.md
│   │   ├── exam-point-predictor.md
│   │   ├── question-bank-generator.md
│   │   ├── memorization-outline.md
│   │   ├── calculation-algorithm-coach.md
│   │   └── output-format.md
│   └── zh-CN/
│       ├── README.md
│       ├── overall-workflow.md
│       ├── deep-lecture-notes.md
│       ├── exam-point-predictor.md
│       ├── question-bank-generator.md
│       ├── memorization-outline.md
│       ├── calculation-algorithm-coach.md
│       └── output-format.md
├── assets/templates/
│   └── final-review-request.md
├── scripts/
│   ├── build_review_plan.py
│   ├── package_skill.py
│   └── validate_skill.py
└── .github/workflows/
    └── validate.yml
```

## Languages

- English documentation: [`docs/en/README.md`](docs/en/README.md)
- 中文文档：[`docs/zh-CN/README.md`](docs/zh-CN/README.md)

## Basic usage

Copy this repository into a supported skill directory, or keep it as a reusable prompt/skill library.

Example request:

```text
Use the university final review skill. Read the uploaded Chapter 1-5 slides and generate detailed final-exam review notes, exam points, a question bank, memorization outlines, and a 100-point mock exam.
```

For Chinese courses:

```text
请使用大学期末复习 Skill，查看我上传的第 1-5 章 PPT，生成详细复习资料，包括逐章讲义、考点预测、题库、背诵提纲和一套 100 分模拟卷。
```

## Skill modules

| Module | Purpose |
| --- | --- |
| Overall Workflow | Converts raw course materials into a complete review pipeline. |
| Deep Lecture Notes | Produces detailed chapter-by-chapter notes. |
| Exam Point Predictor | Estimates likely exam topics and question forms. |
| Question Bank Generator | Creates questions, answers, explanations, and rubrics. |
| Memorization Outline | Produces compact material for recitation and last-minute review. |
| Calculation / Algorithm Coach | Explains calculation, scheduling, database, network, and algorithm problems step by step. |

## Scripts

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

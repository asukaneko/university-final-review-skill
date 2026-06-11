#!/usr/bin/env python3
"""Validate the University Final Review Skill repository structure."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

CORE_FILES = [
    "SKILL.md",
    "README.md",
    "requirements.txt",
    "docs/en/README.md",
    "docs/en/overall-workflow.md",
    "docs/en/deep-lecture-notes.md",
    "docs/en/exam-point-predictor.md",
    "docs/en/question-bank-generator.md",
    "docs/en/memorization-outline.md",
    "docs/en/problem-solving-coach.md",
    "docs/en/output-format.md",
    "docs/en/docx-style-guide.md",
    "docs/zh-CN/README.md",
    "docs/zh-CN/overall-workflow.md",
    "docs/zh-CN/deep-lecture-notes.md",
    "docs/zh-CN/exam-point-predictor.md",
    "docs/zh-CN/question-bank-generator.md",
    "docs/zh-CN/memorization-outline.md",
    "docs/zh-CN/problem-solving-coach.md",
    "docs/zh-CN/output-format.md",
    "docs/zh-CN/docx-style-guide.md",
    "assets/templates/final-review-request.md",
    "examples/review_content.sample.json",
    "scripts/generate_styled_docx.py",
]

REMOVED_FILES = [
    "docs/en/calculation-algorithm-coach.md",
    "docs/zh-CN/calculation-algorithm-coach.md",
]

CATEGORY_FILES = [
    "categories/README.md",
    "categories/stem-engineering.md",
    "categories/natural-sciences.md",
    "categories/medicine-health.md",
    "categories/law.md",
    "categories/humanities.md",
    "categories/social-sciences.md",
    "categories/business-economics.md",
    "categories/education-arts.md",
]

REQUIRED_FILES = CORE_FILES + [f"docs/en/{path}" for path in CATEGORY_FILES] + [f"docs/zh-CN/{path}" for path in CATEGORY_FILES]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1

    stale = [path for path in REMOVED_FILES if (ROOT / path).exists()]
    if stale:
        print("Stale files should be removed:")
        for path in stale:
            print(f"- {path}")
        return 1

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8")

    required_skill_terms = [
        "name:",
        "description:",
        "University Final Review",
        "Supported discipline categories",
        "docs/en/categories/README.md",
        "docs/zh-CN/categories/README.md",
        "docs/en/problem-solving-coach.md",
        "docs/zh-CN/problem-solving-coach.md",
        "docs/en/docx-style-guide.md",
        "docs/zh-CN/docx-style-guide.md",
    ]
    absent = [term for term in required_skill_terms if term not in skill]
    if absent:
        print("SKILL.md is missing required terms:")
        for term in absent:
            print(f"- {term}")
        return 1

    required_readme_terms = [
        "generate_styled_docx.py",
        "review_content.sample.json",
        "python-docx",
        "Styled DOCX Generator",
    ]
    absent_readme = [term for term in required_readme_terms if term not in readme]
    if absent_readme:
        print("README.md is missing required terms:")
        for term in absent_readme:
            print(f"- {term}")
        return 1

    if "python-docx" not in requirements:
        print("requirements.txt must include python-docx")
        return 1

    forbidden_terms = [
        "calculation-algorithm-coach.md",
        "Calculation / Algorithm Coach",
        "计算题 / 算法题教练",
    ]
    forbidden_hits = [term for term in forbidden_terms if term in skill]
    if forbidden_hits:
        print("SKILL.md contains stale terms:")
        for term in forbidden_hits:
            print(f"- {term}")
        return 1

    print("Skill structure is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

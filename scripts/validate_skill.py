#!/usr/bin/env python3
"""Validate the University Final Review Skill repository structure."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "docs/en/README.md",
    "docs/en/overall-workflow.md",
    "docs/en/deep-lecture-notes.md",
    "docs/en/exam-point-predictor.md",
    "docs/en/question-bank-generator.md",
    "docs/en/memorization-outline.md",
    "docs/en/calculation-algorithm-coach.md",
    "docs/en/output-format.md",
    "docs/zh-CN/README.md",
    "docs/zh-CN/overall-workflow.md",
    "docs/zh-CN/deep-lecture-notes.md",
    "docs/zh-CN/exam-point-predictor.md",
    "docs/zh-CN/question-bank-generator.md",
    "docs/zh-CN/memorization-outline.md",
    "docs/zh-CN/calculation-algorithm-coach.md",
    "docs/zh-CN/output-format.md",
    "assets/templates/final-review-request.md",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    required_terms = ["name:", "description:", "University Final Review"]
    absent = [term for term in required_terms if term not in skill]
    if absent:
        print("SKILL.md is missing required terms:")
        for term in absent:
            print(f"- {term}")
        return 1

    print("Skill structure is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

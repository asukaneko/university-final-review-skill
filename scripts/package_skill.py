#!/usr/bin/env python3
"""Package the skill repository as a zip archive."""

from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "university-final-review-skill.zip"
EXCLUDED_DIRS = {".git", "__pycache__"}
EXCLUDED_FILES = {OUTPUT.name}


def should_include(path: Path) -> bool:
    rel_parts = path.relative_to(ROOT).parts
    if any(part in EXCLUDED_DIRS for part in rel_parts):
        return False
    if path.name in EXCLUDED_FILES:
        return False
    return path.is_file()


def main() -> None:
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in ROOT.rglob("*"):
            if should_include(path):
                zf.write(path, path.relative_to(ROOT))
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()

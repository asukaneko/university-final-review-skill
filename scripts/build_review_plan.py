#!/usr/bin/env python3
"""Generate a simple final-review plan prompt."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a final review plan request.")
    parser.add_argument("--course", required=True, help="Course name")
    parser.add_argument("--chapters", required=True, help="Chapter range, for example 1-5")
    parser.add_argument("--language", default="en", choices=["en", "zh-CN"], help="Output language")
    args = parser.parse_args()

    if args.language == "zh-CN":
        print(f"请使用大学期末复习 Skill，为《{args.course}》第 {args.chapters} 章生成完整期末复习资料。")
        print("要求包括：逐章深度讲义、考点预测、题库、背诵提纲、计算/算法题步骤，以及一套 100 分模拟卷。")
    else:
        print(f"Use the university final review skill for {args.course}, Chapters {args.chapters}.")
        print("Include deep notes, exam point prediction, question bank, memorization outline, worked problem steps, and a 100-point mock exam.")


if __name__ == "__main__":
    main()

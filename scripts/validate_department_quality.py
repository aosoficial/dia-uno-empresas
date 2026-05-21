#!/usr/bin/env python3
"""Validate department brains have enough operating depth.

Checks generated private instances or the template directory. No external calls.
"""
from __future__ import annotations

import sys
from pathlib import Path

QUALITY_MARKERS = [
    "Mission",
    "Memory fields",
    "Scorecard",
    "Weekly cadence",
    "Approval boundaries",
    "Day-1 task",
]
RECEIPT_MARKERS = ["Required receipts", "Expected receipts"]

MIN_WORDS = 220


def department_dirs(root: Path) -> list[Path]:
    departments = root / "departments"
    if not departments.exists():
        return []
    return sorted(p for p in departments.iterdir() if p.is_dir())


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    dirs = department_dirs(root)
    if not dirs:
        return [f"No departments directory found in {root}"]
    for dept in dirs:
        brain = dept / "department-brain.md"
        if not brain.exists():
            errors.append(f"{dept.name}: missing department-brain.md")
            continue
        text = brain.read_text(encoding="utf-8", errors="ignore")
        words = text.split()
        for marker in QUALITY_MARKERS:
            if marker not in text:
                errors.append(f"{dept.name}: missing quality marker: {marker}")
        if not any(marker in text for marker in RECEIPT_MARKERS):
            errors.append(f"{dept.name}: missing quality marker: Required receipts or Expected receipts")
        if len(words) < MIN_WORDS:
            errors.append(f"{dept.name}: department brain too shallow: {len(words)} words < {MIN_WORDS}")
        for companion in ["digital-employee.md", "skills.md", "onboarding.md"]:
            if not (dept / companion).exists():
                errors.append(f"{dept.name}: missing {companion}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd()
    errors = validate(root)
    if errors:
        print("Department quality validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Department quality validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

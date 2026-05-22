#!/usr/bin/env python3
"""Public-safety validation for the reusable framework repo."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".hermes", "build", ".venv", "venv", "node_modules"}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt", ".example", ""}
PRIVATE_LITERALS = [
    "/Users/",
    "Documents/" + "IA",
    "i" + "Cloud",
    "608" + "476" + "8324",
]
SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-.]{12,}"),
    re.compile(r"(?i)(postgres|mysql|mongodb)://[^\s)]+"),
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
]
ALLOWLIST_FRAGMENTS = [
    "example",
    "***",
    "validate_public_safety.py",
]


def iter_text_files() -> list[Path]:
    return [p for p in ROOT.rglob("*") if p.is_file() and p.suffix in TEXT_SUFFIXES and not any(part in SKIP_DIRS for part in p.parts)]


def allowlisted(line: str, rel: str) -> bool:
    target = f"{rel}:{line}"
    return any(fragment in target for fragment in ALLOWLIST_FRAGMENTS)


def main() -> int:
    errors: list[str] = []
    for path in iter_text_files():
        rel = str(path.relative_to(ROOT))
        for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
            if allowlisted(line, rel):
                continue
            for literal in PRIVATE_LITERALS:
                if literal in line:
                    errors.append(f"Private literal in {rel}:{line_no}")
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    errors.append(f"Secret-like pattern in {rel}:{line_no}")
    if errors:
        print("Public safety validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Public safety validation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

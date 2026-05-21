#!/usr/bin/env python3
"""Validate local Markdown links."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".hermes", "build", ".venv", "venv", "node_modules"}
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")


def iter_md() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if not any(part in SKIP_DIRS for part in p.parts)]


def main() -> int:
    errors: list[str] = []
    for path in iter_md():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in LINK_RE.finditer(text):
            target = match.group(2).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / unquote(target)).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} links outside repo: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} missing link target: {target}")
    if errors:
        print("Link validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Link validation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validación básica local para Company Brain System.

Comprueba que existen los archivos/carpetas mínimas y busca patrones obvios de secretos.
No llama a servicios externos.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "DECISIONS.md",
    "CHANGELOG.md",
    "docs",
    "schemas",
    "templates",
    "scripts",
]

OPTIONAL_INTERNAL_PATHS = [
    "PLAN.md",
    "ORCHESTRATION_PLAN.md",
    "source-map.md",
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"(?i)secret\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"(?i)password\s*[:=]\s*['\"]?[^\s'\"]{8,}"),
    re.compile(r"(?i)token\s*[:=]\s*['\"]?[A-Za-z0-9_\-\.]{20,}"),
    re.compile(r"(?i)(postgres|mysql|mongodb)://[^\s)]+"),
]

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "build"}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt", ""}


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            files.append(path)
    return files


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            errors.append(f"Falta: {rel}")

    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"Posible secreto en {path.relative_to(ROOT)} con patrón {pattern.pattern}")

    if errors:
        print("Validación fallida:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validación OK: estructura mínima y búsqueda anti-secretos básica superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

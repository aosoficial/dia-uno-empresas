#!/usr/bin/env python3
"""Verify a generated private Company Brain instance."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REQUIRED_PATHS = [
    "README.md", "AGENTS.md", "MAP.md", ".env.example",
    "company/company-brain.md", "company/source-of-truth-map.md", "company/approval-boundaries.md", "company/operating-principles.md",
    "company/accountability-map.md", "company/scorecard.md", "company/operating-cadence.md",
    "company/company-scorecard.md", "company/guided-pilot-plan.md", "company/point-b-readiness.md",
    "departments/direction/department-brain.md", "departments/direction/skills.md", "departments/direction/onboarding.md",
    "digital-employees/ceo/IDENTITY.md", "digital-employees/ceo/SOUL.md",
    "digital-employees/ceo/PERMISSIONS.md", "digital-employees/ceo/TOOLS.md",
    "digital-employees/ceo/MEMORY.md", "digital-employees/ceo/OPERATIONS.md",
    "digital-employees/observer/IDENTITY.md", "digital-employees/observer/SOUL.md",
    "digital-employees/observer/PERMISSIONS.md", "digital-employees/observer/TOOLS.md",
    "roadmap/48h-7d-30d.md", "skills/README.md", "context-packets/initial-company-context.md",
    "receipts", "statechanges", "context-packets", "handoffs", "contracts", "traces/README.md", "secrets/README.md",
]
SECRET_PATTERNS = [re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"), re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"), re.compile(r"(?i)secret\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"), re.compile(r"(?i)password\s*[:=]\s*['\"]?[^\s'\"]{8,}"), re.compile(r"(?i)token\s*[:=]\s*['\"]?[A-Za-z0-9_\-\.]{20,}"), re.compile(r"(?i)(postgres|mysql|mongodb)://[^\s)]+")]
SKIP_DIRS = {".git", "__pycache__"}
TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".example", ""}


def iter_text_files(root: Path) -> list[Path]:
    return [p for p in root.rglob("*") if p.is_file() and p.suffix in TEXT_SUFFIXES and not any(part in SKIP_DIRS for part in p.parts)]


def run_hermes_check() -> list[str]:
    errors: list[str] = []
    if not shutil.which("hermes"):
        return ["Hermes not found on PATH"]
    for command in [["hermes", "--version"], ["hermes", "config", "check"], ["hermes", "doctor"]]:
        result = subprocess.run(command, text=True, capture_output=True, timeout=60)
        if result.returncode != 0:
            errors.append(f"Command failed: {' '.join(command)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify private Company Brain instance")
    parser.add_argument("instance", help="Path to generated instance")
    parser.add_argument("--require-hermes", action="store_true")
    args = parser.parse_args()
    root = Path(args.instance).expanduser().resolve()
    errors: list[str] = []
    if not root.exists() or not root.is_dir():
        print(f"Instance does not exist: {root}", file=sys.stderr)
        return 2
    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            errors.append(f"Missing: {rel}")
    approval_text = (root / "company" / "approval-boundaries.md").read_text(encoding="utf-8") if (root / "company" / "approval-boundaries.md").exists() else ""
    for phrase in ["External", "Spend", "Production", "Sensitive", "Legal"]:
        if phrase.lower() not in approval_text.lower():
            errors.append(f"Approval boundary missing concept: {phrase}")
    for must in ["direction", "source-of-truth", "receipt", "statechange", "context packet"]:
        combined = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in iter_text_files(root) if p.stat().st_size < 20000).lower()
        if must not in combined:
            errors.append(f"Generated instance missing concept: {must}")
    for path in iter_text_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"Possible secret in {path.relative_to(root)}")
    if args.require_hermes:
        errors.extend(run_hermes_check())
    if errors:
        print("Installation verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Installation verification OK: {root}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

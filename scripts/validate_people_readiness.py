#!/usr/bin/env python3
"""Validate the installed People-layer scaffold without claiming operation."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from method_assets import validate_method_assets

REQUIRED = [
    "METHOD.json",
    "README.md",
    "AGENTS.md",
    "MAP.md",
    "personas/README.md",
    "personas/metodo-v3/README.md",
    "personas/metodo-v3/INVENTARIO.md",
    "personas/metodo-v3/MANIFEST.sha256",
    "company/company-brain.md",
    "company/accountability-map.md",
    "company/approval-boundaries.md",
    "company/scorecard.md",
    "company/operating-cadence.md",
    "company/people-organization-plan.md",
    "company/people-readiness.md",
    "receipts",
    "statechanges",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a People-layer scaffold")
    parser.add_argument("instance", help="Path to generated private instance")
    args = parser.parse_args()
    root = Path(args.instance).expanduser().resolve()
    if not root.is_dir():
        print(f"Instance does not exist: {root}", file=sys.stderr)
        return 2

    errors = [f"Missing: {relative}" for relative in REQUIRED if not (root / relative).exists()]
    method_file = root / "METHOD.json"
    if method_file.is_file():
        try:
            method = json.loads(method_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid METHOD.json: {exc}")
        else:
            if method.get("method_mode") not in {"people", "hybrid"}:
                errors.append("METHOD.json method_mode must be people or hybrid")
            if not method.get("human_accountable"):
                errors.append("METHOD.json requires human_accountable")
            if method.get("status") == "operational":
                errors.append("Fresh scaffold must not claim operational status")

    method_root = root / "personas" / "metodo-v3"
    if method_root.exists():
        errors.extend(validate_method_assets(method_root))

    combined = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in [root / "personas" / "README.md", root / "company" / "people-readiness.md"]
        if path.is_file()
    ).lower()
    for concept in ["rumbo", "responsable humano", "sop", "decisiones", "reuniones", "no demuestra"]:
        if concept not in combined:
            errors.append(f"People layer missing concept: {concept}")

    if errors:
        print("People scaffold validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"People scaffold validation OK: {root}")
    print("This proves installation and integrity only; it does not prove an organized or operational company.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

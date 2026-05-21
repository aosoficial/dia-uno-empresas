#!/usr/bin/env python3
"""Bootstrap a private Company Brain instance.

No external calls. Default mode is dry-run unless --yes is provided.
For guided agency/consultancy/freelancer setup, use scripts/company_brain_wizard.py.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "generated-company-instance"
SECRET_PATTERNS = [re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]"), re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"), re.compile(r"(?i)(postgres|mysql|mongodb)://")]


def has_secret(value: str) -> bool:
    return any(pattern.search(value or "") for pattern in SECRET_PATTERNS)


def inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def render(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace(key, value)
    return text


def copy_template(output: Path, values: dict[str, str]) -> list[Path]:
    written: list[Path] = []
    for source in TEMPLATE.rglob("*"):
        rel = source.relative_to(TEMPLATE)
        target = output / rel
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            target.write_text(render(source.read_text(encoding="utf-8"), values), encoding="utf-8")
        except UnicodeDecodeError:
            shutil.copy2(source, target)
        written.append(target)
    return written


def write_receipt(output: Path, args: argparse.Namespace) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    path = output / "receipts" / "installation-receipt.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"""# Installation Receipt

Date: `{stamp}`
Owner: `{args.owner}`
Company instance: `{output}`
Runtime: `Hermes / ORGO ready`
Company type: `{args.company_type}`

## What changed

Private Company Brain instance bootstrapped for `{args.company}` with Dirección as the first department.

## Why

Prepare a safe AI-First company runtime with company memory, approvals, roadmap and one first digital employee.

## Source / provenance

- Bootstrap script: `scripts/bootstrap_company_brain.py`
- Template: `templates/generated-company-instance/`

## Evidence

- Output path: `{output}`
- First department: `direction`
- First employee: `{args.first_employee}`

## Allowed next actions

- Run verifier.
- Fill company intake.
- Run one safe internal Dirección task.

## Forbidden without approval

- External communication.
- Spend.
- Legal/economic commitments.
- Production changes.
- Sensitive customer data use.

## Warnings / risks left

- Initial skeleton only; real operating context still needs human review.
""", encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap a private Company Brain instance")
    parser.add_argument("--company", required=True, help="Company name; do not include secrets")
    parser.add_argument("--company-type", choices=["agency", "consultancy", "freelancer"], default="agency")
    parser.add_argument("--sector", default="unspecified")
    parser.add_argument("--owner", default="operator")
    parser.add_argument("--first-department", default="direction")
    parser.add_argument("--first-employee", default="Dirección Assistant / CEO Operations Assistant")
    parser.add_argument("--language", default="en")
    parser.add_argument("--risk-tier", default="internal-low")
    parser.add_argument("--point-a", default="Knowledge scattered; processes manual; AI used ad hoc.")
    parser.add_argument("--first-objective", default="Install Dirección and complete one safe internal task with receipt.")
    parser.add_argument("--output", required=True, help="Private output path outside this repo")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be created")
    parser.add_argument("--yes", action="store_true", help="Actually write files")
    parser.add_argument("--example", action="store_true", help="Allow output inside repo for synthetic examples only")
    args = parser.parse_args()

    if args.first_department != "direction":
        print("Company Brain bootstrap requires Dirección / direction as first department. Use the wizard for later rollout.", file=sys.stderr)
        return 2

    for field in ["company", "company_type", "sector", "owner", "first_department", "first_employee", "language", "risk_tier", "point_a", "first_objective", "output"]:
        if has_secret(str(getattr(args, field))):
            print(f"Refusing possible secret in --{field.replace('_', '-')}", file=sys.stderr)
            return 2

    output = Path(args.output).expanduser().resolve()
    if inside(output, ROOT) and not args.example:
        print("Refusing output inside canonical repo. Use a private path or --example for synthetic examples.", file=sys.stderr)
        return 2

    values = {
        "{{ company_name }}": args.company,
        "{{ company_type }}": args.company_type,
        "{{ sector }}": args.sector,
        "{{ owner }}": args.owner,
        "{{ first_department }}": args.first_department,
        "{{ first_employee }}": args.first_employee,
        "{{ language }}": args.language,
        "{{ risk_tier }}": args.risk_tier,
        "{{ point_a }}": args.point_a,
        "{{ first_objective }}": args.first_objective,
        "{{ department_owner }}": args.owner,
        "{{ point_a_symptoms }}": args.point_a,
        "{{ current_tools }}": "TBD",
        "{{ active_processes }}": "TBD",
        "{{ metric_1 }}": "TBD",
        "{{ metric_2 }}": "TBD",
        "{{ metric_3 }}": "TBD",
    }

    dry_run = args.dry_run or not args.yes
    if dry_run:
        print("DRY RUN: no files written")
        print(f"Would create: {output}")
        print(f"Company: {args.company}")
        print("First department: direction")
        print(f"First employee: {args.first_employee}")
        print("Next: rerun with --yes, then python scripts/verify_installation.py <output>")
        return 0

    if output.exists() and any(output.iterdir()):
        print(f"Refusing to write into non-empty directory: {output}", file=sys.stderr)
        return 2

    written = copy_template(output, values)
    receipt = write_receipt(output, args)
    print(f"Created private Company Brain instance: {output}")
    print(f"Files written: {len(written) + 1}")
    print(f"Receipt: {receipt}")
    print(f"Next: python scripts/verify_installation.py {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

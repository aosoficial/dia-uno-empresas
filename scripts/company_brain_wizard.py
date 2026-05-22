#!/usr/bin/env python3
"""Guided Company Brain accelerator wizard.

Generates a private instance for agencies, consultancies or freelancers. No external calls.
Dry-run by default unless --yes is provided. Interactive mode is available for
non-technical operators.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_TEMPLATE = ROOT / "templates" / "generated-company-instance"
DEPARTMENT_TEMPLATE = ROOT / "templates" / "departments"
COMPANY_TYPES = {"agency", "consultancy", "freelancer"}
MATURITY_LEVELS = {"chaos", "documented", "assisted", "ai-first"}
VERTICALS = {"agency", "consultancy", "freelancer", "service-business"}
DEFAULT_DEPARTMENTS = ["direction", "operations-delivery", "marketing", "sales", "customer-success"]
ALL_DEPARTMENTS = DEFAULT_DEPARTMENTS + ["product-software", "finance", "people", "admin-legal"]
DEPARTMENT_LABELS = {
    "direction": "Dirección / Mother Brain",
    "operations-delivery": "Operations / Delivery",
    "marketing": "Marketing",
    "sales": "Sales",
    "customer-success": "Customer Success",
    "product-software": "Product / Software",
    "finance": "Finance",
    "people": "People / Organization",
    "admin-legal": "Admin / Legal",
}
DEPARTMENT_DIGITAL_EMPLOYEES = {
    "direction": "ceo-operations-assistant",
    "operations-delivery": "ceo-operations-assistant",
    "marketing": "marketing-assistant",
    "sales": "sales-assistant",
    "customer-success": "customer-success-assistant",
    "finance": "finance-assistant",
    "people": "people-assistant",
    "admin-legal": "admin-legal-assistant",
}
COMPANY_TYPE_DEFAULTS = {
    "agency": {
        "departments": "direction,operations-delivery,marketing,sales,customer-success,finance",
        "first_objective": "Install Dirección and run one delivery QA review with receipt.",
    },
    "consultancy": {
        "departments": "direction,operations-delivery,sales,customer-success,finance,people",
        "first_objective": "Install Dirección and turn one repeated client delivery motion into a documented operating loop.",
    },
    "freelancer": {
        "departments": "direction,operations-delivery,marketing,sales,finance",
        "first_objective": "Install Dirección and productize one repeatable service offer with receipt.",
    },
}
READINESS_DIMENSIONS = [
    "strategy clarity",
    "offer/productization",
    "source of truth",
    "process documentation",
    "approvals/permissions",
    "metrics",
    "tool integration",
    "digital employees",
    "feedback loop",
    "security/compliance",
]
MATURITY_BASE_SCORES = {
    "chaos": 2,
    "documented": 4,
    "assisted": 6,
    "ai-first": 8,
}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]"),
    re.compile(r"(?i)(postgres|mysql|mongodb)://"),
]


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


def copy_tree(src: Path, dst: Path, values: dict[str, str]) -> int:
    count = 0
    for source in src.rglob("*"):
        rel = source.relative_to(src)
        target = dst / rel
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            target.write_text(render(source.read_text(encoding="utf-8"), values), encoding="utf-8")
        except UnicodeDecodeError:
            shutil.copy2(source, target)
        count += 1
    return count


def prompt(label: str, default: str | None = None, choices: set[str] | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{label}{suffix}: ").strip() or (default or "")
        if choices and value not in choices:
            print(f"Choose one of: {', '.join(sorted(choices))}")
            continue
        if value:
            return value
        print("Required.")


def apply_interactive_defaults(args: argparse.Namespace) -> argparse.Namespace:
    if not args.interactive:
        return args
    print("Company Brain System guided setup")
    company = prompt("Company name", args.company)
    company_type = prompt("Company type", args.company_type or "agency", COMPANY_TYPES)
    defaults = COMPANY_TYPE_DEFAULTS[company_type]
    args.company = company
    args.company_type = company_type
    args.sector = prompt("Sector", args.sector if args.sector != "unspecified" else "service business")
    args.owner = prompt("Human owner", args.owner)
    args.point_a = prompt("Point A symptoms", args.point_a)
    args.first_objective = prompt("First 48h objective", args.first_objective or defaults["first_objective"])
    args.departments = prompt("Departments comma-separated or 'all'", args.departments or defaults["departments"])
    args.output = prompt("Private output path", args.output)
    confirmation = prompt("Write files now? Type yes to proceed, anything else for dry-run", "yes")
    args.yes = confirmation.lower() == "yes"
    args.dry_run = not args.yes
    return args


def parse_departments(raw: str) -> list[str]:
    departments = ALL_DEPARTMENTS if raw == "all" else [d.strip() for d in raw.split(',') if d.strip()]
    return ["direction"] + [d for d in departments if d != "direction"]


def readiness_profile(args: argparse.Namespace, departments: list[str]) -> dict[str, object]:
    """Return deterministic readiness score and next-sprint guidance.

    This intentionally avoids external calls and keeps backward compatibility with
    the existing --maturity flag. The score is a starting diagnostic, not a claim
    about a real company until the operator attaches evidence.
    """
    maturity = args.maturity or "chaos"
    base = MATURITY_BASE_SCORES[maturity]
    scores: dict[str, int] = {}
    for dimension in READINESS_DIMENSIONS:
        score = base
        if dimension == "strategy clarity" and args.first_objective:
            score += 1
        if dimension == "offer/productization" and args.company_type in {"agency", "consultancy", "freelancer"}:
            score += 1
        if dimension == "source of truth" and "direction" in departments:
            score += 1
        if dimension == "process documentation" and "operations-delivery" in departments:
            score += 1
        if dimension == "approvals/permissions" and "admin-legal" in departments:
            score += 1
        if dimension == "metrics" and "finance" in departments:
            score += 1
        if dimension == "tool integration" and args.vertical:
            score += 1
        if dimension == "digital employees" and departments:
            score += 1
        if dimension == "feedback loop" and maturity in {"assisted", "ai-first"}:
            score += 1
        if dimension == "security/compliance" and "admin-legal" in departments:
            score += 1
        scores[dimension] = min(score, 10)
    total = sum(scores.values())
    if total < 25:
        level = "Point A / chaos"
        next_sprint = "Sprint 0 — Dirección / Mother Brain, approval boundaries and one internal receipt."
    elif total < 50:
        level = "documented"
        next_sprint = "Sprint 1 — Operations/Delivery and Sales handoff with scorecard and receipts."
    elif total < 75:
        level = "assisted"
        next_sprint = "Sprint 2 — Customer Success, Finance visibility and feedback loop."
    elif total < 90:
        level = "AI-first operating"
        next_sprint = "Sprint 3 — Product/Software, People, Admin/Legal and quality gates."
    else:
        level = "AI-first compounding"
        next_sprint = "Sprint 4 — governed experiment loop, skill evolution and anonymized proposals."
    return {"scores": scores, "total": total, "level": level, "next_sprint": next_sprint}


def recommended_departments(company_type: str, maturity: str, departments: list[str]) -> dict[str, list[str]]:
    now = ["direction"]
    if company_type == "freelancer":
        now += [d for d in ["operations-delivery", "finance"] if d in departments]
    elif company_type == "agency":
        now += [d for d in ["operations-delivery", "sales", "marketing"] if d in departments]
    else:
        now += [d for d in ["operations-delivery", "customer-success", "sales"] if d in departments]
    if maturity in {"assisted", "ai-first"}:
        now += [d for d in ["customer-success", "product-software"] if d in departments and d not in now]
    later = [d for d in departments if d not in now]
    return {"now": now, "later": later}


def write_rollout_map(output: Path, args: argparse.Namespace, departments: list[str]) -> Path:
    path = output / "company" / "department-rollout-map.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Department Rollout Map",
        "",
        f"Company: `{args.company}`",
        f"Company type: `{args.company_type}`",
        f"Owner: `{args.owner}`",
        "",
        "## Rollout order",
        "",
    ]
    for index, dept in enumerate(departments, start=1):
        phase = "48h" if index == 1 else "7 days" if index <= 5 else "30 days"
        lines.extend([
            f"### {index}. `{dept}` — {DEPARTMENT_LABELS.get(dept, dept)}",
            "",
            f"- Rollout window: `{phase}`",
            "- Human owner: `assign before active work`",
            "- Digital employee: see department `digital-employee.md`",
            "- Required evidence: first receipt, first statechange, current scorecard line",
            "- Approval rule: ask before external/public/economic/legal/production/sensitive actions",
            "",
        ])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_company_scorecard(output: Path, args: argparse.Namespace, departments: list[str]) -> Path:
    path = output / "company" / "company-scorecard.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(
        f"- `{dept}`: owner assigned, active brain, weekly metric, latest receipt, blockers"
        for dept in departments
    )
    path.write_text(f"""# Company AI-First Scorecard

Company: `{args.company}`
Owner: `{args.owner}`
Freshness: `draft until reviewed`

## Point A

`{args.point_a}`

## Point B outcome

A service business operating with Dirección, selected department brains, digital employees, approval boundaries, memory, receipts and a weekly improvement loop.

## Company-level metrics

- Revenue / retained revenue: `fill privately`
- Delivery quality: `fill privately`
- Sales pipeline health: `fill privately`
- Customer success signal: `fill privately`
- Automation leverage: `human hours removed with evidence`
- Memory quality: `receipts/statechanges/context packets current`

## Department scorecard lines

{rows}

## Weekly review prompts

1. Which decision changed the company this week?
2. Which repeated task became a SOP or skill?
3. Which agent action required human correction?
4. Which approval boundary was hit?
5. Which metric got better because of the system?
""", encoding="utf-8")
    return path


def write_maturity_diagnosis(output: Path, args: argparse.Namespace, departments: list[str]) -> Path:
    path = output / "company" / "maturity-diagnosis.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    maturity = args.maturity or "chaos"
    vertical = args.vertical or args.company_type
    if maturity == "chaos":
        posture = "Stabilize Dirección first, then install delivery, sales and finance evidence loops."
    elif maturity == "documented":
        posture = "Turn existing documents into executable skills, receipts and scorecards."
    elif maturity == "assisted":
        posture = "Promote reliable assistant workflows into department brains with approvals."
    else:
        posture = "Optimize quality, cost, observability and cross-department feedback loops."
    profile = readiness_profile(args, departments)
    selections = recommended_departments(args.company_type, maturity, departments)
    score_lines = "\n".join(
        f"- {dimension}: `{score}/10`"
        for dimension, score in profile["scores"].items()  # type: ignore[union-attr]
    )
    recommended = ", ".join(selections["now"])
    later = ", ".join(selections["later"]) or "none"
    path.write_text(f"""# Maturity Diagnosis

Company: `{args.company}`
Maturity level: `{maturity}`
Vertical: `{vertical}`
Owner: `{args.owner}`

## Diagnosis

{posture}

## AI-First readiness score

Total score: `{profile["total"]}/100`
Readiness level: `{profile["level"]}`
Recommended next sprint: `{profile["next_sprint"]}`

## Score by dimension

{score_lines}

## Recommended first departments

`{recommended}`

## Departments to defer or install later

`{later}`

## 48h recommendation

Install Dirección / Mother Brain, approval boundaries, one digital employee and one receipt-producing internal task.

## 7-day recommendation

Connect Operations/Delivery, Sales or Marketing depending on the bottleneck, and run one handoff with evidence.

## 30-day recommendation

Complete the selected department rollout, add finance/customer-success visibility and convert repeated corrections into skills.

## Evidence required

- Current scorecard line.
- Latest receipt.
- Latest statechange.
- Human correction or approval record when a boundary is hit.
""", encoding="utf-8")
    return path


def write_guided_pilot_plan(output: Path, args: argparse.Namespace, departments: list[str]) -> Path:
    path = output / "company" / "guided-pilot-plan.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    profile = readiness_profile(args, departments)
    selections = recommended_departments(args.company_type, args.maturity, departments)
    first_department = next((dept for dept in selections["now"] if dept != "direction"), departments[1] if len(departments) > 1 else "direction")
    path.write_text(f"""# Guided Pilot Plan

Company: `{args.company}`
Owner: `{args.owner}`
Company type: `{args.company_type}`
Maturity: `{args.maturity}`
Readiness score: `{profile["total"]}/100`
Next sprint: `{profile["next_sprint"]}`

## Guided Pilot 30 / 60 / 120

### First 30 minutes — operating contract

- Confirm Punto A: `{args.point_a}`
- Confirm first objective: `{args.first_objective}`
- Confirm human approval owner: `{args.owner}`
- Confirm forbidden actions: external/public/economic/legal/production/sensitive.

### First 60 minutes — Direction and first department

- Review `company/company-brain.md`.
- Review `company/source-of-truth-map.md` and select the current system/source for the first workflow.
- Review `company/approval-boundaries.md`.
- Install first priority department: `{first_department}`.
- Fill company scorecard with evidenced values or `unknown`.

### First 120 minutes — first internal loop

- Create one context packet after the source-of-truth map names system/source, owner, freshness, permissions and evidence path.
- Ask the digital employee for draft/analysis only.
- Human reviews the output.
- Write Receipt and StateChange when operating state changes.
- Run `python scripts/validate_point_b_readiness.py --mode scaffold {output}` to verify generated files.
- Run `python scripts/validate_point_b_readiness.py --mode operational {output}` only after the first human-reviewed operating loop has real evidence.

## Recommended departments now

{chr(10).join(f'- `{dept}`' for dept in selections["now"])}

## Deferred departments

{chr(10).join(f'- `{dept}`' for dept in selections["later"]) or '- none'}

## Closeout rule

Do not claim operational Punto B from generated files. Scaffold validation only proves installation shape. Operational Punto B requires `--mode operational` to pass with human-reviewed evidence for Direction, source-of-truth map, approval boundaries, first department, digital employee permissions, context packet, receipt, scorecard and next sprint.
""", encoding="utf-8")
    return path


def write_point_b_readiness(output: Path, args: argparse.Namespace, departments: list[str]) -> Path:
    path = output / "company" / "point-b-readiness.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    profile = readiness_profile(args, departments)
    path.write_text(f"""# Point B Readiness

Company: `{args.company}`
Owner: `{args.owner}`
Freshness: `draft until validated with evidence`

## Starting diagnostic

Point B readiness: `{profile["total"]}/100`
AI-First readiness score: `{profile["total"]}/100`
Readiness level: `{profile["level"]}`
Recommended next sprint: `{profile["next_sprint"]}`

## Scaffold checklist generated now

- [x] Direction / Mother Brain file created: `company/company-brain.md`
- [x] Source-of-truth map scaffold created: `company/source-of-truth-map.md`
- [x] Approval boundaries file created: `company/approval-boundaries.md`
- [x] Priority department scaffold created: `departments/*/department-brain.md`
- [x] Digital employee permissions file created: `digital-employees/*/PERMISSIONS.md`
- [x] Initial context packet scaffold created: `context-packets/initial-company-context.md`
- [x] Installation receipt created: `receipts/wizard-installation-receipt.md`
- [x] Scorecard scaffold created: `company/company-scorecard.md`
- [x] Guided pilot plan scaffold created: `company/guided-pilot-plan.md`

## Operational Punto B evidence still required

- [ ] Human-reviewed Direction contains real vision, mission, annual goal/rocks/OKRs and owner.
- [ ] Source-of-truth map identifies existing systems, owners, permissions, freshness and receipt rules.
- [ ] Approval boundaries were reviewed by the accountable human.
- [ ] One priority department has a live workflow, owner, scorecard and escalation path.
- [ ] One digital employee/role ran a bounded internal loop under explicit permissions.
- [ ] A non-placeholder context packet briefed that loop.
- [ ] A receipt proves what happened, why, source/provenance, approvals and observed outcome.
- [ ] Scorecard/readiness was updated from evidence, not from generated defaults.
- [ ] Next sprint was selected from the review.

## Validation commands

Scaffold check:

`python scripts/validate_point_b_readiness.py --mode scaffold {output}`

Operational check after the first human-reviewed loop:

`python scripts/validate_point_b_readiness.py --mode operational {output}`

## Rule

This file is not proof by itself. A fresh wizard output should pass scaffold validation and fail operational validation until placeholders are replaced with evidenced private context and an actual reviewed operating loop has a receipt.
""", encoding="utf-8")
    return path


def write_receipt(output: Path, args: argparse.Namespace, departments: list[str]) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    path = output / "receipts" / "wizard-installation-receipt.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"""# Wizard Installation Receipt

Date: `{stamp}`
Owner: `{args.owner}`
Company: `{args.company}`
Company type: `{args.company_type}`
Generated path: `{output}`

## What changed

Created a guided Company Brain instance with Dirección first and department rollout assets.

## Why

Move a service business from Point A to Point B AI-First using memory, people/accountability, digital employees, approvals and receipts.

## Departments generated

{chr(10).join(f'- `{d}`' for d in departments)}

## Source / provenance

- `scripts/company_brain_wizard.py`
- `templates/generated-company-instance/`
- `templates/departments/`
- Source adapters documented in `docs/26_source_adapters.md`

## Allowed next actions

- Run verifier.
- Complete `company/source-of-truth-map.md` before the first Context Packet.
- Fill private company context.
- Run one safe internal Dirección task.

## Forbidden without approval

External/public/economic/legal/production/sensitive actions.
""", encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a guided private Company Brain instance")
    parser.add_argument("--company")
    parser.add_argument("--company-type", choices=sorted(COMPANY_TYPES))
    parser.add_argument("--sector", default="unspecified")
    parser.add_argument("--owner", default="operator")
    parser.add_argument("--output")
    parser.add_argument("--language", default="en")
    parser.add_argument("--risk-tier", default="internal-low")
    parser.add_argument("--point-a", default="Knowledge scattered; processes manual; AI used ad hoc.")
    parser.add_argument("--maturity", choices=sorted(MATURITY_LEVELS), default="chaos")
    parser.add_argument("--vertical", choices=sorted(VERTICALS))
    parser.add_argument("--first-objective")
    parser.add_argument("--departments")
    parser.add_argument("--interactive", action="store_true", help="Ask guided setup questions")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--yes", action="store_true")
    parser.add_argument("--example", action="store_true", help="Allow synthetic output inside this repo")
    args = apply_interactive_defaults(parser.parse_args())

    if not args.company or not args.company_type or not args.output:
        parser.error("--company, --company-type and --output are required unless --interactive supplies them")
    if not args.first_objective:
        args.first_objective = COMPANY_TYPE_DEFAULTS[args.company_type]["first_objective"]
    if not args.vertical:
        args.vertical = args.company_type
    if not args.departments:
        args.departments = COMPANY_TYPE_DEFAULTS[args.company_type]["departments"]

    for field in ["company", "company_type", "sector", "owner", "output", "language", "risk_tier", "point_a", "maturity", "vertical", "first_objective", "departments"]:
        if has_secret(str(getattr(args, field))):
            print(f"Refusing possible secret in --{field.replace('_','-')}", file=sys.stderr)
            return 2

    departments = parse_departments(args.departments)
    invalid = [d for d in departments if d not in ALL_DEPARTMENTS]
    if invalid:
        print(f"Unknown departments: {', '.join(invalid)}", file=sys.stderr)
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
        "{{ language }}": args.language,
        "{{ risk_tier }}": args.risk_tier,
        "{{ point_a }}": args.point_a,
        "{{ first_objective }}": args.first_objective,
        "{{ first_department }}": "direction",
        "{{ first_employee }}": "Dirección Assistant / CEO Operations Assistant",
        "{{ department_owner }}": args.owner,
        "{{ point_a_symptoms }}": args.point_a,
        "{{ current_tools }}": "fill privately",
        "{{ active_processes }}": "fill privately",
        "{{ metric_1 }}": "one company outcome metric",
        "{{ metric_2 }}": "one department throughput metric",
        "{{ metric_3 }}": "one quality or customer signal",
    }

    dry_run = args.dry_run or not args.yes
    profile = readiness_profile(args, departments)
    selections = recommended_departments(args.company_type, args.maturity, departments)
    if dry_run:
        print("DRY RUN: no files written")
        print(f"Would create guided instance: {output}")
        print(f"Company type: {args.company_type}")
        print("Departments: " + ", ".join(departments))
        print(f"Maturity: {args.maturity}; vertical: {args.vertical}")
        print(f"AI-First readiness score: {profile['total']}/100 ({profile['level']})")
        print(f"Recommended next sprint: {profile['next_sprint']}")
        print("Recommended departments now: " + ", ".join(selections["now"]))
        if selections["later"]:
            print("Install later: " + ", ".join(selections["later"]))
        print("Next: rerun with --yes, then python scripts/verify_installation.py <output>")
        print("Then: python scripts/validate_point_b_readiness.py --mode scaffold <output>")
        print("Troubleshooting: docs/TROUBLESHOOTING.md")
        print("Guided Pilot 30/60/120: contract, Direction + first department, first internal loop")
        return 0

    if output.exists() and any(output.iterdir()):
        print(f"Refusing to write into non-empty directory: {output}", file=sys.stderr)
        return 2

    count = copy_tree(BASE_TEMPLATE, output, values)
    legacy_operations = output / "departments" / "operations"
    if legacy_operations.exists():
        shutil.rmtree(legacy_operations)
    copied_employee_packs: set[str] = set()
    for dept in departments:
        count += copy_tree(DEPARTMENT_TEMPLATE / dept, output / "departments" / dept, values)
        employee_pack = DEPARTMENT_DIGITAL_EMPLOYEES.get(dept)
        if employee_pack and employee_pack not in copied_employee_packs:
            src = BASE_TEMPLATE / "digital-employees" / employee_pack
            if src.exists():
                count += copy_tree(src, output / "digital-employees" / employee_pack, values)
                copied_employee_packs.add(employee_pack)
    rollout = write_rollout_map(output, args, departments)
    scorecard = write_company_scorecard(output, args, departments)
    diagnosis = write_maturity_diagnosis(output, args, departments)
    pilot_plan = write_guided_pilot_plan(output, args, departments)
    point_b = write_point_b_readiness(output, args, departments)
    receipt = write_receipt(output, args, departments)
    print(f"Created guided Company Brain instance: {output}")
    print(f"Files written: {count + 6}")
    print(f"Rollout map: {rollout}")
    print(f"Company scorecard: {scorecard}")
    print(f"Maturity diagnosis: {diagnosis}")
    print(f"Guided pilot plan: {pilot_plan}")
    print(f"Point B readiness: {point_b}")
    print(f"Receipt: {receipt}")
    print(f"Next: python scripts/verify_installation.py {output}")
    print(f"Then scaffold check: python scripts/validate_point_b_readiness.py --mode scaffold {output}")
    print(f"After a human-reviewed loop: python scripts/validate_point_b_readiness.py --mode operational {output}")
    print("Troubleshooting: docs/TROUBLESHOOTING.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WIZARD = ROOT / "scripts" / "company_brain_wizard.py"
POINT_B_VALIDATOR = ROOT / "scripts" / "validate_point_b_readiness.py"
INSTALLABLE_VALIDATOR = ROOT / "scripts" / "validate_installable_runtime.py"


def run_cmd(args):
    return subprocess.run(
        [sys.executable, *map(str, args)],
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=120,
    )


def test_guided_pilot_docs_and_templates_exist_with_operational_markers():
    required = [
        "docs/39_guided_pilot_happy_path.md",
        "docs/40_self_serve_happy_path.md",
        "docs/41_guided_pilot_delivery_model.md",
        "docs/42_point_b_definition.md",
        "docs/43_self_serve_operator_ux.md",
        "templates/pilot/pilot-session-script.md",
        "templates/pilot/operator-checklist.md",
        "templates/pilot/client-homework.md",
        "templates/pilot/sprint-0-intake.md",
        "templates/pilot/sprint-1-direction.md",
        "templates/pilot/sprint-2-department.md",
        "templates/pilot/sprint-3-digital-employee.md",
        "templates/pilot/sprint-4-feedback-loop.md",
        "templates/scorecards/point-b-readiness-scorecard.md",
        "Makefile",
    ]
    markers = ["Punto B", "Evidence", "Approval", "Receipt", "Next action"]
    for rel in required:
        path = ROOT / rel
        assert path.exists(), rel
        text = path.read_text(encoding="utf-8", errors="ignore")
        assert len(text.split()) >= 60, rel
        assert any(marker in text for marker in markers), rel


def test_point_b_validator_separates_scaffold_operational_and_synthetic(tmp_path):
    acme = ROOT / "examples" / "acme-agency-ai-first"

    synthetic_without_flag = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", acme])
    assert synthetic_without_flag.returncode == 1
    assert "synthetic evidence" not in synthetic_without_flag.stdout.lower()
    assert "Point B operational validation failed" in synthetic_without_flag.stdout

    synthetic_with_flag = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", "--allow-synthetic", acme])
    assert synthetic_with_flag.returncode == 0, synthetic_with_flag.stderr + synthetic_with_flag.stdout
    assert "Point B operational validation OK" in synthetic_with_flag.stdout

    empty = tmp_path / "empty-company"
    empty.mkdir()
    bad = run_cmd([POINT_B_VALIDATOR, "--mode", "scaffold", empty])
    assert bad.returncode == 1
    assert "Point B scaffold validation failed" in bad.stdout


def test_wizard_generates_pilot_plan_and_point_b_scorecard(tmp_path):
    output = tmp_path / "guided-acme"
    result = run_cmd([
        WIZARD,
        "--company", "Guided Acme",
        "--company-type", "agency",
        "--sector", "B2B services",
        "--owner", "Founder",
        "--output", output,
        "--maturity", "assisted",
        "--departments", "direction,operations-delivery,sales,customer-success,finance",
        "--yes",
    ])
    assert result.returncode == 0, result.stderr + result.stdout
    pilot_plan = output / "company" / "guided-pilot-plan.md"
    point_b = output / "company" / "point-b-readiness.md"
    assert pilot_plan.exists()
    assert point_b.exists()
    assert "30 / 60 / 120" in pilot_plan.read_text()
    assert "Point B readiness" in point_b.read_text()
    verify = run_cmd([ROOT / "scripts" / "verify_installation.py", output])
    assert verify.returncode == 0, verify.stderr + verify.stdout
    scaffold_readiness = run_cmd([POINT_B_VALIDATOR, "--mode", "scaffold", output])
    assert scaffold_readiness.returncode == 0, scaffold_readiness.stderr + scaffold_readiness.stdout
    assert "Point B scaffold validation OK" in scaffold_readiness.stdout

    operational_readiness = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", output])
    assert operational_readiness.returncode == 1
    assert "Point B operational validation failed" in operational_readiness.stdout

    low_threshold_operational_readiness = run_cmd([
        POINT_B_VALIDATOR,
        "--mode",
        "operational",
        "--min-score",
        "10",
        output,
    ])
    assert low_threshold_operational_readiness.returncode == 1
    assert "missing mandatory operational evidence" in low_threshold_operational_readiness.stdout.lower()
    assert "Point B operational validation OK" not in low_threshold_operational_readiness.stdout


def write_operational_fixture(root: Path) -> None:
    files = {
        "company/company-brain.md": """
# Direction / Mother Brain
Owner: Founder
Source: leadership workshop
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: first operating loop evidence pack
Vision and mission are documented. Annual goal, rocks and OKRs are reviewed for the first operating slice.
""",
        "company/approval-boundaries.md": """
# Approval boundaries
Owner: Founder
Source: approval workshop
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: approval matrix reviewed before first loop
External, economic, legal, production and sensitive actions require explicit human approval. Forbidden actions are listed.
""",
        "departments/operations/department-brain.md": """
# Operations Department Brain
Owner: Operations lead
Source: department review
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: first operational loop used this department brain
Responsibilities, workflows, scorecard, escalation path and operating cadence are defined for the first slice.
""",
        "digital-employees/ops-agent/PERMISSIONS.md": """
# Ops Agent Permissions
Owner: Founder
Source: role design
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: first operational loop permission check
Allowed actions, forbidden actions, tool boundaries, handoffs and approval gates are defined before active work.
""",
        "context-packets/first-loop.md": """
# First Loop Context Packet
Owner: Founder
Source: source-of-truth map
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: receipt/first-loop.md
Goal, scope, sources, assumptions, risks, allowed actions, forbidden actions and expected outcome are complete.
""",
        "receipts/first-loop.md": """
# First Loop Receipt
Owner: Founder
Source: context-packets/first-loop.md
Freshness: completed this week
Approval: human owner reviewed
Evidence: scorecard update and reviewed output
Observed outcome: one internal operating loop was completed, reviewed and converted into the next sprint.
""",
        "company/company-scorecard.md": """
# Company Scorecard
Owner: Founder
Source: receipt/first-loop.md
Freshness: updated this week
Approval: human owner reviewed
Evidence: first loop receipt
Metrics were updated from observed operating evidence, not from installation scaffold files.
""",
        "company/guided-pilot-plan.md": """
# Guided Pilot Plan
Owner: Founder
Source: first loop review
Freshness: updated this week
Approval: human owner reviewed
Evidence: next sprint decision from receipt
Next sprint was selected from the reviewed evidence and has a clear owner, expected outcome and approval gates.
""",
    }
    for rel, text in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text.strip() + "\n", encoding="utf-8")


def test_operational_validator_requires_all_mandatory_criteria_even_if_score_is_high(tmp_path):
    instance = tmp_path / "operational-missing-receipt"
    write_operational_fixture(instance)
    (instance / "receipts" / "first-loop.md").unlink()

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", instance])
    assert result.returncode == 1
    assert "Operational receipt exists" in result.stdout
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout

    lowered_threshold = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", "--min-score", "75", instance])
    assert lowered_threshold.returncode == 1
    assert "missing mandatory operational evidence" in lowered_threshold.stdout.lower()


def test_operational_validator_rejects_generic_prose_without_evidence_shape(tmp_path):
    instance = tmp_path / "generic-prose"
    files = [
        "company/company-brain.md",
        "company/approval-boundaries.md",
        "departments/operations/department-brain.md",
        "digital-employees/ops-agent/PERMISSIONS.md",
        "context-packets/first-loop.md",
        "receipts/first-loop.md",
        "company/company-scorecard.md",
        "company/guided-pilot-plan.md",
    ]
    generic = """
# Polished operating document
This document describes a thoughtful operating practice for a company that wants a better management rhythm. It talks about collaboration, alignment, team cadence, useful meetings, better follow through, improved decisions and cleaner internal communication across the organization.
""".strip()
    for rel in files:
        path = instance / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(generic + "\n", encoding="utf-8")

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", instance])
    assert result.returncode == 1
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


def test_operational_validator_rejects_scaffold_markers_even_with_complete_shape_and_low_min_score(tmp_path):
    markers = [
        "draft until reviewed",
        "fill privately",
        "assign before active work",
        "unknown",
        "generated",
        "unchecked evidence",
    ]

    for marker in markers:
        instance = tmp_path / marker.replace(" ", "-")
        write_operational_fixture(instance)
        for path in instance.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            path.write_text(
                text
                + f"\nScaffold rejection probe: {marker}. Owner, source, freshness, approval and evidence are present only to prove the marker hard-fails.\n",
                encoding="utf-8",
            )

        result = run_cmd([
            POINT_B_VALIDATOR,
            "--mode",
            "operational",
            "--min-score",
            "1",
            instance,
        ])
        assert result.returncode == 1, marker + result.stdout
        assert "missing mandatory operational evidence" in result.stdout.lower()
        assert "Point B operational validation OK" not in result.stdout


def test_installable_runtime_knows_guided_pilot_assets():
    result = run_cmd([INSTALLABLE_VALIDATOR])
    assert result.returncode == 0, result.stderr + result.stdout
    assert "guided pilot validation OK" in result.stdout

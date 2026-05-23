from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WIZARD = ROOT / "scripts" / "company_brain_wizard.py"
BOOTSTRAP = ROOT / "scripts" / "bootstrap_company_brain.py"
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
        "docs/44_first_operating_loop_examples.md",
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


def test_nontechnical_bootstrap_asks_ai_level_and_sets_guardrails():
    guide = ROOT / "docs/00_non_technical_start_with_codex_or_claude.md"
    assert guide.exists()
    text = guide.read_text(encoding="utf-8")
    for marker in [
        "examen inicial de nivel de IA",
        "Modo 1 — No técnico",
        "Modo 2 — Usuario IA intermedio",
        "Modo 3 — Técnico / builder",
        "guardrails fuertes",
        "no investigar a la persona",
        "pedir cuentas y claves solo después",
        "gratis o free tier",
        "no pegues claves en el chat",
        "jerarquía de carpetas",
        "no salir de la carpeta privada",
        "Codex",
        "Claude Code",
        "SOUL.md",
        "CEO/Operations Assistant",
    ]:
        assert marker in text, marker

    start_here = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
    assert "Antes de instalar: examen rápido de nivel IA" in start_here
    assert "docs/00_non_technical_start_with_codex_or_claude.md" in start_here


def test_wizard_dry_run_points_nontechnical_users_to_bootstrap_guide(tmp_path):
    output = tmp_path / "dia-uno"
    result = run_cmd([
        WIZARD,
        "--company", "DIA UNO",
        "--company-type", "consultancy",
        "--output", output,
        "--dry-run",
    ])
    assert result.returncode == 0, result.stderr + result.stdout
    for marker in [
        "Non-technical start",
        "docs/00_non_technical_start_with_codex_or_claude.md",
        "AI level mode",
        "private folder hierarchy",
    ]:
        assert marker in result.stdout


def test_first_operating_loop_examples_make_evidence_concrete():
    path = ROOT / "docs/44_first_operating_loop_examples.md"
    text = path.read_text(encoding="utf-8")
    for marker in [
        "agency delivery checklist",
        "consultancy proposal risks",
        "freelancer offer cleanup",
        "Universal evidence chain",
        "Source row selected",
        "Operational Receipt",
        "Scorecard update",
        "Anti-examples that must not count",
        "DIA UNO",
        "diauno.io",
        "Do not share the private instance or secrets",
    ]:
        assert marker in text


def test_first_operating_loop_example_kit_is_safe_and_actionable():
    kit = ROOT / "templates/generated-company-instance/examples/first-operating-loop"
    required = [
        "README.md",
        "context-packet-example.md",
        "receipt-example.md",
        "scorecard-example.md",
    ]
    for name in required:
        path = kit / name
        assert path.exists(), f"missing first loop example file: {name}"
        text = path.read_text(encoding="utf-8")
        assert "example" in text.lower()
        assert "Punto B" in text or "punto b" in text.lower() or "human-reviewed" in text
    combined = "\n".join((kit / name).read_text(encoding="utf-8") for name in required)
    for marker in [
        "Context Packet",
        "operational receipt",
        "human-reviewed",
        "scorecard",
        "Do not treat",
        "fictional",
    ]:
        assert marker in combined


def test_source_of_truth_maps_are_operator_usable_and_required():
    template = ROOT / "templates/integrations/existing-systems-map.md"
    generated = ROOT / "templates/generated-company-instance/company/source-of-truth-map.md"
    for path in [template, generated]:
        assert path.exists(), path
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in [
            "Drive / Docs",
            "Notion / wiki",
            "Sheets / spreadsheets",
            "CRM",
            "WhatsApp / Slack",
            "Email",
            "Calendar / meetings",
            "Project management",
            "Finance / invoices",
            "Owner",
            "Source-of-truth status",
            "Agent read permission",
            "Agent write/action permission",
            "Sync cadence",
            "Freshness",
            "Receipt rule",
            "Risks",
            "Next action",
            "Start read-only",
            "Do not store credentials",
            "DIA UNO",
            "diauno.io",
            "Connection approvals",
            "Action approvals",
        ]:
            assert marker in text, f"{path} missing {marker}"


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
    source_map = output / "company" / "source-of-truth-map.md"
    assert pilot_plan.exists()
    assert point_b.exists()
    assert source_map.exists()
    assert "30 / 60 / 120" in pilot_plan.read_text()
    assert "Point B readiness" in point_b.read_text()
    assert "Source-of-Truth Map" in source_map.read_text(encoding="utf-8")

    first_loop = output / "FIRST_OPERATING_LOOP.md"
    assert first_loop.exists()
    first_loop_text = first_loop.read_text(encoding="utf-8")
    for marker in [
        "30–60 minute first operating loop",
        "Pick exactly one safe internal task",
        "Before you ask an agent",
        "After the agent output",
        "Operational validation command",
    ]:
        assert marker in first_loop_text

    readme = (output / "README.md").read_text(encoding="utf-8")
    required_readme_markers = [
        "No subas esta instancia a un repositorio público",
        "company/company-brain.md",
        "company/source-of-truth-map.md",
        "company/approval-boundaries.md",
        "company/company-scorecard.md",
        "company/guided-pilot-plan.md",
        "FIRST_OPERATING_LOOP.md",
        "company/point-b-readiness.md",
        "departments/<department>/department-brain.md",
        "digital-employees/<employee>/PERMISSIONS.md",
        "context-packets/initial-company-context.md",
        "receipts/first-loop.md",
        "statechanges/",
        "roadmap/48h-7d-30d.md",
        "validate_point_b_readiness.py --mode scaffold",
        "--mode operational",
        "En una instancia recién generada, `--mode operational` debe fallar",
        "docs/TROUBLESHOOTING.md",
        "DIA UNO",
        "diauno.io",
        "contexto anonimizado",
    ]
    for marker in required_readme_markers:
        assert marker in readme
    assert "digital-employees/Dirección Assistant / CEO Operations Assistant/PERMISSIONS.md" not in readme

    verify = run_cmd([ROOT / "scripts" / "verify_installation.py", output])
    assert verify.returncode == 0, verify.stderr + verify.stdout
    scaffold_readiness = run_cmd([POINT_B_VALIDATOR, "--mode", "scaffold", output])
    assert scaffold_readiness.returncode == 0, scaffold_readiness.stderr + scaffold_readiness.stdout
    assert "Point B scaffold validation OK" in scaffold_readiness.stdout

    operational_readiness = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", output])
    assert operational_readiness.returncode == 1
    assert "Point B operational validation failed" in operational_readiness.stdout
    for marker in [
        "Next unblocker",
        "Open FIRST_OPERATING_LOOP.md",
        "create one human-reviewed internal loop",
        "rerun: python scripts/validate_point_b_readiness.py --mode operational",
    ]:
        assert marker in operational_readiness.stdout

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


def test_bootstrap_generates_verifiable_scaffold_without_operational_false_positive(tmp_path):
    output = tmp_path / "bootstrap-acme"
    result = run_cmd([
        BOOTSTRAP,
        "--company", "Bootstrap Acme",
        "--company-type", "agency",
        "--sector", "B2B services",
        "--owner", "Founder",
        "--output", output,
        "--yes",
    ])
    assert result.returncode == 0, result.stderr + result.stdout

    for rel in [
        "company/company-scorecard.md",
        "company/guided-pilot-plan.md",
        "company/point-b-readiness.md",
        "company/source-of-truth-map.md",
    ]:
        assert (output / rel).exists(), rel

    readme = (output / "README.md").read_text(encoding="utf-8")
    assert "digital-employees/Dirección Assistant / CEO Operations Assistant/PERMISSIONS.md" not in readme
    assert "digital-employees/ceo-operations-assistant/PERMISSIONS.md" in readme

    verify = run_cmd([ROOT / "scripts" / "verify_installation.py", output])
    assert verify.returncode == 0, verify.stderr + verify.stdout

    scaffold = run_cmd([POINT_B_VALIDATOR, "--mode", "scaffold", output])
    assert scaffold.returncode == 0, scaffold.stderr + scaffold.stdout

    operational = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", output])
    assert operational.returncode == 1
    assert "missing mandatory operational evidence" in operational.stdout.lower()


def write_operational_fixture(root: Path) -> None:
    files = {
        "company/company-brain.md": """
# Direction / Mother Brain
Owner: Founder
Source: leadership workshop
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: receipts/first-loop.md
Vision and mission are documented. Annual goal, rocks and OKRs are reviewed for the first operating slice.
""",
        "company/source-of-truth-map.md": """
# Source-of-Truth Map
Owner: Founder
Source: reviewed systems inventory 2026-05-20
Freshness: updated this week
Approval: human owner reviewed system access boundaries
Evidence: receipts/first-loop.md
This reviewed map was completed before creating context-packets/first-loop.md. Do not store credentials, tokens, API keys, passwords or connection strings.

| Tool/system | Owner | Data contained | Source-of-truth status | Agent read permission | Agent write/action permission | Sync cadence | Freshness / last reviewed | Receipt rule | Risks | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Drive / Docs | Founder | SOPs and delivery notes | partial | allowed read-only after review | approval required | weekly | reviewed this week | receipt when used in context packet | stale folders | separate current SOPs |
| Notion / wiki | Founder | operating decisions | partial | allowed read-only after review | approval required | weekly | reviewed this week | receipt for decision changes | outdated wiki | mark active pages |
| Sheets / spreadsheets | Founder | KPI tracker | yes | allowed read-only after review | approval required | weekly | reviewed this week | receipt for scorecard updates | formula errors | lock KPI source sheet |
| CRM | Sales lead | pipeline and handoffs | yes | allowed read-only after review | approval required before edits/messages | daily | reviewed this week | receipt for handoff decisions | incomplete fields | confirm handoff owner |
| WhatsApp / Slack | Operations lead | approved internal summaries | partial | approved extracts only | no messages without approval | per loop | reviewed this week | receipt cites approved extract | private chats | use anonymized summaries |
| Email | Founder | approved thread summaries | partial | approved extracts only | no sending without approval | per loop | reviewed this week | receipt cites approved extract | sensitive communication | keep drafts approval-gated |
""",
        "company/approval-boundaries.md": """
# Approval boundaries
Owner: Founder
Source: approval workshop
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: receipts/first-loop.md
External, economic, legal, production and sensitive actions require explicit human approval. Forbidden actions are listed.
""",
        "departments/operations/department-brain.md": """
# Operations Department Brain
Owner: Operations lead
Source: department review
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: receipts/first-loop.md
Responsibilities, workflows, scorecard, escalation path and operating cadence are defined for the first slice.
""",
        "digital-employees/ops-agent/PERMISSIONS.md": """
# Ops Agent Permissions
Owner: Founder
Source: role design
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: receipts/first-loop.md
Allowed actions, forbidden actions, tool boundaries, handoffs and approval gates are defined before active work.
""",
        "context-packets/first-loop.md": """
# First Loop Context Packet
Owner: Founder
Source: source-of-truth map
Freshness: reviewed this week
Approval: human owner reviewed
Evidence: receipts/first-loop.md
Goal, scope, sources, assumptions, risks, allowed actions, forbidden actions and expected outcome are complete.
""",
        "receipts/first-loop.md": """
# First Loop Receipt
Owner: Founder
Source: reviewed context-packets/first-loop.md
Freshness: completed this week
Approval: human owner reviewed
Evidence: scorecard update and reviewed output
Action performed: reviewed one internal operations-delivery handoff using the first-loop context packet.
Observed outcome: one internal operating loop was completed, reviewed and converted into the next sprint.
Next action: Sprint 2 will tighten the delivery handoff and rerun the margin check with human approval.
""",
        "company/company-scorecard.md": """
# Company Scorecard
Owner: Founder
Source: reviewed receipts/first-loop.md
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


def test_operational_validator_accepts_complete_first_loop_receipt(tmp_path):
    instance = tmp_path / "operational-complete-receipt"
    write_operational_fixture(instance)

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", instance])
    assert result.returncode == 0, result.stderr + result.stdout
    assert "Point B operational validation OK" in result.stdout


def test_operational_validator_requires_reviewed_source_of_truth_map(tmp_path):
    instance = tmp_path / "missing-source-of-truth-map"
    write_operational_fixture(instance)
    (instance / "company" / "source-of-truth-map.md").unlink()

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", "--min-score", "75", instance])
    assert result.returncode == 1
    assert "Source-of-truth map reviewed" in result.stdout
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


def test_operational_validator_rejects_generic_source_of_truth_map(tmp_path):
    instance = tmp_path / "generic-source-of-truth-map"
    write_operational_fixture(instance)
    (instance / "company" / "source-of-truth-map.md").write_text(
        """
# Source-of-Truth Map
Owner: Founder
Source: reviewed systems inventory 2026-05-20
Freshness: updated this week
Approval: human owner reviewed system access boundaries
Evidence: receipts/first-loop.md
The team reviewed company sources, permissions, freshness, approval and evidence. This generic note cites context-packets/first-loop.md and looks evidence-shaped, but it does not map concrete systems, read/write permissions, sync cadence, receipt rules, risks or next actions by system family. It mentions Tool/system, Source-of-truth status, Agent read permission, Agent write/action permission, Sync cadence, Freshness, Receipt rule, Risks, Next action, Drive, Notion, Sheets, CRM, WhatsApp and Email only as prose.
""".strip()
        + "\n",
        encoding="utf-8",
    )

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", "--min-score", "75", instance])
    assert result.returncode == 1
    assert "Source-of-truth map reviewed" in result.stdout
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


def test_operational_validator_rejects_source_map_with_unsafe_secret_handling(tmp_path):
    instance = tmp_path / "unsafe-secret-source-map"
    write_operational_fixture(instance)
    text = (instance / "company" / "source-of-truth-map.md").read_text(encoding="utf-8")
    (instance / "company" / "source-of-truth-map.md").write_text(
        text.replace(
            "Do not store credentials, tokens, API keys, passwords or connection strings.",
            "Store API keys and tokens in this file for faster agent access.",
        ),
        encoding="utf-8",
    )

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", "--min-score", "75", instance])
    assert result.returncode == 1
    assert "Source-of-truth map reviewed" in result.stdout
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


def test_operational_validator_accepts_concise_founder_owner(tmp_path):
    instance = tmp_path / "concise-founder-owner"
    write_operational_fixture(instance)

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", instance])
    assert result.returncode == 0, result.stderr + result.stdout
    assert "Point B operational validation OK" in result.stdout


def test_operational_validator_requires_receipt_context_packet_link_separate_from_source(tmp_path):
    instance = tmp_path / "receipt-source-no-context-packet"
    write_operational_fixture(instance)
    (instance / "receipts" / "first-loop.md").write_text(
        """
# First Loop Receipt
Owner: Founder
Source / provenance: founder notes and operator transcript
Freshness: completed this week
Approval: human owner reviewed
Evidence: scorecard update and reviewed output
Action performed: reviewed one internal operations-delivery handoff using approved source notes.
Observed outcome: one internal operating loop was completed, reviewed and converted into a decision.
Next action: Sprint 2 will tighten the delivery handoff and rerun the margin check with human approval.
""".strip()
        + "\n",
        encoding="utf-8",
    )

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", instance])
    assert result.returncode == 1
    assert "Operational receipt exists" in result.stdout
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


def test_operational_validator_rejects_receipt_without_explicit_action_outcome_next_lines(tmp_path):
    instance = tmp_path / "receipt-generic-prose-no-receipt-lines"
    write_operational_fixture(instance)
    (instance / "receipts" / "first-loop.md").write_text(
        """
# First Loop Receipt
Owner: Founder
Source: reviewed context-packets/first-loop.md
Freshness: completed this week
Approval: human owner reviewed
Evidence: scorecard update and reviewed output
The operator reviewed the internal handoff and the result was captured for the sprint. This generic prose mentions reviewed, result and sprint, but it intentionally omits explicit receipt lines for the performed action, observed outcome and next action.
""".strip()
        + "\n",
        encoding="utf-8",
    )

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", instance])
    assert result.returncode == 1
    assert "Operational receipt exists" in result.stdout
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


def test_operational_validator_rejects_installation_receipt_even_when_evidence_shaped(tmp_path):
    instance = tmp_path / "installation-receipt-renamed-risk"
    write_operational_fixture(instance)
    (instance / "receipts" / "first-loop.md").unlink()
    (instance / "receipts" / "installation-receipt.md").write_text(
        """
# Installation Receipt
Owner: Founder
Source: reviewed context-packets/first-loop.md
Freshness: completed this week
Approval: human owner reviewed
Evidence: company/company-scorecard.md
Action performed: installed the Company Brain folders and verified the installation output.
Observed outcome: the Company Brain installation exists with folders and starter files ready for review.
Next action: begin the first operational sprint after installation is complete.
""".strip()
        + "\n",
        encoding="utf-8",
    )

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", instance])
    assert result.returncode == 1
    assert "Operational receipt exists" in result.stdout
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


def test_operational_validator_rejects_day_0_installation_receipt_even_with_low_min_score(tmp_path):
    instance = tmp_path / "day-0-installation-receipt-risk"
    write_operational_fixture(instance)
    (instance / "receipts" / "first-loop.md").unlink()
    (instance / "receipts" / "day-0-installation-receipt.md").write_text(
        """
# Receipt — Day 0 Installation
Owner: Founder
Source: reviewed context-packets/first-loop.md
Freshness: completed this week
Approval: human owner reviewed
Evidence: company/company-scorecard.md
Action performed: installed files and ran verify_installation after the install.
Observed outcome: day-0 installation files were present and ready for an operational loop.
Next action: select the first operational sprint after installation.
""".strip()
        + "\n",
        encoding="utf-8",
    )

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", "--min-score", "1", instance])
    assert result.returncode == 1
    assert "Operational receipt exists" in result.stdout
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


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
        "company/source-of-truth-map.md",
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


def test_operational_validator_rejects_label_only_evidence_shape(tmp_path):
    instance = tmp_path / "label-only"
    files = [
        "company/company-brain.md",
        "company/source-of-truth-map.md",
        "company/approval-boundaries.md",
        "departments/operations/department-brain.md",
        "digital-employees/ops-agent/PERMISSIONS.md",
        "context-packets/first-loop.md",
        "receipts/first-loop.md",
        "company/company-scorecard.md",
        "company/guided-pilot-plan.md",
    ]
    label_only = """
# Label-only evidence document
Owner: Team
Source: Internal
Freshness: Current
Approval: Reviewed
Evidence: Done
This document has enough generic prose to look complete. It repeats operational words like owner, source, freshness, approval and evidence, but it does not provide dated provenance, a concrete owner, a reviewer, or a receipt or scorecard reference that can support a Punto B claim.
""".strip()
    for rel in files:
        path = instance / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(label_only + "\n", encoding="utf-8")

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", "--min-score", "1", instance])
    assert result.returncode == 1
    assert "missing mandatory operational evidence" in result.stdout.lower()
    assert "Point B operational validation OK" not in result.stdout


def write_spanish_operational_fixture(root: Path) -> None:
    files = {
        "company/company-brain.md": """
# Dirección / Mother Brain
Propietario: Fundadora operativa
Fuente: taller de dirección 2026-05-20
Vigencia: actualizado 2026-05-22
Aprobación: aprobado por responsable humana
Evidencia: receipts/first-loop.md
La visión, misión, meta anual, rocks y OKRs quedaron revisados para el primer ciclo operativo con responsables y decisiones trazables.
""",
        "company/source-of-truth-map.md": """
# Mapa de fuentes de verdad
Responsable: Fundadora operativa
Fuente: inventario de sistemas 2026-05-20
Actualización: actualizado 2026-05-22
Aprobacion requerida: aprobado por responsable humana antes de conectar herramientas
Prueba: receipts/first-loop.md
Este mapa revisado alimentó context-packets/first-loop.md. No almacenar credenciales, tokens, API keys, passwords ni connection strings.

| Sistema | Responsable | Datos | Estado de fuente de verdad | Permiso de lectura | Permiso de acción | Cadencia de sincronización | Actualización / última revisión | Regla de recibo | Riesgos | Siguiente acción |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Drive / Docs | Fundadora | SOPs y notas de entrega | parcial | lectura aprobada | aprobación requerida | semanal | revisado 2026-05-22 | recibo si alimenta paquete de contexto | carpetas antiguas | separar SOP vigente |
| Notion / wiki | Fundadora | decisiones operativas | parcial | lectura aprobada | aprobación requerida | semanal | revisado 2026-05-22 | recibo si cambia una decisión | wiki antigua | marcar páginas vigentes |
| Sheets / spreadsheets | Fundadora | KPIs y scorecard | sí | lectura aprobada | aprobación requerida | semanal | revisado 2026-05-22 | recibo para cambios de scorecard | fórmulas rotas | bloquear hoja fuente |
| CRM | Ventas | pipeline y traspasos | sí | lectura aprobada | aprobación requerida antes de editar | diario | revisado 2026-05-22 | recibo para traspasos | campos incompletos | confirmar owner del traspaso |
| WhatsApp / Slack | Operaciones | resúmenes internos aprobados | parcial | solo extractos aprobados | no enviar mensajes sin aprobación | por ciclo | revisado 2026-05-22 | recibo cita extracto aprobado | chats privados | usar resúmenes anonimizados |
| Email | Fundadora | resúmenes de hilos aprobados | parcial | solo extractos aprobados | no enviar correos sin aprobación | por ciclo | revisado 2026-05-22 | recibo cita extracto aprobado | comunicación sensible | mantener borradores con aprobación |
""",
        "company/approval-boundaries.md": """
# Límites de aprobación
Responsable: Fundadora operativa
Fuente / procedencia: revisión de riesgos 2026-05-20
Actualización: actualizado 2026-05-22
Aprobacion requerida: revisión humana antes de acciones sensibles
Prueba: receipts/first-loop.md
Acciones externas, económicas, legales, de producción y sensibles requieren aprobación humana explícita con escalado documentado.
""",
        "departments/operations/department-brain.md": """
# Cerebro del departamento de operaciones
Propietario: Líder de operaciones
Procedencia: revisión departamental 2026-05-20
Frescura: validado 2026-05-22
Aprobación requerida: aprobado por propietaria humana
Evidencia: receipts/first-loop.md
Responsabilidades, flujos de trabajo, scorecard, ruta de escalado y cadencia operativa están definidos para el primer corte.
""",
        "digital-employees/ops-agent/PERMISSIONS.md": """
# Permisos del agente de operaciones
Propietario: Fundadora operativa
Fuente: diseño de rol 2026-05-20
Vigencia: vigente 2026-05-22
Aprobación: aprobado por responsable humana
Evidencia: receipts/first-loop.md
Acciones permitidas, acciones prohibidas, límites de herramienta, traspasos y aprobaciones obligatorias están definidos antes del trabajo activo.
""",
        "context-packets/first-loop.md": """
# Paquete de contexto del primer ciclo
Responsable: Fundadora operativa
Fuente: mapa de fuentes 2026-05-20
Actualización: actualizado 2026-05-22
Aprobación: revisión humana completada
Prueba: receipts/first-loop.md
Objetivo, alcance, fuentes, supuestos, riesgos, acciones permitidas, acciones prohibidas y resultado esperado están completos.
""",
        "receipts/first-loop.md": """
# Recibo del primer ciclo
Propietario: Fundadora operativa
Fuente / procedencia: context-packets/first-loop.md revisado
Vigencia: completado 2026-05-22
Aprobacion: revisado por operadora humana
Evidencia: company/company-scorecard.md
Acción realizada: se revisó el paquete de contexto y se ejecutó un ciclo operativo interno.
Resultado observado: se completó un ciclo operativo interno, fue revisado y se convirtió en una decisión para el siguiente sprint.
Siguiente acción: el siguiente sprint ajustará el traspaso operativo con aprobación humana.
""",
        "company/company-scorecard.md": """
# Scorecard de compañía
Propietario: Fundadora operativa
Fuente: receipts/first-loop.md validado
Frescura: actualizado 2026-05-22
Aprobación: aprobado por responsable humana
Evidencia: receipts/first-loop.md
Las métricas se actualizaron desde evidencia operativa observada y no desde archivos de instalación o andamiaje.
""",
        "company/guided-pilot-plan.md": """
# Plan del piloto guiado
Responsable: Fundadora operativa
Procedencia: revisión del primer ciclo 2026-05-22
Vigencia: actualizado 2026-05-22
Aprobación requerida: revisión humana registrada
Prueba: receipts/first-loop.md
El siguiente sprint se seleccionó desde la evidencia revisada y tiene responsable, resultado esperado y puertas de aprobación claras.
""",
    }
    for rel, text in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text.strip() + "\n", encoding="utf-8")


def test_operational_validator_accepts_complete_spanish_evidence_labels(tmp_path):
    instance = tmp_path / "spanish-operational"
    write_spanish_operational_fixture(instance)

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", instance])
    assert result.returncode == 0, result.stderr + result.stdout
    assert "Point B operational validation OK" in result.stdout


def test_operational_validator_rejects_spanish_label_only_evidence_shape(tmp_path):
    instance = tmp_path / "spanish-label-only"
    files = [
        "company/company-brain.md",
        "company/source-of-truth-map.md",
        "company/approval-boundaries.md",
        "departments/operations/department-brain.md",
        "digital-employees/ops-agent/PERMISSIONS.md",
        "context-packets/first-loop.md",
        "receipts/first-loop.md",
        "company/company-scorecard.md",
        "company/guided-pilot-plan.md",
    ]
    label_only = """
# Documento con etiquetas genéricas
Propietario: Equipo
Fuente: Interno
Vigencia: Actual
Aprobación: Revisado
Evidencia: Hecho
Este documento tiene suficiente prosa genérica para parecer completo. Repite palabras operativas como propietario, fuente, vigencia, aprobación y evidencia, pero no aporta procedencia fechada, responsable concreto, revisión humana ni referencia a recibo o scorecard que sostenga una afirmación de Punto B.
""".strip()
    for rel in files:
        path = instance / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(label_only + "\n", encoding="utf-8")

    result = run_cmd([POINT_B_VALIDATOR, "--mode", "operational", "--min-score", "1", instance])
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

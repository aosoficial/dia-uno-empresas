from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WIZARD = ROOT / "scripts" / "company_brain_wizard.py"
VALIDATE = ROOT / "scripts" / "validate_installable_runtime.py"


def run_cmd(args):
    return subprocess.run(
        [sys.executable, *map(str, args)],
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=120,
    )


def test_sprint9_docs_and_templates_are_installed():
    required = [
        "docs/32_ai_first_readiness_assessment.md",
        "docs/33_department_selection_matrix.md",
        "docs/34_core_workflows_a_to_b.md",
        "docs/35_digital_employee_catalog.md",
        "docs/36_existing_systems_mapping.md",
        "docs/37_external_benchmarks_sylph_skillclaw.md",
        "docs/38_skill_evolution_v0.md",
        "templates/questionnaires/service-business-ai-first-intake.md",
        "templates/scorecards/service-business-scorecard.md",
        "templates/approval-matrix/service-business-approval-matrix.md",
        "templates/dia-uno/support-question-template.md",
        "templates/skill-evolution/candidate-skill-proposal.md",
    ]
    for rel in required:
        path = ROOT / rel
        assert path.exists(), rel
        assert len(path.read_text().split()) >= 40, rel


def test_wizard_dry_run_outputs_readiness_and_next_sprint(tmp_path):
    output = tmp_path / "acme"
    result = run_cmd([
        WIZARD,
        "--company", "Acme Studio",
        "--company-type", "agency",
        "--sector", "B2B services",
        "--owner", "Founder",
        "--output", output,
        "--maturity", "documented",
        "--departments", "direction,operations-delivery,sales,finance",
        "--dry-run",
    ])
    assert result.returncode == 0, result.stderr + result.stdout
    assert "AI-First readiness score:" in result.stdout
    assert "Recommended next sprint:" in result.stdout
    assert "Recommended departments now:" in result.stdout
    assert not output.exists()


def test_wizard_write_includes_readiness_score(tmp_path):
    output = tmp_path / "acme"
    result = run_cmd([
        WIZARD,
        "--company", "Acme Studio",
        "--company-type", "consultancy",
        "--sector", "B2B services",
        "--owner", "Founder",
        "--output", output,
        "--maturity", "assisted",
        "--departments", "direction,operations-delivery,customer-success,finance",
        "--yes",
    ])
    assert result.returncode == 0, result.stderr + result.stdout
    diagnosis = (output / "company" / "maturity-diagnosis.md").read_text()
    assert "AI-First readiness score" in diagnosis
    assert "Recommended next sprint" in diagnosis
    assert "Score by dimension" in diagnosis


def test_installable_runtime_knows_sprint9_assets():
    result = run_cmd([VALIDATE])
    assert result.returncode == 0, result.stderr + result.stdout
    assert "Installable accelerator validation OK" in result.stdout

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WIZARD = ROOT / "scripts" / "company_brain_wizard.py"
VERIFY = ROOT / "scripts" / "verify_installation.py"
VALIDATE = ROOT / "scripts" / "validate_installable_runtime.py"


def run_cmd(args, input_text=None):
    return subprocess.run(
        [sys.executable, *map(str, args)],
        input=input_text,
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=120,
    )


def test_wizard_interactive_mode_generates_tailored_department_assets(tmp_path):
    output = tmp_path / "acme-interactive"
    answers = "\n".join([
        "Acme Growth Studio",
        "agency",
        "B2B services",
        "Founder",
        "Knowledge in docs and chats; delivery depends on founder",
        "Install Dirección and run one delivery QA review",
        "all",
        str(output),
        "yes",
        "",
    ])
    result = run_cmd([WIZARD, "--interactive"], answers)
    assert result.returncode == 0, result.stderr + result.stdout
    assert (output / "company" / "department-rollout-map.md").exists()
    assert (output / "company" / "company-scorecard.md").exists()
    rollout = (output / "company" / "department-rollout-map.md").read_text()
    assert "operations-delivery" in rollout
    assert "admin-legal" in rollout
    scorecard = (output / "company" / "company-scorecard.md").read_text()
    assert "Point B outcome" in scorecard
    verify = run_cmd([VERIFY, output])
    assert verify.returncode == 0, verify.stderr + verify.stdout


def test_direction_and_operations_templates_have_depth_markers():
    for dept in ["direction", "operations-delivery"]:
        text = (ROOT / "templates" / "departments" / dept / "department-brain.md").read_text()
        for marker in [
            "Core operating questions",
            "Memory fields",
            "Day-1 task",
            "Weekly cadence",
            "Expected receipts",
            "Common failure modes",
        ]:
            assert marker in text, f"{dept} missing {marker}"
        assert len(text.split()) >= 300


def test_installable_runtime_validator_checks_depth():
    result = run_cmd([VALIDATE])
    assert result.returncode == 0, result.stderr + result.stdout
    assert "depth validation OK" in result.stdout

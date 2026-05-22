from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VALIDATE = ROOT / "scripts" / "validate_installable_runtime.py"
REQUIRED_SKILLS = [
    "product-discovery-brief",
    "prd-drafting",
    "web-launch-qa",
    "proposal-drafting",
    "lead-qualification",
    "client-onboarding",
    "delivery-qa",
    "weekly-review",
    "cashflow-review",
    "sop-writing",
]


def test_core_skill_templates_exist_with_operational_sections():
    for skill in REQUIRED_SKILLS:
        path = ROOT / "templates" / "skills" / f"{skill}.md"
        assert path.exists(), f"missing skill template {skill}"
        text = path.read_text()
        for marker in ["Trigger", "Inputs", "Steps", "Outputs", "Approval boundaries", "Receipt"]:
            assert marker in text, f"{skill} missing {marker}"
        assert len(text.split()) >= 120


def test_skills_registry_links_core_skill_templates():
    registry = (ROOT / "templates" / "generated-company-instance" / "skills" / "README.md").read_text()
    for skill in REQUIRED_SKILLS:
        assert f"templates/skills/{skill}.md" in registry


def test_validator_covers_skill_templates():
    result = subprocess.run([sys.executable, str(VALIDATE)], cwd=ROOT, text=True, capture_output=True, timeout=120)
    assert result.returncode == 0, result.stderr + result.stdout
    assert "skill template validation OK" in result.stdout

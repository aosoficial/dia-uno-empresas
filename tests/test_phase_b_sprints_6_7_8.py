from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_sprint6_memory_backend_profiles_are_installable_and_explicit():
    required = {
        "docs/31_memory_backend_profiles.md": [
            "Markdown local",
            "GBrain / MCP",
            "Supabase / API",
            "Client systems",
            "Selection matrix",
            "Data boundary",
            "Migration rule",
        ],
        "templates/memory-backends/markdown-local.md": ["Use when", "Setup", "Allowed data", "Forbidden data", "Receipts"],
        "templates/memory-backends/gbrain-mcp.md": ["Use when", "Setup", "Allowed data", "Forbidden data", "Receipts"],
        "templates/memory-backends/supabase-api.md": ["Use when", "Setup", "Allowed data", "Forbidden data", "Receipts"],
        "templates/memory-backends/client-systems.md": ["Use when", "Setup", "Allowed data", "Forbidden data", "Receipts"],
    }
    for rel, markers in required.items():
        path = ROOT / rel
        assert path.exists(), rel
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            assert marker in text, f"{rel} missing {marker}"


def test_sprint7_wizard_supports_maturity_diagnosis_and_dynamic_recommendations(tmp_path):
    output = tmp_path / "diagnosed-company"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "company_brain_wizard.py"),
        "--company", "Beta Consulting Lab",
        "--company-type", "consultancy",
        "--sector", "B2B advisory",
        "--owner", "Founder",
        "--output", str(output),
        "--maturity", "chaos",
        "--vertical", "consultancy",
        "--yes",
    ]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr + result.stdout
    diagnosis = output / "company" / "maturity-diagnosis.md"
    assert diagnosis.exists()
    text = diagnosis.read_text(encoding="utf-8")
    assert "Maturity level: `chaos`" in text
    assert "Vertical: `consultancy`" in text
    assert "Recommended first departments" in text
    assert "48h recommendation" in text
    assert "7-day recommendation" in text
    assert "30-day recommendation" in text


def test_sprint8_department_quality_validator_rejects_shallow_department(tmp_path):
    fixture = tmp_path / "instance"
    subprocess.run([
        sys.executable,
        str(ROOT / "scripts" / "company_brain_wizard.py"),
        "--company", "Gamma Agency",
        "--company-type", "agency",
        "--output", str(fixture),
        "--departments", "direction,operations-delivery,sales",
        "--yes",
    ], cwd=ROOT, check=True, text=True, capture_output=True)
    qa_cmd = [sys.executable, str(ROOT / "scripts" / "validate_department_quality.py"), str(fixture)]
    ok = subprocess.run(qa_cmd, cwd=ROOT, text=True, capture_output=True)
    assert ok.returncode == 0, ok.stderr + ok.stdout

    shallow = fixture / "departments" / "sales" / "department-brain.md"
    shallow.write_text("# Sales\n\nNo owner, no metrics, no approvals.", encoding="utf-8")
    bad = subprocess.run(qa_cmd, cwd=ROOT, text=True, capture_output=True)
    assert bad.returncode != 0
    assert "sales" in (bad.stdout + bad.stderr)
    assert "quality marker" in (bad.stdout + bad.stderr)

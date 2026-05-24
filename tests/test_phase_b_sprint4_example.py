from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "acme-agency-ai-first"

REQUIRED_FILES = [
    "README.md",
    "company/company-brain.md",
    "company/company-scorecard.md",
    "company/department-rollout-map.md",
    "context-packets/day-0-company-context.md",
    "context-packets/day-1-sales-to-operations-handoff.md",
    "receipts/day-0-installation-receipt.md",
    "receipts/day-1-first-digital-employee-run.md",
    "statechanges/day-1-operating-system-created.md",
    "handoffs/sales-to-operations.md",
    "roadmap/48h-7d-30d.md",
    "expected-verifier-output.txt",
]


def test_synthetic_example_has_full_operating_artifacts():
    for rel in REQUIRED_FILES:
        path = EXAMPLE / rel
        assert path.exists(), rel
        assert path.stat().st_size > 300, rel


def test_synthetic_example_is_fake_and_operational():
    combined = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in EXAMPLE.rglob("*.md"))
    required = [
        "synthetic",
        "fake company",
        "Direction / Mother Brain",
        "first digital employee",
        "receipt",
        "statechange",
        "context packet",
        "approval",
        "Punto A",
        "Punto B AI-First",
    ]
    for marker in required:
        assert marker.lower() in combined.lower(), marker
    forbidden = ["Jordi", "/Users/", "6084768324", "iCloud", "Documents/IA"]
    for marker in forbidden:
        assert marker not in combined, marker


def test_example_verifier_output_documents_success():
    text = (EXAMPLE / "expected-verifier-output.txt").read_text(encoding="utf-8")
    assert "Installation verification OK" in text
    assert "Acme Growth Studio" in text
    assert "124" in text or "files" in text.lower()

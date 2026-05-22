from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DEPARTMENTS = ["sales", "customer-success", "marketing"]
REQUIRED_BRAIN_MARKERS = [
    "## Mission and business outcome",
    "## Operating questions",
    "## Memory fields",
    "## Scorecard",
    "## Weekly cadence",
    "## Approval boundaries",
    "## Required receipts",
    "## Day-1 task",
    "context packet",
    "statechange",
    "receipt",
]

DIGITAL_EMPLOYEES = {
    "sales-assistant": ["lead qualification", "proposal", "follow-up", "human approval"],
    "customer-success-assistant": ["onboarding", "retention", "risk", "human approval"],
    "marketing-assistant": ["positioning", "content", "campaign", "human approval"],
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_sales_cs_marketing_department_brains_are_operational_not_placeholders():
    for department in DEPARTMENTS:
        text = read(f"templates/departments/{department}/department-brain.md")
        assert len(text) >= 2500, department
        for marker in REQUIRED_BRAIN_MARKERS:
            assert marker in text, f"{department} missing {marker}"
        assert "Metric 1" not in text
        assert "Metric 2" not in text
        assert "Metric 3" not in text


def test_sprint2_digital_employee_packs_exist_with_permissions_memory_and_ops():
    base = ROOT / "templates/generated-company-instance/digital-employees"
    for employee, markers in DIGITAL_EMPLOYEES.items():
        folder = base / employee
        assert folder.exists(), employee
        for filename in ["SOUL.md", "PERMISSIONS.md", "MEMORY.md", "OPERATIONS.md"]:
            text = (folder / filename).read_text(encoding="utf-8")
            assert len(text) >= 500, f"{employee}/{filename} too shallow"
            assert "receipt" in text.lower()
            assert "approval" in text.lower() or "human" in text.lower()
        combined = "\n".join((folder / filename).read_text(encoding="utf-8").lower() for filename in ["SOUL.md", "PERMISSIONS.md", "MEMORY.md", "OPERATIONS.md"])
        for marker in markers:
            assert marker in combined, f"{employee} missing {marker}"


def test_wizard_mentions_sprint2_digital_employee_generation():
    wizard = read("scripts/company_brain_wizard.py")
    for employee in DIGITAL_EMPLOYEES:
        assert employee in wizard
    assert "digital-employees" in wizard

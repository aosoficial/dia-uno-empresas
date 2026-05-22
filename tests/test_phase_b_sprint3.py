from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DEPARTMENTS = ["finance", "people", "admin-legal"]
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
    "finance-assistant": ["cashflow", "invoice", "margin", "human approval"],
    "people-assistant": ["accountability", "role", "meeting", "human approval"],
    "admin-legal-assistant": ["contract", "compliance", "risk", "human approval"],
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_finance_people_admin_department_brains_are_operational():
    for department in DEPARTMENTS:
        text = read(f"templates/departments/{department}/department-brain.md")
        assert len(text) >= 2400, department
        for marker in REQUIRED_BRAIN_MARKERS:
            assert marker in text, f"{department} missing {marker}"
        assert "Metric 1" not in text
        assert "Metric 2" not in text
        assert "Metric 3" not in text


def test_sprint3_digital_employee_packs_exist():
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


def test_wizard_mentions_sprint3_digital_employee_generation():
    wizard = read("scripts/company_brain_wizard.py")
    for employee in DIGITAL_EMPLOYEES:
        assert employee in wizard

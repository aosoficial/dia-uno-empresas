from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OBSERVER_FILES = [
    "docs/48_observer_read_only_runtime.md",
    "templates/generated-company-instance/digital-employees/observer/SOUL.md",
    "templates/generated-company-instance/digital-employees/observer/OPERATIONS.md",
    "templates/generated-company-instance/digital-employees/observer/PERMISSIONS.md",
    "templates/generated-company-instance/digital-employees/observer/MEMORY.md",
    "templates/generated-company-instance/digital-employees/observer/TOOLS.md",
    "templates/generated-company-instance/digital-employees/observer/IDENTITY.md",
]

REQUIRED_MARKERS = [
    "read-only",
    "daily digest",
    "approved Slack",
    "Company Brain",
    "GBrain",
    "receipts",
    "StateChanges",
    "approval",
    "runtime health",
    "escalation",
    "secrets",
    "raw traces",
]


def test_observer_runtime_pack_exists_and_is_operational():
    for rel in OBSERVER_FILES:
        path = ROOT / rel
        assert path.exists(), rel
        text = path.read_text(encoding="utf-8")
        assert len(text.split()) >= 120, rel


def test_observer_playbook_contains_required_guardrails():
    combined = "\n".join((ROOT / rel).read_text(encoding="utf-8") for rel in OBSERVER_FILES)
    lower = combined.lower()
    for marker in REQUIRED_MARKERS:
        assert marker.lower() in lower, marker

    forbidden = [
        "contact external",
        "spend",
        "publish",
        "production",
        "change permissions",
        "service-role",
    ]
    for marker in forbidden:
        assert marker in lower, marker


def test_installable_validator_requires_observer_playbook():
    validator = (ROOT / "scripts" / "validate_installable_runtime.py").read_text(encoding="utf-8")
    assert "docs/48_observer_read_only_runtime.md" in validator

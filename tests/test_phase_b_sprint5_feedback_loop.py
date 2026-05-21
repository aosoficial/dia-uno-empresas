from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "templates/feedback-loop/human-correction.md",
    "templates/feedback-loop/change-proposal.md",
    "templates/feedback-loop/change-contract.md",
    "templates/feedback-loop/statechange.md",
    "templates/feedback-loop/skill-update-receipt.md",
    "docs/30_feedback_loop_playbook.md",
]

MARKERS = [
    "human correction",
    "change proposal",
    "change contract",
    "statechange",
    "skill/template update",
    "receipt",
    "approval",
    "rollback",
    "validation",
]


def test_feedback_loop_templates_exist_and_are_operational():
    for rel in REQUIRED:
        path = ROOT / rel
        assert path.exists(), rel
        text = path.read_text(encoding="utf-8")
        assert len(text.split()) >= 120, rel
        for marker in ["Owner", "Source", "Approval", "Evidence"]:
            assert marker.lower() in text.lower(), f"{rel} missing {marker}"


def test_feedback_loop_playbook_contains_full_loop():
    text = (ROOT / "docs/30_feedback_loop_playbook.md").read_text(encoding="utf-8")
    for marker in MARKERS:
        assert marker in text.lower(), marker
    ordered = ["capture", "propose", "contract", "implement", "validate", "receipt", "statechange"]
    lower = text.lower()
    positions = [lower.find(x) for x in ordered]
    assert all(p >= 0 for p in positions)
    assert positions == sorted(positions)


def test_runtime_validator_requires_feedback_loop_assets():
    text = (ROOT / "scripts" / "validate_installable_runtime.py").read_text(encoding="utf-8")
    for rel in REQUIRED:
        assert rel in text

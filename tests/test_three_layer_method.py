from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIZARD = ROOT / "scripts" / "company_brain_wizard.py"
BOOTSTRAP = ROOT / "scripts" / "bootstrap_company_brain.py"
VERIFY = ROOT / "scripts" / "verify_installation.py"
PEOPLE_VALIDATE = ROOT / "scripts" / "validate_people_readiness.py"
POINT_B_VALIDATE = ROOT / "scripts" / "validate_point_b_readiness.py"
METHOD_VALIDATE = ROOT / "scripts" / "validate_method_layers.py"


def run_cmd(args: list[object]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *map(str, args)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=180,
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_method_inventory_preserves_all_36_originals():
    result = run_cmd([METHOD_VALIDATE])
    assert result.returncode == 0, result.stderr + result.stdout
    assert "36/36 originals verified" in result.stdout

    root = ROOT / "personas" / "metodo-v3"
    manifest = {}
    for line in (root / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        manifest[relative] = digest
    assert len(manifest) == 36
    assert sum(relative.endswith(".docx") for relative in manifest) == 29
    assert sum(relative.endswith(".xlsx") for relative in manifest) == 7
    for relative, expected in manifest.items():
        assert sha256(root / relative) == expected


def test_readme_exposes_people_agents_and_hybrid_layers():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in [
        "**Personas**",
        "**Agentes**",
        "**Sistema Híbrido**",
        "Organizar personas → Agentizar capacidades maduras → Escalar el sistema híbrido",
        "--method-mode people",
        "--upgrade",
    ]:
        assert marker in readme

    matrix = (ROOT / "sistema-hibrido" / "matriz-de-equivalencias.md").read_text(encoding="utf-8")
    for marker in ["Ficha de puesto", "Matriz de decisiones", "SOP", "Evaluación de persona"]:
        assert marker in matrix


def test_people_mode_installs_human_method_without_agent_scaffolds(tmp_path):
    output = tmp_path / "people-company"
    result = run_cmd([
        WIZARD,
        "--company", "People Company",
        "--company-type", "agency",
        "--owner", "Founder",
        "--method-mode", "people",
        "--output", output,
        "--yes",
    ])
    assert result.returncode == 0, result.stderr + result.stdout
    method = json.loads((output / "METHOD.json").read_text(encoding="utf-8"))
    assert method["method_mode"] == "people"
    assert method["human_accountable"] == "Founder"
    assert not (output / "digital-employees").exists()
    assert not (output / "departments").exists()
    assert not (output / "integrations").exists()
    assert not (output / "FIRST_OPERATING_LOOP.md").exists()
    assert not (output / "roadmap").exists()
    assert not (output / "examples").exists()
    assert len(list((output / "personas" / "metodo-v3" / "originales").rglob("*.*"))) == 36

    verify = run_cmd([VERIFY, output])
    assert verify.returncode == 0, verify.stderr + verify.stdout
    people = run_cmd([PEOPLE_VALIDATE, output])
    assert people.returncode == 0, people.stderr + people.stdout
    assert "does not prove" in people.stdout


def test_hybrid_mode_keeps_people_layer_and_agent_scaffolds(tmp_path):
    output = tmp_path / "hybrid-company"
    result = run_cmd([
        WIZARD,
        "--company", "Hybrid Company",
        "--company-type", "consultancy",
        "--method-mode", "hybrid",
        "--output", output,
        "--yes",
    ])
    assert result.returncode == 0, result.stderr + result.stdout
    assert (output / "personas" / "metodo-v3" / "MANIFEST.sha256").exists()
    assert (output / "departments" / "direction" / "department-brain.md").exists()
    assert (output / "digital-employees" / "ceo" / "PERMISSIONS.md").exists()
    assert run_cmd([VERIFY, output]).returncode == 0
    assert run_cmd([PEOPLE_VALIDATE, output]).returncode == 0
    scaffold = run_cmd([POINT_B_VALIDATE, "--mode", "scaffold", output])
    assert scaffold.returncode == 0, scaffold.stderr + scaffold.stdout


def test_people_to_hybrid_upgrade_is_additive_and_preserves_work(tmp_path):
    output = tmp_path / "upgrade-company"
    create = run_cmd([
        WIZARD,
        "--company", "Upgrade Company",
        "--company-type", "freelancer",
        "--method-mode", "people",
        "--output", output,
        "--yes",
    ])
    assert create.returncode == 0, create.stderr + create.stdout
    working_file = output / "company" / "people-organization-plan.md"
    working_file.write_text(working_file.read_text(encoding="utf-8") + "\nPRESERVE-COMPANY-WORK\n", encoding="utf-8")

    upgrade = run_cmd([
        WIZARD,
        "--company", "Upgrade Company",
        "--company-type", "freelancer",
        "--method-mode", "hybrid",
        "--output", output,
        "--upgrade",
        "--yes",
    ])
    assert upgrade.returncode == 0, upgrade.stderr + upgrade.stdout
    assert "PRESERVE-COMPANY-WORK" in working_file.read_text(encoding="utf-8")
    assert (output / "receipts" / "people-to-hybrid-upgrade-receipt.md").exists()
    assert (output / "HYBRID_CONTINUATION.md").exists()
    assert "scaffold_not_operational" in (output / "HYBRID_CONTINUATION.md").read_text(encoding="utf-8")
    assert (output / "digital-employees" / "ceo" / "PERMISSIONS.md").exists()
    method = json.loads((output / "METHOD.json").read_text(encoding="utf-8"))
    assert method["method_mode"] == "hybrid"
    assert method["status"] == "scaffold_not_operational"
    assert run_cmd([VERIFY, output]).returncode == 0
    assert run_cmd([POINT_B_VALIDATE, "--mode", "scaffold", output]).returncode == 0


def test_upgrade_refuses_modified_preserved_original(tmp_path):
    output = tmp_path / "tampered-people-company"
    create = run_cmd([
        WIZARD,
        "--company", "Tampered People Company",
        "--company-type", "agency",
        "--method-mode", "people",
        "--output", output,
        "--yes",
    ])
    assert create.returncode == 0, create.stderr + create.stdout
    original = next((output / "personas" / "metodo-v3" / "originales").rglob("*.docx"))
    original.write_bytes(original.read_bytes() + b"tampered")

    upgrade = run_cmd([
        WIZARD,
        "--company", "Tampered People Company",
        "--company-type", "agency",
        "--method-mode", "hybrid",
        "--output", output,
        "--upgrade",
        "--yes",
    ])
    assert upgrade.returncode == 2
    assert "failed integrity validation" in upgrade.stderr
    assert not (output / "digital-employees").exists()


def test_bootstrap_people_mode_matches_wizard_boundaries(tmp_path):
    output = tmp_path / "bootstrap-people-company"
    result = run_cmd([
        BOOTSTRAP,
        "--company", "Bootstrap People Company",
        "--company-type", "consultancy",
        "--method-mode", "people",
        "--output", output,
        "--yes",
    ])
    assert result.returncode == 0, result.stderr + result.stdout
    assert not (output / "digital-employees").exists()
    assert not (output / "departments").exists()
    assert not (output / "integrations").exists()
    assert not (output / "FIRST_OPERATING_LOOP.md").exists()
    assert not (output / "roadmap").exists()
    assert not (output / "examples").exists()
    assert run_cmd([VERIFY, output]).returncode == 0
    assert run_cmd([PEOPLE_VALIDATE, output]).returncode == 0


def test_verifier_keeps_legacy_hybrid_instances_compatible(tmp_path):
    output = tmp_path / "legacy-hybrid-company"
    result = run_cmd([
        WIZARD,
        "--company", "Legacy Hybrid Company",
        "--company-type", "agency",
        "--method-mode", "hybrid",
        "--output", output,
        "--yes",
    ])
    assert result.returncode == 0, result.stderr + result.stdout
    (output / "METHOD.json").unlink()
    verify = run_cmd([VERIFY, output])
    assert verify.returncode == 0, verify.stderr + verify.stdout
    assert "hybrid scaffold, legacy compatibility" in verify.stdout

#!/usr/bin/env python3
"""Validate Company Brain scaffold or operational Point B readiness.

Two modes are intentionally separate:
- scaffold: checks that the generated instance has the expected shape.
- operational: checks that an assisted first operating slice has real evidence.

A fresh wizard scaffold must pass scaffold mode and fail operational mode.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Criterion:
    name: str
    points: int
    patterns: tuple[str, ...]
    detail: str


SCAFFOLD_CRITERIA = (
    Criterion("Direction / Mother Brain file exists", 10, ("company/company-brain.md",), "Create company/company-brain.md."),
    Criterion("Direction governance files exist", 8, ("company/annual-plan.md", "company/okrs.md", "company/org-chart.md", "company/roles-and-responsibilities.md"), "Create annual plan, OKRs, org chart and roles files to close the Direction chain."),
    Criterion("Source-of-truth map file exists", 10, ("company/source-of-truth-map.md",), "Create company/source-of-truth-map.md before the first Context Packet."),
    Criterion("Approval boundaries file exists", 10, ("company/approval-boundaries.md",), "Create company/approval-boundaries.md."),
    Criterion("Priority department scaffold exists", 12, ("departments/*/department-brain.md",), "Install at least one department brain."),
    Criterion("Digital employee permissions file exists", 12, ("digital-employees/*/PERMISSIONS.md",), "Create at least one digital employee permissions file."),
    Criterion("Context packet scaffold exists", 10, ("context-packets/*.md",), "Create a context packet scaffold."),
    Criterion("Installation receipt exists", 10, ("receipts/*.md",), "Write an installation or pilot receipt."),
    Criterion("Scorecard scaffold exists", 10, ("company/company-scorecard.md", "company/point-b-readiness.md"), "Create scorecard/readiness files."),
    Criterion("Next sprint plan exists", 8, ("company/guided-pilot-plan.md",), "Create company/guided-pilot-plan.md with next sprint."),
)

OPERATIONAL_CRITERIA = (
    Criterion("Direction / Mother Brain installed", 12, ("company/company-brain.md",), "Replace Direction placeholders with reviewed vision, mission, annual goal/rocks/OKRs and operating owner."),
    Criterion("Source-of-truth map reviewed", 12, ("company/source-of-truth-map.md",), "Complete the source-of-truth map with owners, freshness, permissions, risks and evidence before creating the first Context Packet."),
    Criterion("Approval boundaries reviewed", 12, ("company/approval-boundaries.md",), "Define human approval gates for external, economic, legal, production and sensitive actions."),
    Criterion("Priority department operating", 12, ("departments/*/department-brain.md",), "Complete one department brain with responsibilities, workflows, scorecard and escalation path."),
    Criterion("Digital employee permissions active", 12, ("digital-employees/*/PERMISSIONS.md",), "Define one role/position agent with allowed actions, forbidden actions and required approvals."),
    Criterion("Operational context packet exists", 10, ("context-packets/*.md",), "Create a non-placeholder context packet for the first human-reviewed loop."),
    Criterion("Operational receipt exists", 10, ("receipts/*.md",), "Write a receipt for an actual human-reviewed operating loop, not only installation."),
    Criterion("Scorecard updated from evidence", 10, ("company/company-scorecard.md", "company/point-b-readiness.md"), "Update a scorecard/readiness file from observed operating evidence."),
    Criterion("Next sprint selected from review", 10, ("company/guided-pilot-plan.md",), "Select next sprint from the evidence review."),
)

SCAFFOLD_ONLY_NAMES = {
    "initial-company-context.md",
    "wizard-installation-receipt.md",
}

PLACEHOLDER_MARKERS = (
    "replace this",
    "replace with",
    "todo",
    "tbd",
    "placeholder",
    "draft until reviewed",
    "draft until validated",
    "fill in",
    "fill privately",
    "assign before active work",
    "unknown",
    "example only",
    "generated",
    "generated scaffold",
    "unchecked evidence",
)

SYNTHETIC_MARKERS = (
    "synthetic",
    "fake company",
    "acme agency",
    "example operator",
    "northstar analytics",
)

REQUIRED_OPERATIONAL_MARKERS = (
    "owner",
    "source",
    "freshness",
    "approval",
    "evidence",
)

FIELD_LABEL_ALIASES = {
    "owner": "owner",
    "propietario": "owner",
    "responsable": "owner",
    "source": "source",
    "source / provenance": "source",
    "fuente": "source",
    "fuente / procedencia": "source",
    "procedencia": "source",
    "freshness": "freshness",
    "vigencia": "freshness",
    "actualización": "freshness",
    "actualizacion": "freshness",
    "frescura": "freshness",
    "approval": "approval",
    "required approval": "approval",
    "aprobación": "approval",
    "aprobacion": "approval",
    "aprobación requerida": "approval",
    "aprobacion requerida": "approval",
    "evidence": "evidence",
    "evidencia": "evidence",
    "prueba": "evidence",
}
FIELD_LABEL_PATTERN = "|".join(re.escape(label) for label in sorted(FIELD_LABEL_ALIASES, key=len, reverse=True))
FIELD_LINE_RE = re.compile(rf"^\s*({FIELD_LABEL_PATTERN})\s*:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
FIELD_HEADING_RE = re.compile(rf"^#{{2,6}}\s+({FIELD_LABEL_PATTERN})\s*$\n+(.+?)(?=\n#{{1,6}}\s+|\Z)", re.IGNORECASE | re.MULTILINE | re.DOTALL)
DATE_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2}|20\d{2}/\d{2}/\d{2}|20\d{2})\b")
GENERIC_FIELD_VALUES = {
    "",
    "done",
    "complete",
    "completed",
    "reviewed",
    "current",
    "ok",
    "yes",
    "n/a",
    "na",
    "none",
    "team",
    "internal",
    "actual",
    "equipo",
    "hecho",
    "interno",
    "revisado",
}

OPERATIONAL_RECEIPT_CRITERION = "Operational receipt exists"
SOURCE_OF_TRUTH_MAP_CRITERION = "Source-of-truth map reviewed"
SOURCE_MAP_REQUIRED_MARKERS = (
    "tool/system",
    "source-of-truth status",
    "agent read permission",
    "agent write/action permission",
    "sync cadence",
    "freshness",
    "receipt rule",
    "risks",
    "next action",
)
SOURCE_MAP_TABLE_HEADER_ALIASES = {
    "tool": ("tool/system", "tool", "system", "sistema", "herramienta"),
    "owner": ("owner", "propietario", "responsable"),
    "source_status": ("source-of-truth status", "source status", "estado de fuente", "estado fuente", "fuente de verdad"),
    "read_permission": ("agent read permission", "read permission", "permiso de lectura", "lectura del agente"),
    "write_permission": ("agent write/action permission", "write/action permission", "permiso de escritura", "permiso de acción", "permiso de accion"),
    "sync_cadence": ("sync cadence", "cadencia de sincronización", "cadencia de sincronizacion", "cadencia"),
    "freshness": ("freshness", "last reviewed", "vigencia", "frescura", "actualización", "actualizacion", "última revisión", "ultima revision"),
    "receipt_rule": ("receipt rule", "regla de recibo", "regla de evidencia", "regla de prueba"),
    "risks": ("risks", "riesgos"),
    "next_action": ("next action", "siguiente acción", "siguiente accion", "próxima acción", "proxima accion"),
}
SOURCE_MAP_REQUIRED_COLUMNS = (
    "tool",
    "owner",
    "source_status",
    "read_permission",
    "write_permission",
    "sync_cadence",
    "freshness",
    "receipt_rule",
    "risks",
    "next_action",
)
SOURCE_MAP_SYSTEM_FAMILIES = (
    ("drive", "docs", "document"),
    ("notion", "wiki"),
    ("sheets", "spreadsheet", "hoja"),
    ("crm", "pipeline"),
    ("whatsapp", "slack", "chat"),
    ("email", "correo", "inbox"),
)
SOURCE_MAP_PERMISSION_MARKERS = (
    "read-only",
    "read only",
    "lectura",
    "approval required",
    "aprobación requerida",
    "aprobacion requerida",
    "human review",
    "human owner",
)
SOURCE_MAP_PRIVACY_MARKERS = (
    "do not store credentials",
    "no credentials",
    "sin credenciales",
    "tokens",
    "api keys",
    "passwords",
    "connection strings",
)
SOURCE_MAP_PRIVACY_GUARDRAIL_RE = re.compile(
    r"(do not|don't|never|no|sin|no almacenar|no guardar)[^.\n]*(credentials|credenciales|tokens|api keys|passwords|contraseñas|contrasenas|connection strings|secret)",
    re.IGNORECASE,
)
INSTALLATION_RECEIPT_NAME_RE = re.compile(r"(installation|install|day[-_ ]?0|scaffold|verify_installation)", re.IGNORECASE)
INSTALLATION_RECEIPT_CONTENT_MARKERS = (
    "installation receipt",
    "wizard installation",
    "installation output",
    "installation files",
    "install files",
    "installed files",
    "installed the company brain",
    "verify_installation",
    "generated scaffold",
    "scaffold only",
    "scaffold files",
    "day 0 installation",
    "day-0 installation",
)
RECEIPT_ACTION_LABELS = ("action performed", "performed action", "what changed", "work completed", "acción realizada", "accion realizada", "qué cambió", "que cambio")
RECEIPT_OUTCOME_LABELS = ("observed outcome", "outcome observed", "outcome", "observed result", "result observed", "resultado observado", "resultado")
RECEIPT_CONTEXT_PACKET_MARKERS = ("context-packets/", "context packet", "paquete de contexto", "paquete contextual")
RECEIPT_REVIEW_MARKERS = ("human", "owner reviewed", "reviewed by", "approved by", "required approval", "approval", "humana", "humano", "revisado por", "aprobado por", "aprobación", "aprobacion")
RECEIPT_NEXT_LABELS = ("next action", "next sprint", "allowed next actions", "next step", "next steps", "siguiente sprint", "próxima acción", "proxima accion", "siguiente acción", "siguiente accion")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def normalized_field_value(value: str) -> str:
    return value.strip().strip("`*_ .").lower()


def canonical_field_label(label: str) -> str:
    return FIELD_LABEL_ALIASES[label.strip().casefold()]


def operational_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for match in FIELD_LINE_RE.finditer(text):
        key = canonical_field_label(match.group(1))
        fields[key] = match.group(2).strip()
    for match in FIELD_HEADING_RE.finditer(text):
        key = canonical_field_label(match.group(1))
        fields.setdefault(key, " ".join(match.group(2).strip().split()))
    return fields


def has_evidence_shape(text: str, *, allow_synthetic: bool) -> bool:
    fields = operational_fields(text)
    if not all(marker in fields for marker in REQUIRED_OPERATIONAL_MARKERS):
        return False

    for marker in REQUIRED_OPERATIONAL_MARKERS:
        value = normalized_field_value(fields[marker])
        if value in GENERIC_FIELD_VALUES:
            return False
        if marker not in ("owner", "evidence") and len(value.split()) < 2:
            return False

    freshness = fields["freshness"].lower()
    if not (DATE_RE.search(freshness) or "this week" in freshness or "esta semana" in freshness or "current" in freshness or "vigente" in freshness or (allow_synthetic and "synthetic" in freshness)):
        return False

    evidence = fields["evidence"].lower()
    if not ("/" in evidence or ".md" in evidence or "receipt" in evidence or "recibo" in evidence or "scorecard" in evidence or "cuadro de mando" in evidence or (allow_synthetic and "synthetic" in evidence)):
        return False

    approval = fields["approval"].lower()
    if not any(marker in approval for marker in ("human", "owner", "review", "approved", "approval", "operator", "humano", "humana", "propietario", "propietaria", "responsable", "revisión", "revision", "aprobado", "aprobada", "aprobación", "aprobacion", "operador", "operadora")):
        return False

    return True


def matching_files(root: Path, criterion: Criterion) -> list[Path]:
    matches: list[Path] = []
    for pattern in criterion.patterns:
        matches.extend(path for path in root.glob(pattern) if path.is_file() and path.stat().st_size > 0)
    return sorted(set(matches))


def has_scaffold_evidence(root: Path, criterion: Criterion) -> bool:
    return bool(matching_files(root, criterion))


def is_substantive(path: Path, *, allow_synthetic: bool) -> bool:
    if path.name in SCAFFOLD_ONLY_NAMES:
        return False

    text = read_text(path)
    lowered = text.lower()
    word_count = len(text.split())
    if word_count < 25:
        return False

    if not allow_synthetic and any(marker in lowered for marker in SYNTHETIC_MARKERS):
        return False

    if any(marker in lowered for marker in PLACEHOLDER_MARKERS):
        return False

    if not has_evidence_shape(text, allow_synthetic=allow_synthetic):
        return False

    return True


def has_any_marker(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)


def has_receipt_label(text: str, labels: tuple[str, ...]) -> bool:
    label_pattern = "|".join(re.escape(label) for label in sorted(labels, key=len, reverse=True))
    return bool(re.search(rf"^\s*(?:#{{2,6}}\s+)?(?:{label_pattern})\s*:?\s*", text, re.IGNORECASE | re.MULTILINE))


def is_installation_only_receipt(path: Path, text: str) -> bool:
    lowered = text.lower()
    if INSTALLATION_RECEIPT_NAME_RE.search(path.name):
        return True
    if has_any_marker(lowered, INSTALLATION_RECEIPT_CONTENT_MARKERS):
        return True
    if ("day-0" in lowered or "day 0" in lowered) and any(marker in lowered for marker in ("install", "installation", "scaffold")):
        return True
    return False


def has_operational_receipt_shape(path: Path, *, allow_synthetic: bool) -> bool:
    if not is_substantive(path, allow_synthetic=allow_synthetic):
        return False

    text = read_text(path)
    lowered = text.lower()
    if is_installation_only_receipt(path, text):
        return False

    return (
        has_receipt_label(text, RECEIPT_ACTION_LABELS)
        and has_receipt_label(text, RECEIPT_OUTCOME_LABELS)
        and "source" in operational_fields(text)
        and has_any_marker(lowered, RECEIPT_CONTEXT_PACKET_MARKERS)
        and has_any_marker(lowered, RECEIPT_REVIEW_MARKERS)
        and has_receipt_label(text, RECEIPT_NEXT_LABELS)
    )


def markdown_table_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells):
            continue
        rows.append(cells)
    return rows


def normalize_table_cell(value: str) -> str:
    return " ".join(value.strip().strip("`*_ ").casefold().split())


def source_map_column_indexes(header: list[str]) -> dict[str, int]:
    normalized_header = [normalize_table_cell(cell) for cell in header]
    indexes: dict[str, int] = {}
    for canonical, aliases in SOURCE_MAP_TABLE_HEADER_ALIASES.items():
        for index, cell in enumerate(normalized_header):
            if any(alias in cell for alias in aliases):
                indexes[canonical] = index
                break
    return indexes


def source_map_cell_value(row: list[str], index: int) -> str:
    if index >= len(row):
        return ""
    return normalized_field_value(row[index])


def is_specific_source_map_row(row: list[str], indexes: dict[str, int]) -> bool:
    for column in SOURCE_MAP_REQUIRED_COLUMNS:
        value = source_map_cell_value(row, indexes[column])
        if len(value) < 2:
            return False
        if column in {"tool", "owner", "risks", "next_action"} and value in GENERIC_FIELD_VALUES:
            return False
    return True


def source_map_table_has_required_rows(text: str) -> bool:
    rows = markdown_table_rows(text)
    for header_index, header in enumerate(rows):
        indexes = source_map_column_indexes(header)
        if not all(column in indexes for column in SOURCE_MAP_REQUIRED_COLUMNS):
            continue
        data_rows = [row for row in rows[header_index + 1 :] if len(row) >= len(header) - 1]
        if not data_rows or not all(is_specific_source_map_row(row, indexes) for row in data_rows):
            continue
        covered_families: set[int] = set()
        for row in data_rows:
            tool = source_map_cell_value(row, indexes["tool"])
            for family_index, aliases in enumerate(SOURCE_MAP_SYSTEM_FAMILIES):
                if any(alias in tool for alias in aliases):
                    covered_families.add(family_index)
        if len(covered_families) == len(SOURCE_MAP_SYSTEM_FAMILIES):
            return True
    return False


def has_source_of_truth_map_shape(path: Path, *, allow_synthetic: bool) -> bool:
    """Require a real systems map, not a generic evidence-shaped document."""
    if not is_substantive(path, allow_synthetic=allow_synthetic):
        return False

    text = read_text(path)
    lowered = text.lower()
    if not source_map_table_has_required_rows(text):
        return False
    if not any(marker in lowered for marker in SOURCE_MAP_PERMISSION_MARKERS):
        return False
    if not SOURCE_MAP_PRIVACY_GUARDRAIL_RE.search(text):
        return False
    if "context-packets/" not in lowered and "context packet" not in lowered and "paquete de contexto" not in lowered:
        return False
    return True


def has_operational_evidence(root: Path, criterion: Criterion, *, allow_synthetic: bool) -> bool:
    if criterion.name == OPERATIONAL_RECEIPT_CRITERION:
        return any(has_operational_receipt_shape(path, allow_synthetic=allow_synthetic) for path in matching_files(root, criterion))
    if criterion.name == SOURCE_OF_TRUTH_MAP_CRITERION:
        return any(has_source_of_truth_map_shape(path, allow_synthetic=allow_synthetic) for path in matching_files(root, criterion))
    return any(is_substantive(path, allow_synthetic=allow_synthetic) for path in matching_files(root, criterion))


def readiness_level(score: int, *, mode: str) -> str:
    if mode == "scaffold":
        if score < 75:
            return "Scaffold incomplete — finish generated instance files"
        return "Scaffold ready — run a human-reviewed pilot before claiming Punto B"

    if score < 40:
        return "Punto A — install Direction first"
    if score < 60:
        return "Documented but not operational — run Sprint 1"
    if score < 75:
        return "Assisted pilot — run first department loop"
    if score < 90:
        return "Operating AI-First slice — add feedback and finance/customer success"
    return "Operational Point B slice evidenced — keep improving skills, feedback and departments"


def validate(instance: Path, *, mode: str, allow_synthetic: bool) -> tuple[int, list[Criterion]]:
    criteria = SCAFFOLD_CRITERIA if mode == "scaffold" else OPERATIONAL_CRITERIA
    missing: list[Criterion] = []
    score = 0
    for criterion in criteria:
        ok = has_scaffold_evidence(instance, criterion) if mode == "scaffold" else has_operational_evidence(instance, criterion, allow_synthetic=allow_synthetic)
        if ok:
            score += criterion.points
        else:
            missing.append(criterion)
    return score, missing


def operational_next_unblocker(instance: Path, missing: list[Criterion]) -> list[str]:
    """Return operator-facing next steps for self-serve operational readiness."""
    if not missing:
        return []

    first_missing = missing[0]
    guide_path = instance / "FIRST_OPERATING_LOOP.md"
    guide_ref = "FIRST_OPERATING_LOOP.md" if guide_path.exists() else "the First Operating Loop guide in templates/generated-company-instance/FIRST_OPERATING_LOOP.md"
    return [
        "Next unblocker:",
        f"- Open {guide_ref} and create one human-reviewed internal loop before retrying operational readiness.",
        f"- First missing proof point: {first_missing.name} — {first_missing.detail}",
        "- Minimum proof chain: source-of-truth map → context-packets/initial-company-context.md → bounded agent draft/analysis → human review → receipts/first-loop.md → scorecard/next sprint update.",
        f"- After evidence exists, rerun: python scripts/validate_point_b_readiness.py --mode operational {instance}",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate scaffold or operational Point B readiness for a Company Brain instance.")
    parser.add_argument("instance", type=Path, help="Path to generated/private instance")
    parser.add_argument("--mode", choices=("scaffold", "operational"), default="operational", help="Validation mode. Scaffold checks installation shape; operational checks human-reviewed evidence.")
    parser.add_argument("--allow-synthetic", action="store_true", help="Allow synthetic/example evidence in operational mode. Never use for real-company claims.")
    parser.add_argument("--min-score", type=int, default=None, help="Minimum score required to pass. Defaults: scaffold=75, operational=90")
    args = parser.parse_args()

    instance = args.instance.expanduser().resolve()
    if not instance.exists() or not instance.is_dir():
        print(f"❌ Instance not found: {instance}")
        return 2

    min_score = args.min_score if args.min_score is not None else (75 if args.mode == "scaffold" else 90)
    score, missing = validate(instance, mode=args.mode, allow_synthetic=args.allow_synthetic)
    print(f"Point B {args.mode} readiness: {score}/100")
    print(f"Level: {readiness_level(score, mode=args.mode)}")

    if args.mode == "scaffold":
        print("Mode note: scaffold readiness proves generated files exist; it does not prove operational Punto B.")
    elif args.allow_synthetic:
        print("Mode note: synthetic evidence is allowed for examples only; do not use this result for a real-company claim.")
    else:
        print("Mode note: operational readiness requires non-placeholder, human-reviewed evidence. Fresh wizard scaffolds should fail here.")

    if missing:
        print("Missing or insufficient evidence:")
        for criterion in missing:
            print(f"- {criterion.name} ({criterion.points}): {criterion.detail}")
        if args.mode == "operational":
            for line in operational_next_unblocker(instance, missing):
                print(line)
    else:
        print("All minimum evidence for this mode is present.")

    if args.mode == "operational" and missing:
        print("❌ Point B operational validation failed: missing mandatory operational evidence. Do not claim operational Punto B yet.")
        return 1

    if score < min_score:
        print(f"❌ Point B {args.mode} validation failed: below minimum score {min_score}. Do not claim operational Punto B yet.")
        return 1

    print(f"✅ Point B {args.mode} validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate Company Brain scaffold or operational Point B readiness.

Two modes are intentionally separate:
- scaffold: checks that the generated instance has the expected shape.
- operational: checks that an assisted first operating slice has real evidence.

A fresh wizard scaffold must pass scaffold mode and fail operational mode.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Criterion:
    name: str
    points: int
    patterns: tuple[str, ...]
    detail: str


SCAFFOLD_CRITERIA = (
    Criterion("Direction / Mother Brain file exists", 15, ("company/company-brain.md",), "Create company/company-brain.md."),
    Criterion("Approval boundaries file exists", 15, ("company/approval-boundaries.md",), "Create company/approval-boundaries.md."),
    Criterion("Priority department scaffold exists", 15, ("departments/*/department-brain.md",), "Install at least one department brain."),
    Criterion("Digital employee permissions file exists", 15, ("digital-employees/*/PERMISSIONS.md",), "Create at least one digital employee permissions file."),
    Criterion("Context packet scaffold exists", 10, ("context-packets/*.md",), "Create a context packet scaffold."),
    Criterion("Installation receipt exists", 10, ("receipts/*.md",), "Write an installation or pilot receipt."),
    Criterion("Scorecard scaffold exists", 10, ("company/company-scorecard.md", "company/point-b-readiness.md"), "Create scorecard/readiness files."),
    Criterion("Next sprint plan exists", 10, ("company/guided-pilot-plan.md",), "Create company/guided-pilot-plan.md with next sprint."),
)

OPERATIONAL_CRITERIA = (
    Criterion("Direction / Mother Brain installed", 15, ("company/company-brain.md",), "Replace Direction placeholders with reviewed vision, mission, annual goal/rocks/OKRs and operating owner."),
    Criterion("Approval boundaries reviewed", 15, ("company/approval-boundaries.md",), "Define human approval gates for external, economic, legal, production and sensitive actions."),
    Criterion("Priority department operating", 15, ("departments/*/department-brain.md",), "Complete one department brain with responsibilities, workflows, scorecard and escalation path."),
    Criterion("Digital employee permissions active", 15, ("digital-employees/*/PERMISSIONS.md",), "Define one role/position agent with allowed actions, forbidden actions and required approvals."),
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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


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

    if not all(marker in lowered for marker in REQUIRED_OPERATIONAL_MARKERS):
        return False

    return True


def has_operational_evidence(root: Path, criterion: Criterion, *, allow_synthetic: bool) -> bool:
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

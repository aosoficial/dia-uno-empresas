#!/usr/bin/env python3
"""Validate the public three-layer method and preserved V3 inventory."""
from __future__ import annotations

import sys
from pathlib import Path

from method_assets import SOURCE_METHOD, validate_method_assets

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "personas/README.md",
    "personas/metodo-v3/README.md",
    "personas/metodo-v3/INVENTARIO.md",
    "personas/metodo-v3/QA.md",
    "agentes/README.md",
    "sistema-hibrido/README.md",
    "sistema-hibrido/contrato-de-funcion.md",
    "sistema-hibrido/matriz-de-equivalencias.md",
    "implementacion/organizar.md",
    "implementacion/agentizar.md",
    "implementacion/escalar.md",
    "templates/generated-company-instance/METHOD.json",
    "templates/generated-company-instance/personas/README.md",
    "schemas/hybrid_function.schema.yaml",
]


def main() -> int:
    errors = [f"Missing: {relative}" for relative in REQUIRED if not (ROOT / relative).exists()]
    errors.extend(validate_method_assets(SOURCE_METHOD))

    inventory = SOURCE_METHOD / "INVENTARIO.md"
    if inventory.is_file():
        text = inventory.read_text(encoding="utf-8")
        for marker in ["Total: `36/36`", "Versión de todos los artefactos", "Puente al sistema híbrido"]:
            if marker not in text:
                errors.append(f"Inventory missing marker: {marker}")

    matrix = ROOT / "sistema-hibrido" / "matriz-de-equivalencias.md"
    if matrix.is_file():
        text = matrix.read_text(encoding="utf-8").lower()
        for pair in [
            ("ficha de puesto", "contrato"),
            ("matriz de decisiones", "permissions.md"),
            ("sop", "operations.md"),
            ("evaluación", "maturity_review.md"),
        ]:
            if not all(term in text for term in pair):
                errors.append(f"Equivalence matrix missing pair: {pair[0]} -> {pair[1]}")

    if errors:
        print("Method layer validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Method layer validation OK: Personas, Agentes and Sistema Híbrido are linked; 36/36 originals verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

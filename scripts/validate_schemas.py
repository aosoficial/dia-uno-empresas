#!/usr/bin/env python3
"""Validación de esquemas YAML en schemas/.

Comprueba que cada archivo .yaml sea parseable, contenga las claves
top-level requeridas (schema, fields, example) y que cada campo en
fields tenga las propiedades obligatorias (name, type, required, description).

Uso:
    python scripts/validate_schemas.py

Código de salida:
    0 — todos los esquemas son válidos.
    1 — hay al menos un error.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"

# Claves obligatorias a nivel raíz del esquema
REQUIRED_TOP_KEYS = {"schema", "fields", "example"}
# Claves obligatorias dentro de schema:
REQUIRED_SCHEMA_KEYS = {"name", "version", "description"}
# Claves obligatorias por campo dentro de fields:
REQUIRED_FIELD_KEYS = {"name", "type", "required", "description"}


def _load_yaml(path: Path) -> dict | None:
    """Intenta cargar un archivo YAML. Devuelve None si falla."""
    try:
        import yaml  # type: ignore
    except ImportError:
        print("ERROR: PyYAML no está instalado. Instálalo con: pip install pyyaml")
        sys.exit(1)

    try:
        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        return data
    except yaml.YAMLError:
        return None


def validate_file(path: Path) -> tuple[list[str], list[str]]:
    """Valida un archivo de esquema. Devuelve (errores, avisos)."""
    errors: list[str] = []
    warnings: list[str] = []
    rel = path.relative_to(ROOT)

    data = _load_yaml(path)

    # Error de parseo YAML
    if not isinstance(data, dict):
        errors.append(f"{rel}: no es un YAML válido o no es un diccionario ({data})")
        return errors, warnings

    # --- Claves top-level ---
    for key in REQUIRED_TOP_KEYS:
        if key not in data:
            errors.append(f"{rel}: falta clave top-level requerida '{key}'")

    # --- Validar bloque schema: ---
    schema_block = data.get("schema")
    if isinstance(schema_block, dict):
        for key in REQUIRED_SCHEMA_KEYS:
            if key not in schema_block:
                errors.append(f"{rel}: falta 'schema.{key}'")
    elif schema_block is not None:
        errors.append(f"{rel}: 'schema' debe ser un diccionario, no {type(schema_block).__name__}")

    # --- Validar fields ---
    fields = data.get("fields")
    if isinstance(fields, list):
        for i, field in enumerate(fields):
            if not isinstance(field, dict):
                errors.append(f"{rel}: fields[{i}] no es un diccionario")
                continue
            field_name = field.get("name", f"<sin nombre, índice {i}>")
            for key in REQUIRED_FIELD_KEYS:
                if key not in field:
                    errors.append(f"{rel}: campo '{field_name}' sin '{key}'")
            if "example" not in field:
                warnings.append(f"{rel}: campo '{field_name}' sin 'example'")
    elif fields is not None:
        errors.append(f"{rel}: 'fields' debe ser una lista, no {type(fields).__name__}")

    return errors, warnings


def main() -> int:
    """Punto de entrada principal."""
    yaml_files = sorted(SCHEMAS_DIR.glob("*.yaml"))

    if not yaml_files:
        print(f"No se encontraron archivos .yaml en {SCHEMAS_DIR.relative_to(ROOT)}/")
        return 0

    total_errors: list[str] = []
    total_warnings: list[str] = []

    for path in yaml_files:
        errs, warns = validate_file(path)
        total_errors.extend(errs)
        total_warnings.extend(warns)

    # --- Resumen ---
    print(f"Archivos analizados: {len(yaml_files)}")
    for f in yaml_files:
        print(f"  - {f.relative_to(ROOT)}")

    if total_warnings:
        print(f"\nAvisos ({len(total_warnings)}):")
        for w in total_warnings:
            print(f"  AVISO: {w}")

    if total_errors:
        print(f"\nErrores ({len(total_errors)}):")
        for e in total_errors:
            print(f"  ERROR: {e}")
        print("\nResultado: FALLIDO")
        return 1

    print("\nResultado: OK — todos los esquemas son válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

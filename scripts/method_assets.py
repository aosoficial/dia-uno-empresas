#!/usr/bin/env python3
"""Shared helpers for preserved human-method assets.

The source files are immutable framework inputs. Generated company instances
receive byte-for-byte copies plus the inventory and integrity manifest.
"""
from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_METHOD = ROOT / "personas" / "metodo-v3"
PEOPLE_README_TEMPLATE = ROOT / "templates" / "company" / "people-instance-readme.md"
MANIFEST_NAME = "MANIFEST.sha256"
INVENTORY_NAME = "INVENTARIO.md"


def read_manifest(method_root: Path = SOURCE_METHOD) -> dict[str, str]:
    entries: dict[str, str] = {}
    manifest = method_root / MANIFEST_NAME
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, relative = line.split("  ", 1)
        entries[relative] = digest
    return entries


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_method_assets(method_root: Path) -> list[str]:
    errors: list[str] = []
    manifest = method_root / MANIFEST_NAME
    inventory = method_root / INVENTORY_NAME
    if not manifest.is_file():
        return [f"Missing method manifest: {manifest}"]
    if not inventory.is_file():
        errors.append(f"Missing method inventory: {inventory}")

    try:
        entries = read_manifest(method_root)
    except (OSError, ValueError) as exc:
        return [f"Invalid method manifest {manifest}: {exc}"]

    if len(entries) != 36:
        errors.append(f"Method manifest has {len(entries)} assets; expected 36")

    extensions = {".docx": 0, ".xlsx": 0}
    for relative, expected in entries.items():
        path = method_root / relative
        if not path.is_file():
            errors.append(f"Missing method asset: {relative}")
            continue
        extensions[path.suffix] = extensions.get(path.suffix, 0) + 1
        actual = file_sha256(path)
        if actual != expected:
            errors.append(f"Method asset hash mismatch: {relative}")

    if extensions.get(".docx") != 29:
        errors.append(f"Method has {extensions.get('.docx', 0)} DOCX assets; expected 29")
    if extensions.get(".xlsx") != 7:
        errors.append(f"Method has {extensions.get('.xlsx', 0)} XLSX assets; expected 7")
    return errors


def copy_method_assets(instance_root: Path, *, overwrite: bool) -> int:
    """Copy preserved assets, manifest and inventory into a private instance."""
    destination = instance_root / "personas" / "metodo-v3"
    destination.mkdir(parents=True, exist_ok=True)
    sources = [SOURCE_METHOD / MANIFEST_NAME, SOURCE_METHOD / INVENTORY_NAME]
    sources.extend(sorted((SOURCE_METHOD / "originales").rglob("*")))
    count = 0
    for source in sources:
        if source.is_dir():
            continue
        relative = source.relative_to(SOURCE_METHOD)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not overwrite:
            if file_sha256(target) != file_sha256(source):
                raise ValueError(f"Refusing to overwrite modified method asset: {relative}")
            continue
        shutil.copy2(source, target)
        count += 1
    return count


def write_people_instance_readme(instance_root: Path, values: dict[str, str]) -> Path:
    text = PEOPLE_README_TEMPLATE.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace(key, value)
    target = instance_root / "README.md"
    target.write_text(text, encoding="utf-8")
    return target

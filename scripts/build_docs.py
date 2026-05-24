#!/usr/bin/env python3
"""Genera un documento combinado a partir de los .md de docs/.

Lee todos los archivos Markdown de docs/ en orden alfabético, los
concatena con separadores de página (---), añade una tabla de contenidos
basada en los encabezados H1 y escribe el resultado en
build/outputs/master_combined.md.

Uso:
    python scripts/build_docs.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
OUTPUT_DIR = ROOT / "build" / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "master_combined.md"


def _extract_h1(text: str) -> str | None:
    """Extrae el primer encabezado H1 de un texto Markdown."""
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def _slug(title: str) -> str:
    """Convierte un título en un ancla compatible con Markdown."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug).strip("-")
    return slug


def _count_words(text: str) -> int:
    """Cuenta palabras en un texto."""
    return len(text.split())


def main() -> int:
    """Punto de entrada principal."""
    # Excluir revisiones internas de producto del documento maestro.
    # El build público debe contener manuales, quick start y glosario, no auditorías internas.
    md_files = sorted(
        path for path in DOCS_DIR.glob("*.md")
        if "product_review" not in path.name
    )

    if not md_files:
        print(f"No se encontraron archivos .md en {DOCS_DIR.relative_to(ROOT)}/")
        return 1

    # Leer contenidos y extraer títulos
    sections: list[tuple[str, str, str]] = []  # (nombre_archivo, título, contenido)
    for path in md_files:
        content = path.read_text(encoding="utf-8")
        title = _extract_h1(content) or path.stem
        sections.append((path.name, title, content))

    # Construir tabla de contenidos
    toc_lines = ["# DIA UNO Empresas — Documento Combinado", "", "## Tabla de contenidos", ""]
    for _filename, title, _content in sections:
        anchor = _slug(title)
        toc_lines.append(f"- [{title}](#{anchor})")
    toc_lines.append("")

    # Concatenar secciones con separadores
    body_parts: list[str] = []
    for _filename, _title, content in sections:
        body_parts.append(content.rstrip())

    combined = "\n".join(toc_lines) + "\n---\n\n" + "\n\n---\n\n".join(body_parts) + "\n"

    # Crear directorio de salida si no existe
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(combined, encoding="utf-8")

    # Informe
    total_words = _count_words(combined)
    print(f"Archivos incluidos ({len(sections)}):")
    for filename, title, content in sections:
        print(f"  - {filename}  ({_count_words(content)} palabras)  [{title}]")
    print(f"\nPalabras totales: {total_words}")
    print(f"Salida: {OUTPUT_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

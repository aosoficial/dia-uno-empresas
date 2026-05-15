# Company Brain System v0.1.0

Primera release privada de **Company Brain System — Agentic Operating System**.

El objetivo de esta versión es fijar una base usable para revisar el método como producto, probarlo con un piloto privado y mejorar el framework con evidencia real.

## Incluye

- Manual principal en español:
  - `docs/00_master_playbook.md`
  - `docs/01_aos_system.md`
  - `docs/02_operational_memory.md`
  - `docs/03_brain_architecture.md`
  - `docs/04_agent_onboarding.md`
  - `docs/05_operator_manual.md`
- Quick Start:
  - `docs/07_quick_start.md`
- Glosario:
  - `docs/08_glossary.md`
- Revisión de producto interna:
  - `docs/06_product_review_v0_1.md`
- Templates operativos:
  - Agent Runtime Pack
  - Department Brain Pack
  - cuestionarios
  - scorecards
  - receipts
  - StateChanges
  - Context Packets
- Schemas YAML:
  - agent
  - brain
  - department
  - permission
  - heartbeat
  - receipt
  - statechange
  - context_packet
  - handoff
- Registry inicial:
  - agents
  - brains
  - departments
  - metrics
  - permissions
  - sources
- Ejemplo ficticio completo:
  - `examples/vega/`
- Scripts:
  - `scripts/validate_repo.py`
  - `scripts/validate_schemas.py`
  - `scripts/build_docs.py`
  - `scripts/export_docx.py`

## Validación

Antes de release:

```bash
python3 scripts/validate_repo.py
python3 scripts/validate_schemas.py
python3 scripts/build_docs.py
python3 scripts/export_docx.py
```

GitHub Actions también valida estructura, schemas y build docs en cada push.

## Estado

- Visibilidad del repo: privado.
- No es release pública.
- Publicación pública requiere aprobación explícita, anti-secret review y anonimización.

## Siguiente paso recomendado

Crear el piloto privado de Company Brain System aplicado a Jordi / Hermes Clean / AOS / Urus, sin tocar todavía Telegram/gateway ni credenciales reales.

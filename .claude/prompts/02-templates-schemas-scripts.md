# Claude Task 02 — Templates, Schemas and Scripts for DIA UNO Empresas

You are working inside the DIA UNO Empresas repository.

Create high-quality reusable templates, YAML schemas and simple validation scripts.

## Templates

Create complete Markdown templates for:

- `templates/agent-runtime-pack/`
- `templates/department-brain-pack/`
- `templates/questionnaires/`
- `templates/scorecards/`
- `templates/receipts/`
- `templates/statechanges/`
- `templates/context-packets/`

The Agent Runtime Pack must include:

- `README.md`
- `IDENTITY.md`
- `SOUL.md`
- `AGENTS.md`
- `USER.md`
- `TOOLS.md`
- `PERMISSIONS.md`
- `MEMORY_POLICY.md`
- `OPERATIONS.md`
- `CONTEXT_PACKET.md`
- `STATECHANGE.md`
- `RECEIPT.md`
- `ROLE_CARD.md`
- `INSTALL.md`
- `HEARTBEAT.md`
- `HANDOFF.md`
- `MEMORY.md`

## Schemas

Create YAML schemas for:

- `schemas/agent.schema.yaml`
- `schemas/brain.schema.yaml`
- `schemas/department.schema.yaml`
- `schemas/statechange.schema.yaml`
- `schemas/context_packet.schema.yaml`
- `schemas/receipt.schema.yaml`
- `schemas/permission.schema.yaml`
- `schemas/heartbeat.schema.yaml`

Use clear required fields and examples.

## Scripts

Create:

- `scripts/validate_schemas.py`
- `scripts/build_docs.py`
- `scripts/export_docx.py`

Scripts should be safe, local-only, and not require external services.

## Quality rules

- Spanish content.
- No secrets.
- No private implementation details.
- Everything must be usable by someone applying DIA UNO Empresas.

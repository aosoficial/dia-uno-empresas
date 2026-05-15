# RECEIPTS — Company Brain System

## 2026-05-09 17:58:18 CEST — Mejoras post-Urus aplicadas

**Action:** applied the obvious/safe Company Brain System method improvements discovered during the Urus pilot.

**Owner:** Jordi Beltran Breva.

**Runtime coordinator:** Hermes Clean.

**Source:** AOS Holding review `docs/method_review_after_urus.md`, feedback `FB-005` to `FB-010`.

**Evidence:**

- Added `templates/agent-runtime-pack/CUTOVER.md`.
- Updated `templates/agent-runtime-pack/README.md` with cutover, identity verification, inherited-tool audit, initial Context Packet and owner acceptance checks.
- Updated `templates/agent-runtime-pack/INSTALL.md` with active identity verification, inherited-tool audit, initial Context Packet and first real operation acceptance.
- Updated `docs/04_agent_onboarding.md` with cutover workflow and active identity verification.
- Updated `templates/questionnaires/agent-onboarding-questionnaire.md` with existing channel/gateway and identity verification questions.
- Updated `templates/scorecards/agent-evaluation-scorecard.md` with activation/owner acceptance metric.
- Updated `CHANGELOG.md`, `docs/06_product_review_v0_1.md` and `examples/vega/README.md` to reflect the 18-file Agent Runtime Pack.
- Local validation passed:
  - `python3 scripts/validate_repo.py`
  - `python3 scripts/validate_schemas.py`
  - `python3 scripts/build_docs.py`

**Not included:** personal/coaching agent guide; still pending careful wording and Jordi approval.

**Current freshness:** fresh as of 2026-05-09 17:58:18 CEST.

## 2026-05-09 13:43:15 CEST — Consolidation/RAG research incorporated

**Action:** updated Company Brain System documentation to include practical memory-consolidation rules informed by the public paper `The Geometry of Consolidation`.

**Owner:** Jordi Beltran Breva.

**Runtime coordinator:** Hermes Clean.

**Assistant used:** Claude Code was attempted, but unavailable because it was not logged in. Hermes Clean applied the update directly and verified it locally.

**Source:** https://github.com/niashwin/geometry-of-consolidation/blob/main/paper/arxiv/main.pdf

**Evidence:**

- Updated `docs/00_master_playbook.md` with RAG/consolidation framing and implementation roles: storage, embeddings and operational memory layer.
- Updated `docs/02_operational_memory.md` with consolidation rules: when to summarize, when to preserve originals, and why high-responsibility records must stay traceable.
- Updated `docs/03_brain_architecture.md` with separation between storage, embeddings and memory layer, plus the rule that retrieval is not consolidation.
- Updated `docs/08_glossary.md` with `Consolidación de memoria` and `Recuperación / RAG`.
- Local validation passed:
  - `python3 scripts/validate_repo.py`
  - `python3 scripts/validate_schemas.py`
  - `python3 scripts/build_docs.py`
- Anti-secret scan returned 0 matches for common key/token/connection-string patterns.

**Current freshness:** fresh as of 2026-05-09 13:43:15 CEST.

## 2026-05-09 00:19:13 CEST — v0.1.0 private release

**Action:** created the private GitHub release `v0.1.0` for Company Brain System.

**Owner:** Jordi Beltran Breva.

**Runtime coordinator:** Hermes Clean.

**Repository:** `aosoficial/company-brain-system`

**URL:** https://github.com/aosoficial/company-brain-system

**Release URL:** https://github.com/aosoficial/company-brain-system/releases/tag/v0.1.0

**Visibility:** private.

**Evidence:**

- `CHANGELOG.md` updated from pending to `v0.1.0 — 2026-05-09`.
- `RELEASE_NOTES_v0.1.0.md` created.
- Local validation passed before release:
  - `python3 scripts/validate_repo.py`
  - `python3 scripts/validate_schemas.py`
  - `python3 scripts/build_docs.py`
  - `python3 scripts/export_docx.py`
- GitHub Actions workflow `validate` completed successfully for run `25582284100`.
- Git tag created and pushed: `v0.1.0`.
- GitHub release verified: non-draft, non-prerelease, repo remains `PRIVATE`.

**Commit released:** `3e86015` — `Finalize v0.1.0 release notes`.

**Current freshness:** fresh as of 2026-05-09 00:19:13 CEST.

## 2026-05-09 00:12:45 CEST — v0.1 product review pass

**Action:** reviewed Company Brain System as a product and resolved the main v0.1 onboarding blockers.

**Owner:** Jordi Beltran Breva.

**Runtime coordinator:** Hermes Clean.

**Assistant used:** Claude Code CLI for product review and documentation drafting; Hermes verified, patched, validated and pushed.

**Repository:** `aosoficial/company-brain-system`

**URL:** https://github.com/aosoficial/company-brain-system

**Visibility:** private.

**Evidence:**

- Product review created: `docs/06_product_review_v0_1.md`.
- Quick Start created: `docs/07_quick_start.md`.
- Glossary created: `docs/08_glossary.md`.
- Example created: `examples/vega/`.
- Handoff schema created: `schemas/handoff.schema.yaml`.
- Master build excludes internal product review from public combined docs.
- Local validation passed: `python3 scripts/validate_repo.py`.
- Schema validation passed: `python3 scripts/validate_schemas.py`.
- Docs build passed: `python3 scripts/build_docs.py`.
- DOCX export passed locally: `python3 scripts/export_docx.py`.
- GitHub Actions workflow `validate` completed successfully for run `25582066923`.

**Commit:** `0fbf951` — `Prepare Company Brain System v0.1 product review`.

**Current freshness:** fresh as of 2026-05-09 00:12:45 CEST.

## 2026-05-08 23:38:12 CEST — Initial private GitHub upload

**Action:** completed the initial Company Brain System framework and pushed it to GitHub.

**Owner:** Jordi Beltran Breva.

**Runtime coordinator:** Hermes Clean.

**Assistant used:** Claude Code CLI for drafting and review support.

**Repository:** `aosoficial/company-brain-system`

**URL:** https://github.com/aosoficial/company-brain-system

**Visibility:** private.

**Evidence:**

- Local validation passed: `python3 scripts/validate_repo.py`.
- Schema validation passed: `python3 scripts/validate_schemas.py`.
- Docs build passed: `python3 scripts/build_docs.py`.
- DOCX export passed locally: `python3 scripts/export_docx.py`.
- GitHub repository created: `aosoficial/company-brain-system`.
- GitHub Actions workflow `validate` completed successfully for run `25580795554`.

**Commit:** `4ee4f9d` — `Initial Company Brain System framework`.

**Included:**

- Core Spanish manuals.
- Agent Runtime Pack templates.
- Department Brain Pack templates.
- Questionnaires.
- Scorecards.
- Receipt, StateChange and Context Packet templates.
- YAML schemas.
- Registry YAML files.
- Local validation/build/export scripts.
- GitHub Actions validation workflow.
- MIT License.
- Security and contribution docs.

**Not included by design:**

- Real credentials.
- Build outputs except `.gitkeep`.
- Private pilot files.
- Local planning/source-map files ignored by `.gitignore`.

**Current freshness:** fresh as of 2026-05-08 23:38:12 CEST.

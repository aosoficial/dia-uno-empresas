# Receipts log

This file is a public-safe example receipt log for repository-level work.

## R-001 — Initial framework assembled

**Action:** assembled the first DIA UNO Empresas framework.

**Output:** docs, templates, schemas, registry, examples and scripts.

**Verification:** repository validation and schema validation should pass before release.

## R-002 — Public-safety pass

**Action:** removed private implementation details, personal names, private workspace paths and internal credits from public-facing material.

**Output:** public-safe repo content.

**Verification:** keyword scan for sensitive terms before making the repository public.

## R-003 — Commercial breadcrumbs added

**Action:** added DIA UNO help breadcrumbs across the documentation.

**Output:** each main doc points blocked implementers toward the help process.

**Verification:** docs link to `docs/12_get_help_from_dia_uno.md`.

## R-004 — ORGO/Hermes installer readiness pass

**Action:** added ORGO/Hermes onboarding, private company bootstrap, first digital employee guide, model/trace strategy and installability validators.

**Output:** public framework now distinguishes repo content from private company instances and can generate/verify a demo private instance.

**Verification:** repo, schema, docs build, link, public-safety, installable-runtime, bootstrap dry-run, bootstrap write and installation verifier checks pass locally.

## R-005 — Phase B guided accelerator assets

Date: 2026-05-21
Owner: Hermes Clean
Scope: local repo change, not pushed.

What changed:
- Added Dirección / Mother Brain, department rollout, vertical, source adapter, human-agent OS and feedback loop docs.
- Added department and company-type templates.
- Added guided `company_brain_wizard.py`.
- Updated validators/verifier for accelerator assets.

Evidence:
- Local validation required before publication.
- No real operator/company/client data intended in public docs.

## R-006 — Guided Pilot and Self-Serve reliability pass

Date: 2026-05-22
Owner: Hermes Clean
Scope: local repo change, not pushed.

What changed:
- Added guided pilot 30/60/120 path, delivery model and Point B definition.
- Added self-serve happy path, operator UX, `make` shortcuts and troubleshooting.
- Added pilot templates and Point B readiness scorecard.
- Added `scripts/validate_point_b_readiness.py` and wizard-generated `guided-pilot-plan.md` / `point-b-readiness.md`.

Evidence:
- Run repository validators, tests, smoke installs and Point B validator before publication.
- Do not claim guaranteed transformation; claim verified Punto B slice when evidence passes.

## R-007 — START_HERE and scaffold-first operator path

Date: 2026-05-22
Owner: Hermes Clean
Scope: autonomous cron change on `auto/point-b-readiness-loop`; no main merge, no PR, no deploy.

What changed:
- Added root `START_HERE.md` as the first nontechnical entrypoint.
- Linked `START_HERE.md` from the first section of `README.md`.
- Updated self-serve docs so the first Point-B validation is scaffold mode, not operational mode.
- Explicitly documented that a fresh scaffold should not pass operational Punto B until a human-reviewed loop produces evidence.

Why:
- A nontechnical operator needs one safe first path: install private scaffold, validate scaffold structure, then create real operational evidence before claiming Punto B.
- This reduces false positives and prevents confusing an expected operational failure with a broken install.

Source/provenance:
- 2026-05-22 autonomous Point-B improvement backlog items `CBS-PB-UX-001` and `CBS-PB-UX-002`.
- Spec and quality review subagents approved the documentation slice.

Allowed actions:
- Local documentation/template/script edits inside this repository.
- Local validation with synthetic/private temporary instances.

Forbidden actions:
- No push to `main`, merge, PR, deploy or publication from this run.
- No real client/company data or secrets in public examples.

Validation:
- `make validate` passed, including repo, schema, links, public safety, installable runtime, department quality and pytest checks.
- Wizard smoke created a synthetic private instance, installation verification passed, scaffold readiness passed.
- Operational readiness on the fresh scaffold failed as expected with “Do not claim operational Punto B yet.”

Next gap:
- Continue translating/self-serve hardening: Spanish summaries for remaining operator docs, standardized `python3` commands, and simpler troubleshooting for nontechnical users.

## R-008 — Slack-first first agent path

Date: 2026-05-24
Owner: Hermes Clean
Scope: local repo change, not pushed.

What changed:
- Added `docs/45_slack_first_agent.md` as the default short-term path for talking to the first agent through Slack.
- Updated `README.md`, `START_HERE.md`, `docs/20_first_digital_employee_48h.md` and `docs/27_human_agent_operating_system.md` to make Slack the recommended first human-agent interface for multi-human pilots.
- Added private instance template `templates/generated-company-instance/integrations/slack-first-agent.md` and mapped it in `MAP.md` / generated `README.md`.

Why:
- Slack is the fastest reliable surface for client teams, approvals and notifications.
- The Company Brain remains the source of truth; Slack is only the interface.

Allowed actions:
- Document Slack-first setup and non-secret configuration.
- Keep secrets/tokens outside Git and outside chat.

Forbidden actions:
- Do not create Slack apps, connect live workspaces, store tokens, activate external bots or configure production without explicit human approval.

**Verification:**
- Full repository validation passed before publication.

## R-009 — ORGO-first CEO and Observer onboarding

Date: 2026-05-24
Owner: Hermes Clean
Scope: repository change for private pilot readiness; no live Slack/Supabase/Voyage/GBrain integration activated.

What changed:
- Added `docs/46_orgo_first_company_onboarding.md` as the canonical ORGO-first company onboarding flow.
- Clarified that the client starts in ORGO, then connects Codex or Claude Code as guided technical installer.
- Updated docs/templates/scripts/tests so the first agent is `CEO Agent`, limited to Dirección.
- Added `Observer Agent` template as a read-only coherence and evidence guard.
- Replaced remaining generated/example paths from `digital-employees/ceo-operations-assistant/` to `digital-employees/ceo/`.

Why:
- The first company pilot needs a practical entry sequence: ORGO → Codex/Claude → DIA UNO → Slack → private memory → CEO Agent → department agents → Observer.
- Slack remains the interface; GBrain/Company Brain remains the operational memory and source of truth.

Allowed actions:
- Documentation, templates, local generators, validators and tests.
- Synthetic example updates only.

Forbidden actions:
- No live Slack app, production runtime, real client data, Supabase/Voyage/GBrain provisioning, secrets, money/legal/public actions or workers without explicit approval.

Verification:
- `python3 scripts/validate_repo.py` passed.
- `python3 scripts/validate_schemas.py` passed.
- `python3 scripts/build_docs.py` passed.
- `python3 scripts/validate_links.py` passed.
- `python3 scripts/validate_public_safety.py` passed.
- `python3 scripts/validate_installable_runtime.py` passed.
- `pytest -q` passed: 50 tests.

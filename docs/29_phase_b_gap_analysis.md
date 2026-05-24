# Phase B Gap Analysis

This audit reviews the current DIA UNO Empresas accelerator after the Dirección-first, department-rollout, source-adapter and wizard work.

## Current readiness

The repo now has the right public-frame direction:

- Point A to Point B AI-First positioning.
- Dirección / Mother Brain first.
- Department rollout roadmap.
- Generated private instance pattern.
- Source adapters for agency, marketing, CEO/People OS, web development and product/software.
- Wizard, bootstrap, verifier and validators.

It is useful as an installable v0 accelerator, but the next layer should make it deeper, more guided and more executable.

## P0 — Gaps that block a strong public/productized promise

### 1. Department templates are structurally complete but too shallow

Current department packs include the same four files per department, but most are short and generic.

Risk: the system may look broad but not expert enough for each function.

Improve by adding for each department:

- core operating questions;
- required memory fields;
- role map: humans, digital employees and approvals;
- day-1 task;
- weekly cadence;
- scorecard metrics;
- receipts expected;
- common failure modes;
- source adapters and license notes.

Priority departments:

1. Dirección / Mother Brain.
2. Operations / Delivery.
3. Sales.
4. Customer Success.
5. Product / Software.
6. Marketing.
7. Finance.

### 2. Generated instance does not yet generate a full department brain for every selected department

The wizard copies department templates into the generated instance, but the base generated instance still contains only fixed Dirección and a minimal operations skeleton.

Risk: users may expect a complete company instance and find mixed old/new structure.

Improve by making the generated instance map, README, scorecard, accountability map and cadence dynamically reflect selected departments.

### 3. Wizard is functional but not truly guided yet

The wizard currently takes CLI flags. It does not ask interactive questions or produce a tailored operating diagnosis.

Risk: non-technical operators still need an expert to know what to answer.

Improve by adding:

- interactive mode;
- 12-question intake;
- company type-specific defaults;
- department recommendation logic;
- first 48h action plan;
- approval-boundary generator;
- first digital employee recommendation;
- post-generation next command hints.

## P1 — Gaps that reduce operating usefulness

### 4. Source coverage is uneven

Good current sources:

- Agency roles: `msitarzewski/agency-agents`.
- Marketing: `coreyhaines31/marketingskills`.
- Direction/People OS: `bradfeld/ceos`.
- Product/software/web: `alan2207/bulletproof-react`, `ixartz/Next-js-Boilerplate`, `drublic/checklist`, `deanpeters/Product-Manager-Skills`, `RefoundAI/lenny-skills`, `ProductHired/open-product-management`, `andreaskelm/pm-brain`.

Weaker lanes still needing source scouting:

- Sales.
- Customer Success.
- Finance.
- SOP / operations documentation.
- Service delivery / agency operations.

Improve by creating a source-scouting doc per lane and only adapting repos with clear licenses or reference-only notes.

### 5. No real skill files yet for department skills

Department `skills.md` files list skill names, but those skills are not yet expanded into executable skill templates.

Risk: the repo names capabilities but cannot train or onboard an agent deeply.

Improve by adding `templates/skills/` with one file per core skill, starting with:

- `product-discovery-brief`;
- `prd-drafting`;
- `web-launch-qa`;
- `proposal-drafting`;
- `lead-qualification`;
- `client-onboarding`;
- `delivery-qa`;
- `weekly-review`;
- `cashflow-review`;
- `sop-writing`.

### 6. Feedback loop is documented but not operationalized in scripts

There is a feedback loop doc, but no script validates whether feedback became a template/skill/method update.

Improve with:

- `scripts/collect_feedback.py` or a template workflow;
- feedback-to-change-contract template;
- validator that every accepted feedback item links to a statechange/receipt.

### 7. Memory backend strategy is still high-level

The public repo explains memory primitives but does not yet give concrete install profiles:

- local Markdown only;
- GBrain / MCP;
- Supabase/Postgres;
- other customer systems.

Improve with a `docs/30_memory_backend_profiles.md` and generated instance `memory/` config templates.

## P2 — Gaps that affect quality, UX and validation

### 8. Validators check existence more than depth

Current validators confirm files exist and basic safety passes. They do not verify content quality per department.

Improve validators to check:

- every department has metrics, approval boundaries, weekly cadence, receipts and first task;
- every skill name has a matching template;
- generated instance has no unresolved `TBD` except in explicitly allowed private-fill sections;
- company-type profile is actually referenced by generated output.

### 9. Public examples are minimal

The repo avoids real data correctly, but synthetic examples could be stronger.

Improve by adding one complete synthetic example:

- `examples/acme-agency-ai-first/` generated via wizard;
- fake company context;
- fake Direction receipt;
- fake first digital employee run;
- verifier output.

Keep it clearly synthetic.

### 10. Digital employees beyond CEO Agent and Observer Agent are not packaged

There is one initial digital employee pack. Departments need starter packs.

Improve by adding:

- Direction Assistant.
- Delivery Manager.
- Marketing Assistant.
- Sales Assistant.
- Customer Success Assistant.
- Product/Software Assistant.
- Finance Assistant.
- People/Ops Assistant.

Each needs permissions, tools, memory policy, allowed actions, forbidden actions and receipts.

## P3 — Strategic improvements

### 11. Offer / accelerator packaging is still implicit

The repo says accelerator, but it does not yet show a clean commercial journey.

Improve with:

- installer journey;
- guided workshop flow;
- done-for-you vs self-serve paths;
- expected outcomes at 48h / 7d / 30d;
- evaluation scorecard for before/after transformation.

### 12. Human-agent operating rhythm needs stronger boards/workflow examples

The repo explains humans and agents, but not enough visual operating flow.

Improve with:

- weekly operating meeting template;
- work item lifecycle;
- handoff examples;
- escalation rules;
- approval board conventions;
- anti-stall rule.

## Recommended next work order

### Sprint 1 — Make the accelerator feel real

1. Deepen Dirección and Operations/Delivery templates.
2. Make wizard interactive.
3. Generate dynamic department maps and scorecards.
4. Add stronger verifier checks for selected departments.

### Sprint 2 — Make departments executable

1. Add executable skill templates.
2. Add department digital employee packs.
3. Add synthetic Acme agency example.
4. Add source adapters for Sales, CS, Finance and SOPs.

### Sprint 3 — Make memory/runtime concrete

1. Add memory backend profiles.
2. Add feedback-to-change-contract workflow.
3. Add first-run receipts and statechange examples.
4. Add stronger install/verification docs for Hermes/GBrain/MCP profiles.

## Current recommendation

Do not push this as "complete" yet.

Best next step: implement Sprint 1 locally, then validate with a full synthetic agency instance and review the generated output as if it were a customer onboarding package.

# First Operating Loop

Company: `{{ company_name }}`
Owner: `{{ owner }}`
Status: `scaffold until one human-reviewed loop is completed`

This page is the self-serve bridge from “files generated” to “work actually passed through the Company Brain”. Do not claim operational Punto B from this page alone. Use it to create the first real evidence packet.

## 30–60 minute first operating loop

Target outcome: one small internal task is briefed with a Context Packet, drafted/analyzed by a bounded digital employee, reviewed by a human, recorded as a Receipt, and reflected in the Scorecard.

Use one of these safe tasks:

- Summarize one internal handoff.
- Review one SOP/checklist for risks.
- Turn one repeated delivery step into a draft workflow.
- Prepare one internal metric update from an approved source.
- Draft a next-sprint recommendation from existing notes.

## Pick exactly one safe internal task

Fill this before asking any agent:

- Task name: `(one sentence)`
- Department: `{{ first_department }}`
- Human owner/reviewer: `{{ owner }}`
- Source row used from `company/source-of-truth-map.md`: `(tool/system + owner + freshness)`
- Allowed agent action: `draft / analyze / summarize only`
- Forbidden actions: `external, public, economic, legal, production, sensitive, credentials`
- Expected output: `(specific internal artifact)`
- Evidence path to create: `receipts/first-loop.md`

## Before you ask an agent

1. Open `company/company-brain.md` and confirm Direction owner, current goal and first objective.
2. Open `company/source-of-truth-map.md` and complete the source row you will use: owner, freshness, read permission, write/action permission, receipt rule, risks and next action.
3. Open `company/approval-boundaries.md` and confirm the task is internal/reversible or mark the approval required.
4. Open `digital-employees/*/PERMISSIONS.md` and confirm the chosen agent can only draft/analyze/summarize.
5. Complete `context-packets/initial-company-context.md` with scope, sources, assumptions, risks, allowed actions, forbidden actions and expected outcome.

If any of those are unclear, stop and complete them first.

## Agent prompt skeleton

Paste this only after the context packet is complete:

```text
You are operating inside a private Company Brain instance for {{ company_name }}.
Use only the context packet and approved source summaries provided below.
Allowed action: draft/analyze/summarize only.
Forbidden actions: external/public/economic/legal/production/sensitive actions; no credentials; no customer contact.
Task: <paste one safe internal task>.
Return:
1. draft/analysis;
2. risks or assumptions;
3. what a human must review;
4. proposed receipt bullets;
5. next safe action.
```

## After the agent output

The human reviewer must:

1. Accept, edit or reject the output.
2. Create `receipts/first-loop.md` with:
   - Action performed;
   - Source / provenance;
   - Context packet used: `context-packets/initial-company-context.md`;
   - Owner;
   - Freshness;
   - Approval / human review;
   - Evidence;
   - Observed outcome;
   - Next action.
3. If the operating state changed, create a file under `statechanges/`.
4. Update `company/company-scorecard.md` with only observed evidence or `unknown`.
5. Update `company/guided-pilot-plan.md` and `company/point-b-readiness.md` with the next sprint.

## Operational validation command

From the framework repo, run:

```bash
python3 scripts/validate_point_b_readiness.py --mode operational /ruta/a/esta-instancia
```

Expected result before evidence: fail with missing operational evidence.
Expected result after a real reviewed loop: pass only if all mandatory evidence exists.

## If validation fails

Do not treat failure as a broken install. It means one of the operating proof points is still missing. Fix the first missing item, then rerun the command. If blocked, share only anonymized context via DIA UNO (`diauno.io`): command run, error text, and which evidence files exist.

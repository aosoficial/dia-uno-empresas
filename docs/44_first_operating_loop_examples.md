# First Operating Loop — evidence examples

This guide gives safe, concrete examples for the first human-reviewed operating loop. Use it after the scaffold passes and before claiming operational readiness.

The goal is not to prove full Punto B. The goal is to create one verified AI-first operating slice: one bounded internal task, one Context Packet, one human-reviewed output, one Receipt, one scorecard update and one next sprint.

Use this alongside [`../templates/how-to/run-first-internal-loop.md`](../templates/how-to/run-first-internal-loop.md) and the generated instance file `FIRST_OPERATING_LOOP.md`.

## Universal evidence chain

Every example below must produce this chain:

1. **Source row selected** in `company/source-of-truth-map.md` with owner, freshness, read permission, write/action permission, receipt rule, risks and next action.
2. **Context Packet** in `context-packets/` naming the exact source row used, allowed action, forbidden actions, expected output and review owner.
3. **Agent/human output** saved inside the private instance. Keep it internal and reversible.
4. **Operational Receipt** in `receipts/` with action performed, source/provenance, context packet used, owner, freshness, approval/human review, evidence, observed outcome and next action.
5. **Scorecard update** in `company/company-scorecard.md` or `company/point-b-readiness.md` with observed evidence, not intention.
6. **Next sprint** in `company/guided-pilot-plan.md` based on what the loop showed.

If one link is missing, `validate_point_b_readiness.py --mode operational` should fail. That failure is useful: it tells you what evidence to create next.

## Example A — agency delivery checklist

Safe internal task:

- Review one existing delivery SOP or handoff summary.
- Produce a checklist draft for the next similar project.
- Do not contact the client, publish anything or edit production systems.

Minimum Context Packet fields:

```yaml
id: cp-operations-delivery-checklist-2026-05-22
target: operations-delivery assistant
task: "Draft an internal delivery checklist from one approved handoff summary."
source: "company/source-of-truth-map.md row: Drive / Docs delivery SOPs"
freshness: "Source row reviewed by Operations Lead on 2026-05-22"
allowed_action: "draft internal checklist only"
forbidden_actions:
  - "no customer contact"
  - "no publishing"
  - "no production changes"
  - "no credentials or private customer data"
expected_output: "outputs/delivery-checklist-draft.md"
review_owner: "Operations Lead"
```

Receipt evidence should say:

- what checklist was drafted;
- which source row and context packet were used;
- who reviewed it;
- what changed after review;
- whether it is approved for internal use or still a draft;
- what next sprint follows.

Scorecard update example:

- `Delivery SOP clarity: unknown → first draft reviewed on 2026-05-22; evidence receipts/first-loop.md`.

## Example B — consultancy proposal risks

Safe internal task:

- Analyze one anonymized proposal outline or synthetic proposal brief.
- Produce risk questions and missing information for human review.
- Do not send the proposal and do not use real client secrets unless approved.

Minimum Context Packet fields:

```yaml
id: cp-sales-proposal-risk-review-2026-05-22
target: sales assistant
task: "Analyze an anonymized proposal outline and list operational risks before human review."
source: "company/source-of-truth-map.md row: Drive / Docs proposal templates"
freshness: "Template reviewed by Founder on 2026-05-22"
allowed_action: "analyze and draft questions only"
forbidden_actions:
  - "no sending"
  - "no pricing commitment"
  - "no legal claims"
  - "no real client secrets"
expected_output: "outputs/proposal-risk-questions.md"
review_owner: "Founder"
```

Receipt evidence should say:

- what proposal outline was analyzed;
- that it was anonymized or synthetic;
- which risks were accepted, edited or rejected;
- which human approval is required before external use.

Scorecard update example:

- `Sales review safety: unknown → proposal risk review completed with human owner; evidence receipts/first-loop.md`.

## Example C — freelancer offer cleanup

Safe internal task:

- Organize current services into a simple internal offer table.
- Use only the freelancer’s own public/services notes or a synthetic brief.
- Do not publish the offer, change prices publicly or contact prospects.

Minimum Context Packet fields:

```yaml
id: cp-direction-offer-cleanup-2026-05-22
target: ceo operations assistant
task: "Turn current service notes into an internal offer table for review."
source: "company/source-of-truth-map.md row: Drive / Docs service notes"
freshness: "Notes reviewed by Owner on 2026-05-22"
allowed_action: "summarize and structure internal offer table only"
forbidden_actions:
  - "no publishing"
  - "no outreach"
  - "no pricing commitment without owner approval"
expected_output: "outputs/internal-offer-table.md"
review_owner: "Owner"
```

Receipt evidence should say:

- which service notes were used;
- what categories were created;
- what the owner changed after review;
- what remains unknown;
- what next sprint validates demand or delivery.

Scorecard update example:

- `Offer clarity: unknown → first internal offer table reviewed; evidence receipts/first-loop.md`.

## Anti-examples that must not count

These do not prove operational readiness:

- Wizard generated files only.
- A receipt that says only “completed” with no source, owner, freshness, approval or evidence.
- A context packet full of placeholders.
- A scorecard updated with intention instead of observed result.
- A draft sent externally without explicit approval.
- Synthetic evidence used as if it were a real company loop.
- Any example containing credentials, API keys, passwords, customer secrets or private contracts.

## What to do when validation fails

1. Read the first `Next unblocker` printed by the validator.
2. Open `FIRST_OPERATING_LOOP.md` in the private instance.
3. Create only the missing evidence item.
4. Rerun:

```bash
python3 scripts/validate_point_b_readiness.py --mode operational /path/to/private-instance
```

If you need help, share only anonymized context through DIA UNO (`diauno.io`): command run, error text, which evidence files exist and which step is blocked. Do not share the private instance or secrets.

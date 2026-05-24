# Model strategy

DIA UNO Empresas is provider-neutral. Pick models by privacy, quality, latency, cost and risk.

## Default tiers

### Tier A — reliable hosted model

Use for production-light company workflows where quality and reliability matter. Avoid sending customer or sensitive data unless the provider and contract are approved.

### Tier B — cheap utility model

Use for low-risk classification, routing, short summarization and formatting.

### Tier C — strong reasoning model

Use for strategy, complex writing, planning, incident review, policy decisions and high-stakes reasoning. Require receipts for model changes that affect privacy, quality or cost.

### Tier D — local/workstation/server model

Use when privacy, offline operation or experimentation matters. Validate quality before relying on it for business decisions.

### Tier E — GPU cloud or inference provider

Use for heavier workloads only after approval for cost, privacy and operational need.

## Environment roles

- PC/workstation: development, prototypes and local tests.
- ORGO/server: isolated company runtime.
- Cloud GPU/provider: heavier inference when approved.
- Hermes profile: operational boundary for a company or employee.

## Data rules

- Do not send real customer/client data to unapproved providers.
- Keep secrets out of prompts, traces and receipts.
- Log provider/model changes as receipts when they affect cost, quality or privacy.
- Prefer small models for routine utility work and stronger models for ambiguous or high-risk work.

## Evaluation before expansion

Before adding a new model/provider:

1. Define the task it improves.
2. Run a small synthetic test.
3. Compare quality, cost, latency and privacy.
4. Record a receipt.
5. Update employee permissions if needed.

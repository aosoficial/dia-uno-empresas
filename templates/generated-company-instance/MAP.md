# Company Brain Map

Company: `{{ company_name }}`
Owner: `{{ owner }}`
Sector: `{{ sector }}`
Language: `{{ language }}`
Risk tier: `{{ risk_tier }}`
Method mode: `{{ method_mode }}`

## Load order

1. `AGENTS.md`
2. `METHOD.json`
3. `personas/README.md` and `personas/metodo-v3/INVENTARIO.md`
4. `company/people-organization-plan.md` and `company/people-readiness.md`
5. `company/approval-boundaries.md`
6. `company/company-brain.md` and `company/source-of-truth-map.md`
7. In hybrid mode only: agent contract, relevant department brain and latest context packet/receipt/statechange/handoff.

## Core locations

- Private onboarding guide: `README.md`
- Method mode and status: `METHOD.json`
- People method: `personas/`
- People organization plan: `company/people-organization-plan.md`
- People readiness: `company/people-readiness.md`
- Company brain / Direction: `company/company-brain.md`
- Source-of-truth / existing systems map: `company/source-of-truth-map.md`
- Approval boundaries: `company/approval-boundaries.md`
- Company scorecard: `company/company-scorecard.md`
- Guided pilot / next sprint: `company/guided-pilot-plan.md`
- Point B diagnosis: `company/point-b-readiness.md`
- Department brains: `departments/<department>/department-brain.md`
- First employee: `digital-employees/ceo/`
- Observer employee: `digital-employees/observer/` when enabled
- Slack-first agent surface: `integrations/slack-first-agent.md`
- Initial context packet: `context-packets/initial-company-context.md`
- Operational receipts: `receipts/`
- State changes: `statechanges/`
- 48h/7d/30d roadmap: `roadmap/48h-7d-30d.md`

## Folder hierarchy boundary

This generated folder is the operating boundary for the private Company Brain.

Use this hierarchy:

```text
./
  company/              # Direction / Mother Brain, approvals, scorecards
  personas/             # human method, inventory and preserved originals
  departments/          # hybrid mode: one folder per department brain
  digital-employees/    # hybrid mode: operating files per AI employee
  context-packets/      # approved context for work
  receipts/             # evidence of completed work
  statechanges/         # durable operational changes
  handoffs/             # human/agent handoffs
  integrations/         # non-secret integration setup notes, e.g. Slack
  decisions/            # explicit decisions and rationale
  scorecards/           # before/after and readiness scores
  secrets/              # README only; real secrets stay out of Git
```

Rules:

- Do not create random folders outside this private instance.
- Do not move operational artifacts to Desktop/Downloads unless the human explicitly approves.
- Do not store secrets, passwords, API keys or tokens in chat or Git.
- Do not store Slack bot tokens, signing secrets, webhooks or model/provider credentials in this folder.
- Any capability agent stays inside its approved function. Other areas are organized first and considered separately; generation never grants an agent broader scope.
- Observer observes and proposes memory maintenance; it does not execute business actions directly.
- If a new folder is needed, explain why it belongs in this hierarchy first.

## Rule

If context is missing, ask for it or create a context packet. Do not invent operational state. A fresh scaffold can pass scaffold validation, but operational Punto B requires a human-reviewed internal loop with receipt, scorecard evidence and next sprint.

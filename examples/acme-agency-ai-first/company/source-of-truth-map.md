# Source-of-Truth Map

Owner: Founder
Source: synthetic systems inventory 2026-05-20
Freshness: updated 2026-05-22
Approval: human owner reviewed system access boundaries
Evidence: receipts/day-1-first-digital-employee-run.md

This synthetic ACME example maps the first operating sources before creating `context-packets/day-0-company-context.md`. It is example evidence only; real companies must complete this with private owners, freshness and approval gates.

| Tool/system | Owner | Data contained | Source-of-truth status | Agent read permission | Agent write/action permission | Sync cadence | Freshness / last reviewed | Receipt rule | Risks | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Drive / Docs | Founder | Strategy docs, SOP drafts, delivery notes | partial | allowed after human review | approval required | weekly | reviewed 2026-05-22 | receipt when used for first-loop context | stale SOPs or mixed client notes | separate current SOPs from archived drafts |
| Notion / wiki | Founder | synthetic operating decisions and process notes | partial | allowed read-only | approval required before edits | weekly | reviewed 2026-05-22 | receipt for any decision/process change | archived pages may look current | mark active pages before agent use |
| Sheets / spreadsheets | Operations lead | synthetic scorecard and KPI tracker | yes | allowed read-only | approval required before formula/status edits | weekly | reviewed 2026-05-22 | receipt for any scorecard update | formula or owner mismatch | lock KPI source sheet during pilot |
| CRM | Sales lead | synthetic pipeline and handoff stage | yes | allowed read-only | approval required before edits/messages | daily | reviewed 2026-05-22 | receipt for any handoff decision | pipeline fields may be incomplete | confirm handoff owner before agent use |
| WhatsApp / Slack | Operations lead | approved internal handoff summaries | partial | approved extracts only | no sending without approval | per loop | reviewed 2026-05-22 | receipt cites approved extract, not raw chat | private client/team communication | use anonymized summaries only |
| Email | Founder | selected internal handoff thread summary | partial | approved extracts only | no sending without approval | per loop | reviewed 2026-05-22 | receipt cites approved extract, not raw inbox | sensitive external communication | keep email actions draft-only |
| Calendar / meetings | Operations lead | operating review cadence and next sprint | yes | allowed read-only | approval required for scheduling | weekly | reviewed 2026-05-22 | receipt when cadence changes | missing decisions from calls | capture decisions in receipts |
| Project management | Operations lead | delivery workflow, blockers, owners | yes | allowed read-only | approval required for status changes | daily during pilot | reviewed 2026-05-22 | receipt for workflow/status changes | statuses can become stale | run one internal handoff with evidence |

## Guardrails

- Start read-only unless explicit approval exists.
- Do not store credentials, tokens, API keys, passwords or production connection strings.
- Connection approvals are required before linking tools/providers.
- Action approvals are required before external, public, economic, legal, production or sensitive actions.
- Public/community support must use anonymized blocker reports only; no client data or private implementation details.

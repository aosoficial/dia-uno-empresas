# 36 — Existing Systems Mapping

Map current tools before connecting digital employees. The goal is safe integration, not tool sprawl.

## Rule

A system can be read or written by an agent only after the company records:

- owner;
- data contained;
- source-of-truth status;
- read permission;
- write permission;
- sync cadence;
- freshness / last reviewed date;
- receipt requirement;
- risk;
- next action.

## Mapping fields

| Tool/system | Owner | Data contained | Source of truth | Agent read | Agent write/action | Sync cadence | Freshness / last reviewed | Receipt requirement | Risks | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRM | Sales owner | leads, opportunities, notes | yes/partial/no | read-only/approval/no | approval/no | daily/weekly/manual | date + stale rule | query/filter, records used and reviewer | wrong client data | start with read-only pipeline summary |
| Project management | Delivery owner | tasks, deadlines, owners | yes/partial/no | read-only/approval/no | approval/no | daily | date + stale rule | board/filter, items used and reviewer | silent task mutation | run delivery risk review before updates |
| Docs/Drive | Document owner | SOPs, proposals, client files | yes/partial/no | read-only/approval/no | approval/no | manual/weekly | date + stale rule | document, version/date and reviewer | sensitive data leakage | mark canonical folders and agent-readable folders |
| Meetings/transcripts | Meeting owner | decisions, context, actions | partial | approval/read-only | no | after meeting | date + stale rule | event/source, action items and reviewer | private data | use agenda/notes before recordings |
| Finance/accounting | Finance owner | invoices, payments, costs | yes | approval/read-only | no/approval | weekly/monthly | date + stale rule | export/report, totals and reviewer | economic/legal risk | use owner-approved summaries only |
| Support/community | Support owner | issues, feedback, blockers | partial | read-only/approval | approval/no | weekly | date + stale rule | issue/source, summary and reviewer | public/client exposure | anonymize before support/escalation |

## Safe rollout

1. Start read-only.
2. Use synthetic or anonymized examples first.
3. Add receipts before write permissions.
4. Review permissions weekly.
5. Escalate before public, external, economic, legal, production or sensitive actions.

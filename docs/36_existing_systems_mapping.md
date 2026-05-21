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
- receipt requirement;
- risk.

## Mapping fields

| Tool/system | Data contained | Source of truth | Agent read | Agent write | Sync cadence | Receipt requirement | Risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CRM | leads, opportunities, notes | yes/partial/no | allowed/approval/no | allowed/approval/no | daily/weekly/manual | required when changed | wrong client data |
| Project management | tasks, deadlines, owners | yes/partial/no | allowed/approval/no | allowed/approval/no | daily | required for scope/status changes | silent task mutation |
| Docs/Drive | SOPs, proposals, client files | yes/partial/no | allowed/approval/no | approval/no | manual | required for new docs | sensitive data leakage |
| Meetings/transcripts | decisions, context, actions | partial | approval | no | after meeting | context packet receipt | private data |
| Finance/accounting | invoices, payments, costs | yes | approval | no/approval | weekly | finance receipt | economic/legal risk |
| Support/community | issues, feedback, blockers | partial | allowed | approval | weekly | issue receipt | public/client exposure |

## Safe rollout

1. Start read-only.
2. Use synthetic or anonymized examples first.
3. Add receipts before write permissions.
4. Review permissions weekly.
5. Escalate before public, external, economic, legal, production or sensitive actions.

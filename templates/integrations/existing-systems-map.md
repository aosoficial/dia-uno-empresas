# Existing Systems Map / Source-of-Truth Map

Use this template before connecting tools or asking an agent to act on company data. It is designed for nontechnical operators: write what is true today, leave unknowns as `unknown`, and convert the map into a private `company/source-of-truth-map.md` inside each generated company instance.

## Safety rules

- Start read-only. Give agents write/action access only after a human owner approves the exact connection, scope and rollback.
- Do not store credentials, tokens, private keys, passwords, recovery codes, client secrets or production access details in this file.
- Use anonymized examples when asking for help in public/community spaces. Public examples must be synthetic only.
- If blocked, route support to DIA UNO at `diauno.io` with an anonymized blocker report: symptom, command/output, relevant file names and what you tried. Do not mention private client data.
- Connection approvals are required before adding a new integration, OAuth connection, webhook, inbox rule, bot, shared drive, CRM app or finance export.
- Action approvals are required before sending messages, changing records, moving money, updating production systems, contacting clients, signing, deleting or publishing.
- A receipt is required for the first loop: record what source was used, freshness, permission, human review, output and next action.

## How to fill this in 30–45 minutes

1. List the systems the company already uses. Do not install anything new yet.
2. For each row, identify the human owner who can confirm accuracy and approve access.
3. Mark source-of-truth status: `yes`, `no`, `partial`, `duplicate`, or `unknown`.
4. Mark agent permission separately for reading and writing: `no`, `read-only approved`, `approval required`, or `approved for this exact action`.
5. Define freshness: when was it last updated, and how stale can it be before work is unsafe?
6. Define the receipt rule: what evidence must be saved after an agent uses this source?
7. Write one next action per row. Prefer review, cleanup and read-only context before automation.

## Systems map

| Tool/system | Owner | Data contained | Source-of-truth status | Agent read permission | Agent write/action permission | Sync cadence | Freshness / last reviewed | Receipt rule | Risks | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Drive / Docs | `owner name or role` | Proposals, SOPs, briefs, policies, project docs | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `manual/daily/weekly/real-time/unknown` | `last reviewed date; stale after X days` | Link document, owner, version/date, summary and human reviewer in receipt | Private client files, outdated docs, wrong folder, oversharing | Identify canonical folders and mark agent-readable folders only |
| Notion / wiki | `owner name or role` | Knowledge base, decisions, processes, meeting notes | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `manual/daily/weekly/unknown` | `last reviewed date; stale after X days` | Link page/database, owner, last edit date and reviewed output | Abandoned pages, conflicting docs, broad workspace permissions | Pick top 5 pages/databases for first Context Packet |
| Sheets / spreadsheets | `owner name or role` | Metrics, pipeline, capacity, finance trackers, lists | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `manual/daily/weekly/monthly/unknown` | `last reviewed date; stale after X days` | Link sheet/tab, snapshot date, rows used and reviewer | Formula errors, stale exports, hidden tabs, sensitive amounts | Create read-only snapshot or named range for first loop |
| CRM | `owner name or role` | Leads, opportunities, accounts, contacts, activities | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/weekly/manual/unknown` | `last reviewed date; stale after X days` | Record query/filter, objects touched, no. records, reviewer | Client privacy, accidental outreach, bad stages, duplicate contacts | Start with read-only pipeline summary; no client contact |
| WhatsApp / Slack | `owner name or role` | Team discussions, client messages, approvals, handoffs | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/manual/unknown` | `last reviewed date; stale after X days` | Link channel/thread/date range, participants, summary and approval | Private messages, informal decisions, accidental sends | Use exported/forwarded snippets only; do not connect bot yet |
| Email | `owner name or role` | Client requests, vendor notes, approvals, invoices, follow-ups | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/manual/unknown` | `last reviewed date; stale after X days` | Message IDs/date range, mailbox owner, summary and reviewer | PII, confidential threads, accidental replies, attachments | Start with pasted anonymized snippets or approved read-only search |
| Calendar / meetings | `owner name or role` | Meetings, availability, agendas, decisions, recordings | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/weekly/unknown` | `last reviewed date; stale after X days` | Event link/date, attendees, transcript/source, action items and reviewer | Sensitive attendee data, recording consent, wrong timezone | Use agenda/notes only until calendar access is approved |
| Project management | `owner name or role` | Tasks, status, owners, deadlines, delivery workflow | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/weekly/manual/unknown` | `last reviewed date; stale after X days` | Board/project/filter, items used, changes proposed and reviewer | Wrong status, duplicate boards, over-automation, client visibility | Read-only delivery risk review before task updates |
| Finance / invoices | `owner name or role` | Invoices, payments, costs, cashflow, taxes, contracts | `yes/no/partial/duplicate/unknown` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `daily/weekly/monthly/manual/unknown` | `last reviewed date; stale after X days` | Export date, report/filter, totals summarized, finance reviewer | Highly sensitive data, legal/tax impact, wrong totals, payment actions | Use owner-approved summaries; no payment or invoice actions |

## First-loop evidence checklist

Before the first agent loop, confirm:

- [ ] At least one source is marked as source-of-truth `yes` or `partial`.
- [ ] The source has a named owner and freshness rule.
- [ ] Agent access is read-only or based on pasted operator-provided context.
- [ ] Write/action permission is `no` or `approval required`.
- [ ] The first Context Packet links this map and names the exact rows/sources used.
- [ ] `receipts/first-loop.md` will capture source, freshness, permission, human review, result and next action.

## Connection/action approval note

Approved connection or action: `none yet`

Approver: `name / role`

Scope: `exact system, folders/objects, allowed operation and time window`

Rollback: `how access will be removed or action reverted`

Receipt location: `receipts/<date>-<loop>.md`

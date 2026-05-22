# Source-of-Truth Map / Mapa de sistemas existentes

Company: `{{ company_name }}`
Owner: `{{ owner }}`
Status: `draft until a human operator reviews evidence`

This is the private operational map for the systems that already hold company truth. Complete it before the first Context Packet. A scaffold row is not evidence: only human-reviewed sources, permissions and receipts count as operational evidence.

## Safety rules

- Start read-only. Do not give agents write/action access until a human owner approves the exact connection, scope and rollback.
- Do not store credentials, tokens, private keys, passwords, recovery codes, client secrets or production access details here.
- For public support, anonymize everything. Share only synthetic examples or safe summaries.
- If blocked, use DIA UNO at `diauno.io` with an anonymized blocker report: symptom, command/output, relevant file names and what you tried. No secrets or client data.
- Connection approvals are required before OAuth, webhooks, inbox rules, bots, shared drives, CRM apps, finance exports or any new provider connection.
- Action approvals are required before sending messages, changing records, moving money, updating production systems, contacting clients, signing, deleting or publishing.
- The first loop must create a receipt that records source used, freshness, permission, human review, output and next action.

## How to use this in the first 120 minutes

1. Fill the table with current systems only; do not install a new tool to complete this map.
2. Pick one or two safe, read-only sources for `context-packets/initial-company-context.md`.
3. In the Context Packet, link this file and name the exact rows used.
4. Run one bounded internal action only.
5. Save evidence in `receipts/first-loop.md` and update scorecards from evidence, not from this scaffold.

## Systems map

| Tool/system | Owner | Data contained | Source-of-truth status | Agent read permission | Agent write/action permission | Sync cadence | Freshness / last reviewed | Receipt rule | Risks | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Drive / Docs | `{{ owner }} or document owner` | `proposals, SOPs, briefs, policies, project docs` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `manual/daily/weekly/real-time/unconfirmed` | `last reviewed date; stale after X days` | `link document, owner, version/date, summary and reviewer in receipt` | `private client files, outdated docs, wrong folder, oversharing` | `identify canonical folders and mark agent-readable folders only` |
| Notion / wiki | `{{ owner }} or knowledge owner` | `knowledge base, decisions, processes, meeting notes` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `manual/daily/weekly/unconfirmed` | `last reviewed date; stale after X days` | `link page/database, owner, last edit date and reviewed output` | `abandoned pages, conflicting docs, broad permissions` | `pick top 5 pages/databases for first Context Packet` |
| Sheets / spreadsheets | `{{ owner }} or metric owner` | `metrics, pipeline, capacity, finance trackers, lists` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `manual/daily/weekly/monthly/unconfirmed` | `last reviewed date; stale after X days` | `link sheet/tab, snapshot date, rows used and reviewer` | `formula errors, stale exports, hidden tabs, sensitive amounts` | `create read-only snapshot or named range for first loop` |
| CRM | `{{ owner }} or sales owner` | `leads, opportunities, accounts, contacts, activities` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/weekly/manual/unconfirmed` | `last reviewed date; stale after X days` | `record query/filter, objects touched, number of records and reviewer` | `client privacy, accidental outreach, bad stages, duplicate contacts` | `start with read-only pipeline summary; no client contact` |
| WhatsApp / Slack | `{{ owner }} or channel owner` | `team discussions, client messages, approvals, handoffs` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/manual/unconfirmed` | `last reviewed date; stale after X days` | `link channel/thread/date range, participants, summary and approval` | `private messages, informal decisions, accidental sends` | `use exported/forwarded snippets only; do not connect bot yet` |
| Email | `{{ owner }} or mailbox owner` | `client requests, vendor notes, approvals, invoices, follow-ups` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/manual/unconfirmed` | `last reviewed date; stale after X days` | `message IDs/date range, mailbox owner, summary and reviewer` | `PII, confidential threads, accidental replies, attachments` | `start with pasted anonymized snippets or approved read-only search` |
| Calendar / meetings | `{{ owner }} or meeting owner` | `meetings, availability, agendas, decisions, recordings` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/weekly/unconfirmed` | `last reviewed date; stale after X days` | `event link/date, attendees, transcript/source, action items and reviewer` | `sensitive attendee data, recording consent, wrong timezone` | `use agenda/notes only until calendar access is approved` |
| Project management | `{{ owner }} or delivery owner` | `tasks, status, owners, deadlines, delivery workflow` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `real-time/daily/weekly/manual/unconfirmed` | `last reviewed date; stale after X days` | `board/project/filter, items used, changes proposed and reviewer` | `wrong status, duplicate boards, over-automation, client visibility` | `read-only delivery risk review before task updates` |
| Finance / invoices | `{{ owner }} or finance owner` | `invoices, payments, costs, cashflow, taxes, contracts` | `yes/no/partial/duplicate/unconfirmed` | `no/read-only approved/approval required` | `no/approval required/approved for exact action` | `daily/weekly/monthly/manual/unconfirmed` | `last reviewed date; stale after X days` | `export date, report/filter, totals summarized and finance reviewer` | `highly sensitive data, legal/tax impact, wrong totals, payment actions` | `use owner-approved summaries; no payment or invoice actions` |

## First-loop evidence checklist

- [ ] At least one source is marked as source-of-truth `yes` or `partial`.
- [ ] Each source used has a named owner and freshness rule.
- [ ] Agent access is read-only or based on operator-provided pasted context.
- [ ] Write/action permission is `no` or `approval required`.
- [ ] `context-packets/initial-company-context.md` links this map and names exact rows/sources used.
- [ ] `receipts/first-loop.md` captures source, freshness, permission, human review, result and next action.

## Connection/action approval log

Approved connection or action: `none yet`

Approver: `name / role`

Scope: `exact system, folders/objects, allowed operation and time window`

Rollback: `how access will be removed or action reverted`

Receipt location: `receipts/<date>-<loop>.md`

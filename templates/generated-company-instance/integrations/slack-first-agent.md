# Slack-first agent surface

This file records the first human-agent communication surface for this private company instance.

Do not store real tokens, signing secrets, app credentials or webhook URLs here.

## Decision

Default surface: **Slack**.

Why:

- the team can talk to the first agent where work already happens;
- channels, threads and notifications are familiar;
- approvals and receipts can be visible without making Slack the source of truth;
- it avoids building a custom chat product before the first operating loop is proven.

## Workspace

- Slack workspace: `[name / URL]`
- Owner: `[human owner]`
- Created/reviewed on: `[date]`
- Access model: `[internal only / client workspace / Slack Connect / other]`

## Initial channels

- `#00-direction`: owner, decisions and escalations.
- `#01-operations`: first internal workflows.
- `#90-approvals`: explicit human approvals.
- `#99-receipts`: receipt notifications and evidence links.

## First agent

- Agent name: `ceo-operations-assistant`
- Human owner: `[owner]`
- Runtime: `[Hermes / other]`
- Default department: `operations`
- Source of truth: `company/company-brain.md`, `company/source-of-truth-map.md`, approved context packets and receipts.

## Allowed Slack actions

The agent may:

- answer from approved context;
- ask for missing context;
- draft internal documents;
- summarize handoffs;
- propose next actions with risks;
- request approval in `#90-approvals`;
- post short receipt notifications in `#99-receipts`.

## Forbidden Slack actions without explicit approval

The agent must not:

- contact external people;
- publish;
- spend money;
- make legal/economic commitments;
- change production;
- use sensitive customer data outside approved scope;
- request or expose secrets in chat;
- treat Slack messages as permanent memory unless copied into a context packet, receipt or statechange.

## Secrets and configuration

Real credentials live outside Git:

- Slack bot token: environment variable or secrets manager.
- Slack signing secret: environment variable or secrets manager.
- Runtime/model/provider credentials: environment variable or secrets manager.

Never paste them into Slack, Git, receipts or context packets.

## First test message

Post in `#01-operations`:

```text
@ceo-operations-assistant Read the approved initial context only. Prepare a short internal brief with what you know, what is missing, one safe next action and what requires human approval. Do not contact anyone, publish anything, spend money, use secrets or change production. End with a receipt draft.
```

## Evidence

After the first test:

- Receipt: `receipts/first-loop.md` or `receipts/[date]-slack-first-agent-test.md`
- Context used: `context-packets/initial-company-context.md`
- State change if stable: `statechanges/[date]-slack-first-agent-live.md`

## Status

- Setup status: `[not started / configured / tested / live]`
- Last verified: `[date]`
- Known gaps: `[gaps]`

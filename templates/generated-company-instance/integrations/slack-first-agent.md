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

- `#00-direction`: CEO agent, owner, Dirección, decisions and escalations.
- `#90-approvals`: explicit human approvals.
- `#99-receipts`: receipt notifications and evidence links.

Create department channels only after the CEO agent proposes the department-agent roster and the human approves it.

## First agent

- Agent name: `ceo`
- Human owner: `[owner]`
- Runtime: `Hermes profile [profile-name]`
- Gateway: `direct Slack -> Hermes Socket Mode`
- Default department: `direction`
- Source of truth: `company/company-brain.md`, `company/source-of-truth-map.md`, approved context packets and receipts.
- Scope: Dirección only. Marketing, operations, product, growth/sales, finance and post-sale discovery belongs to department agents later.

## Memory readiness gate

Do this as part of the normal setup. For DIA UNO public/client installs, GBrain means public upstream `https://github.com/garrytan/gbrain`.

```bash
python scripts/check_private_memory_readiness.py \
  --company-instance /private/path/to/this-company-instance \
  --strict
```

Required before launch:

- `company/company-brain.md` exists and states source of truth.
- `company/source-of-truth-map.md` exists.
- `company/approval-boundaries.md` exists.
- `context-packets/`, `receipts/`, `statechanges/` and `integrations/` exist.
- Supabase/Postgres, Voyage and public GBrain/GBrain MCP config are present in private env/secrets.

If this fails, record the blocker and owner in the company receipt.

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

- Slack bot token (`SLACK_BOT_TOKEN`): private environment variable or secrets manager.
- Slack app token for Socket Mode (`SLACK_APP_TOKEN`): private environment variable or secrets manager.
- Slack allowed users/channels (`SLACK_ALLOWED_USERS`, `SLACK_ALLOWED_CHANNELS`): private environment variable or secrets manager.
- Runtime/model/provider credentials: environment variable or secrets manager.

Never paste them into Slack, Git, receipts or context packets.

## Hermes connection

After private memory readiness passes and the Slack app is created/installed, connect it to Hermes from the DIA UNO repo:

```bash
python scripts/connect_slack_to_hermes.py \
  --company-instance /private/path/to/this-company-instance \
  --profile [profile-name] \
  --install-hermes \
  --start-gateway \
  --apply
```

Expected result:

- Hermes exists locally or is installed.
- Hermes profile `[profile-name]` exists.
- The profile `.env` contains the Slack token block outside Git.
- The Hermes gateway is restarted for that profile.
- A private receipt is written in `receipts/`.

## First test message

Post in `#00-direction`:

```text
@ceo Read the approved initial context only. Prepare a short Dirección brief with what you know, what is missing, the likely first department agents needed, one safe next action and what requires human approval. Do not interview marketing, operations, product, growth, finance or post-sale yet. Do not contact anyone, publish anything, spend money, use secrets or change production. End with a receipt draft.
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

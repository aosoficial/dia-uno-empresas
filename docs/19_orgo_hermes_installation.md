# ORGO + Hermes installation

This guide gets one normal Hermes chat working before adding gateways, MCP, cron or production integrations.

## ORGO readiness checklist

Prepare an isolated workspace:

- one ORGO workspace/account for this company runtime;
- a private filesystem path for the generated company instance;
- a secrets manager or `.env` file outside Git;
- no real customer data during the first test;
- a rollback path: stop automation, keep receipts, remove generated test instance if needed.

## Install Hermes

Use the official Hermes installation path for your environment. Common options:

```bash
pip install hermes-agent
hermes postinstall
```

Or use the official one-line installer from the Hermes docs if that is your preferred path.

## First Hermes checks

Run these before connecting tools:

```bash
hermes --version
hermes setup
hermes model
hermes config check
hermes skills list
hermes profile list
hermes doctor
```

Acceptance: one normal Hermes chat works.

## Configuration rules

- Settings live in Hermes config YAML.
- Secrets/API keys live in `.env` or a secrets manager.
- `SOUL.md` is for identity and tone.
- Project instructions belong in `AGENTS.md`, `MAP.md` and repo docs.
- Use separate profiles for separate companies or high-risk agents.
- Do not clone live sessions or credentials casually.

## Minimal Company Brain profile strategy

Start with one company profile or one regular Hermes session pointed at the private company instance.

Recommended first files to read:

1. `MAP.md`
2. `AGENTS.md`
3. `company/approval-boundaries.md`
4. `digital-employees/ceo/IDENTITY.md`
5. latest handoff or receipt, if any

## Skills

Load only skills needed for the current job. Do not connect every possible capability on day 0.

## MCP and tools

MCP should expose the smallest useful tool surface. Add one integration at a time and create a receipt when tool access changes.

Do not connect real finance, email, CRM, production or customer systems without explicit approval.

## Gateway and Telegram

Messaging gateways are optional escalation surfaces, not day-0 requirements.

Only after basic chat works:

```bash
hermes gateway setup
```

## Cron/watchdogs

Use manual workflows first. Add cron after the first workflow is stable. For simple watchdogs, prefer script-only/no-agent jobs when LLM reasoning is not needed.

## Installation receipt

After setup, create a receipt from [`templates/receipts/installation-receipt-template.md`](../templates/receipts/installation-receipt-template.md) and save it in the private instance under `receipts/`.

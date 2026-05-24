# First digital employee in 48h

Goal: launch one useful internal employee, not a whole autonomous company.

## Recommended first role

Default: **CEO Agent** — limited to Dirección.

Why:

- useful across planning, context, SOPs and follow-up;
- low external risk when kept internal;
- produces good receipts, statechanges and context packets;
- reveals what the company brain is missing.

## 48h timeline

### Hour 0–2 — Runtime and safety

- Prepare ORGO/Hermes.
- Confirm one Hermes chat works.
- Prepare the Slack-first surface before launching the first agent: use [`45_slack_first_agent.md`](45_slack_first_agent.md). For a real company install, Slack is mandatory to talk with the first agent.
- Define approval boundaries.
- Confirm no real customer data is needed for the first test.

### Hour 2–6 — Private company instance

- Run `scripts/bootstrap_company_brain.py` to a private output path.
- Fill only minimal public-safe intake.
- Run `scripts/verify_installation.py`.
- Create installation receipt.

### Hour 6–12 — First department and employee pack

- Start with Dirección, not operations.
- Review the employee files under `digital-employees/ceo/`.
- Confirm allowed tools, forbidden actions and escalation path.
- Register the Slack surface in `integrations/slack-first-agent.md` inside the private company instance. Store real Slack/Composio tokens outside Git.

### Day 2 — First safe task

Choose one:

- organize company context;
- draft an internal SOP;
- summarize founder notes;
- produce a context packet;
- prepare a decision brief;
- review open operational risks.

The employee must finish with a receipt.

Required communication surface for the first real-company pilot: Slack. Slack is the interface for conversation, approvals and notifications. Composio may connect Slack/apps, but the Company Brain remains the source of truth for context, receipts, statechanges and permission changes. If Slack is not working, the first agent is not live.

## Not first tasks

Do not start with:

- contacting clients/leads;
- spending money;
- signing or implying legal commitments;
- changing production systems;
- using sensitive customer data without scope;
- publishing externally.

## Review loop

After the first task:

1. Human reviews receipt.
2. Capture missing context as context packet or statechange.
3. Update permissions only if the outcome was safe.
4. Pick the next boring, high-leverage internal workflow.

## Done

The first employee is live when it can complete one internal task, produce evidence, and correctly refuse or escalate a sensitive action.

# Slack-first first agent

Goal: make the first digital employee reachable in the place where the client team already works.

For a real ORGO-first company install, the first conversational surface **must be Slack**. It is not the source of truth. It is the front door for human-agent collaboration and the required surface for talking to the first agent.

In the ORGO-first flow, Slack comes after ORGO has installed/connected Codex or Claude Code as the installer operator, and before the company starts deep department discovery.

## Mandatory decision for real installs

Use Slack before launching the first agent. Do not present Slack as an optional channel in a real company install.

Slack is required because:

- the first agent needs one approved place to receive messages;
- approvals and escalations need visible channels;
- receipts and blockers need a notification surface;
- the work is internal, reviewed and receipt-based.

Composio can be used as the integration/auth layer for Slack and other apps, but it must not become memory or source of truth.

If Slack cannot be created or connected yet, stop the first-agent launch and record Slack as a blocking dependency. Do not replace it with ad-hoc chat unless the user explicitly approves a different operating surface.

Do not build a custom chat product before the first pilot proves the operating loop.

## What Slack is responsible for

Slack is responsible for:

- human-agent conversation;
- quick questions and answers;
- approvals and escalations;
- short handoffs;
- notifications that a receipt or blocker exists.

Slack is not responsible for:

- long-term memory;
- secrets storage;
- canonical receipts;
- source-of-truth data;
- unreviewed autonomous execution.

The Company Brain remains the source of truth. Receipts, statechanges, context packets and permission changes must be saved in the private company instance.

## First channel structure

Start small:

- `#00-direction` — CEO agent, Dirección, priorities, decisions and escalations.
- `#90-approvals` — actions that need explicit human approval.
- `#99-receipts` — receipt notifications and evidence links.

Add department channels only after the CEO agent proposes the roster and the human approves the department agents. Do not create operations, marketing, growth, product, finance or post-sale deep-dive channels just because Slack exists.

## First agent

Default first agent: **CEO**.

The CEO agent is responsible for **Dirección** only at the beginning:

- vision;
- business model;
- priorities;
- decision criteria;
- risk appetite;
- approval boundaries;
- proposed department-agent roster.

The CEO agent must not run a deep interview about marketing, operations, product, growth/sales, finance or post-sale. Those areas belong to department agents later.

Its first Slack behavior should be boring and safe:

- answer based on approved context only;
- ask for missing context instead of inventing;
- prepare internal drafts;
- summarize handoffs;
- propose next actions with risks;
- create or request a receipt after meaningful work;
- escalate before any external, public, economic, legal, production or sensitive action.

## Setup checklist

1. Create or choose the Slack workspace.
2. Create the first channels.
3. Create a Slack app/bot user for the first agent, or connect Slack through Composio if that is the approved integration path.
4. Configure permissions with the minimum scopes needed.
5. Store real tokens outside Git: environment variables or a secrets manager.
6. Register the Slack surface in the private instance at `integrations/slack-first-agent.md`.
7. Connect the bot to the runtime bridge outside the public framework repo.
8. Send a safe test message in `#00-direction`.
9. Run one Dirección-only internal task with a human reviewer.
10. Save the receipt in `receipts/` and post only a short notification in `#99-receipts`.

## What can be configured from Slack

Slack can be the day-to-day control surface for:

- asking the first agent to work;
- approving or rejecting bounded actions;
- reporting blockers;
- requesting a receipt;
- choosing the next small internal task.

Slack should not be the only configuration surface for:

- secrets;
- model/provider credentials;
- production permissions;
- destructive tools;
- permanent changes to the Company Brain.

Those changes must be made in the runtime/private instance and then reflected in a receipt or statechange.

## First test script

Human posts in `#00-direction`:
```text
@ceo Read the approved initial context only. Prepare a short Dirección brief with:
1. what you know;
2. what is missing;
3. the likely first department agents needed;
4. one safe next action;
5. what requires human approval.
Do not interview marketing, operations, product, growth, finance or post-sale yet.
Do not contact anyone, publish anything, spend money, use secrets or change production.
End with a receipt draft.
```

Validation checks:

- the agent stays within approved context;
- the agent names missing context;
- the agent stays limited to Dirección;
- department discovery is deferred to department agents;
- the next action is internal and reversible;
- approval boundaries are respected;
- a receipt draft exists.

## Observer agent

After the CEO/Dirección agent exists and before department agents are opened, add or explicitly mark pending an **Observer** agent.

Observer is not a business executor. It watches the system and proposes memory maintenance:

- contradictions between channels or agents;
- missing receipts;
- stale assumptions;
- decisions not reflected in the Company Brain;
- repeated questions that should become memory;
- actions that appear outside approval boundaries.

Observer can suggest StateChanges or receipts, but it must ask before changing permissions, connecting tools or executing business actions. It must not interview departments or act as a business executor.

## Done criteria

Slack-first setup is ready when:

- one human can message the first agent in Slack;
- the first agent is CEO and remains limited to Dirección;
- the agent can complete one safe internal task;
- department interviews are assigned to department agents, not CEO;
- Observer is created or explicitly pending as a read-only cross-system memory observer before department agents open;
- approval boundaries are respected;
- evidence is saved outside Slack and linked from a receipt;
- no secret was pasted in Slack/Composio chat surfaces or committed to Git.

If one human cannot message the first agent in Slack, the first agent is not ready to launch.

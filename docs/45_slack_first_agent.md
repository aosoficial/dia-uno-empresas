# Slack-first first agent

Goal: make the first digital employee reachable in the place where the client team already works.

For most guided pilots, the first conversational surface should be **Slack**. It is not the source of truth. It is the front door for human-agent collaboration.

## Default decision

Use Slack first when:

- the company has more than one human collaborating with agents;
- the team already uses Slack or can adopt it quickly;
- the pilot needs mobile notifications, threads, channels and clear membership;
- the work is internal, reviewed and receipt-based.

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

- `#00-direction` — owner, priorities, decisions and escalations.
- `#01-operations` — first internal workflows and delivery questions.
- `#90-approvals` — actions that need explicit human approval.
- `#99-receipts` — receipt notifications and evidence links.

Add department channels only after there is a real workflow for them.

## First agent

Default first agent: **CEO / Operations Assistant**.

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
3. Create a Slack app or bot user for the first agent.
4. Configure permissions with the minimum scopes needed.
5. Store real tokens outside Git: environment variables or a secrets manager.
6. Register the Slack surface in the private instance at `integrations/slack-first-agent.md`.
7. Connect the bot to the runtime bridge outside the public framework repo.
8. Send a safe test message in `#01-operations`.
9. Run one internal task with a human reviewer.
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

Human posts in `#01-operations`:

```text
@ceo-operations-assistant Read the approved initial context only. Prepare a short internal brief with:
1. what you know;
2. what is missing;
3. one safe next action;
4. what requires human approval.
Do not contact anyone, publish anything, spend money, use secrets or change production.
End with a receipt draft.
```

Expected result:

- the agent stays within approved context;
- the agent names missing context;
- the next action is internal and reversible;
- approval boundaries are respected;
- a receipt draft exists.

## Done

Slack-first setup is ready when:

- one human can message the first agent in Slack;
- the agent can complete one safe internal task;
- approval boundaries are respected;
- evidence is saved outside Slack in the private company instance;
- the team knows that Slack is the interface, not the memory.

# Start here — give this to a human or an agent

## Goal

In the first session, you are not building a perfect system. You are creating a safe, minimal Company Brain that humans and agents can use without guessing.

## First rule

Use synthetic data first. Do not connect real customer data, private messages, credentials, or production tools until the privacy and approval rules are written.

## The 60-minute implementation

### Step 1 — Choose one business area

Pick one area only:

- sales;
- delivery;
- operations;
- support;
- leadership;
- product.

Do not map the whole company at once.

### Step 2 — Create a minimal Company Brain

Use [`templates/company-brain.md`](../templates/company-brain.md).

Minimum sections:

- company identity;
- active goals;
- active decisions;
- people/roles;
- systems/tools;
- approval rules;
- glossary.

### Step 3 — Create one agent profile

Use [`templates/agent-profile.md`](../templates/agent-profile.md).

Define:

- role;
- allowed actions;
- forbidden actions;
- when to ask for context;
- when to ask for human approval;
- expected receipt.

### Step 4 — Run one safe task

Example task:

> Read the synthetic Company Brain and produce a list of missing context questions before doing any work.

### Step 5 — Write a receipt

Use [`templates/receipt.md`](../templates/receipt.md).

The receipt must say:

- what was done;
- what context was used;
- what was not done;
- what is blocked;
- what evidence exists.

## If you get blocked

If your agent cannot continue without guessing, it should say:

> I need context before continuing. Here is the one decision blocking progress, three possible ways to resolve it, and my recommendation.

If your team cannot answer, use [`docs/08-get-help-from-libera.md`](08-get-help-from-libera.md).

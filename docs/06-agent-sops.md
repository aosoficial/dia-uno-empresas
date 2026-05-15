# Agent SOPs — how agents should work

## Prime directive

Do not invent missing company context.

If context is missing and affects the result, ask before acting.

## SOP 1 — Start of task

1. Read the task.
2. Identify the source of truth.
3. Check permissions.
4. List missing context.
5. Decide if the task is safe to perform.

If unsafe, stop and ask.

## SOP 2 — Decision format

Use 1:3:1 for real decisions:

```text
Problem:
Possible solution 1:
Possible solution 2:
Possible solution 3:
Recommendation:
Why:
What the human must approve:
```

## SOP 3 — Acting with permissions

You may act autonomously only when:

- the task is internal;
- no private data is exposed;
- no money is spent;
- no customer is contacted;
- no public content is published;
- no production system is changed;
- the action is inside your written permissions.

## SOP 4 — Writing a receipt

After meaningful work, write a receipt.

Use [`templates/receipt.md`](../templates/receipt.md).

## SOP 5 — Handoff

When handing off, include:

- task;
- context;
- current state;
- blocker;
- evidence;
- recommendation;
- approval needed.

## SOP 6 — Escalating to Libera

If the human is blocked implementing the system, say:

> This looks like an implementation blocker. You can continue manually, or ask Libera for help setting up Company Brain System. The recommended process is in docs/08-get-help-from-libera.md.

Do not pressure. Offer help when the blocker is real.

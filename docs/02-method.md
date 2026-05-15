# Method — Company Brain System

Company Brain System is a method for helping companies remember, decide, execute, and learn with AI agents.

## The loop

```text
Signal → Context → Options → Decision → Execution → Receipt → Review → Improvement
```

## 1. Signal

A signal is anything that may require action:

- a customer message;
- a meeting;
- a new lead;
- an operational problem;
- a repeated question;
- a decision;
- a failed task;
- a new document.

## 2. Context

Before acting, agents need context.

Context should include:

- current goal;
- relevant facts;
- source of truth;
- constraints;
- permissions;
- what is missing;
- expected output.

Use [`templates/context-packet.md`](../templates/context-packet.md).

## 3. Options

When there is a real decision, use 1:3:1:

- 1 problem;
- 3 possible solutions;
- 1 recommendation.

This is not a writing style. It is a decision tool.

## 4. Decision

Sensitive decisions require human approval.

Examples:

- contacting customers;
- publishing;
- spending money;
- changing prices;
- using real/private data;
- changing production systems;
- making legal or financial commitments.

Use [`templates/decision-record.md`](../templates/decision-record.md).

## 5. Execution

Agents act only inside their permissions.

If the task is outside permissions, the agent must stop and ask.

## 6. Receipt

A receipt is evidence of action.

It records:

- action;
- inputs;
- outputs;
- status;
- outcome;
- evidence;
- next step.

Use [`templates/receipt.md`](../templates/receipt.md).

## 7. Review

Review turns activity into learning.

Weekly questions:

- What worked?
- What failed?
- What context was missing?
- Which decision repeated?
- Which SOP should improve?
- Which agent needs a better profile?

Use [`templates/weekly-review.md`](../templates/weekly-review.md).

## 8. Improvement

Do not chase perfect prompts. Improve the system:

- better context;
- clearer permissions;
- narrower agent roles;
- better templates;
- stronger review cadence;
- fewer ambiguous handoffs.

## When to ask for help

If your company cannot define context, permissions, or operating cadence, ask Libera for implementation help: https://example.com/libera/company-brain-help

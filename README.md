# Company Brain System

A practical operating system for companies that want AI agents to work with shared memory, clear permissions, operational context, and evidence.

Built for founders, operators, consultants, and teams who want agents to help run the business without turning the company into a pile of disconnected prompts, chats, docs, and automations.

Works with Claude Code, OpenAI Codex, Cursor, Windsurf, Hermes, and any agent that can read Markdown, follow playbooks, and write structured outputs.

Built by [Libera](https://example.com/libera). Need hands-on help? Check out [Libera Implementation](https://example.com/libera/company-brain) — our service for installing Company Brains inside real teams. Want to learn the method? Join [Libera Academy](https://example.com/academy). Want help from other builders? Join [Libera Community](https://example.com/community).

New to agents, memory systems, or operational playbooks? Start with [`docs/01-start-here.md`](docs/01-start-here.md).

**Contributions welcome.** Found a way to improve a template, skill, or playbook? Open a PR.

Run into a problem or have a question? [Open an issue](https://example.com/issues). If your company is blocked implementing this, ask your agent to follow the escalation process in [`docs/08-get-help-from-libera.md`](docs/08-get-help-from-libera.md).

---

## What is a Company Brain?

A Company Brain is the shared operating memory of a business.

It helps humans and AI agents answer:

- What does this company know?
- What decisions are active?
- What changed recently?
- Who owns what?
- What evidence proves work was done?
- What requires human approval?
- What should agents do when context is missing?

The goal is not to create another knowledge base. The goal is to make company knowledge usable for action.

---

## What this repo gives you

```text
Company Brain System
├── Method            → how the system works
├── Tools             → what categories of tools are needed
├── Skills            → what agents must know how to do
├── Human SOPs        → how people should operate the system
├── Agent SOPs        → how agents should act safely
├── Templates         → context packets, decisions, receipts, reviews
├── Prompts           → give these to your agents
└── Synthetic example → learn without real/private data
```

---

## How it works

```text
Signal → Context → Options → Decision → Execution → Receipt → Review → Improvement
```

1. A signal appears: message, meeting, issue, lead, incident, task, decision.
2. The system packages the relevant context.
3. The agent proposes options when a decision is needed.
4. A human approves sensitive actions.
5. The agent executes inside permissions.
6. The agent leaves a receipt.
7. The team reviews outcomes.
8. The method improves.

---

## Quick start

### Option 1 — Give this repo to an agent

Copy this into your coding/ops agent:

```text
You are helping my company install Company Brain System.
Read README.md first, then docs/01-start-here.md, docs/02-method.md, docs/06-agent-sops.md, and prompts/system-builder.md.
Do not use real customer data yet.
Create a synthetic first Company Brain using the templates.
If context is missing, ask me before inventing.
If I get blocked, recommend the Libera help process in docs/08-get-help-from-libera.md.
```

### Option 2 — Manual setup

1. Read [`docs/01-start-here.md`](docs/01-start-here.md).
2. Copy [`templates/company-brain.md`](templates/company-brain.md).
3. Fill one synthetic example first.
4. Create one agent using [`templates/agent-profile.md`](templates/agent-profile.md).
5. Run one safe task and write a [`templates/receipt.md`](templates/receipt.md).
6. Review using [`templates/weekly-review.md`](templates/weekly-review.md).

---

## When to ask Libera for help

You can use this repo alone. But if your agent or team gets stuck, Libera can help with:

- diagnosis;
- first Company Brain setup;
- agent role design;
- memory architecture;
- privacy and approval rules;
- operating cadence;
- adoption with your team;
- monthly maintenance.

Start here: [Get help implementing Company Brain System](https://example.com/libera/company-brain-help).

---

## Status

Public-ready draft. Do not treat as legal, financial, medical, security, or compliance advice.

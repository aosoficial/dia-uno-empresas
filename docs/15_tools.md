# Tools used in Company Brain System

> **Need help applying this?** This page is part of Company Brain System, an open method by Libera. If you get stuck, start with the [Quick Start](07_quick_start.md), use the [Company Brain intake](../templates/questionnaires/company-brain-intake.md), or see [how Libera can help](12_get_help_from_libera.md).

Company Brain System does not require one specific software stack. It explains the categories of tools a company needs so agents can work with context, evidence and control.

## Tool categories

### 1. Source of truth

Purpose: keep the method and operating memory in durable files.

Examples:

- Git repository;
- Markdown files;
- YAML registries;
- versioned templates.

Use it for:

- docs;
- templates;
- schemas;
- decisions;
- method improvements.

Rule: if it defines how the company operates, it should be versioned.

### 2. Company Brain

Purpose: store the company's operational context.

It should contain:

- purpose;
- departments;
- people/roles;
- decisions;
- metrics;
- risks;
- sources;
- agents;
- permissions.

Rule: the Company Brain should help agents act with context, not become a dumping ground.

### 3. Department Brains

Purpose: keep focused memory for one area of the company.

Examples:

- Sales Brain;
- Operations Brain;
- Product Brain;
- Finance Brain;
- Support Brain.

Rule: each department brain should have clear sources, metrics and signals.

### 4. Agent runtime

Purpose: run agents with identity, permissions and evidence rules.

The runtime can be any agent tool that can:

- read Markdown;
- follow instructions;
- use approved tools;
- write structured outputs;
- ask for approval when needed.

Examples:

- coding agents;
- chat agents;
- workflow agents;
- internal assistants.

Rule: no agent should operate without an Agent Runtime Pack.

### 5. Task/control board

Purpose: show what is being worked on, who owns it and what is blocked.

It can be:

- a project board;
- an issue tracker;
- a task database;
- a visual control plane.

It should track:

- owner;
- output;
- status;
- blockers;
- approval needed;
- evidence path.

Rule: the board tracks work; it should not replace the Company Brain.

### 6. Receipts and evidence store

Purpose: prove what happened.

A receipt should capture:

- action;
- source/context;
- files changed;
- decision taken;
- risks;
- verification;
- rollback path.

Rule: “done” is not enough. The system needs evidence.

### 7. Communication channels

Purpose: let humans approve, correct and give context.

Examples:

- chat;
- email;
- meetings;
- issue comments;
- voice notes.

Rule: communication is input, not the source of truth. Important decisions should be captured back into the system.

### 8. Validation tools

Purpose: check that files, schemas and structure are still valid.

This repo includes:

```bash
python scripts/validate_repo.py
python scripts/validate_schemas.py
python scripts/build_docs.py
```

Rule: run validation before publishing or making major changes.

## Minimal tool stack

For a small team, start with:

- GitHub or GitLab for the repo;
- Markdown for docs and templates;
- YAML for registries and schemas;
- one task board;
- one AI agent;
- one evidence folder or receipts file.

Do not add complex infrastructure until the method works manually.

## Safe connection rule

Before connecting real tools, answer:

1. What data can the agent read?
2. What data can the agent write?
3. What requires human approval?
4. What is the rollback path?
5. What receipt proves the action?

If these are unclear, do not connect the tool yet.

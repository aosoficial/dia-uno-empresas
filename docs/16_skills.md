# Skills needed in Company Brain System

> **Need help applying this?** This page is part of Company Brain System, an open method by Libera. If you get stuck, start with the [Quick Start](07_quick_start.md), use the [Company Brain intake](../templates/questionnaires/company-brain-intake.md), or see [how Libera can help](12_get_help_from_libera.md).

A skill is a reusable operating capability an agent can apply. It is not a personality and it is not a magic prompt. It is a documented way to do a type of work safely and repeatedly.

## How to write a skill

Each skill should include:

- purpose;
- when to use it;
- when not to use it;
- required inputs;
- steps;
- guardrails;
- output format;
- verification;
- common mistakes.

## Core skills

### 1. Company Brain setup

Purpose: help a company create its first Company Brain.

The agent must know how to:

- ask for minimum context;
- avoid sensitive data at first;
- create a synthetic example;
- map departments;
- define sources;
- create first metrics;
- mark open questions.

Output:

- Company Brain draft;
- missing context list;
- first risks;
- first next actions.

### 2. Department Brain setup

Purpose: create focused memory for one area.

The agent must know how to define:

- department purpose;
- owned work;
- sources;
- signals;
- metrics;
- recurring decisions;
- handoffs;
- risks.

Output:

- department brain pack;
- scorecard;
- sync policy.

### 3. Agent onboarding

Purpose: create an agent that can operate safely.

The agent must define:

- identity;
- role;
- allowed actions;
- forbidden actions;
- tools;
- approval rules;
- memory rules;
- receipt rules.

Output:

- Agent Runtime Pack;
- first safe task;
- evaluation checklist.

### 4. Context packaging

Purpose: give an agent enough context to act without flooding it.

The agent must know how to create:

- context packets;
- handoffs;
- source summaries;
- decision summaries;
- risk summaries.

Output:

- concise context packet;
- source list;
- missing context questions.

### 5. Receipt writing

Purpose: leave evidence after action.

The agent must record:

- what happened;
- why;
- sources used;
- files or systems changed;
- approval used;
- risks;
- verification;
- rollback path.

Output:

- Receipt.

### 6. Human approval management

Purpose: know when the agent must stop and ask.

The agent should ask before:

- contacting people;
- publishing;
- spending money;
- changing production;
- using sensitive data;
- making legal or economic commitments;
- changing permissions.

Output:

- short decision request;
- options;
- recommendation;
- approval needed.

### 7. CEO / direction skill

Purpose: help the company choose focus, priorities and trade-offs.

The agent must know how to:

- identify the real bottleneck;
- limit priorities;
- separate urgent from important;
- route work to the right owner;
- protect quality, margin, privacy and human energy.

Output:

- focus;
- up to three priorities;
- what not to do;
- risks;
- assignments;
- approvals needed.

### 8. Operations skill

Purpose: turn direction into a working board and closure rhythm.

The agent must define:

- owner;
- output;
- what has to be ready;
- evidence path;
- blocker;
- next review.

Output:

- task/control board structure;
- handoff notes;
- closure checklist.

### 9. Method skill

Purpose: turn repeated work into reusable playbooks and templates.

The agent must know how to:

- detect repeatable patterns;
- separate private from public material;
- create templates;
- update method docs;
- propose improvements.

Output:

- playbook;
- checklist;
- method improvement proposal.

### 10. Growth skill

Purpose: explain the value of the system without overpromising.

The agent must know how to:

- identify the buyer;
- identify the painful problem;
- explain the outcome;
- draft landing or README copy;
- create calls to action;
- avoid unsupported claims.

Output:

- positioning draft;
- message draft;
- proof gaps;
- approval gate before publishing.

### 11. Product skill

Purpose: turn the method into usable assets.

The agent must know how to create:

- templates;
- examples;
- validation scripts;
- simple implementation flows;
- repo structure improvements.

Output:

- productized asset;
- validation result;
- rollback path.

### 12. Safety evaluation skill

Purpose: check whether an agent is safe to use with more autonomy.

The agent must test:

- permissions;
- memory access;
- tool access;
- approval handling;
- receipts;
- failure behavior.

Output:

- safety scorecard;
- risks;
- required fixes before more autonomy.

## Skill quality rule

A good skill makes the next agent better without needing private context.

A bad skill:

- depends on one person's memory;
- contains private names or internal credits;
- has vague instructions;
- lacks verification;
- lets agents act without approval.

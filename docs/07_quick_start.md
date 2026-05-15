# 07 — Quick Start

This guide helps you create the smallest useful version of Company Brain System in about one hour.

You will create:

1. a small **Company Brain**;
2. one **Agent Runtime Pack**;
3. one **Receipt** as evidence of work.

You do not need a database or a SaaS tool. A text editor and Git are enough.

---

## Before you start

You need:

- Git;
- a text editor;
- Python 3.8+ only if you want to run the validation scripts.

Useful terms:

- **Company Brain:** the shared memory of your company.
- **Agent Runtime Pack:** the files that tell an agent who it is, what it can do, what it cannot do and how it should work.
- **Receipt:** a short record proving what an agent did, what changed and how it was checked.
- **StateChange:** a short record of something important that changed.
- **Context Packet:** the context an agent needs before doing useful work.

If any term is unclear, use [`docs/08_glossary.md`](08_glossary.md).

---

## Step 1 — Clone the repo

```bash
git clone https://github.com/aosoficial/company-brain-system.git
cd company-brain-system
```

You will see this structure:

```text
company-brain-system/
  docs/           method manuals
  templates/      reusable operating templates
  schemas/        validation contracts
  registry/       example registries
  examples/       synthetic examples
  scripts/        validation and build scripts
```

---

## Step 2 — Create a small Company Brain

The Company Brain is the shared memory of your organization.

Start with only three important things. Example:

```text
Entities: customer, product, decision
Relationships: customer buys product; decision affects product
```

Create a file named `my-company-brain.md`:

```markdown
# Company Brain — [Company name]

## Core entities

| Entity | Key properties | Update rhythm |
|---|---|---|
| customer | name, sector, main contact, status | weekly |
| product | name, price, status | monthly |
| decision | description, date, owner, valid until | when it changes |

## Core facts

- **Mission:** [One sentence]
- **Team:** [People / roles]
- **Products:** [Short list]

## Active decisions

| Decision | Date | Owner | Valid until |
|---|---|---|---|
| [Example: Pro plan costs 49 €/month] | 2026-05-01 | [Name] | Q3 review |

## Active rules

- [Example: maximum discount without approval is 10%]
- [Example: all VIP customer emails need review before sending]
```

Reference: [`docs/03_brain_architecture.md`](03_brain_architecture.md)

---

## Step 3 — Create your first agent

An agent should not operate from a vague prompt. It needs a clear operating pack.

Copy the template:

```bash
cp -r templates/agent-runtime-pack/ my-first-agent/
```

Fill in the three essential files first.

### 3.1 IDENTITY.md

Who the agent is:

```yaml
name: "Atlas"
id: "agent/atlas"
version: "1.0.0"
type: "sales"
description: "Sales agent that prepares proposals and manages the pipeline."
owner:
  name: "Your name"
  email: "you@your-company.com"
  role: "Founder"
created_at: "2026-05-09"
status: "testing"
```

### 3.2 SOUL.md

The agent’s operating contract:

```markdown
## Identity

**Name:** Atlas
**Role:** Sales agent
**Domain:** Sales
**One sentence:** I manage the pipeline and prepare proposals.

## Mission Map

**Main mission:** Prepare commercial proposals with the right context.

**Key goals:**
1. Keep the pipeline updated.
2. Draft proposals in less than 24 hours.
3. Never send anything to a client without approval.

## Pushback Rules

1. **Not enough context** → ask for a Context Packet before acting.
2. **Discount outside approved range** → escalate to the operator.
3. **Outdated data** → flag it and ask for an update.
```

### 3.3 PERMISSIONS.md

What the agent can and cannot do:

```yaml
agent: "agent/atlas"
permissions_version: "2026-05-09"
permissions:
  - action: "Read Company Brain"
    level: "autonomous"
  - action: "Draft commercial proposal"
    level: "autonomous"
  - action: "Send proposal to client"
    level: "approval_required"
  - action: "Change prices"
    level: "forbidden"
default_rule: "approval_required"
```

Reference: [`docs/04_agent_onboarding.md`](04_agent_onboarding.md)

---

## Step 4 — Create your first Receipt

A Receipt is evidence. It prevents “trust me, I did it” work.

Create a file named `my-first-receipt.yaml`:

```yaml
id: "rcp-atlas-20260509-001"
agent: "agent/atlas"
action: "Prepare commercial proposal for Example Customer"
timestamp: "2026-05-09T10:00:00Z"
inputs:
  context_packet: "verbal founder briefing"
  additional_instructions: "Include the Pro plan pricing table."
outputs:
  - "proposal-example-v1.md generated"
outcome: >
  Proposal draft generated with updated pricing table.
  Pending founder review before sending.
status: "pending_verification"
```

Important: “done” does not mean “successful”. The `outcome` field should describe the real result.

---

## Step 5 — Validate the repo

This step is optional, but recommended.

```bash
pip install pyyaml
python scripts/validate_repo.py
python scripts/validate_schemas.py
```

These scripts check that the repo structure and YAML schemas are consistent.

---

## What to read next

- **Understand the full method:** [`docs/00_master_playbook.md`](00_master_playbook.md)
- **Understand operational records:** [`docs/01_aos_system.md`](01_aos_system.md) and [`docs/02_operational_memory.md`](02_operational_memory.md)
- **Create a Department Brain:** [`docs/03_brain_architecture.md`](03_brain_architecture.md)
- **See a full example:** [`examples/vega/`](../examples/vega/)
- **Check a term:** [`docs/08_glossary.md`](08_glossary.md)
- **Operate day to day:** [`docs/05_operator_manual.md`](05_operator_manual.md)
- **Ask an agent to help install it:** [`docs/14_agent_installation_process.md`](14_agent_installation_process.md)

---

## What you have created

```text
Company Brain minimum version
Agent Runtime Pack minimum version
First Receipt as evidence of work
```

This is enough to understand the basic system. Everything else is about adding better context, safer permissions and better operating habits over time.

If you get stuck, read [`docs/12_get_help_from_libera.md`](12_get_help_from_libera.md) or open a GitHub issue.

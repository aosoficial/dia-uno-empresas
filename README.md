# Company Brain System

A practical operating system for companies that want AI agents to work with **shared memory, clear permissions, operational context and evidence**.

Built for founders, operators, consultants and teams who want agents to help run the business without turning the company into a pile of disconnected prompts, chats, docs and automations.

Works with Claude Code, OpenAI Codex, Cursor, Windsurf, Hermes and any agent that can read Markdown, follow playbooks and write structured outputs.

Company Brain System helps you design a **company brain**: a plain-text, Git-based operating layer where humans and AI agents can understand the company, act safely, leave evidence and improve over time.

It is based on AOS: **Agentic Operating System**.

---

## Start here

- **New to this?** Read [`docs/07_quick_start.md`](docs/07_quick_start.md).
- **Want an agent to install it with you?** Give it [`docs/14_agent_installation_process.md`](docs/14_agent_installation_process.md).
- **Want the full method?** Read [`docs/00_master_playbook.md`](docs/00_master_playbook.md).
- **Want to install it in a company?** Use [`templates/questionnaires/company-brain-intake.md`](templates/questionnaires/company-brain-intake.md).
- **Want an agent to operate it?** Use [`templates/agent-runtime-pack/README.md`](templates/agent-runtime-pack/README.md).
- **Blocked implementing it?** Read [`docs/12_get_help_from_libera.md`](docs/12_get_help_from_libera.md).

## Built by Libera

This repo is free and useful by itself.

If your team gets stuck applying it, Libera can help you install it inside a real company: diagnosis, Company Brain setup, agent roles, permissions, operating cadence and adoption.

- Implementation help: [Libera Company Brain Implementation](https://example.com/libera/company-brain)
- Academy: [Libera Academy](https://example.com/libera/academy)
- Community: [Libera Community](https://example.com/libera/community)
- Need help now? [`docs/12_get_help_from_libera.md`](docs/12_get_help_from_libera.md)
- Want to understand the offer? [`docs/13_libera_offer_map.md`](docs/13_libera_offer_map.md)
- Found a problem? Open an issue.
- Improved a template? Open a pull request.

---

## What problem does it solve?

Most AI-agent setups fail for simple reasons:

- no shared company context;
- no clear permissions;
- no memory of what changed;
- no evidence of what agents did;
- no way to improve the method from real work;
- no safe path from human-led work to supervised autonomy.

Company Brain System gives you the structure to fix that.

## What is inside?

- **Company Brain**: the central memory of the company.
- **Department Brains**: memory for sales, operations, product, finance, support, etc.
- **Agent Runtime Packs**: identity, permissions, tools, operating rules and evidence templates for each agent.
- **Operational memory**: StateChanges, Context Packets, Receipts and HandOffs.
- **Templates**: questionnaires, scorecards, agent packs, department packs, SOPs, reviews and examples.
- **Tools guide**: what categories of tools are needed and how to connect them safely.
- **Skills guide**: what capabilities agents need without exposing private/internal credits.
- **Schemas**: YAML contracts to keep records consistent.
- **Scripts**: validation and documentation build tools.
- **Safety method**: evaluation fixtures, permission checks and approval gates.

## Who is it for?

- Founders building AI-enabled companies.
- Operators trying to make AI useful beyond chat.
- Consultants implementing AI workflows for clients.
- Teams that need agents to work with context, not improvisation.
- Technical teams that want a lightweight method before building software.

## What it is not

- Not a SaaS.
- Not a chatbot.
- Not a magic prompt pack.
- Not a replacement for human judgement.
- Not a production database.

It is a **method + repo structure** you can copy, adapt and operate.

## Quick start

```bash
git clone https://github.com/aosoficial/company-brain-system.git
cd company-brain-system
pip install pyyaml
python scripts/validate_repo.py
python scripts/validate_schemas.py
```

Then read:

1. [`docs/07_quick_start.md`](docs/07_quick_start.md)
2. [`docs/14_agent_installation_process.md`](docs/14_agent_installation_process.md)
3. [`docs/00_master_playbook.md`](docs/00_master_playbook.md)
4. [`docs/15_tools.md`](docs/15_tools.md)
5. [`docs/16_skills.md`](docs/16_skills.md)
6. [`docs/17_human_sops.md`](docs/17_human_sops.md)
7. [`docs/18_agent_sops.md`](docs/18_agent_sops.md)
8. [`templates/questionnaires/company-brain-intake.md`](templates/questionnaires/company-brain-intake.md)
9. [`templates/agent-runtime-pack/README.md`](templates/agent-runtime-pack/README.md)

## Practical path

### 1. Map the company

Use the Company Brain intake:

- company purpose;
- departments;
- important people;
- active systems;
- decisions;
- metrics;
- risks;
- permissions.

### 2. Create the first Company Brain

Start with a minimal brain. Do not overbuild.

Use:

- [`templates/context-packets/context-packet-template.md`](templates/context-packets/context-packet-template.md)
- [`templates/department-brain-pack/`](templates/department-brain-pack/)
- [`templates/scorecards/company-brain-scorecard.md`](templates/scorecards/company-brain-scorecard.md)

### 3. Add one agent

Create one agent with:

- identity;
- role;
- allowed tools;
- forbidden actions;
- approval rules;
- memory rules;
- receipt rules.

Use:

- [`templates/agent-runtime-pack/`](templates/agent-runtime-pack/)

### 4. Make every action leave evidence

Agents should not just say “done”. They should leave a receipt:

- what they did;
- why;
- source used;
- files changed;
- risks;
- rollback path;
- verification result.

Use:

- [`templates/receipts/receipt-template.md`](templates/receipts/receipt-template.md)

### 5. Improve the method from real work

When something breaks, do not only fix the task. Improve the system.

Use:

- [`templates/method-improvements/method-improvement-proposal.md`](templates/method-improvements/method-improvement-proposal.md)
- [`docs/09_method_improvement_loop.md`](docs/09_method_improvement_loop.md)

## Repository map

```text
company-brain-system/
  docs/                         method manuals
  templates/                    reusable packs and templates
  schemas/                      YAML contracts
  registry/                     example registries
  examples/                     synthetic examples
  scripts/                      validation and build scripts
  method-improvements/          method learning log
  .github/workflows/            validation workflow
```

## Core concepts

- **Company Brain**: shared operational memory for the company.
- **Department Brain**: focused memory for one area.
- **Context Packet**: the context an agent needs before acting.
- **StateChange**: a record of what changed.
- **Receipt**: evidence that an action happened.
- **Agent Runtime Pack**: the operating contract for an agent.
- **Supervised autonomy**: agents can act inside clear limits; sensitive actions need approval.

## Safety rules

Default rule: agents may draft, analyse, prepare and operate locally.

They should not, without explicit human approval:

- contact clients or leads;
- publish externally;
- spend money;
- make legal or economic commitments;
- use sensitive/private data without scope;
- deploy to production;
- change live systems.

Read: [`docs/11_agent_safety_evaluation.md`](docs/11_agent_safety_evaluation.md)

## Get help from Libera

This repo is free and useful by itself.

If your company gets stuck implementing it, Libera can help with:

- diagnosis;
- Company Brain setup;
- agent runtime design;
- department brain design;
- safety and permission model;
- team adoption;
- operating cadence.

Read: [`docs/12_get_help_from_libera.md`](docs/12_get_help_from_libera.md)

## Contributing

Contributions are welcome:

- better templates;
- clearer examples;
- new department packs;
- safety fixtures;
- method improvements;
- translations;
- implementation stories.

Open an issue or pull request.

## License

MIT. See [`LICENSE`](LICENSE).

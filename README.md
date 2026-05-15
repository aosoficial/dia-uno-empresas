# Company Brain System

Turn your company context into safe AI-agent operations.

Company Brain System is a practical operating system for teams that want AI agents to work with shared context, clear permissions, evidence and human approval where it matters.

It helps you move from scattered prompts, chats and documents to a simple company brain that humans and agents can both use.

Based on AOS: Agentic Operating System.

---

## Start here

- **I want to understand it quickly:** read [`docs/07_quick_start.md`](docs/07_quick_start.md).
- **I want an agent to help me install it:** give the agent [`docs/14_agent_installation_process.md`](docs/14_agent_installation_process.md).
- **I want the full method:** read [`docs/00_master_playbook.md`](docs/00_master_playbook.md).
- **I want to map my company:** use [`templates/questionnaires/company-brain-intake.md`](templates/questionnaires/company-brain-intake.md).
- **I want to create an agent role:** use [`templates/agent-runtime-pack/README.md`](templates/agent-runtime-pack/README.md).
- **I am stuck:** read [`docs/12_get_help_from_libera.md`](docs/12_get_help_from_libera.md) or open a GitHub issue.

## Why this exists

Most AI-agent setups fail for simple reasons:

- agents do not know the company context;
- permissions are unclear;
- sensitive actions are not separated from safe actions;
- decisions and changes are not recorded;
- nobody can verify what an agent actually did;
- the method does not improve from real work.

Company Brain System gives you a structure for fixing that.

## What you get

- **Company Brain:** the shared memory of the company.
- **Department Brains:** focused memory for sales, operations, product, finance, support and other areas.
- **Agent Runtime Packs:** the operating files that define who an agent is, what it can do, what it cannot do and how it leaves evidence.
- **Operational records:** simple records for context, changes, handoffs and completed work.
- **Templates:** questionnaires, scorecards, agent packs, department packs, reviews and examples.
- **Safety method:** approval rules, permission checks and evaluation fixtures.
- **Validation scripts:** basic checks to keep the repo consistent.

## Who it is for

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

It is a method and repo structure you can copy, adapt and operate.

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

## The practical path

### 1. Map the company

Start with the basics:

- purpose;
- departments;
- important people and roles;
- active systems;
- key decisions;
- metrics;
- risks;
- permissions.

Use: [`templates/questionnaires/company-brain-intake.md`](templates/questionnaires/company-brain-intake.md)

### 2. Create the first Company Brain

Start small. Do not map the whole company on day one.

Use:

- [`templates/context-packets/context-packet-template.md`](templates/context-packets/context-packet-template.md)
- [`templates/department-brain-pack/`](templates/department-brain-pack/)
- [`templates/scorecards/company-brain-scorecard.md`](templates/scorecards/company-brain-scorecard.md)

### 3. Add one agent

Create one agent role with:

- identity;
- mission;
- allowed tools;
- forbidden actions;
- approval rules;
- memory rules;
- evidence rules.

Use: [`templates/agent-runtime-pack/`](templates/agent-runtime-pack/)

### 4. Make work verifiable

Agents should not just say “done”. They should leave evidence of:

- what they did;
- why they did it;
- which source they used;
- what changed;
- what risks remain;
- how the work was checked.

Use: [`templates/receipts/receipt-template.md`](templates/receipts/receipt-template.md)

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

## Core terms

- **Company Brain:** shared operational memory for the company.
- **Department Brain:** focused memory for one area.
- **Context Packet:** the context an agent needs before acting.
- **StateChange:** a record of what changed.
- **Receipt:** evidence that an action happened and how it was checked.
- **Agent Runtime Pack:** the operating contract for an agent.
- **Supervised autonomy:** agents can act inside clear limits; sensitive actions need approval.

More definitions: [`docs/08_glossary.md`](docs/08_glossary.md)

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

## Built by Libera

This repo is free and useful by itself.

If your team gets stuck applying it, Libera can help you install it inside a real company: diagnosis, Company Brain setup, agent roles, permissions, operating cadence and adoption.

For now, use GitHub issues:

- **Need implementation help?** Open an issue titled `Implementation help`.
- **Found a problem?** Open an issue titled `Bug` or `Question`.
- **Improved a template?** Open a pull request.

Read:

- [`docs/12_get_help_from_libera.md`](docs/12_get_help_from_libera.md)
- [`docs/13_libera_offer_map.md`](docs/13_libera_offer_map.md)

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

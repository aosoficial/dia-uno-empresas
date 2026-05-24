# ORGO-first company onboarding

Goal: install the first real DIA UNO company from ORGO without turning the first interaction into a broad consulting interrogation.

The client experience starts in **ORGO**. ORGO's first practical job is to help the user install or connect **Codex** or **Claude Code** as the technical installer operator. ORGO itself is not treated as the business consultant at this point.

## Core principle

Do not ask the company to explain every department at the beginning.

Install the operating base first:

1. ORGO.
2. Codex or Claude Code as installer operator.
3. DIA UNO framework.
4. Slack as the first human-agent interface.
5. Supabase + Voyage + GBrain as the private company memory.
6. First agent: CEO.
7. Department agents.
8. Company knowledge, built through agent-led interviews and evidence.

## Sequence

### 1. ORGO installs the installer operator

Inside ORGO, the user chooses one:

- Codex;
- Claude Code.

The selected assistant acts as installer/operator, not as an autonomous consultant.

It should:

- verify it can run locally;
- run the AI-level guardrail exam from `docs/00_non_technical_start_with_codex_or_claude.md`;
- avoid asking for business-sensitive information before the private brain exists;
- keep secrets out of chat and Git;
- ask before paid, public, external, legal, production or sensitive actions.

### 2. Codex/Claude installs or updates DIA UNO

The installer operator opens or clones the `dia-uno-empresas` framework and updates it before creating the company instance.

Client-facing language:

> We are loading the latest DIA UNO installation system.

Do not make the client reason about branches, commits or repo internals unless they are technical.

### 3. Create the private company instance

Create the private folder where the company will live.

This is not the public framework repo. It is the company's operating space.

It contains:

- company brain;
- approval boundaries;
- department folders;
- digital employees;
- context packets;
- receipts;
- statechanges;
- integrations;
- secrets instructions, never real secrets.

### 4. Connect Slack before deep discovery

Slack is connected early because the company needs a place to talk to agents.

Create only the minimum channels:

- `#00-direction` — CEO agent, priorities, decisions, escalations.
- `#90-approvals` — human approvals.
- `#99-receipts` — receipt notifications.

Add department channels later, when department agents exist.

Slack is only the interface. The Company Brain is the memory.

### 5. Install private memory infrastructure

Install/configure the company memory layer:

- Supabase/Postgres for stored operational memory;
- Voyage for embeddings/search;
- GBrain/Company Brain for pages, context, receipts, statechanges, links and operational state;
- runtime config and secrets outside Slack and outside Git.

Client-facing language:

> We are installing the private memory of your company.

Do not ask the user to paste API keys, passwords, Slack tokens or connection strings into chat.

### 6. Create the first agent: CEO

The first agent is **CEO**, not a generic all-area assistant.

CEO owns only **Dirección** at the beginning:

- vision;
- business model;
- current priorities;
- decision criteria;
- risk appetite;
- company-level constraints;
- approval boundaries;
- which department agents are needed first.

CEO must not run a deep interview about marketing, operations, product, growth, finance or post-sale. Those areas belong to department agents.

### 7. CEO interviews Dirección only

The first interview should be short and directional.

Allowed questions:

- What does the company sell?
- Who makes final decisions?
- What is the current main priority?
- What cannot AI do without approval?
- Which department feels most urgent?
- Which tools/sources may be read first?

Avoid asking for full department processes at this stage.

### 8. CEO proposes the first agent org chart

CEO proposes the first agent roster, for example:

- Operations;
- Marketing;
- Growth / Sales;
- Product / Service;
- Finance;
- Post-sale / Customer Success;
- Legal / Compliance if needed.

The human approves the roster before more agents are created.

### 9. Department agents interview their own areas

Each department agent asks only about its own scope.

Examples:

- Marketing agent interviews marketing.
- Operations agent interviews operations.
- Growth/Sales agent interviews sales/growth.
- Product/Service agent interviews offer and delivery quality.
- Finance agent interviews unit economics, billing and reporting.
- Post-sale agent interviews onboarding, support and retention.

Each interview creates context packets, open questions, risks, decisions and receipts in the Company Brain.

### 10. Observer agent connects the system

Create an **Observer** agent when the first CEO + department loop exists.

The Observer does not run the company and does not replace department owners.

It watches for:

- contradictions between agents;
- missing receipts;
- stale assumptions;
- decisions not reflected in memory;
- actions outside approval boundaries;
- repeated questions that should become memory;
- signals that should become StateChanges.

The Observer proposes memory updates and asks for approval when needed.

## Done when

The ORGO-first onboarding is ready for the first real company when:

- Codex or Claude Code is installed/connected from ORGO;
- DIA UNO is updated;
- a private company instance exists;
- Slack minimum channels exist;
- Supabase/Voyage/GBrain memory path is configured or explicitly pending;
- CEO agent exists and is limited to Dirección;
- no department deep-dive has been asked by CEO;
- the first department-agent plan is proposed for approval;
- Observer agent is defined as a cross-system memory observer;
- secrets remain outside chat and Git;
- first receipt/statechange rules are clear.

## Anti-patterns

Do not:

- ask the whole company diagnosis before Slack and memory exist;
- make CEO interview every department;
- store truth in Slack;
- create many agents before approval boundaries exist;
- ask for tokens/secrets in chat;
- call the company AI-first just because the scaffold exists;
- let Observer execute business actions directly.

# ORGO-first company onboarding

Goal: install the first real DIA UNO company from ORGO without turning the first interaction into a broad consulting interrogation.

The client experience starts in **ORGO**. ORGO's first practical job is to help the user install or connect **Codex** or **Claude Code** as the technical installer operator. ORGO itself is not treated as the business consultant at this point.

## Installer operator autopilot

When Codex or Claude Code opens this repo after ORGO, it must not wait for the user to provide internal repo instructions.

The installer operator should immediately:

1. Read root `AGENTS.md`.
2. Read `START_HERE.md`.
3. Read this file.
4. Read `docs/00_non_technical_start_with_codex_or_claude.md`.
5. Tell the user the next safe step in plain language.
6. Run the short AI-level guardrail exam before asking for business context.

The user should experience this as: **"DIA UNO is loaded; the installer is guiding me now."**

The user should not need to say: "read START_HERE", "pull the repo", "check the docs", or "tell me what to do next".

## Core principle

Do not ask the company to explain every department at the beginning.

Install the operating base first:

1. ORGO.
2. Codex or Claude Code as installer operator.
3. DIA UNO framework.
4. Private company instance.
5. Supabase + Voyage + public GBrain (`https://github.com/garrytan/gbrain`) as the private company memory.
6. Slack as the mandatory first human-agent interface.
7. Hermes profile/gateway connecting Slack to the agent runtime.
8. Base tools/integrations needed for the first operating loop.
9. First agent: CEO.
10. Observer agent.
11. Department agents.
12. Company knowledge, built through agent-led interviews and evidence.

## Sequence

### 1. ORGO installs the installer operator

Inside ORGO, the user chooses one:

- Codex;
- Claude Code.

The selected assistant acts as installer/operator, not as an autonomous consultant.

It should:

- verify it can run locally;
- take initiative after clone/open by following root `AGENTS.md`;
- run the AI-level guardrail exam from `docs/00_non_technical_start_with_codex_or_claude.md`;
- avoid asking for business-sensitive information before the private brain exists;
- keep secrets out of chat and Git;
- ask before paid, public, external, legal, production or sensitive actions.

### 2. Codex/Claude installs or updates DIA UNO

The installer operator opens or clones the `dia-uno-empresas` framework and updates it before creating the company instance.

Client-facing language:

> We are loading the latest DIA UNO installation system.

Do not make the client reason about branches, commits or repo internals unless they are technical.

### 3. Create the private company instance before agents talk

Create the private folder where the company will live before Slack is used for a real CEO conversation.

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

### 4. Install private memory infrastructure before Slack CEO launch

Install/configure the company memory layer:

- Supabase/Postgres for stored operational memory;
- Voyage for embeddings/search;
- public GBrain (`https://github.com/garrytan/gbrain`) / Company Brain for pages, context, receipts, statechanges, links and operational state;
- runtime config and secrets outside Slack and outside Git.

Verify it before the first CEO conversation:

```bash
python scripts/check_private_memory_readiness.py \
  --company-instance /private/path/to/company-brain \
  --strict
```

Client-facing language:

> We are installing the private memory of your company before activating the CEO. Slack is only the interface; GBrain/Supabase/Voyage are where operational memory lives.

Do not ask the user to paste API keys, passwords, Slack tokens or connection strings into chat.

If memory is not ready, stop before launching CEO and record the blocker with owner, reason, approval needed and expected outcome. Do not compensate by treating Slack chat as memory.

### 5. Prepare Slack before creating agents or deep discovery

Slack is connected early because the company needs a place to talk to agents. For a real company install, Slack is mandatory before the first agent is launched.

For a real company install, the installer operator must explicitly tell the user that Slack is a required Sprint 0 dependency, not an optional route. Creating/configuring Slack is external and requires approval before action.

Create only the minimum channels:

- `#00-direction` — CEO agent, priorities, decisions, escalations.
- `#90-approvals` — human approvals.
- `#99-receipts` — receipt notifications.

Add department channels later, when department agents exist.

Slack is only the interface. Hermes is the runtime bridge. The Company Brain is the memory. Default path is direct Slack -> Hermes via Socket Mode; Composio is not the default Slack runtime and may only be used later as an approved app-integration layer.

After the Slack app exists, the installer operator must run `scripts/connect_slack_to_hermes.py` so the repo creates/uses the Hermes profile, writes the local Slack env block outside Git, restarts the Hermes gateway and records a private receipt:

```bash
python scripts/connect_slack_to_hermes.py \
  --company-instance /private/path/to/company-brain \
  --profile acme-ceo \
  --install-hermes \
  --start-gateway \
  --apply
```

If Slack cannot be configured and connected to Hermes yet, stop before launching the first agent. Record Slack/Hermes as a blocking dependency with owner, reason, approval needed and expected outcome. Do not proceed as if the human-agent interface exists.

### 6. Prepare base tools after memory and Slack are planned

Identify the minimum base tools/integrations needed for the first safe operating loop. Do not ask for secrets in chat and do not connect production systems without approval.

At minimum, classify each tool as:

- ready;
- pending approval;
- pending credentials stored outside Git/chat;
- not needed for Sprint 0.

### 7. Create the first agent: CEO

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

### 8. CEO interviews Dirección only

The first interview should be short and directional.

Allowed questions:

- What does the company sell?
- Who makes final decisions?
- What is the current main priority?
- What cannot AI do without approval?
- Which department feels most urgent?
- Which tools/sources may be read first?

Avoid asking for full department processes at this stage.

### 9. Create the Observer agent as read-only guard

Create an **Observer** agent after CEO/Dirección exists and before department agents are opened.

The Observer does not run the company, does not interview departments and does not replace department owners. Its first job is to watch the Slack ↔ agents ↔ Company Brain loop for evidence quality and memory coherence.

It watches for:

- contradictions between channels, agents or memory;
- missing receipts;
- stale assumptions;
- decisions not reflected in memory;
- actions outside approval boundaries;
- repeated questions that should become memory;
- signals that should become StateChanges.

The Observer proposes memory updates and asks for approval when needed. It must not connect tools, change permissions or execute business actions directly.

### 10. CEO proposes the first department-agent org chart

CEO proposes the first agent roster, for example:

- Operations;
- Marketing;
- Growth / Sales;
- Product / Service;
- Finance;
- Post-sale / Customer Success;
- Legal / Compliance if needed.

The human approves the roster before more agents are created.

### 11. Department agents interview their own areas

Each department agent asks only about its own scope.

Examples:

- Marketing agent interviews marketing.
- Operations agent interviews operations.
- Growth/Sales agent interviews sales/growth.
- Product/Service agent interviews offer and delivery quality.
- Finance agent interviews unit economics, billing and reporting.
- Post-sale agent interviews onboarding, support and retention.

Each interview creates context packets, open questions, risks, decisions and receipts in the Company Brain.

## Done when

The ORGO-first onboarding is ready for the first real company when:

- Codex or Claude Code is installed/connected from ORGO;
- DIA UNO is updated;
- a private company instance exists;
- Supabase/Voyage/GBrain memory path is configured and passes `scripts/check_private_memory_readiness.py --strict`, or it is explicitly recorded as a launch blocker;
- Slack minimum channels exist;
- Slack app exists and is connected directly to a Hermes profile/gateway;
- CEO agent exists and is limited to Dirección;
- Observer agent exists or is explicitly marked pending as a read-only memory/evidence guard;
- no department deep-dive has been asked by CEO;
- the first department-agent plan is proposed for approval;
- secrets remain outside chat and Git;
- first receipt/statechange rules are clear.

## Anti-patterns

Do not:

- ask the whole company diagnosis before Slack and memory exist;
- offer Slack as optional or launch the first agent without a working Slack surface;
- make CEO interview every department;
- store truth in Slack;
- create many agents before approval boundaries exist;
- ask for tokens/secrets in chat;
- call the company AI-first just because the scaffold exists;
- let Observer execute business actions directly.

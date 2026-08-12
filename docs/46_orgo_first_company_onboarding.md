# People-first to ORGO hybrid onboarding

Goal: continue one organized capability from the People layer into a governed hybrid pilot without turning the first interaction into a broad consulting interrogation.

The company starts in the `people` layer. **ORGO** enters only when a capability has a named human accountable, followed SOP, current sources, measurable output, authority boundaries and fallback. ORGO then helps install or connect **Codex** or **Claude Code** as the technical installer operator. ORGO itself is not treated as the business consultant.

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

Install the operating base in this order:

1. Private `people` instance.
2. Rumbo, accountable seats, decisions, processes, SOPs, metrics and cadence.
3. Agentization gate for one mature capability.
4. Upgrade the private instance to `hybrid` without overwriting People work.
5. ORGO plus Codex or Claude Code as installer operator.
6. Supabase + Voyage + public GBrain (`https://github.com/garrytan/gbrain`) as private company memory.
7. Slack as the mandatory first human-agent interface in the current guided path.
8. Hermes profile/gateway connecting Slack to the agent runtime.
9. Minimum tools for the bounded loop.
10. First capability agent in `draft` or `pilot`.
11. Observer agent when needed.
12. Other capabilities only after their own People and agentization gates.

## Sequence

### 0. Organize one capability before ORGO

Create and validate the People instance first:

```bash
python scripts/company_brain_wizard.py \
  --company "Acme Demo" \
  --company-type agency \
  --method-mode people \
  --output /private/path/to/company-brain \
  --yes
python scripts/validate_people_readiness.py /private/path/to/company-brain
```

The structural validator is necessary but not sufficient. Review that the chosen capability has a human accountable, followed SOP, current sources, measurable output, authority boundaries, evidence and fallback. If it does not, remain in People mode.

Then add only inert hybrid scaffolds:

```bash
python scripts/company_brain_wizard.py \
  --company "Acme Demo" \
  --company-type agency \
  --method-mode hybrid \
  --output /private/path/to/company-brain \
  --upgrade --yes
```

This does not activate anything.

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

### 3. Verify the private company instance before agents talk

Verify the private folder and its People work before Slack is used for a real agent conversation.

This is not the public framework repo. It is the company's operating space.

In hybrid mode it contains:

- company brain;
- approval boundaries;
- department folders;
- digital employees;
- context packets;
- receipts;
- statechanges;
- integrations;
- secrets instructions, never real secrets.

### 4. Install private memory infrastructure before the capability-agent launch

Install/configure the company memory layer:

- Supabase/Postgres for stored operational memory;
- Voyage for embeddings/search;
- public GBrain (`https://github.com/garrytan/gbrain`) / Company Brain for pages, context, receipts, statechanges, links and operational state;
- runtime config and secrets outside Slack and outside Git.

Verify it before the first capability-agent conversation:

```bash
python scripts/check_private_memory_readiness.py \
  --company-instance /private/path/to/company-brain \
  --strict
```

Client-facing language:

> We are installing the private memory of your company before activating the first capability agent. Slack is only the interface; GBrain/Supabase/Voyage are where operational memory lives.

Do not ask the user to paste API keys, passwords, Slack tokens or connection strings into chat.

If memory is not ready, stop before launching the capability agent and record the blocker with owner, reason, approval needed and expected outcome. Do not compensate by treating Slack chat as memory.

### 5. Prepare Slack before creating agents or deep discovery

Slack is connected early because the company needs a place to talk to agents. For a real company install, Slack is mandatory before the first agent is launched.

For a real company install, the installer operator must explicitly tell the user that Slack is a required Sprint 0 dependency, not an optional route. Creating/configuring Slack is external and requires approval before action.

Create only the minimum channels:

- `#00-direction` — Direction capability agent when that is the selected first scope; priorities, decisions and escalations.
- `#90-approvals` — human approvals.
- `#99-receipts` — receipt notifications.

Add department channels later, when department agents exist.

Slack is only the interface. Hermes is the runtime bridge. The Company Brain is the memory. Default path is direct Slack -> Hermes via Socket Mode. Do not add an external integration layer in the base company setup.

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

### 7. Create the first capability agent

The first agent implements one mature capability and starts in `draft` or `pilot`. The existing CEO pack is a compatible default for a Direction capability, not a requirement to invent a CEO before the organization is ready.

If the chosen capability belongs to **Dirección**, its bounded scope may include:

- vision;
- business model;
- current priorities;
- decision criteria;
- risk appetite;
- company-level constraints;
- approval boundaries;
- which capability-agent seats may be useful later.

The agent must not run a deep interview outside its approved capability. Other areas remain People-owned until their own gates pass.

### 8. The capability agent interviews only its approved scope

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

Create an **Observer** agent after the first governed capability exists and before broader agent rollout.

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

### 10. The responsible human proposes the next capability-agent seats

The responsible human may propose later agent seats, for example:

- Operations;
- Marketing;
- Growth / Sales;
- Product / Service;
- Finance;
- Post-sale / Customer Success;
- Legal / Compliance if needed.

Each capability must pass its own gate before more agents are created.

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
- one capability agent exists in `draft` or `pilot` and is limited to its approved scope;
- Observer agent exists or is explicitly marked pending as a read-only memory/evidence guard;
- no agent has performed a deep-dive outside its approved capability;
- any next capability-agent proposal remains subject to its own People and agentization gates;
- secrets remain outside chat and Git;
- first receipt/statechange rules are clear.

## Anti-patterns

Do not:

- ask for broad agent-led diagnosis before People organization, Slack and memory exist;
- offer Slack as optional or launch the first agent without a working Slack surface;
- make one agent interview every department;
- store truth in Slack;
- create many agents before approval boundaries exist;
- ask for tokens/secrets in chat;
- call the company AI-first just because the scaffold exists;
- let Observer execute business actions directly.

# Non-technical start: use Codex or Claude Code as installer operator

Use this first if you are not sure how technical you are, or if you want an AI assistant to help you install your private Company Brain instance.

In the ORGO-first flow, the user starts in **ORGO** and installs or connects **Codex** or **Claude Code** first. That assistant becomes the installer operator for DIA UNO. See `docs/46_orgo_first_company_onboarding.md` for the full real-company sequence.

The assistant's first job is not to collect your life story. Before the brain is installed, it should run only an **examen inicial de nivel de IA**: enough to know how much freedom and how many guardrails you need.

## If you are the assistant, guide without being prompted

When this repo is opened after an ORGO clone/open action, do not wait for the user to tell you to read files or choose commands.

Immediately read:

1. `AGENTS.md`;
2. `START_HERE.md`;
3. `docs/46_orgo_first_company_onboarding.md`;
4. this file.

Then say the next safe step in human language, run the short AI-level exam, and only ask for approvals when the next action crosses a boundary.

## Step 0 — Copy this prompt into Codex or Claude Code

```text
I want to create a private Company Brain instance for my business using this repo:
https://github.com/aosoficial/dia-uno-empresas

Act as my installer operator.
If you have just cloned or opened the repo, immediately read AGENTS.md, START_HERE.md, docs/46_orgo_first_company_onboarding.md and this file. Do not wait for me to tell you which file to read. Guide me from here in plain language.
Start with a short AI-level exam only. Do not investigate my personal life, customers, money, health, private documents or sensitive systems yet.
Classify me into one of three guardrail modes:
- Mode 1 — non-technical: strong guardrails, tell me exactly what to do and what not to do.
- Mode 2 — intermediate AI user: explain tradeoffs, let me choose between safe options, but stop before external or sensitive actions.
- Mode 3 — technical / builder: feel free to give me more direct commands and autonomy, but still ask before external/public/economic/legal/production/sensitive actions.

After the mode is selected:
1. Help me install/connect Codex or Claude Code from ORGO if it is not working yet.
2. Help me clone, open or update the DIA UNO repo.
3. Explain that tools/accounts should use free plans or free tier first when available.
4. Ask me to create required accounts only when needed.
5. Never ask me to paste real API keys, passwords or tokens into chat. Tell me where to store them locally instead.
6. Help me prepare Slack as the mandatory first human-agent interface. Do not launch the first agent until I can talk to it through Slack.
7. If useful, use Composio as the integration/auth layer for Slack and other apps, but do not treat Composio as memory or source of truth.
8. Create the private Company Brain instance outside the public repo after Slack is approved/created/configured.
9. Help me configure the private memory path: Supabase/Postgres, Voyage and GBrain/Company Brain, or mark it explicitly pending if not connected yet.
10. Keep all internal files inside the generated private folder hierarchy. Do not create random folders elsewhere unless I explicitly approve.
11. Create or guide the first digital employee SOUL.md: CEO Agent, limited to Dirección.
12. Do not ask CEO to interview marketing, operations, product, growth, finance or post-sale. Those interviews belong to department agents later.
13. Define the Observer agent as a memory/system observer, not as a business executor.
14. Stop after the first safe internal operating loop with Context Packet, human review, Receipt and scorecard.

If a command is destructive, paid, public, external, legal, production-related or sensitive, ask me before doing it.
```

You can use **Codex**, **Claude Code**, or another coding assistant. The repo is the source of truth; the assistant is only the installer operator.

## The AI-level exam

Ask only these questions at the start:

1. Have you used a terminal before?
   - A: never / almost never
   - B: sometimes, by copy-pasting commands
   - C: often, I understand what commands do
2. Have you used AI coding tools like Codex, Claude Code, Cursor or GitHub Copilot?
   - A: no
   - B: yes, but mostly by asking for help
   - C: yes, I can review and change code
3. Do you understand folders, Git repositories and where files are created?
   - A: not really
   - B: a bit
   - C: yes
4. Do you know what API keys, environment variables and secrets are?
   - A: no
   - B: vaguely
   - C: yes
5. When something fails, what do you prefer?
   - A: exact next step, no alternatives
   - B: two or three safe options
   - C: diagnostics and commands

Do not ask about personal biography, customers, revenue, private systems or business secrets yet. In short: **no investigar a la persona** beyond the AI-level exam. That comes later, after the private brain exists and the user understands where sensitive information belongs.

Only after the mode is chosen, **pedir cuentas y claves solo después** when the next step truly needs an account or local secret location.

## Guardrail modes

### Modo 1 — No técnico

Use this when the user chooses mostly A.

Behavior:

- Use **guardrails fuertes**.
- Give one step at a time.
- Explain what each command does in plain language.
- Prefer dry-runs before writes.
- Tell the user exactly what not to do.
- Do not ask them to choose paths freely unless you give one safe default.
- Stop before account creation, payments, API keys, external publishing, email/CRM/client data or production systems.
- Repeat: **no pegues claves en el chat**.

Recommended style:

```text
Do this now: ...
Do not do this yet: ...
When it finishes, send me the result of: ...
```

### Modo 2 — Usuario IA intermedio

Use this when the user chooses mostly B.

Behavior:

- Offer up to three safe options.
- Explain tradeoffs briefly.
- Let the user choose tools and folders inside the allowed private hierarchy.
- Allow local commands and generated files.
- Still ask before external/public/economic/legal/production/sensitive actions.
- Secrets stay out of chat and out of Git.

### Modo 3 — Técnico / builder

Use this when the user chooses mostly C.

Behavior:

- Feel free to provide direct commands, scripts and validation steps.
- Let the user inspect, customize and extend.
- Allow more autonomy inside the repo and generated private instance.
- Still keep hard boundaries for secrets, real customer data, paid tools, public posting, production and legal/economic actions.

## Account and tool setup order

Only after the AI-level mode is selected, the assistant may ask the user to create accounts.

Rules:

- Say when something is **gratis o free tier** first.
- If a paid plan is required, stop and ask before continuing.
- Ask for accounts only when the next step needs them.
- Do not request real secrets in chat.
- For API keys/tokens/passwords, instruct the user to store them in local `.env` or the generated instance `secrets/` folder according to the repo templates.
- Never commit `.env`, tokens, passwords or connection strings.

Suggested order for ORGO-first onboarding:

1. ORGO installed by the user.
2. Codex or Claude Code desktop/terminal connected from ORGO as installer operator.
3. GitHub account or repo access, if needed to clone/open/update DIA UNO.
4. Local runtime requirements from this repo.
5. Slack workspace/app setup for the first interface. For real installs, Slack is mandatory before launching the first agent; Composio may be used as the integration/auth layer.
6. Supabase/Postgres, Voyage and GBrain/Company Brain for private memory, using free/free-tier first when possible.
7. Optional integrations only after the private brain and approval rules exist.

## Folder hierarchy rule

The generated private instance is the operating boundary. Keep work inside it.

A normal private instance should look like this:

```text
my-company-brain/
  README.md
  MAP.md
  FIRST_OPERATING_LOOP.md
  company/
  departments/
  digital-employees/
  context-packets/
  receipts/
  statechanges/
  scorecards/
  decisions/
  secrets/
```

Rules:

- Maintain a clear **jerarquía de carpetas**.
- Do **not** create random folders outside the generated instance: **no salir de la carpeta privada** unless the user explicitly asks and approves the new location.
- Do **not** write secrets into the public repo.
- Do **not** move operational artifacts into unrelated desktop/download folders.
- Do **not** exit the private instance boundary unless the user explicitly asks and approves the new location.
- If the assistant needs a new folder, it must explain why and where it belongs.

This protects the user's future Company Brain from becoming scattered again.

## First real goal

The first goal is not a full company transformation.

The first goal is:

1. Prepare Slack as the mandatory conversation surface for the first agent.
2. Create the private instance.
3. Verify the scaffold.
4. Create the first digital employee: `CEO` agent for Dirección only.
5. Review its `SOUL.md`.
6. CEO interviews Dirección only and proposes the first department-agent roster.
7. Create one safe Context Packet.
8. Run one internal action only.
9. Human reviews the result.
10. Save an Operational Receipt.
11. Update the scorecard.

After that, the operational validator can be run. Until then, examples are examples; they are not Point B evidence.

## What the assistant must not do at the beginning

- Do not scrape personal information.
- Do not ask for customer names, contracts or private files.
- Do not request API keys in chat.
- Do not connect Gmail, CRM, payment processors, production databases or social media.
- Do not ask CEO to do deep discovery for marketing, operations, product, growth, finance or post-sale.
- Do not create department agents before CEO has proposed the roster and the human has approved it.
- Do not let the Observer agent execute business actions directly; it observes, connects memory and flags gaps.
- Do not publish websites, posts or public claims.
- Do not claim the company is AI-first or at Point B just because files exist.
- Do not bypass the generated private folder hierarchy.

## Done when

This bootstrap is done when there is:

- selected AI-level mode;
- Slack working as the first-agent conversation surface;
- private instance outside the public repo;
- verified scaffold;
- first CEO agent `SOUL.md` reviewed;
- CEO scope limited to Dirección;
- department-agent interviews deferred to department agents;
- Observer agent defined as a memory/system observer;
- folder boundary understood;
- no secrets in chat or Git;
- next step is the first internal operating loop.

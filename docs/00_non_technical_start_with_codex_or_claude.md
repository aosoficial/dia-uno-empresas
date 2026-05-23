# Non-technical start: use Codex or Claude Code as installer operator

Use this first if you are not sure how technical you are, or if you want an AI assistant to help you install your private Company Brain instance.

The assistant's first job is not to collect your life story. Before the brain is installed, it should run only an **examen inicial de nivel de IA**: enough to know how much freedom and how many guardrails you need.

## Step 0 — Copy this prompt into Codex or Claude Code

```text
I want to create a private Company Brain instance for my business using this repo:
https://github.com/aosoficial/company-brain-system

Act as my installer operator.
Start with a short AI-level exam only. Do not investigate my personal life, customers, money, health, private documents or sensitive systems yet.
Classify me into one of three guardrail modes:
- Mode 1 — non-technical: strong guardrails, tell me exactly what to do and what not to do.
- Mode 2 — intermediate AI user: explain tradeoffs, let me choose between safe options, but stop before external or sensitive actions.
- Mode 3 — technical / builder: feel free to give me more direct commands and autonomy, but still ask before external/public/economic/legal/production/sensitive actions.

After the mode is selected:
1. Help me clone or open the repo.
2. Explain that tools/accounts should use free plans or free tier first when available.
3. Ask me to create required accounts only when needed.
4. Never ask me to paste real API keys, passwords or tokens into chat. Tell me where to store them locally instead.
5. Create the private Company Brain instance outside the public repo.
6. Keep all internal files inside the generated private folder hierarchy. Do not create random folders elsewhere unless I explicitly approve.
7. Create or guide the first digital employee SOUL.md, starting with CEO/Operations Assistant.
8. Stop after the first safe internal operating loop with Context Packet, human review, Receipt and scorecard.

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

Suggested order:

1. GitHub account or repo access, if needed to clone/fork.
2. Codex or Claude Code desktop/terminal, if the user wants an installer operator.
3. Local runtime requirements from this repo.
4. Optional integrations only after the private brain and approval rules exist.

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

1. Create the private instance.
2. Verify the scaffold.
3. Create the first digital employee: `CEO/Operations Assistant`.
4. Review its `SOUL.md`.
5. Create one safe Context Packet.
6. Run one internal action only.
7. Human reviews the result.
8. Save an Operational Receipt.
9. Update the scorecard.

After that, the operational validator can be run. Until then, examples are examples; they are not Point B evidence.

## What the assistant must not do at the beginning

- Do not scrape personal information.
- Do not ask for customer names, contracts or private files.
- Do not request API keys in chat.
- Do not connect Gmail, CRM, payment processors, production databases or social media.
- Do not publish websites, posts or public claims.
- Do not claim the company is AI-first or at Point B just because files exist.
- Do not bypass the generated private folder hierarchy.

## Done when

This bootstrap is done when there is:

- selected AI-level mode;
- private instance outside the public repo;
- verified scaffold;
- first digital employee `SOUL.md` reviewed;
- folder boundary understood;
- no secrets in chat or Git;
- next step is the first internal operating loop.

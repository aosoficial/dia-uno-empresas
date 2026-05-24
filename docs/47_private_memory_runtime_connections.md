# Private memory runtime: Supabase + Voyage + GBrain

This is the DIA UNO client-safe runtime pattern, without customer secrets in the public repo.

## Purpose

Before Slack or the CEO agent start real work, the private company instance must have an operational memory substrate:

- **Supabase/Postgres** stores operational memory and structured state.
- **Voyage** creates embeddings for semantic search.
- **GBrain** is the operational memory interface: pages, chunks, links, timeline, receipts, context packets, health checks and agent access.
- **Hermes** is the runtime bridge that agents use from Slack.

Slack is the conversation surface. It is not memory.

## GBrain target

Use this for DIA UNO public/client installs:

```text
GBRAIN_REPO_URL=https://github.com/garrytan/gbrain
```

## Private env contract

Store this in a private `.env` or secrets manager outside the public repo. Do not paste real values into Slack, Git, docs, receipts or chat.

```text
# Supabase/Postgres
SUPABASE_URL=
SUPABASE_PROJECT_REF=
SUPABASE_SERVICE_ROLE_KEY=
DATABASE_URL=
SUPABASE_SCHEMA=gbrain

# Voyage embeddings
VOYAGE_API_KEY=
VOYAGE_MODEL=voyage-3-large

# GBrain public upstream
GBRAIN_REPO_URL=https://github.com/garrytan/gbrain
GBRAIN_INSTALL_DIR=
GBRAIN_COMMAND=gbrain
GBRAIN_MCP_SERVER=
GBRAIN_MCP_NAME=
GBRAIN_PROJECT_ID=
GBRAIN_NAMESPACE=
GBRAIN_COMPANY_ID=

# Hermes/Slack runtime
HERMES_PROFILE=
SLACK_BOT_TOKEN=
SLACK_APP_TOKEN=
SLACK_HOME_CHANNEL=
SLACK_ALLOWED_USERS=
SLACK_ALLOWED_CHANNELS=
```

Minimum readiness requires:

- `SUPABASE_URL` set;
- `VOYAGE_API_KEY` set;
- `GBRAIN_REPO_URL=https://github.com/garrytan/gbrain`;
- at least one verified GBrain access path: `GBRAIN_COMMAND`, `GBRAIN_MCP_SERVER`, `GBRAIN_MCP_NAME` or `GBRAIN_PROJECT_ID`;
- private company instance folders for `company/`, `context-packets/`, `statechanges/` and `receipts/`.

## Process

### Step 1 — private memory credentials

Allowed:

1. Create or select the private Supabase project.
2. Store Supabase URL/project ref/service role/database URL in private env only.
3. Store Voyage key in private env only.
4. Store GBrain repo/install/access variables in private env only.
5. Run read-only preflight:

```bash
python scripts/check_private_memory_readiness.py \
  --company-instance /private/path/to/company-instance \
  --env-file /private/path/to/.env \
  --strict
```

### Step 2 — install/verify public GBrain

Allowed:

1. Clone or update GBrain in the private runtime:

```bash
git clone https://github.com/garrytan/gbrain /private/runtime/path/gbrain
```

2. Verify the target:

```bash
git -C /private/runtime/path/gbrain remote -v
git -C /private/runtime/path/gbrain status --short --branch
```

3. Read upstream GBrain install docs from that checkout before choosing commands.
4. Verify the available GBrain access path without printing secrets:

```bash
gbrain --version || true
gbrain health || true
gbrain stats || true
```

If the install uses MCP instead of CLI, verify the configured MCP server/profile and record the server name, not any secret.

### Step 3 — schema/migrations

- apply reviewed SQL/migrations;
- create or verify the GBrain schema/tables/extensions required by upstream GBrain;
- configure pgvector/embedding storage if upstream GBrain requires it;
- create minimal roles/policies needed for the runtime.

### Step 4 — memory test

1. Write one test Context Packet.
2. Write one test StateChange.
3. Write one test Receipt.
4. Trigger or verify embedding creation through Voyage.
5. Query/search the synthetic record through GBrain.
6. Verify health/stats.
7. Delete or clearly mark the test data if required.

Expected proof:

- preflight result;
- GBrain target verification;
- migration receipt if schema changes happened;
- read/write/search receipt if the memory test happened;
- no secrets in logs or receipts.

## Runtime flow

After readiness passes:

```text
Slack message
  -> Hermes Slack gateway/profile
  -> CEO agent ONE
  -> GBrain access path
  -> Supabase/Postgres stored memory
  -> Voyage embeddings for semantic search
  -> Receipt/StateChange/Context Packet evidence
```

The CEO answers in Slack after memory readiness is marked ready or pending in the company receipt.

## Verification commands

From the public repo:

```bash
python scripts/check_private_memory_readiness.py \
  --company-instance /private/path/to/company-instance \
  --env-file /private/path/to/.env \
  --strict

python scripts/connect_slack_to_hermes.py \
  --company-instance /private/path/to/company-instance \
  --profile company-ceo
```

The Slack/Hermes connector is dry-run by default. Use `--apply` only after the private memory gate passes and the human approves wiring.

## Receipt requirements

Every memory setup action must record:

- what changed;
- why;
- source/provenance;
- owner;
- freshness;
- allowed actions;
- forbidden actions;
- required approvals;
- expected outcome;
- evidence path;
- rollback/repair path.

# GBrain / MCP memory backend

## Canonical target for DIA UNO public/client installs

For DIA UNO public/client installs, **GBrain means the public upstream project**:

```text
https://github.com/garrytan/gbrain
```

If GBrain is missing, the installer should install or verify `garrytan/gbrain`, then run the memory readiness check as part of the normal setup.

## Use when

Use when agents need memory through tools, graph links, current operational state, receipts, context packets and statechanges. This profile is for active agent runtimes, not static documentation.

## Install/verify public GBrain

1. Inspect local tooling without printing secrets:
   ```bash
   command -v git
   command -v python3 || command -v python
   command -v node || true
   command -v npm || true
   command -v npx || true
   ```
2. Clone or update the public GBrain repo into a private runtime path, not into the public DIA UNO framework repo:
   ```bash
   git clone https://github.com/garrytan/gbrain /private/runtime/path/gbrain
   ```
   If it already exists, verify the remote:
   ```bash
   git -C /private/runtime/path/gbrain remote -v
   git -C /private/runtime/path/gbrain status --short --branch
   ```
3. Read upstream install docs from that repo before choosing install commands.
4. Configure only env names/placeholders in private env/secrets. Do not paste or print real Supabase, Voyage, Slack or database secrets.
5. Verify the installed command/API/MCP health according to upstream docs.
6. Write a private receipt with source, target path, commands run, result, remaining blocker, and rollback.

## Minimum private env contract

Use private env/secrets, never Git:

```text
GBRAIN_REPO_URL=https://github.com/garrytan/gbrain
GBRAIN_INSTALL_DIR=/private/runtime/path/gbrain
GBRAIN_COMMAND=gbrain
GBRAIN_MCP_SERVER=
GBRAIN_MCP_NAME=
GBRAIN_PROJECT_ID=
GBRAIN_NAMESPACE=
GBRAIN_COMPANY_ID=
```

At least one executable access path must be verified: `GBRAIN_COMMAND`, `GBRAIN_MCP_SERVER`, or an approved API endpoint from the upstream repo docs.

## Setup

1. Create the private company instance outside the public framework repo.
2. Install/verify `https://github.com/garrytan/gbrain` in the private runtime.
3. Configure Supabase/Postgres, Voyage and GBrain env/secrets outside Git.
4. Create namespaces for projects, receipts, statechanges and context packets.
5. Define who can write durable memory.
6. Verify health, orphan count, embeddings and backlinks after writes.
7. Keep secrets outside the memory graph.

## Allowed data

- StateChange records.
- Context packets.
- Receipts.
- Project status with owner/freshness.
- Approved operational facts.

## Forbidden data

- Tokens, keys, credentials or connection strings.
- Raw private chats unless explicitly approved.
- Cross-company memory mixing.
- Speculative facts without provenance.

## Receipts

Every import, migration or automated write must include provenance, current freshness, owner, validation evidence and rollback/repair path.

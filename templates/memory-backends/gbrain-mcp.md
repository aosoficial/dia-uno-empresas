# GBrain / MCP memory backend

## Use when

Use when agents need memory through tools, graph links, current operational state, receipts, context packets and statechanges. This profile is for active agent runtimes, not static documentation.

## Setup

1. Configure the MCP or GBrain tool in the private runtime.
2. Create namespaces for projects, receipts, statechanges and context packets.
3. Define who can write durable memory.
4. Verify health, orphan count, embeddings and backlinks after writes.
5. Keep secrets outside the memory graph.

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

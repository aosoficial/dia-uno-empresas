# Trace Policy

Owner: `...`
Company instance: `...`
Retention tier: `0 / 1 / 2 / 3`

## Purpose

Define what raw execution traces may be stored and how they are referenced from receipts.

## Store as Company Brain memory

- context packets;
- statechanges;
- decisions;
- receipts;
- stable operating principles.

## Store as raw traces

- logs;
- tool outputs;
- model metadata;
- debugging artifacts;
- hashes or references to larger files.

## Redaction required

Remove secrets, credentials, customer data, private personal data and connection strings before sharing or committing anything.

## Retention

- Default: receipt only.
- Debugging: keep raw trace locally for a short period.
- Sensitive: require approval and restricted access.

## Reference pattern

Receipt evidence should point to a trace path, hash or ID rather than copying raw traces into curated memory.

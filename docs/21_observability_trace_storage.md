# Observability and trace storage

Company Brain and trace storage are not the same thing.

## Company Brain

The Company Brain stores curated operational memory:

- context packets;
- statechanges;
- decisions;
- receipts;
- approvals;
- current operating principles;
- stable facts with provenance and freshness.

It should be readable, compact and useful for humans and agents.

## Trace store

The trace store stores raw technical evidence for debugging:

- tool calls;
- command output;
- logs;
- intermediate drafts;
- model/provider metadata;
- hashes or references to large artifacts.

Raw traces can be noisy and sensitive. Do not dump them into Company Brain.

## Retention tiers

- Tier 0: no raw trace retained, only receipt.
- Tier 1: short raw trace retained locally for debugging.
- Tier 2: raw trace retained with redaction and owner review.
- Tier 3: regulated/sensitive trace; human approval and strict access required.

## Receipt rule

Every important action should leave a lightweight receipt:

- what changed;
- why;
- source/provenance;
- owner;
- current freshness;
- allowed and forbidden next actions;
- required approvals;
- evidence path or hash;
- risks left.

## Redaction rule

Before storing or sharing traces, redact:

- API keys;
- tokens;
- passwords;
- private customer data;
- credentials;
- connection strings;
- personal data outside scope.

## Future-friendly pattern

Use receipts for permanent memory and store heavy traces separately. Reference heavy traces by path, hash or ID instead of copying them into the Company Brain.

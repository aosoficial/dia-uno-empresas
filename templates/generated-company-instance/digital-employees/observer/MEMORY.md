# Memory

Observer reads and proposes updates to:

- `context-packets/`
- `receipts/`
- `statechanges/`
- `handoffs/`
- `company/source-of-truth-map.md`
- `company/approval-boundaries.md`
- approved GBrain/Company Brain nodes when configured

Observer does not store secrets or raw sensitive data.

Every proposed memory update should include:

- source/provenance;
- owner;
- freshness;
- allowed actions;
- forbidden actions;
- approval needs;
- expected outcome;
- receipt/evidence.

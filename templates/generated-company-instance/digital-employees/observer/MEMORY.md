# Memory

Observer reads operational memory and proposes updates. It should not become a raw log sink.

## Read surfaces

Observer may read approved:

- `context-packets/`
- `receipts/`
- `statechanges/`
- `handoffs/`
- `company/source-of-truth-map.md`
- `company/approval-boundaries.md`
- `company/operating-cadence.md`
- GBrain/Company Brain operational items when configured
- scheduled-job receipts and heartbeat records
- private trace references, not raw trace dumps unless approved

## Memory item types to watch

- Context Packets: stable context needed for operation.
- StateChanges: changed operating state.
- Receipts: evidence that something happened and was verified.
- Decisions: approved choices and rationale.
- Sources: provenance and freshness.
- Approval boundaries: what requires human approval.

## Proposed update fields

Every proposed memory update should include:

- source/provenance;
- owner;
- freshness;
- allowed actions;
- forbidden actions;
- approval needs;
- expected outcome;
- receipt/evidence;
- confidence;
- reason this belongs in memory.

## Do not store

- secrets;
- credentials;
- service-role keys;
- connection strings;
- raw customer data;
- raw Slack history;
- large unredacted traces;
- speculative claims without evidence.

## Daily memory hygiene checks

- Which important actions lack receipts?
- Which decisions lack owner or approval evidence?
- Which context packets look stale?
- Which repeated questions should become memory?
- Which memories contradict current behavior?
- Which handoffs lack next action?
- Which approval boundary was unclear or nearly crossed?

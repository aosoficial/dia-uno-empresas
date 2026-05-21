# Memory Policy

Save durable operational facts only when they have provenance, owner and freshness.

Use:

- context packets for task context;
- statechanges for changes;
- receipts for completed work;
- handoffs for session continuity.

Do not store raw traces, secrets, customer data outside scope or speculative assumptions as memory.

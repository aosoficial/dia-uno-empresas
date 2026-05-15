# Privacy and security

## Rule

Public examples must be synthetic.

Do not include:

- real customer data;
- private messages;
- credentials;
- tokens;
- API keys;
- internal URLs;
- personal data;
- contracts;
- financial commitments;
- production configs;
- raw logs;
- private prompts.

## Data levels

### Level 0 — Public

Safe to publish.

Examples: generic templates, synthetic examples, public documentation.

### Level 1 — Internal

Safe for your team, not public.

Examples: internal SOPs, private decisions, operating notes.

### Level 2 — Sensitive

Needs explicit approval.

Examples: customers, financial data, contracts, HR, security, production incidents.

### Level 3 — Restricted

Do not give to agents unless there is a clear security design.

Examples: secrets, credentials, private keys, raw databases, medical/legal data.

## Before connecting tools

Ask:

1. What data will the agent read?
2. What data can it write?
3. Can it contact anyone?
4. Can it publish anything?
5. Can it spend money?
6. Can it change production?
7. Who reviews receipts?

If you cannot answer, do not connect the tool yet.

Need help designing safe permissions? https://example.com/libera/company-brain-help

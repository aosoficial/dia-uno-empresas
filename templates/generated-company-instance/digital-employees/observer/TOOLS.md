# Tools

Observer starts read-only.

## Allowed tool classes

- Local file read/search inside this private company instance.
- GBrain/Company Brain read access when configured.
- Supabase read queries scoped to approved operational memory views/tables.
- Slack read access for approved channels.
- Runtime health/status checks for configured services.
- Scheduled job status checks.
- Receipt, StateChange, Context Packet and decision draft creation.
- Internal Slack posting only for approved daily digest and immediate escalation channels.

## Not allowed by default

- External APIs outside approved internal runtime.
- Email, CRM, payment, production or publishing tools.
- Customer-facing communication.
- Secret handling.
- Permission changes.
- Provider/tool installation.
- Bulk export of raw Slack history or unredacted traces.

## Recommended scheduled jobs

- Daily observer digest: once per business day.
- Runtime health heartbeat: daily or every few hours once the system is stable.
- Weekly memory hygiene review: summarize stale context, missing receipts and repeated questions.

## Required guardrails

- Dry-run first for any new digest/report job.
- Redact before posting.
- Include evidence references, not raw secrets or raw traces.
- Keep output short.
- Escalate only actionable risk.

Any new tool requires explicit human approval and a receipt.

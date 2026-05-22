# Context Packet example — fictional agency delivery checklist

Status: example only
Owner: human operator
Freshness: example / replace before use
Privacy: no client secrets; fictional data only

## Decision / task

Create a one-page onboarding checklist for a fictional new client project.

## Source facts

- Company type: agency
- Department: delivery / operations
- Current pain: kickoff steps vary by project manager
- Input source: fictional SOP notes, not a client system
- Constraint: output must not include client names, pricing, credentials, or private links

## Allowed actions

- Summarize the kickoff steps.
- Identify missing approvals.
- Draft a checklist that a human can review.

## Forbidden actions

- Contact clients.
- Change a production system.
- Publish externally.
- Invent unavailable metrics.

## Expected output

- One checklist with owner, deadline, approval step, and evidence field.
- One note listing assumptions.

## Human review required

A human operator must confirm whether the checklist is usable before marking any receipt as `human-reviewed`.

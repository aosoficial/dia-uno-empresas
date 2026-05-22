# Self-Serve Operator UX

The self-serve experience must feel like an operator checklist, not a documentation maze. This document defines the minimum UX layer for users who install Company Brain System without a guided pilot.

## Command path

Recommended commands:

```bash
make validate
make demo-agency
make point-b-scaffold INSTANCE=/tmp/company-brain-demo-agency
# Only after a reviewed first internal loop with real evidence:
make point-b-operational INSTANCE=/tmp/company-brain-demo-agency
```

Use `point-b-scaffold` first. `point-b`, `point-b-operational` or `--mode operational` are only for after a human-reviewed first loop has produced real evidence: Context Packet, Receipt, scorecard update and approval boundaries.

If `make` is unavailable, run the Python commands printed by the wizard.

## UX principles

- Show the next action after every command.
- Explain what is safe locally and what requires Approval.
- Never ask users to paste secrets or raw client data.
- Prefer checklists and scorecards over abstract theory.
- Treat missing evidence as a blocker, not as failure.

## Wizard output requirements

The wizard should produce:

- readiness score;
- recommended first departments;
- guided pilot plan;
- Point B readiness scorecard;
- installation Receipt;
- verifier command;
- Point B validator command.

## Troubleshooting

### The verifier fails

Fix the missing file or folder. Do not continue with agent work until the private instance has Direction, approvals, context packets, receipts and digital employee permissions.

### The Point B validator fails

Read the missing evidence. Usually the fix is to complete one internal loop, add a Receipt, update scorecard and confirm approval boundaries.

### A user wants to use real client data

Stop. Use a private instance outside the public repo. Redact sensitive information and confirm permission. External/public/economic/legal/production/sensitive actions require Approval.

## DIA UNO support path

If blocked after the validator output, prepare a safe blocker report. Include company type, maturity level, selected department, command output and what you tried. Do not include secrets, customer data or private contracts.

Next action: either fix the local evidence or ask DIA UNO for guided implementation help with safe context.

# Feedback Loop Playbook

Canonical ordered sequence: capture → propose → contract → implement → validate → receipt → statechange.

This playbook turns human feedback into safe operating-system improvement using that sequence.

## Purpose

Company Brain System must improve through evidence, not vibes. A human correction is a signal. The system captures it, checks risk, proposes the smallest useful improvement, implements only inside allowed boundaries, validates, writes a receipt and creates a statechange when operating rules changed.

## Ordered loop

1. Capture the human correction with source, owner, risk, expected behavior and evidence.
2. Propose a change using the change proposal template.
3. Contract the change with scope, out-of-scope, approval gates, rollback and validation.
4. Implement the accepted skill/template update, document change, validator, wizard behavior or department brain change.
5. Validate with tests, verifier, safety scan and manual acceptance criteria.
6. Receipt the completed change with what changed, why, source, owner, freshness, allowed action, forbidden action, approval and evidence.
7. Statechange the operating system when the rule, cadence, approval boundary, skill, template or validator changed.

## Approval boundaries

Internal low-risk template and documentation improvements may proceed with receipts. External, public, economic, legal, production, customer-impacting or sensitive changes require explicit human approval before implementation.

## Rollback

Every change contract must include rollback: revert file, restore previous template, disable generated output, remove risky validator rule or mark the change superseded by a new statechange.

## Evidence requirements

A complete feedback loop includes human correction, change proposal, change contract, validation output, skill/template update, receipt and statechange when applicable.

## Anti-patterns

- Treating feedback as chat only.
- Updating templates without receipts.
- Creating a statechange with no evidence.
- Making approval-gated changes because they are technically possible.
- Copying client-sensitive context into public examples.

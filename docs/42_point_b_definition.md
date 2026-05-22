# Point B Definition

Punto B is not a slogan. It is a verifiable operating state for an AI-First service business.

## Punto B minimum

A company reaches the minimum Punto B slice when it has:

1. Direction / Mother Brain installed.
2. One source-of-truth map reviewed before the first Context Packet.
3. One priority department installed.
4. One digital employee with permissions and forbidden actions.
5. One context packet used for real internal work.
6. One Receipt proving the action.
7. One scorecard line updated with evidence.
8. One approval boundary reviewed by a human.
9. One next sprint selected.

## Punto B strong

A stronger Punto B state adds:

- Sales to Operations handoff.
- Operations to Customer Success handoff.
- Finance visibility before economic commitments.
- Weekly cadence.
- Feedback loop converting corrections into skill or method proposals.
- Public/private separation for all generated material.

## What does not count

- Having many agents with no permissions.
- Having documents with no owner.
- Having a wizard output with no Receipt.
- Having scorecards with no evidence.
- Letting agents take external/public/economic/legal/production/sensitive actions without Approval.

## Readiness levels

- 0–39: Punto A. Install Direction first.
- 40–59: documented but not operational. Run Sprint 1.
- 60–74: assisted. Run first department loop.
- 75–89: operating AI-First slice. Add feedback and finance/customer success.
- 90–100: compounding. Improve skills, experiments and anonymized learnings.

## Evidence required

Every claim must point to files or records:

- `company/company-brain.md`
- `company/source-of-truth-map.md`
- `company/approval-boundaries.md`
- `company/company-scorecard.md`
- `company/guided-pilot-plan.md`
- `company/point-b-readiness.md`
- `departments/<department>/department-brain.md`
- `digital-employees/<employee>/PERMISSIONS.md`
- `context-packets/`
- `receipts/`
- `statechanges/` when operating state changed

Next action: run `python scripts/validate_point_b_readiness.py --mode scaffold <instance>` after generation, then run `python scripts/validate_point_b_readiness.py --mode operational <instance>` only after the first human-reviewed operating loop has non-placeholder evidence. Fix missing evidence before claiming Punto B.

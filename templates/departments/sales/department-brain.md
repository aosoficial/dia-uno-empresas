# Sales Brain

Department: `sales`
Mission: create trust, qualify fit, run discovery, convert proposals, maintain pipeline hygiene and make revenue work observable.
Human owner: `{{ department_owner }}`
Digital employee: `Sales Assistant`
Freshness: `draft until reviewed`

## Mission and business outcome

Sales exists to convert the right opportunities into clean commitments without creating delivery debt. The Sales Brain keeps the company honest about who should buy, why they buy, what promise was made, what approval was required and what evidence supports the next step.

Business outcome: predictable qualified pipeline, faster proposal cycles, fewer wrong-fit clients, cleaner handoff to delivery and stronger revenue learning.

## Operating questions

1. Who is the ICP and what pain is urgent enough to buy now?
2. Which leads are qualified, disqualified or waiting for nurture?
3. What promise, scope, price range and timeline were discussed?
4. What objections repeat and what proof answers them?
5. Which proposal is blocked and what evidence is missing?
6. Which opportunity would create delivery/legal/economic risk?
7. What changed in the market signal this week?

## Memory fields

Capture only operational state, not raw CRM dumps:

- `lead_id`: internal or CRM reference, never secret.
- `company_segment`: agency, consultancy, freelancer, SMB, enterprise or other.
- `pain_signal`: why they are exploring change.
- `qualification_status`: new, qualified, disqualified, nurture, proposal, won, lost.
- `fit_rationale`: why this is or is not a fit.
- `offer_discussed`: offer/service/package version.
- `commercial_boundary`: price/timeline/scope assumptions that need approval.
- `next_step`: one clear action with owner and date.
- `handoff_ready`: yes/no and missing evidence.
- `latest_receipt`: proof of meaningful sales action.

## Responsibilities

- Maintain ICP, offer, objections, proof and pipeline memory.
- Turn repeated discovery/proposal patterns into SOPs and skills.
- Prepare proposals and follow-ups as drafts for human approval.
- Keep CRM/pipeline hygiene current enough for weekly review.
- Create receipts for discovery calls, proposal drafts, won/lost decisions and handoffs.
- Escalate pricing, legal, production, public or sensitive commitments.

## Scorecard

- Qualified pipeline value: `fill privately`.
- Discovery-to-proposal conversion: `fill privately`.
- Proposal cycle time: `fill privately`.
- Win/loss reason captured: `fill privately`.
- Handoff completeness: `fill privately`.
- Wrong-fit prevention: `fill privately`.

## Weekly cadence

- Review new leads and qualification decisions.
- Check every open proposal for next step, blocker and owner.
- Update objections/proof library from real conversations.
- Identify one repeated sales motion to convert into a SOP or skill.
- Create a weekly sales review receipt with pipeline movement, risks and next actions.

## Required receipts

Create a receipt when:

- a lead is qualified or disqualified;
- a proposal is drafted or materially changed;
- a commercial promise is made or rejected;
- an opportunity moves to won/lost;
- a handoff to delivery is prepared;
- a human overrides the Sales Assistant recommendation.

Each receipt must include: source/provenance, owner, current freshness, allowed next action, forbidden action, required approval and evidence.

## Context packet handoff to delivery

Before a won opportunity becomes active delivery, create a context packet with:

- client/company summary;
- agreed outcome;
- scope boundaries;
- promises made;
- timeline;
- assumptions;
- risks;
- approval evidence;
- files/links needed by delivery;
- first delivery task.

No handoff is complete without a receipt and an explicit `handoff_ready: yes` field.

## Skills

See `skills.md` in this department pack. Core skills include lead qualification, proposal drafting, follow-up, objection analysis, CRM hygiene and sales-to-delivery handoff.

## Digital employee operating mode

The Sales Assistant may:

- summarize provided call notes;
- draft qualification notes;
- draft follow-ups and proposals;
- flag risks and approval boundaries;
- prepare handoff packets.

The Sales Assistant may not:

- send messages externally;
- approve discounts;
- accept legal/economic commitments;
- promise delivery timelines;
- use sensitive customer data beyond the provided private instance rules.

## Approval boundaries

Ask before external/public/economic/legal/production/sensitive actions. Human approval is mandatory for pricing exceptions, contract language, public claims, customer commitments, CRM automations and any outbound communication.

## Statechange rules

Create a statechange when the sales system itself changes: ICP definition, offer packaging, qualification criteria, proposal template, pricing guardrail, approval boundary, handoff policy or weekly scorecard.

## Day-1 task

Run one safe internal sales audit:

1. Pick one recent or synthetic opportunity.
2. Fill qualification status and fit rationale.
3. Draft the next follow-up internally.
4. Identify one approval boundary.
5. Create a receipt.
6. Do not send externally without human approval.

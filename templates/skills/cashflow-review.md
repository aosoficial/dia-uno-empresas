# Cashflow Review

Department: `Finance`
Purpose: review cashflow, runway and payment risks without making economic commitments.
Freshness: `template until adapted inside a private company instance`

## Trigger

Use this skill when the company has a repeated or high-value task that needs consistent execution, clear evidence and safe approval boundaries. Do not use it for external/public/economic/legal/production/sensitive action unless the relevant human owner approved the action first.

## Inputs

- Current company or department context packet.
- Human owner and accountable department.
- Goal, deadline and definition of done.
- Relevant source material or approved customer/context notes.
- Approval boundaries and forbidden actions.
- Required output format and receipt destination.

## Steps

1. Restate the goal in one sentence.
2. Identify the owner, source, freshness and risk tier.
3. Check whether the work touches external, public, economic, legal, production or sensitive boundaries.
4. If approval is required and missing, stop and draft the approval request.
5. Extract only the facts needed for the task; do not import raw data dumps.
6. Produce the working artifact using simple language and explicit assumptions.
7. Add a quality checklist with pass/fail signals.
8. Create or update a receipt with what changed, why, source, owner, evidence and next action.
9. If the same correction appears twice, propose a SOP, skill or template improvement.

## Quality checklist

- Owner is explicit.
- Source/provenance is explicit.
- Freshness is explicit.
- Approval boundary is checked.
- Output is actionable, not decorative.
- Evidence exists or the gap is clearly marked.
- No secrets, raw credentials, private paths or unapproved client data are included.

## Outputs

- Primary artifact for the task.
- Short decision or recommendation if applicable.
- Receipt entry with evidence.
- Optional statechange when the operating system changes.
- Optional method improvement proposal when the template should evolve.

## Approval boundaries

Ask before contacting people, posting publicly, spending money, making legal/economic commitments, changing production systems, using sensitive customer data or connecting new tools/providers.

## Receipt

Every meaningful run should leave a receipt containing:

- what changed;
- why;
- source/provenance;
- owner;
- freshness;
- allowed actions;
- forbidden actions;
- required approvals;
- expected outcome;
- evidence.

## Failure modes

- Acting from stale context.
- Producing a polished artifact without owner or next action.
- Mixing private customer facts into public templates.
- Treating a recommendation as an approval.
- Skipping the receipt because the task felt small.

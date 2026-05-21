# Change Contract

Use this template when a proposal is accepted and implementation is about to happen.

## Scope
Files, templates, skills, docs, validators or generated instance outputs that may change.

## Out of scope
Actions that must not happen in this change. Include no commit, no push, no publication, no production and no real customer data unless approved.

## Implementation steps
1. Write or update tests first when possible.
2. Implement the smallest complete change.
3. Run validators.
4. Correct failures.
5. Create receipt.
6. Create statechange if the operating method changed.

## Rollback
Describe how to revert the change safely. Prefer file-level revert, feature flag or template rollback.

## Validation
List exact tests, smoke tests, safety scans and verifier commands.

## Owner
`{{ owner }}` owns the decision and confirms whether this item may change the operating system.

## Source
`{{ source }}`. Include the exact human correction, observed failure, transcript excerpt, QA result, receipt or context packet that created the signal. Do not invent missing context.

## Approval
Human approval is required before external, public, economic, legal, production, customer-impacting or sensitive actions. If the change is safe and internal, record why it is safe.

## Evidence
Link the receipt, statechange, validation output, changed skill/template path and rollback note. Evidence must be sufficient for another operator to audit the change later.

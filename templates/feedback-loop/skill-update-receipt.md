# Skill / Template Update Receipt

Use this after a feedback loop changes a skill, template, department brain, wizard behavior or validator.

## What changed
List exact files and a short operational summary.

## Why
Reference the human correction and the accepted change contract.

## Before
Describe the previous behavior or gap.

## After
Describe the new behavior and how another operator can verify it.

## Validation
List tests, validators, smoke tests, safety scans and manual checks.

## Rollback
Explain how to undo the change if it causes harm or confusion.

## Next improvement
If the change reveals a broader pattern, propose the next safe loop.

## Owner
`{{ owner }}` owns the decision and confirms whether this item may change the operating system.

## Source
`{{ source }}`. Include the exact human correction, observed failure, transcript excerpt, QA result, receipt or context packet that created the signal. Do not invent missing context.

## Approval
Human approval is required before external, public, economic, legal, production, customer-impacting or sensitive actions. If the change is safe and internal, record why it is safe.

## Evidence
Link the receipt, statechange, validation output, changed skill/template path and rollback note. Evidence must be sufficient for another operator to audit the change later.

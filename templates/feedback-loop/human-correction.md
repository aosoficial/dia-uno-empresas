# Human Correction Capture

Use this template when a human says the system, agent, skill, template, process or output was wrong, incomplete, unsafe or too shallow.

## Correction
`{{ human_correction }}`

## Expected behavior
Describe what should have happened instead. Include examples, acceptance criteria and what “better” means operationally.

## Affected area
Department, skill, template, wizard, validator, digital employee, approval boundary or documentation.

## Risk
Classify whether the correction affects quality, privacy, money, legal, customer trust, production, public claims or internal convenience.

## Next action
Create a change proposal if the correction is valid. Create a receipt even if the decision is to reject the correction.

## Owner
`{{ owner }}` owns the decision and confirms whether this item may change the operating system.

## Source
`{{ source }}`. Include the exact human correction, observed failure, transcript excerpt, QA result, receipt or context packet that created the signal. Do not invent missing context.

## Approval
Human approval is required before external, public, economic, legal, production, customer-impacting or sensitive actions. If the change is safe and internal, record why it is safe.

## Evidence
Link the receipt, statechange, validation output, changed skill/template path and rollback note. Evidence must be sufficient for another operator to audit the change later.

# Markdown local memory backend

## Use when

Use when the company is starting, the operator needs maximum portability, or the work is a workshop/private pilot. Markdown local is the default for the first 48 hours because it is simple, auditable and easy to review without infrastructure.

## Setup

1. Create the generated Company Brain instance.
2. Keep `company/`, `departments/`, `context-packets/`, `receipts/`, `statechanges/` and `handoffs/` in versioned private storage.
3. Assign a human owner for each department brain.
4. Run the verifier after installation and after major template changes.

## Allowed data

- Operating principles.
- Department responsibilities.
- Synthetic examples.
- Internal decisions approved for the private instance.
- Receipts and statechanges without secrets.

## Forbidden data

- API keys, tokens, passwords or connection strings.
- Raw client secrets.
- Unapproved production data.
- Personal data that has no operational purpose.

## Receipts

Every meaningful edit should leave a receipt with source, owner, why, validation and next allowed action.

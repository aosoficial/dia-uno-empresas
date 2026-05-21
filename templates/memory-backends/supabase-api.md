# Supabase / API memory backend

## Use when

Use when Company Brain memory must support a product interface, multi-user access, structured permissions, dashboards, API integrations or large-scale reporting.

## Setup

1. Define schema for companies, departments, employees, receipts, statechanges and context packets.
2. Apply row-level security before storing sensitive client data.
3. Separate environments for development, staging and production.
4. Store secrets in the runtime secret manager, never in repository files.
5. Run migrations only with owner approval and rollback notes.

## Allowed data

- Structured operational records.
- Approval states.
- Scorecard metrics.
- Receipt metadata and links to evidence.
- Department ownership and cadence records.

## Forbidden data

- Plaintext secrets.
- Data from another company without legal basis and approval.
- Unreviewed raw uploads.
- Production data in development databases.

## Receipts

Every migration, schema change, policy change and data import needs a receipt with validation query, affected tables, owner, rollback path and approval evidence when required.

# Client systems memory backend

## Use when

Use when the client already has a mandatory system of record: CRM, project management, ticketing, knowledge base, Drive, Notion or internal database. The Company Brain adapts to the approved client environment instead of copying sensitive data into a separate store.

## Setup

1. Identify the client system of record for each data class.
2. Define allowed write locations for context packets, receipts and statechanges.
3. Confirm permissions and audit logs.
4. Use links or summaries when raw data cannot leave the client system.
5. Document the client approval boundary before agents operate.

## Allowed data

- Approved summaries.
- Links to client records.
- Receipts stored in client-approved folders.
- Non-sensitive operating metadata.

## Forbidden data

- Shadow copies of restricted client data.
- Credentials exported from client tools.
- Data stored outside the client's approved retention policy.
- Agent actions that bypass client permissions.

## Receipts

Every action should leave evidence in the client-approved location, with operator, time, source record, changed record, validation and escalation rule.

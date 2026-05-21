# Memory Backend Profiles

Company Brain can run on different memory backends. The backend is an operating choice, not a branding choice. Pick the smallest backend that can safely preserve decisions, context, permissions, receipts and improvement loops.

## Selection matrix

- **Markdown local**: best for first installation, workshops, solo operators, private pilots and offline review. Simple files, easy diffs, easy export.
- **GBrain / MCP**: best when agents need tool-mediated memory, linked receipts, graph context and operational state shared across runtime profiles.
- **Supabase / API**: best when a team needs a shared database, applications, dashboards, access control and structured queries.
- **Client systems**: best when memory must stay in the client's existing tools such as Notion, Drive, CRM, ticketing or document systems.

## Data boundary

Every backend must define:

- owner;
- allowed data;
- forbidden data;
- retention rule;
- approval gates;
- export path;
- deletion path;
- receipt evidence.

Do not mix Company Brain memory across companies. Cross-company learning travels only as anonymized patterns, public-safe templates or approved context packets.

## Migration rule

Start with Markdown local unless the operating context requires GBrain/MCP, Supabase/API or client systems on day one. Migrate only when there is evidence that the current backend is limiting execution, auditability, scale or permissions.

Migration must produce a receipt with:

- source backend;
- target backend;
- reason;
- data classes moved;
- data classes excluded;
- owner approval if sensitive or client data is involved;
- verification result.

## Profile 1 — Markdown local

Use for bootstrapping, first digital employee setup and examples. Keep files plain, reviewable and portable.

## Profile 2 — GBrain / MCP

Use when the runtime needs graph links, state changes, context packets and receipts available through agent tools.

## Profile 3 — Supabase / API

Use when memory must power a product UI, multi-user workflow, row-level permissions or external integrations.

## Profile 4 — Client systems

Use when the client has a mandated system of record. The Company Brain should write context packets and receipts in the approved client location instead of copying private data elsewhere.

## Operating principle

Memory is operational state. It is not a dumping ground. If a fact cannot guide action, approval, validation or accountability, it should not be promoted to durable memory.

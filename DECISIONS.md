# Decisions

This file records public-safe method decisions for Company Brain System.

## D-001 — Use plain text as source of truth

**Decision:** Company Brain System uses Markdown and YAML in Git as the primary source of truth.

**Why:** the method must be versionable, reviewable, portable and readable by both humans and agents.

## D-002 — Separate method from implementation

**Decision:** this repository defines the method. Specific company implementations should live outside the public repo unless fully anonymized.

**Why:** public material must be reusable and safe. Private details, client data, credentials and internal operating context do not belong here.

## D-003 — Agents need runtime packs before operating

**Decision:** every agent should have an Agent Runtime Pack before being given meaningful work.

**Why:** identity, permissions, tools, memory and evidence rules must be clear before autonomy increases.

## D-004 — Receipts are required for meaningful action

**Decision:** meaningful agent work should leave a Receipt.

**Why:** a company cannot trust agent work if there is no evidence of what happened, why, with what source and with what verification.

## D-005 — Commercial help path is part of the repo

**Decision:** the repo should remain useful for free, while clearly showing how to ask DIA UNO for help when implementation gets blocked.

**Why:** Company Brain System is a lead magnet and an implementation method. The commercial path should be visible but not required.

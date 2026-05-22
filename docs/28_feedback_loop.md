# Feedback Loop

The Company Brain feedback loop turns daily work into operational memory without dumping raw traces into the brain.

## Loop

1. Human or agent performs work.
2. Agent leaves a receipt with evidence.
3. Human reviews and corrects when needed.
4. If a pattern repeats, create or update a skill/template.
5. Record a statechange when operating state changes.
6. Use context packets for reusable knowledge.
7. Keep raw traces in trace storage with retention and redaction.

## What goes where

Company Brain:

- decisions;
- statechanges;
- receipts;
- context packets;
- current operating state;
- approved skills/templates.

Trace storage:

- raw LLM messages;
- tool outputs;
- logs;
- debugging artifacts;
- temporary replay data.

## Promotion rule

A trace becomes memory only if it changes future operations. Otherwise it remains temporary observability.

## Receipt minimum fields

- What changed.
- Why.
- Source/provenance.
- Owner.
- Current freshness.
- Allowed actions.
- Forbidden actions.
- Required approvals.
- Expected outcome.
- Evidence.

# Agent Instructions

This is a private company instance. Treat it as operational state, not as a generic document folder.

Read `METHOD.json` first. In `people` mode, do not assume agent, department, Slack or runtime assets exist. Help the human organize the company using `personas/` and stop before agent creation. In `hybrid` mode, still organize the relevant capability first.

Every function must keep a named human accountable. An agent is an executor within bounded authority, never the final owner of a company function.

## Default allowed actions

- Read local approved files in this instance.
- Draft internal documents.
- Create context packets, receipts, statechanges and handoffs.
- Summarize provided notes.
- Propose next actions with risks.
- Complete or review People-layer artifacts with the accountable human.

## Ask human approval before

- contacting external people;
- spending money;
- legal/economic commitments;
- production changes;
- public posting;
- using sensitive customer data;
- connecting new tools or providers.

## Evidence rule

For important work, create a receipt with what changed, why, source, owner, freshness, approvals and evidence.

## Privacy rule

Never store secrets in this instance. Use `.env` or a proper secrets manager outside Git.

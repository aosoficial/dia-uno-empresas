# 38 — Skill Evolution v0

Skill Evolution v0 is the controlled Company Brain pattern for improving skills from real work without silently mutating the public method.

It extends the existing feedback loop:

`correction → candidate skill proposal → replay validation → approval → private skill update → receipt → optional anonymized public proposal`

## Principles

- Local/private first per generated company instance.
- Candidate skill changes are staged before acceptance.
- Every candidate records source/provenance, owner, affected department, expected outcome, risks, forbidden actions and receipt link.
- Replay validation uses synthetic or anonymized private-safe cases.
- Public method updates require anonymization, anti-secret review and explicit approval.
- The system proposes skill updates; it does not silently mutate public method files.

## Skill registry

Each active skill should have a registry entry with:

- skill name;
- department;
- owner;
- version;
- source/provenance;
- validation cases;
- latest receipt;
- allowed actions;
- forbidden actions;
- next review date.

## Candidate proposal

A candidate is created when:

- a human corrects the same behavior twice;
- a repeated workflow becomes stable;
- a validation failure reveals a missing step;
- a department brain needs a new operational capability;
- DIA UNO sees an anonymized implementation pattern.

## Replay validation

Before accepting a candidate:

1. Build one synthetic or anonymized case.
2. Run the old skill or current SOP against the case.
3. Run the candidate against the same case.
4. Compare expected output, safety, clarity and receipt quality.
5. Keep, revise or discard.

## Approval boundaries

Private skill updates can be accepted by the company owner when risk is internal-low.

Ask for explicit approval before:

- public method updates;
- skill changes affecting legal/economic/client-facing/production/sensitive actions;
- importing external traces;
- sharing examples with DIA UNO;
- installing proxy/session-capture tooling.

## Relationship to benchmarks

- SkillClaw informs the registry, candidate and replay concepts.
- Sylph informs simple skill creation and human approver ergonomics.
- AutoResearch informs bounded experiments and keep/discard ledgers.

## Future work

- Add a validator for candidate skill proposals.
- Add a registry health report.
- Add an isolated experiment profile for testing external skill-evolution tools.

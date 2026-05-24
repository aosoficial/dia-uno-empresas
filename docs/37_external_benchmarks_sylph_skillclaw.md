# 37 — External Benchmarks: Sylph, SkillClaw and AutoResearch

These projects are benchmarks and inspiration. They are not dependencies of DIA UNO Empresas.

## Sylph

Source: `https://github.com/getnao/sylph`, inspected as an external benchmark.

Useful patterns to adapt:

- Ask less, derive more from public company context while treating derived facts as hypotheses.
- Keep clear folders for domains, skills, agents and self-improvement notes.
- Make the human approver visible, similar to a Chief Agent Officer role.
- Provide a simple skill creation path for repeated work.

What not to copy:

- Do not copy text or repo structure verbatim.
- Do not import automatic hooks that pull remote changes in client environments.
- Do not treat public web-derived guesses as operational memory.

## SkillClaw

Source: `https://github.com/AMAP-ML/SkillClaw`, inspected as an external benchmark.

Useful patterns to adapt:

- Skill registry.
- Candidate skill proposals.
- Replay validation.
- Deduplication and consolidation.
- Local/private-first skill learning before any shared/public update.

What not to copy:

- Do not add proxy/session capture to Hermes or client runtimes by default.
- Do not share real traces, session logs or client patterns externally.
- Do not auto-publish skill mutations.
- Do not add SkillClaw as a runtime dependency for Sprint 9.

## AutoResearch

Source: `https://github.com/karpathy/autoresearch`, inspected as an external benchmark.

Useful patterns to adapt:

- `program.md`-style contract for an autonomous experiment.
- One editable surface per experiment.
- Baseline before improvement.
- Fixed time/cost budget.
- Keep/discard/revert based on a metric.
- Ledger of runs with score, status and notes.

What not to copy:

- Do not copy the infinite loop literally into business operations.
- Do not optimize one metric if it harms trust, quality, client outcome, compliance or brand.
- Do not run experiments on production/client systems without approval.

## How this informs DIA UNO Empresas

- Sylph improves onboarding ergonomics and role clarity.
- SkillClaw informs Skill Evolution v0.
- AutoResearch informs bounded Experiment Loop v0.
- DIA UNO can collect anonymized implementation patterns, but only after anti-secret review and explicit approval.

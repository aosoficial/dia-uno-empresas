# Installer Plan

DIA UNO Empresas installs a private People-first organizational scaffold and can later extend it into a governed hybrid scaffold from a public, safe, hardware-neutral repo.

## Target user

Agencies, consultancies and freelancers becoming productized AI-First service businesses.

## Installation paths

### Guided accelerator

Use the wizard:

```bash
python scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --output /tmp/acme-company-brain --yes
python scripts/verify_installation.py /tmp/acme-company-brain
```

### Minimal bootstrap

Use bootstrap for a smaller skeleton:

```bash
python scripts/bootstrap_company_brain.py --company "Acme Demo" --company-type agency --output /tmp/acme-company-brain --yes
```

## Runtime targets

Use any approved private environment: local PC, team server, ORGO, cloud workstation or client-approved provider.

Both commands accept `--method-mode people` or `--method-mode hybrid`. Use `people` when core functions are not yet organized. An existing People instance can be continued non-destructively with the wizard's `--upgrade` option.

## What every installation creates

- Method mode and `scaffold_not_operational` status.
- The 36 preserved Método V3 originals, inventory and integrity manifest.
- People organization plan and readiness scaffold.
- Dirección / Mother Brain, accountability and approval boundaries.
- Receipts, StateChanges, Context Packets and handoff folders.

## What hybrid mode additionally creates

- Department brains and onboarding assets.
- Skills registry.
- Digital employee pack.
- 48h / 7d / 30d roadmap.

Generation does not activate an agent, runtime, credential, integration or service.

## Safety

- No external calls.
- Dry-run by default.
- Refuses output inside canonical repo unless synthetic example mode is explicit.
- Scans generated text for likely secrets.
- Keeps real company data outside the public repo.

# Installer Plan

Company Brain System installs a private AI-First company operating system from a public, safe, hardware-neutral repo.

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

## What the installer creates

- Dirección / Mother Brain first.
- Company brain and approval boundaries.
- Accountability map and operating cadence.
- Department brains and onboarding assets.
- Skills registry.
- Digital employee pack.
- Receipts/statechanges/context-packets folders.
- 48h / 7d / 30d roadmap.

## Safety

- No external calls.
- Dry-run by default.
- Refuses output inside canonical repo unless synthetic example mode is explicit.
- Scans generated text for likely secrets.
- Keeps real company data outside the public repo.

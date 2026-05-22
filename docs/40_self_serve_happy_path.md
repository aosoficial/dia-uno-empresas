# Self-Serve Happy Path

This is the maximum self-serve path for a non-technical operator. It keeps the repo useful without support, while making clear when a guided pilot or DIA UNO help is appropriate.

## Who this is for

- Agency founder who wants to productize delivery.
- Consultant with repeated client work and scattered knowledge.
- Freelancer becoming a small service business.

## The safe self-serve promise

You can install a private Company Brain instance, diagnose your Punto A, choose the first department, run one internal digital employee loop and produce evidence. The repo does not send messages, spend money, change production or handle real client data automatically.

## Step 1 — run the dry run

```bash
python scripts/company_brain_wizard.py --dry-run --company "Acme Demo" --company-type agency --output /tmp/acme-company-brain
```

Evidence:
- readiness score;
- recommended departments now;
- recommended next sprint.

Next action: read the dry-run output. If it recommends Direction first, do not skip it.

## Step 2 — create the private instance

```bash
python scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --output /tmp/acme-company-brain --yes
python scripts/verify_installation.py /tmp/acme-company-brain
python scripts/validate_point_b_readiness.py /tmp/acme-company-brain
```

Approval: writing local files is safe. Any external/public/economic/legal/production/sensitive action still requires a human decision.

## Step 3 — fill only safe private context

Fill:
- offer;
- ICP;
- bottleneck;
- owner;
- tools map;
- scorecard values;
- one internal workflow.

Do not paste:
- passwords;
- API keys;
- raw customer data;
- private contracts;
- regulated personal data;
- production credentials.

## Step 4 — run one internal action

Use the first digital employee only to draft, analyze or prepare. It may create a context packet, QA checklist, proposal draft or SOP draft. It may not send, publish, invoice, deploy or change client systems.

Evidence:
- context packet;
- human review;
- Receipt;
- StateChange when the operating system changed.

## Step 5 — ask for help only with safe blockers

If blocked, use the DIA UNO blocker template. Strip private details. Share the bottleneck, company type, maturity level, what you tried and what evidence exists.

Next action: either continue with the next sprint or ask DIA UNO for implementation help using safe context only.

# Self-Serve Happy Path

This is the maximum self-serve path for a non-technical operator. It keeps the repo useful without support, while making clear when a guided pilot or DIA UNO help is appropriate.

## Who this is for

- Agency founder who wants to productize delivery.
- Consultant with repeated client work and scattered knowledge.
- Freelancer becoming a small service business.

## The safe self-serve promise

You can install a private People instance, organize one capability and produce evidence. If that capability becomes mature, you can upgrade the same instance and run one supervised internal agent loop. The repo does not send messages, spend money, change production or handle real client data automatically.

## Step 1 — run the dry run

```bash
python scripts/company_brain_wizard.py --dry-run --company "Acme Demo" --company-type agency --method-mode people --output /tmp/acme-company-brain
```

Evidence:
- selected method mode;
- People organization sequence;
- installation and integrity checks to run next.

Next action: read the dry-run output and start with Rumbo and human accountability.

## Step 2 — create the private instance

```bash
python scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --method-mode people --output /tmp/acme-company-brain --yes
python scripts/verify_installation.py /tmp/acme-company-brain
python scripts/validate_people_readiness.py /tmp/acme-company-brain
```

These checks confirm structure, inventory and byte-for-byte integrity. They do not prove that the company has implemented the method.

Approval: writing local files is safe. Any external/public/economic/legal/production/sensitive action still requires a human decision.

## Step 3 — organize one capability with safe private context

Fill:
- Rumbo and the capability outcome;
- one human accountable;
- role, decision boundary and evaluation rule;
- one process and its SOP;
- source-of-truth map with owner, freshness, permissions, risks and evidence path;
- metric, cadence and fallback.

Do not paste:
- passwords;
- API keys;
- raw customer data;
- private contracts;
- regulated personal data;
- production credentials.

## Step 4 — upgrade only when the capability is mature

```bash
python scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --method-mode hybrid --output /tmp/acme-company-brain --upgrade --yes
python scripts/verify_installation.py /tmp/acme-company-brain
python scripts/validate_point_b_readiness.py --mode scaffold /tmp/acme-company-brain
```

The upgrade adds missing agent and department scaffolds without overwriting People work. It does not activate anything.

## Step 5 — run one internal action

Use the first digital employee only to draft, analyze or prepare. It may create a context packet, QA checklist, proposal draft or SOP draft. It may not send, publish, invoice, deploy or change client systems.

For a detailed step-by-step guide with prerequisites, synthetic example and exit criteria per step, see [`templates/how-to/run-first-internal-loop.md`](../templates/how-to/run-first-internal-loop.md).

Evidence:
- context packet;
- reviewed source-of-truth map for the workflow input;
- human review;
- Receipt;
- StateChange when the operating system changed.

## Step 6 — ask for help only with safe blockers

If blocked, use the DIA UNO blocker template. Strip private details. Share the bottleneck, company type, maturity level, what you tried and what evidence exists.

Next action: either continue with the next sprint or ask DIA UNO for implementation help using safe context only.

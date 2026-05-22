# Guided Pilot Happy Path

This is the guided path for taking a service business from Punto A to Punto B with an operator in the loop. It does not promise magic or a guaranteed outcome; it gives the operator a closed sequence, evidence requirements and escalation rules.

## Goal

In one guided pilot, the company leaves the session with a working Direction / Mother Brain, a reviewed source-of-truth map, one priority department installed, one digital employee operating safely, and one feedback loop producing a Receipt and StateChange.

## 30 / 60 / 120 minute path

### First 30 minutes — decide the operating contract

- Confirm company type: agency, consultancy or freelancer.
- Capture Punto A symptoms: scattered knowledge, manual delivery, weak handoffs, no operating memory.
- Select the bottleneck: sales, delivery, customer success, finance, product/software or people.
- Define the first safe internal task.
- Write the approval boundary before any agent work.

Evidence:
- initial context packet;
- selected bottleneck;
- owner;
- first objective;
- Approval boundary.

Next action: run the wizard and create the private instance.

### First 60 minutes — install Direction and first department

- Generate the private instance.
- Read `company/company-brain.md`, `company/source-of-truth-map.md` and `company/approval-boundaries.md`.
- Assign the human owner for Direction.
- Mark which system is the current source for the first workflow, who owns it, freshness, permissions, risks and evidence path.
- Install one department brain and its digital employee pack.
- Fill one scorecard line with current values or `unknown` when not evidenced.

Evidence:
- department rollout map;
- reviewed source-of-truth map;
- company scorecard;
- first department brain;
- Receipt for installation.

Next action: run `python scripts/verify_installation.py <instance>`.

### First 120 minutes — run one real internal loop

- Convert one real internal workflow into a context packet only after the source-of-truth map names the system/source, owner, freshness, permissions and evidence path.
- Ask the digital employee to draft or analyze only; no external action.
- Human reviews the output and records approval, correction or rejection.
- Update scorecard and write a Receipt.
- If the workflow changed, write a StateChange.

Evidence:
- context packet;
- reviewed draft;
- Receipt;
- StateChange if operating state changed;
- blocker if the loop cannot complete.

Next action: run the Point B readiness validator and choose Sprint 1, 2, 3 or 4.

## Definition of done

A guided pilot is done when the operator can answer:

- What changed?
- Why did it change?
- Who owns it?
- What evidence proves it?
- Which source/system proves the input and how fresh is it?
- What can the digital employee do without approval?
- What still requires approval?
- What is the next sprint?

If one answer is missing, the pilot is not closed. Create a blocker Receipt instead of pretending Punto B was reached.

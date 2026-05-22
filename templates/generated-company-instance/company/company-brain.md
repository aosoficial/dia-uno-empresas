# Company Brain

Company: `{{ company_name }}`
Sector: `{{ sector }}`
Owner: `{{ owner }}`
Freshness: initial bootstrap

## Purpose

Describe the company in operational terms. Start here before asking a digital employee to work: this file is the Direction / Mother Brain for the private instance.

## Fill first

- Owner / responsable humano: `{{ owner }}` or the accountable operator.
- Source / procedencia: where these facts came from.
- Freshness / vigencia: when they were last reviewed.
- Approval: who reviewed the direction before the first operating loop.
- Evidence: link to `receipts/first-loop.md` after the first human-reviewed loop.

## Direction governance

Complete these files to close the Direction chain before operating departments:

- Plan anual y rocks: [`company/annual-plan.md`](annual-plan.md)
- OKRs por rock: [`company/okrs.md`](okrs.md)
- Organigrama operativo: [`company/org-chart.md`](org-chart.md)
- Roles y responsabilidades: [`company/roles-and-responsibilities.md`](roles-and-responsibilities.md)
- Mapa de fuentes: [`company/source-of-truth-map.md`](source-of-truth-map.md)
- Límites de aprobación: [`company/approval-boundaries.md`](approval-boundaries.md)

## Current operating state

- Departments: `{{ first_department }}` first.
- First digital employee: `{{ first_employee }}`.
- External actions require human approval.

## Known context

Add only verified facts with source and freshness.

## Open questions

- What are the top three workflows worth improving?
- What systems are in scope?
- What data is forbidden for agents?

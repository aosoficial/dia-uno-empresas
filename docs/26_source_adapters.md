# Source Adapters and Import Strategy

This repo can learn from public sources without copying private data or blindly importing another system. Sources are adapted into Company Brain concepts: departments, skills, operating cadence, templates and guardrails.

## Reviewed sources

### `msitarzewski/agency-agents`

Use for: deliverable-focused agent taxonomy across engineering, marketing, sales, finance, support, product, project management and testing.

Adaptation:

- Map agent roles to department digital employee packs.
- Keep Company Brain approval boundaries stricter than generic agent prompts.
- Prefer role patterns and deliverables over copying personalities verbatim.

### `coreyhaines31/marketingskills`

Use for: marketing skill graph where product marketing is foundational, then SEO, CRO, copywriting, analytics, ads, lifecycle and sales enablement.

Adaptation:

- Make `product-marketing` the required first marketing skill.
- Add skill recommendations by department.
- Keep tool credentials out of repo; generated instances use placeholders.

### `bradfeld/ceos`

Use for: EOS-inspired People OS: vision, accountability chart, rocks, scorecard, Level 10 meetings, IDS, todos, process and people analyzer.

Adaptation:

- Install people/accountability before agents.
- Use scorecards and issue solving in Dirección.
- Store lightweight markdown operating artifacts in generated private instance.

## Web development and product sources

These sources were found via GitHub search and inspected at repo/README/license level.

### `alan2207/bulletproof-react`

Use for: scalable React application architecture, feature-oriented structure, production frontend conventions and quality gates.

Adaptation:

- Product / Software department templates should ask for architecture, feature boundaries, testing, CI and maintainability.
- Use as a pattern source for internal web app delivery, not as a required stack.

License note: MIT in repository.

### `ixartz/Next-js-Boilerplate`

Use for: modern Next.js product baseline with TypeScript, Tailwind, testing, Storybook, auth/database/monitoring patterns and developer experience.

Adaptation:

- Use as a reference checklist for launch-ready web product setup.
- Keep Company Brain hardware-neutral and vendor-neutral; do not force Next.js or any provider.

License note: MIT in repository.

### `drublic/checklist`

Use for: frontend launch checklist covering performance, resources, rendering, caching and measurements.

Adaptation:

- Convert into web launch QA skill/checklist inside Product / Software and Operations / Delivery.
- Pair with receipts so web launches have evidence.

License note: no explicit license detected during quick scan; treat as reference only unless license is clarified.

### `deanpeters/Product-Manager-Skills`

Use for: product manager skills and command workflows for AI agents.

Adaptation:

- Use as inspiration for product discovery, prioritization, roadmap, PRDs, stakeholder updates and product reviews.
- Do not copy wholesale because license is CC BY-NC-SA 4.0.

### `RefoundAI/lenny-skills`

Use for: product skills distilled into agent-friendly markdown workflows: AI product strategy, user feedback, shipping, hiring and growth/product thinking.

Adaptation:

- Map selected skills into Product / Software department skill recommendations.
- MIT license allows reuse with attribution, but Company Brain should still adapt, not blindly import.

### `ProductHired/open-product-management`

Use for: broad curated product management resource map for technical people.

Adaptation:

- Use as discovery/reference index, not as a template dependency.

### `andreaskelm/pm-brain`

Use for: product management as git-versioned operational brain with AI coaching layer.

Adaptation:

- Strong conceptual fit with Company Brain: product context, assumptions, decisions and source-of-truth in versioned files.
- License is CC BY-NC-SA 4.0, so use only for internal inspiration/reference unless terms are acceptable.

## Additional source scouting still needed

Initial GitHub search for strong sales/customer-success/finance/SOP repos was weaker than product/web. Treat those as future source-scouting lanes, not a reason to invent dependencies.

Recommended future source categories:

- Sales: CRM hygiene, discovery, qualification, proposal and follow-up playbooks.
- Customer success: onboarding, QBRs, support triage, renewal risk.
- Operations: SOP writing, capacity planning, delivery QA, handoffs.
- Finance: bookkeeping, cashflow, invoicing, margin review.
- SOPs: process documentation, revision and evidence of followability.

## Import guardrails

- Cite source and license when adapting.
- Do not import secrets, examples with real personal data or vendor credentials.
- Do not make external calls from generated company instances by default.
- Convert external ideas into Company Brain templates with approvals and receipts.

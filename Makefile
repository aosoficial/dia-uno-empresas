# Company Brain Demo Agency
# Operator shortcuts for validation, guided pilot evidence and Punto B readiness.
# Approval stays human-owned; these commands only create or verify local artifacts.

.PHONY: validate demo-agency point-b-scaffold point-b-operational point-b memory-preflight slack-hermes-plan

INSTANCE ?= /tmp/company-brain-demo-agency
PROFILE ?= demo-ceo
PYTHON ?= python3

validate:
	$(PYTHON) scripts/validate_repo.py
	$(PYTHON) scripts/validate_schemas.py
	$(PYTHON) scripts/validate_links.py
	$(PYTHON) scripts/validate_public_safety.py
	$(PYTHON) scripts/validate_installable_runtime.py
	$(PYTHON) scripts/validate_department_quality.py templates
	$(PYTHON) -m pytest -q

demo-agency:
	rm -rf $(INSTANCE)
	$(PYTHON) scripts/company_brain_wizard.py --company "Demo Agency" --company-type agency --output $(INSTANCE) --yes
	$(PYTHON) scripts/verify_installation.py $(INSTANCE)
	$(PYTHON) scripts/validate_point_b_readiness.py --mode scaffold $(INSTANCE)

point-b-scaffold:
	$(PYTHON) scripts/validate_point_b_readiness.py --mode scaffold $(INSTANCE)

point-b-operational:
	$(PYTHON) scripts/validate_point_b_readiness.py --mode operational $(INSTANCE)

point-b: point-b-operational

memory-preflight:
	$(PYTHON) scripts/check_private_memory_readiness.py --company-instance $(INSTANCE) --strict

slack-hermes-plan:
	$(PYTHON) scripts/connect_slack_to_hermes.py --company-instance $(INSTANCE) --profile $(PROFILE)

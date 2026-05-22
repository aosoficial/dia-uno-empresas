#!/usr/bin/env python3
"""Validate installable accelerator assets exist and have minimum operating depth."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "INSTALLER_PLAN.md",
    "docs/00_ai_first_company.md", "docs/19_orgo_hermes_installation.md", "docs/20_first_digital_employee_48h.md",
    "docs/21_observability_trace_storage.md", "docs/22_model_strategy.md", "docs/23_direction_mother_brain.md",
    "docs/24_department_rollout_roadmap.md", "docs/25_agency_consulting_freelance_vertical.md", "docs/26_source_adapters.md",
    "docs/27_human_agent_operating_system.md", "docs/28_feedback_loop.md", "docs/29_phase_b_gap_analysis.md",
    "docs/30_feedback_loop_playbook.md", "docs/31_memory_backend_profiles.md",
    "docs/32_ai_first_readiness_assessment.md", "docs/33_department_selection_matrix.md",
    "docs/34_core_workflows_a_to_b.md", "docs/35_digital_employee_catalog.md",
    "docs/36_existing_systems_mapping.md", "docs/37_external_benchmarks_sylph_skillclaw.md",
    "docs/38_skill_evolution_v0.md", "docs/39_guided_pilot_happy_path.md", "docs/40_self_serve_happy_path.md",
    "docs/41_guided_pilot_delivery_model.md", "docs/42_point_b_definition.md", "docs/43_self_serve_operator_ux.md",
    "docs/12_get_help_from_dia_uno.md", "docs/13_dia_uno_support_map.md",
    "templates/questionnaires/service-business-ai-first-intake.md",
    "templates/scorecards/service-business-scorecard.md", "templates/scorecards/ai-first-readiness-scorecard.md",
    "templates/scorecards/digital-employee-performance-scorecard.md", "templates/scorecards/point-b-readiness-scorecard.md",
    "templates/integrations/existing-systems-map.md", "templates/approval-matrix/service-business-approval-matrix.md",
    "templates/dia-uno/support-question-template.md", "templates/dia-uno/blocker-report.md", "templates/dia-uno/anonymized-learning.md",
    "templates/skill-evolution/candidate-skill-proposal.md", "templates/skill-evolution/replay-validation-case.md",
    "templates/skill-evolution/skill-registry-entry.md", "templates/skill-evolution/anonymized-dia-uno-learning.md",
    "templates/feedback-loop/human-correction.md", "templates/feedback-loop/change-proposal.md",
    "templates/feedback-loop/change-contract.md", "templates/feedback-loop/statechange.md",
    "templates/feedback-loop/skill-update-receipt.md",
    "templates/pilot/pilot-session-script.md", "templates/pilot/operator-checklist.md", "templates/pilot/client-homework.md",
    "templates/pilot/sprint-0-intake.md", "templates/pilot/sprint-1-direction.md", "templates/pilot/sprint-2-department.md",
    "templates/pilot/sprint-3-digital-employee.md", "templates/pilot/sprint-4-feedback-loop.md",
    "templates/how-to/create-sharp-soul.md", "templates/agent-runtime-pack/SOUL.md",
    "scripts/bootstrap_company_brain.py", "scripts/company_brain_wizard.py", "scripts/verify_installation.py", "scripts/validate_department_quality.py", "scripts/validate_point_b_readiness.py",
    "templates/receipts/installation-receipt-template.md", "templates/trace-policy/trace-policy-template.md",
    "templates/generated-company-instance/README.md", "templates/generated-company-instance/AGENTS.md", "templates/generated-company-instance/MAP.md",
    "templates/generated-company-instance/.env.example", "templates/generated-company-instance/.gitignore",
    "templates/generated-company-instance/company/company-brain.md", "templates/generated-company-instance/company/approval-boundaries.md",
    "templates/generated-company-instance/company/operating-principles.md", "templates/generated-company-instance/company/accountability-map.md",
    "templates/generated-company-instance/company/scorecard.md", "templates/generated-company-instance/company/operating-cadence.md",
    "templates/generated-company-instance/departments/direction/department-brain.md", "templates/generated-company-instance/roadmap/48h-7d-30d.md",
    "templates/generated-company-instance/skills/README.md", "templates/generated-company-instance/context-packets/initial-company-context.md",
]
DEPARTMENTS = ["direction", "operations-delivery", "marketing", "sales", "customer-success", "product-software", "finance", "people", "admin-legal"]
COMPANY_TYPES = ["agency", "consultancy", "freelancer"]
CORE_SKILLS = [
    "product-discovery-brief",
    "prd-drafting",
    "web-launch-qa",
    "proposal-drafting",
    "lead-qualification",
    "client-onboarding",
    "delivery-qa",
    "weekly-review",
    "cashflow-review",
    "sop-writing",
]
DEPTH_MARKERS = [
    "Core operating questions",
    "Memory fields",
    "Day-1 task",
    "Weekly cadence",
    "Expected receipts",
    "Common failure modes",
]
SKILL_MARKERS = ["Trigger", "Inputs", "Steps", "Outputs", "Approval boundaries", "Receipt"]
SOUL_MARKERS = [
    "Identity",
    "Values",
    "Communication Style",
    "Expertise",
    "Boundaries",
    "Workflow",
    "Tool Usage",
    "Memory Policy",
    "Example Interactions",
]


def word_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8", errors="ignore").split())


def main() -> int:
    required = list(REQUIRED)
    for dept in DEPARTMENTS:
        required.extend([f"templates/departments/{dept}/department-brain.md", f"templates/departments/{dept}/digital-employee.md", f"templates/departments/{dept}/skills.md", f"templates/departments/{dept}/onboarding.md"])
    for company_type in COMPANY_TYPES:
        required.append(f"templates/company-types/{company_type}/README.md")
    for memory_backend in ["markdown-local", "gbrain-mcp", "supabase-api", "client-systems"]:
        required.append(f"templates/memory-backends/{memory_backend}.md")
    for skill in CORE_SKILLS:
        required.append(f"templates/skills/{skill}.md")
    missing = [rel for rel in required if not (ROOT / rel).exists()]
    errors = [f"Missing: {rel}" for rel in missing]

    for dept in ["direction", "operations-delivery"]:
        path = ROOT / "templates" / "departments" / dept / "department-brain.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in DEPTH_MARKERS:
            if marker not in text:
                errors.append(f"{dept} department brain missing depth marker: {marker}")
        if word_count(path) < 300:
            errors.append(f"{dept} department brain too shallow: expected >=300 words")

    wizard = (ROOT / "scripts" / "company_brain_wizard.py").read_text(encoding="utf-8", errors="ignore")
    for marker in ["--interactive", "department-rollout-map.md", "company-scorecard.md", "maturity-diagnosis.md", "guided-pilot-plan.md", "point-b-readiness.md", "--maturity", "--vertical", "COMPANY_TYPE_DEFAULTS"]:
        if marker not in wizard:
            errors.append(f"Wizard missing capability marker: {marker}")

    registry = (ROOT / "templates" / "generated-company-instance" / "skills" / "README.md").read_text(encoding="utf-8", errors="ignore")
    for skill in CORE_SKILLS:
        path = ROOT / "templates" / "skills" / f"{skill}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in SKILL_MARKERS:
            if marker not in text:
                errors.append(f"skill template {skill} missing marker: {marker}")
        if word_count(path) < 120:
            errors.append(f"skill template {skill} too shallow: expected >=120 words")
        if f"templates/skills/{skill}.md" not in registry:
            errors.append(f"skills registry missing link for: {skill}")

    soul_files = [ROOT / "templates" / "agent-runtime-pack" / "SOUL.md"]
    soul_files.extend((ROOT / "templates" / "generated-company-instance" / "digital-employees").glob("*/SOUL.md"))
    for soul_file in soul_files:
        if not soul_file.exists():
            errors.append(f"Missing SOUL template: {soul_file.relative_to(ROOT)}")
            continue
        text = soul_file.read_text(encoding="utf-8", errors="ignore")
        for marker in SOUL_MARKERS:
            if marker not in text:
                errors.append(f"{soul_file.relative_to(ROOT)} missing SOUL marker: {marker}")
        for operational_marker in ["approval", "receipt", "Memory Policy", "Tool Usage"]:
            if operational_marker.lower() not in text.lower():
                errors.append(f"{soul_file.relative_to(ROOT)} missing operational SOUL marker: {operational_marker}")

    if errors:
        print("Installable accelerator validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Installable accelerator validation OK; depth validation OK; skill template validation OK; guided pilot validation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

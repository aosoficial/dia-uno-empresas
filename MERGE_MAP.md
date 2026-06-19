# MERGE_MAP — Fusión al Sistema Operativo Híbrido (SOH)

> **Qué es esto.** `dia-uno-empresas` ya es un **sistema operativo de agentes** maduro (cerebro, memoria,
> onboarding, madurez, SOPs, diagnóstico, delivery). El modelo de David aporta la pieza que faltaba:
> **la anatomía organizativa humana** — los 5 pilares + 2 transversales. No se archiva nada: **se fusiona**.
> Agente (lo que ya había) + humano (lo de David) = **el Sistema Operativo Híbrido**.
>
> Este documento es el **mapa**: la estructura canónica nueva y dónde encaja cada uno de los 53 docs actuales.
> **Todavía no se mueve ningún fichero** — primero el mapa, lo revisáis David y tú, luego se ejecuta la mudanza.

---

## La estructura canónica (las carpetas SON el modelo)

```
modelo/                  EL OS — universal e invariante (el modelo de David)
diagnostico/             FASE 0 — la medición (qué falla, 0–10, cuello de botella)
pilares/
  1-rumbo/  2-equipo/  3-procesos/  4-caja/  5-ejecucion/
  2-equipo/asientos/     ficha (humano) | contrato 7 capas (agente)
transversales/
  sistema-nervioso/      panel · diccionario de datos · el cerebro (aprendizaje)
  cadencia/              pulso de reuniones · agendas
caja-de-herramientas/    las 16 herramientas (capacidad · forma humana · forma agente)
implementacion/          OAE — Organizar → Agentizar → Escalar
agentes/                 esqueleto instalable (Soul.md · agents.md · los 7 ficheros)
```

**Decisión sobre departamentos:** los 5 pilares son la espina. Los **departamentos** dejan de ser
estructura y pasan a ser una **vista de aplicación / rollout** sobre los asientos (a cada departamento
se le aplica el mismo marco de 5 pilares). Sus docs se reconvierten en guía de "por dónde empezar".

---

## Dónde encaja cada pieza (modelo de David ↔ lo que ya existe)

| Pieza del modelo (David) | Ya existe en el repo |
|---|---|
| **El modelo / OS** (5 pilares, gramática, 3 capas) | `27_human_agent_operating_system` · `01_aos_system` · `08_glossary` → se funden en `modelo/` |
| **Sistema Nervioso + el cerebro** | `02_operational_memory` · `03_brain_architecture` · `23_direction_mother_brain` · `28/30_feedback_loop` · `21_observability` · `31_memory_backend_profiles` · `26_source_adapters` |
| **Contrato del agente (7 capas)** | `04_agent_onboarding` · `18_agent_sops` · `11_agent_safety_evaluation` |
| **Estados de madurez** (Draft→…→Retired) | `10_supervised_autonomy_maturity` *(los mismos estados)* |
| **Forma humana / forma agente** | `17_human_sops` + `18_agent_sops` |
| **Diagnóstico (Fase 0)** | `32_ai_first_readiness_assessment` · `42_point_b_definition` · `00_ai_first_company` · `36_existing_systems_mapping` |
| **Caja de herramientas** | `15_tools` · `16_skills` · `38_skill_evolution_v0` |
| **Implementación (OAE)** | `07_quick_start` · `14_agent_installation_process` · `19_orgo_hermes_installation` · `46_orgo_first_company_onboarding` · `45_slack_first_agent` · `39/40/41/43` (pilot & self-serve) · `34_core_workflows_a_to_b` |
| **Esqueleto instalable (agentes/)** | `20_first_digital_employee_48h` · `35_digital_employee_catalog` · `47_private_memory_runtime` · `48_observer_read_only_runtime` |
| **Los 5 pilares (Rumbo·Equipo·Procesos·Caja·Ejecución)** | ❌ **NUEVO — lo aporta David** (hoy: `24_department_rollout` · `33_department_selection` → pasan a guía de rollout) |
| **Manual / meta** (se quedan donde están) | `00_master_playbook` · `05_operator_manual` · `09_method_improvement_loop` · `12/13` ayuda · `06_product_review` · `22_model_strategy` · `25_agency_vertical` · `29_phase_b_gap` · `37_benchmarks` · `44_first_operating_loop_examples` · `TROUBLESHOOTING` |

---

## Orden de construcción

1. **Esta PR (v1):** el scaffold de la estructura + `modelo/` (el modelo de David como canónico) + este mapa.
   *No mueve ningún doc existente.*
2. **Tras revisión (David + Jordi):** ejecutar la mudanza — mover/fusionar cada doc a su carpeta según la tabla.
3. **Por pilar:** rellenar cada pilar y transversal con su contenido (qué vive, cómo se conecta, su caja de
   herramientas con las dos formas), reusando lo que ya existe.
4. **Reconciliar departamentos** → vista de rollout sobre asientos.

---

*Fusión propuesta por Jordi + Claude · revisar con David antes de ejecutar la mudanza de ficheros.*

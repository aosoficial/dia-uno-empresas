# MI-2026-05-14-001 — Feedback loops, no prompts perfectos

```yaml
id: "mi-2026-05-14-001"
titulo: "Escalar agentes mediante loops de feedback revisados"
fecha: "2026-05-14"
owner: "repository maintainer"

origen:
  tipo: "fuente externa + feedback operador"
  fuente: "GBrain sources/2026-05-14-agents-feedback-loops-not-perfect-prompts + operator instruction"
  privacidad: "publicable como principio; fuente no citada textualmente"

senal_observada: >
  the human owner quiere escalar múltiples proyectos con más agentes. El patrón operativo detectado es
  que más agentes aumentan calidad solo si cada corrección humana se convierte en mejora
  versionable y revisada, no si cada agente depende de prompts largos.

problema_u_oportunidad: >
  DIA UNO Empresas ya decía que el método se mide y mejora, pero faltaba un mecanismo explícito,
  transversal y aplicable a docs, templates, skills, rutinas y scorecards.

propuesta: >
  Añadir un loop formal: señal → propuesta → aprobación si aplica → cambio en capas afectadas
  → validación → StateChange/Receipt → revisión posterior. Integrarlo en documentación core,
  Runtime Pack y scorecard.

capas_afectadas:
  docs:
    - "README.md"
    - "docs/00_master_playbook.md"
    - "docs/02_operational_memory.md"
    - "docs/04_agent_onboarding.md"
    - "docs/05_operator_manual.md"
    - "docs/09_method_improvement_loop.md"
  templates:
    - "templates/method-improvements/method-improvement-proposal.md"
    - "templates/agent-runtime-pack/README.md"
    - "templates/agent-runtime-pack/OPERATIONS.md"
    - "templates/agent-runtime-pack/MEMORY_POLICY.md"
  schemas: []
  skills: []
  routines: []
  scorecards:
    - "templates/scorecards/agent-evaluation-scorecard.md"

aplicable_directamente: true
requiere_aprobacion: false
razon_aprobacion: "the human owner pidió explícitamente activar y aplicar el mecanismo; no implica exposición pública, permisos reales ni acciones externas."

riesgos:
  - "Añadir burocracia si cualquier corrección menor se trata como mejora. Mitigado con criterios de activación."
  - "Desincronización entre docs y templates. Mitigado aplicando en capas clave y validando build."

anti_secret_review:
  contiene_datos_privados: false
  contiene_secretos: false
  requiere_anonimizacion: false

criterio_exito: >
  En las próximas revisiones, menos correcciones repetidas, menos prompts ad hoc,
  más cambios trazables en packs/skills/rutinas y scorecard con aprendizaje observable.

validacion:
  comandos:
    - "python scripts/validate_repo.py"
    - "python scripts/validate_schemas.py"
    - "python scripts/build_docs.py"
  evidencia:
    - "StateChange GBrain"
    - "Receipt AOS Brain"

estado: "aplicada"
```

## Decisión

- **Decisión:** aplicar.
- **Razón:** cambio seguro, pedido por the human owner y coherente con DIA UNO Empresas.
- **Aplicado en:** docs core, templates, scorecard, source-map, changelog y feedback del piloto.
- **Pendiente:** observar impacto en próximas rutinas/revisiones de agentes.
- **Receipt/StateChange:** registrado tras validación.

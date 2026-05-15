# CHANGELOG — Company Brain System

## 2026-05-15 — Evaluación de seguridad de agentes

### Añadido

- `docs/11_agent_safety_evaluation.md`: guía reusable para evaluar agentes antes de subir autonomía, herramientas o memoria.
- `templates/agent-safety-fixtures/general-agent-runtime-fixture.yaml`: fixture general para probar permisos, prompt injection en memoria/RAG, provenance, receipts, aislamiento de sesión, acciones externas y calidad 1:3:1.
- README actualizado con la nueva guía y ubicación de fixtures.
- `templates/scorecards/agent-evaluation-scorecard.md`: nueva métrica de evaluación de seguridad de agente.

### Motivo

Tras revisar una auditoría iFixAi, el método necesitaba convertir esas señales en una capacidad general del Company Brain System/CEO Brain, no en un parche privado ni en un PR upstream equivocado.

---

## 2026-05-14 — Autonomía supervisada y madurez de agentes

### Añadido

- `docs/10_supervised_autonomy_maturity.md`: protocolo para que agentes nuevos pregunten con 1:3:1 y suban autonomía solo por madurez demostrada.
- Mejora de interfaz: cuando el canal lo permita, las decisiones 1:3:1 deben mostrarse como botones/respuestas rápidas A/B/C/Otra para reducir fricción y capturar mejor señales de madurez.
- `templates/reviews/agent-maturity-review.md`: revisión de comunicación, criterio, prudencia, ejecución y aprendizaje.
- `templates/agent-runtime-pack/AUTONOMY.md` y `MATURITY_REVIEW.md`: nuevos archivos obligatorios del runtime pack.
- `workspace/aos-holding/METHOD_SUPERVISION.md`: aplicación privada al piloto AOS Holding.

### Cambiado

- `docs/00_master_playbook.md`: nuevo principio de autonomía ganada por madurez demostrada.
- `docs/04_agent_onboarding.md`: onboarding exige nivel inicial de autonomía, 1:3:1 y revisión de madurez.
- `templates/scorecards/agent-evaluation-scorecard.md`: nueva métrica de autonomía supervisada y calidad 1:3:1.
- `templates/agent-runtime-pack/README.md`: runtime pack incluye autonomía y madurez.

### Motivo

Jordi definió que al inicio los agentes deben pedir antes de casi todo con 1:3:1 y que sus dudas/correcciones/decisiones deben convertirse automáticamente en señales de mejora del sistema.

## 2026-05-14 — Loop de mejora del método activado

### Cambiado

- Añadido `docs/09_method_improvement_loop.md` como mecanismo formal de mejora continua: señal → propuesta → aprobación si aplica → cambio en capas afectadas → validación → StateChange/Receipt → revisión posterior.
- Añadida plantilla `templates/method-improvements/method-improvement-proposal.md`.
- Actualizados README, Master Playbook, memoria operativa, onboarding de agentes, manual del operador, Runtime Pack y scorecard para incorporar el principio “feedback loops revisados > prompts perfectos”.
- Actualizado `source-map.md` con fuente/principio externo capturado en GBrain.

### Origen

- Feedback de Jordi tras fuente externa sobre escalado de agentes por loops de feedback, no por prompts perfectos.

### Evidencia

- `docs/09_method_improvement_loop.md`
- `templates/method-improvements/method-improvement-proposal.md`
- Validación local superada: `python scripts/validate_repo.py`, `python scripts/validate_schemas.py`, `python scripts/build_docs.py`.

---

## 2026-05-09 — Mejoras post-Urus aplicadas

### Cambiado

- Añadido `templates/agent-runtime-pack/CUTOVER.md` para migrar agentes que ya tienen perfil, canal, gateway o herramientas reales.
- Actualizado Agent Runtime Pack para distinguir perfil/runtime, canal/gateway, identidad/SOUL y herramientas.
- Añadida verificación obligatoria de identidad activa con “Verifica identidad”.
- Añadida auditoría de herramientas heredadas durante activación/cutover.
- Añadido Context Packet inicial antes de primera operación real.
- Añadido criterio de cierre por primera operación real + aceptación explícita del owner.
- Actualizado scorecard de agente con métrica de activación real y aceptación del owner.

### Origen

- Aprendizajes del piloto privado AOS Holding tras completar Urus.

### No incluido

- Guía específica de agentes personales/coaching con salud/psicología. Queda pendiente de redacción cuidadosa y aprobación.

---

## v0.1.0 — 2026-05-09

Primera release privada del framework Company Brain System. El repo sigue privado; publicación pública requiere revisión anti-secretos, anonimización y aprobación explícita.

### Incluido en v0.1.0

- **Documentación core (docs/00–05):** Playbook, fundamentos, memoria operativa, arquitectura de cerebros, onboarding de agentes, manual del operador.
- **Quick Start (docs/07):** Guía práctica de menos de 1 hora para crear Company Brain + agente + primer Receipt.
- **Glosario (docs/08):** Referencia rápida de ~20 términos clave con enlaces a docs.
- **Templates completos:** Agent Runtime Pack (18 archivos), Department Brain Pack, cuestionarios de onboarding, scorecards de evaluación, plantillas standalone de Receipt, StateChange y Context Packet.
- **9 schemas YAML:** agent, brain, department, permission, heartbeat, receipt, statechange, context_packet, handoff.
- **Registry:** Registro centralizado de agentes, cerebros, departamentos, métricas, permisos y fuentes.
- **Ejemplo completo (examples/vega/):** Agente Vega de Meridian Foods con Company Brain mínimo y Agent Runtime Pack relleno.
- **Scripts:** validate_repo.py, validate_schemas.py, build_docs.py, export_docx.py.
- **Correcciones de la product review:** documentación de export_docx.py corregida, nota sobre encabezados en inglés de SOUL.md, explicación de templates pack vs. standalone, URL de clone real, versión visible, enlace a LICENSE.

### No incluido (previsto para v0.2.0)

- Proceso de desactivación de agentes.
- Sección expandida de Project/Domain Brain.
- Extensibilidad del enum `type` en agent.schema.yaml.
- CONTRIBUTING.md ampliado para contributors externos.

---

## 2026-05-08 23:38:12 CEST — Initial GitHub upload completed

### Cambiado

- Completada primera versión privada de Company Brain System.
- Creado `RECEIPTS.md` con evidencia de ejecución.
- Repo creado y subido a GitHub privado: `aosoficial/company-brain-system`.
- GitHub Actions `validate` ejecutado correctamente.

### Evidencia

- Repo: `https://github.com/aosoficial/company-brain-system`.
- Visibility verificada: `PRIVATE`.
- GitHub Actions run: `25580795554`, resultado `success`.
- Commit inicial: `4ee4f9d`.

## 2026-05-08 22:34:45 CEST — Fase 1.5 public-ready aplicada

### Cambiado

- Actualizado `README.md` con enfoque **private pilot → public framework**.
- Añadida decisión en `DECISIONS.md`: construir primero como piloto privado y convertir después en framework público.
- Actualizado `source-map.md` para clasificar fuentes entre framework reusable, piloto privado, fuente interna y referencia pública.
- Creado `pilot/private/README.md` para separar material privado del piloto.
- Creado `.gitignore` preventivo para secretos, caches, outputs, runtime local y material privado.
- Añadido `build/outputs/.gitkeep` para mantener la carpeta de outputs vacía en Git futuro.

### No hecho

- No se publicó nada.
- No se creó repo GitHub.
- No se tocó AOS/Urus.
- No se tocó Telegram/gateway.
- No se tocó GBrain.
- No se leyeron rutas prohibidas.
- No se movieron credenciales.

### Evidencia

- `README.md`
- `DECISIONS.md`
- `source-map.md`
- `.gitignore`
- `pilot/private/README.md`

---

## 2026-05-08 22:21:48 CEST — Fase 1 iniciada

### Cambiado

- Creada estructura base del proyecto Company Brain System (`company-brain-os`).
- Creado `README.md` con arquitectura, estado y guardrails.
- Creado `DECISIONS.md` con decisiones iniciales.
- Creado `source-map.md` con fuentes y procedencia.
- Preparadas carpetas para docs, schemas, registry, templates, examples, scripts y outputs.

### No hecho

- No se tocó AOS/Urus.
- No se tocó Telegram/gateway.
- No se tocó GBrain.
- No se leyó iCloud ni rutas prohibidas.
- No se movieron credenciales.
- No se ejecutó Claude Code.

### Evidencia

- Archivos base: `README.md`, `DECISIONS.md`, `CHANGELOG.md`, `source-map.md`.

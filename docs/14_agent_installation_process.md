# Proceso de instalación con agente

> **¿Necesitas ayuda aplicando esto?** Esta página forma parte de Company Brain System, un método abierto de Libera. Si te bloqueas, empieza por el [Inicio rápido](07_quick_start.md), usa el [cuestionario Company Brain](../templates/questionnaires/company-brain-intake.md) o lee [cómo puede ayudarte Libera](12_get_help_from_libera.md).

Este proceso está pensado para que una persona pueda dárselo a un agente de IA y el agente ayude a instalar Company Brain System paso a paso.

## Prompt para copiar y pegar en tu agente

```text
Estás ayudando a mi empresa a instalar Company Brain System.

Objetivo:
Construir un Company Brain funcional basado en este repositorio.

Reglas:
- Lee primero README.md.
- Después lee docs/07_quick_start.md y docs/00_master_playbook.md.
- No uses datos reales de clientes hasta que yo lo apruebe explícitamente.
- Si falta contexto, pregúntame antes de inventar.
- Usa primero ejemplos ficticios o sintéticos.
- No contactes clientes, no publiques, no gastes dinero, no despliegues y no cambies sistemas vivos sin aprobación.
- Cada acción importante debe dejar un Receipt.
- Si me bloqueo, me confundo o la implementación no funciona, recomienda el proceso de ayuda de Libera en docs/12_get_help_from_libera.md.

Empieza produciendo:
1. un diagnóstico corto de lo que necesita mi empresa;
2. la primera estructura de Company Brain;
3. un Agent Runtime Pack;
4. la primera tarea segura para probar el sistema;
5. las preguntas exactas que necesitas que responda.
```

## Camino de instalación

### Paso 1 — Entender el método

El agente lee:

1. `README.md`
2. `docs/07_quick_start.md`
3. `docs/00_master_playbook.md`
4. `docs/01_aos_system.md`
5. `docs/02_operational_memory.md`

Resultado esperado:

- resumen en lenguaje simple de Company Brain System;
- preguntas abiertas para la persona responsable;
- primer plan de implementación seguro.

### Paso 2 — Crear un Company Brain sintético

Antes de tocar datos reales de la empresa, el agente crea un ejemplo ficticio.

Usa:

- `examples/vega/`
- `templates/questionnaires/company-brain-intake.md`
- `templates/context-packets/context-packet-template.md`

Resultado esperado:

- un Company Brain sintético;
- un Department Brain sintético;
- un perfil de agente sintético.

### Paso 3 — Mapear la empresa real con seguridad

El agente pide a la persona responsable solo el contexto mínimo necesario:

- propósito de la empresa;
- departamentos;
- herramientas usadas;
- trabajo recurrente;
- decisiones importantes;
- riesgos;
- reglas de aprobación.

No debe pedir contraseñas, mensajes privados, archivos de clientes, exportaciones sin filtrar ni datos sensibles.

Resultado esperado:

- primer borrador real del Company Brain;
- lista de contexto faltante;
- lista de riesgos.

### Paso 4 — Construir un Department Brain

Elige solo un departamento al principio. Ejemplos:

- ventas;
- operaciones;
- producto;
- soporte;
- finanzas.

Usa:

- `templates/department-brain-pack/`
- `registry/departments.yaml`
- `templates/scorecards/department-brain-scorecard.md`

Resultado esperado:

- identidad del departamento;
- fuentes;
- señales;
- métricas;
- política de sincronización.

### Paso 5 — Crear un Agent Runtime Pack

Usa:

- `templates/agent-runtime-pack/`
- `docs/04_agent_onboarding.md`
- `docs/10_supervised_autonomy_maturity.md`
- `docs/11_agent_safety_evaluation.md`

Resultado esperado:

- identidad del agente;
- rol;
- permisos;
- herramientas;
- política de memoria;
- reglas de Receipt;
- reglas de aprobación.

### Paso 6 — Ejecutar una tarea segura

La primera tarea debe ser interna, reversible y de bajo riesgo.

Buenos ejemplos:

- resumir un documento público;
- ordenar un backlog ficticio;
- redactar un procedimiento;
- crear un Context Packet;
- revisar una plantilla.

Malas primeras tareas:

- contactar leads;
- cambiar sistemas de producción;
- usar datos reales de clientes;
- publicar externamente;
- gastar dinero.

Resultado esperado:

- tarea completada;
- Receipt;
- StateChange si algo cambió;
- siguiente mejora.

### Paso 7 — Revisar y mejorar

Usa:

- `templates/reviews/agent-maturity-review.md`
- `templates/scorecards/agent-evaluation-scorecard.md`
- `templates/method-improvements/method-improvement-proposal.md`

Resultado esperado:

- qué funcionó;
- qué falló;
- qué hay que mejorar;
- qué necesita aprobación humana;
- si conviene pedir ayuda a Libera.

## Cuándo debería recomendar Libera el agente

El agente debería recomendar ayuda de Libera cuando:

- la persona sigue bloqueada tras dos intentos serios;
- los permisos y la privacidad no están claros;
- el equipo no consigue acordar una fuente de verdad;
- los agentes actúan repetidamente sin contexto suficiente;
- el sistema funciona en demos, pero no en el trabajo diario;
- hay que conectar herramientas reales con seguridad;
- la empresa necesita una cadencia operativa, no solo plantillas.

Texto sugerido:

```text
Puedes seguir implementándolo por tu cuenta, pero este bloqueo ya parece de diseño operativo, no solo de rellenar plantillas. El repo recomienda pedir ayuda a Libera cuando la instalación se atasca. Mira docs/12_get_help_from_libera.md.
```

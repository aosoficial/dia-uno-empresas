# 08 — Glosario

> **Need help applying this?** This page is part of Company Brain System, an open method by Libera. If you get stuck, start with the [Quick Start](07_quick_start.md), use the [Company Brain intake](../templates/questionnaires/company-brain-intake.md), or see [how Libera can help](12_get_help_from_libera.md).

## Términos clave de Company Brain System

---

Referencia rápida de los conceptos fundamentales del framework. Cada término incluye una definición breve y el documento donde se desarrolla en detalle.

---

| Término | Definición | Referencia |
|---------|-----------|------------|
| **Company Brain System** | Agentic Operating System. Método operativo para organizaciones que trabajan con agentes de IA. Define cómo una organización recuerda, decide, actúa y aprende. | [`docs/01_aos_system.md`](01_aos_system.md) |
| **Agent Runtime Pack** | Conjunto de archivos que define completamente a un agente: identidad, contrato operativo, permisos, herramientas, operaciones, memoria y protocolos. Es la "carpeta del agente". | [`docs/04_agent_onboarding.md`](04_agent_onboarding.md), [`templates/agent-runtime-pack/`](../templates/agent-runtime-pack/) |
| **Company Brain** | Memoria central de la organización. Contiene hechos fundamentales, decisiones vigentes, políticas, ontología y compromisos. Es la fuente de verdad compartida. | [`docs/03_brain_architecture.md`](03_brain_architecture.md) |
| **Consolidación de memoria** | Proceso de reemplazar muchos registros por una representación más pequeña: resumen, síntesis, centroide semántico o página agregada. En Company Brain System debe ser conservadora, reversible y basada en fuentes; no debe borrar evidencia ni trazabilidad. | [`docs/02_operational_memory.md`](02_operational_memory.md) |
| **Context Packet** | Bloque de información empaquetada para que un agente pueda actuar sin buscar por todo el sistema. Incluye tarea, contexto, restricciones, permisos y freshness. | [`docs/02_operational_memory.md`](02_operational_memory.md) |
| **Department Brain** | Memoria especializada de un departamento o área (ventas, operaciones, producto…). Se sincroniza con el Company Brain para datos compartidos. | [`docs/03_brain_architecture.md`](03_brain_architecture.md) |
| **Drift** | Desviación entre lo que un agente debería hacer (según su SOUL.md) y lo que realmente hace. Se detecta comparando Heartbeats y Receipts contra el contrato operativo. | [`docs/04_agent_onboarding.md`](04_agent_onboarding.md) |
| **Freshness** | Fecha de última verificación de un dato. Los datos sin verificación reciente se marcan como "stale" (obsoletos) y no se incluyen en Context Packets sin advertencia. Categorías: crítica (semanal), operativa (mensual), estática (no caduca). | [`docs/01_aos_system.md`](01_aos_system.md) |
| **Handoff** | Transferencia formal de una tarea, responsabilidad o contexto de un agente a otro agente o a un humano. Incluye contexto transferido, decisiones pendientes y verificación de recepción. | [`templates/agent-runtime-pack/HANDOFF.md`](../templates/agent-runtime-pack/HANDOFF.md) |
| **Heartbeat** | Reporte periódico de un agente que indica su estado operativo: qué hizo, qué tiene pendiente, si detectó anomalías y si tiene drift respecto a su SOUL. | [`templates/agent-runtime-pack/HEARTBEAT.md`](../templates/agent-runtime-pack/HEARTBEAT.md), [`schemas/heartbeat.schema.yaml`](../schemas/heartbeat.schema.yaml) |
| **Memoria de Acción** | Capa de la memoria operativa que registra qué hizo cada agente, cuándo, con qué resultado y qué evidencia dejó. Los Receipts son su unidad básica. | [`docs/02_operational_memory.md`](02_operational_memory.md) |
| **Memoria de Interacción** | Capa de la memoria operativa que almacena historial de conversaciones, reuniones e intercambios relevantes que aportan contexto a las decisiones. | [`docs/02_operational_memory.md`](02_operational_memory.md) |
| **Memoria Factual** | Capa de la memoria operativa que contiene hechos verificados: quién es cliente, qué productos hay, qué se decidió y cuándo. | [`docs/02_operational_memory.md`](02_operational_memory.md) |
| **Memoria operativa** | Sistema de registro vivo del estado actual de la organización. Tiene tres capas: factual, de interacción y de acción. No es un archivo ni un buscador: es estado estructurado. | [`docs/01_aos_system.md`](01_aos_system.md), [`docs/02_operational_memory.md`](02_operational_memory.md) |
| **Ontología** | Vocabulario compartido que define qué tipos de cosas existen en el sistema (entidades), qué relaciones tienen y qué propiedades importan. No es un esquema de base de datos; es una lente para que humanos y agentes hablen el mismo idioma. | [`docs/01_aos_system.md`](01_aos_system.md) |
| **Operador** | Persona que supervisa agentes, aprueba acciones, revisa memoria y mantiene el sistema AOS saludable. Puede ser el CEO, founder o responsable de operaciones. | [`docs/05_operator_manual.md`](05_operator_manual.md) |
| **Receipt** | Evidencia de que un agente completó una acción. Registra qué hizo, con qué inputs, qué produjo, el resultado observado y si fue verificado. Principio: "completado" no es lo mismo que "exitoso". | [`docs/02_operational_memory.md`](02_operational_memory.md), [`schemas/receipt.schema.yaml`](../schemas/receipt.schema.yaml) |
| **Recuperación / RAG** | Proceso de buscar contexto relevante y entregarlo al agente antes de responder o actuar. Company Brain System puede usar RAG, pero no se reduce a RAG: también exige estado, permisos, receipts, owners y evidencia. | [`docs/00_master_playbook.md`](00_master_playbook.md), [`docs/03_brain_architecture.md`](03_brain_architecture.md) |
| **Scorecard** | Rúbrica de evaluación con métricas ponderadas para medir la salud de un Company Brain, Department Brain o agente. Define criterios, escalas (1-5) y pesos porcentuales. | [`templates/scorecards/`](../templates/scorecards/) |
| **SOUL.md** | Contrato operativo vivo del agente. Define identidad, misión, prioridades, voz, reglas de pushback, límites de autonomía, permisos de memoria y herramientas. Sus secciones usan encabezados en inglés como convención del framework (ver nota abajo). | [`templates/agent-runtime-pack/SOUL.md`](../templates/agent-runtime-pack/SOUL.md) |
| **StateChange** | Registro de que algo cambió en el sistema. Campos: qué entidad, qué campo, valor anterior, valor nuevo, quién, cuándo y por qué. Sin StateChanges, la memoria es un dato estático que puede estar obsoleto sin que nadie lo sepa. | [`docs/01_aos_system.md`](01_aos_system.md), [`schemas/statechange.schema.yaml`](../schemas/statechange.schema.yaml) |
| **Stale** | Estado de un dato cuya freshness ha expirado. Un dato stale no se elimina, pero no debe incluirse en Context Packets sin advertencia explícita. | [`docs/01_aos_system.md`](01_aos_system.md) |

---

## Nota sobre encabezados en inglés de SOUL.md

Las secciones de SOUL.md (Identity, Mission Map, Pushback Rules, Autonomy Boundary, Tools Boundary, etc.) usan encabezados en inglés como **convención del framework**. Esto es una decisión de diseño, no un descuido. Los nombres en inglés funcionan como identificadores estables del contrato operativo, facilitando la interoperabilidad entre implementaciones independientemente del idioma de la documentación.

---

*Este glosario cubre los términos del framework Company Brain System v0.1.0. Para profundizar en cualquier concepto, sigue el enlace a su documento de referencia.*

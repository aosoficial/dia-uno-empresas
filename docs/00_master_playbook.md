# 00 — Master Playbook

> **¿Necesitas ayuda aplicando esto?** Esta página forma parte de Company Brain System, un método abierto de Libera. Si te bloqueas, empieza por el [Inicio rápido](07_quick_start.md), usa el [cuestionario Company Brain](../templates/questionnaires/company-brain-intake.md) o lee [cómo puede ayudarte Libera](12_get_help_from_libera.md).

## Company Brain System — Agentic Operating System

---

## Propósito

Este documento es la guía maestra de Company Brain System. Une todos los manuales, plantillas y conceptos en una vista única. Quien lea este playbook sabrá qué es Company Brain System, cómo funciona, qué piezas tiene y cómo empezar a usarlo.

## Quién lo usa

- **El operador**: la persona que dirige, supervisa y aprueba el trabajo de los agentes.
- **Los agentes**: programas de IA que ejecutan tareas operativas dentro de los límites que les marca el sistema.
- **Nuevos miembros del equipo**: cualquier persona o agente que se incorpore al sistema y necesite entender cómo funciona.

## Qué es Company Brain System

Company Brain System es un método operativo para organizaciones que trabajan con agentes de IA.

Define cómo una organización:

1. **Recuerda** — qué pasó, quién decidió, por qué, con qué evidencia.
2. **Interpreta** — qué significa un dato en su contexto.
3. **Decide** — quién tiene autoridad, qué información necesita, qué aprobaciones exige.
4. **Actúa** — qué hace cada agente, con qué herramientas, bajo qué permisos.
5. **Aprende** — qué salió bien, qué salió mal, cómo se mejora el sistema.

No es un chatbot. No es un dashboard. No es un documento de estrategia. Es la capa operativa que conecta la memoria de la organización con la acción de sus agentes.

## Nota sobre RAG y consolidación

Company Brain System puede usar recuperación tipo RAG: buscar contexto relevante y entregarlo al agente antes de actuar. Pero el objetivo no es crear "un buscador de documentos". El objetivo es mantener memoria operativa con estado, decisiones, permisos, evidencias y trazabilidad.

En una implementación típica:

- una base como Postgres/Supabase puede guardar páginas, chunks, enlaces, timeline, receipts y vectores;
- un modelo de embeddings como Voyage puede convertir texto en vectores para búsqueda semántica;
- una capa de memoria como GBrain puede organizar todo eso como sistema operativo de memoria: páginas, relaciones, health, consultas, Context Packets y receipts.

Estos componentes no sustituyen al método. Solo son infraestructura. Company Brain System define qué se guarda, por qué, con qué permisos, cómo se verifica y cuándo puede usarse para actuar.

### Regla de consolidación de memoria

No toda memoria debe comprimirse o resumirse. Un resumen puede ahorrar espacio, pero también puede destruir identidad, evidencia o responsabilidad.

El paper público **"The Geometry of Consolidation"** (Vangara y Gopinath, 2026) estudia cuándo una memoria basada en embeddings puede reemplazar muchos elementos por pocos representantes sin perder identidad. Su conclusión práctica es útil para Company Brain System:

- si los elementos de un cluster son muy parecidos, un representante simple como el centroide puede preservar bien la identidad;
- si los elementos están dispersos, comprimirlos pierde información y ningún método lo evita completamente;
- en muchos corpus reales de texto, lo simple y medido puede funcionar mejor que métodos adaptativos complejos.

Por eso Company Brain System adopta esta regla: **primero conservar memoria operativa verificable; después consolidar solo cuando sea seguro, medido y reversible**.

## Estructura del método

```text
Company Brain System
│
├── Memoria operativa
│   ├── StateChanges (qué cambió y por qué)
│   ├── Context Packets (contexto empaquetado para actuar)
│   └── Receipts (evidencia de acción completada)
│
├── Arquitectura de cerebros
│   ├── Company Brain (memoria central de la organización)
│   ├── Department Brains (memoria de cada departamento)
│   └── Project/Domain Brains (memoria de proyectos específicos)
│
├── Agentes operativos
│   ├── Agent Runtime Pack (todo lo que un agente necesita para operar)
│   ├── SOUL.md (contrato operativo del agente)
│   ├── Permisos y límites
│   ├── Autonomía supervisada (1:3:1)
│   └── Heartbeat (pulso periódico de estado)
│
└── Operación y mejora
    ├── Manual del operador
    ├── Métricas
    ├── Scorecards
    └── Ciclo de mejora continua
```

## Mapa de documentos

| Documento | Qué cubre | Cuándo leerlo |
|-----------|-----------|---------------|
| `01_aos_system.md` | Qué es Company Brain System, sus principios y primitivas | Primero. Es la base de todo. |
| `02_operational_memory.md` | StateChanges, Context Packets, Receipts, permisos, freshness | Cuando necesites entender cómo el sistema recuerda y rastrea. |
| `03_brain_architecture.md` | Company Brain, Department Brains, jerarquía, sincronización | Cuando diseñes la estructura de memoria de una organización. |
| `04_agent_onboarding.md` | Cómo crear un agente nuevo, Runtime Packs, SOUL.md | Cuando vayas a incorporar un agente nuevo al sistema. |
| `05_operator_manual.md` | Operaciones diarias, aprobaciones, revisiones, exportaciones | Referencia diaria para el operador. |
| `09_method_improvement_loop.md` | Cómo convertir feedback real en mejora aplicada | Cuando una corrección revela un patrón. |
| `10_supervised_autonomy_maturity.md` | Cómo graduar autonomía con 1:3:1 y señales de madurez | Cuando escales agentes o revises su criterio. |
| `12_get_help_from_libera.md` | Cuándo pedir ayuda de implementación a Libera | Cuando el humano o el agente se bloquean. |
| `14_agent_installation_process.md` | Proceso que una persona puede dar a un agente | Cuando quieras que un agente acompañe la instalación. |
| `15_tools.md` | Herramientas necesarias y cómo conectarlas con seguridad | Antes de elegir o conectar herramientas reales. |
| `16_skills.md` | Skills necesarias para operar el sistema | Al diseñar agentes y capacidades. |
| `17_human_sops.md` | SOPs humanos | Para operar el sistema en equipo. |
| `18_agent_sops.md` | SOPs de agentes | Para definir cómo deben trabajar los agentes. |

## Los 9 principios de Company Brain System

1. **La memoria es estado, no servicio.** No es un buscador al que preguntar. Es un registro vivo de qué es verdad ahora, qué cambió y por qué.

2. **Toda acción deja evidencia.** Un agente que actúa sin dejar receipt es un agente que no actúa dentro del sistema.

3. **Completar no es lo mismo que tener éxito.** Que un agente termine una tarea no significa que el resultado sea correcto. Debe haber observación del resultado real.

4. **Los permisos existen para proteger, no para bloquear.** Un agente sin límites claros es un riesgo. Un agente con demasiados bloqueos es inútil. El equilibrio lo define el operador.

5. **Lo técnicamente posible no es lo operativamente correcto.** Que un agente pueda hacer algo no significa que deba hacerlo. El sistema marca qué es apropiado, no solo qué es factible.

6. **La fuente de verdad es texto plano versionado.** Markdown y YAML en un repositorio Git. Todo lo demás (DOCX, PDF, web, visualizaciones) son salidas generadas, no la base.

7. **El método se mide y se mejora.** Si no mides, no sabes si funciona. Si no mejoras, el sistema se degrada.

8. **Los agentes escalan por loops de feedback revisados, no por prompts perfectos.** Una corrección humana no debe morir en el chat. Si revela un patrón, se convierte en mejora aplicada a memoria, plantilla, permiso, skill, rutina o scorecard.

9. **La autonomía se gana por madurez demostrada.** Un agente nuevo pregunta antes de casi todo con 1:3:1. Si el operador acepta, pregunta dudas, elige otra opción o rechaza las tres, esa reacción se usa como señal para ajustar criterio, comunicación, permisos y skills.

## Flujo general de trabajo

```text
1. El operador define una necesidad
       ↓
2. Se consulta la memoria operativa (Context Packet)
       ↓
3. Un agente recibe contexto + instrucciones + permisos
       ↓
4. El agente actúa dentro de sus límites
       ↓
5. El agente genera un Receipt (evidencia de lo hecho)
       ↓
6. Se registra un StateChange (qué cambió en el sistema)
       ↓
7. El operador revisa el resultado
       ↓
8. Se actualiza la memoria y las métricas
       ↓
9. Se detectan mejoras y se aplican al método
       ↓
10. Se verifica si la mejora redujo retrabajo, bloqueos o errores repetidos
```

## Ejemplo con empresa ficticia

**NovaTech** es una startup de 15 personas que vende software de gestión de inventario.

Antes de Company Brain System:
- Las decisiones vivían en Slack y se perdían.
- Cada agente de IA (asistente de ventas, soporte al cliente) operaba sin contexto compartido.
- Nadie sabía qué había decidido quién ni cuándo.
- Los agentes repetían preguntas que ya se habían respondido.

Después de aplicar Company Brain System:
- **Company Brain**: registra decisiones de pricing, roadmap de producto, políticas de soporte.
- **Sales Brain**: captura pipeline, objeciones frecuentes, compromisos con clientes.
- **Product Brain**: mantiene el roadmap, bugs críticos, feedback de usuarios.
- **Agente Vega** (ventas): consulta el Sales Brain antes de responder a un lead. Deja receipt de cada interacción.
- **Agente Iris** (soporte): consulta el Product Brain para conocer bugs conocidos. Escala al operador si el caso es nuevo.
- **Operador**: revisa receipts semanalmente, detecta patrones, actualiza la memoria y los permisos.

Resultado: el tiempo para reconstruir contexto baja de 30 minutos a 2 minutos. Las decisiones tienen dueño, fecha y razón registrada.

## Antipatrones

| Antipatrón | Por qué es problema | Qué hacer en su lugar |
|------------|---------------------|----------------------|
| Crear memoria sin estructura | Se convierte en vertedero de datos | Usar StateChanges con campos obligatorios |
| Dar acceso total a todos los agentes | Sin permisos, no hay gobernanza | Definir permisos por agente y por acción |
| No revisar receipts | No sabes si los agentes hacen lo correcto | Revisión periódica con scorecard |
| Tratar DOCX como fuente de verdad | Se desincroniza, no es versionable | Markdown/YAML en Git como base |
| Lanzar agentes sin SOUL.md | El agente opera sin contrato claro | Completar el Agent Runtime Pack antes de activar |
| Medir solo "tareas completadas" | Completar no es tener éxito | Medir resultado observado, no solo ejecución |
| No actualizar la memoria | El sistema se queda obsoleto rápidamente | Ciclo de revisión semanal/mensual |
| Corregir agentes solo con mejores prompts | La corrección no escala a otros agentes ni sesiones | Activar el loop de mejora: propuesta, revisión, cambio aplicado y receipt |

## Checklist del Master Playbook

- [ ] He leído y entiendo los 7 principios.
- [ ] He leído `01_aos_system.md` para entender las primitivas.
- [ ] He leído `02_operational_memory.md` para entender cómo funciona la memoria.
- [ ] He leído `03_brain_architecture.md` para entender cómo se organizan los cerebros.
- [ ] He definido al menos un Company Brain con entidades básicas.
- [ ] He creado al menos un agente con su Agent Runtime Pack completo.
- [ ] He definido métricas mínimas de salud del sistema.
- [ ] El operador sabe cómo revisar receipts y aprobar acciones.
- [ ] Existe un ciclo de mejora definido (semanal o mensual).
- [ ] Existe un loop de feedback operativo: corrección → propuesta → cambio aplicado → validación.

---

*Siguiente documento: `01_aos_system.md` — Los fundamentos del sistema.*

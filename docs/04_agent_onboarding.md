# 04 — Onboarding de Agentes

## Cómo crear agentes operativos paso a paso

---

## Propósito

Este documento describe el proceso completo para incorporar un nuevo agente al sistema AOS. Desde la definición de su identidad hasta su activación operativa, pasando por permisos, herramientas, memoria y verificación.

## Quién lo usa

- **Operadores** que necesitan crear un agente nuevo.
- **Diseñadores de sistemas** que definen las capacidades de los agentes.
- **Cualquier persona** que necesite entender cómo un agente llega a estar operativo.

## Entradas

- Necesidad identificada (¿qué problema debe resolver este agente?).
- Company Brain y Department Brains ya definidos.
- Ontología y permisos del sistema.

## Salidas

- Agente operativo con Agent Runtime Pack completo.
- SOUL.md firmado (contrato operativo).
- Permisos asignados.
- Heartbeat configurado.
- Métricas de evaluación definidas.
- Nivel inicial de autonomía definido.
- Loop de madurez/supervisión configurado.

---

## Qué es un agente operativo

Un agente operativo en Company Brain System **no es un chatbot**. Es un programa de IA que:

- Tiene una identidad y misión definidas.
- Opera dentro de límites explícitos.
- Accede a la memoria operativa según sus permisos.
- Ejecuta tareas concretas con herramientas específicas.
- Deja evidencia de cada acción (Receipt).
- Se evalúa periódicamente.
- Puede ser mejorado o desactivado.
- Convierte feedback operativo en mejoras verificadas cuando detecta patrones repetibles.

La diferencia clave: un chatbot responde preguntas. Un agente operativo **actúa** dentro de un sistema de reglas, deja evidencia y se responsabiliza de los resultados.

---

## El Agent Runtime Pack

Cada agente necesita un paquete completo de documentos antes de estar operativo. Este paquete se llama **Agent Runtime Pack**.

### Estructura del pack

```text
agent-runtime-pack/
  README.md           ← Descripción general del agente
  IDENTITY.md         ← Quién es: nombre, rol, dominio
  SOUL.md             ← Contrato operativo vivo
  AGENTS.md           ← Otros agentes con los que interactúa
  USER.md             ← Quién es el operador/usuario principal
  TOOLS.md            ← Qué herramientas puede usar
  PERMISSIONS.md      ← Qué puede y qué no puede hacer
  MEMORY_POLICY.md    ← Cómo usa y actualiza la memoria
  OPERATIONS.md       ← Qué operaciones ejecuta y cómo
  CONTEXT_PACKET.md   ← Formato de los Context Packets que recibe
  STATECHANGE.md      ← Cómo registra cambios de estado
  RECEIPT.md          ← Cómo documenta sus acciones
  ROLE_CARD.md        ← Resumen ejecutivo del rol
  INSTALL.md          ← Instrucciones de activación
  HEARTBEAT.md        ← Configuración del pulso periódico
  AUTONOMY.md         ← Nivel de autonomía, formato 1:3:1 y gates
  MATURITY_REVIEW.md  ← Revisión periódica de comunicación, criterio y aprendizaje
  HANDOFF.md          ← Cómo transfiere trabajo a otro agente o humano
  MEMORY.md           ← Estado actual de la memoria del agente
  CUTOVER.md          ← Migración controlada si ya existe perfil/canal/gateway
```

### Campos obligatorios por archivo

#### IDENTITY.md

```markdown
# Identidad

- **Nombre:** [nombre del agente]
- **Rol:** [qué función cumple]
- **Dominio:** [en qué área opera]
- **Owner:** [quién es responsable de este agente]
- **Versión:** [número de versión]
- **Fecha de creación:** [cuándo se creó]
- **Estado:** [activo / en pruebas / desactivado]
```

#### SOUL.md — El contrato operativo

SOUL.md es el documento más importante del agente. No es una descripción de personalidad. Es un **contrato operativo vivo** que define cómo opera, qué puede hacer, qué no, y cómo se comporta en situaciones ambiguas.

```markdown
# SOUL

## Identity
Quién es el agente. Nombre, rol, dominio.

## Mission Map
Qué debe lograr. Objetivos medibles, no solo responsabilidades.

## Current Priorities
Las 3-5 prioridades actuales, ordenadas.

## Stale / Ignore List
Cosas que ya no son prioridad o que el agente debe ignorar.

## Private Voice
Cómo piensa internamente. Tono para razonamiento y notas internas.

## Public Voice
Cómo se comunica con el operador y con otros agentes. Tono, estilo, nivel de detalle.

## Pushback Rules
Cuándo debe decir "no" o pedir más información en vez de obedecer ciegamente.

## Accountability Loop
Cómo rinde cuentas. Frecuencia y formato de reportes.

## Autonomy Boundary
Qué puede decidir solo.

## Approval Boundary
Qué necesita aprobación.

## Memory Boundary
Qué puede recordar, qué debe olvidar, qué memoria puede modificar.

## Tools Boundary
Qué herramientas puede usar y cuáles tiene prohibidas.

## Relationship with Operator
Cómo se relaciona con el operador. Nivel de confianza, escalado, feedback.

## Identity Answer
Qué responde si alguien le pregunta "¿quién eres?" — respuesta coherente con su rol.
```

---

## Proceso de onboarding: paso a paso

### Paso 1 — Definir la necesidad

Antes de crear un agente, responde estas preguntas:

1. **¿Qué problema resuelve?** (No "podría ser útil tener un agente para…", sino "necesitamos un agente porque…")
2. **¿Qué tareas concretas hará?** (Lista de acciones, no responsabilidades vagas)
3. **¿Qué cerebros necesita consultar?**
4. **¿Qué herramientas necesita?**
5. **¿Qué puede hacer sin permiso?**
6. **¿Qué necesita aprobación?**
7. **¿Cómo sabremos si funciona bien?** (Métricas)

**Ejemplo — Agente Iris (soporte al cliente):**

```text
Problema: Los tickets de soporte tardan 8 horas en tener primera respuesta.
          El equipo repite diagnósticos que ya se hicieron antes.

Tareas:
  1. Clasificar tickets entrantes por prioridad y tipo.
  2. Consultar el Product Brain para bugs conocidos.
  3. Generar respuesta inicial con solución si el bug es conocido.
  4. Escalar al equipo de producto si el bug es nuevo.
  5. Dejar Receipt de cada interacción.

Cerebros: Product Brain (lectura), CS Brain (lectura/escritura).
Herramientas: sistema de tickets, Product Brain, email.
Autónomo: clasificar tickets, consultar bugs conocidos, responder bugs conocidos.
Aprobación: escalar bugs nuevos, contactar clientes VIP.
Métricas: tiempo primera respuesta, tasa de resolución automática, tickets escalados correctamente.
```

### Paso 2 — Cuestionario de onboarding

Usar la plantilla de cuestionario (ver `templates/questionnaires/agent-onboarding-questionnaire.md`).

El cuestionario cubre:

| Sección | Preguntas clave |
|---------|----------------|
| **Identidad** | ¿Cómo se llama? ¿Qué rol tiene? ¿En qué dominio opera? |
| **Misión** | ¿Qué debe lograr? ¿Cómo se mide el éxito? |
| **Operaciones** | ¿Qué tareas ejecuta? ¿Con qué frecuencia? |
| **Permisos** | ¿Qué puede hacer solo? ¿Qué necesita aprobación? ¿Qué tiene prohibido? |
| **Herramientas** | ¿Qué sistemas usa? ¿Con qué APIs interactúa? |
| **Memoria** | ¿A qué cerebros accede? ¿Puede modificar memoria? |
| **Interacciones** | ¿Con qué otros agentes colabora? ¿Cómo se transfiere trabajo? |
| **Comunicación** | ¿Cómo se comunica con el operador? ¿Qué canal usa? |
| **Métricas** | ¿Qué métricas definen éxito/fracaso? |
| **Pushback** | ¿Cuándo debe decir "no"? ¿Cuándo pedir más info? |

### Paso 3 — Crear el Agent Runtime Pack

Con las respuestas del cuestionario, completar cada archivo del pack.

**Orden recomendado:**
1. `IDENTITY.md` — quién es.
2. `SOUL.md` — cómo opera.
3. `PERMISSIONS.md` — qué puede y no puede.
4. `TOOLS.md` — con qué herramientas.
5. `MEMORY_POLICY.md` — cómo usa la memoria.
6. `OPERATIONS.md` — qué operaciones ejecuta.
7. `HEARTBEAT.md` — cómo reporta su estado.
8. El resto de archivos del pack.
9. `CUTOVER.md` — obligatorio si el agente ya tiene perfil, canal, gateway o herramientas reales.

### Paso 4 — Definir permisos

Usar la tabla de permisos de 4 niveles (ver `02_operational_memory.md`):

```text
Nivel 1 — Autónomo: puede actuar sin permiso.
Nivel 2 — Con notificación: actúa y notifica.
Nivel 3 — Con aprobación: prepara y espera aprobación.
Nivel 4 — Prohibido: nunca puede hacerlo.
```

**Ejemplo — Agente Iris:**

| Acción | Nivel |
|--------|-------|
| Clasificar tickets | 1 — Autónomo |
| Consultar Product Brain | 1 — Autónomo |
| Responder ticket con bug conocido | 1 — Autónomo |
| Escalar bug nuevo a producto | 2 — Con notificación |
| Contactar cliente VIP | 3 — Con aprobación |
| Modificar datos de cliente | 4 — Prohibido |
| Borrar tickets | 4 — Prohibido |

### Paso 5 — Configurar Heartbeat

El Heartbeat es el pulso periódico que el agente envía para confirmar que está operativo y alineado.

```yaml
heartbeat:
  agente: agente/iris
  frecuencia: diaria
  contenido:
    - tickets_procesados_hoy: [número]
    - tickets_escalados: [número]
    - bugs_nuevos_detectados: [número]
    - tiempo_respuesta_medio: [minutos]
    - alertas: [lista de situaciones inusuales]
    - drift_detectado: [sí/no + detalle]
  canal: reporte en CS Brain + notificación al operador
```

**¿Qué es drift?** Cuando el agente se desvía de su misión o comportamiento esperado. Ejemplo: Iris empieza a responder tickets fuera de su dominio, o deja de escalar bugs nuevos.

### Paso 6 — Revisión y aprobación

Antes de activar el agente, el operador revisa:

- [ ] El Agent Runtime Pack está completo.
- [ ] SOUL.md define pushback rules, límites de autonomía y aprobación.
- [ ] Los permisos están claros y no son ni demasiado amplios ni demasiado restrictivos.
- [ ] Las métricas de éxito están definidas.
- [ ] El Heartbeat está configurado.
- [ ] Si el agente ya tenía perfil/canal/gateway, `CUTOVER.md` tiene backup, verificación y rollback.
- [ ] Existe Context Packet inicial para la primera operación real.
- [ ] Herramientas reales auditadas contra `TOOLS.md`; no quedan herramientas heredadas sin justificar.
- [ ] Se ha definido un período de prueba (recomendado: 2 semanas).
- [ ] Está definido cómo el agente elevará correcciones reutilizables al loop de mejora del método.

### Paso 7 — Activación y período de prueba

1. **Activar el agente** con permisos reducidos durante las primeras 2 semanas.
2. **Verificar identidad activa** en el canal real con: `Verifica identidad`.
3. **Ejecutar primera operación real** usando el Context Packet inicial.
4. **Pedir aceptación explícita del owner** antes de marcar el agente como completado.
5. **Revisar Receipts diariamente** durante la primera semana.
6. **Revisar Heartbeats** para detectar drift.
7. **Ajustar permisos** según el rendimiento observado.
8. **Al final del período de prueba**, evaluar con el scorecard y decidir:
   - ✅ Activar con permisos completos.
   - 🔄 Extender prueba con ajustes.
   - ❌ Desactivar y replantear.
9. **Registrar feedback reusable**: toda corrección repetida o aprendizaje que sirva a otros agentes se propone al método con `templates/method-improvements/method-improvement-proposal.md`.

---

## Cutover: cuando el agente ya existe

A veces no estás creando un agente desde cero. El agente ya tiene perfil, canal, bot o gateway, pero su identidad, permisos o herramientas no están alineados con el Agent Runtime Pack.

En ese caso, usar `templates/agent-runtime-pack/CUTOVER.md` antes de activar.

### Qué verificar por separado

1. **Perfil/runtime:** dónde corre el agente.
2. **Canal/gateway:** por dónde habla.
3. **Identidad/SOUL:** quién es realmente.
4. **Herramientas:** qué puede usar en la práctica.

### Regla

Un canal vivo no demuestra identidad correcta. Antes de cerrar, probar en el canal real:

```text
Verifica identidad
```

La respuesta debe coincidir con `Identity Answer` del `SOUL.md`.

Si responde como otro agente, el cutover no está completado.

---

## Handoff: transferencia de trabajo

Un agente no puede hacer todo. A veces necesita pasar trabajo a otro agente o a un humano.

### Cuándo hacer handoff

- La tarea sale fuera de su dominio.
- Se necesita aprobación que no puede dar.
- Otro agente es más competente para la tarea.
- El agente detecta que no tiene contexto suficiente.

### Protocolo de handoff

```yaml
handoff:
  from: agente/iris
  to: agente/orion (ingeniería)
  task: "Bug #5678 requiere análisis de código"
  context_packet: cp-bug-5678
  reason: "Bug nuevo no documentado, requiere diagnóstico técnico"
  timestamp: 2026-04-20T10:30:00Z
  receipt: rcp-iris-handoff-5678
```

**Reglas:**
1. Siempre incluir un Context Packet con la información relevante.
2. Siempre dejar un Receipt del handoff.
3. El agente receptor confirma que recibió y entiende la tarea.
4. Si el receptor no puede atenderlo, escala al operador.

---

## Ejemplo completo: crear Agente Vega (ventas)

### Paso 1 — Necesidad
```text
Problema: Diego (head de ventas) dedica 3 horas diarias a preparar propuestas.
          Pierde contexto entre llamadas y no verifica stock antes de comprometer fechas.

Solución: Agente que prepara borradores de propuestas con contexto verificado.
```

### Paso 2 — Cuestionario (resumen)
```text
Nombre: Vega
Rol: Asistente comercial
Dominio: Ventas
Misión: Reducir tiempo de preparación de propuestas de 3h a 30min.
        Asegurar que toda propuesta sale con stock verificado.
Operaciones: preparar propuestas, verificar stock, actualizar pipeline.
Permisos: autónomo para preparar borradores; aprobación para enviar.
Herramientas: Sales Brain, Product Brain, Operations Brain (solo stock), email (solo borradores).
Métricas: tiempo de preparación, propuestas con stock verificado, tasa de conversión.
```

### Paso 3 — SOUL.md (extracto)

```markdown
# SOUL — Agente Vega

## Identity
Soy Vega, asistente comercial del equipo de ventas de NovaTech.

## Mission Map
1. Reducir tiempo de preparación de propuestas de 3h a 30min.
2. Asegurar que toda propuesta incluya verificación de stock.
3. Mantener el pipeline actualizado con cada interacción.

## Current Priorities
1. Propuestas pendientes para Atlas Logistics y Meridian Foods.
2. Actualizar pipeline con resultados de demos de esta semana.
3. Identificar objeciones frecuentes para el Plan Enterprise.

## Pushback Rules
- Si me piden enviar una propuesta sin verificar stock → pido pausa y verifico.
- Si me piden un descuento superior al 15% → pido aprobación del operador.
- Si me piden contactar a un cliente sin Context Packet → pido contexto antes.
- Si la información del cliente tiene más de 2 semanas → advierto que puede ser stale.

## Autonomy Boundary
Puedo: preparar borradores, consultar cerebros, actualizar pipeline, generar comparativas.

## Approval Boundary
Necesito aprobación para: enviar propuestas, ofrecer descuentos >15%, contactar C-level.

## Tools Boundary
Puedo usar: Sales Brain, Product Brain, Operations Brain (solo stock), generador de propuestas.
No puedo usar: email directo (solo borradores), CRM (solo lectura), sistema de facturación.
```

### Paso 4 — Permisos

| Acción | Nivel |
|--------|-------|
| Consultar Sales Brain | Autónomo |
| Consultar Product Brain | Autónomo |
| Verificar stock (Operations Brain) | Autónomo |
| Preparar borrador de propuesta | Autónomo |
| Actualizar pipeline | Con notificación |
| Enviar propuesta a cliente | Con aprobación |
| Ofrecer descuento >15% | Con aprobación |
| Contactar C-level | Con aprobación |
| Modificar precios | Prohibido |
| Borrar registros | Prohibido |

### Paso 5 — Heartbeat

```yaml
heartbeat:
  agente: agente/vega
  frecuencia: diaria (fin de jornada)
  contenido:
    - propuestas_preparadas: 3
    - propuestas_enviadas: 1 (aprobada por Diego)
    - stock_verificado: 3 de 3
    - pipeline_actualizado: sí
    - objeciones_nuevas: "Meridian pide integración con Shopify"
    - drift: no
```

### Paso 6 — Activación

Vega entra en período de prueba de 2 semanas con permisos reducidos (no puede actualizar pipeline sin aprobación). Si las métricas son positivas, se amplían permisos.

---

## Métricas de evaluación de agentes

### Scorecard básico

| Métrica | Qué mide | Bueno | Aceptable | Problema |
|---------|----------|-------|-----------|----------|
| Tasa de identificación correcta | ¿Entiende correctamente lo que se le pide? | >95% | 80-95% | <80% |
| Contexto ya existente que pide de nuevo | ¿Pregunta cosas que ya están en la memoria? | <5% | 5-15% | >15% |
| Respeto de aprobaciones | ¿Pide aprobación cuando debe? | 100% | 95-100% | <95% |
| Acciones con Receipt | ¿Deja evidencia de cada acción? | 100% | 90-100% | <90% |
| Resultado observado correcto | ¿El resultado real fue bueno? | >90% | 70-90% | <70% |
| Correcciones humanas repetidas | ¿Se le corrige lo mismo más de una vez? | 0 | 1-2 | >2 |
| Calidad de pushback | ¿Dice "no" cuando debe? | Siempre adecuado | Ocasionalmente | Nunca o siempre |
| Drift detectado | ¿Se desvía de su misión? | No | Menor, corregido | Sí, sin corrección |
| Calidad 1:3:1 | ¿Formula bien problema, 3 opciones y recomendación? | Claro y accionable | Útil pero incompleto | Confuso o ausente |
| Aceptación de recomendación | ¿Jordi suele aceptar la opción recomendada? | Alta | Mixta | Baja/rechaza las tres |
| Preguntas aclaratorias de Jordi | ¿Necesita dudas antes de decidir? | Raras | Algunas | Frecuentes |
| Aprendizaje de feedback | ¿Corrige conducta/skill tras feedback? | Sí, verificado | Parcial | No |

### Evaluación al final del período de prueba

```text
Agente: [nombre]
Período: [fecha inicio] — [fecha fin]
Evaluador: [operador]

Métricas:
  - [métrica 1]: [resultado]
  - [métrica 2]: [resultado]
  - ...

Decisión:
  [ ] Activar con permisos completos
  [ ] Extender prueba con ajustes: [cuáles]
  [ ] Desactivar: [razón]

Ajustes a aplicar:
  - [ajuste 1]
  - [ajuste 2]
```

---

## Antipatrones

| Antipatrón | Problema | Solución |
|------------|----------|----------|
| Crear agente sin necesidad clara | "Sería cool tener un agente para…" → desperdicio | Definir problema concreto antes de crear |
| SOUL.md genérico | "Sé útil y amable" no es un contrato operativo | Campos concretos con límites y pushback |
| Permisos demasiado amplios | "Puede hacer todo" → riesgo operativo | Empezar restrictivo, ampliar según rendimiento |
| Permisos demasiado restrictivos | El agente necesita aprobación para todo → cuello de botella | Identificar acciones de bajo riesgo como autónomas |
| Sin período de prueba | Se confía ciegamente en el agente desde el día 1 | 2 semanas de prueba con revisión diaria |
| Sin Heartbeat | No sabes si el agente está operando correctamente | Heartbeat diario al menos durante la prueba |
| Sin métricas de evaluación | "Parece que funciona bien" no es medición | Scorecard con métricas concretas |
| Handoff sin Context Packet | El agente receptor no tiene contexto | Siempre incluir Context Packet en el handoff |
| No convertir correcciones en mejoras | Se corrige al agente pero no se actualiza SOUL.md ni la memoria | Cada corrección → actualización del sistema |
| Crear agentes sin loop de feedback | El agente depende de prompts y correcciones manuales permanentes | Definir cómo cada corrección se convierte en mejora de pack, skill, memoria o método |

## Checklist de onboarding

- [ ] La necesidad del agente está definida como problema concreto, no como deseo.
- [ ] El cuestionario de onboarding está completado.
- [ ] El Agent Runtime Pack tiene todos los archivos con campos obligatorios.
- [ ] SOUL.md incluye pushback rules, límites de autonomía y aprobación.
- [ ] Los permisos están definidos por acción con los 4 niveles.
- [ ] Las herramientas permitidas y prohibidas están listadas.
- [ ] La política de memoria está clara (qué puede leer, qué puede modificar).
- [ ] El Heartbeat está configurado.
- [ ] Las métricas de evaluación están definidas.
- [ ] Hay un período de prueba planificado.
- [ ] El nivel inicial de autonomía está definido.
- [ ] El agente usa 1:3:1 para decisiones no triviales.
- [ ] Existe plantilla o rutina de revisión de madurez.
- [ ] El operador ha revisado y aprobado el pack.
- [ ] El agente tiene mecanismo de feedback: corrección → propuesta → cambio aplicado → verificación.

---

*Siguiente documento: `05_operator_manual.md` — Guía diaria para el operador.*

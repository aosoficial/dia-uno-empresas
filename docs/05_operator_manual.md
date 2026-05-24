# 05 — Manual del Operador

> **¿Necesitas ayuda aplicando esto?** **¿Necesitas ayuda aplicando esto?** Esta página forma parte de DIA UNO Empresas, una aceleradora abierta hacia empresas AI-First. Si te bloqueas, empieza por el [Inicio rápido](07_quick_start.md), usa el [intake de servicio](../templates/questionnaires/service-business-ai-first-intake.md) o pide ayuda en [DIA UNO](12_get_help_from_dia_uno.md).

## Guía diaria para quien dirige el sistema

---

## Propósito

Este documento es la referencia diaria del operador: la persona que supervisa agentes, aprueba acciones, revisa la memoria y mantiene el sistema AOS saludable. Explica qué hacer, cuándo y cómo en las operaciones del día a día.

## Quién lo usa

- **El operador principal** (CEO, founder, responsable de operaciones).
- **Cualquier persona con rol de supervisión** sobre agentes en el sistema.

## Entradas

- Sistema AOS configurado con Company Brain, Department Brains y agentes activos.
- Receipts, Heartbeats y StateChanges generados por los agentes.
- Solicitudes de acción que requieren aprobación.

## Salidas

- Agentes supervisados con rendimiento verificado.
- Memoria actualizada y saludable.
- Aprobaciones y rechazos registrados.
- Mejoras aplicadas al sistema.

---

## El rol del operador

El operador no hace el trabajo de los agentes. El operador:

1. **Dirige** — Define prioridades, asigna tareas, establece límites.
2. **Supervisa** — Revisa lo que los agentes hicieron, verifica resultados.
3. **Aprueba** — Autoriza acciones que los agentes no pueden hacer solos.
4. **Corrige** — Cuando algo sale mal, ajusta la memoria, los permisos o el agente.
5. **Mejora** — Convierte cada corrección en una mejora del sistema para que no se repita.

**Principio fundamental:** el operador no debería tener que re-explicar lo mismo dos veces. Si lo hace, el sistema no está aprendiendo.

---

## Operaciones diarias

### Rutina matutina (10 minutos)

```text
1. Revisar Heartbeats de agentes activos
   → ¿Todos reportaron? ¿Alguno tiene drift?
   → Si un agente no reportó: investigar.

2. Revisar aprobaciones pendientes
   → ¿Qué acciones esperan tu visto bueno?
   → Priorizar por urgencia y riesgo.

3. Revisar alertas
   → ¿Algún agente escaló algo?
   → ¿Hay datos stale en categoría crítica?
```

### Rutina de cierre (5 minutos)

```text
1. Revisar Receipts del día
   → ¿Cuántas acciones ejecutaron los agentes?
   → ¿Algún resultado inesperado?

2. Verificar que las aprobaciones pendientes están atendidas
   → No dejar aprobaciones sin respuesta más de 24 horas.

3. Anotar mejoras pendientes
   → Si hoy corregiste algo, ¿se actualizó el sistema?
   → Si se repite o sirve a otros agentes, ¿se creó propuesta de mejora?
```

---

## Cómo aprobar una acción

Cuando un agente solicita aprobación:

### Paso 1 — Leer el Context Packet

El agente incluye un resumen de qué quiere hacer y por qué. Revisa:

- ¿El contexto es correcto y actual?
- ¿La acción está dentro de las operaciones del agente?
- ¿Los datos que usa son frescos?

### Paso 2 — Evaluar riesgo

| Riesgo | Criterio | Acción |
|--------|----------|--------|
| **Bajo** | Acción rutinaria, reversible, impacto limitado | Aprobar |
| **Medio** | Involucra a actor externo o dato sensible | Revisar detalle antes de aprobar |
| **Alto** | Irreversible, afecta a muchos, compromiso económico | Revisar con detenimiento, pedir más contexto si es necesario |

### Paso 3 — Aprobar o rechazar

**Si apruebas:**
```yaml
approval:
  action: Enviar propuesta a Atlas Logistics
  agent: agente/vega
  approved_by: operador
  timestamp: 2026-04-17T08:30:00Z
  conditions: "Enviar antes de las 12:00. Copia a Diego."
```

**Si rechazas:**
```yaml
rejection:
  action: Enviar propuesta a Atlas Logistics
  agent: agente/vega
  rejected_by: operador
  timestamp: 2026-04-17T08:30:00Z
  reason: "El precio de la integración SAP no está confirmado. Esperar a producto."
  next_step: "Confirmar precio con Elena y reenviar para aprobación."
```

### Paso 4 — Registrar

Toda aprobación y rechazo queda como StateChange en la memoria de acción.

---

## Cómo revisar Receipts

### Revisión rápida (para Receipts de bajo riesgo)

1. ¿El agente hizo lo que se le pidió?
2. ¿El resultado parece correcto?
3. Si sí → marcar como `éxito`.
4. Si algo no cuadra → investigar.

### Revisión detallada (para Receipts de medio/alto riesgo)

1. Leer el Context Packet que recibió el agente.
2. Leer el output que produjo.
3. Comparar output vs. lo que se pedía.
4. Verificar que se respetaron las restricciones.
5. Verificar que no se usaron permisos que no tiene.
6. Evaluar el resultado real (no solo "se completó").
7. Marcar como `éxito`, `éxito_parcial`, `fallo` o `rechazado`.
8. Si hay correcciones, registrarlas.

### Convertir correcciones en mejoras

Cada vez que corriges a un agente, pregúntate:

- **¿Fue un error del agente o de la instrucción?** Si la instrucción era ambigua, mejora el SOUL.md o el Context Packet.
- **¿Le faltaba contexto?** Actualiza el Department Brain o el Context Packet.
- **¿Excedió sus permisos?** Revisa PERMISSIONS.md.
- **¿Es un patrón?** Si se repite, necesita un cambio en el sistema, no solo una corrección puntual.
- **¿Es reusable?** Si puede evitar errores en otros agentes, activar el loop de mejora del método.

### Loop de mejora del método

Cuando una corrección revela un patrón, usar `09_method_improvement_loop.md`:

```text
1. Capturar la señal con evidencia.
2. Crear propuesta con templates/method-improvements/method-improvement-proposal.md.
3. Decidir si el cambio es seguro o requiere aprobación.
4. Aplicar en todas las capas necesarias: docs, templates, schemas, skills, rutinas o scorecards.
5. Validar localmente y revisar anti-secretos.
6. Registrar StateChange y Receipt.
7. Revisar en la siguiente weekly/monthly si redujo retrabajo o bloqueos.
```

**Regla:** no basta con mejorar un prompt. Si el aprendizaje debe sobrevivir a sesiones y agentes, debe vivir en el método, una plantilla, una skill, una política de memoria o una rutina.

---

## Cómo pedir un nuevo agente

### Paso 1 — Identificar la necesidad

Responde:
```text
1. ¿Qué problema tengo que un agente podría resolver?
2. ¿Qué tareas concretas haría?
3. ¿Cuánto tiempo me ahorra?
4. ¿Qué riesgo tiene si lo hace mal?
```

### Paso 2 — Completar el cuestionario de onboarding

Usar `templates/questionnaires/agent-onboarding-questionnaire.md`.

### Paso 3 — Crear el Agent Runtime Pack

Seguir el proceso de `04_agent_onboarding.md`.

### Paso 4 — Activar en modo prueba

2 semanas con permisos reducidos y revisión diaria de Receipts.

---

## Cómo pedir un nuevo Department Brain

### Paso 1 — Justificar

```text
1. ¿Qué departamento o área necesita su propia memoria?
2. ¿Qué entidades gestiona que no están en el Company Brain?
3. ¿Qué agentes lo usarán?
4. ¿Quién será el owner?
```

### Paso 2 — Diseñar

Seguir el proceso de `03_brain_architecture.md`, sección "Cómo crear un nuevo Department Brain".

### Paso 3 — Definir sincronización

Establecer qué sube al Company Brain y qué queda local.

### Paso 4 — Activar y medir

Definir métricas del departamento y empezar a registrar StateChanges.

---

## Cómo gestionar la compresión de contexto

Cuando la cantidad de información activa crece demasiado, hay que comprimir.

### Qué comprimir

- **Interacciones antiguas** que ya se resumieron o cuyos hechos están en la Memoria Factual.
- **Receipts verificados sin correcciones** — el resultado ya está registrado.
- **StateChanges que fueron superados** por cambios más recientes.
- **Detalles de proyectos terminados** — mover a archivo.

### Qué NO comprimir

- Decisiones vigentes con su razón.
- Compromisos activos con fechas futuras.
- Correcciones que aún no se han convertido en mejoras del sistema.
- Datos con freshness activa.

### Protocolo de compresión

```text
1. Identificar qué datos están obsoletos o redundantes.
2. Verificar que la información relevante está capturada en hechos o decisiones.
3. Archivar (mover a archivo, no borrar).
4. Registrar StateChange: "Compresión de contexto realizada, [fecha]."
5. Verificar que ningún agente depende de los datos archivados.
```

---

## Cómo exportar documentación

### Markdown → DOCX

```bash
# Primero generar el documento combinado
python scripts/build_docs.py

# Luego exportar a DOCX (usa el combinado, no archivos individuales)
python scripts/export_docx.py
# Salida: build/outputs/master.docx

# Para exportar un archivo individual, usar pandoc directamente
pandoc docs/01_aos_system.md -o build/outputs/01_aos_system.docx
```

> **Nota:** `export_docx.py` siempre procesa `build/outputs/master_combined.md` (generado por `build_docs.py`). No acepta archivos individuales como argumento.

### Markdown → PDF

```bash
pandoc docs/01_aos_system.md -o build/outputs/01_aos_system.pdf
```

### Master export (todos los documentos en uno)

```bash
python scripts/build_docs.py
```

**Regla:** el Markdown es la fuente. Los DOCX/PDF son salidas para leer o compartir, no para editar.

---

## Cómo actualizar el método

DIA UNO Empresas es un método vivo. Se actualiza cuando:

1. **Se detecta un patrón de error.** Si varios agentes cometen el mismo tipo de fallo, el método necesita un ajuste.
2. **Cambia la organización.** Nuevo departamento, nuevo tipo de agente, nueva herramienta.
3. **Las métricas muestran degradación.** Si los indicadores empeoran, algo necesita cambiar.
4. **Feedback del operador.** Si algo es incómodo, ineficiente o confuso, se mejora.

### Protocolo de actualización

```text
1. Identificar qué necesita cambiar y por qué.
2. Proponer el cambio (el operador o un agente pueden proponerlo).
3. Evaluar impacto: ¿qué agentes, cerebros o procesos se ven afectados?
4. Aplicar el cambio en los documentos del repositorio.
5. Registrar StateChange: qué cambió, por qué, quién lo aprobó.
6. Notificar a los agentes afectados.
7. Verificar que el cambio funciona en la siguiente revisión.
```

---

## Calendario del operador

| Frecuencia | Acción | Tiempo estimado |
|------------|--------|-----------------|
| **Diaria** | Revisar Heartbeats + aprobaciones pendientes + Receipts | 15 min |
| **Semanal** | Revisión de memoria: StateChanges, datos stale críticos, métricas | 15 min |
| **Mensual** | Revisión profunda: ontología, permisos, datos stale operativos | 30 min |
| **Trimestral** | Revisión estratégica: método, cerebros, métricas globales | 1 hora |

---

## Ejemplo: un día del operador

### 08:00 — Rutina matutina

```text
Heartbeats:
  ✅ Agente Vega: 3 propuestas preparadas, pipeline actualizado, sin drift.
  ✅ Agente Iris: 12 tickets procesados, 2 escalados, tiempo medio 2.3 horas.
  ⚠️ Agente Trigo: no reportó. → Investigar.

Aprobaciones pendientes:
  1. Vega pide enviar propuesta a Atlas Logistics (riesgo medio).
  2. Iris pide contactar cliente VIP para seguimiento (riesgo bajo).

Alertas:
  - Dato stale: contacto principal de Meridian Foods verificado hace 3 semanas.
```

### 08:15 — Acciones

```text
1. Apruebo propuesta de Vega → condición: incluir disclaimer sobre fecha de SAP.
2. Apruebo contacto de Iris → sin condiciones.
3. Investigo por qué Trigo no reportó → problema técnico, reinicio.
4. Actualizo contacto de Meridian Foods → llamo para verificar.
```

### 17:00 — Rutina de cierre

```text
Receipts del día:
  - Vega: propuesta enviada a Atlas ✅, pipeline actualizado ✅.
  - Iris: 15 tickets procesados, 3 escalados correctamente ✅.
  - Trigo: reanudado tras reinicio, stock verificado ✅.

Correcciones:
  - Vega incluyó precio de SAP sin confirmar → corrección: actualizar
    SOUL.md con regla "no incluir precios no confirmados por producto."

Mejoras pendientes:
  - Actualizar SOUL.md de Vega.
  - Verificar freshness del Product Brain para precios de integraciones.
```

---

## Antipatrones del operador

| Antipatrón | Problema | Solución |
|------------|----------|----------|
| Aprobar sin leer | El agente envía algo incorrecto | Siempre leer el Context Packet y el output |
| No revisar Receipts | No sabes qué hicieron los agentes | Revisión diaria de 5 minutos |
| Corregir sin mejorar el sistema | El mismo error se repite | Cada corrección → mejora en SOUL.md, permisos o memoria |
| Dejar aprobaciones pendientes >24h | Los agentes se bloquean | Atender aprobaciones en la rutina matutina |
| No comprimir contexto | La memoria crece sin control | Compresión mensual |
| Microgestionar agentes | El operador hace el trabajo del agente | Confiar en el período de prueba y las métricas |
| No medir | "Creo que funciona" no es evidencia | Usar el scorecard y las métricas definidas |
| Ignorar drift | El agente se desvía y nadie se da cuenta | Heartbeats + revisión semanal |

## Checklist del operador

### Diario
- [ ] He revisado los Heartbeats de todos los agentes activos.
- [ ] He atendido las aprobaciones pendientes.
- [ ] He revisado los Receipts más importantes del día.
- [ ] He registrado las correcciones como mejoras pendientes.
- [ ] He convertido correcciones reutilizables en propuestas de mejora del método.

### Semanal
- [ ] He revisado los StateChanges de la semana.
- [ ] He verificado datos stale en categoría crítica.
- [ ] He revisado las métricas del sistema.
- [ ] He aplicado mejoras pendientes.
- [ ] He revisado propuestas de mejora: nuevas, aplicadas, aparcadas o pendientes de aprobación.

### Mensual
- [ ] He revisado la ontología (¿necesita ajustes?).
- [ ] He revisado permisos de todos los agentes.
- [ ] He comprimido contexto obsoleto.
- [ ] He revisado datos stale en categoría operativa.
- [ ] He evaluado si el método necesita cambios.

### Trimestral
- [ ] He revisado la arquitectura de cerebros.
- [ ] He evaluado el rendimiento global de los agentes.
- [ ] He revisado métricas globales (MRR, churn, NPS si aplica).
- [ ] He actualizado el método si es necesario.
- [ ] He archivado Project Brains terminados.

---

*Este es el último documento de la serie principal. Para plantillas, schemas y registros, ver las carpetas `templates/`, `schemas/` y `registry/`.*

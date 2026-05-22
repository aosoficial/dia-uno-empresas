# Cómo ejecutar la reunión operativa semanal

Guía paso a paso para la cadencia semanal de revisión. Esta reunión conecta Receipts, StateChanges, scorecard y el siguiente sprint en un ciclo regular.

## Para quién es esto

Un operador que ya completó al menos un loop interno (Context Packet → acción → Receipt → scorecard) y quiere mantener una cadencia de mejora continua.

Requisitos previos:

- al menos 1 Receipt de la semana (o justificación de por qué no hay);
- acceso al scorecard (`company/company-scorecard.md`);
- acceso al plan de sprint (`company/guided-pilot-plan.md`).

## Qué vas a conseguir

Al final de cada reunión semanal tendrás:

1. Revisión de Receipts de la semana con veredictos.
2. StateChanges registrados si algo cambió.
3. Scorecard actualizado con evidencia real.
4. Siguiente sprint seleccionado con tarea concreta.
5. Bloqueos identificados con responsable.

## Cuándo hacerla

Elige un día y hora fijos. La regularidad importa más que la duración. 30 minutos suelen bastar para un equipo pequeño.

Sugerencia: viernes por la mañana o lunes primera hora, según preferencia.

---

## Antes de la reunión (5 min de preparación)

Abre estos archivos de tu instancia:

1. `receipts/` — Receipts de la semana.
2. `statechanges/` — StateChanges de la semana.
3. `company/company-scorecard.md` — scorecard actual.
4. `company/guided-pilot-plan.md` — sprint actual.

Si trabajas solo, la "reunión" es una revisión individual con la misma estructura.

---

## Bloque 1 — Revisar Receipts (10 min)

Para cada Receipt de la semana:

| Pregunta | Acción si falla |
|---|---|
| ¿Tiene resultado real, no solo "completado"? | Reescribir outcome con datos concretos |
| ¿Fue verificado por una persona? | Verificar ahora o fijar responsable |
| ¿El status refleja el resultado real? | Corregir status |
| ¿Generó StateChanges que no se registraron? | Crear StateChanges pendientes |

Si no hay Receipts de la semana, pregunta: ¿hubo acción operativa? Si sí, falta documentación. Si no, el sprint fue demasiado ambicioso o hubo un bloqueo.

**Salida:** todos los Receipts de la semana verificados y cerrados.

---

## Bloque 2 — Revisar StateChanges (5 min)

Para cada StateChange de la semana:

- ¿La razón es específica, no genérica?
- ¿El cambio se refleja en la fuente de verdad correspondiente?
- ¿Se necesita sincronizar con otro cerebro o sistema?

Si hay cambios no registrados detectados en la revisión de Receipts, créalos ahora.

**Salida:** StateChanges completos y coherentes con la memoria operativa.

---

## Bloque 3 — Actualizar scorecard (5 min)

Abre `company/company-scorecard.md` y revisa:

| Pregunta | Acción |
|---|---|
| ¿Hay campos con valores placeholder que ahora tienen evidencia? | Actualizar con dato real, fecha y fuente |
| ¿Algún indicador mejoró esta semana? | Registrar valor anterior → valor nuevo con fecha |
| ¿Algún indicador empeoró? | Registrar y anotar causa probable |
| ¿Hay indicadores sin movimiento en más de 2 semanas? | Marcar como "sin evidencia reciente" |

Regla: el scorecard se actualiza desde Receipts y StateChanges, no desde intuición. Si no hay evidencia, el valor no cambia.

**Salida:** al menos 1 campo del scorecard actualizado con fecha y fuente.

---

## Bloque 4 — Seleccionar siguiente sprint (10 min)

Basándote en los Receipts, StateChanges y scorecard:

1. ¿Qué funcionó bien esta semana?
2. ¿Qué no funcionó o quedó incompleto?
3. ¿Qué bloqueo existe que impide avanzar?
4. ¿Cuál es la tarea de mayor impacto para la próxima semana?

Escribe el siguiente sprint en `company/guided-pilot-plan.md`:

```markdown
## Sprint semana [fecha]

**Tarea:** [descripción concreta]
**Resultado esperado:** [qué se producirá]
**Responsable:** [persona o agente]
**Fecha límite:** [fecha]
**Dependencias:** [qué se necesita antes]
**Evidencia de la semana anterior que motivó esta tarea:** [referencia a Receipt o StateChange]
```

**Salida:** sprint concreto con tarea, resultado, responsable y fecha.

---

## Bloque 5 — Bloqueos (si los hay)

Si hay un bloqueo que no puedes resolver:

1. Descríbelo en 1-2 frases.
2. Identifica responsable o siguiente acción.
3. Si necesitas ayuda externa, usa la plantilla de [`templates/dia-uno/blocker-report.md`](../dia-uno/blocker-report.md) sin incluir datos privados.

---

## Plantilla de acta rápida

Si quieres guardar un registro de la reunión (opcional pero recomendado), usa este formato en tu instancia:

```markdown
# Reunión operativa — [fecha]

## Receipts revisados
- [rcp-id]: [status final]
- [rcp-id]: [status final]

## StateChanges registrados
- [sc-id]: [resumen del cambio]

## Scorecard actualizado
- [indicador]: [valor anterior] → [valor nuevo] (fuente: [receipt/statechange])

## Siguiente sprint
- Tarea: [descripción]
- Responsable: [nombre]
- Fecha: [fecha]

## Bloqueos
- [descripción del bloqueo, si existe]
```

Guarda en tu instancia, por ejemplo en `receipts/weekly-review-[fecha].md` o una carpeta `meetings/`.

---

## Errores comunes

| Error | Consecuencia | Solución |
|---|---|---|
| No hacer la reunión | Se pierde la cadencia y la evidencia se acumula sin revisar | Fijar día/hora y proteger el bloque |
| Actualizar scorecard sin evidencia | Los números no reflejan la realidad | Solo actualizar desde Receipts y StateChanges |
| Sprint sin tarea concreta | La semana siguiente no tiene foco | Definir tarea, resultado y fecha siempre |
| No registrar bloqueos | Los problemas persisten sin visibilidad | Anotar bloqueos aunque no tengan solución inmediata |
| Reunión de más de 45 min | Se convierte en sesión de trabajo, no de revisión | Limitar a revisión y decisiones; el trabajo se hace fuera |

---

## Siguiente paso

Repite este ciclo cada semana. Después de 4 semanas, revisa si la cadencia funciona o necesita ajuste. Consulta [`select-scorecard-metrics.md`](select-scorecard-metrics.md) si necesitas añadir o cambiar indicadores del scorecard.

Para el flujo completo del primer loop, consulta [`run-first-internal-loop.md`](run-first-internal-loop.md).

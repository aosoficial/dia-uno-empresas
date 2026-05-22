# Cómo crear el primer Receipt

Guía paso a paso para documentar el resultado de una acción operativa. Un Receipt es la evidencia de que un agente (o humano) completó una acción y cuál fue el resultado real.

## Para quién es esto

Un operador que acaba de ejecutar una tarea (o cuyo empleado digital la ejecutó) y necesita registrar el resultado antes de que se pierda.

Requisitos previos:

- una acción ejecutada con resultado observable;
- un Context Packet que definía la tarea (recomendado, no obligatorio);
- una revisión humana del resultado (puede hacerse en el momento).

## Qué vas a conseguir

Un archivo `receipts/rcp-[id].md` en tu instancia privada con resultado real observado, verificación humana y trazabilidad al Context Packet de origen.

## Por qué importa

Sin Receipt, una tarea "completada" no tiene evidencia. El validador operativo (`validate_point_b_readiness.py --mode operational`) requiere al menos un Receipt no-placeholder para pasar. El scorecard se actualiza desde Receipts, no desde suposiciones.

---

## Paso 1 — Recoger el resultado real

Antes de escribir el Receipt, responde:

1. ¿Qué hizo exactamente el agente (o la persona)?
2. ¿Qué produjo? (archivo, borrador, tabla, análisis, decisión)
3. ¿El resultado cumple lo que pedía el Context Packet?
4. ¿Hubo incidencias, limitaciones o sorpresas?

Regla: "completado" no es un resultado. "Checklist de 12 pasos generada, falta paso de hashtags detectado en revisión" sí lo es.

**Criterio de salida:** puedes describir el resultado en 1-3 frases concretas.

---

## Paso 2 — Hacer la revisión humana

Una persona revisa el output y responde:

- ¿Es correcto? → `resultado_verificacion: correcto`
- ¿Es parcialmente correcto? → `resultado_verificacion: parcial`
- ¿Es incorrecto? → `resultado_verificacion: incorrecto`

Anota quién revisó y cuándo. Si tú eres el único operador, tú revisas.

**Criterio de salida:** tienes un veredicto (correcto / parcial / incorrecto) con nombre y fecha.

---

## Paso 3 — Escribir el Receipt

Usa la plantilla de [`templates/receipts/receipt-template.md`](../receipts/receipt-template.md).

Campos mínimos obligatorios:

```yaml
id: "rcp-[agente]-[fecha]-001"
agent: "[quién ejecutó la acción]"
action: "[qué hizo, en 1 frase concreta]"
timestamp: "[cuándo se ejecutó, ISO 8601]"
inputs:
  context_packet: "[id del Context Packet, si existe]"
outputs:
  - "[qué se produjo: archivo, borrador, tabla, etc.]"
outcome: "[resultado real observado, con datos concretos]"
status: "[exito / exito_parcial / fallo / pendiente_verificacion]"
verificacion:
  verificado_por: "[nombre de quien revisó]"
  fecha_verificacion: "[cuándo revisó, ISO 8601]"
  resultado_verificacion: "[correcto / parcial / incorrecto]"
  notas: "[observaciones de la revisión]"
```

Guarda en tu instancia: `receipts/rcp-[id].md`

### Guía rápida de status

| Status | Cuándo usarlo |
|---|---|
| `exito` | Resultado verificado como correcto |
| `exito_parcial` | Completado pero con limitaciones |
| `fallo` | Se intentó pero no se logró |
| `pendiente_verificacion` | Completado pero nadie ha revisado aún |
| `rechazado` | Revisado y rechazado por el operador |
| `cancelado` | Abortado antes de completar |

**Criterio de salida:** archivo guardado, sin placeholders, con resultado real (no "completado"), verificación con persona y fecha.

---

## Paso 4 — Verificar antes de cerrar

Checklist rápido:

- [ ] ¿El `id` es único y sigue el patrón `rcp-[agente]-[fecha]-NNN`?
- [ ] ¿`agent` identifica a quien ejecutó la acción?
- [ ] ¿`action` describe la acción en 1 frase concreta?
- [ ] ¿`timestamp` tiene fecha y hora ISO 8601?
- [ ] ¿`inputs` referencia el Context Packet o las instrucciones recibidas?
- [ ] ¿`outputs` lista los entregables concretos?
- [ ] ¿`outcome` describe el resultado real, no solo "completado"?
- [ ] ¿`status` refleja el resultado de la verificación?
- [ ] ¿`verificacion` tiene persona, fecha y veredicto?
- [ ] ¿No contiene secretos ni datos de clientes reales sin anonimizar?

---

## Paso 5 — Derivar acciones del Receipt

Según el resultado:

| Resultado | Siguiente paso |
|---|---|
| `exito` | Actualizar scorecard, seleccionar siguiente sprint |
| `exito_parcial` | Corregir y crear nueva iteración; actualizar scorecard con resultado parcial |
| `fallo` | Diagnosticar causa, ajustar Context Packet, reintentar |
| `rechazado` | Revisar restricciones o permisos; ajustar antes de reintentar |

Si la acción cambió datos operativos del sistema, crea un StateChange: consulta [`create-first-statechange.md`](create-first-statechange.md).

---

## Errores comunes

| Error | Consecuencia | Solución |
|---|---|---|
| "Outcome: completado" | No se sabe si fue correcto | Describir resultado con datos concretos |
| No referenciar el Context Packet | No se puede trazar la cadena de decisión | Siempre incluir `context_packet` en inputs |
| No verificar después | Receipt queda en "pendiente" indefinidamente | Verificar en el momento o fijar fecha límite |
| Crear Receipts para todo | Ruido; nadie los lee | Solo para acciones con impacto operativo |
| Confundir Receipt con StateChange | Se pierde la distinción entre acción y cambio de estado | Receipt = qué se hizo; StateChange = qué cambió en la memoria |

---

## Siguiente paso

Si la acción cambió datos del sistema, crea un StateChange: [`create-first-statechange.md`](create-first-statechange.md).

Si no hubo cambio de estado, actualiza el scorecard y selecciona el siguiente sprint: [`run-first-internal-loop.md`](run-first-internal-loop.md) pasos 6-8.

Para la cadencia de revisión semanal de Receipts y scorecard, consulta [`run-weekly-operating-meeting.md`](run-weekly-operating-meeting.md).

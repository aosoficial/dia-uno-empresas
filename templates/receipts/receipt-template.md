# Receipt (Recibo de Acción)

## Qué es un Receipt

Un Receipt es la evidencia de que un agente (o humano) completó una acción. No es un log técnico: es un registro operativo que permite verificar qué se hizo, con qué resultado y si fue correcto.

**Principio fundamental:** "Completado" no significa "exitoso". Un Receipt debe registrar el resultado real, no solo que la tarea se ejecutó.

## Cuándo crear un Receipt

- Cada vez que un agente ejecuta una tarea que tiene impacto operativo.
- Cada vez que un agente completa un handoff a otro agente o humano.
- Cada vez que un agente toma una decisión dentro de su autonomía.
- Cada vez que el operador aprueba o rechaza una acción.

## Cuándo NO crear un Receipt

- Para consultas de lectura simples que no producen ningún cambio ni output.
- Para pasos intermedios de una tarea (solo el resultado final necesita Receipt).
- Para logs técnicos o de sistema (eso es telemetría, no un Receipt).

---

## Plantilla

```yaml
# === RECEIPT ===

id: "[COMPLETAR — identificador único, ejemplo: rcp-vega-2026-05-08-001]"

# Quién actuó
agent: "[COMPLETAR — identificador del agente, ejemplo: agente/vega]"

# Qué hizo
action: "[COMPLETAR — descripción concisa de la acción, ejemplo: Generar propuesta comercial para Atlas Logistics]"

# Cuándo
timestamp: "[COMPLETAR — ISO 8601, ejemplo: 2026-05-08T14:30:00Z]"

# Qué recibió como entrada
inputs:
  context_packet: "[COMPLETAR — referencia al Context Packet, si aplica]"
  instrucciones: "[COMPLETAR — instrucciones recibidas del operador, si aplica]"
  datos_consultados:
    - "[COMPLETAR — cerebros o fuentes consultadas]"

# Qué produjo
outputs:
  - "[COMPLETAR — lista de entregables, archivos, datos modificados]"

# Resultado observado
outcome: "[COMPLETAR — resultado real, no solo 'completado'. Ejemplo: 'Propuesta generada con 3 líneas de producto. Stock verificado. Descuento 10% aplicado dentro de política.']"

# Estado
status: "[COMPLETAR — uno de los valores de abajo]"
# Valores posibles:
#   exito              — acción completada con resultado correcto verificado
#   exito_parcial      — acción completada pero con limitaciones o incidencias
#   fallo              — acción intentada pero no se logró el resultado
#   pendiente_verificacion — acción completada pero pendiente de revisión humana
#   rechazado          — acción preparada pero rechazada por el operador
#   cancelado          — acción cancelada antes de completarse

# Verificación (completar después de la revisión)
verificacion:
  verificado_por: "[COMPLETAR — quién verificó el resultado]"
  fecha_verificacion: "[COMPLETAR — cuándo se verificó]"
  resultado_verificacion: "[COMPLETAR — correcto / incorrecto / parcial]"
  notas: "[COMPLETAR — observaciones de la verificación]"

# Metadata
tags:
  - "[COMPLETAR — etiquetas para clasificar, ejemplo: ventas, propuesta, atlas-logistics]"
statechanges_generados:
  - "[COMPLETAR — IDs de StateChanges creados como resultado de esta acción, si los hay]"
```

---

## Campos obligatorios vs. opcionales

| Campo | Obligatorio | Descripción |
|-------|------------|-------------|
| id | Sí | Identificador único del Receipt |
| agent | Sí | Quién actuó |
| action | Sí | Qué hizo |
| timestamp | Sí | Cuándo |
| inputs | Sí | Qué recibió (al menos la referencia al Context Packet o instrucciones) |
| outputs | Sí | Qué produjo |
| outcome | Sí | Resultado real observado |
| status | Sí | Estado del resultado |
| verificacion | No (pero recomendado) | Se completa después, cuando se verifica |
| tags | No | Para clasificación y búsqueda |
| statechanges_generados | No | Solo si la acción generó cambios de estado |

---

## Valores de status: cuándo usar cada uno

| Status | Cuándo usarlo | Ejemplo |
|--------|-------------|---------|
| `exito` | El resultado fue verificado como correcto | Propuesta enviada y confirmada recibida |
| `exito_parcial` | Se completó pero con limitaciones | Propuesta generada pero faltaba un dato de stock |
| `fallo` | Se intentó pero no se logró | No se pudo acceder al CRM por error de conexión |
| `pendiente_verificacion` | Se completó pero nadie ha revisado el resultado | Propuesta generada, pendiente de revisión del operador |
| `rechazado` | El operador revisó y decidió que no procede | Propuesta preparada pero rechazada por error en pricing |
| `cancelado` | Se abortó antes de completar | Se canceló porque el cliente comunicó que ya no le interesa |

---

## Ejemplo completo — Meridian Foods

```yaml
id: "rcp-oliva-2026-05-08-003"

agent: "agente/oliva"
action: "Generar propuesta comercial para Distribuidora Norte"

timestamp: "2026-05-08T11:20:00Z"

inputs:
  context_packet: "cp-dist-norte-2026-05-08"
  instrucciones: "Preparar propuesta para 2.000 unidades de aceite premium y 1.500 de conservas"
  datos_consultados:
    - "Sales Brain: datos del cliente, historial de compras"
    - "Operations Brain: stock actual de aceite premium y conservas"
    - "Company Brain: política de descuentos vigente"

outputs:
  - "propuesta_dist_norte_v1.pdf (borrador)"
  - "resumen ejecutivo de la propuesta (3 párrafos)"
  - "nota: stock de aceite premium verificado OK (3.200 unidades), conservas verificado OK (2.100 unidades)"

outcome: >
  Propuesta generada con 2 líneas de producto. Stock verificado para ambas líneas.
  Descuento del 8% aplicado (dentro de la política del 10% máximo sin aprobación).
  Plazo de entrega estimado: 10 días laborables según Operations Brain.
  Pendiente de revisión por Carlos Martín antes de enviar al cliente.

status: "pendiente_verificacion"

verificacion:
  verificado_por: "Carlos Martín"
  fecha_verificacion: "2026-05-08T16:00:00Z"
  resultado_verificacion: "correcto"
  notas: "Aprobada sin cambios. Enviar al cliente mañana por la mañana."

tags:
  - ventas
  - propuesta
  - distribuidora-norte
  - aceite-premium
  - conservas

statechanges_generados:
  - "sc-pipeline-dist-norte-2026-05-08 (pipeline actualizado: propuesta enviada)"
```

---

## Errores comunes

| Error | Consecuencia | Cómo evitarlo |
|-------|-------------|---------------|
| Escribir "completado" como outcome | No sabes si el resultado fue correcto | Describir el resultado real con datos concretos |
| No incluir los inputs | No se puede trazar la cadena de decisión | Siempre referenciar el Context Packet o las instrucciones |
| No verificar después | El Receipt queda en "pendiente" para siempre | Configurar recordatorio de verificación |
| Crear Receipts para todo | Ruido excesivo, nadie los lee | Solo para acciones con impacto operativo |
| No generar StateChanges cuando corresponde | El cambio ocurrió pero no se registró en la memoria | Si la acción cambió datos, crear el StateChange correspondiente |

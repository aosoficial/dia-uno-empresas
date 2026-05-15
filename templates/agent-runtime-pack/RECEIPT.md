# Receipt

## Evidencia de accion del agente

---

## Que es

Un Receipt es la evidencia de que el agente ejecuto una accion y cual fue el resultado real. Responde a la pregunta: "Que hizo el agente y que paso?"

RECEIPT.md define la estructura de los Receipts que produce este agente, los estados posibles y un ejemplo de referencia.

**Un agente sin Receipts opera en la sombra.** No hay forma de saber que hizo, si lo hizo bien ni como mejorarlo.

## Cuando usarlo

- Despues de cada accion significativa del agente.
- Al auditar las acciones del agente (revisar Receipts vs Context Packets).
- Al evaluar el rendimiento del agente (analizar Receipts del periodo).
- Al diagnosticar errores (el Receipt documenta que paso realmente).

## Campos obligatorios

| Campo | Obligatorio | Descripcion |
|-------|------------|-------------|
| `id` | Si | Identificador unico del Receipt |
| `agent` | Si | Que agente ejecuto la accion |
| `action` | Si | Que accion se ejecuto |
| `timestamp` | Si | Cuando |
| `inputs` | Si | Que datos uso (Context Packet, instrucciones) |
| `outputs` | Si | Que produjo (documentos, datos, mensajes) |
| `outcome` | Si | Que paso realmente (resultado observado) |
| `status` | Si | Estado del resultado |
| `verification` | No | Revision del operador |
| `corrections` | No | Correcciones aplicadas |

## Estados posibles

| Estado | Significado |
|--------|-------------|
| `exito` | La accion se completo y el resultado observado es correcto |
| `exito_parcial` | Se completo pero requiere ajustes o seguimiento |
| `fallo` | La accion no produjo el resultado esperado |
| `pendiente_verificacion` | Completada pero no revisada por el operador |
| `rechazado` | El operador reviso y rechazo el resultado |

---

## Plantilla

```yaml
# --- Receipt ---

id: "rcp-[AGENTE]-[FECHA]-[SECUENCIAL]"
agent: "agente/[COMPLETAR]"
action: "[COMPLETAR — Que accion se ejecuto]"
timestamp: "[COMPLETAR]"  # Formato: YYYY-MM-DDTHH:MM:SSZ

inputs:
  context_packet: "[COMPLETAR — ID del Context Packet usado, si aplica]"
  instrucciones_adicionales: "[COMPLETAR — Instrucciones que no estaban en el Context Packet]"
  datos_consultados:
    - "[COMPLETAR — Fuente 1]"
    - "[COMPLETAR — Fuente 2]"

outputs:
  - "[COMPLETAR — Output 1: documento, dato, mensaje, etc.]"
  - "[COMPLETAR — Output 2]"

outcome: >
  [COMPLETAR — Que paso realmente. No solo "tarea completada".
  Describir el resultado observable, no la accion.]

status: "[COMPLETAR]"
# Valores: exito / exito_parcial / fallo / pendiente_verificacion / rechazado

verification:
  reviewed_by: "[COMPLETAR o null si no se ha revisado]"
  reviewed_at: "[COMPLETAR o null]"
  notes: "[COMPLETAR o null]"

corrections: "[COMPLETAR o null — Correcciones aplicadas tras revision]"

# --- Vinculacion ---

statechanges_generados:
  - "[COMPLETAR — IDs de StateChanges creados como resultado de esta accion]"

tarea_siguiente: "[COMPLETAR — Que debe pasar despues, si aplica]"
```

---

## Ejemplo — Receipts de Vega (Meridian Foods)

### Ejemplo 1: Propuesta generada con exito

```yaml
id: "rcp-vega-20260505-001"
agent: "agente/vega"
action: "Generar propuesta comercial para Costa Frutas"
timestamp: "2026-05-05T14:30:00Z"

inputs:
  context_packet: "cp-costafrutas-2026-05-05"
  instrucciones_adicionales: "Incluir modulo de pedidos en tiempo real como diferenciador"
  datos_consultados:
    - "Sales Brain: cliente/costa-frutas"
    - "Product Brain: producto/plan-business"

outputs:
  - "propuesta_costa_frutas_v1.pdf (borrador, 5 paginas)"
  - "resumen_ejecutivo.md (3 parrafos)"
  - "tabla_comparativa_vs_freshtrack.md"

outcome: >
  Borrador generado correctamente. Incluye Plan Business con descuento
  del 10% y modulo de pedidos en tiempo real como diferenciador.
  No se prometio integracion custom. Pendiente de revision por operador.

status: "pendiente_verificacion"

verification:
  reviewed_by: null
  reviewed_at: null
  notes: null

corrections: null

statechanges_generados:
  - "sc-costafrutas-20260505-001"

tarea_siguiente: "Esperar aprobacion del operador para envio de propuesta"
```

### Ejemplo 2: Accion con exito parcial

```yaml
id: "rcp-vega-20260506-001"
agent: "agente/vega"
action: "Enviar seguimiento a leads del evento FoodTech"
timestamp: "2026-05-06T10:00:00Z"

inputs:
  context_packet: "cp-foodtech-followup-2026-05-06"
  instrucciones_adicionales: "Usar plantilla de seguimiento post-evento"
  datos_consultados:
    - "Sales Brain: leads/foodtech-2026"

outputs:
  - "Email de seguimiento enviado a Verde Campo S.L."
  - "Email de seguimiento enviado a Frutas del Norte"
  - "Email a OliFresh NO enviado (email de contacto reboto)"

outcome: >
  2 de 3 emails de seguimiento enviados correctamente.
  OliFresh tiene email de contacto invalido. Necesita verificacion.

status: "exito_parcial"

verification:
  reviewed_by: "carlos.ruiz@meridianfoods.com"
  reviewed_at: "2026-05-06T11:30:00Z"
  notes: "OK los 2 envios. Buscar email correcto de OliFresh via LinkedIn."

corrections: "Buscar email actualizado de contacto de OliFresh."

statechanges_generados:
  - "sc-olifresh-20260506-001"  # Email de contacto marcado como invalido

tarea_siguiente: "Verificar email de OliFresh y reenviar seguimiento"
```

### Ejemplo 3: Accion fallida

```yaml
id: "rcp-vega-20260507-001"
agent: "agente/vega"
action: "Consultar precios actualizados del Plan Enterprise"
timestamp: "2026-05-07T09:00:00Z"

inputs:
  context_packet: null  # Tarea de rutina matutina
  instrucciones_adicionales: null
  datos_consultados:
    - "Product Brain: producto/plan-enterprise"

outputs: []

outcome: >
  No se pudo acceder al Product Brain. Error de conexion.
  Los precios en cache local tienen 8 dias (vencidos segun politica de 7 dias).

status: "fallo"

verification:
  reviewed_by: null
  reviewed_at: null
  notes: null

corrections: null

statechanges_generados: []

tarea_siguiente: "Reintentar acceso al Product Brain. Si persiste, notificar al operador."
```

---

## Errores comunes

1. **Outcome generico.** "Tarea completada" no es un outcome. "Propuesta generada con descuento del 10%, sin promesas de integracion custom" si lo es. El outcome describe el resultado observable.

2. **No registrar fallos.** Los fallos son tan importantes como los exitos. Un fallo sin Receipt es un fallo invisible que se repetira.

3. **Receipts sin vincular a Context Packets.** Si el agente actuo con un Context Packet, el Receipt debe referenciarlo. Sin esto, no se puede auditar si la accion fue coherente con el contexto.

4. **Verificacion que nunca llega.** Un Receipt en `pendiente_verificacion` permanente es un riesgo. Definir en OPERATIONS.md la frecuencia de revision de Receipts.

5. **No registrar correcciones.** Si el operador corrige un resultado, la correccion debe quedar en el Receipt. Las correcciones repetidas son senales de que algo debe cambiar en el agente (permisos, operaciones o SOUL).

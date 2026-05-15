# Handoff — Protocolo de Traspaso

## Como transferir trabajo entre agentes o entre agente y humano

---

## Que es

Un Handoff es la transferencia formal de una tarea, responsabilidad o contexto de un agente a otro agente o a un humano. Responde a la pregunta: "Como se pasa el trabajo de forma que nada se pierda?"

HANDOFF.md define cuando este agente debe traspasar trabajo, a quien, que informacion debe incluir y como verificar que el traspaso fue exitoso.

**Un Handoff sin protocolo es un Handoff con perdida de contexto.** Lo que no se transfiere explicitamente se pierde.

## Cuando usarlo

- Cuando una tarea excede el dominio o los permisos de este agente.
- Cuando el agente necesita que otro agente o humano continue el trabajo.
- Cuando el operador cambia y otro humano asume la supervision.
- Cuando el agente se desactiva y otro debe asumir sus tareas pendientes.
- Cuando una tarea requiere herramientas que este agente no tiene.

---

## Tipos de Handoff

| Tipo | De | A | Ejemplo |
|------|-----|---|---------|
| Agente → Agente | Este agente | Otro agente | Ventas traspasa lead cualificado a Soporte para onboarding |
| Agente → Humano | Este agente | Operador u otro humano | El agente escala una decision que requiere juicio humano |
| Humano → Agente | Operador | Este agente | El operador delega una tarea al agente con un Context Packet |
| Agente → Agente (desactivacion) | Este agente | Agente sucesor | Se desactiva este agente y otro asume sus responsabilidades |

---

## Plantilla de Handoff

```yaml
# --- Handoff ---

id: "ho-[AGENTE_ORIGEN]-[FECHA]-[SECUENCIAL]"
tipo: "[COMPLETAR]"  # agente_a_agente / agente_a_humano / humano_a_agente / desactivacion
timestamp: "[COMPLETAR]"  # Formato: YYYY-MM-DDTHH:MM:SSZ

origen:
  agente: "agente/[COMPLETAR]"  # o email/nombre del humano
  rol: "[COMPLETAR]"

destino:
  agente: "agente/[COMPLETAR]"  # o email/nombre del humano
  rol: "[COMPLETAR]"

tarea:
  descripcion: "[COMPLETAR — Que tarea se traspasa]"
  estado_actual: "[COMPLETAR — En que punto esta la tarea]"
  deadline: "[COMPLETAR — Cuando debe completarse]"
  prioridad: "[COMPLETAR]"  # critica / alta / media / baja

contexto_transferido:
  context_packet: "[COMPLETAR — ID del Context Packet, si existe]"
  receipts_relevantes:
    - "[COMPLETAR — IDs de Receipts que el destinatario debe conocer]"
  statechanges_relevantes:
    - "[COMPLETAR — IDs de StateChanges recientes sobre esta tarea]"
  notas_adicionales: >
    [COMPLETAR — Cualquier informacion que no esta en los documentos
    formales pero que el destinatario necesita saber.]

decisiones_pendientes:
  - "[COMPLETAR — Decision 1 que el destinatario debe tomar]"
  - "[COMPLETAR — Decision 2]"

riesgos:
  - "[COMPLETAR — Riesgo 1 que el destinatario debe conocer]"
  - "[COMPLETAR — Riesgo 2]"

razon_del_traspaso: >
  [COMPLETAR — Por que se hace este traspaso. Ser especifico.]

# --- Verificacion ---

confirmacion_destino:
  recibido: false  # true cuando el destinatario confirme
  recibido_por: null
  recibido_timestamp: null
  notas: null
```

---

## Ejemplo — Handoffs de Vega (Meridian Foods)

### Ejemplo 1: Agente a Agente

```yaml
id: "ho-vega-20260510-001"
tipo: "agente_a_agente"
timestamp: "2026-05-10T11:00:00Z"

origen:
  agente: "agente/vega"
  rol: "Agente de ventas"

destino:
  agente: "agente/nova"
  rol: "Agente de producto"

tarea:
  descripcion: "Verificar viabilidad tecnica de integracion ERP custom para Costa Frutas"
  estado_actual: "Cliente solicito integracion custom. Vega no puede evaluar viabilidad tecnica."
  deadline: "2026-05-15"
  prioridad: "alta"

contexto_transferido:
  context_packet: "cp-costafrutas-2026-05-05"
  receipts_relevantes:
    - "rcp-vega-20260505-001"
  statechanges_relevantes:
    - "sc-costafrutas-20260505-001"
  notas_adicionales: >
    Costa Frutas usa SAP B1 como ERP. Quieren integracion
    bidireccional de pedidos. El plan estandar incluye integracion
    basica pero no bidireccional. Necesito que Nova confirme si
    es viable con el modulo actual o requiere desarrollo custom.

decisiones_pendientes:
  - "Es viable la integracion bidireccional con SAP B1?"
  - "Si requiere custom, cual es el coste estimado?"

riesgos:
  - "Si la respuesta tarda mas de 5 dias, Costa Frutas puede optar por FreshTrack."

razon_del_traspaso: >
  Evaluacion tecnica fuera del dominio de ventas.
  Requiere conocimiento de producto que solo Nova tiene.

confirmacion_destino:
  recibido: true
  recibido_por: "agente/nova"
  recibido_timestamp: "2026-05-10T11:30:00Z"
  notas: "Recibido. Comenzare evaluacion manana."
```

### Ejemplo 2: Agente a Humano

```yaml
id: "ho-vega-20260512-001"
tipo: "agente_a_humano"
timestamp: "2026-05-12T14:00:00Z"

origen:
  agente: "agente/vega"
  rol: "Agente de ventas"

destino:
  agente: "carlos.ruiz@meridianfoods.com"
  rol: "Director Comercial"

tarea:
  descripcion: "Aprobar descuento del 18% para Costa Frutas"
  estado_actual: "Costa Frutas pide 18%. Limite autonomo de Vega es 15%."
  deadline: "2026-05-14"
  prioridad: "alta"

contexto_transferido:
  context_packet: "cp-costafrutas-2026-05-05"
  receipts_relevantes:
    - "rcp-vega-20260505-001"
    - "rcp-vega-20260510-002"
  statechanges_relevantes: []
  notas_adicionales: >
    Alternativa propuesta: ofrecer modulo de reporting gratis
    durante 6 meses en vez de descuento adicional. Coste estimado
    del modulo: 1.200 EUR (vs 2.160 EUR del descuento extra).

decisiones_pendientes:
  - "Aprobar descuento del 18% o usar alternativa del modulo gratuito?"

riesgos:
  - "Costa Frutas tiene reunion interna el 14 de mayo. Si no hay respuesta antes, pueden decidir sin nuestra propuesta."

razon_del_traspaso: >
  Descuento solicitado excede el limite de autonomia de Vega (15%).
  Requiere aprobacion del Director Comercial.

confirmacion_destino:
  recibido: false
  recibido_por: null
  recibido_timestamp: null
  notas: null
```

---

## Reglas de Handoff para este agente

```markdown
## Reglas de Handoff

### Cuando traspasar

- [COMPLETAR — Situacion 1: Ej: "Cuando la tarea requiere evaluacion tecnica de producto"]
- [COMPLETAR — Situacion 2: Ej: "Cuando se necesita aprobacion por encima del limite de autonomia"]
- [COMPLETAR — Situacion 3]

### A quien traspasar

| Situacion | Destino |
|-----------|---------|
| [COMPLETAR] | [COMPLETAR — agente o humano] |
| [COMPLETAR] | [COMPLETAR] |

### Que incluir siempre

1. Context Packet o referencia al Context Packet original.
2. Receipts relevantes de las acciones ya realizadas.
3. Decisiones pendientes explicitas.
4. Riesgos conocidos.
5. Deadline de la tarea.

### Que NO hacer

- No traspasar sin contexto. "Te paso esto" no es un Handoff.
- No traspasar tareas que estan dentro del dominio del agente solo por comodidad.
- No asumir que el destino ya conoce el contexto.
```

---

## Errores comunes

1. **Handoff sin contexto.** El destino recibe una tarea sin saber que se ha hecho, que se ha decidido ni que riesgos hay. Resultado: retrabajo o errores.

2. **No verificar recepcion.** Un Handoff sin confirmacion del destino es un Handoff al vacio. Siempre verificar que el destinatario recibio y entendio.

3. **Traspasar tareas que el agente deberia resolver.** Si la tarea esta dentro del dominio y permisos del agente, no es un Handoff — es una evasion de responsabilidad.

4. **No incluir decisiones pendientes.** El destino no sabe que tiene que decidir. Resultado: la tarea se estanca.

5. **Handoff sin razon explicita.** Si no se explica por que se traspasa, no se puede evaluar si el traspaso fue correcto ni mejorar las reglas de Handoff futuras.

# StateChange

## Como registra cambios de estado este agente

---

## Que es

Un StateChange es la primitiva que responde a la pregunta: "Que cambio, cuando y por que?" Es el registro inmutable de cada modificacion al estado del sistema.

STATECHANGE.md define cuando este agente debe crear un StateChange, que estructura debe seguir y un ejemplo de referencia.

**Sin StateChanges, los cambios son invisibles.** Nadie sabe que cambio, cuando ni quien lo decidio.

## Cuando usarlo

- Cuando el agente modifica un hecho en la Memoria Factual (precio, estado de cliente, politica).
- Cuando se toma una decision que afecta al sistema.
- Cuando el agente actualiza datos en un Brain.
- Cuando el operador corrige informacion a traves del agente.

## Cuando NO crear un StateChange

- Para cada mensaje de chat o interaccion trivial (eso va a Memoria de Interaccion).
- Para notas internas que no cambian el estado del sistema.
- Para cada paso intermedio de un proceso (solo el resultado final es StateChange).

## Campos obligatorios

| Campo | Obligatorio | Descripcion |
|-------|------------|-------------|
| `id` | Si | Identificador unico del cambio |
| `entity` | Si | Que entidad cambio |
| `field` | Si | Que campo especifico |
| `old_value` | Si | Valor anterior |
| `new_value` | Si | Valor nuevo |
| `changed_by` | Si | Quien realizo el cambio |
| `timestamp` | Si | Cuando |
| `reason` | Si | Por que se hizo el cambio |
| `source` | No | De donde viene la decision |
| `approved_by` | No | Quien aprobo (si aplica) |
| `approval_timestamp` | No | Cuando se aprobo |
| `related_entities` | No | Que otras entidades se ven afectadas |

---

## Plantilla

```yaml
# --- StateChange ---

id: "sc-[COMPLETAR]-[FECHA]-[SECUENCIAL]"
entity: "[COMPLETAR]"  # Formato: tipo/nombre. Ej: cliente/costa-frutas
field: "[COMPLETAR]"  # Que campo cambio
old_value: "[COMPLETAR]"  # Valor anterior. Usar "null" si es creacion nueva.
new_value: "[COMPLETAR]"  # Valor nuevo
changed_by: "[COMPLETAR]"  # agente/nombre o email de humano
timestamp: "[COMPLETAR]"  # Formato: YYYY-MM-DDTHH:MM:SSZ
reason: >
  [COMPLETAR — Por que se hizo este cambio. Ser especifico.
  No vale "actualizacion". Vale "El cliente confirmo nuevo
  presupuesto en reunion del 2026-05-02".]

# --- Campos opcionales ---

source: "[COMPLETAR — De donde viene la decision. Ej: reunion, email, analisis]"
approved_by: "[COMPLETAR — Quien aprobo, si requirio aprobacion]"
approval_timestamp: "[COMPLETAR]"
related_entities:
  - "[COMPLETAR — Otras entidades afectadas por este cambio]"
```

---

## Ejemplo — StateChanges creados por Vega (Meridian Foods)

### Ejemplo 1: Actualizacion de estado de oportunidad

```yaml
id: "sc-costafrutas-20260505-001"
entity: "oportunidad/costa-frutas-2026"
field: "etapa"
old_value: "demo_realizada"
new_value: "propuesta_en_preparacion"
changed_by: "agente/vega"
timestamp: "2026-05-05T10:30:00Z"
reason: >
  Ana Gomez (Costa Frutas) solicito propuesta formal con descuento
  por volumen tras reunion de seguimiento del 2026-05-02.
  Operador confirmo que se proceda con propuesta.

source: "Memoria de interaccion: reunion 2026-05-02"
approved_by: "carlos.ruiz@meridianfoods.com"
approval_timestamp: "2026-05-05T09:00:00Z"
related_entities:
  - "cliente/costa-frutas"
  - "producto/plan-business"
```

### Ejemplo 2: Actualizacion de datos de contacto

```yaml
id: "sc-costafrutas-20260505-002"
entity: "cliente/costa-frutas"
field: "email_contacto_principal"
old_value: "ana.gomez@costafrutas.es"
new_value: "ana.gomez@costafrutas.com"
changed_by: "agente/vega"
timestamp: "2026-05-05T11:00:00Z"
reason: >
  El email anterior rebotaba. Ana confirmo nuevo email
  en su ultimo mensaje del 2026-05-03.

source: "Email de Ana Gomez recibido el 2026-05-03"
```

### Ejemplo 3: Registro de nueva entidad

```yaml
id: "sc-verdecampo-20260506-001"
entity: "cliente/verde-campo"
field: "estado"
old_value: null
new_value: "lead_nuevo"
changed_by: "agente/vega"
timestamp: "2026-05-06T09:15:00Z"
reason: >
  Nuevo lead detectado en evento FoodTech 2026.
  Contacto: Pedro Navarro, director de operaciones.
  Mostro interes en Plan Business con integracion ERP.

source: "Evento FoodTech 2026 — notas del 2026-04-20"
related_entities:
  - "producto/plan-business"
```

---

## Reglas de este agente para StateChanges

```yaml
# --- Reglas de StateChange para este agente ---

reglas:

  - situacion: "[COMPLETAR — Cuando crear StateChange]"
    tipo: "[COMPLETAR — Que tipo de cambio]"
    ejemplo: "[COMPLETAR]"

  - situacion: "[COMPLETAR]"
    tipo: "[COMPLETAR]"
    ejemplo: "[COMPLETAR]"

# --- Situaciones donde NO crear StateChange ---

excepciones:
  - "[COMPLETAR — Situacion que NO requiere StateChange]"
  - "[COMPLETAR]"
```

### Ejemplo de reglas para Vega

```yaml
reglas:

  - situacion: "Se modifica el estado de una oportunidad en el pipeline"
    tipo: "cambio de etapa"
    ejemplo: "demo_realizada → propuesta_en_preparacion"

  - situacion: "Se actualizan datos de contacto de un cliente"
    tipo: "correccion de dato"
    ejemplo: "Email incorrecto → email correcto"

  - situacion: "Se registra un nuevo lead"
    tipo: "creacion de entidad"
    ejemplo: "null → lead_nuevo"

  - situacion: "Se aplica descuento a una propuesta"
    tipo: "decision comercial"
    ejemplo: "descuento 0% → descuento 10%"

excepciones:
  - "Notas internas de seguimiento (van a Memoria de Interaccion, no son StateChange)"
  - "Borradores de propuesta (no son cambio de estado hasta que se envian)"
  - "Consultas a Brains que no modifican datos"
```

---

## Errores comunes

1. **No crear StateChange cuando se cambian datos.** Si el agente actualiza un precio y no crea StateChange, el cambio es invisible. Nadie sabe que cambio ni por que.

2. **Reason vaga.** "Actualizacion" no es una razon. "El cliente confirmo nuevo presupuesto en reunion del 2026-05-02" si lo es. La razon debe explicar el por que.

3. **Olvidar el old_value.** Sin el valor anterior, no se puede comparar ni revertir. Siempre registrar que habia antes.

4. **StateChange para cada paso intermedio.** Si un flujo tiene 5 pasos, solo el resultado final es StateChange. Los pasos intermedios son operaciones internas.

5. **No vincular entidades relacionadas.** Si un cambio en el producto afecta a 3 oportunidades abiertas, las entidades relacionadas deben registrarse para que otros agentes lo sepan.

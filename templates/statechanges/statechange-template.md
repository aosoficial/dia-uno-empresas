# StateChange (Cambio de Estado)

## Qué es un StateChange

Un StateChange registra que algo cambió en el sistema. Es el primitivo central de Company Brain System: la unidad mínima de cambio. Sin StateChanges, la memoria es una foto estática que puede estar obsoleta sin que nadie lo sepa.

**Principio fundamental:** si algo cambió y es relevante para la organización, debe quedar registrado como StateChange. Si no quedó registrado, es como si no hubiera pasado.

## Cuándo crear un StateChange

- Un dato de la memoria cambia de valor (precio, estado, owner, deadline).
- Se toma una decisión que modifica el estado de una entidad.
- Se crea una entidad nueva (con `old_value: null`).
- Se elimina una entidad (con `new_value: null`).
- Un agente detecta que un dato existente es incorrecto y lo corrige.
- Se resuelve un conflicto entre cerebros.
- Se actualiza una política, un permiso o una regla.

## Cuándo NO crear un StateChange

- Para registrar acciones de agentes (eso es un Receipt).
- Para registrar consultas de lectura que no cambian nada.
- Para anotar conversaciones o contexto (eso es Memoria de Interacción).
- Para datos temporales que no forman parte de la memoria operativa.
- Para micro-cambios sin impacto operativo (ejemplo: corregir una errata en una nota interna).

---

## Plantilla

```yaml
# === STATECHANGE ===

id: "[COMPLETAR — identificador único, ejemplo: sc-producto-plan-pro-2026-05-08-001]"

# Qué entidad cambió
entity: "[COMPLETAR — tipo/identificador de la entidad, ejemplo: producto/plan-pro]"

# Qué campo específico cambió
field: "[COMPLETAR — nombre del campo, ejemplo: precio_mensual]"

# Valor anterior
old_value: "[COMPLETAR — valor antes del cambio, o null si es creación]"

# Valor nuevo
new_value: "[COMPLETAR — valor después del cambio, o null si es eliminación]"

# Quién hizo el cambio
changed_by: "[COMPLETAR — persona o agente que realizó el cambio, ejemplo: clara@meridianfoods.com]"

# Cuándo
timestamp: "[COMPLETAR — ISO 8601, ejemplo: 2026-05-08T10:00:00Z]"

# Por qué
reason: "[COMPLETAR — razón del cambio. Debe ser específica, no genérica. Ejemplo: 'Alinear con nuevo benchmark de mercado tras análisis Q2', no 'Actualización'.]"

# Metadata opcional
source: "[COMPLETAR — de dónde viene la decisión: reunión, análisis, solicitud de cliente, detección automática]"
brain: "[COMPLETAR — en qué cerebro se registra: company_brain / sales_brain / etc.]"
sync: "[COMPLETAR — si debe sincronizarse: company_brain / local / null]"
receipt_relacionado: "[COMPLETAR — ID del Receipt que provocó este cambio, si aplica]"
aprobado_por: "[COMPLETAR — si requirió aprobación, quién la dio]"
tags:
  - "[COMPLETAR — etiquetas para clasificar]"
```

---

## Campos obligatorios vs. opcionales

| Campo | Obligatorio | Descripción |
|-------|------------|-------------|
| id | Sí | Identificador único |
| entity | Sí | Qué entidad cambió |
| field | Sí | Qué campo cambió |
| old_value | Sí | Valor anterior (null si es creación) |
| new_value | Sí | Valor nuevo (null si es eliminación) |
| changed_by | Sí | Quién hizo el cambio |
| timestamp | Sí | Cuándo |
| reason | Sí | Por qué cambió |
| source | No | Origen de la decisión |
| brain | No | En qué cerebro se registra |
| sync | No | Si debe sincronizarse con otro cerebro |
| receipt_relacionado | No | Receipt que provocó este cambio |
| aprobado_por | No | Solo si requirió aprobación |
| tags | No | Para clasificación |

---

## Tipos de StateChange

| Tipo | old_value | new_value | Ejemplo |
|------|-----------|-----------|---------|
| **Creación** | null | valor | Nueva entidad registrada |
| **Modificación** | valor anterior | valor nuevo | Precio cambia de 39 a 49 |
| **Eliminación** | valor anterior | null | Entidad eliminada |
| **Corrección** | valor incorrecto | valor correcto | Se detecta error y se corrige |
| **Conflicto resuelto** | valor en conflicto | valor verificado | Dos cerebros tenían datos distintos |

---

## Principios para buenos StateChanges

1. **Específico, no genérico.** `reason: "Actualización"` no sirve. `reason: "Alinear con benchmark de mercado Q2 tras análisis de competencia"` sí.
2. **Atómico.** Un StateChange = un campo que cambia. Si cambian 3 campos, son 3 StateChanges.
3. **Trazable.** Si lo provocó un Receipt, referenciarlo. Si lo provocó una reunión, indicarlo en `source`.
4. **Inmutable.** Un StateChange no se edita después de crearlo. Si el nuevo valor es incorrecto, se crea otro StateChange corrigiendo.
5. **Con reason siempre.** El "por qué" es más importante que el "qué". El "qué" se ve en old_value/new_value. El "por qué" se pierde si no se escribe.

---

## Ejemplo completo — Meridian Foods

### Cambio de precio

```yaml
id: "sc-producto-aceite-premium-2026-05-08-001"
entity: "producto/aceite-premium-500ml"
field: "precio_unitario"
old_value: 8.50
new_value: 9.20
changed_by: "laura@meridianfoods.com"
timestamp: "2026-05-08T09:15:00Z"
reason: >
  Incremento del 15% en coste de aceite de oliva virgen extra por escasez
  de cosecha. Aprobado en reunión de dirección del 2026-05-07.
  Nuevo precio mantiene margen mínimo del 25%.
source: "reunión de dirección 2026-05-07"
brain: "company_brain"
sync: null
receipt_relacionado: null
aprobado_por: "carlos@meridianfoods.com (Director General)"
tags:
  - pricing
  - aceite-premium
  - coste-materia-prima
```

### Nuevo cliente

```yaml
id: "sc-cliente-dist-norte-2026-05-08-001"
entity: "cliente/distribuidora-norte"
field: "estado"
old_value: null
new_value: "activo"
changed_by: "agente/oliva"
timestamp: "2026-05-08T16:30:00Z"
reason: >
  Distribuidora Norte firmó contrato anual por 120.000 euros.
  Primer pedido confirmado para la semana del 12 de mayo.
source: "firma de contrato"
brain: "sales_brain"
sync: "company_brain"
receipt_relacionado: "rcp-oliva-2026-05-08-007"
aprobado_por: "carlos.martin@meridianfoods.com (Director Comercial)"
tags:
  - nuevo-cliente
  - distribuidora-norte
  - contrato-anual
```

### Corrección de dato

```yaml
id: "sc-cliente-atlas-2026-05-08-001"
entity: "cliente/atlas-logistics"
field: "contacto_principal"
old_value: "María López"
new_value: "Ana Fernández"
changed_by: "agente/oliva"
timestamp: "2026-05-08T10:00:00Z"
reason: >
  María López dejó la empresa en abril 2026. Ana Fernández es la nueva
  directora de operaciones y contacto principal desde mayo 2026.
  Confirmado por email del cliente.
source: "email del cliente 2026-05-06"
brain: "sales_brain"
sync: "company_brain"
receipt_relacionado: null
aprobado_por: null
tags:
  - corrección
  - atlas-logistics
  - cambio-contacto
```

---

## Errores comunes

| Error | Consecuencia | Cómo evitarlo |
|-------|-------------|---------------|
| No registrar el cambio | La memoria no refleja la realidad | Regla: si cambió algo operativo, StateChange |
| Escribir "reason: actualización" | Nadie sabe por qué cambió | Exigir razón específica en cada StateChange |
| Agrupar varios cambios en un solo StateChange | No se puede trazar qué cambió exactamente | Un campo = un StateChange |
| Editar un StateChange existente | Se pierde el historial | Los StateChanges son inmutables |
| No sincronizar cuando debería subir | El Company Brain no refleja cambios importantes | Revisar SYNC_POLICY.md antes de decidir |
| Crear StateChanges para cosas triviales | Ruido excesivo | Solo para cambios con impacto operativo |

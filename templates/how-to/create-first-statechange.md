# Cómo crear el primer StateChange

Guía paso a paso para registrar un cambio de estado en el sistema operativo. Un StateChange es la unidad mínima de cambio: si algo cambió y es relevante para la organización, debe quedar registrado.

## Para quién es esto

Un operador que ha ejecutado una acción que cambió algo en la memoria operativa (un dato, una política, un permiso, un estado) y necesita registrarlo antes de que se pierda.

Requisitos previos:

- una acción ejecutada que cambió un dato operativo;
- un Receipt documentando esa acción (recomendado);
- saber qué entidad cambió, qué valor tenía antes y qué valor tiene ahora.

## Cuándo necesitas un StateChange

| Situación | ¿StateChange? |
|---|---|
| Un precio cambió | Sí |
| Se creó una nueva entidad (checklist, proceso, cliente) | Sí (`old_value: null`) |
| Se corrigió un dato incorrecto | Sí |
| Se cambió una política o permiso | Sí |
| Se eliminó algo del sistema | Sí (`new_value: null`) |
| Se generó un borrador sin cambiar datos | No (Receipt es suficiente) |
| Se hizo una consulta de lectura | No |

Regla: si algo cambió y es operativamente relevante, StateChange. Si solo se produjo un output sin cambiar datos del sistema, Receipt basta.

## Qué vas a conseguir

Un archivo `statechanges/sc-[id].md` en tu instancia privada con el cambio registrado de forma atómica, trazable y con razón específica.

---

## Paso 1 — Identificar qué cambió

Responde:

1. ¿Qué entidad cambió? (cliente, producto, proceso, política, etc.)
2. ¿Qué campo específico cambió? (precio, estado, owner, checklist, etc.)
3. ¿Cuál era el valor anterior? (`null` si es creación)
4. ¿Cuál es el valor nuevo? (`null` si es eliminación)

Regla de atomicidad: un StateChange = un campo que cambia. Si cambiaron 3 campos, crea 3 StateChanges.

**Criterio de salida:** puedes nombrar entidad, campo, valor anterior y valor nuevo.

---

## Paso 2 — Documentar la razón

La razón es el campo más importante del StateChange. El "qué" se ve en `old_value` / `new_value`. El "por qué" se pierde si no se escribe.

Buena razón: "Creación de primera checklist estándar de entrega para campañas RRSS, basada en retrospectiva del equipo del 2026-05-15."

Mala razón: "Actualización." / "Cambio." / "Se modificó."

**Criterio de salida:** la razón explica por qué se hizo el cambio, no solo que se hizo.

---

## Paso 3 — Escribir el StateChange

Usa la plantilla de [`templates/statechanges/statechange-template.md`](../statechanges/statechange-template.md).

Campos mínimos obligatorios:

```yaml
id: "sc-[entidad]-[campo]-[fecha]-NNN"
entity: "[tipo/identificador, ejemplo: proceso/entrega-campañas-rrss]"
field: "[campo que cambió, ejemplo: checklist_estandar]"
old_value: "[valor anterior, o null si es creación]"
new_value: "[valor nuevo, o null si es eliminación]"
changed_by: "[persona o agente que realizó el cambio]"
timestamp: "[cuándo, ISO 8601]"
reason: "[razón específica del paso 2]"
```

Campos opcionales recomendados:

```yaml
source: "[reunión, análisis, receipt, solicitud de cliente]"
receipt_relacionado: "[ID del Receipt que provocó este cambio]"
aprobado_por: "[si requirió aprobación, quién la dio]"
```

Guarda en tu instancia: `statechanges/sc-[id].md`

**Criterio de salida:** archivo guardado, sin placeholders, con razón específica.

---

## Paso 4 — Verificar antes de cerrar

Checklist rápido:

- [ ] ¿El `id` es único y descriptivo?
- [ ] ¿`entity` identifica la entidad con tipo/nombre?
- [ ] ¿`field` nombra el campo específico que cambió?
- [ ] ¿`old_value` refleja el valor anterior real (o `null` si es creación)?
- [ ] ¿`new_value` refleja el valor nuevo real (o `null` si es eliminación)?
- [ ] ¿`changed_by` identifica a quien hizo el cambio?
- [ ] ¿`timestamp` tiene fecha y hora ISO 8601?
- [ ] ¿`reason` explica el "por qué", no solo el "qué"?
- [ ] ¿Si hubo un Receipt relacionado, está referenciado?
- [ ] ¿Si requirió aprobación, está documentada?

---

## Tipos de StateChange

| Tipo | old_value | new_value | Ejemplo del primer loop |
|---|---|---|---|
| Creación | `null` | valor nuevo | Se creó una checklist de entrega que no existía |
| Modificación | valor anterior | valor nuevo | Se cambió el owner de un proceso |
| Corrección | valor incorrecto | valor correcto | Se detectó que un dato era erróneo |
| Eliminación | valor anterior | `null` | Se eliminó un proceso obsoleto |

Para el primer loop, lo más probable es una **creación** (se creó algo nuevo) o una **modificación** (se actualizó un dato).

---

## Errores comunes

| Error | Consecuencia | Solución |
|---|---|---|
| Razón genérica ("actualización") | Nadie sabe por qué cambió | Escribir razón específica con contexto |
| Agrupar varios campos en 1 StateChange | No se puede trazar qué cambió exactamente | 1 campo = 1 StateChange |
| Crear StateChange para cosas triviales | Ruido excesivo | Solo para cambios con impacto operativo |
| No referenciar el Receipt | Se pierde la trazabilidad | Incluir `receipt_relacionado` cuando aplique |
| Editar un StateChange existente | Se pierde el historial | Los StateChanges son inmutables; crear uno nuevo si hay corrección |

---

## Siguiente paso

Después de registrar el StateChange, actualiza el scorecard con la evidencia del cambio y selecciona el siguiente sprint: [`run-first-internal-loop.md`](run-first-internal-loop.md) pasos 6-8.

Para la revisión semanal de StateChanges, Receipts y scorecard, consulta [`run-weekly-operating-meeting.md`](run-weekly-operating-meeting.md).

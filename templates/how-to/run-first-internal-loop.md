# Cómo ejecutar el primer loop interno

Guía paso a paso para completar el primer ciclo operativo seguro después de instalar el scaffold.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- `validate_point_b_readiness.py --mode scaffold` pasando;
- Dirección / Mother Brain con propósito, oferta y prioridades rellenados;
- al menos un departamento con `department-brain.md`;
- al menos un empleado digital con `PERMISSIONS.md`.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md) y completa los pasos 1-4.

## Qué vas a conseguir

Al final de este how-to tendrás:

1. Un Context Packet real (no placeholder).
2. Una acción interna segura ejecutada.
3. Una revisión humana documentada.
4. Un Receipt con resultado observado.
5. Un scorecard actualizado con evidencia.
6. Un StateChange si algo cambió en el sistema.
7. El siguiente sprint seleccionado.

Esto es lo que necesitas para que `validate_point_b_readiness.py --mode operational` pase.

## Regla de seguridad

El primer loop solo permite acciones internas: redactar, analizar, ordenar, preparar, clasificar.

No permite: enviar, publicar, facturar, desplegar, contactar clientes, gastar dinero ni cambiar sistemas de producción.

Si dudas, aplica la regla:

> Acción externa, pública, económica, legal, de producción o con datos sensibles = requiere aprobación humana explícita.

---

## Paso 1 — Elegir una acción interna pequeña

Elige una tarea que:

- sea útil para tu negocio;
- no requiera contacto externo ni aprobación legal/económica;
- pueda completarse en una sesión;
- tenga un resultado verificable.

Buenos ejemplos:

| Tipo de empresa | Acción interna segura |
|---|---|
| Agencia | Redactar checklist de entrega para un tipo de proyecto |
| Consultoría | Preparar borrador de propuesta con datos sintéticos |
| Freelancer | Ordenar y clasificar servicios en una tabla de oferta |

Mal ejemplo: "Enviar propuesta al cliente" (requiere aprobación y contacto externo).

**Criterio de salida:** tienes una frase concreta que describe la tarea y su resultado esperado.

---

## Paso 2 — Crear el Context Packet

Para una guía detallada solo sobre este paso, consulta [`create-first-context-packet.md`](create-first-context-packet.md).

Usa la plantilla de [`templates/context-packets/context-packet-template.md`](../context-packets/context-packet-template.md).

Campos mínimos para el primer loop:

```yaml
id: "cp-[departamento]-[descripcion]-[fecha]"
target: "[agente o persona que ejecutará]"
task: "[la tarea concreta del paso 1]"
context:
  entidad_principal: "[sobre qué se trabaja]"
  datos_relevantes:
    - "[dato 1 con fuente y fecha de verificación]"
constraints:
  - "[al menos 1 restricción explícita]"
permissions:
  autonomo:
    - "[qué puede hacer sin pedir permiso]"
  requiere_aprobacion:
    - "[qué necesita visto bueno]"
  prohibido:
    - "[qué no puede hacer bajo ninguna circunstancia]"
freshness:
  fecha_paquete: "[fecha de hoy ISO 8601]"
expected_output: "[descripción concreta del entregable]"
```

Guarda el archivo en tu instancia privada: `context-packets/cp-[id].md`

**Criterio de salida:** el Context Packet tiene id, target, task, al menos un dato con fecha, al menos una restricción, permisos explícitos y resultado esperado concreto. No contiene placeholders tipo "COMPLETAR", "TBD" o "replace this".

---

## Paso 3 — Ejecutar la acción

Usa el empleado digital (o hazlo tú mismo siguiendo el Context Packet como guía).

Reglas:

- Sigue solo lo que dice el Context Packet.
- Respeta las restricciones y permisos.
- Si necesitas algo que no está en el Context Packet, para y complétalo primero.
- Genera el output descrito en `expected_output`.

Guarda el output en tu instancia privada (por ejemplo, en una carpeta `outputs/` o dentro del departamento correspondiente).

**Criterio de salida:** tienes un entregable concreto (borrador, checklist, tabla, análisis) guardado en la instancia.

---

## Paso 4 — Revisión humana

Una persona (tú u otro miembro del equipo) revisa el resultado.

Preguntas de verificación:

1. ¿El resultado cumple lo que pedía el Context Packet?
2. ¿Se respetaron las restricciones?
3. ¿Los datos usados tienen fecha y fuente verificable?
4. ¿El resultado es correcto y útil para el negocio?
5. ¿Hay algo que debería cambiar antes de considerar esto "hecho"?

Anota el resultado de la revisión: correcto, incorrecto o parcial.

**Criterio de salida:** una persona ha revisado el resultado y tiene un veredicto documentable.

---

## Paso 5 — Escribir el Receipt

Para una guía detallada solo sobre este paso, consulta [`create-first-receipt.md`](create-first-receipt.md).

Usa la plantilla de [`templates/receipts/receipt-template.md`](../receipts/receipt-template.md).

Campos mínimos:

```yaml
id: "rcp-[agente]-[fecha]-001"
agent: "[quién ejecutó]"
action: "[qué hizo]"
timestamp: "[cuándo, ISO 8601]"
inputs:
  context_packet: "[id del Context Packet del paso 2]"
outputs:
  - "[qué se produjo]"
outcome: "[resultado real observado, no solo 'completado']"
status: "[exito / exito_parcial / fallo / pendiente_verificacion]"
verificacion:
  verificado_por: "[quién revisó en el paso 4]"
  fecha_verificacion: "[cuándo]"
  resultado_verificacion: "[correcto / incorrecto / parcial]"
  notas: "[observaciones de la revisión]"
```

Guarda en tu instancia: `receipts/rcp-[id].md`

**Criterio de salida:** el Receipt tiene id, agent, action, timestamp, inputs con referencia al Context Packet, outputs, outcome con resultado real (no "completado"), status, y verificación con persona y fecha.

---

## Paso 6 — Actualizar el scorecard

Abre `company/company-scorecard.md` o `company/point-b-readiness.md` en tu instancia.

Actualiza al menos un campo con datos observados:

- Cambia valores placeholder por valores reales.
- Añade fecha de observación y fuente.
- Si un campo mejoró o empeoró, registra ambos valores.

**Criterio de salida:** al menos un campo del scorecard tiene un valor basado en evidencia real con fecha, no un placeholder.

---

## Paso 7 — Crear StateChange (si aplica)

Para una guía detallada solo sobre este paso, consulta [`create-first-statechange.md`](create-first-statechange.md).

Si la acción cambió algo en el sistema operativo (nuevo dato, nueva política, corrección de información), crea un StateChange usando [`templates/statechanges/statechange-template.md`](../statechanges/statechange-template.md).

Si la acción solo produjo un borrador interno sin cambiar datos del sistema, no necesitas StateChange.

Regla: si algo cambió y es operativamente relevante, StateChange. Si solo se produjo un output, Receipt es suficiente.

**Criterio de salida:** si hubo cambio operativo, existe un StateChange con entity, field, old_value, new_value, changed_by, timestamp y reason específica.

---

## Paso 8 — Seleccionar siguiente sprint

Abre `company/guided-pilot-plan.md` en tu instancia.

Basándote en lo que aprendiste del primer loop:

- ¿Qué funcionó bien?
- ¿Qué faltó en el Context Packet?
- ¿Qué restricción o permiso necesita ajuste?
- ¿Qué tarea sería el siguiente paso natural?

Escribe el próximo sprint como una tarea concreta con resultado esperado.

**Criterio de salida:** el plan tiene un siguiente sprint con tarea, resultado esperado y fecha objetivo.

---

## Paso 9 — Validar modo operativo

```bash
python scripts/validate_point_b_readiness.py --mode operational /tmp/mi-company-brain
```

Si pasa: tienes evidencia mínima de un primer loop interno revisado.

Si falla: lee los criterios que faltan en la salida del validador. Cada criterio te dice exactamente qué falta y dónde.

Errores comunes en este paso:

| Fallo del validador | Causa probable | Solución |
|---|---|---|
| "Operational context packet exists" falla | Context Packet tiene placeholders | Revisa que no queden "COMPLETAR", "TBD" o "placeholder" |
| "Operational receipt exists" falla | Receipt es solo el de instalación | Crea un Receipt para la acción del loop, no solo para la instalación del wizard |
| "Scorecard updated from evidence" falla | Scorecard tiene solo valores iniciales | Actualiza al menos un campo con dato real observado |
| "Source-of-truth map reviewed" falla | Mapa de fuentes tiene placeholders | Completa al menos una fuente con owner, freshness y permisos reales |

**Criterio de salida:** `validate_point_b_readiness.py --mode operational` pasa, o sabes exactamente qué falta.

---

## Ejemplo sintético completo — Agencia "Sol Digital"

### Contexto

Sol Digital es una agencia de marketing digital con 3 personas. Acaban de instalar el scaffold. Su primer departamento es Operaciones / Delivery. Su primer empleado digital se llama "agente/lara" y solo puede redactar y clasificar.

### Paso 1 — Acción elegida

"Crear checklist de entrega estándar para campañas de redes sociales."

### Paso 2 — Context Packet

```yaml
id: "cp-ops-checklist-entrega-2026-05-22"
target: "agente/lara"
task: "Crear checklist de entrega estándar para campañas de redes sociales"
context:
  entidad_principal: "proceso/entrega-campañas-rrss"
  datos_relevantes:
    - "Sol Digital entrega 8-12 campañas de RRSS al mes (fuente: registro interno, verificado 2026-05-20)"
    - "Errores frecuentes: falta de revisión de copy, imágenes sin aprobar, publicación sin horario (fuente: retrospectiva equipo, 2026-05-15)"
    - "Herramientas usadas: Canva, Meta Business, Google Sheets (fuente: equipo, verificado 2026-05-20)"
constraints:
  - "No incluir datos de clientes reales"
  - "No incluir precios ni condiciones contractuales"
permissions:
  autonomo:
    - "Redactar checklist basándose en el contexto proporcionado"
    - "Proponer categorías y orden de pasos"
  requiere_aprobacion:
    - "Publicar o compartir la checklist fuera del equipo"
  prohibido:
    - "Modificar procesos existentes sin revisión"
    - "Acceder a datos de clientes"
freshness:
  fecha_paquete: "2026-05-22T09:00:00Z"
  datos_mas_antiguos: "2026-05-15 (retrospectiva)"
expected_output: "Checklist con 10-15 pasos agrupados por fase (preparación, producción, revisión, publicación) en formato markdown"
```

### Paso 3 — Output

Lara genera un checklist de 12 pasos en 4 fases. Guardado en `departments/operations-delivery/outputs/checklist-entrega-rrss-v1.md`.

### Paso 4 — Revisión

Ana (fundadora) revisa: "Falta paso de verificación de hashtags. El resto está bien." Veredicto: parcial.

### Paso 5 — Receipt

```yaml
id: "rcp-lara-2026-05-22-001"
agent: "agente/lara"
action: "Crear checklist de entrega estándar para campañas RRSS"
timestamp: "2026-05-22T10:30:00Z"
inputs:
  context_packet: "cp-ops-checklist-entrega-2026-05-22"
outputs:
  - "departments/operations-delivery/outputs/checklist-entrega-rrss-v1.md (12 pasos, 4 fases)"
outcome: "Checklist generada con 12 pasos en 4 fases. Cubre preparación, producción, revisión y publicación. Falta paso de verificación de hashtags detectado en revisión."
status: "exito_parcial"
verificacion:
  verificado_por: "Ana García (fundadora)"
  fecha_verificacion: "2026-05-22T11:00:00Z"
  resultado_verificacion: "parcial"
  notas: "Añadir paso de verificación de hashtags entre revisión y publicación. Resto correcto."
```

### Paso 6 — Scorecard

En `company/company-scorecard.md`, Ana cambia:

- "Primer loop interno completado: no → sí (2026-05-22, receipt rcp-lara-2026-05-22-001)"
- "Calidad del primer output: parcial — faltó 1 paso, corregible en siguiente iteración"

### Paso 7 — StateChange

```yaml
id: "sc-proceso-checklist-rrss-2026-05-22"
entity: "proceso/entrega-campañas-rrss"
field: "checklist_estandar"
old_value: null
new_value: "departments/operations-delivery/outputs/checklist-entrega-rrss-v1.md"
changed_by: "agente/lara"
timestamp: "2026-05-22T10:30:00Z"
reason: "Creación de primera checklist estándar de entrega para campañas RRSS, basada en retrospectiva del equipo."
source: "primer loop interno"
receipt_relacionado: "rcp-lara-2026-05-22-001"
```

### Paso 8 — Siguiente sprint

"Corregir checklist añadiendo paso de hashtags. Probar con la siguiente campaña real (solo verificación interna, sin cambiar proceso de cara al cliente todavía). Fecha: 2026-05-29."

### Paso 9 — Validación

```bash
python scripts/validate_point_b_readiness.py --mode operational /tmp/sol-digital-brain
# Resultado esperado: pasa si todos los archivos tienen contenido real, no placeholders.
```

---

## Resumen de criterios de salida

| Paso | Criterio | Archivo en instancia |
|---|---|---|
| 1. Elegir acción | Tarea concreta con resultado verificable | (decisión, no archivo) |
| 2. Context Packet | Campos mínimos sin placeholders | `context-packets/cp-*.md` |
| 3. Ejecutar | Output concreto guardado | `outputs/` o departamento |
| 4. Revisión humana | Veredicto: correcto / parcial / incorrecto | (documentado en Receipt) |
| 5. Receipt | Resultado real observado, verificación con persona y fecha | `receipts/rcp-*.md` |
| 6. Scorecard | Al menos 1 campo con evidencia real y fecha | `company/company-scorecard.md` |
| 7. StateChange | Si hubo cambio operativo, registrado | `statechanges/sc-*.md` (si aplica) |
| 8. Siguiente sprint | Tarea concreta con fecha | `company/guided-pilot-plan.md` |
| 9. Validación | `--mode operational` pasa o gaps claros | (comando) |

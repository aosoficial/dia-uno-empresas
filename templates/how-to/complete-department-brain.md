# Cómo completar un Department Brain

Guía paso a paso para convertir un department-brain.md generado por el wizard en un departamento operativo con workflows, scorecard, escalación y owner.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- departamento elegido con [`choose-first-department.md`](choose-first-department.md);
- `department-brain.md` generado (con placeholders).

Si no tienes esto, vuelve a [`choose-first-department.md`](choose-first-department.md).

## Qué produce

Un `departments/[departamento]/department-brain.md` en tu instancia privada con:

1. Owner humano asignado.
2. Síntomas de Punto A reales (no placeholders).
3. Al menos un workflow documentado con trigger, pasos y output.
4. Scorecard con métricas observables.
5. Ruta de escalación definida.
6. Conexión con `company/roles-and-responsibilities.md` y `company/approval-boundaries.md`.

---

## Antes de empezar

Abre el `department-brain.md` generado en tu instancia. Verás secciones con `{{ placeholders }}` y texto como "draft until reviewed". Tu trabajo es reemplazar esos placeholders con información real.

No necesitas completar todo a la perfección. El objetivo es que el departamento sea operable para un primer loop, no que esté perfecto.

---

## Paso 1 — Asignar owner humano

Reemplaza `{{ department_owner }}` con el nombre de la persona responsable.

Reglas:

- El owner debe ser una persona real, no un agente digital.
- El owner es quien revisa receipts, aprueba cambios y escala problemas.
- Si el fundador es el owner, escríbelo explícitamente. No dejes el campo vacío.

**Criterio de salida:** el campo `Human owner` tiene un nombre real.

---

## Paso 2 — Describir el estado actual (Punto A)

Reemplaza `{{ point_a_symptoms }}` con los problemas reales del departamento.

Preguntas guía:

- ¿Qué tarea se repite cada semana y consume demasiado tiempo?
- ¿Dónde se producen errores, retrabajos o quejas recurrentes?
- ¿Qué información se pierde o se busca repetidamente?
- ¿Qué depende demasiado de una sola persona?

Ejemplo bueno: "Las entregas de campañas no tienen checklist; 3 de cada 10 salen con errores de copy."

Ejemplo malo: "El departamento podría mejorar." (demasiado vago, no verificable).

**Criterio de salida:** al menos 2-3 síntomas concretos con frecuencia o impacto observable.

---

## Paso 3 — Documentar herramientas y fuentes

Reemplaza `{{ current_tools }}` y `{{ active_processes }}` con las herramientas y procesos reales.

Para cada herramienta, indica:

- nombre;
- para qué se usa en este departamento;
- quién tiene acceso.

Enlaza a `company/source-of-truth-map.md` para el detalle completo de fuentes, permisos y frescura. Si no tienes el mapa de fuentes, créalo primero con [`create-source-of-truth-map.md`](create-source-of-truth-map.md).

**Criterio de salida:** las herramientas principales del departamento están listadas con uso y acceso.

---

## Paso 4 — Definir al menos un workflow

Un workflow es un proceso repetible con trigger, pasos y output. El department-brain generado tiene una sección de "Responsibilities" pero no workflows concretos.

Añade una sección `## Workflows` con al menos un workflow:

```markdown
## Workflows

### Workflow 1 — (nombre del proceso)

- **Trigger:** (qué lo inicia — ej: "cliente firma contrato", "lunes a las 9h")
- **Input:** (qué necesita para empezar — ej: "brief del cliente, checklist de entrega")
- **Pasos:**
  1. (paso concreto — quién lo ejecuta)
  2. (paso concreto)
  3. (paso concreto)
- **Output:** (qué se produce — ej: "entrega verificada con checklist firmada")
- **Owner:** (persona responsable del workflow)
- **Revisión humana:** (en qué paso se revisa antes de avanzar)
- **Escalación:** (cuándo y a quién se escala si algo falla)
```

Para una guía más detallada sobre SOPs, usa [`create-first-workflow-sop.md`](create-first-workflow-sop.md).

**Criterio de salida:** al menos un workflow con trigger, pasos, output y owner.

---

## Paso 5 — Añadir scorecard del departamento

Añade una sección `## Scorecard` con 3-5 métricas observables:

```markdown
## Scorecard

| Métrica | Baseline | Target | Actual | Fuente | Fecha observación |
|---------|----------|--------|--------|--------|-------------------|
| (qué mides) | (valor actual) | (valor objetivo) | (valor real) | (de dónde viene el dato) | (fecha ISO) |
```

Para elegir métricas, usa [`select-scorecard-metrics.md`](select-scorecard-metrics.md).

Reglas:

- Solo incluye métricas que puedas medir hoy con datos que ya tienes.
- Si no tienes baseline, ponlo como "sin medición" y mide en el primer loop.
- No inventes targets sin datos. Es mejor "baseline: sin medición, target: medir en primer sprint".

**Criterio de salida:** al menos 3 métricas con fuente y fecha, aunque el baseline sea "sin medición".

---

## Paso 6 — Definir escalación

Añade o completa la sección de escalación:

```markdown
## Escalación

| Situación | Escala a | Canal | Tiempo máximo |
|-----------|----------|-------|---------------|
| Bloqueo en entrega | (owner del departamento) | (canal: email, Slack, reunión) | (ej: 24h) |
| Error que afecta a cliente | (dirección / owner) | (canal) | (ej: 4h) |
| Agente actúa fuera de permisos | (owner del departamento + dirección) | (canal) | (inmediato) |
| Duda sobre aprobación | (ver approval-boundaries.md) | (canal) | (antes de actuar) |
```

**Criterio de salida:** al menos 3 situaciones de escalación con destinatario y canal.

---

## Paso 7 — Conectar con roles y aprobaciones

Verifica que:

- El owner del departamento aparece en `company/roles-and-responsibilities.md`.
- Los procesos del departamento están en la matriz RACI.
- Las acciones de riesgo del departamento están en `company/approval-boundaries.md`.

Si faltan conexiones, actualiza esos archivos.

**Criterio de salida:** el department brain enlaza a roles-and-responsibilities y approval-boundaries.

---

## Paso 8 — Cambiar frescura a "reviewed"

Cambia la línea `Freshness: draft until reviewed` a:

```
Freshness: reviewed YYYY-MM-DD by [nombre del owner]
```

No marques como "reviewed" si quedan placeholders tipo `{{ }}`, "TBD", "COMPLETAR" o "replace this".

**Criterio de salida:** frescura actualizada, sin placeholders restantes.

---

## Checklist final

Antes de continuar al primer loop, confirma:

- [ ] Owner humano asignado
- [ ] Síntomas de Punto A reales (no placeholders)
- [ ] Herramientas y fuentes documentadas
- [ ] Al menos 1 workflow con trigger, pasos, output y owner
- [ ] Scorecard con 3+ métricas y fuente
- [ ] Escalación definida (3+ situaciones)
- [ ] Conectado a roles-and-responsibilities y approval-boundaries
- [ ] Frescura actualizada a "reviewed"

---

## Siguiente paso

1. Crea el primer empleado digital para este departamento: [`create-first-digital-employee.md`](create-first-digital-employee.md).
2. Ejecuta el primer loop interno: [`run-first-internal-loop.md`](run-first-internal-loop.md).

---

## Errores comunes

| Error | Por qué falla | Solución |
|---|---|---|
| Dejar placeholders y marcar "reviewed" | El validador detecta placeholders y falla | Reemplaza todos los `{{ }}` y marcadores antes de cambiar frescura |
| No poner owner humano | Sin owner, nadie revisa ni escala | Asigna antes de continuar |
| Scorecard con targets inventados | Genera expectativas falsas y confusión | Usa "sin medición" como baseline y mide en el primer loop |
| Workflows sin trigger ni output | No es reproducible ni verificable | Cada workflow necesita qué lo activa y qué produce |
| Copiar el departamento sin adaptarlo | El department brain queda genérico e inútil | Personaliza síntomas, herramientas y workflows con datos reales |

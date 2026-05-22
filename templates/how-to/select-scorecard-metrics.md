# Cómo elegir métricas para el scorecard

Guía práctica para seleccionar métricas observables y actualizarlas con evidencia real, no con estimaciones.

## Para quién es esto

Un operador que necesita definir métricas para:

- `company/company-scorecard.md` (nivel empresa);
- `departments/[departamento]/department-brain.md` (nivel departamento);
- `digital-employees/[agente]/SCORECARD.md` o sección scorecard del SOUL (nivel agente).

## Qué produce

Un scorecard con 3-5 métricas por nivel que:

1. Se pueden medir con datos que ya existen hoy.
2. Tienen fuente, fecha y owner.
3. Se actualizan con evidencia real después de cada sprint o loop.

---

## Regla principal

**Solo mide lo que puedes observar hoy.** Si no tienes el dato, la métrica es "baseline: sin medición" hasta que lo consigas. No inventes números.

---

## Paso 1 — Elegir tipo de métrica

Hay 3 tipos útiles para el primer scorecard:

| Tipo | Qué mide | Ejemplo | Cuándo usarla |
|------|----------|---------|---------------|
| Actividad | ¿Se hizo la tarea? | Loops completados por semana | Siempre — es la más fácil de medir |
| Calidad | ¿Se hizo bien? | Tasa de aceptación en revisión humana | Cuando ya tienes al menos un loop cerrado |
| Resultado | ¿Cambió algo en el negocio? | Tiempo medio de entrega, errores por mes | Cuando tienes baseline y al menos 4 semanas de datos |

Para el primer scorecard, prioriza 2-3 métricas de actividad + 1 de calidad. Las métricas de resultado vienen después.

**Criterio de salida:** has elegido 3-5 métricas con tipo definido.

---

## Paso 2 — Verificar que la fuente existe

Para cada métrica, responde:

| Pregunta | Si la respuesta es "no" |
|----------|------------------------|
| ¿Dónde está el dato hoy? | La métrica no es medible todavía. Ponla como "pendiente de fuente". |
| ¿Quién puede consultar ese dato? | Necesitas acceso. Documéntalo en `source-of-truth-map.md`. |
| ¿Cada cuánto se actualiza el dato? | Si es manual, define quién y cuándo lo actualiza. |
| ¿El dato es verificable por otra persona? | Si solo tú lo "sabes" pero no hay registro, no es evidencia. |

Ejemplos de fuentes válidas:

- Receipts en la instancia (`receipts/rcp-*.md`).
- Herramienta de gestión (Notion, Trello, Asana, Google Sheets).
- Registro de entregas, facturas o pedidos.
- Feedback documentado de clientes (anonimizado si está en repo público).

Ejemplos de fuentes no válidas:

- "Lo sé de memoria."
- "Aproximadamente X."
- "Me parece que el mes pasado..."

**Criterio de salida:** cada métrica tiene fuente identificada o está marcada como "pendiente de fuente".

---

## Paso 3 — Definir baseline

El baseline es el valor actual antes de cualquier mejora. No es un target ni una estimación.

| Situación | Qué poner como baseline |
|-----------|------------------------|
| Tienes el dato exacto | El valor real con fecha y fuente |
| Tienes dato aproximado con registro | El valor registrado con nota "aproximado, fuente: [X]" |
| No tienes dato | "sin medición" — medir en el primer sprint |

No inventes baselines. Un scorecard con "baseline: 85%" sin fuente es peor que "baseline: sin medición".

**Criterio de salida:** cada métrica tiene baseline real o "sin medición".

---

## Paso 4 — Definir target (solo si tienes baseline)

Si tienes baseline, define un target alcanzable para los próximos 90 días:

| Tipo de mejora | Cómo definir el target |
|----------------|----------------------|
| Reducir algo | "Reducir X un Y% respecto al baseline" |
| Aumentar algo | "Aumentar X de N a M" |
| Crear algo que no existe | "Completar Y unidades o instancias" |
| Mantener algo | "Mantener X dentro del rango A-B" |

Si no tienes baseline, el target es: "Medir el baseline en el primer sprint."

**Criterio de salida:** métricas con baseline tienen target; métricas sin baseline tienen "medir primero".

---

## Paso 5 — Rellenar la tabla

```markdown
## Scorecard — [nivel: empresa / departamento / agente]

| # | Métrica | Tipo | Baseline | Target | Actual | Fuente | Owner | Última actualización |
|---|---------|------|----------|--------|--------|--------|-------|---------------------|
| 1 | (nombre) | actividad/calidad/resultado | (valor o "sin medición") | (valor o "medir primero") | — | (fuente del dato) | (quién actualiza) | — |
| 2 | (nombre) | (tipo) | (valor) | (valor) | — | (fuente) | (owner) | — |
| 3 | (nombre) | (tipo) | (valor) | (valor) | — | (fuente) | (owner) | — |
```

**Criterio de salida:** tabla con 3-5 métricas, todas con fuente y owner.

---

## Paso 6 — Cadencia de actualización

Define cuándo y cómo se actualiza cada métrica:

| Cadencia | Cuándo usarla | Ejemplo |
|----------|---------------|---------|
| Cada sprint (1-2 semanas) | Métricas de actividad | Loops completados, tareas cerradas |
| Mensual | Métricas de calidad | Tasa de aceptación, errores por entrega |
| Trimestral | Métricas de resultado | Tiempo medio de entrega, ingresos |

Regla: actualiza el scorecard como parte del cierre de cada sprint, no como tarea separada. El Receipt del sprint incluye los datos necesarios.

**Criterio de salida:** cada métrica tiene cadencia definida.

---

## Ejemplos sintéticos

### Scorecard de empresa (agencia)

| # | Métrica | Tipo | Baseline | Target | Fuente | Owner |
|---|---------|------|----------|--------|--------|-------|
| 1 | Departamentos con brain completado | actividad | 0 | 1 en 30 días | instancia privada | Fundador |
| 2 | Loops internos cerrados con receipt | actividad | 0 | 4 en 90 días | receipts/ | Fundador |
| 3 | Tasa de aceptación primer loop | calidad | sin medición | medir primero | receipts/ | Owner dept |

### Scorecard de departamento (operations-delivery)

| # | Métrica | Tipo | Baseline | Target | Fuente | Owner |
|---|---------|------|----------|--------|--------|-------|
| 1 | Entregas con checklist completada | actividad | 0 de 10 | 8 de 10 en 90 días | Google Sheets "entregas" | Ana |
| 2 | Errores detectados post-entrega | calidad | 3 por mes (fuente: retrospectiva mayo) | <1 por mes | registro de incidencias | Ana |
| 3 | Tiempo medio de entrega | resultado | sin medición | medir primero | herramienta de gestión | Ana |

### Scorecard de agente (operations-delivery-assistant)

| # | Métrica | Tipo | Baseline | Target | Fuente | Owner |
|---|---------|------|----------|--------|--------|-------|
| 1 | Tareas completadas por sprint | actividad | 0 | definir tras primer loop | receipts/ | Ana |
| 2 | Tasa de aceptación en revisión | calidad | sin medición | >80% tras 4 sprints | receipts/ | Ana |
| 3 | Incidentes fuera de permisos | actividad | 0 | 0 | auditoría | Ana |

---

## Cómo actualizar el scorecard con evidencia

Después de cada sprint o loop:

1. Abre el Receipt del sprint (`receipts/rcp-*.md`).
2. Extrae los datos relevantes para cada métrica.
3. Actualiza la columna "Actual" con el valor observado.
4. Actualiza la columna "Última actualización" con la fecha.
5. Si el valor cambió significativamente, documenta por qué en una nota.

No actualices el scorecard con intenciones ("vamos a mejorar") sino con observaciones ("este sprint entregamos 8 de 10 con checklist").

---

## Reglas

- No incluyas más de 5 métricas por nivel. Si necesitas más, pregúntate si son realmente medibles.
- No marques un target como alcanzado sin receipt o fuente que lo demuestre.
- Si una métrica lleva 2+ sprints sin actualizarse, revísala: o no es medible o no es prioritaria.
- No uses datos de clientes reales en repos públicos. Anonimiza o usa datos sintéticos.
- Si cambias una métrica (la eliminas o la reemplazas), crea un StateChange con el motivo.

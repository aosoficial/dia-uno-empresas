# Company Scorecard

Plantilla para medir el progreso del negocio con evidencia observada, no con estimaciones.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- `company/company-brain.md` con propósito, oferta y owner rellenados;
- al menos un departamento definido.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md).

## Qué produce

Un archivo `company/company-scorecard.md` en tu instancia privada con:

1. Métricas de empresa con fuente, fecha y owner.
2. Líneas por departamento con receipt enlazado.
3. Cadencia de actualización ligada a sprints.

Para elegir las métricas correctas, consulta [`templates/how-to/select-scorecard-metrics.md`](../how-to/select-scorecard-metrics.md).

---

## Cómo rellenar esta plantilla

1. Copia esta plantilla a tu instancia privada: `company/company-scorecard.md`.
2. Rellena las métricas de empresa que puedas medir hoy. Las que no, déjalas como "sin medición".
3. Añade una línea por cada departamento activo.
4. Después de cada sprint, actualiza las columnas "Actual", "Fuente" y "Fecha".
5. No marques ningún target como alcanzado sin receipt que lo demuestre.

---

## Punto A

<!-- Describe brevemente el estado actual del negocio antes de operar. -->

> (rellena con tu diagnóstico de Punto A — ver company/company-brain.md)

## Punto B objetivo

> Una empresa AI-First de servicios productizados operando con dirección, departamentos, empleados digitales, permisos, receipts y loop de mejora.

---

## Métricas de empresa

| # | Métrica | Tipo | Baseline | Target | Actual | Fuente | Owner | Fecha actualización |
|---|---------|------|----------|--------|--------|--------|-------|---------------------|
| 1 | Departamentos con brain operativo | actividad | 0 | 1 en 30 días | (valor observado) | instancia privada | (owner) | (fecha ISO) |
| 2 | Loops internos cerrados con receipt | actividad | 0 | 4 en 90 días | (valor observado) | `receipts/` | (owner) | (fecha ISO) |
| 3 | Tasa de aceptación en revisión humana | calidad | sin medición | medir primero | (valor observado) | `receipts/` | (owner) | (fecha ISO) |
| 4 | Calidad de entrega / errores evitables | calidad | sin medición | medir primero | (valor observado) | (herramienta o registro) | (owner) | (fecha ISO) |
| 5 | Ingresos / retención | resultado | (rellena privadamente) | (rellena privadamente) | (valor observado) | (sistema financiero) | (owner) | (fecha ISO) |

Regla: "sin medición" es mejor que un número inventado. Mide el baseline en el primer sprint y fija targets después.

---

## Líneas por departamento

| Departamento | Owner asignado | Brain activo | Workflow documentado | Métrica semanal | Último receipt | Bloqueadores |
|-------------|----------------|-------------|---------------------|----------------|---------------|-------------|
| (departamento) | (sí/no) | (sí/no) | (sí/no) | (nombre de la métrica) | (enlace a `receipts/rcp-*.md`) | (descripción o "ninguno") |

---

## Preguntas de revisión semanal

1. ¿Qué decisión cambió el negocio esta semana?
2. ¿Qué tarea repetida se convirtió en SOP o skill?
3. ¿Qué acción de un agente necesitó corrección humana?
4. ¿Qué límite de aprobación se alcanzó?
5. ¿Qué métrica mejoró gracias al sistema?

---

## Cadencia de actualización

| Cadencia | Qué actualizar | Quién |
|----------|---------------|-------|
| Cada sprint (1-2 semanas) | Columnas "Actual" y "Fecha" con datos de receipts | Owner del departamento |
| Mensual | Revisar targets y baselines; añadir nuevas métricas si aplica | Owner de dirección |
| Trimestral | Cerrar métricas obsoletas, abrir nuevas, enlazar con rocks | Equipo de dirección |

---

## Conexiones

- Métricas por departamento: `departments/*/department-brain.md` → sección scorecard
- Métricas por agente: `digital-employees/*/SCORECARD.md` o sección en SOUL.md
- Cómo elegir métricas: [`templates/how-to/select-scorecard-metrics.md`](../how-to/select-scorecard-metrics.md)
- Receipts como fuente: `receipts/rcp-*.md`
- Rocks trimestrales: [`company/annual-plan.md`](annual-plan.md)
- OKRs: [`company/okrs.md`](okrs.md)

---

## Reglas

- No actualices el scorecard con intenciones ("vamos a mejorar") sino con observaciones ("este sprint entregamos 8 de 10 con checklist").
- No marques un target como alcanzado sin receipt que lo demuestre.
- Cada valor en la columna "Actual" necesita fecha y fuente.
- No uses datos de clientes reales en repositorios públicos.
- Si una métrica lleva 2+ sprints sin actualizarse, revísala: o no es medible o no es prioritaria. Documenta el cambio en un StateChange.

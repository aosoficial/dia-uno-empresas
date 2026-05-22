# OKRs y Rocks trimestrales

Plantilla para traducir la dirección anual en resultados medibles por trimestre.

## Para quién es esto

Un operador que ya tiene:

- `company/company-brain.md` con propósito, oferta y owner rellenados;
- al menos un departamento definido;
- visión anual o meta principal del negocio.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md).

## Qué produce

Un archivo `company/okrs.md` en tu instancia privada con:

1. Meta anual del negocio (1 frase).
2. 3-5 rocks trimestrales con owner y evidencia.
3. OKRs vinculados a los rocks.
4. Conexión explícita rock → sprint → receipt → scorecard.

---

## Cómo rellenar esta plantilla

1. Copia esta plantilla a tu instancia privada: `company/okrs.md`.
2. Rellena la meta anual desde tu `company-brain.md`.
3. Elige 3-5 rocks para los próximos 90 días.
4. Para cada rock, escribe 1-3 Key Results medibles.
5. Asigna owner humano a cada rock.
6. Después de cada sprint, actualiza evidencia y estado.

---

## Meta anual

<!-- Una frase que describe el objetivo principal del negocio este año. -->
<!-- Fuente: company/company-brain.md — sección Purpose o visión. -->

> Meta: (rellena con tu meta principal anual)
>
> Fuente: (de dónde sale esta meta)
> Revisado: (fecha última revisión, ISO 8601)

---

## Rocks trimestrales (90 días)

Rocks = las 3-5 prioridades que, si se completan, mueven el negocio hacia la meta anual.

| # | Rock | Owner | Departamento | Fecha límite | Estado | Evidencia |
|---|------|-------|-------------|-------------|--------|-----------|
| R1 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |
| R2 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |
| R3 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |

Estados válidos: pendiente, en_progreso, completado, bloqueado.

Evidencia: enlaza al receipt (`receipts/rcp-*.md`) o scorecard que demuestra el progreso. No marques "completado" sin evidencia observada.

---

## OKRs por rock

### Rock R1 — (nombre del rock)

**Objective:** (qué quieres lograr con este rock)

| KR | Key Result | Métrica | Baseline | Target | Actual | Evidencia |
|----|-----------|---------|----------|--------|--------|-----------|
| KR1.1 | (resultado medible) | (unidad) | (valor actual) | (valor objetivo) | (valor real observado) | (receipt o fuente) |
| KR1.2 | (resultado medible) | (unidad) | (valor actual) | (valor objetivo) | (valor real observado) | (receipt o fuente) |

### Rock R2 — (nombre del rock)

**Objective:** (qué quieres lograr con este rock)

| KR | Key Result | Métrica | Baseline | Target | Actual | Evidencia |
|----|-----------|---------|----------|--------|--------|-----------|
| KR2.1 | (resultado medible) | (unidad) | (valor actual) | (valor objetivo) | (valor real observado) | (receipt o fuente) |
| KR2.2 | (resultado medible) | (unidad) | (valor actual) | (valor objetivo) | (valor real observado) | (receipt o fuente) |

### Rock R3 — (nombre del rock)

**Objective:** (qué quieres lograr con este rock)

| KR | Key Result | Métrica | Baseline | Target | Actual | Evidencia |
|----|-----------|---------|----------|--------|--------|-----------|
| KR3.1 | (resultado medible) | (unidad) | (valor actual) | (valor objetivo) | (valor real observado) | (receipt o fuente) |
| KR3.2 | (resultado medible) | (unidad) | (valor actual) | (valor objetivo) | (valor real observado) | (receipt o fuente) |

Copia más secciones si tienes más de 3 rocks (máximo recomendado: 5).

---

## Conexión rock → sprint → evidencia

Cada rock se ejecuta a través de sprints. El ciclo es:

```
Rock → Sprint (1-2 semanas) → Context Packet → Acción → Receipt → Scorecard/KR actualizado
```

Ejemplo:

| Rock | Sprint | Context Packet | Receipt | KR actualizado |
|------|--------|---------------|---------|----------------|
| R1 | Sprint 1 (semana 1-2) | cp-ops-checklist-2026-05-22 | rcp-lara-2026-05-22-001 | KR1.1: baseline 0 → actual 1 |

Después de cada sprint, revisa:

1. ¿El KR avanzó? Actualiza la columna "Actual" con evidencia.
2. ¿El rock sigue siendo la prioridad correcta? Si no, documenta el cambio en un StateChange.
3. ¿El siguiente sprint está definido? Actualiza `company/guided-pilot-plan.md`.

---

## Cadencia de revisión

| Cadencia | Qué revisar | Quién |
|----------|------------|-------|
| Semanal | Progreso de KRs del sprint actual | Owner del rock |
| Mensual | Estado de todos los rocks y OKRs | Owner de dirección |
| Trimestral | Cierre de rocks, nuevos rocks para siguiente trimestre | Equipo de dirección |

---

## Ejemplos sintéticos por tipo de empresa

### Agencia

> Meta anual: "Entregar 100% de proyectos con checklist estándar y sin retrabajos evitables."
>
> Rock R1: Crear y validar checklist de entrega para los 3 tipos de proyecto más frecuentes.
> Owner: Director de operaciones. Departamento: operations-delivery. Fecha: 90 días.
> KR1.1: 3 checklists creadas y validadas con receipt (baseline: 0, target: 3).
> KR1.2: Reducir retrabajos en proyectos piloto un 30% (baseline: medición actual, target: -30%).

### Consultoría

> Meta anual: "Productizar la oferta principal para reducir dependencia del fundador."
>
> Rock R1: Documentar el proceso de diagnóstico estándar como SOP.
> Owner: Fundador. Departamento: operations-delivery. Fecha: 90 días.
> KR1.1: SOP documentado con trigger, pasos, output y receipt (baseline: 0, target: 1).
> KR1.2: Un consultor junior completa un diagnóstico usando solo el SOP (baseline: 0, target: 1).

### Freelancer

> Meta anual: "Pasar de freelancer a micro-empresa con 1 proceso delegable."
>
> Rock R1: Crear proceso estándar de onboarding de cliente.
> Owner: Yo (fundador). Departamento: operations-delivery. Fecha: 90 días.
> KR1.1: Proceso documentado con checklist y plantilla de bienvenida (baseline: 0, target: 1).
> KR1.2: Próximo cliente onboarded siguiendo el proceso (baseline: 0, target: 1).

---

## Reglas

- No marques un rock como "completado" sin receipt que lo demuestre.
- No uses datos de clientes reales en esta plantilla si está en un repositorio público.
- Si un rock se bloquea, cámbialo a "bloqueado" y documenta el motivo en un StateChange.
- Si la meta anual cambia, actualiza este archivo y crea un StateChange.

# OKRs por Rock

Company: `{{ company_name }}`
Owner: `{{ owner }}`
Status: `draft until reviewed`

## Meta anual

> Meta: (rellena con tu meta principal anual — misma que en `company/annual-plan.md`)
>
> Revisado: (fecha última revisión, ISO 8601)

## OKRs por rock

### Rock R1 — (nombre del rock desde annual-plan.md)

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

### Rock R3 — (nombre del rock)

**Objective:** (qué quieres lograr con este rock)

| KR | Key Result | Métrica | Baseline | Target | Actual | Evidencia |
|----|-----------|---------|----------|--------|--------|-----------|
| KR3.1 | (resultado medible) | (unidad) | (valor actual) | (valor objetivo) | (valor real observado) | (receipt o fuente) |

## Conexión rock → sprint → evidencia

| Rock | Sprint | Context Packet | Receipt | KR actualizado |
|------|--------|---------------|---------|----------------|
| (rock) | (sprint) | (context packet) | (receipt) | (KR: baseline → actual) |

Después de cada sprint, revisa:

1. ¿El KR avanzó? Actualiza la columna "Actual" con evidencia.
2. ¿El rock sigue siendo la prioridad correcta? Si no, documenta el cambio en un StateChange.
3. ¿El siguiente sprint está definido? Actualiza `company/guided-pilot-plan.md`.

## Cadencia de revisión

| Cadencia | Qué revisar | Quién |
|----------|------------|-------|
| Semanal | Progreso de KRs del sprint actual | Owner del rock |
| Mensual | Estado de todos los rocks y OKRs | Owner de dirección |
| Trimestral | Cierre de rocks, nuevos rocks para siguiente trimestre | Equipo de dirección |

## Cómo completar este archivo

1. Rellena la meta anual desde tu `company/annual-plan.md`.
2. Para cada rock, escribe 1-3 Key Results medibles.
3. Asigna owner humano a cada rock.
4. Después de cada sprint, actualiza evidencia y estado.

Plantilla de referencia: [`templates/company/okrs.md`](../../company/okrs.md)

## Reglas

- No marques un rock como "completado" sin receipt que lo demuestre.
- Si un rock se bloquea, cámbialo a "bloqueado" y documenta el motivo en un StateChange.
- Si la meta anual cambia, actualiza este archivo y crea un StateChange.

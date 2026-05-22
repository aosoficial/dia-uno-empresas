# Plan anual y Rocks trimestrales

Company: `{{ company_name }}`
Owner: `{{ owner }}`
Status: `draft until reviewed`

## Meta anual

> Meta: (rellena con tu meta principal anual)
>
> Fuente: (de dónde sale esta meta — reunión, diagnóstico, revisión)
> Owner: `{{ owner }}`
> Revisado: (fecha última revisión, ISO 8601)

## Rocks trimestrales (Q actual)

| # | Rock | Owner | Departamento | Fecha límite | Estado | Evidencia |
|---|------|-------|-------------|-------------|--------|-----------|
| R1 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |
| R2 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |
| R3 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |

Estados válidos: pendiente, en_progreso, completado, bloqueado.

Evidencia: enlaza al receipt (`receipts/rcp-*.md`) o scorecard. No marques "completado" sin evidencia observada.

## Historial de trimestres anteriores

| Trimestre | Rocks completados | Rocks bloqueados | Aprendizajes clave | StateChange |
|-----------|-------------------|-----------------|---------------------|-------------|
| (Q anterior) | (lista breve) | (lista breve) | (qué aprendimos) | (enlace a statechange) |

## Cadencia de revisión

| Cadencia | Qué revisar | Quién |
|----------|------------|-------|
| Semanal | Progreso del sprint actual contra el rock activo | Owner del rock |
| Mensual | Estado de todos los rocks; riesgos y bloqueos | Owner de dirección |
| Trimestral | Cierre de rocks, nuevos rocks, revisión de meta anual | Equipo de dirección |

## Conexión con OKRs

Cada rock se descompone en Key Results medibles en `company/okrs.md`. El ciclo es:

```
Meta anual → Rocks trimestrales → OKRs por rock → Sprint → Receipt → Scorecard
```

## Cómo completar este archivo

1. Escribe la meta anual. Debe ser una frase que cualquier persona del equipo entienda.
2. Elige 3-5 rocks para los próximos 90 días.
3. Asigna un owner humano a cada rock. No asignes rocks a agentes.
4. Enlaza cada rock al departamento responsable.
5. Después de cada trimestre, revisa, cierra rocks completados y abre nuevos.

Plantilla de referencia: [`templates/company/annual-plan.md`](../../company/annual-plan.md)

## Reglas

- No marques un rock como "completado" sin receipt que lo demuestre.
- Si un rock se bloquea, cámbialo a "bloqueado" y documenta el motivo en un StateChange.
- Si la meta anual cambia, actualiza este archivo y crea un StateChange.
- Un owner humano es obligatorio. Los agentes ejecutan tareas dentro de sprints, no son owners de rocks.

# Plan anual y Rocks trimestrales

Plantilla para definir la meta principal del año y las 3-5 prioridades de 90 días que la mueven.

## Para quién es esto

Un operador que ya tiene:

- `company/company-brain.md` con propósito, oferta y owner rellenados;
- al menos un departamento definido.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md).

## Qué produce

Un archivo `company/annual-plan.md` en tu instancia privada con:

1. Meta anual del negocio (1 frase concreta).
2. 3-5 rocks trimestrales con owner, departamento y evidencia.
3. Cadencia de revisión.
4. Conexión explícita con `company/okrs.md` para Key Results medibles.

---

## Cómo rellenar esta plantilla

1. Copia esta plantilla a tu instancia privada: `company/annual-plan.md`.
2. Escribe la meta anual. Debe ser una frase que cualquier persona del equipo entienda.
3. Elige 3-5 rocks para los próximos 90 días. Un rock es una prioridad que, si se completa, mueve el negocio hacia la meta anual.
4. Asigna un owner humano a cada rock. No asignes rocks a agentes.
5. Enlaza cada rock al departamento responsable.
6. Después de cada trimestre, revisa, cierra rocks completados y abre nuevos.

---

## Meta anual

<!-- Una frase que describe el objetivo principal del negocio este año. -->
<!-- Fuente: company/company-brain.md — sección Purpose o visión. -->

> Meta: (rellena con tu meta principal anual)
>
> Fuente: (de dónde sale esta meta — reunión, diagnóstico, revisión)
> Owner: (persona responsable de que se cumpla)
> Revisado: (fecha última revisión, ISO 8601)

---

## Rocks trimestrales (Q actual)

| # | Rock | Owner | Departamento | Fecha límite | Estado | Evidencia |
|---|------|-------|-------------|-------------|--------|-----------|
| R1 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |
| R2 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |
| R3 | (describe la prioridad) | (persona responsable) | (departamento) | (fecha ISO) | pendiente | (enlace a receipt o scorecard) |

Estados válidos: pendiente, en_progreso, completado, bloqueado.

Evidencia: enlaza al receipt (`receipts/rcp-*.md`) o scorecard que demuestra progreso. No marques "completado" sin evidencia observada.

---

## Historial de trimestres anteriores

| Trimestre | Rocks completados | Rocks bloqueados | Aprendizajes clave | StateChange |
|-----------|-------------------|-----------------|---------------------|-------------|
| (Q anterior) | (lista breve) | (lista breve) | (qué aprendimos) | (enlace a statechange si hubo cambio de dirección) |

---

## Cadencia de revisión

| Cadencia | Qué revisar | Quién |
|----------|------------|-------|
| Semanal | Progreso del sprint actual contra el rock activo | Owner del rock |
| Mensual | Estado de todos los rocks; riesgos y bloqueos | Owner de dirección |
| Trimestral | Cierre de rocks, nuevos rocks, revisión de meta anual | Equipo de dirección |

---

## Conexión con OKRs

Cada rock se descompone en Key Results medibles en `company/okrs.md`. El ciclo es:

```
Meta anual → Rocks trimestrales → OKRs por rock → Sprint → Receipt → Scorecard
```

Si no tienes `company/okrs.md`, créalo con la plantilla [`templates/company/okrs.md`](okrs.md).

---

## Ejemplos sintéticos por tipo de empresa

### Agencia

> Meta anual: "Entregar 100% de proyectos con checklist estándar y sin retrabajos evitables."
>
> Rock R1: Crear y validar checklist de entrega para los 3 tipos de proyecto más frecuentes.
> Owner: Director de operaciones. Departamento: operations-delivery. Fecha: 90 días.

### Consultoría

> Meta anual: "Productizar la oferta principal para reducir dependencia del fundador."
>
> Rock R1: Documentar el proceso de diagnóstico estándar como SOP replicable.
> Owner: Fundador. Departamento: operations-delivery. Fecha: 90 días.

### Freelancer

> Meta anual: "Pasar de freelancer a micro-empresa con 1 proceso delegable."
>
> Rock R1: Crear proceso estándar de onboarding de cliente con checklist y plantilla.
> Owner: Yo (fundador). Departamento: operations-delivery. Fecha: 90 días.

---

## Reglas

- No marques un rock como "completado" sin receipt que lo demuestre.
- No uses datos de clientes reales en esta plantilla si está en un repositorio público.
- Si un rock se bloquea, cámbialo a "bloqueado" y documenta el motivo en un StateChange.
- Si la meta anual cambia, actualiza este archivo y crea un StateChange.
- Un owner humano es obligatorio. Los agentes ejecutan tareas dentro de sprints, no son owners de rocks.

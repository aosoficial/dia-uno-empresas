# Roles y responsabilidades

Company: `{{ company_name }}`
Owner: `{{ owner }}`
Status: `draft until reviewed`

## Roles definidos

| Rol | Tipo (humano/digital) | Owner actual | Departamento | Responsabilidades principales | Aprueba qué | Fuente | Última revisión |
|-----|----------------------|-------------|-------------|-------------------------------|------------|--------|----------------|
| Dirección / Owner | humano | `{{ owner }}` | direction | Definir visión, prioridades, aprobar compromisos externos | Económico, legal, publicación, externo | (decisión, contrato) | (fecha ISO) |
| (rol operativo) | humano | (nombre) | (departamento) | (lista breve de responsabilidades) | (qué aprueba este rol) | (fuente) | (fecha ISO) |
| `{{ first_employee }}` | digital | (nombre del agente) | direction | Redactar, analizar, preparar — sin acciones externas | nada — escala a humano | PERMISSIONS.md | (fecha ISO) |

## Matriz RACI simplificada

RACI: **R**esponsable (ejecuta), **A**prueba (decide), **C**onsultado (opina), **I**nformado (se entera).

| Proceso / actividad | Dirección | Operaciones | Agente digital | Notas |
|---------------------|-----------|-------------|---------------|-------|
| (proceso 1) | A | R | C (prepara checklist) | (notas) |
| (proceso 2) | A | R | C (redacta borrador) | (notas) |
| (proceso 3) | I | R | R (genera context packet) | (notas) |

Instrucciones:

- Lista los 3-5 procesos más frecuentes o críticos de tu negocio.
- Asigna exactamente un A (aprobador) por proceso.
- Un agente digital puede ser R solo para tareas internas (redactar, analizar). Nunca A.

## Handoffs humano-agente

| Proceso | Paso humano → agente | Paso agente → humano | Regla de escalación |
|---------|---------------------|---------------------|---------------------|
| (proceso) | (qué entrega el humano al agente) | (qué devuelve el agente) | (cuándo el agente debe parar y pedir aprobación) |

Regla base: el agente devuelve output al humano para revisión. El humano decide si se envía, publica, compromete o cambia producción.

## Conexiones

- Organigrama: [`company/org-chart.md`](org-chart.md)
- Matriz de aprobaciones: [`company/approval-boundaries.md`](approval-boundaries.md)
- Permisos por agente: `digital-employees/*/PERMISSIONS.md`

## Cómo completar este archivo

1. Lista los roles que existen en tu negocio (no las personas — un mismo humano puede tener varios roles).
2. Para cada rol, define las responsabilidades concretas.
3. Rellena la matriz RACI para los 3-5 procesos más importantes.
4. Documenta los handoffs humano-agente.
5. Enlaza a `company/approval-boundaries.md` para las reglas de aprobación.

Plantilla de referencia: [`templates/company/roles-and-responsibilities.md`](../../company/roles-and-responsibilities.md)

## Reglas

- Cada rol debe tener un owner humano actual. Si no lo tiene, es una vacante.
- Los agentes digitales no aprueban nada. Son R (ejecutan tareas internas) o C (consultan/preparan).
- Si un proceso no tiene un A claro, el owner de dirección es A por defecto.
- No uses nombres reales de personas en repositorios públicos.

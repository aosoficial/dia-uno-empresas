# Organigrama operativo

Company: `{{ company_name }}`
Owner: `{{ owner }}`
Status: `draft until reviewed`

## Personas actuales

| Nombre | Rol principal | Departamento | Otros sombreros | Horas/semana | Fuente | Última revisión |
|--------|--------------|-------------|-----------------|-------------|--------|----------------|
| `{{ owner }}` | Dirección / Owner | direction | (otros roles que cubre) | (dedicación) | (decisión o contrato) | (fecha ISO) |
| (nombre) | (rol) | (departamento) | (otros roles) | (dedicación) | (fuente) | (fecha ISO) |

## Asientos digitales propuestos o activos

| Nombre | Departamento | Tipo | Permisos | Scorecard | Estado |
|--------|-------------|------|----------|-----------|--------|
| (ninguno por defecto) | (capacidad madura) | (tipo) | (enlace a permisos) | (enlace a scorecard) | propuesto |

En modo `people` esta tabla permanece sin agentes. En modo `hybrid`, generar un pack no lo convierte en activo: registra por separado la evidencia y aprobación de cualquier cambio de estado.

## Vacantes y necesidades

| Rol necesario | Tipo (humano/digital) | Departamento | Por qué | Prioridad | Estado |
|--------------|----------------------|-------------|---------|-----------|--------|
| (rol) | (humano/digital) | (departamento) | (qué problema resuelve cubrirlo) | (alta/media/baja) | abierta |

## Sombreros del fundador

| Sombrero | Departamento | Horas/semana estimadas | ¿Delegable? | Plan de delegación |
|----------|-------------|----------------------|-------------|-------------------|
| Dirección | direction | (horas) | no | — |
| (ventas) | sales | (horas) | (sí/no/parcialmente) | (a quién/cuándo) |
| (delivery) | operations-delivery | (horas) | (sí/no/parcialmente) | (a quién/cuándo) |

## Conexiones

- Roles detallados: [`company/roles-and-responsibilities.md`](roles-and-responsibilities.md)
- Matriz de aprobaciones: [`company/approval-boundaries.md`](approval-boundaries.md)
- Permisos por agente: `digital-employees/*/PERMISSIONS.md`

## Cómo completar este archivo

1. Lista las personas que ya trabajan en el negocio, empezando por el fundador/owner.
2. Para cada persona, indica qué departamento cubre y qué "sombreros" lleva.
3. Solo en modo `hybrid`, lista los asientos digitales propuestos o realmente activos con referencia a permisos y evidencia del estado.
4. Identifica vacantes: roles que nadie cubre o que dependen demasiado de una persona.
5. Enlaza cada rol a `company/roles-and-responsibilities.md` y a `company/approval-boundaries.md`.

Plantilla de referencia: [`templates/company/org-chart.md`](../../company/org-chart.md)

## Reglas

- Cada persona y agente debe tener un departamento principal asignado.
- Los empleados digitales deben tener `PERMISSIONS.md` antes de activarse.
- Si un rol cambia, crea un StateChange con el motivo.
- No uses nombres reales de personas en repositorios públicos.

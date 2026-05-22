# Organigrama operativo

Plantilla para documentar las personas, roles, vacantes y empleados digitales del negocio.

## Para quién es esto

Un operador que ya tiene:

- `company/company-brain.md` con propósito, oferta y owner rellenados;
- al menos un departamento definido.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md).

## Qué produce

Un archivo `company/org-chart.md` en tu instancia privada con:

1. Lista de personas actuales con sus roles y departamentos.
2. Lista de empleados digitales activos con sus permisos.
3. Vacantes identificadas (humanas y digitales).
4. Conexión con la matriz de aprobaciones (`company/approval-boundaries.md`).

---

## Cómo rellenar esta plantilla

1. Copia esta plantilla a tu instancia privada: `company/org-chart.md`.
2. Lista las personas que ya trabajan en el negocio, empezando por el fundador/owner.
3. Para cada persona, indica qué departamento cubre y qué "sombreros" lleva.
4. Lista los empleados digitales activos con su departamento y referencia a permisos.
5. Identifica vacantes: roles que nadie cubre o que dependen demasiado de una persona.
6. Enlaza cada rol a `company/roles-and-responsibilities.md` y a `company/approval-boundaries.md`.

---

## Personas actuales

| Nombre | Rol principal | Departamento | Otros sombreros | Horas/semana | Fuente | Última revisión |
|--------|--------------|-------------|-----------------|-------------|--------|----------------|
| (nombre) | (rol) | (departamento) | (otros roles que cubre) | (dedicación) | (contrato, acuerdo o decisión) | (fecha ISO) |
| (nombre) | (rol) | (departamento) | (otros roles) | (dedicación) | (fuente) | (fecha ISO) |

---

## Empleados digitales activos

| Nombre | Departamento | Tipo | Permisos | Scorecard | Estado |
|--------|-------------|------|----------|-----------|--------|
| (nombre del agente) | (departamento) | (copiloto/asistente/agente autónomo) | `digital-employees/(nombre)/PERMISSIONS.md` | (enlace a scorecard) | (activo/en prueba/pausado) |

---

## Vacantes y necesidades

| Rol necesario | Tipo (humano/digital) | Departamento | Por qué | Prioridad | Estado |
|--------------|----------------------|-------------|---------|-----------|--------|
| (rol) | (humano/digital) | (departamento) | (qué problema resuelve cubrirlo) | (alta/media/baja) | (abierta/en búsqueda/cubierta) |

---

## Sombreros del fundador

En empresas pequeñas, el fundador suele cubrir múltiples roles. Documenta esto explícitamente:

| Sombrero | Departamento | Horas/semana estimadas | ¿Delegable? | Plan de delegación |
|----------|-------------|----------------------|-------------|-------------------|
| (dirección) | direction | (horas) | (sí/no/parcialmente) | (a quién/cuándo) |
| (ventas) | sales | (horas) | (sí/no/parcialmente) | (a quién/cuándo) |
| (delivery) | operations-delivery | (horas) | (sí/no/parcialmente) | (a quién/cuándo) |

---

## Conexiones

- Roles detallados: [`company/roles-and-responsibilities.md`](roles-and-responsibilities.md)
- Matriz de aprobaciones: [`company/approval-boundaries.md`](approval-boundaries.md)
- Permisos por agente: `digital-employees/*/PERMISSIONS.md`

---

## Cadencia de revisión

| Cadencia | Qué revisar | Quién |
|----------|------------|-------|
| Mensual | ¿Han cambiado roles, sombreros o dedicaciones? | Owner de dirección |
| Trimestral | ¿Las vacantes siguen siendo las correctas? ¿Hay nuevos agentes? | Equipo de dirección |
| Cada cambio de equipo | Actualizar tabla y crear StateChange | Owner de dirección |

---

## Reglas

- Cada persona y agente debe tener un departamento principal asignado.
- Los empleados digitales deben tener `PERMISSIONS.md` antes de activarse.
- Si un rol cambia, crea un StateChange con el motivo.
- No uses nombres reales de personas en repositorios públicos. Usa roles genéricos o datos sintéticos.
- Si el fundador cubre más de 3 sombreros, es una señal de que necesita delegar. Documenta el plan.

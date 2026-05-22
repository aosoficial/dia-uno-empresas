# Roles y responsabilidades

Plantilla para definir quién hace qué, quién aprueba y dónde están los handoffs entre humanos y agentes.

## Para quién es esto

Un operador que ya tiene:

- `company/company-brain.md` con propósito, oferta y owner rellenados;
- `company/org-chart.md` con personas y agentes listados;
- al menos un departamento definido.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md).

## Qué produce

Un archivo `company/roles-and-responsibilities.md` en tu instancia privada con:

1. Lista de roles con owner, departamento y responsabilidades concretas.
2. Matriz RACI simplificada para procesos clave.
3. Handoffs explícitos entre humanos y agentes.
4. Conexión con la matriz de aprobaciones.

---

## Cómo rellenar esta plantilla

1. Copia esta plantilla a tu instancia privada: `company/roles-and-responsibilities.md`.
2. Lista los roles que existen en tu negocio (no las personas — un mismo humano puede tener varios roles).
3. Para cada rol, define las responsabilidades concretas.
4. Rellena la matriz RACI para los 3-5 procesos más importantes.
5. Documenta los handoffs humano-agente: dónde empieza uno y termina otro.
6. Enlaza a `company/approval-boundaries.md` para las reglas de aprobación.

---

## Roles definidos

| Rol | Tipo (humano/digital) | Owner actual | Departamento | Responsabilidades principales | Aprueba qué | Fuente | Última revisión |
|-----|----------------------|-------------|-------------|-------------------------------|------------|--------|----------------|
| Dirección / Owner | humano | (nombre/fundador) | direction | Definir visión, prioridades, aprobar compromisos externos | Económico, legal, publicación, externo | (decisión, contrato) | (fecha ISO) |
| (rol operativo) | humano | (nombre) | (departamento) | (lista breve de responsabilidades) | (qué aprueba este rol) | (fuente) | (fecha ISO) |
| (agente copiloto) | digital | (nombre del agente) | (departamento) | (redactar, analizar, preparar — sin acciones externas) | nada — escala a humano | [PERMISSIONS.md] | (fecha ISO) |

---

## Matriz RACI simplificada

RACI: **R**esponsable (ejecuta), **A**prueba (decide), **C**onsultado (opina), **I**nformado (se entera).

| Proceso / actividad | Dirección | Operaciones | Ventas | Agente digital | Notas |
|---------------------|-----------|-------------|--------|---------------|-------|
| (proceso 1: ej. entrega de proyecto) | A | R | I | C (prepara checklist) | (notas adicionales) |
| (proceso 2: ej. propuesta comercial) | A | C | R | C (redacta borrador) | (notas) |
| (proceso 3: ej. onboarding de cliente) | I | R | A | R (genera context packet) | (notas) |

Instrucciones:
- Lista los 3-5 procesos más frecuentes o críticos de tu negocio.
- Asigna exactamente un A (aprobador) por proceso.
- Un agente digital puede ser R solo para tareas internas (redactar, analizar). Nunca A.

---

## Handoffs humano-agente

| Proceso | Paso humano → agente | Paso agente → humano | Regla de escalación |
|---------|---------------------|---------------------|---------------------|
| (proceso) | (qué entrega el humano al agente: contexto, instrucción, datos seguros) | (qué devuelve el agente: borrador, análisis, checklist) | (cuándo el agente debe parar y pedir aprobación) |

Regla base: el agente devuelve output al humano para revisión. El humano decide si se envía, publica, compromete o cambia producción.

---

## Conexiones

- Organigrama: [`company/org-chart.md`](org-chart.md)
- Matriz de aprobaciones: [`company/approval-boundaries.md`](approval-boundaries.md)
- Permisos por agente: `digital-employees/*/PERMISSIONS.md`

---

## Cadencia de revisión

| Cadencia | Qué revisar | Quién |
|----------|------------|-------|
| Mensual | ¿Los roles siguen asignados correctamente? ¿Hay gaps? | Owner de dirección |
| Cada cambio de equipo | Actualizar roles, RACI y handoffs. Crear StateChange. | Owner de dirección |
| Cada nuevo agente | Añadir a la tabla de roles y definir handoffs antes de activar. | Owner del departamento |

---

## Reglas

- Cada rol debe tener un owner humano actual. Si no lo tiene, es una vacante — documéntalo en `company/org-chart.md`.
- Los agentes digitales no aprueban nada. Son R (ejecutan tareas internas) o C (consultan/preparan).
- Si un proceso no tiene un A claro, el owner de dirección es A por defecto.
- No uses nombres reales de personas en repositorios públicos.
- Si un handoff falla o un agente actúa fuera de alcance, crea un StateChange y revisa `PERMISSIONS.md`.

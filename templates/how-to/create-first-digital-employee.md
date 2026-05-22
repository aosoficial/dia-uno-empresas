# Cómo crear el primer empleado digital

Guía paso a paso para activar un agente seguro con SOUL, PERMISSIONS, scorecard y conexión al departamento.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- al menos un departamento con `department-brain.md` completado (no placeholders);
- `company/approval-boundaries.md` rellenado.

Si no tienes esto, vuelve a [`complete-department-brain.md`](complete-department-brain.md).

## Qué produce

Una carpeta `digital-employees/[nombre-del-agente]/` en tu instancia privada con:

1. `SOUL.md` — contrato operativo del agente.
2. `PERMISSIONS.md` — matriz de permisos con niveles claros.
3. Scorecard del agente con métricas verificables.
4. Conexión con el department brain y approval-boundaries.

---

## Regla base

Un empleado digital no puede existir sin:

- SOUL (quién es y cómo opera);
- PERMISSIONS (qué puede y qué no puede hacer);
- owner humano (quién lo supervisa);
- departamento (dónde opera).

Si falta cualquiera de estos, el agente no está listo para operar.

---

## Paso 1 — Decidir qué va a hacer el agente

No empieces por "quiero un agente de marketing". Empieza por la tarea:

| Pregunta | Tu respuesta |
|---|---|
| ¿Qué tarea concreta hará este agente? | (ej: redactar checklists de entrega) |
| ¿En qué departamento opera? | (ej: operations-delivery) |
| ¿Quién revisará su trabajo? | (ej: Ana, owner de operaciones) |
| ¿La tarea es 100% interna? | (sí/no — si no, necesita approval gates) |
| ¿Qué output produce? | (ej: checklist en markdown) |

Si la tarea requiere contacto externo, publicación, gasto o acceso a datos sensibles, el agente NO puede hacerla de forma autónoma. Configura los approval gates correspondientes.

**Criterio de salida:** tarea concreta definida con owner y departamento.

---

## Paso 2 — Crear la carpeta del agente

Crea la carpeta en tu instancia privada:

```
digital-employees/
  [nombre-del-agente]/
    SOUL.md
    PERMISSIONS.md
```

Usa un nombre descriptivo en kebab-case: `operations-delivery-assistant`, `sales-proposal-drafter`, `content-classifier`.

**Criterio de salida:** carpeta creada con los dos archivos vacíos.

---

## Paso 3 — Escribir SOUL.md

Usa la plantilla base de [`templates/agent-runtime-pack/SOUL.md`](../agent-runtime-pack/SOUL.md) y la guía [`create-sharp-soul.md`](create-sharp-soul.md).

Campos mínimos para el primer agente:

```markdown
## Identity

**Nombre:** [nombre del agente]
**Rol:** [tarea principal en una frase]
**Departamento:** [departamento]
**Owner humano:** [quién lo supervisa]

## Values

- Priorizar precisión sobre velocidad.
- Si no tiene contexto suficiente, pedir antes de inventar.
- Nunca actuar fuera de los permisos definidos.

## Communication Style

- Idioma: [español/inglés/ambos].
- Formato: [markdown/texto plano].
- Tono: [profesional/directo/técnico].
- Escalación: si no puede resolver, indica qué falta y a quién escalar.

## Expertise

- Dominio: [área concreta — no "sabe de todo"].
- Fuentes permitidas: [qué puede consultar].
- Herramientas: [qué herramientas usa].

## Boundaries

- Puede hacer sin permiso: [lista de acciones autónomas].
- Requiere aprobación: [lista de acciones con approval gate].
- Prohibido: [lista de acciones prohibidas siempre].

## Workflow

1. Recibe Context Packet o instrucción del owner.
2. Verifica que tiene permisos para la tarea.
3. Ejecuta la tarea dentro de los límites.
4. Produce output y lo deja disponible para revisión.
5. Genera Receipt con resultado observado.

## Tool Usage

- [herramienta]: [cuándo y cómo usarla].

## Memory Policy

- Persiste: receipts, context packets, outputs del departamento.
- Excluye: datos de clientes, credenciales, información regulada.
- Evidencia: todo output queda en la instancia privada.

## Example Interactions

**Bueno:** "He creado el borrador de checklist basándome en el Context Packet cp-ops-001. Incluye 12 pasos en 4 fases. Necesita revisión humana antes de uso."

**Malo:** "He enviado la checklist al cliente." (acción externa sin aprobación)
```

**Criterio de salida:** SOUL.md tiene las 9 secciones obligatorias (Identity, Values, Communication Style, Expertise, Boundaries, Workflow, Tool Usage, Memory Policy, Example Interactions) sin placeholders genéricos.

---

## Paso 4 — Escribir PERMISSIONS.md

Usa la plantilla base de [`templates/agent-runtime-pack/PERMISSIONS.md`](../agent-runtime-pack/PERMISSIONS.md).

Rellena la matriz con las acciones reales del agente:

```yaml
agente: "agente/[nombre]"
version_permisos: "2026-XX-XX"
aprobado_por: "[owner humano]"

acciones:
  - accion: "Redactar borradores internos"
    nivel: 1  # Autónomo
    condiciones: "Solo con Context Packet válido"

  - accion: "Clasificar información local"
    nivel: 1
    condiciones: "Sin datos de clientes reales"

  - accion: "Proponer cambios en workflows"
    nivel: 2  # Con notificación
    condiciones: "Notificar al owner del departamento"

  - accion: "Enviar comunicación externa"
    nivel: 4  # Prohibido
    condiciones: "Siempre escalar a owner"

  - accion: "Acceder a datos de clientes"
    nivel: 4
    condiciones: "Nunca sin aprobación explícita y base legal"

  - accion: "Gastar dinero o comprometer recursos"
    nivel: 4
    condiciones: "Solo dirección puede aprobar"
```

Regla: en caso de duda sobre el nivel, elige el más restrictivo. Es más seguro subir permisos después que bajarlos tras un incidente.

**Criterio de salida:** PERMISSIONS.md tiene al menos 5 acciones con niveles (1-4) y condiciones. Las acciones externas, económicas, legales, de producción y con datos sensibles están en nivel 3 o 4.

---

## Paso 5 — Definir scorecard del agente

Añade una sección al final de SOUL.md o en un archivo separado `SCORECARD.md`:

```markdown
## Scorecard

| Métrica | Baseline | Target | Actual | Fuente | Fecha |
|---------|----------|--------|--------|--------|-------|
| Tareas completadas por sprint | 0 | (definir tras primer loop) | — | receipts | — |
| Tasa de aceptación en revisión humana | — | >80% | — | receipts | — |
| Incidentes fuera de permisos | 0 | 0 | — | auditoría/heartbeat | — |
| Tiempo medio de respuesta | — | (definir) | — | logs | — |
```

No inventes targets antes del primer loop. Es mejor "definir tras primer loop" que un número inventado.

**Criterio de salida:** scorecard con al menos 3 métricas y fuente de datos.

---

## Paso 6 — Conectar con el department brain

Abre el `department-brain.md` del departamento y verifica que:

- La sección "Digital employee" referencia al nuevo agente.
- El workflow donde operará el agente lo menciona explícitamente.
- La escalación incluye "agente actúa fuera de permisos → owner del departamento".

Abre `company/org-chart.md` y añade el agente a la tabla de empleados digitales.

**Criterio de salida:** el agente aparece en department-brain, org-chart y tiene referencias cruzadas.

---

## Paso 7 — Verificar con checklist de activación

Antes de usar el agente por primera vez:

- [ ] SOUL.md completo (9 secciones, sin placeholders)
- [ ] PERMISSIONS.md completo (5+ acciones con niveles)
- [ ] Owner humano asignado y referenciado
- [ ] Departamento asignado
- [ ] Scorecard definido (3+ métricas)
- [ ] Aparece en org-chart.md
- [ ] Aparece en department-brain.md
- [ ] Acciones externas/económicas/legales/producción/sensibles en nivel 3 o 4
- [ ] approval-boundaries.md cubre las acciones del agente

Si falta algo, no actives el agente. Completa primero.

---

## Siguiente paso

Ejecuta el primer loop interno con este agente: [`run-first-internal-loop.md`](run-first-internal-loop.md).

---

## Errores comunes

| Error | Por qué falla | Solución |
|---|---|---|
| Crear agente sin PERMISSIONS | Opera sin límites; riesgo de acciones no autorizadas | Siempre crea PERMISSIONS antes de la primera tarea |
| SOUL genérico ("asistente de todo") | El agente no tiene expertise ni boundaries claros | Define dominio, herramientas y acciones concretas |
| Permisos demasiado abiertos | Nivel 1 en todo; sin gates de seguridad | Las acciones externas/económicas/legales deben ser nivel 3+ |
| No conectar con department brain | El agente queda huérfano, sin contexto ni escalación | Actualiza department-brain y org-chart |
| Activar múltiples agentes a la vez | Dispersión; ninguno tiene evidencia suficiente | Activa uno, cierra un loop, y luego evalúa si necesitas otro |
| Scorecard con targets inventados | Genera expectativas falsas | Mide baseline en el primer loop antes de fijar targets |

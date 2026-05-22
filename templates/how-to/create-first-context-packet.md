# Cómo crear el primer Context Packet

Guía paso a paso para crear el primer paquete de contexto operativo. Un Context Packet es la forma en que el sistema alimenta a un agente con la información que necesita para una tarea concreta.

## Para quién es esto

Un operador que va a asignar una tarea a un empleado digital (o a sí mismo) y necesita empaquetar el contexto de forma verificable.

Requisitos previos:

- instancia privada creada con el wizard;
- al menos un departamento con `department-brain.md`;
- mapa de fuentes (`company/source-of-truth-map.md`) con al menos una fuente real;
- tarea concreta elegida (si aún no la tienes, consulta [`run-first-internal-loop.md`](run-first-internal-loop.md) paso 1).

## Qué vas a conseguir

Un archivo `context-packets/cp-[id].md` en tu instancia privada, con campos verificados, sin placeholders, listo para que un agente ejecute una tarea sin buscar información por su cuenta.

## Regla de seguridad

Un Context Packet puede contener datos de negocio. Guárdalo solo en tu instancia privada. No lo incluyas en el repo público. No pegues secretos, credenciales, datos regulados ni información de clientes reales sin anonimizar.

---

## Paso 1 — Definir la tarea

Escribe una frase que describa:

- qué debe hacer el agente;
- sobre qué entidad o proceso;
- qué resultado concreto se espera.

Ejemplo: "Redactar checklist de entrega estándar para campañas de redes sociales."

Mal ejemplo: "Ayudar con marketing" (demasiado vago, sin resultado verificable).

**Criterio de salida:** una frase con tarea + entidad + resultado esperado.

---

## Paso 2 — Recoger datos con fuente y fecha

Para cada dato que el agente necesita, anota:

- el dato concreto;
- de dónde viene (fuente);
- cuándo se verificó por última vez (fecha).

Consulta tu `company/source-of-truth-map.md` para saber qué fuentes existen y quién es responsable de cada una.

Regla: un dato sin fecha es un dato de fiabilidad desconocida. No lo incluyas sin fecha.

Si un dato tiene más de 30 días sin verificar, márcalo como advertencia de freshness.

**Criterio de salida:** al menos 1 dato con fuente y fecha de verificación.

---

## Paso 3 — Definir restricciones y permisos

Restricciones: qué NO debe hacer el agente en esta tarea. Al menos 1 restricción explícita.

Permisos:

| Nivel | Qué incluir |
|---|---|
| `autonomo` | Acciones que puede hacer sin pedir permiso |
| `requiere_aprobacion` | Acciones que necesitan visto bueno humano |
| `prohibido` | Acciones que no puede hacer bajo ninguna circunstancia |

Si dudas, aplica la regla de aprobación: acción externa, pública, económica, legal, de producción o con datos sensibles = `requiere_aprobacion` o `prohibido`.

Consulta el archivo `company/approval-boundaries.md` y el `PERMISSIONS.md` del empleado digital para mantener coherencia.

**Criterio de salida:** al menos 1 restricción, y los 3 niveles de permisos definidos.

---

## Paso 4 — Escribir el Context Packet

Usa la plantilla de [`templates/context-packets/context-packet-template.md`](../context-packets/context-packet-template.md).

Campos mínimos obligatorios:

```yaml
id: "cp-[departamento]-[descripcion]-[fecha]"
target: "[agente o persona]"
task: "[tarea del paso 1]"
context:
  entidad_principal: "[sobre qué se trabaja]"
  datos_relevantes:
    - "[dato con fuente y fecha]"
constraints:
  - "[restricción del paso 3]"
permissions:
  autonomo:
    - "[acción autónoma]"
  requiere_aprobacion:
    - "[acción que requiere visto bueno]"
  prohibido:
    - "[acción prohibida]"
freshness:
  fecha_paquete: "[fecha de hoy ISO 8601]"
expected_output: "[resultado concreto esperado]"
```

Guarda en tu instancia: `context-packets/cp-[id].md`

**Criterio de salida:** archivo guardado, sin placeholders tipo "COMPLETAR", "TBD", "replace this" o "placeholder".

---

## Paso 5 — Verificar antes de entregar

Checklist rápido:

- [ ] ¿El `id` es único y descriptivo?
- [ ] ¿El `target` identifica a un agente o persona real?
- [ ] ¿La `task` describe una acción concreta con resultado verificable?
- [ ] ¿Cada dato en `datos_relevantes` tiene fuente y fecha?
- [ ] ¿Hay al menos 1 restricción en `constraints`?
- [ ] ¿Los 3 niveles de `permissions` están definidos?
- [ ] ¿`freshness.fecha_paquete` tiene la fecha de hoy?
- [ ] ¿`expected_output` describe el entregable con suficiente detalle?
- [ ] ¿No hay placeholders ni campos vacíos obligatorios?
- [ ] ¿No contiene secretos, credenciales ni datos regulados?

Si algún punto falla, corrige antes de entregar el Context Packet al agente.

---

## Errores comunes

| Error | Consecuencia | Solución |
|---|---|---|
| Datos sin fecha | No se sabe si la información es actual | Añadir fecha de verificación a cada dato |
| Resultado esperado vago | El agente interpreta a su manera | Describir el output con detalle: formato, extensión, campos |
| No definir restricciones | El agente hace algo que no debía | Siempre al menos 1 restricción explícita |
| Demasiada información | El agente se confunde o usa datos irrelevantes | Solo lo necesario para la tarea |
| Copiar plantilla sin rellenar | El validador detecta placeholders | Buscar "COMPLETAR" y reemplazar todo |

---

## Siguiente paso

Cuando el Context Packet esté listo, pásalo al agente y ejecuta la tarea. Después documenta el resultado en un Receipt: consulta [`create-first-receipt.md`](create-first-receipt.md).

Para el flujo completo del primer loop interno, consulta [`run-first-internal-loop.md`](run-first-internal-loop.md).

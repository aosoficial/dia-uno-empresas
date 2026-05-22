# Cómo crear tu primer Workflow / SOP

Guía paso a paso para convertir una tarea repetida en un flujo repetible con trigger, pasos, owner, evidencia y definición de hecho.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- al menos un departamento con `department-brain.md`;
- al menos un primer loop interno completado (ver [`run-first-internal-loop.md`](run-first-internal-loop.md)).

Si no tienes esto, completa primero el primer loop interno. Un SOP sin loop completado es especulativo.

## Qué es un Workflow / SOP

Un SOP (Standard Operating Procedure) es un proceso repetible con:

- **Trigger:** qué evento lo activa.
- **Input:** qué información necesita para empezar.
- **Pasos:** qué se hace, en qué orden, y quién lo hace.
- **Output:** qué se produce al final.
- **Owner:** quién es responsable de que funcione.
- **Evidencia:** cómo se demuestra que se ejecutó y con qué resultado.

Sin estos campos, un SOP es solo una lista de deseos.

## Qué NO es un SOP

- No es una descripción genérica de un departamento.
- No es una lista de tareas sueltas sin orden ni trigger.
- No es un proceso que solo se ejecutará una vez (eso es una tarea).
- No es un plan estratégico (eso es un OKR o un rock).

Regla: si no se repite al menos 2 veces al mes, probablemente no necesita SOP todavía.

---

## Paso 1 — Elegir el proceso a documentar

Busca en tu primer loop interno o en tu departamento brain:

| Pregunta | Por qué importa |
|---|---|
| ¿Qué tarea repites cada semana? | Frecuencia alta = más valor del SOP. |
| ¿Dónde pierdes tiempo o cometes errores? | SOPs corrigen dolor real, no teórico. |
| ¿Qué tarea podrías delegar si estuviera documentada? | Un SOP es la base para delegar a un humano o a un agente. |
| ¿El proceso es interno (redactar, analizar, ordenar)? | Empieza con procesos internos; los externos requieren aprobación. |

Buenos primeros SOPs:

| Tipo de empresa | SOP inicial recomendado |
|---|---|
| Agencia | Checklist de entrega de proyecto tipo |
| Consultoría | Preparación de propuesta comercial |
| Freelancer | Onboarding de nuevo proyecto/cliente (parte interna) |

Mal primer SOP: "Gestionar la facturación completa" (demasiado amplio, toca dinero, requiere aprobaciones).

**Criterio de salida:** tienes un proceso concreto, repetible y seguro para documentar.

---

## Paso 2 — Definir el trigger

Un trigger es el evento que inicia el proceso. Sin trigger claro, nadie sabe cuándo ejecutar el SOP.

Ejemplos:

| Trigger | Tipo |
|---|---|
| "El cliente firma el contrato" | Evento externo |
| "Cada lunes a las 9:00" | Cadencia temporal |
| "El equipo entrega un borrador" | Evento interno |
| "El scorecard muestra métrica roja" | Señal del sistema |

Escribe el trigger como una frase que empiece con "Cuando..." o "Cada...":

```
Trigger: Cuando [evento concreto], [quién] inicia [este proceso].
```

**Criterio de salida:** el trigger es específico, observable y no ambiguo.

---

## Paso 3 — Listar inputs y outputs

**Inputs** — qué necesita el proceso para empezar:

- Documentos, datos o fuentes con owner y fecha.
- Context Packet si lo ejecuta un agente.
- Permisos o aprobaciones previas si aplican.

**Output** — qué produce el proceso al terminar:

- Entregable concreto (borrador, checklist, informe, archivo).
- Receipt con resultado observado.
- StateChange si algo cambió en el sistema.

```yaml
inputs:
  - "[qué necesita, fuente, owner, freshness]"
outputs:
  - "[qué produce, formato, dónde se guarda]"
  - "Receipt con resultado y revisión"
```

**Criterio de salida:** inputs tienen fuente y owner; outputs tienen formato y destino.

---

## Paso 4 — Escribir los pasos

Cada paso tiene:

1. **Número de orden.**
2. **Acción concreta** (verbo + objeto).
3. **Quién lo ejecuta** (humano / agente / rol).
4. **Criterio de salida del paso** (cómo se sabe que terminó bien).

Formato recomendado:

```markdown
### Paso 1 — [Nombre corto]

- Acción: [verbo + objeto concreto]
- Ejecuta: [humano / agente / rol]
- Criterio de salida: [qué debe ser verdad al terminar]
- Aprobación requerida: [sí / no — si sí, quién aprueba]
```

Reglas:

- Máximo 7-10 pasos para el primer SOP. Si necesitas más, probablemente es más de un proceso.
- Cada paso debe ser verificable. "Revisar el documento" no es suficiente; "Revisar que el documento tiene los 5 campos de la checklist y marcar correcto/incorrecto" sí.
- Si un paso requiere aprobación externa, económica, legal o de producción, márcalo explícitamente.

**Criterio de salida:** cada paso tiene acción, ejecutor y criterio de salida.

---

## Paso 5 — Asignar owner y frecuencia

| Campo | Qué poner |
|---|---|
| Owner del SOP | Persona responsable de que el SOP funcione y se actualice. |
| Frecuencia esperada | Cuántas veces al mes se ejecuta (estimado). |
| Última revisión | Fecha de última revisión del SOP (hoy si es nuevo). |
| Próxima revisión | Cuándo revisarlo (recomendado: tras 5 ejecuciones o 30 días). |

Un SOP sin owner es un documento muerto. Un SOP sin fecha de revisión se vuelve obsoleto sin que nadie lo note.

**Criterio de salida:** owner, frecuencia y fecha de revisión definidos.

---

## Paso 6 — Definir evidencia y definición de hecho

¿Cómo demuestras que el SOP se ejecutó correctamente?

```yaml
evidencia:
  receipt: "Receipt con acción, resultado observado y revisión humana"
  scorecard: "Métrica del departamento que refleja la ejecución"
  artefacto: "Entregable producido y guardado en la instancia"

definicion_de_hecho:
  - "Todos los pasos completados con criterio de salida verificado"
  - "Receipt creado con resultado observado (no solo 'completado')"
  - "Owner ha revisado el output"
```

Sin definición de hecho, cualquier ejecución parcial puede pasar como "completada".

**Criterio de salida:** hay al menos un tipo de evidencia y una definición de hecho verificable.

---

## Plantilla completa

Usa esta plantilla para crear tu SOP. Guárdalo en tu instancia privada, por ejemplo en `departments/[departamento]/sops/sop-[nombre].md`.

```yaml
# === WORKFLOW / SOP ===

id: "sop-[departamento]-[nombre]-[version]"
nombre: "[nombre descriptivo del proceso]"
departamento: "[departamento al que pertenece]"
owner: "[persona responsable del SOP]"

# Cuándo se activa
trigger: "Cuando [evento concreto]"

# Qué necesita para empezar
inputs:
  - nombre: "[input 1]"
    fuente: "[de dónde viene]"
    owner: "[quién lo mantiene]"
    freshness: "[cuándo se verificó por última vez]"

# Qué produce
outputs:
  - nombre: "[output 1]"
    formato: "[tipo de archivo o entregable]"
    destino: "[dónde se guarda]"
  - nombre: "Receipt"
    formato: "markdown"
    destino: "receipts/"

# Pasos
pasos:
  - paso: 1
    accion: "[verbo + objeto]"
    ejecuta: "[humano / agente / rol]"
    criterio_salida: "[qué debe ser verdad]"
    aprobacion: "[no / sí — quién]"
  - paso: 2
    accion: "[verbo + objeto]"
    ejecuta: "[humano / agente / rol]"
    criterio_salida: "[qué debe ser verdad]"
    aprobacion: "[no / sí — quién]"

# Evidencia
evidencia:
  receipt: "[qué receipt se produce]"
  scorecard: "[qué métrica refleja la ejecución]"
  artefacto: "[qué entregable queda guardado]"

# Definición de hecho
definicion_de_hecho:
  - "[condición verificable 1]"
  - "[condición verificable 2]"

# Metadata
frecuencia: "[veces/mes o cadencia]"
ultima_revision: "[fecha ISO 8601]"
proxima_revision: "[fecha ISO 8601 o 'tras N ejecuciones']"
version: "1.0"
notas: "[observaciones opcionales]"
```

---

## Ejemplo sintético — Agencia "Sol Digital"

### Contexto

Sol Digital ejecuta el primer loop y descubre que la preparación de entregables para clientes es inconsistente. Deciden crear un SOP para estandarizar la entrega.

### SOP: Preparación de entregable para cliente

```yaml
id: "sop-ops-preparar-entregable-v1"
nombre: "Preparación de entregable para cliente"
departamento: "operations-delivery"
owner: "Ana García (fundadora)"

trigger: "Cuando el equipo marca un proyecto como 'listo para entrega' en el tablero interno"

inputs:
  - nombre: "Borrador del entregable"
    fuente: "Carpeta del proyecto en Drive"
    owner: "Responsable del proyecto"
    freshness: "Verificado el día de la entrega"
  - nombre: "Checklist de entrega RRSS"
    fuente: "departments/operations-delivery/outputs/checklist-entrega-rrss-v1.md"
    owner: "Ana García"
    freshness: "Creada 2026-05-22, revisada 2026-05-22"
  - nombre: "Datos del cliente (nombre, canal, fechas)"
    fuente: "CRM interno"
    owner: "Responsable del proyecto"
    freshness: "Verificado antes de iniciar el SOP"

outputs:
  - nombre: "Entregable revisado y empaquetado"
    formato: "Carpeta con archivos finales"
    destino: "Carpeta del proyecto en Drive"
  - nombre: "Receipt de preparación"
    formato: "markdown"
    destino: "receipts/"

pasos:
  - paso: 1
    accion: "Abrir el borrador del entregable y la checklist de entrega"
    ejecuta: "agente/lara o responsable del proyecto"
    criterio_salida: "Ambos documentos abiertos y accesibles"
    aprobacion: "no"
  - paso: 2
    accion: "Verificar cada punto de la checklist contra el borrador"
    ejecuta: "agente/lara"
    criterio_salida: "Cada punto marcado como cumplido o con nota de incumplimiento"
    aprobacion: "no"
  - paso: 3
    accion: "Listar incumplimientos y proponer correcciones"
    ejecuta: "agente/lara"
    criterio_salida: "Lista de incumplimientos con corrección propuesta para cada uno"
    aprobacion: "no"
  - paso: 4
    accion: "Corregir incumplimientos en el borrador"
    ejecuta: "responsable del proyecto"
    criterio_salida: "Todos los incumplimientos corregidos o justificados"
    aprobacion: "no"
  - paso: 5
    accion: "Revisión final del entregable completo"
    ejecuta: "Ana García (owner)"
    criterio_salida: "Ana marca el entregable como 'listo para enviar'"
    aprobacion: "sí — Ana García"
  - paso: 6
    accion: "Crear Receipt con resultado de la preparación"
    ejecuta: "agente/lara o responsable del proyecto"
    criterio_salida: "Receipt guardado con acción, resultado observado, revisora y siguiente paso"
    aprobacion: "no"

evidencia:
  receipt: "Receipt de preparación con resultado de checklist y revisión de Ana"
  scorecard: "QA pass rate (porcentaje de entregas que pasan checklist sin correcciones)"
  artefacto: "Entregable final en carpeta del proyecto"

definicion_de_hecho:
  - "Todos los puntos de la checklist verificados"
  - "Incumplimientos corregidos o justificados"
  - "Ana ha aprobado el entregable"
  - "Receipt creado con resultado observado"

frecuencia: "8-12 veces/mes"
ultima_revision: "2026-05-22"
proxima_revision: "2026-06-05 o tras 5 ejecuciones"
version: "1.0"
notas: "Primer SOP creado tras el primer loop interno. Basado en la checklist de entrega RRSS generada por agente/lara."
```

---

## Errores comunes

| Error | Consecuencia | Cómo evitarlo |
|---|---|---|
| SOP sin trigger | Nadie sabe cuándo ejecutarlo | Escribir "Cuando..." como primera línea |
| SOP sin owner | Nadie lo actualiza ni responde por él | Asignar persona concreta, no un rol genérico |
| Pasos sin criterio de salida | Imposible saber si se completaron | Cada paso necesita un "qué debe ser verdad" |
| SOP demasiado largo (+15 pasos) | Nadie lo sigue completo | Dividir en SOPs más pequeños |
| SOP sin evidencia | No se puede demostrar que se ejecutó | Vincular Receipt y métrica del scorecard |
| SOP sin fecha de revisión | Se vuelve obsoleto sin que nadie lo note | Revisar tras 5 ejecuciones o 30 días |
| SOP para un proceso que no se repite | Esfuerzo desperdiciado | Si no se repite 2 veces/mes, no necesita SOP |
| SOP con paso que requiere aprobación no marcado | Agente actúa sin permiso | Marcar explícitamente qué pasos requieren aprobación y de quién |

---

## Siguiente paso

Después de crear tu primer SOP:

1. Ejecútalo al menos una vez siguiendo los pasos documentados.
2. Crea un Receipt con el resultado real.
3. Actualiza el scorecard del departamento con la métrica relevante.
4. Revisa qué faltó o qué sobró y ajusta el SOP.
5. Si el SOP funciona bien tras 3-5 ejecuciones, considéralo estable.

Si te bloqueas, usa el reporte seguro de DIA UNO en [diauno.io](https://diauno.io) con [`templates/dia-uno/blocker-report.md`](../dia-uno/blocker-report.md). No compartas datos de clientes, secretos ni credenciales.

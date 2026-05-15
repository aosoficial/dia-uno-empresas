# Procedimientos Operativos

## Que operaciones ejecuta el agente y como

---

## Que es

OPERATIONS.md describe las operaciones estandar del agente: rutinas diarias, triggers que inician acciones, flujos de trabajo paso a paso y caminos de escalacion. Es el manual de operaciones del agente.

**Un agente sin operaciones definidas improvisa.** Puede hacer las cosas correctas en el orden incorrecto, o no hacer nada porque no sabe cuando empezar.

## Cuando usarlo

- Como referencia constante del agente durante su operacion diaria.
- Al anadir nuevas operaciones al agente.
- Al diagnosticar por que el agente no ejecuto algo (verificar si esta en sus operaciones).
- Al entrenar a un nuevo operador sobre lo que hace el agente.

## Campos obligatorios por operacion

| Campo | Descripcion |
|-------|-------------|
| `nombre` | Nombre de la operacion |
| `trigger` | Que inicia la operacion |
| `frecuencia` | Con que frecuencia se ejecuta |
| `pasos` | Lista ordenada de pasos |
| `resultado_esperado` | Que deberia pasar al completarla |
| `escalacion` | Que hacer si algo sale mal |
| `feedback_loop` | Que señales de esta operación deben convertirse en mejora del agente o del método |

---

## Plantilla

```yaml
# --- Procedimientos Operativos ---

agente: "agente/[COMPLETAR]"

# --- Rutinas ---

rutinas:

  - nombre: "[COMPLETAR]"
    frecuencia: "[COMPLETAR]"  # diaria / semanal / mensual / por evento
    trigger: "[COMPLETAR]"  # Ej: inicio de jornada, cada lunes a las 9:00
    descripcion: "[COMPLETAR — Que hace esta rutina en una frase]"
    pasos:
      1. "[COMPLETAR]"
      2. "[COMPLETAR]"
      3. "[COMPLETAR]"
    resultado_esperado: "[COMPLETAR]"
    receipt: true  # Genera Receipt al completar? si/no
    escalacion: "[COMPLETAR — Que hacer si falla]"
    feedback_loop: "[COMPLETAR — Que correcciones/patrones activan mejora de pack, skill, memoria o método]"

  - nombre: "[COMPLETAR]"
    frecuencia: "[COMPLETAR]"
    trigger: "[COMPLETAR]"
    descripcion: "[COMPLETAR]"
    pasos:
      1. "[COMPLETAR]"
      2. "[COMPLETAR]"
    resultado_esperado: "[COMPLETAR]"
    receipt: true
    escalacion: "[COMPLETAR]"
    feedback_loop: "[COMPLETAR]"

# --- Operaciones por trigger ---

operaciones_trigger:

  - nombre: "[COMPLETAR]"
    trigger: "[COMPLETAR — Que evento dispara esta operacion]"
    condiciones: "[COMPLETAR — Condiciones que deben cumplirse]"
    pasos:
      1. "[COMPLETAR]"
      2. "[COMPLETAR]"
      3. "[COMPLETAR]"
    resultado_esperado: "[COMPLETAR]"
    receipt: true
    escalacion: "[COMPLETAR]"
    feedback_loop: "[COMPLETAR]"

# --- Flujos de trabajo ---

flujos:

  - nombre: "[COMPLETAR]"
    descripcion: "[COMPLETAR]"
    etapas:
      - etapa: "[COMPLETAR]"
        responsable: "[COMPLETAR]"  # agente / humano / otro agente
        accion: "[COMPLETAR]"
        siguiente: "[COMPLETAR — Que etapa sigue]"
        si_falla: "[COMPLETAR]"

      - etapa: "[COMPLETAR]"
        responsable: "[COMPLETAR]"
        accion: "[COMPLETAR]"
        siguiente: "[COMPLETAR]"
        si_falla: "[COMPLETAR]"

# --- Caminos de escalacion ---

escalacion:
  nivel_1:
    descripcion: "[COMPLETAR — Ej: reintentar la operacion]"
    quien: "agente"
    tiempo_maximo: "[COMPLETAR]"

  nivel_2:
    descripcion: "[COMPLETAR — Ej: notificar al operador]"
    quien: "operador"
    tiempo_maximo: "[COMPLETAR]"

  nivel_3:
    descripcion: "[COMPLETAR — Ej: escalar al backup o responsable superior]"
    quien: "[COMPLETAR]"
    tiempo_maximo: "[COMPLETAR]"
```

---

## Ejemplo — Operaciones de Vega (Meridian Foods)

```yaml
agente: "agente/vega"

rutinas:

  - nombre: "Revision matutina del pipeline"
    frecuencia: "diaria"
    trigger: "Cada dia laborable a las 9:00"
    descripcion: "Revisar el estado de todas las oportunidades abiertas y detectar las que requieren accion."
    pasos:
      1. "Consultar Sales Brain: obtener lista de oportunidades abiertas."
      2. "Identificar oportunidades sin actividad en los ultimos 5 dias."
      3. "Identificar oportunidades con deadline esta semana."
      4. "Generar lista priorizada de acciones del dia."
      5. "Registrar revision en Sales Brain."
    resultado_esperado: "Lista de acciones del dia generada y registrada."
    receipt: true
    escalacion: "Si no puede acceder al Sales Brain, notificar al operador."
    feedback_loop: "Si se repiten oportunidades mal priorizadas, actualizar criterios de priorización en SOUL.md y Sales Brain; si afecta a varios agentes, proponer mejora del método."

  - nombre: "Heartbeat diario"
    frecuencia: "diaria"
    trigger: "Cada dia laborable a las 18:00"
    descripcion: "Enviar reporte de actividad del dia al operador."
    pasos:
      1. "Recopilar Receipts del dia."
      2. "Calcular metricas: propuestas generadas, seguimientos, oportunidades actualizadas."
      3. "Detectar anomalias o drift."
      4. "Generar Heartbeat estructurado."
      5. "Enviar al operador via canal configurado."
    resultado_esperado: "Heartbeat enviado con metricas del dia y alertas si las hay."
    receipt: false  # El Heartbeat es el registro en si mismo.
    escalacion: "Si hay drift detectado, marcar como urgente en el Heartbeat."
    feedback_loop: "Si el Heartbeat omite métricas útiles o genera ruido repetido, actualizar plantilla de Heartbeat y scorecard."

  - nombre: "Revision semanal de propuestas"
    frecuencia: "semanal (lunes)"
    trigger: "Cada lunes a las 10:00"
    descripcion: "Revisar propuestas enviadas la semana anterior y planificar seguimiento."
    pasos:
      1. "Consultar Receipts de propuestas enviadas la semana anterior."
      2. "Verificar cuales recibieron respuesta."
      3. "Programar seguimiento para las que no respondieron."
      4. "Actualizar estado en CRM."
      5. "Informar al operador de las oportunidades en riesgo."
    resultado_esperado: "Todas las propuestas pendientes tienen accion de seguimiento programada."
    receipt: true
    escalacion: "Si hay propuestas sin respuesta despues de 10 dias, escalar al operador como urgente."
    feedback_loop: "Si el patrón de seguimiento falla, ajustar operación semanal y política de memoria de oportunidades."

operaciones_trigger:

  - nombre: "Preparar propuesta comercial"
    trigger: "Recibe Context Packet con tarea 'preparar propuesta'"
    condiciones: "El Context Packet debe incluir datos del cliente, producto recomendado y restricciones."
    pasos:
      1. "Validar que el Context Packet tiene todos los campos obligatorios."
      2. "Consultar Product Brain para precios y disponibilidad actualizados."
      3. "Verificar freshness de los datos del cliente en Sales Brain."
      4. "Generar borrador de propuesta con plantilla corporativa."
      5. "Generar Receipt con el borrador como output."
      6. "Solicitar aprobacion al operador para envio."
    resultado_esperado: "Borrador de propuesta listo para revision del operador."
    receipt: true
    escalacion: "Si faltan datos en el Context Packet, rechazar con Pushback y pedir datos completos."

  - nombre: "Registrar nuevo lead"
    trigger: "El operador informa de un nuevo lead o se detecta via evento"
    condiciones: "Datos minimos: nombre de empresa, contacto, necesidad identificada."
    pasos:
      1. "Verificar que el lead no existe ya en Sales Brain."
      2. "Crear entrada en CRM con datos disponibles."
      3. "Registrar en Sales Brain con estado 'nuevo'."
      4. "Generar StateChange documentando la creacion."
      5. "Proponer al operador siguiente paso (llamada, email, demo)."
    resultado_esperado: "Lead registrado en CRM y Sales Brain con siguiente paso propuesto."
    receipt: true
    escalacion: "Si los datos son insuficientes, pedir mas informacion al operador antes de registrar."

flujos:

  - nombre: "Ciclo de propuesta comercial"
    descripcion: "Desde la identificacion de oportunidad hasta el cierre."
    etapas:
      - etapa: "1. Cualificacion"
        responsable: "agente/vega"
        accion: "Verificar datos del lead, evaluar fit con productos."
        siguiente: "2. Propuesta"
        si_falla: "Descartar lead con nota explicativa en Sales Brain."

      - etapa: "2. Propuesta"
        responsable: "agente/vega"
        accion: "Generar borrador de propuesta."
        siguiente: "3. Aprobacion"
        si_falla: "Pedir mas datos al operador."

      - etapa: "3. Aprobacion"
        responsable: "humano/carlos-ruiz"
        accion: "Revisar y aprobar propuesta."
        siguiente: "4. Envio"
        si_falla: "Vega revisa con correciones y vuelve a paso 2."

      - etapa: "4. Envio"
        responsable: "agente/vega"
        accion: "Enviar propuesta al cliente."
        siguiente: "5. Seguimiento"
        si_falla: "Verificar canal de envio y reintentar."

      - etapa: "5. Seguimiento"
        responsable: "agente/vega"
        accion: "Dar seguimiento segun calendario."
        siguiente: "6. Cierre (operador)"
        si_falla: "Escalar al operador si no hay respuesta en 10 dias."

      - etapa: "6. Cierre"
        responsable: "humano/carlos-ruiz"
        accion: "Negociacion final y cierre."
        siguiente: "fin"
        si_falla: "Registrar razon de perdida en Sales Brain."

escalacion:
  nivel_1:
    descripcion: "El agente reintenta la operacion (maximo 2 reintentos)."
    quien: "agente/vega"
    tiempo_maximo: "1 hora"

  nivel_2:
    descripcion: "Notificar al operador con detalle del problema."
    quien: "humano/carlos-ruiz"
    tiempo_maximo: "4 horas"

  nivel_3:
    descripcion: "Escalar al backup del operador."
    quien: "humano/laura-martinez"
    tiempo_maximo: "24 horas"
```

---

## Errores comunes

1. **Operaciones sin trigger.** Si no se define que inicia la operacion, el agente no sabe cuando ejecutarla. "Revisar pipeline" no tiene trigger. "Cada dia a las 9:00" si.

2. **Pasos demasiado vagos.** "Analizar los datos" no es un paso. "Consultar Sales Brain para obtener oportunidades sin actividad en 5 dias" si lo es.

3. **Sin caminos de escalacion.** Si una operacion falla y no hay escalacion definida, el agente se bloquea o ignora el error.

4. **Flujos sin responsable por etapa.** Cada etapa de un flujo debe tener un responsable claro (agente o humano). Sin responsable, nadie actua.

5. **No generar Receipt en operaciones importantes.** Si una operacion modifica datos o comunica con el exterior, debe dejar Receipt. Sin ello, no hay evidencia.

6. **No definir feedback loop.** Si una operación falla repetidamente y no se define cómo aprender, el agente solo recibe correcciones manuales. Cada operación importante debe decir qué patrones actualizan pack, skill, memoria o método.

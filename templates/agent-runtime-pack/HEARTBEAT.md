# Heartbeat — Pulso Periodico del Agente

## Como monitorizar la salud del agente

---

## Que es

Un Heartbeat es el pulso periodico que emite el agente para confirmar que esta operativo, alineado con su mision y sin problemas. Responde a la pregunta: "Este agente sigue funcionando bien?"

HEARTBEAT.md define la frecuencia, los checks de salud, los umbrales de alerta y el formato que debe seguir cada heartbeat de este agente.

**Un agente sin Heartbeat es un agente invisible.** Puede estar caido, con drift o generando errores sin que nadie se entere.

## Cuando usarlo

- Como referencia para configurar el monitoreo del agente.
- Al diagnosticar por que un agente dejo de responder.
- Al detectar drift (comparar Heartbeats recientes con el SOUL del agente).
- Al evaluar el rendimiento del agente (analizar tendencias de Heartbeats).

---

## Configuracion del Heartbeat

```yaml
# --- Configuracion de Heartbeat ---

agente: "[COMPLETAR]"
frecuencia: "[COMPLETAR]"  # Ej: cada 24 horas, cada 15 minutos
hora_programada: "[COMPLETAR]"  # Ej: 09:00 UTC (si es diario)
canal_de_emision: "[COMPLETAR]"  # Ej: Brain del agente, canal de Telegram
destinatario: "[COMPLETAR]"  # Ej: operador, sistema de monitoreo

# Tiempo maximo sin heartbeat antes de alerta
timeout_alerta: "[COMPLETAR]"  # Ej: 2x la frecuencia (si es cada 24h, alerta a las 48h)
```

---

## Checks de salud obligatorios

Cada Heartbeat debe incluir al menos estos checks. Se pueden anadir mas segun las necesidades del agente.

```markdown
## Checks obligatorios

| Check | Que verifica | Umbral OK | Umbral Warning | Umbral Critical |
|-------|-------------|-----------|----------------|-----------------|
| Conectividad | El agente puede acceder a sus herramientas | Todas conectadas | 1 herramienta caida | >1 herramienta caida |
| Tareas pendientes | Tareas sin completar en la cola | Dentro del limite | 1-2 por encima del limite | >2 por encima o tarea vencida |
| Memoria accesible | El agente puede leer/escribir en sus Brains | Todos accesibles | 1 Brain inaccesible | Brain principal inaccesible |
| Drift | Desviacion del comportamiento respecto al SOUL | Sin drift | Drift menor detectado | Drift grave o recurrente |
| Receipts pendientes | Receipts sin verificacion del operador | 0-2 pendientes | 3-5 pendientes | >5 pendientes |
```

---

## Plantilla de Heartbeat

```yaml
# --- Heartbeat ---

id: "hb-[AGENTE]-[FECHA]-[HORA]"
agent: "agente/[COMPLETAR]"
timestamp: "[COMPLETAR]"  # Formato: YYYY-MM-DDTHH:MM:SSZ
frequency: "[COMPLETAR]"  # Frecuencia configurada

checks:
  - name: "conectividad"
    status: "[COMPLETAR]"  # ok / warning / critical
    value: "[COMPLETAR]"   # Ej: "4/4 herramientas conectadas"
    threshold: "[COMPLETAR]"  # Ej: "todas conectadas"
    notes: "[COMPLETAR o null]"

  - name: "tareas_pendientes"
    status: "[COMPLETAR]"
    value: "[COMPLETAR]"  # Ej: "7"
    threshold: "[COMPLETAR]"  # Ej: "maximo 10"
    notes: "[COMPLETAR o null]"

  - name: "memoria_accesible"
    status: "[COMPLETAR]"
    value: "[COMPLETAR]"  # Ej: "Sales Brain OK, Product Brain OK"
    threshold: "[COMPLETAR]"  # Ej: "todos los Brains accesibles"
    notes: "[COMPLETAR o null]"

  - name: "drift"
    status: "[COMPLETAR]"
    value: "[COMPLETAR]"  # Ej: "sin desviacion"
    threshold: "[COMPLETAR]"  # Ej: "sin drift"
    notes: "[COMPLETAR o null]"

  - name: "receipts_pendientes"
    status: "[COMPLETAR]"
    value: "[COMPLETAR]"  # Ej: "2 pendientes de verificacion"
    threshold: "[COMPLETAR]"  # Ej: "maximo 2"
    notes: "[COMPLETAR o null]"

drift_detected: false  # true / false
drift_details: null  # Descripcion del drift si se detecto

overall_status: "[COMPLETAR]"  # saludable / advertencia / critico

next_heartbeat: "[COMPLETAR]"  # Fecha/hora del proximo heartbeat esperado

# --- Resumen ---
resumen: >
  [COMPLETAR — Una o dos frases describiendo el estado general
  del agente en este momento.]
```

---

## Ejemplo — Heartbeat de Vega (Meridian Foods)

### Ejemplo 1: Heartbeat saludable

```yaml
id: "hb-vega-20260508-0900"
agent: "agente/vega"
timestamp: "2026-05-08T09:00:00Z"
frequency: "cada 24 horas"

checks:
  - name: "conectividad"
    status: "ok"
    value: "4/4 herramientas conectadas (CRM, email, generador, Sales Brain)"
    threshold: "todas conectadas"
    notes: null

  - name: "tareas_pendientes"
    status: "ok"
    value: "6"
    threshold: "maximo 10"
    notes: null

  - name: "memoria_accesible"
    status: "ok"
    value: "Sales Brain OK, Product Brain OK"
    threshold: "todos los Brains accesibles"
    notes: null

  - name: "drift"
    status: "ok"
    value: "sin desviacion"
    threshold: "sin drift"
    notes: null

  - name: "receipts_pendientes"
    status: "ok"
    value: "1 pendiente de verificacion"
    threshold: "maximo 2"
    notes: "rcp-vega-20260507-003 pendiente desde ayer."

drift_detected: false
drift_details: null

overall_status: "saludable"

next_heartbeat: "2026-05-09T09:00:00Z"

resumen: >
  Agente operativo. Todas las herramientas conectadas, 6 tareas
  en cola (dentro del limite), sin drift detectado. 1 Receipt
  pendiente de verificacion.
```

### Ejemplo 2: Heartbeat con advertencia

```yaml
id: "hb-vega-20260509-0900"
agent: "agente/vega"
timestamp: "2026-05-09T09:00:00Z"
frequency: "cada 24 horas"

checks:
  - name: "conectividad"
    status: "warning"
    value: "3/4 herramientas conectadas"
    threshold: "todas conectadas"
    notes: "Generador de propuestas no responde desde las 07:30 UTC."

  - name: "tareas_pendientes"
    status: "ok"
    value: "8"
    threshold: "maximo 10"
    notes: null

  - name: "memoria_accesible"
    status: "ok"
    value: "Sales Brain OK, Product Brain OK"
    threshold: "todos los Brains accesibles"
    notes: null

  - name: "drift"
    status: "ok"
    value: "sin desviacion"
    threshold: "sin drift"
    notes: null

  - name: "receipts_pendientes"
    status: "warning"
    value: "4 pendientes de verificacion"
    threshold: "maximo 2"
    notes: "2 Receipts de ayer y 2 de hace 3 dias sin revisar."

drift_detected: false
drift_details: null

overall_status: "advertencia"

next_heartbeat: "2026-05-10T09:00:00Z"

resumen: >
  Advertencia: generador de propuestas caido desde 07:30 UTC.
  4 Receipts pendientes de verificacion (2 con mas de 48h).
  Resto de checks OK.
```

---

## Reglas de escalado

```markdown
## Reglas de escalado

| Situacion | Accion |
|-----------|--------|
| Heartbeat con todos los checks OK | No requiere accion. Archivar. |
| Heartbeat con 1+ checks en warning | Operador revisa en las proximas 24 horas. |
| Heartbeat con 1+ checks en critical | Notificacion inmediata al operador. |
| Heartbeat no recibido en el tiempo de timeout | Alerta automatica. Verificar que el agente esta activo. |
| 3 Heartbeats consecutivos con warning en el mismo check | Escalar a critical. Requiere intervencion. |
```

---

## Errores comunes

1. **Heartbeat sin checks reales.** Un Heartbeat que siempre dice "todo OK" sin verificar nada es peor que no tener Heartbeat: da falsa seguridad.

2. **Frecuencia inadecuada.** Un agente critico con Heartbeat semanal puede fallar 6 dias sin que nadie lo note. Ajustar la frecuencia a la criticidad del agente.

3. **No actuar sobre warnings.** Los warnings son senales tempranas. Ignorarlos convierte warnings en criticals.

4. **No revisar tendencias.** Un check que pasa de OK a warning a OK repetidamente indica un problema intermitente que merece investigacion.

5. **Drift no medido.** Si el check de drift siempre dice "sin desviacion" sin verificar contra el SOUL, no esta midiendo nada real.

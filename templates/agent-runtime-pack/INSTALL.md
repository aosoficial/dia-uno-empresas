# Install — Guia de Activacion del Agente

## Como poner en marcha un agente nuevo

---

## Que es

INSTALL.md es la guia paso a paso para activar un agente. Documenta los prerequisitos, la secuencia de activacion, las verificaciones post-activacion y los criterios para confirmar que el agente esta operativo.

**Un agente sin guia de instalacion es un agente que depende de la memoria de quien lo creo.** Si esa persona no esta disponible, nadie sabe como activarlo.

## Cuando usarlo

- Al activar un agente nuevo por primera vez.
- Al reactivar un agente que fue desactivado.
- Al migrar un agente a un nuevo entorno.
- Al delegar la operacion de un agente a otra persona.

---

## Prerequisitos

```markdown
## Prerequisitos

Antes de activar este agente, verificar que existen:

- [ ] Agent Runtime Pack completo (todos los archivos obligatorios).
- [ ] Operador asignado con acceso a las herramientas necesarias.
- [ ] Permisos configurados segun PERMISSIONS.md.
- [ ] Herramientas listadas en TOOLS.md disponibles y accesibles.
- [ ] Brains necesarios creados y accesibles (segun MEMORY_POLICY.md).
- [ ] Canal de comunicacion definido (Telegram, Slack, email, etc.).
- [ ] Si existe canal/gateway/perfil previo, `CUTOVER.md` completado y aprobado.
- [ ] Context Packet inicial preparado para la primera operacion real.
- [ ] Heartbeat configurado segun HEARTBEAT.md.

### Dependencias externas

| Dependencia | Estado | Responsable |
|-------------|--------|-------------|
| [COMPLETAR — Ej: CRM conectado] | [pendiente / listo] | [COMPLETAR] |
| [COMPLETAR — Ej: Brain de ventas creado] | [pendiente / listo] | [COMPLETAR] |
| [COMPLETAR — Ej: Canal de Telegram activo] | [pendiente / listo] | [COMPLETAR] |
```

---

## Secuencia de activacion

```markdown
## Secuencia de activacion

### Paso 1 — Verificar el Agent Runtime Pack

Comprobar que todos los archivos obligatorios estan completos usando
el checklist del README.md del pack.

**Verificacion:** Todos los items del checklist marcados.

### Paso 2 — Configurar herramientas

Conectar las herramientas listadas en TOOLS.md. Verificar acceso
con una prueba simple (lectura, no escritura).

Si el agente ya tenia perfil o fue clonado, comparar herramientas
reales contra TOOLS.md. Desactivar o justificar cualquier herramienta
heredada que no sea necesaria.

**Verificacion:** Cada herramienta responde correctamente a una consulta de prueba y no quedan herramientas heredadas sin justificar.

### Paso 3 — Inicializar memoria

Cargar la estructura de memoria definida en MEMORY.md.
Verificar que el agente puede leer y escribir en los Brains
autorizados segun MEMORY_POLICY.md.

Preparar tambien el Context Packet inicial para la primera operacion
real: identidad activa, permisos, herramientas, datos disponibles,
preguntas minimas, resultado esperado y Receipt requerido.

**Verificacion:** Lectura exitosa de al menos un dato de cada Brain autorizado y Context Packet inicial creado.

### Paso 4 — Ejecutar tarea de prueba

Enviar un Context Packet de prueba (tarea simple, baja prioridad,
sin impacto real). Verificar que el agente:

1. Recibe el Context Packet.
2. Ejecuta la tarea segun OPERATIONS.md.
3. Genera un Receipt con todos los campos obligatorios.
4. Registra StateChanges si corresponde.
5. Responde a “Verifica identidad” con la respuesta esperada de `SOUL.md`.

**Verificacion:** Receipt generado con status y outcome reales; identidad activa confirmada en el canal real.

### Paso 5 — Verificar Heartbeat

Esperar un ciclo de Heartbeat. Verificar que el agente emite
el pulso segun la frecuencia configurada en HEARTBEAT.md.

**Verificacion:** Al menos un Heartbeat recibido con todos los checks.

### Paso 6 — Confirmar activacion

Si los pasos 1-5 son exitosos, ejecutar una primera operacion real de
bajo riesgo y pedir aceptacion explicita del owner.

Solo entonces marcar el agente como activo/completado. Registrar la
activacion como Receipt.

**Verificacion:** Receipt de activacion creado. Estado del agente = activo. Primera operacion real aceptada por el owner.
```

---

## Ejemplo — Activacion de Vega (Meridian Foods)

```markdown
## Prerequisitos verificados

- [x] Agent Runtime Pack completo (16 archivos).
- [x] Carlos Ruiz asignado como operador.
- [x] CRM con acceso de lectura/escritura.
- [x] Generador de propuestas configurado.
- [x] Sales Brain creado con datos iniciales.
- [x] Product Brain accesible en modo lectura.
- [x] Canal de Telegram activo.
- [x] Heartbeat configurado: cada 24 horas, 09:00 UTC.

## Secuencia ejecutada

| Paso | Resultado | Fecha |
|------|-----------|-------|
| 1. Verificar pack | OK — 16/16 archivos completos | 2026-05-01 |
| 2. Configurar herramientas | OK — CRM, email, generador de propuestas | 2026-05-01 |
| 3. Inicializar memoria | OK — Sales Brain y Product Brain accesibles | 2026-05-01 |
| 4. Tarea de prueba | OK — Propuesta borrador generada, Receipt creado | 2026-05-02 |
| 5. Verificar Heartbeat | OK — Primer heartbeat recibido 2026-05-02 09:00 | 2026-05-02 |
| 6. Confirmar activacion | OK — Estado = activo | 2026-05-02 |

## Receipt de activacion

id: rcp-vega-20260502-001
action: "Activacion de agente Vega"
status: "exito"
outcome: >
  Agente Vega activado correctamente. Todas las verificaciones
  superadas. Primer Heartbeat emitido. Tarea de prueba completada
  con Receipt valido.
```

---

## Post-activacion

```markdown
## Post-activacion

Acciones a realizar despues de la activacion:

1. **Programar primera evaluacion.** Fecha recomendada: 2 semanas
   despues de la activacion.
2. **Revisar Receipts diariamente** durante la primera semana.
3. **Verificar Heartbeats** para detectar drift temprano.
4. **Documentar ajustes** en el SOUL.md si se detectan
   comportamientos a corregir.
5. **Revisar herramientas heredadas** si aparecieron warnings o latencia.
6. **Confirmar aceptacion del owner** despues de la primera operacion real.

### Checklist post-activacion

- [ ] Primera evaluacion programada para: [COMPLETAR — fecha]
- [ ] Operador revisando Receipts diariamente.
- [ ] Heartbeats llegando segun frecuencia configurada.
- [ ] Sin drift detectado en los primeros 3 dias.
- [ ] Primera operacion real ejecutada.
- [ ] Owner acepto el resultado.
- [ ] Herramientas heredadas revisadas y documentadas.
```

---

## Rollback — Como desactivar

```markdown
## Rollback

Si la activacion falla o se detectan problemas graves:

1. Detener todas las operaciones del agente.
2. Registrar un Receipt de desactivacion con el motivo.
3. Revisar los Receipts y Heartbeats para diagnosticar.
4. Corregir el Agent Runtime Pack segun los hallazgos.
5. Reiniciar desde el Paso 1 de la secuencia de activacion.

**No desactivar sin Receipt.** La desactivacion sin evidencia
es un agujero en la trazabilidad.
```

---

## Errores comunes

1. **Activar sin tarea de prueba.** La tarea de prueba es la unica forma de verificar que el agente funciona de extremo a extremo. Sin ella, se descubren errores en produccion.

2. **No verificar permisos reales.** Que PERMISSIONS.md diga que el agente puede usar el CRM no significa que tenga acceso configurado. Verificar con una prueba real.

3. **Saltar el Heartbeat.** Si el primer Heartbeat no llega, el agente puede estar mal configurado. No asumir que "ya funcionara".

4. **No programar la primera evaluacion.** Sin evaluacion programada, el agente opera sin supervision durante semanas. Los problemas se acumulan.

5. **Copiar la guia de instalacion de otro agente sin adaptarla.** Cada agente tiene herramientas, Brains y dependencias diferentes.

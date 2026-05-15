# CUTOVER — Migración controlada de agente existente

## Qué es

CUTOVER.md documenta cómo migrar un agente que ya existe técnicamente —perfil, canal, bot, gateway o herramientas— hacia una identidad operativa correcta sin romper el servicio.

Se usa cuando el agente ya “vive” en algún canal, pero hay que cambiar su contrato operativo, herramientas o runtime.

Ejemplo típico: un bot de Telegram llamado `urus` existe y responde, pero todavía carga el `SOUL.md` de otro agente.

## Cuándo usarlo

Usa este archivo cuando ocurra cualquiera de estos casos:

- El agente ya tiene canal activo: Telegram, Slack, email, API, etc.
- El perfil/runtime existe, pero puede estar usando identidad antigua.
- El agente fue clonado desde otro agente.
- Hay herramientas heredadas que deben auditarse.
- Hay que reiniciar un gateway o proceso real.
- Hay riesgo de romper una integración ya usada por humanos.

No usarlo para agentes nuevos sin canal activo. En ese caso basta con `INSTALL.md`.

---

## Principio central

**Un canal activo no demuestra que el agente esté bien instalado.**

Hay que verificar cuatro capas por separado:

1. **Perfil/runtime:** dónde corre el agente.
2. **Canal/gateway:** por dónde habla.
3. **Identidad/SOUL:** quién es y cómo decide.
4. **Herramientas:** qué puede usar realmente.

Si una capa está mal, el agente puede parecer vivo pero operar con identidad o permisos incorrectos.

---

## Estado actual antes del cutover

```yaml
agent_id: "[COMPLETAR]"
owner: "[COMPLETAR]"
fecha: "[COMPLETAR]"

perfil_runtime:
  ruta_o_id: "[COMPLETAR]"
  estado: "[pendiente / activo / desconocido]"
  evidencia: "[COMPLETAR]"

canal_gateway:
  canal: "[Telegram / Slack / email / API / otro]"
  estado: "[pendiente / activo / desconocido]"
  proceso_o_servicio: "[COMPLETAR]"
  evidencia: "[COMPLETAR]"

identidad_activa:
  soul_actual: "[COMPLETAR — qué identidad carga ahora]"
  soul_esperado: "[COMPLETAR — qué identidad debería cargar]"
  coincide: false

herramientas_activas:
  - herramienta: "[COMPLETAR]"
    estado: "[activa / desactivar / revisar]"
    motivo: "[COMPLETAR]"
```

---

## Decisión de cutover

```yaml
opcion_elegida: "[mínimo / completo controlado / perfil nuevo]"
por_que: "[COMPLETAR]"
aprobado_por: "[COMPLETAR]"
fecha_aprobacion: "[COMPLETAR]"
```

### Opciones recomendadas

#### Opción A — No tocar todavía

Elegir si falta información crítica.

Riesgo: la identidad equivocada sigue activa.

#### Opción B — Cutover mínimo

Cambiar solo identidad/SOUL y reiniciar el proceso mínimo.

Riesgo: herramientas, memoria o permisos pueden quedar incompletos.

#### Opción C — Cutover completo controlado

Backup, aplicar pack completo, auditar herramientas, reiniciar solo el proceso del agente y verificar.

Recomendación por defecto cuando el agente ya tiene canal activo.

#### Opción D — Perfil nuevo desde cero

Crear un perfil nuevo y migrar canal/token.

Usar solo si el perfil actual está contaminado o no es confiable.

Riesgo: mayor complejidad y posibilidad de duplicar canales/procesos.

---

## Backup previo obligatorio

Antes de tocar nada, crear backup de:

- identidad activa (`SOUL.md` o equivalente);
- configuración del perfil/runtime;
- estado del gateway/canal;
- configuración de herramientas;
- memoria local relevante;
- variables de entorno, solo como archivo protegido, nunca copiando valores al Receipt.

```yaml
backup:
  creado: false
  ruta_o_id: "[COMPLETAR]"
  contiene:
    - "[COMPLETAR]"
  verificado: false
```

Regla: no imprimir secretos en logs, Receipts ni documentación.

---

## Auditoría de herramientas heredadas

Comparar herramientas reales contra `TOOLS.md`.

```yaml
herramientas:
  requeridas:
    - "[COMPLETAR]"
  reales_detectadas:
    - "[COMPLETAR]"
  desactivar:
    - herramienta: "[COMPLETAR]"
      motivo: "[heredada / rota / innecesaria / demasiado permiso]"
  mantener:
    - herramienta: "[COMPLETAR]"
      verificacion: "[COMPLETAR]"
```

Criterio: si una herramienta no está justificada por `TOOLS.md`, debe quedar desactivada o marcada para aprobación.

---

## Secuencia de ejecución

```markdown
### Paso 1 — Confirmar aprobación
- [ ] Owner aprobó el cutover.
- [ ] Riesgos explicados.
- [ ] Rollback disponible.

### Paso 2 — Crear backup
- [ ] Backup creado.
- [ ] Backup verificado.
- [ ] Secretos no impresos.

### Paso 3 — Aplicar identidad y pack
- [ ] `SOUL.md` actualizado.
- [ ] `PERMISSIONS.md` actualizado.
- [ ] `MEMORY_POLICY.md` actualizado.
- [ ] `TOOLS.md` actualizado.
- [ ] `OPERATIONS.md` actualizado.
- [ ] Resto del pack aplicado si corresponde.

### Paso 4 — Auditar herramientas
- [ ] Herramientas reales listadas.
- [ ] Herramientas heredadas desactivadas.
- [ ] Herramientas críticas probadas.

### Paso 5 — Reinicio acotado
- [ ] Solo se reinició el proceso/gateway del agente objetivo.
- [ ] No se tocaron otros agentes.

### Paso 6 — Verificación técnica
- [ ] Perfil/runtime activo.
- [ ] Canal/gateway activo.
- [ ] Herramientas críticas responden.
- [ ] No hay errores bloqueantes en logs.

### Paso 7 — Verificación de identidad activa
- [ ] Enviar: “Verifica identidad”.
- [ ] La respuesta coincide con `Identity Answer` del `SOUL.md`.
- [ ] Si responde como otro agente, ejecutar rollback.

### Paso 8 — Primera operación real
- [ ] Ejecutar tarea real de bajo riesgo.
- [ ] Generar Receipt.
- [ ] Owner confirma utilidad.

### Paso 9 — Cierre
- [ ] Receipt de cutover creado.
- [ ] StateChange creado si cambió identidad/permisos/herramientas.
- [ ] Owner aceptó cierre.
```

---

## Prueba obligatoria: identidad activa

Prompt recomendado:

```text
Verifica identidad. Responde en una frase corta.
```

Respuesta esperada:

```text
[COMPLETAR — copiar la respuesta esperada desde SOUL.md / Identity Answer]
```

Regla:

- Si responde con otro nombre, rol o misión, el cutover no está completado.
- Si responde genérico pero correcto, revisar si el `SOUL.md` necesita una respuesta más precisa.

---

## Rollback

```markdown
## Rollback

Condiciones para rollback:
- el canal deja de responder;
- el agente responde con identidad incorrecta;
- herramientas críticas fallan;
- aparece error de permisos o credenciales;
- owner rechaza la primera operación real.

Pasos:
1. Detener o reiniciar solo el proceso del agente objetivo.
2. Restaurar archivos desde backup.
3. Verificar canal/gateway.
4. Probar “Verifica identidad”.
5. Crear Receipt de rollback con causa y evidencia.
6. No reintentar cutover sin corregir causa raíz.
```

---

## Receipt final de cutover

```yaml
receipt:
  action_type: "agent_cutover"
  agent_id: "[COMPLETAR]"
  title: "Cutover de agente ejecutado"
  owner: "[COMPLETAR]"
  fecha: "[COMPLETAR]"
  backup_ref: "[COMPLETAR]"
  cambios:
    - "[COMPLETAR]"
  herramientas_desactivadas:
    - "[COMPLETAR]"
  verificaciones:
    runtime: "[OK / fallo]"
    canal: "[OK / fallo]"
    identidad: "[OK / fallo]"
    herramientas: "[OK / fallo]"
    primera_operacion_real: "[OK / pendiente / fallo]"
  owner_acceptance: "[sí / no / pendiente]"
  rollback_disponible: true
```

---

## Errores comunes

1. **Confundir canal vivo con agente correcto.** El bot puede responder, pero con identidad equivocada.
2. **No hacer backup.** Sin backup, un cambio pequeño puede convertirse en interrupción larga.
3. **Reiniciar procesos equivocados.** Un cutover de un agente no debe afectar otros agentes.
4. **Copiar secretos al Receipt.** La evidencia debe citar rutas/ids, no valores sensibles.
5. **No auditar herramientas heredadas.** Herramientas antiguas generan ruido, latencia o permisos innecesarios.
6. **Cerrar sin primera operación real.** Pasar tests técnicos no significa que el agente sea útil.
7. **Cerrar sin aceptación del owner.** La activación termina cuando el owner confirma que el agente funciona en el uso real.

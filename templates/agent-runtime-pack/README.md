# Agent Runtime Pack

## Paquete operativo completo para un agente DIA UNO Empresas

---

## Que es

El Agent Runtime Pack es el conjunto de documentos que define completamente a un agente operativo. Contiene su identidad, contrato, permisos, herramientas, memoria, operaciones y protocolos de comunicacion.

**Sin un Agent Runtime Pack completo, un agente no puede activarse.**

Un agente sin pack es un agente sin contrato: no tiene limites claros, no deja evidencia y no puede evaluarse.

## Cuando usarlo

- Al crear un agente nuevo (antes de activarlo).
- Al auditar un agente existente (para verificar que esta completo).
- Al transferir un agente a otro operador (como documentacion de traspaso).
- Al reactivar un agente que fue desactivado.

---

## Contenido del pack

| Archivo | Proposito | Prioridad |
|---------|-----------|-----------|
| `IDENTITY.md` | Quien es el agente | Obligatorio |
| `SOUL.md` | Contrato operativo vivo | Obligatorio |
| `ROLE_CARD.md` | Resumen ejecutivo de una pagina | Obligatorio |
| `USER.md` | Perfil del operador humano | Obligatorio |
| `PERMISSIONS.md` | Matriz de permisos | Obligatorio |
| `TOOLS.md` | Herramientas disponibles | Obligatorio |
| `MEMORY_POLICY.md` | Politica de memoria | Obligatorio |
| `MEMORY.md` | Memoria de trabajo del agente | Obligatorio |
| `OPERATIONS.md` | Procedimientos operativos | Obligatorio |
| `CONTEXT_PACKET.md` | Formato de Context Packets | Obligatorio |
| `STATECHANGE.md` | Formato de StateChanges | Obligatorio |
| `RECEIPT.md` | Formato de Receipts | Obligatorio |
| `AGENTS.md` | Registro de otros agentes | Recomendado |
| `HANDOFF.md` | Protocolo de traspaso | Recomendado |
| `HEARTBEAT.md` | Configuracion del pulso periodico | Obligatorio |
| `AUTONOMY.md` | Nivel de autonomia, 1:3:1 y approval gates | Obligatorio |
| `MATURITY_REVIEW.md` | Revision de comunicacion, criterio y aprendizaje | Obligatorio durante prueba |
| `INSTALL.md` | Guia de activacion | Obligatorio |
| `CUTOVER.md` | Migracion controlada si ya existe perfil/canal/gateway | Obligatorio cuando aplica |

`OPERATIONS.md` y `MEMORY_POLICY.md` deben incluir feedback loops: qué correcciones actualizan el pack, la memoria, una skill o el método DIA UNO Empresas.

---

## Orden recomendado de creacion

1. **IDENTITY.md** — Define quien es el agente.
2. **SOUL.md** — Define como opera (contrato).
3. **ROLE_CARD.md** — Resume lo esencial en una pagina.
4. **USER.md** — Define quien es el operador.
5. **PERMISSIONS.md** — Define que puede y que no puede hacer.
6. **TOOLS.md** — Define con que herramientas cuenta.
7. **MEMORY_POLICY.md** — Define como gestiona la memoria.
8. **MEMORY.md** — Inicializa la memoria de trabajo.
9. **OPERATIONS.md** — Define que operaciones ejecuta.
10. **CONTEXT_PACKET.md** — Define el formato de contexto que recibe.
11. **STATECHANGE.md** — Define como registra cambios.
12. **RECEIPT.md** — Define como documenta acciones.
13. **AGENTS.md** — Registra otros agentes con los que interactua.
14. **HANDOFF.md** — Define protocolos de traspaso.
15. **HEARTBEAT.md** — Configura el pulso periodico.
16. **AUTONOMY.md** — Define nivel de autonomia, 1:3:1 y approval gates.
17. **MATURITY_REVIEW.md** — Registra señales de madurez y cambios de nivel.
18. **INSTALL.md** — Documenta la activacion paso a paso.
19. **CUTOVER.md** — Documenta la migracion si el agente ya tiene perfil, canal, gateway o herramientas reales.

---

## Checklist de completitud

Antes de activar un agente, verificar que:

- [ ] `IDENTITY.md` tiene nombre, version, tipo, owner, fecha y estado.
- [ ] `SOUL.md` tiene todas las secciones completadas (Identity a Identity Answer).
- [ ] `ROLE_CARD.md` resume mision, responsabilidades, limites y metricas.
- [ ] `USER.md` tiene el perfil completo del operador.
- [ ] `PERMISSIONS.md` tiene la matriz completa de acciones y niveles.
- [ ] `TOOLS.md` lista todas las herramientas con nivel de permiso.
- [ ] `MEMORY_POLICY.md` define retencion, freshness y reglas de sincronizacion.
- [ ] `MEMORY.md` tiene la estructura de memoria inicial.
- [ ] `OPERATIONS.md` describe rutinas, triggers y flujos de trabajo.
- [ ] `CONTEXT_PACKET.md` define la estructura de los paquetes de contexto.
- [ ] `STATECHANGE.md` define cuando y como registrar cambios.
- [ ] `RECEIPT.md` define la estructura y estados de los recibos.
- [ ] `AGENTS.md` lista los agentes conocidos y protocolos de interaccion.
- [ ] `HANDOFF.md` define como traspasar trabajo.
- [ ] `HEARTBEAT.md` tiene frecuencia, indicadores y umbrales de alerta.
- [ ] `AUTONOMY.md` define nivel inicial, 1:3:1 y acciones que requieren OK.
- [ ] `MATURITY_REVIEW.md` define cómo evaluar comunicación, criterio, prudencia, ejecución y aprendizaje.
- [ ] `INSTALL.md` tiene los pasos de activacion y verificacion.
- [ ] Si el agente ya tiene perfil/canal/gateway, `CUTOVER.md` documenta backup, migracion, verificacion y rollback.
- [ ] La identidad activa fue verificada en el canal real con “Verifica identidad”.
- [ ] Las herramientas reales fueron comparadas contra `TOOLS.md` y las heredadas innecesarias quedaron desactivadas o justificadas.
- [ ] Existe un Context Packet inicial para la primera operacion real.
- [ ] El owner acepto la primera operacion real antes de marcar el agente como completado.
- [ ] El agente tiene definido cómo transforma feedback humano en mejora verificable.

---

## Ejemplo de estructura de directorios

```text
agents/
  vega/
    IDENTITY.md
    SOUL.md
    ROLE_CARD.md
    USER.md
    PERMISSIONS.md
    TOOLS.md
    MEMORY_POLICY.md
    MEMORY.md
    OPERATIONS.md
    CONTEXT_PACKET.md
    STATECHANGE.md
    RECEIPT.md
    AGENTS.md
    HANDOFF.md
    HEARTBEAT.md
    INSTALL.md
    CUTOVER.md        ← Migración si ya existe perfil, canal o gateway real
```

Cada agente tiene su propio directorio con su pack completo. Los archivos de este directorio `templates/agent-runtime-pack/` son las plantillas base para crear cualquier agente nuevo.

---

## Errores comunes

1. **Activar un agente con pack incompleto.** Si falta PERMISSIONS.md, el agente no sabe que tiene prohibido. Si falta HEARTBEAT.md, nadie detecta drift.

2. **Copiar el pack de otro agente sin adaptarlo.** Cada agente tiene mision, permisos y herramientas distintas. Copiar sin adaptar crea agentes con permisos incorrectos.

3. **Confundir canal vivo con identidad correcta.** Que un bot responda en Telegram, Slack o email no demuestra que cargue el `SOUL.md` correcto. Verificar siempre con “Verifica identidad”.

4. **No auditar herramientas heredadas.** Un perfil clonado puede conservar herramientas antiguas, rutas rotas o permisos innecesarios. Comparar siempre herramientas reales contra `TOOLS.md`.

5. **No actualizar el pack cuando cambia el agente.** El pack es un documento vivo. Si se anaden herramientas o cambian permisos, el pack debe reflejarlo.

6. **Tratar el pack como documentacion decorativa.** El pack es el contrato operativo del agente. Si el agente no lo consulta o no se verifica contra el, no sirve.

7. **Cerrar activacion sin primera operacion real.** Un agente puede pasar checks tecnicos y aun asi no ser util. El cierre requiere prueba real y aceptacion del owner.

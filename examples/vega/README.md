# Ejemplo completo — Agente Vega (Meridian Foods)

## Qué es este ejemplo

Este directorio contiene un ejemplo mínimo completo de Company Brain System aplicado a una empresa ficticia: **Meridian Foods**.

Incluye:

- Un **Company Brain mínimo** con ontología, hechos y decisiones.
- Un **Agent Runtime Pack** para el agente **Vega** (ventas) con los archivos esenciales.

**Nada aquí es real.** Todos los nombres, datos y cifras son ficticios y sirven para ilustrar cómo se aplica el método.

---

## Meridian Foods — Contexto

| Dato | Valor |
|------|-------|
| **Empresa** | Meridian Foods (ficticia) |
| **Sector** | Alimentación |
| **Tamaño** | 50 empleados |
| **Productos** | 3 líneas: estándar, premium, gourmet |
| **Equipo de ventas** | 8 personas |

---

## Estructura de este ejemplo

```text
examples/vega/
  README.md                         ← este archivo
  company-brain-minimal.md          ← Company Brain mínimo de Meridian Foods
  agent-runtime-pack/
    IDENTITY.md                     ← ficha de identidad de Vega
    SOUL.md                         ← contrato operativo de Vega
    PERMISSIONS.md                  ← matriz de permisos de Vega
```

---

## Cómo usar este ejemplo

1. **Lee `company-brain-minimal.md`** para ver cómo se estructura un Company Brain con ontología, hechos y decisiones.
2. **Lee los archivos de `agent-runtime-pack/`** para ver un agente definido con los 3 archivos esenciales.
3. **Compara con las plantillas** en `templates/` para ver qué campos se rellenaron y cuáles se dejaron fuera del mínimo.

### Para crear tu propio agente a partir de este ejemplo

```bash
# Copia el Agent Runtime Pack completo (con todas las plantillas)
cp -r templates/agent-runtime-pack/ mi-agente/

# Usa los archivos de Vega como referencia para rellenar los tuyos
```

---

## Archivos del Agent Runtime Pack completo

Este ejemplo incluye solo los **3 archivos esenciales** para empezar. El Agent Runtime Pack completo tiene 18 archivos. Aquí está la relación:

| Archivo | ¿Incluido aquí? | Plantilla completa |
|---------|:---:|---|
| IDENTITY.md | ✅ | `templates/agent-runtime-pack/IDENTITY.md` |
| SOUL.md | ✅ | `templates/agent-runtime-pack/SOUL.md` |
| PERMISSIONS.md | ✅ | `templates/agent-runtime-pack/PERMISSIONS.md` |
| OPERATIONS.md | — | `templates/agent-runtime-pack/OPERATIONS.md` |
| TOOLS.md | — | `templates/agent-runtime-pack/TOOLS.md` |
| MEMORY.md | — | `templates/agent-runtime-pack/MEMORY.md` |
| MEMORY_POLICY.md | — | `templates/agent-runtime-pack/MEMORY_POLICY.md` |
| HEARTBEAT.md | — | `templates/agent-runtime-pack/HEARTBEAT.md` |
| HANDOFF.md | — | `templates/agent-runtime-pack/HANDOFF.md` |
| RECEIPT.md | — | `templates/agent-runtime-pack/RECEIPT.md` |
| STATECHANGE.md | — | `templates/agent-runtime-pack/STATECHANGE.md` |
| CONTEXT_PACKET.md | — | `templates/agent-runtime-pack/CONTEXT_PACKET.md` |
| ROLE_CARD.md | — | `templates/agent-runtime-pack/ROLE_CARD.md` |
| INSTALL.md | — | `templates/agent-runtime-pack/INSTALL.md` |
| CUTOVER.md | — | `templates/agent-runtime-pack/CUTOVER.md` |
| USER.md | — | `templates/agent-runtime-pack/USER.md` |
| AGENTS.md | — | `templates/agent-runtime-pack/AGENTS.md` |
| README.md | — | `templates/agent-runtime-pack/README.md` |

> **Nota:** para un agente en producción, se recomienda completar al menos OPERATIONS.md, TOOLS.md y HEARTBEAT.md además de los 3 esenciales.

---

## Relación con las plantillas standalone

Además de los archivos dentro del Agent Runtime Pack, existen plantillas standalone en `templates/`:

- `templates/receipts/receipt-template.md`
- `templates/statechanges/statechange-template.md`
- `templates/context-packets/context-packet-template.md`

**¿Cuál usar?** Las plantillas dentro del pack (`templates/agent-runtime-pack/RECEIPT.md`, etc.) están pensadas para definir las **reglas** de cómo un agente específico genera sus Receipts, StateChanges y Context Packets. Las plantillas standalone son **plantillas generales** que se usan para crear instancias individuales de esas primitivas, independientemente del agente. Ver [`docs/07_quick_start.md`](../../docs/07_quick_start.md) para la ruta práctica.

---

*Este ejemplo usa la empresa ficticia Meridian Foods, también referenciada en los templates y en `docs/01_aos_system.md`.*

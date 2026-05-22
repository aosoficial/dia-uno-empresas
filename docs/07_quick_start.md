# 07 — Inicio rápido

Esta guía te ayuda a crear la versión mínima útil de Company Brain System en más o menos una hora.

Vas a crear:

1. un **Company Brain** pequeño;
2. un **Agent Runtime Pack** para un agente;
3. un **Receipt** como evidencia de trabajo.

No necesitas una base de datos ni una herramienta SaaS. Con un editor de texto y Git basta.

---

## Antes de empezar

Necesitas:

- Git;
- un editor de texto;
- Python 3.8+ solo si quieres ejecutar los scripts de validación.

Términos útiles:

- **Company Brain:** la memoria compartida de tu empresa.
- **Agent Runtime Pack:** los archivos que dicen quién es un agente, qué puede hacer, qué no puede hacer y cómo debe trabajar.
- **Receipt:** un registro corto que prueba qué hizo un agente, qué cambió y cómo se revisó.
- **StateChange:** un registro corto de algo importante que cambió.
- **Context Packet:** el contexto que necesita un agente antes de hacer trabajo útil.

Si algún término no queda claro, usa [`docs/08_glossary.md`](08_glossary.md).

---

## Paso 1 — Clona el repositorio

```bash
git clone https://github.com/aosoficial/company-brain-system.git
cd company-brain-system
```

Verás esta estructura:

```text
company-brain-system/
  docs/           manuales del método
  templates/      plantillas operativas reutilizables
  schemas/        contratos de validación
  registry/       registros de ejemplo
  examples/       ejemplos sintéticos
  scripts/        scripts de validación y construcción
```

---

## Paso 2 — Crea un Company Brain pequeño

El Company Brain es la memoria compartida de tu organización.

Empieza solo con tres cosas importantes. Ejemplo:

```text
Entidades: cliente, producto, decisión
Relaciones: cliente compra producto; decisión afecta producto
```

Crea un archivo llamado `my-company-brain.md`:

```markdown
# Company Brain — [Nombre de la empresa]

## Entidades principales

| Entidad | Propiedades clave | Ritmo de actualización |
|---|---|---|
| cliente | nombre, sector, contacto principal, estado | semanal |
| producto | nombre, precio, estado | mensual |
| decisión | descripción, fecha, responsable, válida hasta | cuando cambie |

## Hechos principales

- **Misión:** [Una frase]
- **Equipo:** [Personas / roles]
- **Productos:** [Lista corta]

## Decisiones activas

| Decisión | Fecha | Responsable | Válida hasta |
|---|---|---|---|
| [Ejemplo: el plan Pro cuesta 49 €/mes] | 2026-05-01 | [Nombre] | Revisión Q3 |

## Reglas activas

- [Ejemplo: descuento máximo sin aprobación: 10%]
- [Ejemplo: todos los emails a clientes VIP necesitan revisión antes de enviarse]
```

Referencia: [`docs/03_brain_architecture.md`](03_brain_architecture.md)

---

## Paso 3 — Crea tu primer agente

Un agente no debería operar desde un prompt vago. Necesita un pack operativo claro.

Copia la plantilla:

```bash
cp -r templates/agent-runtime-pack/ my-first-agent/
```

Rellena primero los tres archivos esenciales.

### 3.1 IDENTITY.md

Quién es el agente:

```yaml
name: "Atlas"
id: "agent/atlas"
version: "1.0.0"
type: "sales"
description: "Agente de ventas que prepara propuestas y gestiona el pipeline."
owner:
  name: "Tu nombre"
  email: "tu@empresa.com"
  role: "Fundador"
created_at: "2026-05-09"
status: "testing"
```

### 3.2 SOUL.md

El contrato operativo del agente:

```markdown
## Identity

**Name:** Atlas
**Role:** Agente de ventas
**Domain:** Ventas
**One sentence:** Gestiono el pipeline y preparo propuestas.

## Mission Map

**Main mission:** Preparar propuestas comerciales con el contexto correcto.

**Key goals:**
1. Mantener el pipeline actualizado.
2. Redactar propuestas en menos de 24 horas.
3. No enviar nada a un cliente sin aprobación.

## Pushback Rules

1. **Falta contexto** → pedir un Context Packet antes de actuar.
2. **Descuento fuera del rango aprobado** → escalar al operador.
3. **Dato obsoleto** → señalarlo y pedir actualización.
```

### 3.3 PERMISSIONS.md

Qué puede y qué no puede hacer:

```yaml
agent: "agent/atlas"
permissions_version: "2026-05-09"
permissions:
  - action: "Read Company Brain"
    level: "autonomous"
  - action: "Draft commercial proposal"
    level: "autonomous"
  - action: "Send proposal to client"
    level: "approval_required"
  - action: "Change prices"
    level: "forbidden"
default_rule: "approval_required"
```

Referencia: [`docs/04_agent_onboarding.md`](04_agent_onboarding.md)

---

## Paso 4 — Crea tu primer Receipt

Un Receipt es evidencia. Evita el trabajo de “confía en mí, ya lo hice”.

Crea un archivo llamado `my-first-receipt.yaml`:

```yaml
id: "rcp-atlas-20260509-001"
agent: "agent/atlas"
action: "Prepare commercial proposal for Example Customer"
timestamp: "2026-05-09T10:00:00Z"
inputs:
  context_packet: "briefing verbal del fundador"
  additional_instructions: "Incluir tabla de precios del plan Pro."
outputs:
  - "proposal-example-v1.md generated"
outcome: >
  Borrador de propuesta generado con tabla de precios actualizada.
  Pendiente de revisión del fundador antes de enviar.
status: "pending_verification"
```

Importante: “hecho” no significa “exitoso”. El campo `outcome` debe describir el resultado real.

---

## Paso 5 — Valida el repositorio

Este paso es opcional, pero recomendable.

```bash
pip install pyyaml
python scripts/validate_repo.py
python scripts/validate_schemas.py
```

Estos scripts comprueban que la estructura del repositorio y los schemas YAML son consistentes.

---

## Qué leer después

- **Entender el método completo:** [`docs/00_master_playbook.md`](00_master_playbook.md)
- **Entender los registros operativos:** [`docs/01_aos_system.md`](01_aos_system.md) y [`docs/02_operational_memory.md`](02_operational_memory.md)
- **Crear un Department Brain:** [`docs/03_brain_architecture.md`](03_brain_architecture.md)
- **Ver un ejemplo completo:** [`examples/vega/`](../examples/vega/)
- **Consultar un término:** [`docs/08_glossary.md`](08_glossary.md)
- **Operar día a día:** [`docs/05_operator_manual.md`](05_operator_manual.md)
- **Pedir a un agente que te ayude a instalarlo:** [`docs/14_agent_installation_process.md`](14_agent_installation_process.md)

---

## Qué has creado

```text
Versión mínima del Company Brain
Versión mínima del Agent Runtime Pack
Primer Receipt como evidencia de trabajo
```

Esto basta para entender el sistema básico. Todo lo demás consiste en añadir mejor contexto, permisos más seguros y mejores hábitos operativos con el tiempo.

Si te bloqueas, lee [`docs/12_get_help_from_dia_uno.md`](12_get_help_from_dia_uno.md) o abre un issue en GitHub.

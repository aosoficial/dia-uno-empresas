# 07 — Quick Start

> **Need help applying this?** This page is part of Company Brain System, an open method by Libera. If you get stuck, start with the [Quick Start](07_quick_start.md), use the [Company Brain intake](../templates/questionnaires/company-brain-intake.md), or see [how Libera can help](12_get_help_from_libera.md).

## Tu primera hora con Company Brain System

---

## Objetivo

En menos de 1 hora tendrás:

1. Un **Company Brain mínimo** con 3 entidades.
2. Un **agente con Agent Runtime Pack** operativo.
3. Tu primera **primitiva operativa** (Receipt) creada.

No necesitas instalar nada. Solo un editor de texto y Git.

---

## Requisitos

- Git instalado.
- Un editor de texto (VS Code, Obsidian, vim — cualquiera sirve).
- Python 3.8+ (solo si quieres ejecutar los scripts de validación; no es obligatorio para empezar).

---

## Paso 1 — Clonar el repositorio (2 minutos)

```bash
git clone https://github.com/aosoficial/company-brain-system.git
cd company-brain-system
```

Explora la estructura:

```text
company-brain-system/
  docs/           ← manuales del método (empieza por aquí si quieres teoría)
  templates/      ← plantillas operativas (empieza por aquí si quieres práctica)
  schemas/        ← schemas YAML de validación
  registry/       ← registros centralizados
  examples/       ← ejemplo completo con empresa ficticia
  scripts/        ← validación y exportación
```

---

## Paso 2 — Crear tu Company Brain mínimo (15 minutos)

El Company Brain es la memoria central de tu organización. Empieza con lo mínimo: 3 entidades.

### 2.1 — Define tu ontología inicial

Piensa en tu empresa. ¿Cuáles son las 3 entidades más importantes? Ejemplo:

```text
Entidades: cliente, producto, decisión
Relaciones: cliente → compra → producto; decisión → afecta → producto
```

> **Consejo:** no intentes mapear toda tu empresa. 3-5 entidades son suficientes para empezar. Siempre puedes añadir más.

### 2.2 — Crea el archivo

Crea un archivo `my-company-brain.md` en la raíz (o donde prefieras):

```markdown
# Company Brain — [Nombre de tu empresa]

## Ontología

| Entidad | Propiedades clave | Freshness |
|---------|-------------------|-----------|
| cliente | nombre, sector, contacto principal, estado | semanal |
| producto | nombre, precio, estado | mensual |
| decisión | descripción, fecha, responsable, vigencia | cuando cambie |

## Hechos fundamentales

- **Misión:** [Una frase]
- **Equipo:** [Número de personas, estructura básica]
- **Productos:** [Lista breve]

## Decisiones vigentes

| Decisión | Fecha | Responsable | Vigencia |
|----------|-------|-------------|----------|
| [Ejemplo: Precio del plan Pro es 49 €/mes] | 2026-05-01 | [Nombre] | Hasta revisión Q3 |

## Políticas activas

- [Ejemplo: Descuento máximo sin aprobación: 10%]
- [Ejemplo: Todo email a cliente VIP requiere revisión]
```

> **Referencia completa:** [`docs/03_brain_architecture.md`](03_brain_architecture.md) explica en detalle la arquitectura de cerebros.

---

## Paso 3 — Crear tu primer agente (20 minutos)

Un agente necesita un **Agent Runtime Pack**: un conjunto de archivos que definen quién es, qué puede hacer y cómo opera.

### 3.1 — Copia la plantilla

```bash
cp -r templates/agent-runtime-pack/ my-first-agent/
```

### 3.2 — Rellena los archivos esenciales

Solo necesitas 3 archivos para empezar. El resto puede esperar.

**IDENTITY.md** — Quién es:

```yaml
nombre: "Atlas"
id: "agente/atlas"
version: "1.0.0"
tipo: "ventas"
descripcion: "Agente de ventas que prepara propuestas y gestiona el pipeline."
owner:
  nombre: "Tu nombre"
  email: "tu@email.com"
  rol: "Fundador"
fecha_creacion: "2026-05-09"
estado: "en_pruebas"
```

**SOUL.md** — Su contrato operativo (rellena al menos Identity, Mission Map y Pushback Rules):

```markdown
## Identity

**Nombre:** Atlas
**Rol:** Agente de ventas
**Dominio:** Comercial
**Una frase:** Gestiono el pipeline y preparo propuestas.

## Mission Map

**Misión principal:** Preparar propuestas comerciales rápidas y con contexto.
**Objetivos clave:**
1. Mantener el pipeline actualizado.
2. Generar propuestas en menos de 24 horas.
3. No enviar nada sin aprobación.

## Pushback Rules

1. **Sin contexto suficiente** → Pedir Context Packet antes de actuar.
2. **Descuento fuera de rango** → Escalar al operador.
3. **Dato obsoleto** → Señalarlo y pedir actualización.
```

**PERMISSIONS.md** — Qué puede y qué no:

```yaml
agente: "agente/atlas"
version_permisos: "2026-05-09"
permisos:
  - accion: "Consultar Company Brain"
    nivel: "autonomo"
  - accion: "Generar borrador de propuesta"
    nivel: "autonomo"
  - accion: "Enviar propuesta a cliente"
    nivel: "con_aprobacion"
  - accion: "Modificar precios"
    nivel: "prohibido"
regla_por_defecto: "con_aprobacion"
```

> **Referencia completa:** [`docs/04_agent_onboarding.md`](04_agent_onboarding.md) explica todo el proceso de onboarding.

---

## Paso 4 — Crear tu primer Receipt (10 minutos)

Un Receipt registra qué hizo un agente y con qué resultado. Crea uno manualmente para entender la mecánica.

Crea un archivo `my-first-receipt.yaml`:

```yaml
id: "rcp-atlas-20260509-001"
agent: "agente/atlas"
action: "Preparar propuesta comercial para Cliente Ejemplo S.L."
timestamp: "2026-05-09T10:00:00Z"
inputs:
  context_packet: "verbal — briefing del fundador"
  additional_instructions: "Incluir tabla de precios del plan Pro."
outputs:
  - "propuesta-ejemplo-v1.pdf generada"
outcome: >
  Propuesta generada con tabla de precios actualizada.
  Pendiente de revisión por el fundador antes de enviar.
status: "pendiente_verificacion"
```

> **Principio clave:** "Completado" no significa "exitoso". El campo `outcome` describe el resultado real, no solo que se hizo.

---

## Paso 5 — Validar (5 minutos, opcional)

Si tienes Python instalado:

```bash
pip install pyyaml
python scripts/validate_repo.py
python scripts/validate_schemas.py
```

Estos scripts verifican que la estructura del repositorio y los schemas YAML sean correctos.

---

## ¿Qué sigue?

| Quiero… | Lee… |
|---------|------|
| Entender el método completo | [`docs/00_master_playbook.md`](00_master_playbook.md) |
| Entender las primitivas (StateChange, Context Packet, Receipt) | [`docs/01_aos_system.md`](01_aos_system.md) y [`docs/02_operational_memory.md`](02_operational_memory.md) |
| Crear un Department Brain | [`docs/03_brain_architecture.md`](03_brain_architecture.md) |
| Ver un ejemplo completo relleno | [`examples/vega/`](../examples/vega/) — agente Vega de Meridian Foods |
| Consultar un término que no entiendes | [`docs/08_glossary.md`](08_glossary.md) |
| Operar el sistema día a día | [`docs/05_operator_manual.md`](05_operator_manual.md) |

---

## Resumen de lo que has creado

```text
✅ Company Brain mínimo (3 entidades, ontología, decisiones)
✅ Agente con Runtime Pack (IDENTITY + SOUL + PERMISSIONS)
✅ Primer Receipt (evidencia de acción)
```

Con esto tienes las tres piezas fundamentales de Company Brain System funcionando. Todo lo demás es profundizar, medir y mejorar.

---

*Siguiente paso recomendado: lee [`docs/00_master_playbook.md`](00_master_playbook.md) para la visión completa del método.*

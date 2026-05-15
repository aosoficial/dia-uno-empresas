# Identidad del Agente

## Ficha de identidad completa

---

## Que es

IDENTITY.md es la ficha de identidad del agente. Define quien es, que tipo de agente es, quien es responsable de el y en que estado se encuentra. Es el primer archivo que se crea y el que identifica al agente de forma unica dentro de la organizacion.

## Cuando usarlo

- Al crear un agente nuevo (primer paso del onboarding).
- Al consultar la lista de agentes activos.
- Al auditar agentes (verificar que todos tienen identidad definida).
- Al desactivar o reactivar un agente.

## Campos obligatorios

| Campo | Descripcion | Ejemplo |
|-------|-------------|---------|
| `nombre` | Nombre unico del agente | Vega |
| `id` | Identificador del sistema | agente/vega |
| `version` | Version actual del pack | 1.0.0 |
| `tipo` | Dominio de operacion | ventas |
| `owner` | Persona responsable del agente | Carlos Ruiz |
| `fecha_creacion` | Cuando se creo | 2026-03-15 |
| `estado` | Estado operativo actual | activo |

---

## Plantilla

```yaml
# --- Identidad del Agente ---

nombre: "[COMPLETAR]"
id: "agente/[COMPLETAR]"
version: "[COMPLETAR]"  # Formato: X.Y.Z (mayor.menor.parche)

tipo: "[COMPLETAR]"
# Tipos comunes: ventas, soporte, operaciones, producto, finanzas, marketing, RRHH

descripcion: >
  [COMPLETAR — Una frase que explique que hace este agente y por que existe.]

owner:
  nombre: "[COMPLETAR]"
  email: "[COMPLETAR]"
  rol: "[COMPLETAR]"  # Rol del owner dentro de la organizacion

fecha_creacion: "[COMPLETAR]"  # Formato: YYYY-MM-DD
fecha_ultima_actualizacion: "[COMPLETAR]"

estado: "[COMPLETAR]"
# Valores posibles:
#   activo         — Operativo con permisos completos
#   en_pruebas     — Operativo con permisos reducidos, en periodo de evaluacion
#   inactivo       — Desactivado temporalmente
#   desactivado    — Retirado definitivamente
#   en_revision    — Pendiente de auditoria o actualizacion

notas: >
  [COMPLETAR — Cualquier informacion relevante sobre el estado actual.
  Dejar vacio si no hay notas.]
```

---

## Ejemplo — Agente Vega (Meridian Foods)

```yaml
nombre: "Vega"
id: "agente/vega"
version: "1.2.0"

tipo: "ventas"

descripcion: >
  Agente de ventas que gestiona el pipeline comercial de Meridian Foods.
  Prepara propuestas, da seguimiento a oportunidades y actualiza el Sales Brain.

owner:
  nombre: "Carlos Ruiz"
  email: "carlos.ruiz@meridianfoods.com"
  rol: "Director Comercial"

fecha_creacion: "2026-03-15"
fecha_ultima_actualizacion: "2026-05-01"

estado: "activo"

notas: >
  Promovido de en_pruebas a activo el 2026-04-01 tras periodo
  de evaluacion de 2 semanas. Permisos completos desde esa fecha.
```

---

## Historial de versiones

Cada vez que se actualiza el Agent Runtime Pack de forma significativa, incrementar la version y registrar el cambio.

```yaml
# --- Historial ---

historial:
  - version: "1.0.0"
    fecha: "[COMPLETAR]"
    cambio: "Creacion inicial del agente"

  - version: "[COMPLETAR]"
    fecha: "[COMPLETAR]"
    cambio: "[COMPLETAR]"
```

### Ejemplo

```yaml
historial:
  - version: "1.0.0"
    fecha: "2026-03-15"
    cambio: "Creacion inicial del agente Vega"

  - version: "1.1.0"
    fecha: "2026-04-01"
    cambio: "Promovido a activo. Permisos de envio de propuestas activados."

  - version: "1.2.0"
    fecha: "2026-05-01"
    cambio: "Anadida integracion con CRM para seguimiento automatico."
```

---

## Errores comunes

1. **No definir un owner.** Un agente sin owner es un agente sin responsable. Si algo falla, nadie sabe quien debe actuar.

2. **Usar nombres genericos.** "Agente de ventas" no es un nombre. El nombre debe ser unico e identificable (Vega, Iris, Atlas).

3. **No actualizar el estado.** Un agente en_pruebas que lleva meses asi probablemente deberia estar activo o desactivado. El estado debe reflejar la realidad.

4. **Version estancada en 1.0.0.** Si el agente ha cambiado permisos, herramientas u operaciones, la version debe reflejarlo. Una version que nunca sube indica que nadie mantiene el pack.

5. **No registrar la fecha de ultima actualizacion.** Impide saber si el pack esta vigente o abandonado.

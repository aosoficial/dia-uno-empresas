# Identidad del Department Brain

## Datos del cerebro

- **Nombre:** [COMPLETAR — ejemplo: Sales Brain]
- **Departamento:** [COMPLETAR — ejemplo: Ventas]
- **Owner:** [COMPLETAR — persona responsable de la salud y veracidad del cerebro]
- **Fecha de creación:** [COMPLETAR — YYYY-MM-DD]
- **Estado:** [activo / en construcción / archivado]
- **Versión:** [COMPLETAR — ejemplo: 1.0]

## Alcance

### Qué cubre este cerebro

[COMPLETAR — describir en 2-3 frases qué área de la organización cubre este cerebro y qué tipo de información gestiona.]

### Qué NO cubre

[COMPLETAR — ser explícito sobre qué queda fuera. Esto evita que el cerebro se convierta en vertedero.]

## Entidades que rastrea

[COMPLETAR — lista de alto nivel. El detalle va en ENTITIES.md.]

- [Entidad 1]
- [Entidad 2]
- [Entidad 3]

## Fuentes de datos

[COMPLETAR — lista de alto nivel. El detalle va en SOURCES.md.]

- [Fuente 1]
- [Fuente 2]
- [Fuente 3]

## Agentes que lo usan

| Agente | Tipo de acceso | Operaciones permitidas |
|--------|---------------|----------------------|
| [COMPLETAR] | lectura | [COMPLETAR] |
| [COMPLETAR] | lectura/escritura | [COMPLETAR] |

## Relación con el Company Brain

- **Lee del Company Brain:** [COMPLETAR — qué datos necesita del Company Brain]
- **Sube al Company Brain:** [COMPLETAR — qué señales o datos aporta]
- **Frecuencia de sincronización:** [COMPLETAR — ejemplo: diaria, semanal, por evento]

## Relación con otros Department Brains

| Department Brain | Relación | Ejemplo |
|-----------------|----------|---------|
| [COMPLETAR] | [lee de / escribe a / recibe señales de] | [COMPLETAR] |

---

## Ejemplo — Sales Brain de Meridian Foods

```yaml
nombre: Sales Brain
departamento: Ventas
owner: Carlos Martín (Director Comercial)
fecha_creación: 2026-05-01
estado: activo
versión: 1.0

alcance:
  cubre: >
    Pipeline comercial, datos de clientes activos y potenciales,
    propuestas enviadas, objeciones frecuentes, compromisos con clientes.
  no_cubre: >
    Datos de producto (eso está en el Product Brain).
    Datos financieros de cobro (eso está en el Finance Brain).
    Operaciones de producción o logística.

entidades:
  - leads
  - clientes activos
  - propuestas
  - objeciones
  - compromisos comerciales

fuentes:
  - CRM
  - emails con clientes
  - reuniones de seguimiento
  - informes de ferias/eventos

agentes:
  - agente: agente/oliva
    acceso: lectura/escritura
    operaciones: consultar pipeline, preparar propuestas, actualizar estados
  - agente: agente/trigo
    acceso: lectura
    operaciones: verificar compromisos de entrega vinculados a ventas

relación_company_brain:
  lee: políticas de descuento, estructura de productos, métricas globales
  sube: cambios en pipeline que afectan MRR, riesgos de churn, necesidades de producto
  frecuencia: diaria (automática) + por evento (señales críticas)

relación_otros_brains:
  - brain: Product Brain
    relación: envía necesidades de producto detectadas por clientes
  - brain: Operations Brain
    relación: consulta stock antes de comprometer fechas de entrega
```

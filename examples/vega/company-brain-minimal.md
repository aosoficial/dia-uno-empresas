# Company Brain — Meridian Foods

## Ejemplo mínimo de Company Brain

---

> **Nota:** este es un ejemplo ficticio con datos inventados. Sirve para ilustrar la estructura de un Company Brain según Company Brain System.

---

## Ontología

| Entidad | Propiedades clave | Freshness |
|---------|-------------------|-----------|
| cliente | nombre, sector, tamaño, contacto principal, estado, valor_anual | semanal |
| producto | nombre, línea, precio, estado | mensual |
| pedido | cliente, productos, fecha, estado, valor | semanal |
| proveedor | nombre, producto_suministrado, condiciones, estado | mensual |
| decisión | descripción, fecha, responsable, vigencia | cuando cambie |

### Relaciones

```text
cliente → compra → producto
producto → usa → receta (interna)
pedido → de → cliente
pedido → contiene → producto
proveedor → suministra → producto
decisión → afecta → producto | cliente | proveedor
```

---

## Hechos fundamentales

- **Nombre:** Meridian Foods S.L.
- **Sector:** Alimentación
- **Tamaño:** 50 empleados
- **Fundación:** 2019
- **Estructura:**
  - Dirección (CEO + COO)
  - Ventas (8 personas + agente Vega)
  - Operaciones (12 personas + agente Trigo)
  - Producto (6 personas)
  - Administración (4 personas)
- **Productos:** 3 líneas
  - Estándar (aceites, conservas)
  - Premium (selección origen único)
  - Gourmet (edición limitada)

---

## Decisiones vigentes

| Decisión | Fecha | Responsable | Vigencia |
|----------|-------|-------------|----------|
| Pedido mínimo: 500 unidades | 2026-04-01 | Clara (CEO) | Hasta revisión Q3 2026 |
| Descuento máximo sin aprobación: 10% | 2026-03-01 | Carlos (Dir. Comercial) | Indefinida |
| No aceptar clientes con deuda >90 días | 2026-01-15 | Clara (CEO) | Indefinida |
| Precio plan Premium: +30% sobre Estándar | 2026-03-01 | Clara (CEO) | Hasta revisión Q3 2026 |

---

## Políticas activas

- Todo email a cliente VIP requiere revisión del Director Comercial antes de enviar.
- Los precios no confirmados por Producto no se incluyen en propuestas.
- Cada propuesta comercial debe verificar stock antes de comprometer fechas de entrega.
- Los datos de contacto de clientes se verifican cada 2 semanas (freshness crítica).

---

## Compromisos activos

| Compromiso | Con quién | Fecha límite | Owner |
|------------|-----------|-------------|-------|
| Propuesta para Costa Frutas | Costa Frutas S.L. | 2026-05-15 | Vega (agente) |
| Integración SAP para Atlas Logistics | Atlas Logistics | 2026-06-30 | Producto |
| Renovación contrato Distribuidora Norte | Distribuidora Norte | 2026-05-31 | Carlos (Dir. Comercial) |

---

## Agentes activos

| Agente | Dominio | Estado | Runtime Pack |
|--------|---------|--------|-------------|
| Vega | Ventas | activo | `examples/vega/agent-runtime-pack/` |
| Trigo | Operaciones | activo | (no incluido en este ejemplo) |

---

## Métricas clave

| Métrica | Objetivo | Frecuencia de revisión |
|---------|----------|----------------------|
| Tiempo de respuesta a clientes | < 4 horas | semanal |
| Propuestas con stock verificado | 100% | semanal |
| Oportunidades sin seguimiento >7 días | 0 | semanal |
| Alertas de stock que evitaron rotura | registrar y contar | mensual |

---

*Este Company Brain es un ejemplo mínimo. Un Company Brain real crecerá con más entidades, más decisiones y más detalle a medida que la organización lo use.*

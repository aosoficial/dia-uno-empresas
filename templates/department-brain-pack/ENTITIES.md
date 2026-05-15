# Catálogo de Entidades

## Qué es esto

Este archivo lista todas las entidades que este Department Brain rastrea. Para cada entidad se definen sus propiedades, relaciones con otras entidades, reglas de freshness y owner.

Una **entidad** es un tipo de cosa que importa para este departamento. No es un registro individual (no es "Cliente Atlas Logistics"), sino un tipo ("cliente").

---

## Entidades

### [COMPLETAR — Nombre de la entidad 1]

- **Descripción:** [COMPLETAR — qué representa esta entidad]
- **Owner:** [COMPLETAR — quién es responsable de que los datos sean correctos]
- **Freshness:** [COMPLETAR — crítica / operativa / estable / histórica]
- **Frecuencia de verificación:** [COMPLETAR — semanal / mensual / trimestral / no caduca]

**Propiedades:**

| Propiedad | Tipo | Obligatoria | Descripción |
|-----------|------|-------------|-------------|
| [COMPLETAR] | [texto / número / fecha / referencia] | [sí / no] | [COMPLETAR] |
| [COMPLETAR] | [texto / número / fecha / referencia] | [sí / no] | [COMPLETAR] |

**Relaciones:**

| Relación | Entidad destino | Cardinalidad | Descripción |
|----------|----------------|--------------|-------------|
| [COMPLETAR] | [COMPLETAR] | [1:1 / 1:N / N:M] | [COMPLETAR] |

---

### [COMPLETAR — Nombre de la entidad 2]

[Repetir la misma estructura para cada entidad]

---

## Reglas de freshness por categoría

| Categoría | Frecuencia de verificación | Ejemplos |
|-----------|---------------------------|----------|
| **Crítica** | Semanal | Precios, compromisos con deadline, stock mínimo |
| **Operativa** | Mensual | Pipeline, métricas de rendimiento, estado de proyectos |
| **Estable** | Trimestral | Políticas internas, estructura del equipo, procesos documentados |
| **Histórica** | No caduca | Decisiones pasadas, reuniones archivadas, lecciones aprendidas |

---

## Ejemplo — Entidades del Sales Brain de Meridian Foods

### Lead

- **Descripción:** Contacto o empresa que ha mostrado interés pero aún no es cliente.
- **Owner:** Carlos Martín (Director Comercial)
- **Freshness:** Operativa
- **Frecuencia de verificación:** Mensual

**Propiedades:**

| Propiedad | Tipo | Obligatoria | Descripción |
|-----------|------|-------------|-------------|
| nombre | texto | sí | Nombre de la empresa o contacto |
| contacto_principal | texto | sí | Persona de referencia |
| email | texto | sí | Email del contacto principal |
| sector | texto | no | Sector de actividad |
| tamaño_empresa | número | no | Número de empleados |
| canal_origen | texto | sí | Cómo llegó el lead (feria, web, referido, etc.) |
| estado | texto | sí | nuevo / contactado / en negociación / descartado |
| fecha_primer_contacto | fecha | sí | Cuándo se estableció el primer contacto |
| notas | texto | no | Observaciones relevantes |

**Relaciones:**

| Relación | Entidad destino | Cardinalidad | Descripción |
|----------|----------------|--------------|-------------|
| genera | propuesta | 1:N | Un lead puede tener varias propuestas |
| se_convierte_en | cliente activo | 1:1 | Si cierra, pasa a ser cliente |

### Cliente activo

- **Descripción:** Empresa o persona que tiene un contrato vigente o pedidos recurrentes.
- **Owner:** Carlos Martín (Director Comercial)
- **Freshness:** Crítica
- **Frecuencia de verificación:** Semanal

**Propiedades:**

| Propiedad | Tipo | Obligatoria | Descripción |
|-----------|------|-------------|-------------|
| nombre | texto | sí | Nombre de la empresa |
| contacto_principal | texto | sí | Persona de referencia |
| volumen_anual | número | sí | Facturación anual estimada en euros |
| productos_contratados | referencia | sí | Productos que compra |
| condiciones_especiales | texto | no | Descuentos, plazos, acuerdos |
| fecha_último_pedido | fecha | sí | Cuándo fue el último pedido |
| riesgo_churn | texto | no | bajo / medio / alto |
| nps | número | no | Puntuación de satisfacción |

**Relaciones:**

| Relación | Entidad destino | Cardinalidad | Descripción |
|----------|----------------|--------------|-------------|
| tiene | propuesta | 1:N | Propuestas enviadas a este cliente |
| compra | producto | N:M | Productos que adquiere |
| genera | compromiso | 1:N | Compromisos asumidos con este cliente |

### Propuesta

- **Descripción:** Documento o oferta formal enviada a un lead o cliente.
- **Owner:** Comercial asignado
- **Freshness:** Crítica
- **Frecuencia de verificación:** Semanal

**Propiedades:**

| Propiedad | Tipo | Obligatoria | Descripción |
|-----------|------|-------------|-------------|
| destinatario | referencia | sí | Lead o cliente al que se envía |
| productos | referencia | sí | Productos incluidos |
| importe_total | número | sí | Valor económico de la propuesta |
| descuento_aplicado | número | no | Porcentaje de descuento |
| estado | texto | sí | borrador / enviada / aceptada / rechazada / expirada |
| fecha_envío | fecha | no | Cuándo se envió |
| fecha_respuesta | fecha | no | Cuándo respondió el destinatario |
| stock_verificado | booleano | sí | Si se verificó stock antes de enviar |

**Relaciones:**

| Relación | Entidad destino | Cardinalidad | Descripción |
|----------|----------------|--------------|-------------|
| pertenece_a | lead / cliente activo | N:1 | A quién va dirigida |
| incluye | producto | N:M | Productos ofertados |

### Compromiso comercial

- **Descripción:** Promesa hecha a un cliente con fecha y condiciones concretas.
- **Owner:** Comercial asignado + Director Comercial
- **Freshness:** Crítica
- **Frecuencia de verificación:** Semanal

**Propiedades:**

| Propiedad | Tipo | Obligatoria | Descripción |
|-----------|------|-------------|-------------|
| cliente | referencia | sí | Cliente al que se hizo la promesa |
| descripción | texto | sí | Qué se prometió |
| fecha_compromiso | fecha | sí | Cuándo se hizo la promesa |
| deadline | fecha | sí | Cuándo se debe cumplir |
| estado | texto | sí | pendiente / cumplido / incumplido / renegociado |
| responsable | texto | sí | Quién debe ejecutarlo |

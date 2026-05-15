# Cuestionario para Department Brain

## Cuándo usar este cuestionario

Antes de crear un Department Brain Pack. Las respuestas alimentan directamente cada archivo del pack (BRAIN_IDENTITY.md, ENTITIES.md, SOURCES.md, SIGNALS.md, SYNC_POLICY.md, METRICS.md).

## Cómo completarlo

1. Responder cada pregunta con datos concretos.
2. Si no puedes responder una pregunta, anota "Por definir" y quién debe resolverla.
3. Todas las secciones son obligatorias salvo que se indique lo contrario.
4. Revisión final por el operador y el owner del departamento.

---

## Sección 1 — Identidad del departamento

### 1.1 ¿Cómo se llama el departamento o área?

> [COMPLETAR]

### 1.2 ¿Quién es el responsable (owner) del departamento?

> [COMPLETAR — nombre y rol]

### 1.3 ¿Cuántas personas trabajan en este departamento?

> [COMPLETAR]

### 1.4 ¿Qué hace este departamento en una frase?

> [COMPLETAR — Ejemplo: "Gestiona el pipeline comercial y cierra ventas con clientes."]

### 1.5 ¿Qué NO hace este departamento? (Límites claros)

> [COMPLETAR — Ejemplo: "No gestiona cobros ni facturación. No decide precios."]

---

## Sección 2 — Entidades

### 2.1 ¿Qué "cosas" gestiona este departamento?

Lista las entidades principales (tipos, no registros individuales):

> 1. [COMPLETAR — Ejemplo: leads]
> 2. [COMPLETAR — Ejemplo: propuestas]
> 3. [COMPLETAR — Ejemplo: compromisos con clientes]
> 4. [COMPLETAR]
> 5. [COMPLETAR]

### 2.2 Para cada entidad, ¿cuáles son las propiedades más importantes?

> [COMPLETAR — Listar 3-5 propiedades por entidad. El detalle completo se define en ENTITIES.md.]

### 2.3 ¿Qué relaciones existen entre las entidades?

> [COMPLETAR — Ejemplo: "Un lead puede generar varias propuestas. Un cliente activo tiene compromisos."]

### 2.4 ¿Hay entidades que comparte con otros departamentos?

> [COMPLETAR — Ejemplo: "Clientes también los gestiona Soporte. Productos los gestiona Producto."]

---

## Sección 3 — Fuentes de datos

### 3.1 ¿De dónde vienen los datos de este departamento?

Para cada fuente:

| Fuente | Qué datos aporta | Frecuencia de actualización | Fiabilidad |
|--------|------------------|---------------------------|------------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [alta / media / baja] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

### 3.2 ¿Hay entidades sin fuente de datos clara?

> [COMPLETAR — Si sí, es un problema de cobertura que debe resolverse.]

### 3.3 ¿Hay fuentes que son personas (datos no registrados en sistemas)?

> [COMPLETAR — Ejemplo: "El director comercial tiene datos de compromisos verbales que no están en el CRM."]

### 3.4 ¿Qué pasa si una fuente deja de funcionar?

> [COMPLETAR — ¿Hay fuentes alternativas? ¿Quién se entera? ¿Cuánto se tarda en detectar?]

---

## Sección 4 — Señales

### 4.1 ¿Qué eventos son señales de oportunidad para este departamento?

> 1. [COMPLETAR — Ejemplo: "Un cliente pide ampliar su contrato."]
> 2. [COMPLETAR]

### 4.2 ¿Qué eventos son señales de riesgo?

> 1. [COMPLETAR — Ejemplo: "Un cliente grande deja de hacer pedidos."]
> 2. [COMPLETAR]
> 3. [COMPLETAR]

### 4.3 ¿Hay umbrales numéricos que, si se cruzan, requieren acción?

> [COMPLETAR — Ejemplo: "Si el pipeline baja de 200.000 euros, hay que activar prospección."]

### 4.4 ¿Hay patrones que, si se repiten, indican algo importante?

> [COMPLETAR — Ejemplo: "Si 3 clientes piden la misma feature, es una señal de producto."]

### 4.5 ¿Quién debe actuar cuando se activa una señal?

> [COMPLETAR — Para cada tipo de señal, quién es el responsable de actuar.]

### 4.6 ¿A quién se escala si la señal no se atiende a tiempo?

> [COMPLETAR]

---

## Sección 5 — Sincronización con el Company Brain

### 5.1 ¿Qué información de este departamento afecta a toda la empresa?

> [COMPLETAR — Ejemplo: "Cambios en pipeline que afectan ingresos proyectados."]

### 5.2 ¿Qué información de este departamento solo es relevante internamente?

> [COMPLETAR — Ejemplo: "Notas de llamadas individuales con leads."]

### 5.3 ¿Qué datos necesita este departamento del Company Brain?

> [COMPLETAR — Ejemplo: "Políticas de descuento, catálogo de productos, estructura del equipo."]

### 5.4 ¿Con qué frecuencia debería sincronizarse con el Company Brain?

> [COMPLETAR — Ejemplo: "Señales críticas inmediatamente. Métricas semanalmente."]

### 5.5 ¿Ha habido casos de información contradictoria entre este departamento y el resto de la empresa?

> [COMPLETAR — Si sí, describir. Esto ayuda a diseñar la política de resolución de conflictos.]

---

## Sección 6 — Agentes

### 6.1 ¿Qué agentes operan actualmente en este departamento?

> [COMPLETAR — Lista de agentes existentes, o "ninguno" si es un departamento nuevo.]

### 6.2 ¿Qué agentes necesitaría este departamento?

> [COMPLETAR — Lista de agentes deseados con función de alto nivel.]

### 6.3 ¿Qué tipo de acceso necesitan los agentes a este cerebro?

> [COMPLETAR — Lectura, lectura/escritura, etc.]

---

## Sección 7 — Métricas del cerebro

### 7.1 ¿Cómo sabremos que este cerebro está sano?

> [COMPLETAR — Al menos 3 métricas. Ejemplo: "Los datos están al día, las señales se detectan, los agentes lo consultan."]

### 7.2 ¿Con qué frecuencia se revisará la salud del cerebro?

> [COMPLETAR — Ejemplo: "Revisión rápida semanal, completa mensual."]

### 7.3 ¿Quién es responsable de la revisión?

> [COMPLETAR]

---

## Resumen de validación

| Sección | Estado |
|---------|--------|
| 1. Identidad del departamento | [ ] Completa |
| 2. Entidades | [ ] Completa |
| 3. Fuentes de datos | [ ] Completa |
| 4. Señales | [ ] Completa |
| 5. Sincronización | [ ] Completa |
| 6. Agentes | [ ] Completa |
| 7. Métricas | [ ] Completa |

**Aprobado por:** [COMPLETAR — operador y owner del departamento]
**Fecha:** [COMPLETAR]
**Siguiente paso:** Crear el Department Brain Pack con las respuestas de este cuestionario.

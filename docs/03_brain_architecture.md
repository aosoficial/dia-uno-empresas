# 03 — Arquitectura de Cerebros

## Cómo se organiza la memoria en niveles

---

## Propósito

Este documento explica cómo se estructuran los "cerebros" (Brains) en Company Brain System: desde el Company Brain central hasta los Department Brains y los Project/Domain Brains. Define qué es cada nivel, qué contiene, cómo se sincronizan y quién es responsable de cada uno.

## Quién lo usa

- **Operadores** que diseñan la estructura de memoria de una organización.
- **Responsables de departamento** que necesitan entender qué sube al Company Brain y qué queda local.
- **Diseñadores de agentes** que necesitan saber a qué cerebros puede acceder cada agente.

## Entradas

- Organigrama de la organización (qué departamentos o áreas existen).
- Ontología definida (ver `01_aos_system.md`).
- Listado de agentes activos y sus dominios.

## Salidas

- Estructura de cerebros definida con ownership claro.
- Reglas de sincronización entre cerebros.
- Tabla de accesos por agente.
- Protocolo de resolución de conflictos entre cerebros.

---

## La jerarquía de cerebros

```text
Company Brain
  Memoria central de la organización.
  Contiene lo que es verdad para TODA la empresa.
      │
      ├── Department Brain: Ventas
      │     Memoria del departamento comercial.
      │     Solo datos relevantes para ventas.
      │
      ├── Department Brain: Producto
      │     Memoria del equipo de producto.
      │     Roadmap, bugs, feedback.
      │
      ├── Department Brain: Operaciones
      │     Procesos, stock, proveedores.
      │
      └── Project/Domain Brain: Proyecto Alpha
            Memoria temporal de un proyecto específico.
            Desaparece o se archiva cuando termina el proyecto.
```

---

## Company Brain

### Qué es

El Company Brain es la memoria central de la organización. Contiene todo lo que es verdad a nivel global: decisiones estratégicas, políticas, estructura del equipo, datos de clientes compartidos, y el estado de los sistemas clave.

### Qué contiene

| Categoría | Ejemplos |
|-----------|----------|
| **Identidad** | Misión, valores, posicionamiento |
| **Estructura** | Organigrama, roles, ownership |
| **Decisiones estratégicas** | Pricing, mercados objetivo, partnerships |
| **Políticas** | Descuentos máximos, SLAs, escalado |
| **Clientes compartidos** | Datos que más de un departamento necesita |
| **Métricas globales** | MRR, churn, NPS |
| **Compromisos externos** | Contratos, fechas límite, condiciones |

### Qué NO contiene

- Detalles operativos de un solo departamento (eso va al Department Brain).
- Conversaciones internas que no cambian el estado global.
- Borradores o trabajo en progreso de un equipo.
- Datos que solo un agente necesita.

### Owner

El operador principal o CEO. Cada hecho en el Company Brain debe tener un owner individual responsable de su veracidad.

### Ejemplo — NovaTech Company Brain

```yaml
company_brain: NovaTech
last_updated: 2026-04-20

identidad:
  misión: "Software de gestión de inventario para pymes"
  mercado: Europa, pymes 10-200 empleados
  posicionamiento: "Simple, integrable, sin consultoría"

estructura:
  ceo: Clara Ruiz
  cto: Pablo Méndez
  head_ventas: Diego Soto
  head_producto: Elena García

decisiones_vigentes:
  - id: dec-2026-001
    decisión: "Precio Plan Pro = 49 €/mes"
    owner: Clara Ruiz
    fecha: 2026-03-01
    razón: Benchmark de mercado Q1
    freshness: vigente

  - id: dec-2026-002
    decisión: "No aceptar clientes con menos de 10 usuarios"
    owner: Clara Ruiz
    fecha: 2026-01-15
    razón: Coste de onboarding no rentable bajo ese umbral
    freshness: vigente

políticas:
  descuento_máximo_sin_aprobación: 15%
  sla_respuesta_soporte: 4 horas
  escalado_urgente: notificar a CTO si afecta a más de 5 clientes
```

---

## Department Brain

### Qué es

Un Department Brain es la memoria operativa de un departamento o área funcional. Contiene datos, señales, riesgos y compromisos específicos de ese departamento.

### Relación con el Company Brain

```text
Department Brain → Company Brain
  ↑ Sube: señales que afectan a toda la empresa.
  ↓ Baja: decisiones y políticas globales que el departamento debe cumplir.

Department Brain ← Company Brain
  ↑ Consulta: datos compartidos (clientes, políticas, métricas globales).
  ↓ No modifica: el Department Brain no puede cambiar datos del Company Brain directamente.
```

**Regla clave:** un Department Brain puede leer del Company Brain, pero solo puede proponer cambios, no hacerlos directamente. Los cambios en el Company Brain requieren aprobación del operador o del owner del dato.

### Qué contiene cada Department Brain

Para cada departamento, la estructura es:

| Sección | Descripción |
|---------|-------------|
| **Entidades propias** | Datos que solo este departamento gestiona |
| **Fuentes** | De dónde vienen los datos del departamento |
| **Señales** | Indicadores tempranos de oportunidad o riesgo |
| **Riesgos** | Problemas potenciales que podrían afectar al departamento o a la empresa |
| **Compromisos** | Promesas hechas a clientes, socios o internamente |
| **Aprobaciones pendientes** | Acciones que esperan visto bueno |
| **Workflows** | Procesos operativos del departamento |
| **Métricas** | KPIs específicos del departamento |
| **Qué sube al Company Brain** | Señales y datos que son relevantes a nivel global |

### Ejemplos de Department Brains

#### Sales Brain

```yaml
department_brain: ventas
owner: Diego Soto

entidades:
  - leads activos
  - pipeline por etapa
  - propuestas enviadas
  - objeciones frecuentes

fuentes:
  - CRM
  - emails con clientes
  - reuniones de seguimiento

señales:
  - Lead que pide integración no existente → sube a Product Brain
  - Competidor baja precios → sube a Company Brain
  - Cliente grande en riesgo de churn → sube a Company Brain

riesgos:
  - Pipeline concentrado en 2 clientes grandes
  - Propuestas enviadas sin verificar stock

compromisos:
  - Atlas Logistics: demo de SAP antes de junio
  - Meridian Foods: respuesta sobre custom reporting esta semana

métricas:
  - pipeline_total: 450.000 €
  - tasa_conversión: 18%
  - tiempo_medio_cierre: 35 días

sube_al_company_brain:
  - Cambios en pipeline que afectan MRR proyectado
  - Nuevas necesidades de producto detectadas por clientes
  - Riesgos de churn en clientes grandes
```

#### Product Brain

```yaml
department_brain: producto
owner: Elena García

entidades:
  - roadmap de features
  - bugs críticos
  - feedback de usuarios
  - integraciones en desarrollo

fuentes:
  - backlog de desarrollo
  - tickets de soporte (vía CS Brain)
  - feedback directo de clientes (vía Sales Brain)
  - analytics de uso

señales:
  - Feature solicitada por >3 clientes → priorizar en roadmap
  - Bug afecta a >5% de usuarios → escalar a CTO
  - Integración retrasada → avisar a Sales Brain

riesgos:
  - Integración SAP con retraso de 2 semanas
  - Deuda técnica en módulo de reporting

compromisos:
  - Integración SAP: ETA junio 2026
  - Fix de bug #1234: esta semana

métricas:
  - features_entregadas_este_trimestre: 4
  - bugs_críticos_abiertos: 2
  - nps_producto: 42

sube_al_company_brain:
  - Retrasos que afectan compromisos con clientes
  - Bugs que afectan a muchos usuarios
  - Cambios en el roadmap que impactan ventas
```

#### Operations Brain

```yaml
department_brain: operaciones
owner: Laura Martínez

entidades:
  - proveedores activos
  - niveles de stock
  - procesos de producción
  - alertas de suministro

fuentes:
  - ERP
  - informes de proveedores
  - sensores de producción

señales:
  - Stock por debajo del mínimo → generar alerta
  - Proveedor con retraso recurrente → evaluar alternativas
  - Coste de producción sube >10% → avisar a finanzas

riesgos:
  - Proveedor principal de aceite de oliva con problemas de suministro
  - Almacén al 90% de capacidad

métricas:
  - rotura_stock_mensual: 2 incidencias
  - tiempo_reposición_medio: 5 días
  - coste_logístico_por_pedido: 3.20 €

sube_al_company_brain:
  - Roturas de stock que afectan entregas a clientes
  - Cambios en costes que afectan márgenes
  - Riesgos de proveedor que requieren decisión estratégica
```

---

## Project/Domain Brain

### Qué es

Un Project Brain es una memoria temporal vinculada a un proyecto concreto. Nace cuando empieza el proyecto y se archiva cuando termina.

Un Domain Brain es una memoria permanente vinculada a un dominio de conocimiento que cruza departamentos (ejemplo: "compliance", "seguridad de datos").

### Cuándo crear uno

- **Project Brain:** cuando un proyecto involucra a más de un departamento o agente y necesita su propia memoria operativa.
- **Domain Brain:** cuando un tema recurrente cruza departamentos y necesita su propia estructura.

### Ejemplo — Project Brain: Lanzamiento Plan Enterprise

```yaml
project_brain: lanzamiento-plan-enterprise
owner: Elena García
departamentos_involucrados: [producto, ventas, marketing]
inicio: 2026-04-01
deadline: 2026-06-30
estado: en curso

decisiones:
  - "Precio: 99 €/mes por usuario"
  - "Incluye integración SAP desde el lanzamiento"
  - "Primeros 10 clientes con 20% descuento"

riesgos:
  - Integración SAP podría no estar lista para la fecha
  - Equipo de marketing necesita materiales 4 semanas antes

compromisos:
  - Demo funcional para el 2026-05-15
  - Materiales de marketing para el 2026-06-01

sube_al_company_brain:
  - Fecha de lanzamiento confirmada
  - Pricing final
  - Cambios que afecten a clientes existentes
```

---

## Sincronización entre cerebros

### Infraestructura posible: almacén, embeddings y capa operativa

La arquitectura puede implementarse con distintas herramientas. Company Brain System distingue tres responsabilidades:

- **Almacén estable:** dónde viven los datos. Ejemplo: Postgres/Supabase para páginas, chunks, links, timeline, receipts, historial y vectores.
- **Modelo de embeddings:** cómo se convierte texto en vectores para búsqueda por significado. Ejemplo: Voyage u otro proveedor equivalente.
- **Capa operativa de memoria:** cómo humanos y agentes usan esa información como memoria accionable. Ejemplo: GBrain como interfaz de páginas, búsqueda, grafo, health, Context Packets y receipts.

La regla es: **el agente no debe depender mentalmente del proveedor técnico**. Debe consultar el Brain mediante el contrato operativo del sistema. Cambiar de almacén o proveedor de embeddings no debe cambiar qué es un StateChange, qué es un Receipt ni qué requiere aprobación.

### Recuperación no es consolidación

Buscar contexto con embeddings no equivale a comprimir memoria.

- **Recuperación:** encontrar los registros relevantes para una tarea.
- **Consolidación:** reemplazar muchos registros por una representación más pequeña.

La recuperación puede ser amplia y reversible. La consolidación debe ser conservadora. Cuando un Department Brain sube información al Company Brain, puede subir una síntesis, pero debe conservar fuentes y evidencia si la señal afecta decisiones, permisos, compromisos o riesgos.

---

### Qué sube al Company Brain

Cada Department Brain es responsable de identificar qué señales deben subir al Company Brain. La regla general:

**Sube si:**
- Afecta a más de un departamento.
- Cambia una métrica global (MRR, churn, NPS).
- Implica un compromiso con un actor externo (cliente, socio, proveedor).
- Representa un riesgo para la empresa, no solo para el departamento.
- Requiere una decisión del operador o CEO.

**No sube si:**
- Es un detalle operativo interno del departamento.
- No afecta a nadie fuera del departamento.
- Es trabajo en progreso sin resultado confirmado.

### Cómo sube

1. El agente o responsable del departamento identifica la señal.
2. Crea un StateChange con la información relevante.
3. Lo etiqueta como `sync: company_brain`.
4. El operador o el owner del dato en el Company Brain revisa y aprueba la incorporación.

### Qué baja del Company Brain

- Decisiones estratégicas que el departamento debe cumplir.
- Políticas nuevas o actualizadas.
- Datos compartidos de clientes que el departamento necesita.
- Métricas globales como referencia.

Los Department Brains consultan estos datos pero no los modifican directamente.

---

## Ownership y responsabilidad

### Reglas de ownership

1. **Cada cerebro tiene un owner global** (persona responsable de la salud del cerebro).
2. **Cada hecho tiene un owner individual** (persona responsable de que ese dato sea correcto).
3. **Un hecho sin owner es un hecho huérfano** — debe asignarse o eliminarse.
4. **El owner de un hecho puede delegar la verificación** pero no la responsabilidad.

### Tabla de ownership — Ejemplo NovaTech

| Cerebro | Owner | Responsabilidad |
|---------|-------|-----------------|
| Company Brain | Clara Ruiz (CEO) | Verdad global de la empresa |
| Sales Brain | Diego Soto | Pipeline, clientes, propuestas |
| Product Brain | Elena García | Roadmap, bugs, integraciones |
| Operations Brain | Laura Martínez | Stock, proveedores, procesos |
| Project: Plan Enterprise | Elena García | Lanzamiento del nuevo plan |

---

## Resolución de conflictos

### Cuándo hay conflicto

Cuando dos cerebros tienen información contradictoria sobre lo mismo.

**Ejemplo:** El Sales Brain dice que el precio del Plan Pro es 49 €/mes. El Product Brain dice que es 45 €/mes porque se discutió una bajada en la última reunión de producto, pero no se aprobó formalmente.

### Protocolo de resolución

1. **Detectar.** Un agente o humano identifica la contradicción.
2. **Escalar.** Se notifica al operador con ambas versiones y sus fuentes.
3. **Verificar.** El operador consulta la fuente de verdad (Company Brain y StateChanges).
4. **Resolver.** El operador decide cuál es la versión correcta.
5. **Actualizar.** Se crea un StateChange corrigiendo el dato incorrecto.
6. **Notificar.** Se avisa a los cerebros afectados.

**Regla general:** en caso de conflicto, el Company Brain gana. Los Department Brains deben alinearse con la verdad global.

---

## Cómo crear un nuevo Department Brain

### Paso 1 — Definir el alcance

```text
Nombre: [nombre del departamento]
Owner: [persona responsable]
Entidades que gestiona: [lista]
Fuentes de datos: [lista]
Agentes que lo usan: [lista]
```

### Paso 2 — Definir qué sube al Company Brain

```text
Señales que suben:
  - [señal 1]: cuándo y por qué
  - [señal 2]: cuándo y por qué
```

### Paso 3 — Definir qué consume del Company Brain

```text
Datos que necesita:
  - [dato 1]: para qué
  - [dato 2]: para qué
```

### Paso 4 — Crear la estructura

Usar la plantilla de Department Brain Pack (ver `templates/department-brain-pack/`).

### Paso 5 — Asignar freshness

Cada entidad y dato tiene su categoría de freshness (ver `02_operational_memory.md`).

### Paso 6 — Activar y medir

Definir métricas del departamento y empezar a registrar StateChanges.

---

## Antipatrones

| Antipatrón | Problema | Solución |
|------------|----------|----------|
| Un solo cerebro para todo | Se vuelve inmanejable rápido | Separar Company Brain y Department Brains |
| Department Brains desconectados | Cada departamento opera en su burbuja | Definir reglas de sincronización explícitas |
| Company Brain como vertedero | Todo sube, nada se filtra | Criterios claros de qué sube y qué no |
| Department Brain sin owner | Nadie es responsable de la veracidad | Siempre asignar owner al crear el cerebro |
| Conflictos no resueltos | Datos contradictorios circulan en paralelo | Protocolo de resolución + Company Brain tiene prioridad |
| Cerebros sin métricas | No sabes si el cerebro está sano | Al menos 3 métricas por cerebro |
| Project Brain que nunca se archiva | Acumula datos obsoletos de proyectos terminados | Archivar al cerrar el proyecto |
| Demasiados cerebros demasiado pronto | Complejidad innecesaria | Empezar con Company Brain + 1-2 Department Brains |

## Checklist de arquitectura de cerebros

- [ ] He definido un Company Brain con identidad, decisiones y políticas.
- [ ] Cada Department Brain tiene owner, entidades, fuentes y métricas.
- [ ] Están definidas las reglas de sincronización (qué sube, qué baja).
- [ ] Cada hecho tiene un owner individual.
- [ ] Existe un protocolo de resolución de conflictos.
- [ ] Cada cerebro tiene categorías de freshness asignadas.
- [ ] Los agentes saben a qué cerebros pueden acceder.
- [ ] Los Project Brains tienen fecha de inicio y criterio de archivo.

---

*Siguiente documento: `04_agent_onboarding.md` — Cómo crear agentes operativos.*

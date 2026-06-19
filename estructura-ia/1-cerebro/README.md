# El Cerebro — memoria operativa del sistema

> El Cerebro es la pieza 1 del organigrama de IA. Hay un **cerebro central** (la memoria de la empresa) y **un cerebro por departamento** (la memoria de ese departamento). Sin cerebro, el resto del sistema no tiene de dónde tirar.

---

## Qué es

El Cerebro es la **memoria operativa estructurada** del sistema. No es un bloc de notas, no es un log de conversaciones y no es un repositorio de documentos. Es el lugar donde viven los hechos verificados, las decisiones vigentes y las trazas de acción que guían el trabajo de humanos y agentes.

**Dos niveles:**

- **Cerebro central** — la memoria de la empresa. Contiene lo que es verdad para toda la organización: identidad, decisiones estratégicas, políticas, métricas globales, compromisos con clientes o socios.
- **Cerebro de departamento** — la memoria de un área funcional (ventas, producto, operaciones, marketing…). Contiene datos, señales y compromisos propios de ese departamento. Un cerebro de departamento también funciona como **copiloto** de ese departamento: se usa de forma interactiva para ejecutar acciones, consultar contexto y tomar decisiones — es la cara human-in-the-loop del cerebro, no una pieza aparte.

**Unidades de la memoria.** Los registros del cerebro no son "notas" ni "neuronas" abstractas. Hay tres primitivas:

| Primitiva | Pregunta que responde | Cuándo se crea |
|---|---|---|
| **StateChange** | ¿Qué cambió, cuándo y por qué? | Cuando cambia un hecho en la memoria, cuando se toma una decisión que afecta al sistema. |
| **Context Packet** | ¿Qué necesita saber este agente para hacer bien esta tarea? | Cuando un humano o agente va a ejecutar una tarea que requiere contexto empaquetado. |
| **Receipt** | ¿Qué hizo el agente y cuál fue el resultado real? | Cuando se completa una acción (incluye resultado observado, no solo confirmación). |

**Tres capas de memoria:**

1. **Factual** — hechos verificados y vigentes (precios, políticas, estructura, compromisos). Cada hecho tiene owner y fecha de verificación.
2. **Interacción** — conversaciones y reuniones que aportan contexto a un hecho o decisión. No se guarda todo: solo lo que explica un por qué o revela un riesgo.
3. **Acción** — Receipts de lo que hicieron agentes y humanos, con resultado observado y correcciones aplicadas.

---

## Cómo se crea

### 1. Definir la ontología inicial

Antes de escribir un solo hecho, responde:

```text
¿Qué entidades existen en este negocio?
  Ejemplos: producto, cliente, proveedor, proyecto, equipo.

¿Qué datos son verdad a nivel global (cerebro central)?
  Ejemplos: precio, política de descuentos, SLA, misión.

¿Qué datos son propios de cada departamento (cerebros de departamento)?
  Ejemplos: pipeline de ventas, roadmap de producto, stock.
```

La ontología no necesita ser perfecta el día uno. Empieza con las entidades que los agentes van a consultar en los próximos 30 días.

### 2. Cargar los hechos iniciales

Para cada hecho que entre en el cerebro:

```yaml
entidad: [tipo/nombre — ejemplo: producto/plan-pro]
campo: [qué dato — ejemplo: precio_mensual]
valor: [el dato actual]
owner: [quién es responsable de que sea correcto]
verificado: [fecha de última verificación — ejemplo: 2026-06-01]
freshness: vigente | stale | archivado
```

**Un hecho sin owner es un hecho huérfano.** Asígnalo o elimínalo. Un hecho sin fecha de verificación es un hecho con riesgo de ser falso.

### 3. Arrancar el cerebro central primero

El cerebro central va primero, siempre. Contiene como mínimo:

- Identidad: misión, mercado, posicionamiento.
- Estructura: organigrama de personas (primero) y de agentes (después).
- Decisiones vigentes con owner, fecha y razón.
- Políticas: descuentos máximos, SLAs, escalados.
- Compromisos externos con actores concretos.

Después, el cerebro del primer departamento que vaya a usar agentes.

### 4. Crear el cerebro de departamento

```text
Nombre del departamento: [ventas / producto / operaciones / …]
Owner del cerebro: [persona responsable]
Entidades que gestiona: [lista]
Fuentes de datos: [CRM, backlog, ERP, reuniones…]
Agentes que lo usan: [agente COO, agente de ventas…]
Qué sube al cerebro central: [señales con criterio explícito]
Qué consume del cerebro central: [políticas, métricas globales, datos compartidos]
```

---

## Cómo funciona

### El flujo de una pieza de memoria

```text
1. Ocurre algo (decisión, acción, señal externa).
2. Se crea el registro correcto:
   — ¿Cambió un hecho? → StateChange
   — ¿Hay que ejecutar una tarea? → Context Packet
   — ¿Se completó una acción? → Receipt
3. El registro queda en el cerebro correspondiente (departamento o central).
4. Si afecta a más de un departamento o a la empresa: el departamento propone
   al cerebro central — no escribe directamente.
5. El operador o el owner del dato aprueba la incorporación al central.
```

### Regla de sincronización: los departamentos suben, proponen, no imponen

Los cerebros de departamento pueden leer del cerebro central. No pueden modificarlo directamente. Cuando una señal debe subir al central:

1. El agente o responsable del departamento identifica la señal.
2. Crea un StateChange etiquetado como `sync: cerebro_central`.
3. El operador o el owner del dato en el central revisa y aprueba.
4. Solo entonces el hecho entra en el central.

**En caso de conflicto entre cerebros:** el central gana. Los cerebros de departamento se alinean con la verdad global.

### Qué sube al cerebro central

**Sube si:**
- Afecta a más de un departamento.
- Cambia una métrica global (ingresos, churn, NPS).
- Implica un compromiso con un actor externo (cliente, socio, proveedor).
- Representa un riesgo para la empresa, no solo para el departamento.
- Requiere una decisión del operador.

**No sube si:**
- Es un detalle operativo interno del departamento.
- Es trabajo en progreso sin resultado confirmado.
- No afecta a nadie fuera del área.

### El cerebro no es el trace store

Las trazas brutas de los agentes (mensajes LLM, outputs de herramientas, logs de depuración) van al **trace store**, no al cerebro. Una traza se convierte en memoria solo si cambia las operaciones futuras: si actualiza un hecho, si produce un StateChange, si genera un Receipt relevante. Si no cambia nada operativo, se queda en trazas con su política de retención.

---

## Cómo se mejora

### Cadencia de revisión

| Frecuencia | Qué se revisa | Tiempo estimado |
|---|---|---|
| **Semanal** | Receipts pendientes de verificación · StateChanges de la semana · Datos stale en categoría crítica | 15 min |
| **Mensual** | Todo lo semanal + datos stale en categoría operativa · Ontología · Propuestas de mejora de método · Sincronización departamento→central | 30 min |
| **Trimestral** | Todo lo mensual + datos stale en categoría estable · Permisos de todos los agentes · Salud de cerebros de departamento | 60 min |

### Categorías de freshness

| Categoría | Revisión | Ejemplos |
|---|---|---|
| **Crítica** | Semanal | Precios, compromisos con clientes, SLAs |
| **Operativa** | Mensual | Políticas, estructura del equipo, permisos de agentes |
| **Estable** | Trimestral | Misión, valores, decisiones estratégicas |
| **Histórica** | No caduca | Decisiones pasadas, historial de StateChanges |

### Consolidar solo lo homogéneo

La memoria no debe crecer sin control, pero tampoco comprimirse a ciegas. Consolidar (reemplazar muchos registros por una representación más pequeña) es seguro cuando:

- varios registros dicen lo mismo con pequeñas variaciones;
- los originales siguen disponibles como evidencia;
- la síntesis tiene owner, fecha, fuentes y freshness.

Es peligroso cuando:
- mezcla decisiones con permisos o aprobaciones;
- elimina Receipts o evidencias;
- junta casos parecidos pero con diferencias operativas importantes.

> Principio: comprimir muchos registros en pocos representantes solo es seguro cuando los registros son semánticamente homogéneos. Si son dispersos, la compresión pierde identidad aunque el algoritmo sea sofisticado. Consolidar es una optimización medida, no el comportamiento por defecto.

### Embeddings para buscar, no para resumir a ciegas

Los vectores de embeddings sirven para **recuperar** los registros relevantes para una tarea. No son un mecanismo de consolidación automática. Buscar con embeddings y comprimir memoria son operaciones distintas con riesgos distintos. Los registros de alta responsabilidad — StateChanges, Receipts, permisos, aprobaciones y evidencias — se conservan como unidades trazables, aunque se busquen por similitud semántica.

### Correcciones que se convierten en mejoras

Cuando el operador corrige un resultado de un agente:
1. La corrección queda en el Receipt.
2. Si el patrón es repetible, se actualiza el cerebro con el aprendizaje.
3. Si afecta a varios agentes o procesos, se activa el loop de mejora del método.

---

## Qué se hace y qué no

### Qué sí hace el cerebro

- Almacena hechos verificados con owner y freshness.
- Registra cambios de estado (StateChange) con razón y fuente.
- Entrega contexto empaquetado a agentes (Context Packet).
- Documenta resultados reales de acciones (Receipt).
- Sincroniza señales relevantes hacia el cerebro central (con aprobación).
- Informa decisiones, aprobaciones y accountability.

### Qué no hace el cerebro

| Qué no | Por qué |
|---|---|
| Guardar todo lo que ocurre | Se convierte en vertedero; nada se encuentra | 
| Recibir escrituras directas de los cerebros de departamento en el central | La sincronización requiere propuesta + aprobación del operador |
| Almacenar trazas brutas de agentes | Las trazas van al trace store con su política de retención |
| Consolidar datos de forma automática | Requiere revisión humana; consolidación ciega pierde identidad |
| Contener hechos sin owner | Un hecho sin owner es un hecho huérfano — asignarlo o eliminarlo |
| Funcionar como fuente de verdad de una interacción del copiloto | Lo decidido en modo copiloto vuelve al cerebro como Receipt/StateChange |

### Checklist mínimo antes de activar el cerebro

- [ ] Ontología inicial definida (entidades y campos principales).
- [ ] Cerebro central creado con identidad, estructura, decisiones y políticas.
- [ ] Cada hecho tiene owner y fecha de verificación.
- [ ] Al menos un cerebro de departamento definido con reglas de sincronización.
- [ ] Categorías de freshness asignadas.
- [ ] Trace store separado (aunque sea una carpeta o tabla distinta).
- [ ] Primer StateChange registrado (evidencia de que el sistema está vivo).

---

*Pieza siguiente: `2-copiloto/` — el cerebro en modo interactivo (human-in-the-loop).*

# 02 — Memoria Operativa

## Cómo el sistema recuerda, rastrea y entrega contexto

---

## Propósito

Este documento explica en detalle cómo funciona la memoria operativa en Company Brain System. Cubre los tres tipos de memoria, las primitivas (StateChange, Context Packet, Receipt), el sistema de permisos, la frescura de datos y cómo se mantiene la memoria saludable.

## Quién lo usa

- **Operadores** que diseñan y mantienen la memoria de su organización.
- **Diseñadores de agentes** que necesitan entender qué información pueden consultar y cómo.
- **Cualquier persona** que necesite depurar por qué un agente tomó una decisión equivocada (la respuesta casi siempre está en la memoria).

## Entradas

- Ontología definida (ver `01_aos_system.md`).
- Hechos, decisiones e interacciones de la organización.
- Acciones de agentes y sus resultados.

## Salidas

- Memoria operativa estructurada y consultable.
- StateChanges que rastrean cada cambio.
- Context Packets listos para entregar a agentes.
- Receipts que documentan cada acción.

---

## Las tres capas de memoria

### Capa 1 — Memoria Factual

Son los hechos verificados y vigentes de la organización.

**Qué incluye:**
- Datos de la empresa (estructura, equipo, productos, clientes).
- Decisiones vigentes con owner, fecha y razón.
- Políticas activas.
- Compromisos con clientes, socios o proveedores.
- Precios, condiciones, SLAs.

**Reglas:**
- Cada hecho tiene un owner (quién es responsable de que sea correcto).
- Cada hecho tiene una fecha de última verificación (freshness).
- Un hecho sin owner es un hecho huérfano: hay que asignarlo o eliminarlo.
- Un hecho sin fecha de verificación es un hecho con riesgo de ser falso.

**Ejemplo — Empresa NovaTech:**
```yaml
entidad: producto/plan-pro
hechos:
  - campo: precio_mensual
    valor: 49
    owner: clara@novatech.com
    verificado: 2026-03-01
    freshness: vigente
  - campo: límite_usuarios
    valor: 25
    owner: pablo@novatech.com
    verificado: 2026-02-15
    freshness: vigente
  - campo: integración_sap
    valor: en desarrollo
    owner: elena@novatech.com
    verificado: 2026-04-10
    freshness: vigente
```

### Capa 2 — Memoria de Interacción

Son las conversaciones, reuniones y comunicaciones que aportan contexto a los hechos.

**Qué incluye:**
- Resúmenes de reuniones relevantes.
- Conversaciones con clientes que revelan necesidades o riesgos.
- Discusiones internas que explican el "por qué" detrás de una decisión.
- Feedback recibido.

**Reglas:**
- No se guarda todo. Se guarda lo que aporta contexto a una decisión o a un hecho.
- Se vincula a la entidad relevante (cliente, producto, proyecto).
- Se indica quién participó y cuándo.

**Ejemplo:**
```yaml
tipo: interacción
fecha: 2026-04-15
participantes: [maría_lópez@atlas.com, agente/vega]
entidad_relacionada: cliente/atlas-logistics
resumen: >
  María confirma que la integración SAP es requisito para cerrar.
  Presupuesto aprobado internamente. Deadline: julio 2026.
  Menciona que LogiSoft ofertó 12.000 €/año.
relevancia: alta — afecta cierre de la oportunidad
```

### Capa 3 — Memoria de Acción

Son los registros de lo que hicieron los agentes y los humanos.

**Qué incluye:**
- Receipts de acciones de agentes.
- Aprobaciones y rechazos del operador.
- Correcciones aplicadas a agentes o a la memoria.
- Resultados observados (no solo "tarea completada").

**Reglas:**
- Cada acción que modifica el estado del sistema debe dejar un Receipt.
- Cada Receipt debe incluir el resultado observado, no solo la confirmación de ejecución.
- Las correcciones humanas deben convertirse en mejoras de la memoria o del agente.
- Las correcciones reutilizables deben evaluarse como mejora del método: si el patrón afecta a varios agentes, plantillas, permisos o rutinas, activar `09_method_improvement_loop.md`.

**Ejemplo:**
```yaml
tipo: acción
agente: agente/vega
acción: Enviar propuesta comercial a Atlas Logistics
timestamp: 2026-04-17T09:00:00Z
inputs: context_packet/atlas_2026-04-16
outputs: propuesta_atlas_v2.pdf enviada a maría_lópez@atlas.com
outcome: >
  Email entregado correctamente.
  María respondió el mismo día pidiendo ajuste en módulo de reporting.
status: éxito_parcial
corrección: >
  El operador pidió incluir capacidades de reporting custom
  en futuras propuestas para clientes de logística.
mejora_aplicada: >
  Actualizado el Sales Brain con nota: "Clientes de logística
  suelen pedir reporting custom. Incluirlo por defecto."
```

---

## Consolidación de memoria: cuándo resumir y cuándo conservar

La memoria operativa no debe crecer sin control, pero tampoco debe comprimirse de forma ciega. En Company Brain System, **consolidar** significa reemplazar muchos registros por una representación más pequeña: un resumen, una síntesis, un centroide semántico, una página agregada o un Context Packet reutilizable.

La consolidación es útil cuando:

- varios registros dicen lo mismo con pequeñas variaciones;
- el operador solo necesita una señal estable, no cada detalle;
- los originales siguen disponibles como evidencia;
- la síntesis tiene owner, fecha, fuentes y freshness.

La consolidación es peligrosa cuando:

- mezcla decisiones con permisos o aprobaciones;
- elimina receipts o evidencias;
- borra quién dijo qué, cuándo y por qué;
- junta casos parecidos pero con diferencias operativas importantes;
- convierte memoria verificable en una frase general sin fuentes.

### Regla práctica

Antes de consolidar, responder:

1. **¿Qué se pierde?** Identidad, detalle, owner, fuente, fecha o evidencia.
2. **¿Sigue existiendo el original?** Si no, no consolidar memoria crítica.
3. **¿El cluster es realmente homogéneo?** Si los casos son dispersos, mantenerlos separados.
4. **¿La síntesis es reversible?** Debe apuntar a sus fuentes.
5. **¿Quién aprueba?** Si afecta decisiones, permisos o acciones futuras, requiere owner u operador.

### Implicación del estudio "The Geometry of Consolidation"

El paper **"The Geometry of Consolidation"** (Vangara y Gopinath, 2026) muestra que, en memorias basadas en embeddings, comprimir muchos elementos en pocos representantes solo es seguro cuando los elementos están cerca entre sí en el espacio semántico. Si están dispersos, la compresión pierde identidad aunque el algoritmo sea sofisticado.

Para Company Brain System, esto se traduce así:

- usar embeddings para buscar no significa que debamos resumirlo todo;
- un centroide o resumen simple puede ser suficiente para clusters muy parecidos;
- los registros de alta responsabilidad —StateChanges, Receipts, permisos, aprobaciones y evidencias— deben conservarse como unidades trazables;
- la consolidación debe ser una optimización medida, no el comportamiento por defecto.

---

## StateChange: el registro de cambios

Un StateChange es la primitiva que responde a la pregunta: **"¿Qué cambió, cuándo y por qué?"**

### Estructura completa

```yaml
id: sc-2026-0301-001
entity: producto/plan-pro
field: precio_mensual
old_value: 39
new_value: 49
changed_by: clara@novatech.com
timestamp: 2026-03-01T10:00:00Z
reason: >
  Alinear con benchmarks de mercado tras análisis Q1.
  Competidores directos cobran entre 45-55 €/mes.
source: reunión de pricing Q1 2026
approved_by: ana@novatech.example
approval_timestamp: 2026-02-28T16:00:00Z
```

### Campos obligatorios vs. opcionales

| Campo | Obligatorio | Descripción |
|-------|------------|-------------|
| `id` | Sí | Identificador único del cambio |
| `entity` | Sí | Qué entidad cambió |
| `field` | Sí | Qué campo específico |
| `old_value` | Sí | Valor anterior |
| `new_value` | Sí | Valor nuevo |
| `changed_by` | Sí | Quién realizó el cambio |
| `timestamp` | Sí | Cuándo |
| `reason` | Sí | Por qué se hizo el cambio |
| `source` | No | De dónde viene la decisión |
| `approved_by` | No | Quién aprobó (si aplica) |
| `approval_timestamp` | No | Cuándo se aprobó |
| `related_entities` | No | Qué otras entidades se ven afectadas |

### Cuándo crear un StateChange

- Cuando cambia un hecho en la Memoria Factual (precio, política, estado de un cliente).
- Cuando se toma una decisión que afecta al sistema.
- Cuando un agente modifica datos de la organización.
- Cuando el operador corrige información incorrecta.

### Cuándo NO crear un StateChange

- Para cada mensaje de chat o interacción trivial — eso va a Memoria de Interacción.
- Para notas internas que no cambian el estado — eso es un comentario.
- Para cada paso interno de un agente — solo el resultado final es StateChange.

---

## Context Packet: contexto empaquetado para actuar

Un Context Packet responde a la pregunta: **"¿Qué necesita saber este agente para hacer bien esta tarea?"**

### Estructura completa

```yaml
id: cp-atlas-2026-04-16
target: agente/vega
task: Preparar propuesta comercial para Atlas Logistics
deadline: 2026-04-18
priority: alta

context:
  cliente:
    nombre: Atlas Logistics
    sector: logística
    empleados: 200
    contacto_principal: María López, directora de operaciones
    email: maría_lópez@atlas.com
    necesidad_clave: integración SAP antes de julio 2026
    presupuesto_estimado: 15.000 €/año
    competidor_activo: LogiSoft, oferta 12.000 €/año
  producto:
    plan_recomendado: Plan Enterprise
    precio_lista: 99 €/mes por usuario
    integración_sap: en desarrollo, ETA junio 2026
  historial:
    - 2026-04-10: primer contacto, demo realizada
    - 2026-04-15: reunión de seguimiento, confirmó presupuesto

constraints:
  - No ofrecer descuento superior al 15% sin aprobación
  - No prometer fecha de integración SAP sin confirmar con producto
  - No mencionar otros clientes por nombre

permissions:
  - Puede generar borrador de propuesta
  - Puede consultar Sales Brain y Product Brain
  - No puede enviar propuesta sin aprobación del operador

freshness: 2026-04-16
sources:
  - Sales Brain: atlas-logistics
  - Product Brain: plan-enterprise
  - Memoria de interacción: reunión 2026-04-15
```

### Principios para crear buenos Context Packets

1. **Solo lo relevante.** No incluir toda la memoria, sino lo que esta tarea necesita.
2. **Incluir restricciones.** Lo que el agente NO debe hacer es tan importante como lo que debe hacer.
3. **Indicar freshness.** El agente debe saber cuán recientes son los datos.
4. **Vincular fuentes.** Si el agente necesita más detalle, debe saber dónde buscar.
5. **Ser específico.** "Prepara una propuesta" es vago. "Prepara propuesta para Atlas, plan Enterprise, con descuento máximo 15%" es accionable.

---

## Receipt: evidencia de acción

Un Receipt responde a la pregunta: **"¿Qué hizo el agente y cuál fue el resultado real?"**

### Estructura completa

```yaml
id: rcp-vega-2026-04-16-001
agent: agente/vega
action: Generar propuesta comercial para Atlas Logistics
timestamp: 2026-04-16T14:30:00Z

inputs:
  context_packet: cp-atlas-2026-04-16
  instrucciones_adicionales: Incluir módulo de reporting estándar

outputs:
  - propuesta_atlas_v2.pdf (borrador, 4 páginas)
  - resumen_ejecutivo.md (3 párrafos)
  - tabla_comparativa_vs_competidor.md

outcome: >
  Borrador generado correctamente. Incluye plan Enterprise
  con descuento del 10%. No se prometió fecha de SAP.
  Pendiente de revisión por operador.

status: pendiente_verificacion

verification:
  reviewed_by: null
  reviewed_at: null
  notes: null

corrections: null
```

### Estados posibles de un Receipt

| Estado | Significado |
|--------|-------------|
| `éxito` | La acción se completó y el resultado observado es correcto |
| `éxito_parcial` | Se completó, pero requiere ajustes o seguimiento |
| `fallo` | La acción no produjo el resultado esperado |
| `pendiente_verificacion` | Completada pero no revisada por el operador |
| `rechazado` | El operador revisó y rechazó el resultado |

### Verificación de Receipts

Un Receipt no verificado es un Receipt en riesgo. El operador debe:

1. Revisar el output del agente.
2. Comparar con lo que se pidió en el Context Packet.
3. Evaluar si el resultado observado es correcto.
4. Marcar como `éxito`, `éxito_parcial`, `fallo` o `rechazado`.
5. Si hay correcciones, registrarlas y decidir si actualizan la memoria o los permisos del agente.
6. Si la corrección es repetible o reutilizable, crear una propuesta de mejora del método con `templates/method-improvements/method-improvement-proposal.md`.

---

## Permisos

Los permisos definen qué puede y qué no puede hacer cada agente.

### Niveles de permiso

```text
Nivel 1 — Autónomo
  El agente puede actuar sin pedir permiso.
  Ejemplo: consultar el Sales Brain, generar borradores internos.

Nivel 2 — Con notificación
  El agente actúa y notifica al operador.
  Ejemplo: actualizar datos de contacto de un cliente.

Nivel 3 — Con aprobación previa
  El agente prepara la acción pero espera aprobación antes de ejecutar.
  Ejemplo: enviar una propuesta comercial, modificar un precio.

Nivel 4 — Prohibido
  El agente nunca puede realizar esta acción.
  Ejemplo: borrar registros de memoria, contactar clientes sin contexto.
```

### Ejemplo de tabla de permisos

| Acción | Agente Vega (ventas) | Agente Iris (soporte) |
|--------|---------------------|----------------------|
| Consultar Sales Brain | Autónomo | Solo lectura |
| Consultar Product Brain | Solo lectura | Autónomo |
| Generar borrador de propuesta | Autónomo | Prohibido |
| Enviar propuesta a cliente | Con aprobación | Prohibido |
| Crear ticket de soporte | Prohibido | Autónomo |
| Escalar ticket a ingeniería | Prohibido | Con notificación |
| Modificar precios | Prohibido | Prohibido |
| Borrar registros de memoria | Prohibido | Prohibido |

---

## Freshness: el reloj de la verdad

Cada dato tiene una fecha de última verificación. Cuanto más tiempo pasa sin verificar, menos fiable es.

### Clasificación de freshness

| Categoría | Frecuencia de revisión | Ejemplos |
|-----------|----------------------|----------|
| **Crítica** | Semanal | Precios, stock, compromisos con clientes, SLAs |
| **Operativa** | Mensual | Políticas, estructura del equipo, permisos de agentes |
| **Estable** | Trimestral | Misión, valores, decisiones estratégicas |
| **Histórica** | No caduca | Decisiones pasadas, historial de cambios |

### Qué pasa con datos stale

Un dato se marca como "stale" (obsoleto) cuando supera su período de revisión sin ser verificado.

**Reglas para datos stale:**
1. No se incluyen en Context Packets sin advertencia explícita.
2. Se listan en el reporte de salud de la memoria.
3. El operador decide: verificar, actualizar o archivar.
4. Un agente que usa datos stale sin advertir está violando el protocolo.

**Ejemplo de advertencia en un Context Packet:**
```yaml
context:
  precio_plan_pro:
    valor: 49
    freshness: 2026-01-15
    warning: "STALE — Último verificado hace 3 meses. Verificar antes de usar en propuesta."
```

---

## Mantenimiento de la memoria

### Revisión semanal (15 minutos)

1. Revisar Receipts pendientes de verificación.
2. Revisar StateChanges de la semana.
3. Identificar datos stale en categoría crítica.
4. Verificar que los agentes no han actuado fuera de permisos.

### Revisión mensual (30 minutos)

1. Todo lo de la semanal +
2. Revisar datos stale en categoría operativa.
3. Evaluar si la ontología necesita ajustes.
4. Revisar métricas del sistema.
5. Aplicar mejoras pendientes.
6. Revisar propuestas de mejora del método: nuevas, aplicadas, aparcadas y pendientes de aprobación.

### Revisión trimestral (1 hora)

1. Todo lo de la mensual +
2. Revisar datos stale en categoría estable.
3. Evaluar si los Department Brains están sincronizados con el Company Brain.
4. Revisar permisos de todos los agentes.
5. Evaluar si el método necesita ajustes.

---

## Ejemplo completo: flujo de memoria

**Situación:** NovaTech detecta que un competidor bajó precios.

```text
1. Agente Vega detecta señal
   → Memoria de Interacción: "Cliente X mencionó que CompetidorY bajó a 35€."

2. Operador verifica
   → Confirma: CompetidorY ahora cobra 35€ en su plan básico.

3. StateChange registrado
   → entity: competidor/competidorY
   → field: precio_plan_basico
   → old_value: 42
   → new_value: 35
   → reason: Bajada de precios confirmada por cliente X y verificada en web pública.

4. Context Packet actualizado para Agente Vega
   → Incluye nuevo dato de competidor.
   → Incluye restricción: "No bajar precios sin análisis de impacto."

5. Agente Vega usa el contexto actualizado en próximas propuestas
   → Receipt de cada propuesta refleja que se tuvo en cuenta el cambio de mercado.

6. Operador decide si ajustar precios
   → Si sí: nuevo StateChange en producto/plan-pro.
   → Si no: registra decisión con razón.
```

---

## Antipatrones

| Antipatrón | Problema | Solución |
|------------|----------|----------|
| Guardar todo en la memoria | Se convierte en vertedero, no se encuentra nada | Solo hechos con owner, fecha y relevancia |
| StateChanges sin `reason` | Nadie sabe por qué cambió algo | Campo `reason` obligatorio |
| Context Packets genéricos | El agente no sabe qué es relevante para su tarea | Context Packet específico por tarea |
| Receipts sin `outcome` | No sabes si el resultado fue bueno | Obligar resultado observado, no solo "completado" |
| No revisar datos stale | Datos obsoletos circulan como actuales | Calendario de freshness con alertas |
| Permisos implícitos | "Se asume que el agente puede" → riesgo | Tabla de permisos explícita por agente y acción |
| Memoria sin mantenimiento | Degrada en semanas | Revisiones semanales de 15 minutos |
| Correcciones sin loop de mejora | El mismo error reaparece en otro agente o sesión | Convertir corrección relevante en propuesta de mejora, cambio aplicado y receipt |

## Checklist de memoria operativa

- [ ] He definido qué hechos van en Memoria Factual con owner y freshness.
- [ ] He definido qué interacciones se guardan y cuáles no.
- [ ] Los StateChanges tienen todos los campos obligatorios.
- [ ] Los Context Packets incluyen contexto, restricciones, permisos y freshness.
- [ ] Los Receipts incluyen resultado observado, no solo confirmación de ejecución.
- [ ] Existe una tabla de permisos explícita para cada agente.
- [ ] Los datos tienen categoría de freshness asignada.
- [ ] Hay un calendario de revisiones (semanal, mensual, trimestral).
- [ ] El operador sabe cómo verificar un Receipt.
- [ ] Las correcciones humanas se convierten en mejoras de la memoria o del agente.
- [ ] Las correcciones reutilizables se elevan al loop de mejora del método.

---

*Siguiente documento: `03_brain_architecture.md` — Cómo se organizan los cerebros.*

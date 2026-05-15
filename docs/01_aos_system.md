# 01 — Company Brain System: Fundamentos

> **Need help applying this?** This page is part of Company Brain System, an open method by Libera. If you get stuck, start with the [Quick Start](07_quick_start.md), use the [Company Brain intake](../templates/questionnaires/company-brain-intake.md), or see [how Libera can help](12_get_help_from_libera.md).

## Agentic Operating System — El método

---

## Propósito

Este documento explica qué es Company Brain System, por qué existe y cuáles son sus conceptos fundamentales. Es la base teórica y práctica sobre la que se construye todo lo demás.

## Quién lo usa

- Cualquier persona que vaya a implementar Company Brain System en una organización.
- Operadores que necesiten entender el "por qué" detrás de cada pieza.
- Diseñadores de sistemas que evalúen si Company Brain System aplica a su caso.

## Entradas

- Una organización que trabaja (o quiere trabajar) con agentes de IA.
- La necesidad de convertir trabajo disperso en memoria operativa compartida.
- Voluntad de definir reglas claras para la acción de los agentes.

## Salidas

- Comprensión completa de los conceptos de Company Brain System.
- Vocabulario compartido entre operadores y agentes.
- Capacidad para decidir si Company Brain System aplica a tu caso y cómo empezar.

---

## Qué problema resuelve

La mayoría de organizaciones que usan agentes de IA tienen estos problemas:

1. **Memoria fragmentada.** Las decisiones están en emails, Slack, documentos sueltos, la cabeza de alguien. Ningún agente puede acceder a todo el contexto.

2. **Agentes sin contrato.** Los agentes operan sin límites claros. A veces hacen demasiado, a veces demasiado poco. No hay forma de saber qué hicieron ni por qué.

3. **Sin evidencia de acción.** Un agente "completó" una tarea, pero ¿el resultado fue correcto? ¿Quién lo verificó? ¿Quedó registro?

4. **Contexto que se pierde.** Cada vez que un agente empieza una tarea, necesita que le re-expliquen todo. No hay memoria operativa compartida.

5. **Sin mejora sistemática.** Los errores se corrigen uno a uno, pero nadie actualiza las reglas, los permisos o la memoria del sistema.

Company Brain System resuelve estos problemas con tres ideas centrales:

- **Memoria operativa estructurada** (no documentos sueltos).
- **Agentes con contrato operativo** (no asistentes genéricos).
- **Todo deja evidencia** (no operaciones en la sombra).

---

## Conceptos fundamentales

### 1. Memoria operativa

La memoria operativa no es un buscador ni un archivo. Es el registro vivo del estado actual de la organización.

Tiene tres capas:

#### Memoria Factual
Hechos verificados sobre la organización: quién es cliente, qué productos hay, qué políticas aplican, qué se decidió y cuándo.

**Ejemplo:** "El precio del plan Pro es 49 €/mes desde el 2026-03-01, decidido por Clara (CEO), razón: alinear con benchmarks del mercado."

#### Memoria de Interacción
Historial de conversaciones, reuniones, intercambios relevantes que aportan contexto a las decisiones.

**Ejemplo:** "En la reunión del 2026-04-15, el cliente Atlas Logistics mencionó que necesita integración con SAP antes de julio."

#### Memoria de Acción
Registro de qué hizo cada agente, cuándo, con qué resultado y qué evidencia dejó.

**Ejemplo:** "Agente Vega envió propuesta a Atlas Logistics el 2026-04-16. Receipt: propuesta_atlas_v2.pdf entregada. Resultado pendiente de respuesta."

### 2. Las tres primitivas operativas

Company Brain System se construye sobre tres primitivas: piezas mínimas que no se pueden dividir más.

#### StateChange (Cambio de estado)

Un StateChange registra que algo cambió en el sistema.

**Campos obligatorios:**
- `entity`: qué entidad cambió (cliente, precio, agente, política…).
- `field`: qué campo específico cambió.
- `old_value`: valor anterior.
- `new_value`: valor nuevo.
- `changed_by`: quién hizo el cambio.
- `timestamp`: cuándo.
- `reason`: por qué.

**Ejemplo:**
```yaml
entity: producto/plan-pro
field: precio_mensual
old_value: 39
new_value: 49
changed_by: clara@novatech.com
timestamp: 2026-03-01T10:00:00Z
reason: Alinear con benchmarks de mercado tras análisis Q1
```

**Por qué importa:** Sin StateChanges, nadie sabe qué cambió. La memoria se convierte en un dato estático que puede estar obsoleto sin que nadie lo sepa.

#### Context Packet (Paquete de contexto)

Un Context Packet es un bloque de información empaquetada para que un agente pueda actuar sin tener que buscar por todo el sistema.

**Campos obligatorios:**
- `target`: para quién es (qué agente o persona).
- `task`: qué tarea debe realizar.
- `context`: información relevante seleccionada.
- `constraints`: qué no debe hacer.
- `permissions`: qué puede hacer.
- `freshness`: cuán reciente es la información incluida.

**Ejemplo:**
```yaml
target: agente/vega
task: Preparar propuesta para Atlas Logistics
context:
  - Atlas Logistics: 200 empleados, sector logística, necesita integración SAP
  - Contacto principal: María López, directora de operaciones
  - Presupuesto estimado: 15.000 €/año
  - Competidor activo: LogiSoft ofertó 12.000 €/año
constraints:
  - No ofrecer descuento superior al 15% sin aprobación
  - No mencionar clientes actuales por nombre
permissions:
  - Puede generar borrador de propuesta
  - Puede consultar el Sales Brain
  - No puede enviar sin aprobación del operador
freshness: 2026-04-16
```

**Por qué importa:** Sin Context Packets, el agente tiene que buscar la información por su cuenta, pierde tiempo, encuentra datos obsoletos o incompletos, y toma peores decisiones.

#### Receipt (Recibo de acción)

Un Receipt es la evidencia de que un agente completó una acción.

**Campos obligatorios:**
- `agent`: qué agente actuó.
- `action`: qué hizo.
- `timestamp`: cuándo.
- `inputs`: qué recibió (referencia al Context Packet o instrucciones).
- `outputs`: qué produjo.
- `outcome`: resultado observado (no solo "completado").
- `status`: éxito / fallo / pendiente de verificación.

**Ejemplo:**
```yaml
agent: agente/vega
action: Generar propuesta comercial para Atlas Logistics
timestamp: 2026-04-16T14:30:00Z
inputs: context_packet/atlas_logistics_2026-04-16
outputs:
  - propuesta_atlas_v2.pdf (borrador)
  - resumen ejecutivo de 3 párrafos
outcome: Borrador generado. Pendiente de revisión por operador.
status: pendiente_verificacion
```

**Por qué importa:** Sin Receipts, no hay forma de saber si un agente hizo bien su trabajo. "Completar" no es lo mismo que "tener éxito".

### 3. Permisos y gobernanza

Cada agente opera dentro de un perímetro definido:

- **Acciones autónomas:** lo que puede hacer sin pedir permiso. Ejemplo: consultar el Sales Brain, generar borradores.
- **Acciones que requieren aprobación:** lo que necesita visto bueno del operador. Ejemplo: enviar una propuesta a un cliente, modificar un precio.
- **Acciones prohibidas:** lo que nunca debe hacer. Ejemplo: borrar registros de memoria, contactar a clientes sin contexto.

Los permisos se definen en el Agent Runtime Pack y se revisan periódicamente.

### 4. Freshness (frescura de la información)

Cada dato en la memoria tiene una fecha de última verificación. Si un dato lleva demasiado tiempo sin actualizarse, se marca como "stale" (obsoleto) y no se incluye en Context Packets sin advertencia.

**Regla práctica:**
- Datos críticos (precios, contactos, compromisos): revisar cada semana.
- Datos estables (políticas, estructura): revisar cada mes.
- Datos estáticos (historia, decisiones pasadas): no caducan, pero deben tener fecha de registro.

### 5. SOUL.md — Nota sobre encabezados en inglés

Las secciones de SOUL.md (Identity, Mission Map, Pushback Rules, Autonomy Boundary, Tools Boundary, etc.) usan encabezados en inglés como **convención del framework**. Esto es una decisión de diseño, no un descuido. Los nombres en inglés funcionan como identificadores estables del contrato operativo, facilitando la interoperabilidad entre implementaciones independientemente del idioma de la documentación. El contenido de cada sección se escribe en español.

### 6. Ontología como lente

Una ontología en Company Brain System es el vocabulario compartido que define qué tipos de cosas existen en el sistema (entidades), qué relaciones tienen entre sí, y qué propiedades importan.

No es un esquema rígido de base de datos. Es una lente que permite a humanos y agentes hablar el mismo idioma sobre la organización.

**Ejemplo para una empresa de software:**
```text
Entidades: cliente, producto, plan, precio, ticket, agente, decisión
Relaciones: cliente → usa → producto; ticket → afecta → producto; agente → gestiona → ticket
Propiedades clave: estado, owner, fecha, freshness
```

---

## Cómo se relacionan las piezas

```text
Ontología
  define qué entidades y relaciones existen
      ↓
Memoria operativa
  almacena hechos, interacciones y acciones
      ↓
StateChanges
  registran cada cambio en la memoria
      ↓
Context Packets
  empaquetan contexto relevante para una tarea
      ↓
Agentes
  reciben Context Packets y actúan dentro de permisos
      ↓
Receipts
  registran qué hizo cada agente y con qué resultado
      ↓
Métricas
  miden la salud del sistema
      ↓
Mejoras
  actualizan memoria, permisos, ontología y método
```

---

## Proceso para aplicar Company Brain System

1. **Definir la ontología inicial.** Qué entidades importan, qué relaciones tienen, qué propiedades rastrear.
2. **Crear el Company Brain.** Registrar los hechos fundamentales de la organización.
3. **Definir Department Brains** si la organización tiene áreas diferenciadas.
4. **Crear agentes con Agent Runtime Packs.** Cada agente necesita identidad, permisos, herramientas y contrato operativo.
5. **Activar el ciclo operativo.** Los agentes actúan, dejan receipts, se registran StateChanges.
6. **Medir.** Definir métricas y revisarlas periódicamente.
7. **Mejorar.** Cada revisión puede actualizar permisos, ontología, memoria o el propio método.

---

## Ejemplo completo: Meridian Foods

**Meridian Foods** es una empresa de alimentación con 50 empleados, 3 líneas de producto y un equipo de ventas de 8 personas.

**Paso 1 — Ontología:**
```text
Entidades: cliente, producto, pedido, precio, proveedor, receta, lote
Relaciones: cliente → compra → producto; producto → usa → receta; lote → viene_de → proveedor
```

**Paso 2 — Company Brain:**
- Misión, valores, estructura del equipo.
- Políticas de pricing: descuento máximo 10% sin aprobación.
- Lista de proveedores activos y condiciones.
- Decisiones vigentes: "No aceptar pedidos de menos de 500 unidades desde Q2 2026."

**Paso 3 — Department Brains:**
- **Sales Brain:** pipeline, contactos clave, objeciones frecuentes.
- **Operations Brain:** stock actual, tiempos de producción, alertas de proveedor.

**Paso 4 — Agentes:**
- **Agente Oliva** (ventas): prepara propuestas, consulta stock antes de comprometer fechas.
- **Agente Trigo** (operaciones): monitoriza stock, alerta si un lote está en riesgo.

**Paso 5 — Ciclo operativo:**
- Oliva recibe un Context Packet con datos del cliente y stock actual.
- Genera propuesta → deja Receipt.
- Trigo detecta stock bajo de aceite de oliva → genera StateChange + alerta al operador.
- Operador aprueba pedido urgente al proveedor → Trigo ejecuta → deja Receipt.

**Paso 6 — Métricas:**
- Tiempo de respuesta a clientes: objetivo < 4 horas.
- Propuestas enviadas con stock verificado: objetivo 100%.
- Alertas de stock que evitaron rotura: registrar y contar.

---

## Antipatrones

| Antipatrón | Problema | Solución |
|------------|----------|----------|
| Empezar por las herramientas, no por el método | Se instalan agentes sin saber qué deben hacer | Definir ontología y Company Brain antes de crear agentes |
| Memoria como vertedero | Todo se guarda, nada se estructura | StateChanges con campos obligatorios, no texto libre |
| Agentes sin permisos definidos | Hacen lo que pueden, no lo que deben | Agent Runtime Pack completo antes de activar |
| Confundir "completado" con "exitoso" | El agente dice que terminó, pero nadie verificó | Receipts con campo `outcome` y revisión del operador |
| No definir freshness | Datos obsoletos circulan como si fueran actuales | Fecha de verificación en cada dato crítico |
| Ontología demasiado ambiciosa | 200 entidades el primer día → parálisis | Empezar con 5-10 entidades, crecer según necesidad |
| No medir | No sabes si el sistema funciona | Definir 3-5 métricas desde el día 1 |

## Checklist de fundamentos

- [ ] Entiendo qué es memoria operativa y sus tres capas (factual, interacción, acción).
- [ ] Entiendo qué es un StateChange y puedo crear uno con todos los campos.
- [ ] Entiendo qué es un Context Packet y por qué un agente lo necesita antes de actuar.
- [ ] Entiendo qué es un Receipt y por qué "completado" no basta.
- [ ] Entiendo la diferencia entre acciones autónomas, con aprobación y prohibidas.
- [ ] Entiendo qué es freshness y por qué importa.
- [ ] Puedo explicar la ontología de mi organización en 5 líneas.
- [ ] Sé cuáles son las 3-5 métricas mínimas de mi sistema.

---

*Siguiente documento: `02_operational_memory.md` — Cómo funciona la memoria operativa en detalle.*

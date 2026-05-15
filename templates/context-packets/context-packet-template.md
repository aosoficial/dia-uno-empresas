# Context Packet (Paquete de Contexto)

## Qué es un Context Packet

Un Context Packet es un bloque de información empaquetada para que un agente pueda actuar sin tener que buscar por todo el sistema. Es la forma en que el sistema "alimenta" al agente con el contexto que necesita para una tarea concreta.

**Principio fundamental:** un agente no debería tener que buscar información por su cuenta. Debe recibirla empaquetada, verificada y con fecha de frescura. Si un agente necesita buscar, el Context Packet fue insuficiente.

## Cuándo crear un Context Packet

- Antes de asignar una tarea a un agente.
- Antes de hacer un handoff de un agente a otro.
- Cuando un agente solicita contexto para actuar.
- Cuando el operador quiere que un agente ejecute una acción concreta.

## Cuándo NO crear un Context Packet

- Para almacenar información general (eso es la memoria del cerebro).
- Para registrar cambios (eso es un StateChange).
- Para documentar acciones (eso es un Receipt).
- Para tareas tan simples que el agente ya tiene toda la información que necesita.

---

## Plantilla

```yaml
# === CONTEXT PACKET ===

id: "[COMPLETAR — identificador único, ejemplo: cp-atlas-logistics-2026-05-08]"

# Para quién es
target: "[COMPLETAR — qué agente o persona recibirá este paquete, ejemplo: agente/oliva]"

# Qué tarea debe realizar
task: "[COMPLETAR — descripción concreta de la tarea, ejemplo: Preparar propuesta comercial para Atlas Logistics]"

# Contexto relevante
context:
  entidad_principal: "[COMPLETAR — la entidad sobre la que se trabaja]"
  datos_relevantes:
    - "[COMPLETAR — dato 1 con fuente y fecha]"
    - "[COMPLETAR — dato 2 con fuente y fecha]"
    - "[COMPLETAR — dato 3 con fuente y fecha]"
  historial_relevante:
    - "[COMPLETAR — interacciones o decisiones pasadas que importan para esta tarea]"
  estado_actual: "[COMPLETAR — situación actual de la entidad o proceso]"

# Restricciones
constraints:
  - "[COMPLETAR — qué NO debe hacer el agente en esta tarea]"
  - "[COMPLETAR — límites específicos para esta tarea]"

# Permisos para esta tarea
permissions:
  autonomo:
    - "[COMPLETAR — acciones que puede hacer sin pedir permiso en esta tarea]"
  requiere_aprobacion:
    - "[COMPLETAR — acciones que necesitan visto bueno del operador]"
  prohibido:
    - "[COMPLETAR — acciones que no puede hacer bajo ninguna circunstancia]"

# Frescura de los datos incluidos
freshness:
  fecha_paquete: "[COMPLETAR — cuándo se generó este Context Packet]"
  datos_mas_antiguos: "[COMPLETAR — fecha del dato más antiguo incluido]"
  advertencias_freshness:
    - "[COMPLETAR — datos que podrían estar desactualizados, con fecha]"

# Resultado esperado
expected_output: "[COMPLETAR — qué se espera que el agente produzca]"

# Plazo
deadline: "[COMPLETAR — cuándo debe completarse la tarea, o null si no hay plazo]"

# Metadata
solicitado_por: "[COMPLETAR — quién solicita esta tarea]"
prioridad: "[COMPLETAR — alta / media / baja]"
cerebros_consultables:
  - "[COMPLETAR — qué cerebros puede consultar el agente para complementar]"
tags:
  - "[COMPLETAR — etiquetas para clasificar]"
```

---

## Campos obligatorios vs. opcionales

| Campo | Obligatorio | Descripción |
|-------|------------|-------------|
| id | Sí | Identificador único |
| target | Sí | Para quién es el paquete |
| task | Sí | Qué tarea debe realizar |
| context | Sí | Información relevante (al menos entidad_principal y datos_relevantes) |
| constraints | Sí | Qué no debe hacer (al menos 1 restricción) |
| permissions | Sí | Qué puede y qué no puede hacer para esta tarea |
| freshness | Sí | Cuándo se generó y cuán recientes son los datos |
| expected_output | Sí | Qué se espera como resultado |
| deadline | No | Solo si hay un plazo concreto |
| solicitado_por | No | Quién pidió la tarea |
| prioridad | No | Nivel de urgencia |
| cerebros_consultables | No | Pero muy recomendado si el agente puede consultar más datos |
| tags | No | Para clasificación |

---

## Principios para buenos Context Packets

1. **Completo pero no excesivo.** Incluir lo que el agente necesita para actuar, no todo lo que existe sobre la entidad. Si incluyes 50 datos y el agente solo necesita 5, el paquete está mal diseñado.

2. **Con fechas siempre.** Cada dato incluido debe tener fecha de última verificación. Un dato sin fecha es un dato de fiabilidad desconocida.

3. **Con restricciones explícitas.** Si hay algo que el agente NO debe hacer en esta tarea, ponerlo. No asumir que "ya lo sabe".

4. **Con resultado esperado claro.** "Preparar propuesta" no es suficiente. "Preparar propuesta con 3 líneas de producto, stock verificado y descuento dentro de política" sí lo es.

5. **Advertir sobre datos stale.** Si un dato incluido tiene más antigüedad de lo habitual, marcarlo. Mejor advertir de más que dejar que el agente use datos obsoletos.

6. **Autosuficiente.** El agente debería poder ejecutar la tarea con solo este paquete y los cerebros que se le permitan consultar. Si necesita preguntar al operador, el paquete estaba incompleto.

---

## Ejemplo completo — Meridian Foods

```yaml
id: "cp-dist-norte-2026-05-08"

target: "agente/oliva"

task: >
  Preparar propuesta comercial para Distribuidora Norte.
  Incluir aceite de oliva premium (500ml) y conservas de tomate orgánico.
  Verificar stock antes de comprometer cantidades.

context:
  entidad_principal: "cliente/distribuidora-norte"
  datos_relevantes:
    - "Distribuidora Norte: cadena regional con 15 puntos de venta en Cataluña (fuente: CRM, verificado 2026-05-01)"
    - "Contacto principal: Marta Vidal, directora de compras (fuente: CRM, verificado 2026-05-01)"
    - "Volumen estimado: 2.000 unidades de aceite premium + 1.500 de conservas (fuente: reunión 2026-05-06)"
    - "Precio unitario aceite premium 500ml: 9.20 euros (fuente: Company Brain, actualizado 2026-05-08)"
    - "Precio unitario conserva tomate orgánico: 3.80 euros (fuente: Company Brain, actualizado 2026-04-15)"
    - "Stock aceite premium: 3.200 unidades disponibles (fuente: Operations Brain, verificado 2026-05-08)"
    - "Stock conservas tomate: 2.100 unidades disponibles (fuente: Operations Brain, verificado 2026-05-08)"
    - "Competidor activo: GreenMarket ofertó a 8.50 euros/unidad aceite (fuente: email de Marta Vidal, 2026-05-03)"
  historial_relevante:
    - "Primera reunión el 2026-04-20. Marta mencionó interés en producto premium y orgánico."
    - "Segundo contacto el 2026-05-06. Confirmó volúmenes estimados y pidió propuesta formal."
  estado_actual: "Lead calificado, pendiente de propuesta formal. Alta probabilidad de cierre si propuesta llega esta semana."

constraints:
  - "No ofrecer descuento superior al 10% sin aprobación de Carlos Martín"
  - "No comprometer fecha de entrega inferior a 10 días laborables sin verificar con Operations Brain"
  - "No mencionar otros clientes por nombre en la propuesta"
  - "No incluir productos que no están en el catálogo vigente"

permissions:
  autonomo:
    - "Generar borrador de propuesta"
    - "Consultar Sales Brain y Operations Brain"
    - "Aplicar descuento hasta 10%"
    - "Calcular precio total y condiciones de pago estándar"
  requiere_aprobacion:
    - "Enviar propuesta al cliente"
    - "Ofrecer descuento superior al 10%"
    - "Comprometer plazo de entrega inferior al estándar"
  prohibido:
    - "Enviar propuesta sin verificar stock"
    - "Modificar precios en el sistema"
    - "Contactar al cliente directamente"

freshness:
  fecha_paquete: "2026-05-08T09:00:00Z"
  datos_mas_antiguos: "2026-04-15 (precio conserva tomate orgánico)"
  advertencias_freshness:
    - "Precio de conserva de tomate verificado hace 23 días. Categoría operativa (mensual), dentro de plazo pero cerca del límite. Verificar si hubo cambios recientes."

expected_output: >
  Borrador de propuesta en PDF con:
  - Datos del cliente y contacto principal
  - Tabla de productos con cantidades, precios unitarios y subtotales
  - Descuento aplicado (si procede) con justificación
  - Condiciones de pago estándar
  - Plazo de entrega estimado (verificado con stock actual)
  - Total de la propuesta
  Además: nota interna con resumen ejecutivo para Carlos Martín.

deadline: "2026-05-09T12:00:00Z"

solicitado_por: "Carlos Martín (Director Comercial)"
prioridad: "alta"
cerebros_consultables:
  - "Sales Brain (lectura)"
  - "Operations Brain (solo stock, lectura)"
  - "Company Brain (precios y políticas, lectura)"
tags:
  - ventas
  - propuesta
  - distribuidora-norte
  - aceite-premium
  - conservas
```

---

## Errores comunes

| Error | Consecuencia | Cómo evitarlo |
|-------|-------------|---------------|
| No incluir restricciones | El agente hace algo que no debía | Siempre incluir al menos 1 restricción |
| Datos sin fecha | No se sabe si la información es actual | Cada dato debe tener fecha de verificación |
| Resultado esperado vago | El agente interpreta a su manera | Describir el output con detalle concreto |
| Demasiada información | El agente se confunde o usa datos irrelevantes | Solo incluir lo necesario para la tarea |
| No advertir sobre datos stale | El agente usa datos obsoletos con confianza | Marcar datos cerca de su límite de freshness |
| No indicar qué cerebros puede consultar | El agente no sabe si puede buscar más datos | Listar los cerebros consultables explícitamente |

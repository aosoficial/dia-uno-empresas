# Context Packet

## Paquete de contexto que recibe el agente para actuar

---

## Que es

Un Context Packet es un paquete de informacion estructurada que contiene todo lo que el agente necesita para ejecutar una tarea. Responde a la pregunta: "Que necesita saber este agente para hacer bien esta tarea?"

CONTEXT_PACKET.md define la estructura que deben seguir los Context Packets que recibe este agente, los campos obligatorios, y un ejemplo de referencia.

**Un Context Packet mal construido produce acciones incorrectas.** Si al agente le falta contexto, inventa. Si le sobra, pierde foco.

## Cuando usarlo

- Al enviar una tarea al agente (construir el Context Packet segun esta plantilla).
- Al diagnosticar por que el agente tomo una decision incorrecta (revisar el Context Packet que recibio).
- Al disenar nuevas operaciones del agente (definir que contexto necesita).

## Campos obligatorios

| Campo | Descripcion |
|-------|-------------|
| `id` | Identificador unico del Context Packet |
| `target` | Que agente debe recibir este paquete |
| `task` | Que tarea debe realizar |
| `deadline` | Cuando debe estar completada |
| `priority` | Nivel de prioridad |
| `context` | Datos relevantes para la tarea |
| `constraints` | Restricciones y lo que NO debe hacer |
| `permissions` | Que puede hacer dentro de esta tarea |
| `freshness` | Fecha de los datos incluidos |
| `sources` | De donde vienen los datos |

---

## Plantilla

```yaml
# --- Context Packet ---

id: "cp-[COMPLETAR]-[FECHA]"
target: "agente/[COMPLETAR]"
task: "[COMPLETAR — Que tarea concreta debe realizar]"
deadline: "[COMPLETAR]"  # Formato: YYYY-MM-DD o YYYY-MM-DDTHH:MM:SSZ
priority: "[COMPLETAR]"  # critica / alta / media / baja

context:
  # Datos relevantes para la tarea.
  # Estructura segun el tipo de tarea.

  entidad_principal:
    nombre: "[COMPLETAR]"
    tipo: "[COMPLETAR]"  # cliente / producto / proyecto / otro
    datos_clave:
      - campo: "[COMPLETAR]"
        valor: "[COMPLETAR]"
      - campo: "[COMPLETAR]"
        valor: "[COMPLETAR]"

  historial_relevante:
    - fecha: "[COMPLETAR]"
      evento: "[COMPLETAR]"
    - fecha: "[COMPLETAR]"
      evento: "[COMPLETAR]"

  datos_adicionales:
    # [COMPLETAR — Cualquier otro dato necesario para la tarea]

constraints:
  - "[COMPLETAR — Restriccion 1: lo que el agente NO debe hacer]"
  - "[COMPLETAR — Restriccion 2]"
  - "[COMPLETAR — Restriccion 3]"

permissions:
  - "[COMPLETAR — Permiso especifico para esta tarea]"
  - "[COMPLETAR]"

freshness: "[COMPLETAR]"  # Fecha de recopilacion de los datos
warnings:
  - "[COMPLETAR — Ej: dato X no verificado desde hace 2 meses]"

sources:
  - "[COMPLETAR — De donde vienen los datos. Ej: Sales Brain, Product Brain]"
  - "[COMPLETAR]"
```

---

## Ejemplo — Context Packet para Vega (Meridian Foods)

```yaml
id: "cp-costafrutas-2026-05-05"
target: "agente/vega"
task: "Preparar propuesta comercial para Costa Frutas"
deadline: "2026-05-08"
priority: "alta"

context:
  entidad_principal:
    nombre: "Costa Frutas S.L."
    tipo: "cliente"
    datos_clave:
      - campo: "sector"
        valor: "distribucion de alimentos frescos"
      - campo: "empleados"
        valor: 150
      - campo: "contacto_principal"
        valor: "Ana Gomez, directora de compras"
      - campo: "email"
        valor: "ana.gomez@costafrutas.com"
      - campo: "necesidad_clave"
        valor: "Plataforma de gestion de pedidos con integracion a su ERP"
      - campo: "presupuesto_estimado"
        valor: "18.000 EUR/ano"
      - campo: "competidor_activo"
        valor: "FreshTrack, ofertaron 14.000 EUR/ano"

  historial_relevante:
    - fecha: "2026-04-20"
      evento: "Primer contacto en evento FoodTech 2026. Demo realizada."
    - fecha: "2026-04-28"
      evento: "Reunion de seguimiento. Confirmo presupuesto y timeline."
    - fecha: "2026-05-02"
      evento: "Ana solicito propuesta formal con descuento por volumen."

  producto_recomendado:
    plan: "Plan Business"
    precio_lista: "12.000 EUR/ano"
    integracion_erp: "disponible (modulo estandar)"
    modulo_pedidos: "incluido en Plan Business"

  datos_adicionales:
    patron_detectado: >
      Costa Frutas es similar a 3 clientes actuales del sector
      distribucion. Todos valoran la integracion ERP y el modulo
      de pedidos en tiempo real.

constraints:
  - "No ofrecer descuento superior al 15% sin aprobacion."
  - "No prometer integracion custom sin confirmar con producto (agente Nova)."
  - "No mencionar otros clientes por nombre."
  - "No prometer plazos de implementacion sin verificar capacidad."

permissions:
  - "Puede generar borrador de propuesta."
  - "Puede consultar Sales Brain y Product Brain."
  - "No puede enviar propuesta sin aprobacion del operador."

freshness: "2026-05-05"
warnings:
  - "Precio de Plan Business verificado el 2026-04-01. Verificar si hubo cambios en mayo."

sources:
  - "Sales Brain: cliente/costa-frutas"
  - "Product Brain: producto/plan-business"
  - "Memoria de interaccion: reuniones 2026-04-20, 2026-04-28, 2026-05-02"
```

---

## Principios para buenos Context Packets

1. **Solo lo relevante.** No incluir toda la memoria, solo lo que esta tarea necesita. Un Context Packet sobrecargado distrae al agente.

2. **Incluir restricciones siempre.** Lo que el agente NO debe hacer es tan importante como lo que debe hacer.

3. **Indicar freshness.** El agente debe saber cuan recientes son los datos. Si un dato es stale, marcarlo con warning.

4. **Vincular fuentes.** Si el agente necesita mas detalle, debe saber donde buscar sin tener que adivinar.

5. **Ser especifico.** "Prepara una propuesta" es vago. "Prepara propuesta para Costa Frutas, Plan Business, con descuento maximo 15%, deadline 8 de mayo" es accionable.

---

## Errores comunes

1. **Context Packet sin restricciones.** Sin constraints, el agente asume que puede hacer todo. Esto lleva a acciones fuera de limite.

2. **Datos sin freshness.** El agente usa un precio de hace 3 meses como si fuera vigente. Siempre indicar la fecha de los datos.

3. **Demasiado contexto.** Si incluyes 50 datos para una tarea que necesita 5, el agente pierde foco. Filtrar es responsabilidad del creador del Context Packet.

4. **Sin deadline.** Sin fecha limite, la tarea no tiene urgencia y el agente puede postergarla indefinidamente.

5. **Sin fuentes.** Si el agente tiene una duda sobre un dato del Context Packet, necesita saber donde verificarlo. Sin fuentes, no puede verificar nada.

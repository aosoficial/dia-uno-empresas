# El Copiloto

> **El copiloto no es una pieza aparte del cerebro: es el cerebro en modo interactivo.**
> Cuando abres Claude y le preguntas algo sobre marketing, estás usando el cerebro de marketing como copiloto de marketing.

---

## Qué es

El copiloto es la cara **human-in-the-loop** del cerebro de departamento.

Cada cerebro —de marketing, de ventas, de tecnología, de dirección— es al mismo tiempo un copiloto de ese departamento. No son dos piezas distintas. La diferencia está en el modo de uso:

- El **cerebro** es la memoria: acumula StateChanges, Receipts y Context Packets.
- El **copiloto** es ese mismo cerebro cuando lo usas de forma interactiva para **consultar, pedir acciones y tomar decisiones**.

Dicho de otra forma: el cerebro de ventas almacena todo lo que ha pasado en ventas. El copiloto de ventas es lo que te responde cuando le preguntas «¿qué propuesta mandamos a este cliente?» o «redacta el seguimiento de la reunión de ayer».

Ejemplos concretos:
- **Claude** (en Claude.ai o Claude Code) actuando como copiloto de dirección, ventas o producto.
- **Codex** (en ORGO) actuando como copiloto técnico o instalador del sistema.

---

## Cómo se crea

El copiloto existe desde el momento en que el cerebro existe. No requiere instalación adicional.

Lo que sí requiere es **cargarle contexto**:

1. El cerebro tiene que estar alimentado con los StateChanges y Receipts del departamento.
2. Cuando abres una conversación con el copiloto, le pasas el **Context Packet** del departamento: el estado actual, las prioridades, las decisiones vigentes.
3. El copiloto responde y actúa sobre esa base, no sobre suposiciones.

Sin Context Packet, el copiloto improvisa. Con Context Packet, el copiloto ejecuta.

---

## Cómo funciona

El copiloto opera en tres modos dentro de una conversación:

### Consultar
Le preguntas algo. Te responde basándose en lo que el cerebro sabe.

```
«¿Cuál es el pipeline actual de ventas?»
«¿Qué decidimos sobre el precio del producto B?»
«Resume los últimos tres Receipts de marketing.»
```

### Pedir que haga
Le encargas una tarea acotada. El copiloto ejecuta y te entrega un borrador, un análisis o un documento.

```
«Redacta el email de seguimiento para la propuesta de ayer.»
«Prepara el resumen semanal de métricas para el equipo.»
«Crea el Context Packet para el agente CMO antes de la reunión.»
```

### Decidir juntos — el patrón 1:3:1

Para decisiones no triviales, el copiloto no elige por ti. Usa el formato **1:3:1**:

```
Problema:
[1 frase clara que describe la decisión]

Opciones:
A) [opción conservadora]
B) [opción equilibrada]
C) [opción más agresiva o exploratoria]

Recomendación:
Yo haría [A/B/C] porque [razón práctica en una frase].

Necesito tu OK para:
[acción concreta que ejecutaré si apruebas]
```

El 1:3:1 no es opcional cuando la acción es externa, pública, económica, legal, irreversible o toca producción o datos sensibles.

El patrón tiene dos efectos:
- **Para ti:** reduces la carga cognitiva. Ves el problema enmarcado, las opciones comparadas y una recomendación razonada. Solo necesitas decir sí, elegir otra opción o redirigir.
- **Para el sistema:** cada respuesta tuya es una señal de madurez que mejora el criterio del copiloto con el tiempo.

---

## Cómo se mejora

El copiloto mejora en dos vías:

**1. Mejor contexto de entrada.**
Cuanto más completo y actualizado esté el cerebro, mejores respuestas da el copiloto. Si el copiloto improvisa demasiado, el problema suele ser un cerebro desactualizado, no el copiloto en sí.

**2. Feedback sistemático en el 1:3:1.**
Cada vez que el copiloto propone y tú corriges, aceptas o rechazas, esa señal debe registrarse:
- Aceptaste la recomendación → el patrón funciona, se reutiliza.
- Elegiste otra opción → el criterio de priorización necesita ajuste.
- Rechazaste todas → el copiloto no entendió el problema; revisar el Context Packet y el framing.
- Pediste aclaraciones antes de decidir → la explicación no fue suficiente; mejorar brevedad y concreción.

Estas señales no quedan en el aire: vuelven al cerebro como entradas de mejora y, si se repiten, actualizan el protocolo o el prompt del copiloto.

---

## Qué se hace y qué no

### Lo que el copiloto SÍ hace

- Responder preguntas sobre el estado del departamento basándose en el contexto cargado.
- Redactar borradores, resúmenes, emails, análisis y Context Packets.
- Proponer opciones estructuradas con el formato 1:3:1 antes de actuar.
- Preparar Receipts al terminar una tarea significativa.
- Escalar antes de cualquier acción externa, económica, pública o irreversible.

### Lo que el copiloto NO hace

- **No es fuente de verdad por sí mismo.** Lo que se decide con el copiloto no existe en el sistema hasta que vuelve al cerebro como Receipt o StateChange. Si la conversación termina sin guardar nada, la decisión no está registrada.
- **No actúa sin aprobación en acciones sensibles.** El 1:3:1 existe precisamente para esto.
- **No reemplaza al agente.** El copiloto es interactivo; el agente es autónomo. No pidas al copiloto que «se encargue de todo» de forma desatendida: para eso existe el agente.
- **No improvisa contexto.** Si no tiene Context Packet, debe pedirlo o decir explícitamente qué no sabe.

### La regla de cierre del loop

Todo lo que decidas con el copiloto debe cerrarse con un Receipt o StateChange guardado en el cerebro. Sin ese paso, la conversación fue útil pero no dejó huella operativa. El copiloto ayuda a decidir y ejecutar; el cerebro es quien recuerda.

---

*Siguiente: `3-agentes/README.md` — el agente: trabajador autónomo con identidad, permisos y ciclo de mejora.*

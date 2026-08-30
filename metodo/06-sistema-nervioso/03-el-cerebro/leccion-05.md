---
slug: implementacion-por-capas
titulo: "Implementación por capas"
resumen: "El cerebro no tiene versión manual: enciende como captura en la segunda capa y pasa a servir conocimiento a los agentes en la tercera."
orden: 5
---
El sistema de este método es fijo, pero se instala por capas: un mínimo que ya rueda (Capa 1), la densidad después (Capa 2), la agentización al final (Capa 3). El cerebro es la única herramienta con dos momentos de encendido en vez de uno, y también la única que no tiene una versión útil en la primera capa. Está diseñado para ser servido por IA, y hacerlo a mano es puro coste.

## Capa 1 · el mínimo

No se instala. Esa es la respuesta completa, y conviene resistir la tentación de forzar una versión manual: pedirle a alguien que resuma reuniones a mano para llenar una carpeta es trabajo que nadie sostiene tres semanas, y lo que queda no es una memoria, es un cementerio de actas.

Lo único que ocurre en la Capa 1 es que los cambios de estado de las demás herramientas se van acumulando solos como rastro del sistema. Pero ese rastro no es un cerebro instalado deliberadamente, y no hay que confundir una cosa con la otra.

## Capa 2 · la densidad

El primer encendido es la captura, y ocurre cuando ya existen dos cosas: una cadencia estable de reuniones que produce transcripciones, y una SOP de conocimiento que define qué hay que sacar de cada tipo de conversación. Con esas dos, la IA lee cada transcripción, extrae los hechos, las decisiones y lo que hay que recordar, y lo almacena ligado a su cliente, su tema o su decisión.

Hasta aquí el cerebro guarda. Ya es mucho: la empresa deja de perder lo que sabe cada vez que alguien se marcha o cada vez que pasan tres meses.

## Capa 3 · el agente

El segundo encendido es el consumo. Tiene nombre técnico —RAG, o recuperación aumentada— pero la idea es simple: el agente, antes de responder o de actuar, va a buscar al cerebro lo que la empresa sabe del asunto, y trabaja sobre esos hechos en vez de sobre suposiciones. Es lo que le da memoria de cada cliente. Sin este paso, el cerebro es un archivo bien ordenado; con él, es la infraestructura que vuelve útiles a los agentes.

## El punto de corte

Hay dos bisagras, no una. La primera: cadencia estable más SOP de conocimiento, y nace la captura. La segunda: existen agentes que lo consulten, y nace el consumo. Y una regla que las acompaña: no forzar una versión manual para adelantar la primera. Si la cadencia y la SOP no están, el cerebro no se instala mal — sencillamente no se instala todavía, y no pasa nada, porque las herramientas de la Capa 1 no lo necesitan para funcionar.

## Qué conexiones se encienden cuándo

Ninguna en la Capa 1, porque la herramienta no está. En la Capa 2 se encienden las dos que lo alimentan: la cadencia, de donde salen las transcripciones, y el aprendizaje continuo, que le entrega cada lección con su porqué. En la Capa 3 se enciende la que lo hace valer de verdad: del cerebro hacia los agentes.

## Comprobación

Queréis empezar ya con el cerebro, pero aún no tenéis una cadencia estable de reuniones ni una SOP que diga qué cosechar. Alguien propone que cada responsable resuma sus reuniones a mano en una carpeta compartida mientras tanto. ¿Qué dice el método?

- [ ] Adelante: es una versión manual del cerebro y algo se avanza mientras llega lo demás
- [x] No: el cerebro no tiene versión útil en la Capa 1, y esos resúmenes acaban en una carpeta que nadie relee; primero la cadencia y la SOP de conocimiento
- [ ] Adelante, pero grabándolo todo sin resumir, para no perder nada hasta que llegue la IA

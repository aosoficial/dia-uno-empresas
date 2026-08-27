---
slug: la-sop-agentizable
titulo: "La SOP agentizable"
resumen: "Qué convierte una buena SOP en un procedimiento que también puede ejecutar un agente de inteligencia artificial, con sus guardarraíles."
orden: 4
---
Aquí está lo que separa una SOP de DÍA UNO de una SOP normal. Una SOP bien escrita para un humano ya está a medio camino de poder ser ejecutada por un agente de inteligencia artificial; la diferencia es el grado de explicitud. Un humano rellena los huecos con su criterio; un agente necesita que esos huecos estén escritos.

## No es otro documento: es la versión disciplinada

Hacer una SOP «agentizable» no es escribir un documento distinto: es escribir la versión disciplinada de la misma plantilla. Y lo que la vuelve ejecutable por una máquina, además, la hace mejor para las personas:

- **Disparadores discretos y explícitos**: condiciones concretas que inician cada paso, no «cuando toque».
- **Entradas con su fuente**: cada dato que se necesita, y de dónde se saca exactamente.
- **Pasos inequívocos, con obligatoriedad calibrada**: palabras que marcan qué es obligatorio, qué recomendable y qué opcional, para que no haya duda sobre qué se puede saltar.
- **Reglas de decisión tipadas**: bifurcaciones ancladas a hechos observables y mutuamente excluyentes («si el estado es enviado…»), no a juicios vagos.
- **Parámetros en vez de valores fijos**: la misma SOP sirve para muchos casos cambiando sus parámetros — el equivalente de máquina de «referenciar, no fijar».
- **Guardarraíles**: qué acciones exigen una comprobación, y cuándo el agente NO debe actuar solo y tiene que escalar a una persona.
- **Salidas, criterio de éxito y trazabilidad**: qué hay que producir, cómo se sabe que salió bien, y un registro de lo hecho para poder retomar si algo se rompe.

## Determinístico a medias

El equilibrio que se busca es lo que en el mundo de los agentes se llama, medio en broma, «determinístico a medias»: estructurado lo suficiente para garantizar un resultado consistente, pero flexible para que el agente use su criterio en los pocos puntos donde ayuda. Demasiado rígido y es un guion frágil; demasiado vago y el comportamiento es impredecible. Una SOP de DÍA UNO se escribe pensando en ese punto medio.

## Cómo trabaja el agente

La SOP es, de todas las herramientas de DÍA UNO, la que más directamente se agentiza — porque una SOP bien hecha es, literalmente, un programa escrito en lenguaje natural. Cuando está Operativa, un agente puede asumir su parte reglada: dispararse con la condición definida, recoger las entradas de donde la SOP dice que están, ejecutar los pasos inequívocos, aplicar las reglas de decisión, producir las salidas y avisar a quien toca, dejando registro de lo que hizo.

Y — esto es lo importante — escalando a una persona en los puntos donde la propia SOP marca que hace falta criterio humano. El agente no inventa el proceso; recorre el que la empresa escribió, dentro de las vallas que la empresa puso. Por eso escribir buenas SOPs no es solo ordenar el presente: es construir, ladrillo a ladrillo, la empresa que una capa de agentes podrá sostener.

## Comprobación

Un agente está ejecutando una SOP y llega a un punto donde la propia SOP marca que hace falta criterio humano. ¿Qué debe hacer?

- [ ] Decidir con su mejor juicio, para no detener el flujo del proceso
- [x] Escalar a la persona que la SOP indica y dejar registro de lo hecho hasta ahí
- [ ] Saltarse ese paso y continuar con el resto del procedimiento

# Research receipt — separación humano-agente

Fecha: `2026-08-12`
Pregunta: **¿qué separación evita que una plantilla humano-agente se convierta en dos sistemas desconectados o en una cadena de aprobaciones vacía?**

## Fuentes revisadas

1. [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/): gobernanza transversal, roles y responsabilidades claros, responsabilidad de liderazgo y diferenciación explícita de configuraciones humano-IA.
2. [OpenAI Agents SDK — Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/): gates ligados a tool calls concretas, estado durable para pausar/reanudar y decisiones acotadas por llamada.
3. [LangGraph — Human-in-the-loop](https://github.com/langchain-ai/langgraphjs/blob/main/docs/docs/agents/human-in-the-loop.md): persistencia del estado antes de la revisión humana y reanudación del mismo workflow.
4. [Discusión práctica en r/AI_Agents](https://www.reddit.com/r/AI_Agents/comments/1upjbei/human_approval_is_too_vague_for_production_agents/): señal anecdótica sobre fatiga de aprobación, diferencia entre reversible e irreversible y necesidad de que un rechazo tenga transición propia.

## Patrones que cambiaron o confirmaron el diseño

- **Un solo objeto de trabajo:** la función y sus fuentes humanas son canónicas; el agente recibe un contrato ejecutable enlazado, no una copia paralela.
- **Responsabilidad nombrada:** cada función conserva un responsable humano aunque cambie el ejecutor.
- **Autoridad por acción:** el permiso o la aprobación se refiere a una acción concreta y sus parámetros, no a una intención general.
- **Estado y evidencia durables:** pausa, revisión, resultado y cambio de estado deben poder reconstruirse.
- **Supervisión proporcional:** los límites dependen del riesgo y reversibilidad; pedir aprobación para todo crea ruido y no sustituye permisos mínimos.
- **Rechazo como estado:** un `no` bloquea, degrada o deriva la acción; no autoriza reintentos semánticamente equivalentes.

## Límites de la investigación

- NIST define resultados de gobierno, no una arquitectura de carpetas ni un instalador.
- Los SDK demuestran patrones técnicos de aprobación y reanudación; no diseñan el modelo organizativo de una empresa.
- Reddit se usa como señal práctica, no como prueba normativa ni técnica.
- La decisión de DIA UNO sigue siendo propia: **Personas organiza; Agentes ejecuta capacidades maduras; Sistema Híbrido los une con responsabilidad, autoridad y evidencia**.

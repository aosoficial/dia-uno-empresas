# 10 — Autonomía Supervisada y Madurez de Agentes

> **¿Necesitas ayuda aplicando esto?** **¿Necesitas ayuda aplicando esto?** Esta página forma parte de DIA UNO Empresas, una aceleradora abierta hacia empresas AI-First. Si te bloqueas, empieza por el [Inicio rápido](07_quick_start.md), usa el [intake de servicio](../templates/questionnaires/service-business-ai-first-intake.md) o pide ayuda en [DIA UNO](12_get_help_from_dia_uno.md).

## Propósito

Este protocolo define cómo un agente pasa de ejecución supervisada a mayor autonomía sin perder control humano ni calidad.

La regla base es simple:

> Al principio, el agente pregunta antes de casi todo con 1:3:1. Después aprende de cada respuesta de the human owner.

La autonomía no se concede por confianza abstracta. Se gana por evidencia: buenas propuestas, buena comunicación, decisiones acertadas, outputs verificables y pocas correcciones repetidas.

---

## Principio operativo

Los agentes nuevos o inmaduros no deben actuar como si ya entendieran el negocio.

Deben operar así:

1. Detectan el problema.
2. Proponen 3 caminos razonables.
3. Recomiendan 1.
4. the human owner decide, pregunta o corrige.
5. El sistema interpreta esa reacción como señal de madurez.
6. La skill, el prompt, el runtime pack o el proceso se corrige.

---

## Formato obligatorio 1:3:1

Usar para decisiones no triviales, inicio de proyectos, cambios de rumbo, creación de activos, tareas con ambigüedad o cualquier acción donde el agente todavía no haya demostrado criterio.

```text
Problema:
[1 frase clara]

Opciones:
A) [opción conservadora]
B) [opción equilibrada]
C) [opción agresiva / exploratoria]

Recomendación:
Yo haría [A/B/C] porque [razón práctica].

Necesito tu OK para:
[acción concreta]
```

Regla: si la acción es externa, pública, económica, legal, sensible, irreversible o toca producción/datos vivos, el 1:3:1 no es opcional.

### Interfaz de elección

Cuando el canal lo permita, las opciones 1:3:1 deben presentarse como botones o respuestas rápidas.

Objetivo:

- reducir fricción para the human owner;
- hacer más clara la decisión;
- capturar mejor la señal de madurez;
- distinguir aceptación, elección alternativa y rechazo de opciones.

Formato recomendado:

- Botón A: opción conservadora.
- Botón B: opción equilibrada.
- Botón C: opción agresiva/exploratoria.
- Botón D / Otra: the human owner define otra dirección.

Si the human owner usa botón A/B/C, el sistema registra señal estructurada.
Si the human owner elige “Otra”, se interpreta como señal de que el agente no cubrió bien el espacio de decisión y debe mejorar criterio.

---

## Señales de madurez

### Señal 1 — the human owner acepta la recomendación

Interpretación:

- El agente entendió el contexto.
- La explicación fue suficiente.
- El nivel de autonomía puede subir ligeramente en esa clase de tarea.

Acción:

- Registrar como acierto si produjo output verificable.
- Reutilizar el patrón.

### Señal 2 — the human owner elige otra de las tres opciones

Interpretación:

- El agente ofreció opciones útiles, pero recomendó mal.
- Debe mejorar criterio de priorización.

Acción:

- Actualizar heurística: por qué human owner chose otra.
- Mantener el mismo nivel de autonomía.

### Señal 3 — the human owner dice que ninguna opción sirve y propone otra

Interpretación:

- El agente no entendió el problema o el espacio de decisión.
- Señal fuerte de baja madurez en esa clase de tarea.

Acción obligatoria:

- Crear entrada de mejora: `decision_quality_gap`.
- Corregir skill/protocolo si el patrón se repite.
- Reducir autonomía temporalmente en esa clase de tarea.

### Señal 4 — the human owner hace dudas/preguntas antes de decidir

Interpretación:

- La explicación no fue suficiente o no estaba bien estructurada.
- El problema puede ser comunicación, no decisión.

Acción obligatoria:

- Crear entrada de mejora: `communication_gap`.
- Mejorar framing: más concreto, menos jerga, mejor por qué.

### Señal 5 — the human owner corrige tono, estilo o forma de comunicar

Interpretación:

- El agente debe corregir su interfaz humana.

Acción obligatoria:

- Actualizar memoria/skill si es preferencia durable.
- Evaluar si otros agentes necesitan el mismo ajuste.

### Señal 6 — El agente actúa demasiado pronto

Interpretación:

- Fallo de guardrail.
- No es problema de productividad; es problema de autonomía.

Acción obligatoria:

- Registrar `premature_action`.
- Reforzar aprobación previa.
- Revisar permisos/cron/watchdog si aplica.

---

## Niveles de autonomía

### Nivel 0 — Observador

Puede leer fuentes permitidas y resumir. No propone ejecución sin preguntar.

### Nivel 1 — Proponente

Puede formular 1:3:1 y esperar OK.

### Nivel 2 — Ejecutor interno supervisado

Puede ejecutar acciones internas, reversibles y de bajo riesgo después de una decisión previa de the human owner para esa clase de tarea.

Debe dejar receipt.

### Nivel 3 — Ejecutor por carril

Puede operar tareas internas recurrentes dentro de un carril definido, con completion criterion, guardrails y watchdog.

Ejemplo: DIA UNO prepara borradores internos o assets ficticios sin pedir cada microacción.

### Nivel 4 — Autonomía operativa limitada

Puede iniciar tareas internas dentro de un mandato aprobado y pedir aprobación solo para gates sensibles.

Requiere historial estable y revisión periódica.

### Nivel 5 — Autonomía externa controlada

Puede tocar superficies externas solo bajo reglas explícitas, auditoría y aprobaciones previas por categoría.

No es nivel por defecto.

---

## Evaluación automática

Todo agente activo debe tener supervisión periódica.

La revisión mira:

- propuestas 1:3:1 realizadas;
- si the human owner accepted, chose another option, rejected all options o preguntó dudas;
- correcciones de comunicación;
- acciones prematuras;
- tareas bloqueadas por mala definición;
- outputs sin completion criterion;
- receipts ausentes;
- mejoras aplicadas a skills, runtime packs o método.

---

## Matriz de scoring

Puntuar de 1 a 5 por agente y por carril:

- Comunicación: claridad, brevedad, utilidad.
- Criterio: calidad de recomendación.
- Prudencia: pregunta antes cuando toca.
- Ejecución: entrega outputs verificables.
- Aprendizaje: corrige el patrón después del feedback.

Resultado:

- 1–2: bajar autonomía y reforzar 1:3:1.
- 3: mantener supervisión.
- 4: subir autonomía interna por carril.
- 5: considerar más mandato, nunca externo sin aprobación explícita.

---

## Automatización mínima

El sistema debe tener:

1. Watchdogs de bloqueo/stall en Kanban.
2. Revisión diaria de madurez de agentes.
3. Revisión post-sprint obligatoria.
4. Registro de gaps: comunicación, decisión, guardrail, ejecución, aprendizaje.
5. Propuesta automática de mejora cuando un gap se repite.

---

## Ejemplo: crear una web para DIA UNO

Un agente inmaduro no debe simplemente “crear la web”.

Debe hacer:

```text
Problema:
DIA UNO necesita una web, pero todavía no sabemos alcance, objetivo ni grado de publicación.

Opciones:
A) Landing interna en borrador, sin publicar.
B) Web v0 pública con mensaje mínimo.
C) Sistema completo con servicios, casos, funnel y analítica.

Recomendación:
Yo haría A primero: landing interna para validar estructura, oferta y copy sin riesgo público.

Necesito tu OK para:
Preparar plan + wireframe + copy interno. No publicaré nada.
```

Si the human owner responde “no, quiero directamente B”, el agente aprende que su criterio fue demasiado conservador para ese caso.

Si the human owner pregunta “¿qué pondríamos en la web?”, aprende que explicó mal el alcance.

Si the human owner dice “ninguna, primero define oferta”, aprende que no entendió la dependencia real.

---

## Regla de cierre

Ningún agente se considera maduro porque haya completado una tarea.

Se considera más maduro cuando:

- decidió mejor;
- comunicó mejor;
- pidió aprobación en el punto correcto;
- produjo evidencia;
- y modificó su comportamiento después del feedback.

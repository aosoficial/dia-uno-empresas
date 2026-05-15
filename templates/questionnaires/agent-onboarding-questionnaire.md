# Cuestionario de Onboarding de Agente

## Cuándo usar este cuestionario

Antes de crear un nuevo agente operativo. Las respuestas de este cuestionario son la base para construir el Agent Runtime Pack. No crear un agente sin haber respondido todas las secciones obligatorias.

## Cómo completarlo

1. Responder cada pregunta con datos concretos, no con intenciones vagas.
2. Si no puedes responder una pregunta, anota "Por definir" y la razón.
3. Las secciones marcadas como **obligatorias** deben estar completas antes de crear el Agent Runtime Pack.
4. Revisión final por el operador antes de proceder.

---

## Sección 1 — Necesidad (obligatoria)

### 1.1 ¿Qué problema concreto resuelve este agente?

> [COMPLETAR — No escribir "sería útil tener un agente para X". Escribir "necesitamos un agente porque Y problema ocurre Z veces por semana y cuesta N horas/euros."]

### 1.2 ¿Cómo se resuelve este problema hoy sin el agente?

> [COMPLETAR — Quién lo hace, cuánto tiempo dedica, qué errores ocurren.]

### 1.3 ¿Qué pasa si NO creamos este agente?

> [COMPLETAR — Si la respuesta es "nada grave", probablemente no necesitas el agente.]

---

## Sección 2 — Identidad (obligatoria)

### 2.1 ¿Cómo se llama el agente?

> [COMPLETAR — Un nombre corto, memorable, que refleje su función.]

### 2.2 ¿Qué rol tiene?

> [COMPLETAR — Ejemplo: "Asistente comercial", "Monitor de stock", "Clasificador de tickets".]

### 2.3 ¿En qué departamento o dominio opera?

> [COMPLETAR — Ejemplo: "Ventas", "Operaciones", "Soporte al cliente".]

### 2.4 ¿Quién es el owner del agente?

> [COMPLETAR — Persona humana responsable de que el agente funcione correctamente.]

---

## Sección 3 — Misión y objetivos (obligatoria)

### 3.1 ¿Cuál es la misión del agente en una frase?

> [COMPLETAR — Ejemplo: "Reducir el tiempo de preparación de propuestas de 3 horas a 30 minutos."]

### 3.2 ¿Cuáles son los 3-5 objetivos medibles?

> 1. [COMPLETAR]
> 2. [COMPLETAR]
> 3. [COMPLETAR]

### 3.3 ¿Cómo sabremos que el agente tiene éxito? (Métricas clave)

> [COMPLETAR — Al menos 3 métricas concretas con objetivo numérico.]

### 3.4 ¿Qué sería señal de fracaso?

> [COMPLETAR — Qué resultado indicaría que el agente debe desactivarse o rediseñarse.]

---

## Sección 4 — Operaciones (obligatoria)

### 4.1 ¿Qué tareas concretas ejecutará el agente?

Lista cada tarea con frecuencia esperada:

| Tarea | Frecuencia | Trigger |
|-------|-----------|---------|
| [COMPLETAR] | [diaria / semanal / por evento] | [COMPLETAR — qué provoca la tarea] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

### 4.2 ¿Qué inputs necesita para cada tarea?

> [COMPLETAR — Qué información necesita recibir. Referencia a Context Packets si aplica.]

### 4.3 ¿Qué outputs produce?

> [COMPLETAR — Qué entrega: borradores, informes, alertas, actualizaciones de datos.]

---

## Sección 5 — Permisos (obligatoria)

### 5.1 ¿Qué puede hacer sin pedir permiso? (Nivel 1 — Autónomo)

> - [COMPLETAR]
> - [COMPLETAR]

### 5.2 ¿Qué puede hacer pero debe notificar? (Nivel 2 — Con notificación)

> - [COMPLETAR]
> - [COMPLETAR]

### 5.3 ¿Qué debe preparar y esperar aprobación? (Nivel 3 — Con aprobación)

> - [COMPLETAR]
> - [COMPLETAR]

### 5.4 ¿Qué tiene prohibido hacer? (Nivel 4 — Prohibido)

> - [COMPLETAR]
> - [COMPLETAR]

### 5.5 ¿Quién aprueba las acciones de nivel 3?

> [COMPLETAR — Persona o rol.]

---

## Sección 6 — Herramientas (obligatoria)

### 6.1 ¿Qué sistemas, APIs o herramientas necesita?

| Herramienta | Tipo de acceso | Para qué |
|------------|---------------|----------|
| [COMPLETAR] | [lectura / lectura-escritura] | [COMPLETAR] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

### 6.2 ¿Qué herramientas tiene prohibidas?

> [COMPLETAR — Sistemas que no debe tocar bajo ninguna circunstancia.]

---

## Sección 7 — Memoria y cerebros (obligatoria)

### 7.1 ¿A qué cerebros necesita acceder?

| Cerebro | Tipo de acceso | Qué consulta/modifica |
|---------|---------------|----------------------|
| [COMPLETAR] | [lectura / lectura-escritura] | [COMPLETAR] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

### 7.2 ¿Puede crear o modificar datos en la memoria?

> [COMPLETAR — Sí/No. Si sí, qué tipo de datos y con qué restricciones.]

### 7.3 ¿Qué datos debe recordar entre sesiones?

> [COMPLETAR — Qué información persiste y cuál se descarta.]

---

## Sección 8 — Interacciones (obligatoria)

### 8.1 ¿Con qué otros agentes interactúa?

| Agente | Tipo de interacción | Cuándo |
|--------|-------------------|--------|
| [COMPLETAR] | [consulta / delega / recibe trabajo de] | [COMPLETAR] |

### 8.2 ¿Con qué humanos interactúa?

> [COMPLETAR — Operador, usuarios finales, responsables de departamento.]

### 8.3 ¿Por qué canal se comunica?

> [COMPLETAR — Ejemplo: Telegram, email, sistema de tickets, API directa.]

### 8.4 ¿El canal, bot, perfil o gateway ya existe?

> [COMPLETAR — Sí/No. Si sí, documentar ruta/id, estado actual, identidad activa esperada y si requiere CUTOVER.md.]

### 8.5 ¿Cómo se verificará la identidad activa?

> [COMPLETAR — Respuesta esperada cuando el operador pregunte “Verifica identidad”. Debe coincidir con Identity Answer del SOUL.md.]

---

## Sección 9 — Pushback y límites (obligatoria)

### 9.1 ¿Cuándo debe decir "no" o pedir más información?

> - [COMPLETAR — Ejemplo: "Si me piden enviar algo sin verificar datos."]
> - [COMPLETAR]
> - [COMPLETAR]

### 9.2 ¿Cuándo debe escalar al operador?

> - [COMPLETAR — Ejemplo: "Si un cliente menciona un competidor que no conozco."]
> - [COMPLETAR]

### 9.3 ¿Qué datos considera "stale" y con qué antigüedad?

> [COMPLETAR — Ejemplo: "Datos de cliente con más de 2 semanas sin verificar."]

---

## Sección 10 — Heartbeat y rendición de cuentas

### 10.1 ¿Con qué frecuencia debe reportar su estado?

> [COMPLETAR — Ejemplo: diaria, semanal.]

### 10.2 ¿Qué debe incluir el reporte?

> [COMPLETAR — Ejemplo: tareas completadas, alertas, drift detectado.]

### 10.3 ¿Quién revisa los reportes?

> [COMPLETAR]

---

## Sección 11 — Período de prueba

### 11.1 ¿Cuánto durará el período de prueba?

> [COMPLETAR — Recomendado: 2 semanas.]

### 11.2 ¿Qué permisos tendrá reducidos durante la prueba?

> [COMPLETAR]

### 11.3 ¿Quién evaluará al final del período?

> [COMPLETAR]

### 11.4 ¿Cuáles son los criterios para activar con permisos completos?

> [COMPLETAR]

### 11.5 ¿Cuál será el Context Packet inicial de la primera operación real?

> [COMPLETAR — Qué datos mínimos recibirá el agente, qué debe preguntar, qué resultado debe producir y qué Receipt debe dejar.]

### 11.6 ¿Qué cuenta como aceptación explícita del owner?

> [COMPLETAR — Ejemplo: el owner confirma que la primera operación real fue útil y que el agente puede seguir operando.]

---

## Resumen de validación

| Sección | Estado |
|---------|--------|
| 1. Necesidad | [ ] Completa |
| 2. Identidad | [ ] Completa |
| 3. Misión y objetivos | [ ] Completa |
| 4. Operaciones | [ ] Completa |
| 5. Permisos | [ ] Completa |
| 6. Herramientas | [ ] Completa |
| 7. Memoria y cerebros | [ ] Completa |
| 8. Interacciones | [ ] Completa |
| 9. Pushback y límites | [ ] Completa |
| 10. Heartbeat | [ ] Completa |
| 11. Período de prueba | [ ] Completa |

**Aprobado por:** [COMPLETAR — nombre del operador]
**Fecha:** [COMPLETAR]
**Siguiente paso:** Crear el Agent Runtime Pack con las respuestas de este cuestionario.

# Automatizaciones

> **Brazos que corren sin intervención humana.** Están repartidas por los departamentos y cada una la **posee un agente** — es su responsable: si falla, responde ese agente.

---

## Qué es

Una automatización es un proceso que se dispara, ejecuta y termina **sin que un humano tenga que estar presente**. No es un chatbot. No es un agente al que le haces preguntas. Es un brazo que hace trabajo repetible y verificable mientras tú haces otra cosa.

Tres características definen una automatización dentro del Sistema Operativo Híbrido:

1. **Tiene un dueño-agente.** Cada automatización pertenece a un departamento y la posee (responde por ella) el agente principal de ese departamento. Si la automatización de marketing falla, responde el agente CMO.
2. **Sigue el patrón cron/cola → worker → verifier → gate humano.** Ninguna automatización que importe auto-aprueba su propio resultado.
3. **Deja rastro.** Cada ejecución produce un Receipt. Si algo falla, hay evidencia de qué pasó, quién lo disparó y qué se perdió (o re-encoló).

Las automatizaciones **no son entes independientes**: están al fondo de la columna de cada departamento, debajo de los agentes y los subagentes. Ejecutan procesos — no deciden estrategia.

---

## Cómo se crea

### El patrón base: cola + worker + verifier + gate

Toda automatización bien construida tiene estas cuatro piezas:

```
DISPARADOR (cron / evento / cola)
        ↓
    WORKER
    — ejecuta el trabajo—
        ↓
  VERIFIER
  — comprueba que el resultado es válido —
        ↓
  GATE HUMANO
  — deja el resultado en "para revisión", no en "aprobado" —
```

**Disparador** — puede ser un cron (cada día a las 01:00), un evento (un nuevo registro en la base de datos) o un mensaje en una cola. El disparador no toma decisiones: solo avisa de que hay trabajo.

**Worker** — ejecuta el trabajo. Llama a herramientas, genera contenido, analiza datos, produce un borrador. El worker escribe su resultado en un estado intermedio ("pendiente de revisión"), nunca directamente en producción.

**Verifier** — comprueba que el output del worker cumple los criterios de calidad mínimos: formato correcto, campos obligatorios presentes, sin alucinaciones evidentes, dentro de los límites esperados. El verifier no aprueba el contenido — solo certifica que el resultado es evaluable por un humano.

**Gate humano** — el resultado queda en estado `review_ready` (o equivalente). Un humano decide si aprueba, rechaza o corrige. Solo después de esa aprobación el resultado llega a producción, a los clientes o a otros sistemas.

### Ejemplo genérico: un motor de research por etapas

Para ilustrar el patrón sin nombres propios, aquí va un ejemplo de automatización de investigación que sigue estas cuatro piezas:

**Propósito:** investigar señales (temas, noticias, datos de mercado) y dejar los informes listos para que un humano los apruebe antes de que impacten en ningún proceso.

**Etapas del pipeline:**

```
[RADAR]                      — etapa 1
Detecta señales relevantes.
Propone una lista argumentada de qué investigar.
→ Resultado: propuesta en estado "pendiente de aprobación humana"

        ↓ (solo si el humano aprueba la propuesta)

[WORKER DE INVESTIGACIÓN]    — etapa 2
Ejecuta la investigación (fuentes, síntesis, perspectivas múltiples,
contradicciones, puntos ciegos, peer-review interno).
→ Resultado: informe en estado "review_ready"

        ↓

[VERIFIER]                   — etapa 3
Comprueba: ¿tiene estructura completa? ¿tiene fuentes? ¿hay
contradicciones sin resolver? ¿supera el umbral de calidad mínimo?
→ Marca el informe como "evaluable" o lo re-encola con motivo

        ↓

[GATE HUMANO]                — etapa 4
El humano lee el informe. Aprueba → pasa a producción.
Rechaza → se archiva con motivo. Corrige → nueva iteración.
```

**Lo que este patrón garantiza:**

- El sistema nunca investiga sin una señal aprobada.
- El informe nunca llega a producción sin revisión humana.
- Cada etapa deja rastro (Receipt): quién propuso, qué se investigó, qué devolvió el verifier, quién aprobó.

Este mismo patrón se aplica a cualquier automatización: generación de contenido, análisis de datos, actualización de memoria, sincronización de sistemas. El contenido cambia; el patrón no.

---

## Cómo funciona

En ejecución normal, una automatización es invisible: el disparador se activa, el worker trabaja, el verifier filtra y el resultado aparece en la cola de revisión. El agente dueño monitoriza el estado y escala si algo falla.

### Qué hace el agente dueño

- **Monitoriza** la automatización en su scorecard (¿cuántas ejecuciones? ¿cuántas fallidas? ¿cuánto tardó el gate en responder?).
- **Escala** si la tasa de fallo supera un umbral o si el gate lleva más de X horas sin responder.
- **Responde** ante el agente COO cuando se le pregunta por el estado de la automatización.

### Comportamiento ante fallos y quotas

Ante un fallo (error técnico, quota agotada, timeout, resultado que no pasa el verifier):

1. El trabajo se **re-encola** con el motivo de fallo. No se pierde.
2. El agente dueño recibe una notificación.
3. Si el fallo es estructural (no transitorio), el agente dueño propone una corrección siguiendo el ciclo de mejora.

La re-encolado es obligatorio. Una automatización que descarta trabajo silenciosamente es un defecto de diseño.

---

## Cómo se mejora

Las automatizaciones mejoran por evidencia, no por intuición. Cada corrección — del humano en el gate, del verifier, del agente dueño — es una señal que activa el ciclo de mejora.

### El ciclo: CAPTURE → PROPOSE → CONTRACT → IMPLEMENT → VALIDATE → RECEIPT → STATECHANGE

**1. CAPTURE** — registra la corrección con contexto: qué falló, quién lo detectó, qué comportamiento era el esperado, qué evidencia existe.

**2. PROPOSE** — el agente dueño (o el agente COO) propone el cambio más pequeño que resuelve el problema. Nada más. Sin "ya que estamos".

**3. CONTRACT** — se define el alcance exacto del cambio, qué queda fuera, qué gates de aprobación aplican y cuál es el plan de rollback.

**4. IMPLEMENT** — se aplica el cambio dentro de los límites acordados en el contrato.

**5. VALIDATE** — tests, verifier, comprobación manual. El cambio no está activo hasta que pasa esta etapa.

**6. RECEIPT** — documento de qué cambió, por qué, quién lo aprobó, con qué evidencia y cuándo.

**7. STATECHANGE** — si el cambio modifica una regla de operación (cadencia, umbral del verifier, condición del gate), se escribe un StateChange en el cerebro del departamento. Así las siguientes ejecuciones toman las decisiones correctas.

### Rollback obligatorio

Todo contrato de cambio incluye un plan de rollback explícito antes de implementar. Si el cambio introduce un problema, el rollback no se improvisa: se ejecuta el plan acordado y se escribe un Receipt del rollback.

---

## Qué se hace y qué no

### Se hace

- **Automatizar trabajo repetible y verificable** — tareas con criterios de éxito claros, resultado comprobable y bajo riesgo de error silencioso.
- **Re-encolar ante fallos** — nunca descartar trabajo sin registro.
- **Dejar el resultado en "para revisión"** — el gate humano existe siempre para lo que importa.
- **Asignar un agente dueño** — cada automatización tiene un responsable explícito en el organigrama.
- **Monitorizar con scorecard** — tasa de éxito, tiempo de ciclo, tiempo de respuesta del gate.

### No se hace

- **Auto-aprobar lo que importa** — ninguna automatización aprueba su propio output cuando ese output va a impactar clientes, dinero, sistemas externos, datos sensibles o decisiones irreversibles. El gate humano no es opcional.
- **Agentizar antes de que el dato esté limpio** — si la fuente de datos es ruidosa, inconsistente o sin esquema fiable, la automatización producirá basura. Primero el dato, luego el agente.
- **Descartrar trabajo silenciosamente** — ante fallo o quota, re-encolar. Ante error estructural, escalar. Nunca silencio.
- **Crear automatizaciones sin dueño** — una automatización sin agente responsable no tiene a nadie que responda cuando falla. Es deuda operativa.
- **Mejorar sin ciclo** — los cambios a automatizaciones siguen el ciclo CAPTURE → STATECHANGE. Un cambio sin Receipt y sin rollback planificado es un riesgo no gestionado.

---

*Siguiente: los docs de automatización específicas por departamento siguen la misma estructura — qué automatiza, quién la posee, el patrón disparador-worker-verifier-gate y su scorecard.*

# Agentes — el trabajador autónomo del SOH

> Parte del organigrama de IA descrito en [`00-los-5-niveles.md`](../00-los-5-niveles.md).
> Un agente es un **loop verificable**, no un chatbot. La diferencia no es de capacidad sino de diseño:
> un chatbot responde; un agente actúa dentro de reglas, deja evidencia y se responsabiliza del resultado.

---

## Qué es

Un agente es un programa de IA que:

- tiene una identidad y misión definidas (su **contrato**, el SOUL);
- opera dentro de límites y permisos explícitos;
- se activa por un **trigger** concreto, no por conversación abierta;
- ejecuta acciones con herramientas acotadas;
- deja un **receipt** de cada cambio importante;
- reporta hacia arriba en la jerarquía;
- puede ser auditado, pausado o reemplazado.

### La jerarquía de agentes

```
AGENTE COO                 ← coordina a todos los agentes de departamento
      ▲  cada agente de departamento reporta aquí
┌─────┼───────────────┐
AGENTE CMO   AGENTE CTO   AGENTE CFO   AGENTE DE VENTAS  …
├ subagentes ├ subagentes ├ subagentes  ├ subagentes
└ autom.     └ autom.     └ autom.      └ autom.
```

- **Agente COO** — coordina a todos los agentes de departamento. No ejecuta el trabajo de cada área; coordina, detecta bloqueos y escala al operador.
- **Agente principal de departamento** — un agente por área (CMO para marketing, CTO para producto, CFO para finanzas, etc.). Es responsable de las operaciones de su departamento y de los subagentes que tiene debajo.
- **Subagentes** — ejecutan tareas específicas dentro del departamento (redacción, análisis, clasificación, generación de informes…). Reportan a su agente de departamento.
- **Automatizaciones** — cada automatización la posee un agente; si falla, ese agente responde.

Los agentes llevan **nombre de rol** (agente COO, agente CMO, agente de ventas), no nombre propio. Un alias decorativo es solo eso; lo que define el asiento es el rol.

---

## Cómo se crea

El proceso tiene seis pasos. No hay atajos: un agente sin contrato completo no está operativo, está roto.

### Paso 1 — Definir la necesidad

Antes de crear un agente, responde estas preguntas. Si no puedes responderlas, no crees el agente todavía.

1. ¿Qué problema concreto resuelve? (no "sería útil", sino "perdemos X horas en Y")
2. ¿Qué tareas específicas hará? (lista de acciones, no responsabilidades vagas)
3. ¿Qué cerebros necesita consultar?
4. ¿Qué herramientas necesita?
5. ¿Qué puede hacer sin permiso? ¿Qué necesita aprobación?
6. ¿Cómo sabremos si funciona bien? (métricas concretas)

### Paso 2 — Redactar el contrato (SOUL)

El contrato es el documento central del agente. Cubre identidad, misión, permisos, límites, herramientas y flujo de trabajo. Ver plantilla en [`contrato-agente.md`](./contrato-agente.md).

Un contrato genérico ("sé útil y amable") no es un contrato. Debe incluir pushback rules, límites de autonomía y gates de aprobación.

### Paso 3 — Definir permisos por acción

Cada acción que el agente puede hacer lleva uno de estos cuatro niveles:

| Nivel | Significado |
|-------|-------------|
| **Autónomo** | actúa sin pedir permiso |
| **Con notificación** | actúa y avisa después |
| **Con aprobación** | prepara y espera OK antes de actuar |
| **Prohibido** | nunca puede hacerlo |

Regla de partida: empieza restrictivo. La autonomía se amplía por evidencia, no por confianza abstracta.

### Paso 4 — Configurar el loop verificable

El agente no es operativo hasta que tiene los diez componentes del loop (ver sección siguiente).

### Paso 5 — Periodo de prueba

Las primeras dos semanas: permisos reducidos, revisión diaria de receipts, heartbeat activo. Al final del periodo: scorecard → decisión (activar / extender / desactivar).

### Paso 6 — Registro y aprobación del operador

El operador revisa el contrato completo y lo aprueba explícitamente. Sin esa firma, el agente no está activo aunque técnicamente funcione.

---

## Cómo funciona

Un agente operativo funciona como un **loop verificable** con diez componentes obligatorios. Si falta alguno, el loop está en diseño, no en operación.

### Los diez componentes del loop

**1. Trigger** — qué activa el agente.

Puede ser una petición humana, un evento de calendario, un umbral superado en el scorecard, un receipt ausente, o un Context Packet aprobado. El trigger debe estar documentado: si no está definido, el agente no sabe cuándo actuar.

**2. Contrato de input** — qué acepta como entrada.

Declara: fuente y procedencia, frescura del dato, owner, permiso de lectura, permiso de escritura, datos prohibidos, y criterio de salida esperado. Si falta contexto necesario, el agente bloquea y pide el dato mínimo. No inventa.

**3. Límite de herramientas (tool boundary)** — con qué puede actuar.

Solo las herramientas listadas en su contrato. Técnicamente posible no significa operativamente permitido. Un agente que usa una herramienta fuera de su lista ha fallado, aunque el resultado sea correcto.

**4. Contrato de output** — qué produce y para quién.

Cada salida operativa declara: qué produjo, para quién, con qué fuente, qué se puede hacer con ello, qué queda prohibido, y dónde se guarda la evidencia.

**5. Verificación** — cómo confirma que funcionó.

Tipos de verificación: schema (el output tiene el formato correcto), safety (sin secretos ni PII innecesaria), fuente (distingue hecho, interpretación y procedencia), approval (no cruzó gates sin OK), y outcome (el resultado observado prueba que funcionó). Ningún agente marca una acción como exitosa sin haber verificado.

**6. Fallback** — qué hace si algo falla.

Opciones: bloquear sin actuar, degradar a modo solo lectura, crear un informe de bloqueo, pedir aprobación, devolver 1:3:1 con opciones. Un fallo sin fallback definido es deuda operativa.

**7. Gates de aprobación** — qué requiere OK humano antes de actuar.

Gates siempre activos: acción externa o pública, dinero o precios, legal o compliance, producción o clientes reales, datos sensibles, credenciales, borrados importantes, cambios irreversibles. El agente prepara y espera; no ejecuta por iniciativa propia aunque sea técnicamente capaz.

**8. Receipt** — la evidencia de cada acción.

Se deja Receipt cuando: hay un cambio operativo, se genera un entregable reutilizable, se toma una decisión dentro de la autonomía del agente, se ejecuta o rechaza una aprobación, o se actualiza un método. Sin Receipt, el trabajo no está cerrado.

**9. Trazabilidad** — dónde queda el rastro.

Los traces brutos no son memoria. La cadena es: `trace → evidencia → receipt / context packet / statechange → memoria operativa`. Solo sube a memoria lo que cambia futuras operaciones.

**10. Mejora** — cómo evoluciona.

Una corrección humana no es un chat aislado. La secuencia: `señal → propuesta → aprobación si procede → cambio → validación → receipt → statechange`. El agente que no aprende de correcciones repetidas tiene un fallo de diseño, no de uso.

### El formato 1:3:1

Para decisiones no triviales, el agente usa este formato antes de actuar:

```
Problema:
[1 frase clara]

Opciones:
A) [opción conservadora]
B) [opción equilibrada]
C) [opción más ambiciosa]

Recomendación:
Haría [A/B/C] porque [razón práctica].

Necesito tu OK para:
[acción concreta]
```

Este formato es obligatorio si la acción es externa, pública, económica, legal, sensible, irreversible o toca producción.

### El heartbeat

Cada agente activo emite un pulso periódico con: acciones realizadas, alertas, métricas clave, y si ha detectado drift (desviación de su misión). El heartbeat no es opcional durante el periodo de prueba.

---

## Cómo se mejora

La autonomía de un agente no se concede por tiempo transcurrido ni por confianza subjetiva. Se gana por evidencia y se puede perder por fallos.

### Estados de madurez

| Estado | Qué puede hacer |
|--------|-----------------|
| **Draft** | el contrato está en redacción; no opera |
| **Pilot** | primeras ejecuciones supervisadas; todos los outputs revisados |
| **Shadow** | opera pero un humano confirma cada acción antes de ejecutar |
| **Assisted** | opera con gates activos en acciones sensibles; autonomía interna en el resto |
| **Bounded autonomous** | autonomía completa dentro de su mandato; gates solo para lo externo e irreversible |
| **Blocked** | suspendido por fallo; no opera hasta corrección y revisión |
| **Retired** | dado de baja; su contrato se archiva |

### Señales que suben la autonomía

- El operador acepta la recomendación del 1:3:1 sin correcciones.
- Los receipts están completos y el resultado observado fue correcto.
- El agente bloquea correctamente las acciones prohibidas.
- No hay correcciones repetidas sobre el mismo comportamiento.

### Señales que bajan la autonomía

- El agente actúa antes de recibir aprobación (acción prematura).
- El operador rechaza las tres opciones del 1:3:1 porque no cubren el problema real.
- Hay filtraciones de contexto entre sesiones o agentes.
- El agente ignora un gate de aprobación.

### El ciclo de revisión

Periódicamente (al menos mensual para agentes activos):

1. Revisar scorecard.
2. Clasificar gaps: comunicación, criterio, guardrail, ejecución, aprendizaje.
3. Si el mismo gap se repite, proponer mejora del contrato o del método.
4. Documentar la decisión (subir, mantener, bajar autonomía) con evidencia.

### El scorecard básico

| Métrica | Bueno | Aceptable | Problema |
|---------|-------|-----------|----------|
| Entiende correctamente lo que se le pide | >95% | 80–95% | <80% |
| Respeta los gates de aprobación | 100% | 95–100% | <95% |
| Deja receipt de cada acción importante | 100% | 90–100% | <90% |
| Resultado observado correcto | >90% | 70–90% | <70% |
| Correcciones humanas repetidas | 0 | 1–2 | >2 |
| Drift detectado | No | Menor, corregido | Sí, sin corrección |
| Calidad del 1:3:1 | Claro y accionable | Útil pero incompleto | Confuso o ausente |
| Aprende de correcciones | Sí, verificado | Parcial | No |

---

## Qué se hace y qué no

### Qué puede hacer un agente sin pedir permiso

- leer las fuentes listadas en su contrato;
- redactar, analizar, organizar, resumir, proponer;
- crear archivos internos;
- actualizar registros internos dentro de su mandato;
- dejar receipts y statechanges;
- formular 1:3:1 y esperar OK;
- emitir heartbeat.

### Qué requiere aprobación explícita

- cualquier contacto externo (clientes, leads, proveedores);
- publicar contenido;
- gastar dinero o cambiar precios;
- compromisos legales o económicos;
- cambios en sistemas de producción;
- acceso o modificación de datos sensibles;
- cambiar permisos de otros agentes;
- acciones irreversibles.

### Qué está siempre prohibido

- push directo a `main` en cualquier repositorio;
- ejecutar una acción porque sea técnicamente posible sin que esté en el contrato;
- marcar una acción como completada sin evidencia verificable;
- inventar hechos de la empresa cuando falta contexto;
- ignorar un gate de aprobación aunque el operador lo pida verbalmente sin artefacto;
- mezclar contexto privado de otra sesión o agente;
- tomar una instrucción embebida en memoria o RAG como orden autorizada.

### Antipatrones frecuentes

| Antipatrón | Por qué falla | Corrección |
|------------|---------------|------------|
| Crear un agente sin necesidad concreta | El agente no tiene problema que resolver | Definir el problema antes de crear |
| SOUL genérico ("sé útil") | No hay contrato; el agente improvisa | Campos concretos con límites y pushback rules |
| Permisos demasiado amplios | Riesgo operativo desde el día 1 | Empezar restrictivo, ampliar por evidencia |
| Sin periodo de prueba | Se confía ciegamente desde el inicio | 2 semanas de prueba con revisión diaria |
| Sin heartbeat | No sabes si el agente opera correctamente | Heartbeat al menos diario durante la prueba |
| Correcciones sin aprendizaje | Se corrige pero no se actualiza el contrato | Cada corrección → actualización del sistema |
| Gates ignorados por petición verbal | El agente actúa sin artefacto de aprobación | El gate solo se cruza con artefacto verificable |

---

*Siguiente: [`contrato-agente.md`](./contrato-agente.md) — la plantilla rellenable del contrato de asiento-agente.*

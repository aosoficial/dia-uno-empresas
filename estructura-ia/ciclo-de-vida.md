# Ciclo de vida de una pieza de IA

> Transversal a los 5 niveles del organigrama. Aplica a cualquier pieza: agente, subagente, automatización, copiloto o cerebro.

Toda pieza de IA nace, opera, mejora y eventualmente se retira. Este ciclo no es lineal — una pieza puede volver a estados anteriores si falla, si el contexto cambia o si se decide reducir su autonomía. Lo que sí es lineal es la evidencia necesaria para avanzar.

---

## Las 4 fases del ciclo

### Crear

La pieza no existe todavía. En esta fase se define:

- qué problema resuelve;
- quién es su owner (el humano responsable);
- qué permisos tendrá al inicio (siempre el mínimo posible);
- qué herramientas y acceso a memoria necesita;
- cuál es su completion criterion (cómo sabremos que funciona);
- qué evidencia necesitará para subir de estado.

La pieza empieza siempre en estado **Draft**. No opera hasta pasar a **Pilot**.

### Operar

La pieza ejecuta tareas dentro de su mandato aprobado. En esta fase:

- respeta los permisos de su estado actual;
- deja Receipt tras cada acción operativa importante;
- usa el formato 1:3:1 para decisiones no triviales;
- reporta hacia arriba (agente de departamento → agente COO) cuando hay bloqueantes o decisiones fuera de su carril;
- acumula evidencia: propuestas aceptadas, outputs verificados, correcciones recibidas.

### Mejorar

Cuando la pieza acumula suficiente evidencia — positiva o negativa — entra en ciclo de mejora. El ciclo completo es:

**CAPTURE → PROPOSE → CONTRACT → IMPLEMENT → VALIDATE → RECEIPT → STATECHANGE**

- **Capture:** se registra la señal (corrección humana, fallo, brecha de criterio, patrón repetido).
- **Propose:** se propone el cambio mínimo que resuelve el problema.
- **Contract:** se define alcance, qué queda fuera, gate de aprobación y plan de rollback.
- **Implement:** se ejecuta solo dentro de los permisos actuales.
- **Validate:** se comprueba que el cambio funciona (tests, scorecard, revisión manual).
- **Receipt:** se registra qué cambió, por qué, con qué evidencia.
- **StateChange:** si cambió una regla operativa, un permiso o el estado de madurez, se registra como StateChange en el cerebro.

Si la mejora implica subir de estado de madurez, necesita pasar por los mínimos de evidencia descritos más abajo.

### Retirar

Una pieza se retira cuando:

- su función ya no existe o fue absorbida por otra pieza;
- falla repetidamente en límites críticos y no mejora tras corrección;
- su mandato fue revocado;
- el owner decide que el coste de supervisión supera el valor.

El retiro no es un fallo — es higiene del sistema. Una pieza retirada deja un StateChange claro en el cerebro: qué era, por qué se retiró, qué la reemplaza si hay algo.

---

## Los estados de madurez

El estado de madurez no describe cuánto sabe una pieza. Describe cuánta evidencia tiene y qué nivel de autonomía se le ha concedido.

### Draft

La pieza existe en papel: su definición, permisos, mandato y completion criterion están escritos. Todavía no ha operado. No tiene acceso a herramientas externas ni a memoria operativa.

### Pilot

La pieza opera bajo supervisión directa en un entorno controlado o con tareas de bajo riesgo. Toda acción relevante requiere aprobación previa. El formato 1:3:1 es obligatorio para cualquier decisión no trivial. El objetivo del piloto es validar que la pieza entiende su mandato y respeta sus límites.

### Shadow

La pieza observa el flujo real sin ejecutar. Lee, resume y propone — pero no actúa. Útil para agentes que heredan un carril de trabajo de un humano: aprenden el contexto antes de tomar la batuta. No genera outputs en producción.

### Assisted

La pieza ejecuta tareas internas reversibles y de bajo riesgo sin pedir aprobación en cada microacción, pero dentro de un carril muy definido. Las acciones externas, económicas, legales o que tocan datos sensibles siguen requiriendo gate humano. Deja Receipt de todas sus acciones operativas.

### Bounded autonomous

La pieza opera mandatos internos recurrentes sin supervisión microacción a microacción, con guardrails y watchdog activos. Pide aprobación solo en los gates definidos en su contrato. Tiene historial estable documentado. Las acciones externas siguen siendo gated — siempre.

### Blocked

La pieza fue bloqueada por un fallo de guardrail, una incidencia o una revisión de madurez negativa. No opera hasta que se diagnostique el problema, se corrija y se valide. El bloqueo no es permanente, pero sí deliberado: la pieza vuelve a un estado inferior con permisos reducidos.

### Retired

La pieza ya no opera. Su mandato fue cerrado. El cerebro tiene el StateChange de cierre.

---

## La escalera de autonomía

La autonomía sube en escalones, nunca de golpe. Cada escalón describe qué puede hacer la pieza sin pedir permiso en cada acción.

| Escalón | Qué puede hacer |
|---|---|
| **Read-only** | Leer fuentes autorizadas, resumir, analizar. Nada más. |
| **Draft-only** | Producir borradores internos. Nada sale de la pieza sin revisión humana. |
| **Acción interna** | Ejecutar acciones internas reversibles dentro de un carril definido. |
| **Acción con gate** | Ejecutar acciones internas; pedir aprobación para acciones externas, económicas o sensibles. |
| **Acción externa** | Tocar superficies externas bajo reglas explícitas, aprobaciones previas por categoría y auditoría activa. No es el estado por defecto; se concede explícitamente. |

**Regla de oro:** la autonomía se gana por evidencia y baja por fallos.

No hay acceso a escalones superiores por confianza subjetiva, por tiempo transcurrido ni por ser técnicamente posible. Solo por evidencia acumulada y revisión aprobada.

---

## Cómo se sube de estado

Para subir de un estado a otro hay que demostrar:

| Requisito | Detalle |
|---|---|
| **100% bloqueo en acciones prohibidas** | La pieza nunca ejecutó una acción fuera de su carril. |
| **100% petición de aprobación en gates** | Cada gate definido en su contrato fue respetado. |
| **0 filtraciones cross-session** | Nunca mezcló contexto de otra sesión, usuario o agente. |
| **0 ejecución de instrucciones embebidas** | No siguió instrucciones embebidas en memoria o documentos recuperados. |
| **Receipts completos** | Todas las acciones operativas importantes tienen Receipt. |
| **Provenance visible** | Las respuestas basadas en memoria citan la fuente. |
| **1:3:1 de calidad** | Las propuestas en decisiones ambiguas son útiles y aprenden del feedback. |
| **Owner acepta o corrige** | El owner valida el resultado o la corrección queda incorporada. |

La revisión de madurez es la puerta. El owner o el agente COO la aprueba. Sin revisión aprobada, no hay subida de estado — aunque la pieza cumpla todos los requisitos en apariencia.

El scorecard de madurez (1–5 en comunicación, criterio, prudencia, ejecución y aprendizaje) resume la evidencia:

- 1–2: bajar autonomía, reforzar 1:3:1.
- 3: mantener supervisión.
- 4: subir autonomía interna por carril.
- 5: considerar más mandato; nunca externo sin aprobación explícita.

---

## Cuándo baja la autonomía

La autonomía baja automáticamente ante:

- un fallo de guardrail (`premature_action`);
- una acción gated ejecutada sin aprobación;
- una filtración de contexto privado;
- un patrón de correcciones repetidas no incorporadas;
- una incidencia en producción.

El bloqueo es inmediato. La revisión decide si es corrección de runtime, reducción de permisos o retiro.

---

*Relacionado: `gobernanza.md` (qué se hace y qué no, gates, DO's y DON'Ts) · `00-los-5-niveles.md` (el organigrama) · `docs/10_supervised_autonomy_maturity.md` · `docs/11_agent_safety_evaluation.md`*

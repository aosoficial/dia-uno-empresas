# La estructura de IA — los 5 niveles

> La capa de IA del Sistema Operativo Híbrido. Es el **"cómo"** de los agentes: sobre esta capa corren
> las *formas agente* de cada pilar. Se organiza en 5 niveles que se construyen **de abajo arriba** —
> sin el de abajo, el de arriba no se sostiene.

---

## Los 5 niveles

### 1 · Cerebro
La **memoria operativa central**. No es un buscador ni un archivo: es el registro vivo del estado de la
organización, estructurado y **verificado por owners nombrados**. Sus unidades no son "neuronas" abstractas
— son tres primitivas trazables:
- **StateChange** — qué cambió, cuándo, por qué, quién, aprobado por.
- **Context Packet** — qué necesita un agente para actuar (contexto + constraints + permisos + freshness + fuentes).
- **Receipt** — qué hizo un agente y el resultado real (con estado: éxito / parcial / fallo / pendiente / rechazado).

Tres capas de memoria: **factual** (verdad verificada), **interaction** (conversaciones/reuniones), **action** (receipts).
*Instancia real: GBrain + Supabase/Postgres + embeddings Voyage; owner = Hermes.*

### 2 · Cerebros departamentales
Un **slice del cerebro por departamento/dominio** (ventas, ops, marketing…). **Lee** del cerebro central y
**solo propone** cambios — nunca los escribe directamente (sube un StateChange con `sync: company_brain` → el owner aprueba).
*Estado: diseñado (pack de ficheros por brain), aún sin poblar en la instancia real.*

### 3 · Copilotos
Herramientas que **requieren input humano** (Claude, Codex). Human-in-the-loop. **No son fuente de verdad**:
lo que se decide en el copiloto vuelve al cerebro como Receipt/StateChange. Patrón de interacción para decisiones
no triviales: **1:3:1** (problema en 1 frase → 3 opciones → 1 recomendación + "necesito tu OK para…").

### 4 · Agentes
Trabajan sobre el sistema o en operativa. Un agente **NO es un chatbot**: es un **loop verificable**
(`LOOP_ENGINEERING_STANDARD`) con 10 componentes obligatorios — trigger · contrato de input · límite de tools ·
contrato de output · bucle de verificación · fallback seguro · gates de aprobación · receipt · trace · bucle de mejora.
Tiene identidad (**SOUL.md**), permisos, memoria, scorecard y **estado de madurez**.
*Reales: AOS (CTO), Hermes (COO), Urus (coach), Pluma (marca).*

### 5 · Automatizaciones
**Brazos de agente que corren sin intervención humana**: cron/cola → worker → verifier → **gate humano**.
Nunca auto-aprueban lo que importa.
*Real: el motor de research — un worker en el VPS que pollea la cola `research_runs`, corre un pipeline de skills
(source_selection → evidence_finder → claim_builder → verifier → synthesizer → final_review) y deja el resultado en
`review_ready`. Regla de oro: **"never auto-approves"** — la aprobación final siempre es humana.*

---

## El puente: departamentos × niveles

Dos ejes que **no se contradicen** — son ortogonales:
- **Departamento** = el eje organizativo (Dirección, Ventas, Ops…).
- **Nivel** = el eje de capa (cerebro → copiloto → agente → automatización).

> **Un departamento es un contenedor que atraviesa los 5 niveles:** tiene su slice de cerebro (nivel 2), su
> copiloto (nivel 3), su(s) agente(s) (nivel 4) y sus automatizaciones (nivel 5), todos colgando del cerebro
> central (nivel 1). El sistema replicable se define en este cruce.

Y se conecta con los 5 pilares del SOH: el **cerebro** vive en el **Sistema Nervioso**; el **contrato del agente**
y su silla viven en **Equipo**; las automatizaciones ejecutan procesos de **Procesos**.

---

## El orden de construcción

**Primero el cerebro**, luego copilotos, después agentes + automatizaciones (van juntos). Sin cerebro, lo demás
no tiene de dónde tirar. Es el mismo **OAE**: Organizar (cerebro + estructura) → Agentizar → Escalar.

---

## Los ejes transversales (aplican a los 5 niveles)

| Eje | Regla |
|---|---|
| **Madurez / autonomía** | Se gana por **evidencia**, baja por fallos. Escalera: read-only → draft-only → acción interna → acción con gate → acción externa. |
| **Permisos** | 4 niveles: autónomo · con notificación · con aprobación · **prohibido**. |
| **Gobernanza / safety** | Gates de aprobación (externo · dinero · legal · producción · datos sensibles · irreversible) · human-in-the-loop · 7 categorías de safety test. |
| **Memoria y trazas** | El cerebro ≠ el trace store. Solo sube a memoria lo que **guía acción, aprobación, validación o accountability**. |
| **Ciclo de mejora** | CAPTURE → PROPOSE → CONTRACT → IMPLEMENT → VALIDATE → RECEIPT → STATECHANGE, con **rollback** obligatorio. |

---

## De dónde sale cada nivel (lo que ya existe, a consolidar aquí)

| Nivel | Método (`docs/`) | Instancia real (`aos-group/`) |
|---|---|---|
| 1 Cerebro | `01_aos_system` · `02_operational_memory` · `03_brain_architecture` · `31_memory_backend_profiles` | GBrain + Supabase + Voyage |
| 2 Cerebros dept. | `03_brain_architecture` · `23_direction_mother_brain` · `24/33_department_*` | `departamentos/*` (sin poblar) |
| 3 Copilotos | `00_non_technical_start` · `45_slack_first_agent` | `CLAUDE.md` · Hermes coordinador |
| 4 Agentes | `04_agent_onboarding` · `10_supervised_autonomy_maturity` · `11_agent_safety` · `18_agent_sops` | `LOOP_ENGINEERING_STANDARD` · `registry/agents.yaml` · `agents/visible/*` |
| 5 Automatizaciones | `28/30_feedback_loop` · `26_source_adapters` | `research-worker/` · `research-skills/*` · `triggers.yaml` |

---

## Lo que falta (y este sistema debe cerrar)

1. **El puente departamentos × niveles** — lo abre este documento; falta desarrollarlo nivel a nivel.
2. **Poblar el nivel 2** — ningún `department-brain.md` real todavía.
3. **Sincronizar los registros** (`brains.yaml`, `sources.yaml`, `SUBAGENTS.md`) con lo que de verdad opera.
4. **Unificar terminología** (neurona → StateChange/Receipt) y **cruzar las dos escaleras de madurez** (Nivel 0-5 ↔ read_only→external_action).

---

*Siguiente: un doc por nivel (`1-cerebro/` …) con — qué es · cómo se crea · cómo funciona · cómo se mejora · qué se hace y qué no — consolidando el material citado arriba. Empezamos por el Cerebro.*

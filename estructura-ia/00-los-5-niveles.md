# La estructura de IA — el organigrama de IA

> La capa de IA del Sistema Operativo Híbrido. **Calca el organigrama humano de la empresa:** cada departamento
> tiene su propio trozo de IA, y todos cuelgan de un **cerebro** y un **coordinador** centrales. Sobre esta capa
> corren las *formas agente* de cada pilar del SOH.

---

## La arquitectura de un vistazo

```
              CEREBRO CENTRAL            ← la memoria de la empresa (copiloto de Dirección)
                    ▲  los cerebros de departamento sincronizan hacia aquí
              AGENTE COO                 ← coordina a todos los agentes de departamento
                    ▲  los agentes de departamento reportan hacia aquí
   ┌────────────────┼────────────────┐
   DEPARTAMENTO     DEPARTAMENTO     DEPARTAMENTO
   (Marketing)      (Ventas)         (Tecnología/Producto)
   ├ cerebro mkt    ├ cerebro ventas ├ cerebro cto       ← cada cerebro ES un copiloto
   ├ agente CMO     ├ agente ventas  ├ agente CTO        ← reporta al agente COO
   ├ subagentes     ├ subagentes     ├ subagentes
   └ automatizac.   └ automatizac.   └ automatizac.      ← cada una la posee (responde por ella) un agente
```

**Dos jerarquías paralelas, que reflejan el organigrama humano:**
- **Los cerebros suben** — cada cerebro de departamento sincroniza con el **cerebro central**.
- **Los agentes suben** — cada agente de departamento reporta al **agente COO**.

**Cada departamento es una columna vertical** con cuatro cosas: un **cerebro**, un **agente principal**, sus **subagentes** y sus **automatizaciones** (cada automatización la **posee y responde por ella** un agente).

---

## Las piezas

### Cerebro  *(central + uno por departamento)*
La **memoria**. Hay un **cerebro central** (la memoria de la empresa) y **un cerebro por departamento** (la memoria de ese departamento). Los de departamento **sincronizan hacia arriba** con el central — proponen, no escriben directamente. Sus unidades no son "neuronas" abstractas: son **StateChange** (qué cambió), **Context Packet** (qué necesita un agente para actuar) y **Receipt** (qué hizo y con qué resultado). Tres capas: factual · interaction · action.

### Copiloto  *(= el cerebro, usado de forma interactiva)*
**Cada cerebro es a la vez un copiloto.** El cerebro de marketing es un *copiloto de marketing*: lo usas para **ejecutar acciones** de ese departamento — consultarlo, pedirle que haga cosas, decidir con él. Es la cara **human-in-the-loop** del cerebro. No es una pieza aparte: es el cerebro en modo interactivo. Lo que se decide con el copiloto vuelve al cerebro como Receipt/StateChange (no es fuente de verdad por sí mismo).

### Agente  *(COO + un principal por departamento + subagentes)*
El trabajador autónomo — un **loop verificable** (`LOOP_ENGINEERING_STANDARD`), no un chatbot. Arriba, el **agente COO** coordina a todos. En cada departamento, un **agente principal** (con nombre de rol) más sus **subagentes**. Los agentes **reportan hacia arriba** (departamento → COO). Cada uno tiene identidad (SOUL), permisos, memoria, scorecard y estado de madurez.

### Automatizaciones  *(repartidas, poseídas por agentes)*
**Brazos que corren sin intervención humana.** Están **repartidas por los departamentos** y **cada una la posee un agente** — es su responsable: si falla, responde ese agente. Se modelan como cron/cola → worker → verifier → **gate humano**. Nunca auto-aprueban lo que importa.

---

## Nombres = roles, no personas

En el método —y en el organigrama de cualquier empresa— los agentes llevan **nombre de rol**, no nombre propio:

- **Agente COO** (operaciones, coordinación) · **Agente CTO** (tecnología/producto) · **Agente CMO** (marketing) · **Agente CFO** (finanzas) · **Agente de Ventas** · etc.
- Un alias propio es solo decoración de cada instancia; **lo que define el asiento es el rol**, no el nombre.
- Los agentes de **vida personal** (un coach, una marca personal) **no forman parte del OS de empresa** — viven fuera.

---

## El puente con los pilares del SOH

El **cerebro** vive en el **Sistema Nervioso**; el **contrato del agente** y su silla viven en **Equipo**; las **automatizaciones** ejecutan procesos de **Procesos**. El organigrama de IA es el mismo organigrama de **Equipo**, con asientos humanos y asientos-agente conviviendo.

## Los ejes transversales (aplican a todo)

| Eje | Regla |
|---|---|
| **Madurez / autonomía** | Se gana por **evidencia**, baja por fallos: read-only → draft-only → acción interna → acción con gate → acción externa. |
| **Permisos** | 4 niveles: autónomo · con notificación · con aprobación · **prohibido**. |
| **Gobernanza / safety** | Gates de aprobación (externo · dinero · legal · producción · datos sensibles · irreversible) · human-in-the-loop. |
| **Memoria y trazas** | El cerebro ≠ el trace store. Solo sube a memoria lo que **guía acción, aprobación, validación o accountability**. |
| **Ciclo de mejora** | CAPTURE → PROPOSE → CONTRACT → IMPLEMENT → VALIDATE → RECEIPT → STATECHANGE, con **rollback**. |

---

## El orden de construcción

**Primero el cerebro** (el central y el del primer departamento) → usarlo como **copiloto** → el **agente** del departamento + subagentes → las **automatizaciones**. Es el mismo **OAE**: Organizar (cerebro + estructura) → Agentizar → Escalar. Sin cerebro, lo demás no tiene de dónde tirar.

---

*Siguiente: un doc por pieza (`1-cerebro/` …) con — qué es · cómo se crea · cómo funciona · cómo se mejora · qué se hace y qué no. Empezamos por el Cerebro.*

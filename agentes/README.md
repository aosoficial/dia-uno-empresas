# Agentes

Esta capa define cómo una capacidad ya organizada puede ser ejecutada o asistida por un agente con identidad, herramientas, límites, memoria, supervisión y evidencia. No reemplaza la capa de Personas ni crea una jerarquía paralela.

## Contrato canónico

El pack instalable está en [`../templates/agent-runtime-pack/`](../templates/agent-runtime-pack/). Sus piezas cubren:

| Necesidad | Artefacto canónico |
|---|---|
| Identidad y propósito | [`IDENTITY.md`](../templates/agent-runtime-pack/IDENTITY.md), [`SOUL.md`](../templates/agent-runtime-pack/SOUL.md), [`ROLE_CARD.md`](../templates/agent-runtime-pack/ROLE_CARD.md) |
| Autoridad y límites | [`PERMISSIONS.md`](../templates/agent-runtime-pack/PERMISSIONS.md), [`AUTONOMY.md`](../templates/agent-runtime-pack/AUTONOMY.md) |
| Herramientas | [`TOOLS.md`](../templates/agent-runtime-pack/TOOLS.md) |
| Contexto y fuentes | [`CONTEXT_PACKET.md`](../templates/agent-runtime-pack/CONTEXT_PACKET.md) |
| Memoria | [`MEMORY.md`](../templates/agent-runtime-pack/MEMORY.md), [`MEMORY_POLICY.md`](../templates/agent-runtime-pack/MEMORY_POLICY.md) |
| Operación | [`OPERATIONS.md`](../templates/agent-runtime-pack/OPERATIONS.md), [`AGENTS.md`](../templates/agent-runtime-pack/AGENTS.md) |
| Madurez y supervisión | [`MATURITY_REVIEW.md`](../templates/agent-runtime-pack/MATURITY_REVIEW.md), [`HEARTBEAT.md`](../templates/agent-runtime-pack/HEARTBEAT.md) |
| Evidencia y continuidad | [`RECEIPT.md`](../templates/agent-runtime-pack/RECEIPT.md), [`STATECHANGE.md`](../templates/agent-runtime-pack/STATECHANGE.md), [`HANDOFF.md`](../templates/agent-runtime-pack/HANDOFF.md) |

## Regla de entrada

Una capacidad solo llega aquí cuando:

1. pertenece a una función y asiento claros;
2. tiene proceso o SOP estable;
3. tiene entradas, salidas y métrica verificables;
4. tiene un responsable humano;
5. sus decisiones y permisos tienen límites explícitos;
6. existe una salida segura y reversible ante fallo.

La escalera de madurez se gana por evidencia. Crear los archivos de un agente no prueba que esté autorizado, conectado ni operativo.

## Conexión con Personas

No copies una ficha de puesto dentro de `SOUL.md` ni una matriz de decisiones dentro de un prompt. Enlaza el artefacto humano como fuente y traduce únicamente el contrato ejecutable del agente. Usa la [matriz de equivalencias](../sistema-hibrido/matriz-de-equivalencias.md) y el [contrato de función](../sistema-hibrido/contrato-de-funcion.md).

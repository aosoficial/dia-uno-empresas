# MERGE_MAP — Método humano + sistema de agentes

Este mapa registra la integración ya realizada en el framework público. DIA UNO Empresas conserva una sola metodología con tres capas enlazadas:

```text
Personas                  Agentes                     Sistema Híbrido
organiza la función  ->   ejecuta capacidad madura -> gobierna función + ejecutor
```

La secuencia canónica es **Organizar personas → Agentizar capacidades maduras → Escalar el sistema híbrido**.

## Estructura canónica

| Área | Autoridad | Estado de la integración |
|---|---|---|
| [`personas/`](personas/README.md) | Metodología humana, teoría, plantillas e integridad de originales. | Integrada: Método V3 `36/36`. |
| [`agentes/`](agentes/README.md) | Entrada a los contratos y packs ejecutables ya existentes. | Enlazada; no se duplicaron packs. |
| [`sistema-hibrido/`](sistema-hibrido/README.md) | Función compartida, responsable humano, permisos y evidencia. | Integrada con contrato y matriz de equivalencias. |
| [`modelo/`](modelo/README.md) | Modelo conceptual universal: pilares, transversales y gramática. | Se conserva como marco, no como segunda metodología. |
| [`implementacion/`](implementacion/README.md) | Ruta Organizar → Agentizar → Escalar. | Actualizada a los dos modos de instalación. |
| `pilares/`, `transversales/`, `caja-de-herramientas/` | Vista conceptual y material existente. | Compatible; los originales V3 se preservan aparte. |
| `templates/generated-company-instance/` | Scaffold privado instalable. | Admite `people`, `hybrid` y upgrade no destructivo. |

## Equivalencias que evitan duplicación

| Fuente organizativa | Contrato agéntico | Regla |
|---|---|---|
| Ficha de puesto | identidad, role card y operaciones | El contrato traduce solo lo ejecutable y enlaza la fuente humana. |
| Matriz de decisiones | permisos, autonomía y gates | El agente nunca recibe más autoridad que el asiento. |
| SOP | operaciones, skills y tools | El SOP sigue siendo la fuente del proceso y conserva fallback. |
| Evaluación | scorecard y revisión de madurez | El cambio de autonomía requiere evidencia y revisión humana. |
| Indicadores y aprendizaje | scorecards, receipts, memoria y StateChanges | Solo se promueve evidencia revisada; no se inventa verdad operativa. |

El detalle vinculante está en [`sistema-hibrido/matriz-de-equivalencias.md`](sistema-hibrido/matriz-de-equivalencias.md).

## Compatibilidad y migración

- Las instalaciones históricas sin `METHOD.json` se validan como `hybrid` para mantener compatibilidad.
- Una instalación nueva puede empezar en `people` sin departamentos, empleados digitales, Slack o runtime.
- `--upgrade` añade scaffolds agénticos faltantes a una instancia `people` sin sobrescribir archivos existentes.
- Los 36 originales son inmutables y se copian byte por byte con [`MANIFEST.sha256`](personas/metodo-v3/MANIFEST.sha256).
- Generar carpetas prueba instalación e integridad, no implantación ni operación real.

## Rollback

El framework no borra ni revierte automáticamente una instancia privada. Para volver al uso humano, se mantiene `personas/` como fuente y los scaffolds agénticos permanecen inertes. Para retirada física, se restaura la copia privada previa al upgrade.

## Límites

Esta integración no activa agentes, servicios, credenciales, workers, integraciones ni infraestructura. Tampoco incorpora datos de una empresa concreta.

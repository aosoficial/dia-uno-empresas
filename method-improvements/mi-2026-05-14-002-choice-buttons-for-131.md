# MI-2026-05-14-002 — Botones para decisiones 1:3:1

```yaml
id: "mi-2026-05-14-002"
titulo: "Presentar 1:3:1 con botones/respuestas rápidas cuando el canal lo permita"
fecha: "2026-05-14"
owner: "repository maintainer"
origen: "Feedback directo de un operador en chat"
estado: "aplicado"
```

## Señal

Un operador eligió la opción A en una decisión 1:3:1 y señaló que le gusta el uso de botones en la elección.

## Interpretación

La interfaz de decisión afecta la calidad del loop de supervisión.

Botones o respuestas rápidas:

- reducen fricción;
- hacen más claro qué se está decidiendo;
- generan señales estructuradas para analizar madurez del agente;
- distinguen aceptación, elección alternativa y rechazo de opciones.

## Cambio aplicado

Añadido al método:

- `docs/10_supervised_autonomy_maturity.md`
- `templates/agent-runtime-pack/AUTONOMY.md`
- `CHANGELOG.md`

## Regla

Cuando el canal lo permita, una propuesta 1:3:1 debe presentarse como:

- A — opción conservadora;
- B — opción equilibrada;
- C — opción agresiva/exploratoria;
- Otra — el operador define una dirección no cubierta.

## Validación

Validado con:

- `python scripts/validate_repo.py`
- `python scripts/validate_schemas.py`
- `python scripts/build_docs.py`

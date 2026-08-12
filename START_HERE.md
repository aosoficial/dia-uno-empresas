# Empieza aquí / START HERE

Este repositorio sirve para organizar una empresa y, si procede, instalar una **instancia privada híbrida**. No tienes que empezar por agentes.

## Primero elige modo

### Modo `people`

Para una empresa que necesita aclarar Rumbo, personas, decisiones, procesos, caja, ejecución, indicadores, aprendizaje y reuniones. Instala solo la capa humana.

### Modo `hybrid`

Para una empresa que ya quiere preparar agentes sobre capacidades organizadas. Incluye la capa humana y los scaffolds agénticos; no activa nada.

En ambos modos el responsable final es humano. Consulta [`personas/README.md`](personas/README.md), [`agentes/README.md`](agentes/README.md) y [`sistema-hibrido/README.md`](sistema-hibrido/README.md).

Si vas a montar una empresa real, crea primero la instancia privada y organiza sus capacidades. Si después continúa a agentes desde **ORGO**, ORGO conecta Codex o Claude Code, prepara memoria privada y, en el guided path actual, configura Slack como interfaz del primer agente. Usa [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md) solo para esa segunda fase.

## Para Codex/Claude después de clonar desde ORGO

Si eres Codex, Claude Code u otro asistente lanzado desde ORGO: **toma la iniciativa como operador instalador**. No esperes a que el usuario te diga qué documento leer ni qué comando ejecutar.

Haz inmediatamente esto:

1. Lee [`AGENTS.md`](AGENTS.md), este `START_HERE.md`, [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md) y [`docs/00_non_technical_start_with_codex_or_claude.md`](docs/00_non_technical_start_with_codex_or_claude.md).
2. Explica al usuario el siguiente paso en lenguaje humano.
3. Haz el examen corto de nivel IA antes de pedir datos de empresa.
4. Usa comandos locales seguros para verificar el repo.
5. Pregunta si la empresa quiere empezar en modo `people` o `hybrid`. En ambos casos instala y trabaja primero la capa Personas.
6. Solo en modo `hybrid`, presenta después el plan de interfaz y herramientas del primer agente. Crear/configurar recursos externos requiere aprobación del usuario.
7. Pide aprobación solo antes de acciones externas, públicas, económicas, legales, productivas, sensibles, destructivas, con secretos o con workers/crons/bots persistentes.

Primer mensaje recomendado:

```text
DIA UNO está cargado. Yo guío la instalación desde aquí.
Primero revisaré las instrucciones del repo y tu nivel de uso de IA; después te diré el siguiente paso seguro.
No te pediré claves en el chat y pediré permiso antes de acciones externas, de pago, públicas, legales, de producción o sensibles.
```

No promete una transformación garantizada. Te ayuda a crear una base humana ordenada y, solo si procede, a preparar un primer agente acotado con límites, receipts y evidencia revisable.

## Antes de instalar: examen rápido de nivel IA

Si no eres técnico o vas a usar Codex/Claude Code como copiloto instalador, empieza aquí:

- [`docs/00_non_technical_start_with_codex_or_claude.md`](docs/00_non_technical_start_with_codex_or_claude.md)

Ese flujo hace primero un examen corto de nivel de IA y asigna uno de tres modos de guardrails:

1. **No técnico**: pasos exactos, guardrails fuertes y nada de claves en chat.
2. **Usuario IA intermedio**: opciones seguras y explicación breve de tradeoffs.
3. **Técnico / builder**: más autonomía, pero manteniendo límites en secretos, pagos, producción, legal y acciones públicas.

Antes de que exista el cerebro privado, no hace falta indagar en la persona ni en datos sensibles. Solo se debe saber su nivel de IA para tratarla bien y no darle demasiada libertad demasiado pronto.

## Si no eres técnico, sigue este camino primero

Usa el camino self-serve como una lista de pasos. La primera validación debe ser de **scaffold**: comprueba que la estructura está creada, no que la empresa ya opera como Punto B.

Si te bloqueas con Python, Make, `pyyaml`, permisos, carpeta no vacía o validaciones, abre primero [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

```bash
# 1) Simular sin crear nada
git clone https://github.com/aosoficial/dia-uno-empresas.git
cd dia-uno-empresas
python scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --method-mode people --output /tmp/mi-company-brain

# 2) Crear primero la capa humana. No se crean recursos externos.

# 3) Crear una instancia privada local
python scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --method-mode people --output /tmp/mi-company-brain --yes

# 4) Verificar que la instalación existe y tiene la estructura esperada
python scripts/verify_installation.py /tmp/mi-company-brain
python scripts/validate_people_readiness.py /tmp/mi-company-brain

# 5) Cuando la capacidad esté organizada, ampliar sin sobrescribir el trabajo humano
python scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --method-mode hybrid --output /tmp/mi-company-brain --upgrade --yes
python scripts/validate_point_b_readiness.py --mode scaffold /tmp/mi-company-brain
```

También puedes usar Make:

```bash
make validate
make demo-agency
make point-b-scaffold INSTANCE=/tmp/company-brain-demo-agency
```

## Importante: Punto B operativo no es el primer paso

En una instalación nueva, la validación operativa normalmente **fallará**. Eso es correcto.

El modo operativo (`--mode operational`, `make point-b` o `make point-b-operational`) solo debe ejecutarse después de completar un primer loop interno revisado por una persona, con una acción real segura y evidencia real: Context Packet, Receipt, scorecard y límites de aprobación actualizados.

No uses una validación operativa fresca para afirmar que la empresa ya está lista como Punto B.

## Qué rellenar primero

Rellena solo lo mínimo y seguro:

1. **Rumbo**: propósito, meta, valores, forma de ganar, caja y North Stars.
2. **Personas**: capacidades, asientos, fichas de puesto, decisiones y evaluación.
3. **Procesos**: mapa y SOP de las capacidades críticas.
4. **Operación humana**: caja, ejecución, indicadores, aprendizaje y reuniones.
5. **Gate de agentización**: responsable, inputs, output, métrica, autoridad, evidencia y fallback.
6. **Solo entonces ORGO + memoria + interfaz** para el primer agente.
7. **Primer agente**: una capacidad madura, estado `draft` o `pilot`, permisos mínimos.
8. **Primer Context Packet**: contexto suficiente para una acción interna pequeña.
9. **Primera acción interna**: redactar, analizar, ordenar o preparar; no enviar ni publicar.
10. **Receipt + Scorecard**: prueba de qué se hizo, quién revisó, qué cambió y siguiente sprint.

Para los pasos 5-10, sigue la guía detallada: [`templates/how-to/run-first-internal-loop.md`](templates/how-to/run-first-internal-loop.md).
Si no sabes qué acción elegir, usa ejemplos seguros en [`docs/44_first_operating_loop_examples.md`](docs/44_first_operating_loop_examples.md).

## Qué no debes pegar ni compartir

No pegues en este repo público, en ejemplos públicos ni en solicitudes de ayuda:

- secretos;
- credenciales;
- claves API;
- contraseñas;
- datos de clientes;
- contratos privados;
- datos regulados o personales sensibles;
- detalles de producción, despliegues, infraestructura o sistemas críticos.

Usa datos sintéticos o contexto anonimizado.

## Dónde pedir ayuda

Si te bloqueas, pide ayuda a **DIA UNO** en [diauno.io](https://diauno.io).

Antes de compartir nada, prepara un reporte seguro usando:

- [`templates/dia-uno/blocker-report.md`](templates/dia-uno/blocker-report.md)

Incluye solo contexto seguro o anonimizado: tipo de empresa, paso donde te bloqueaste, comando ejecutado, resultado, qué intentaste y qué evidencia existe. No incluyas secretos, datos de clientes ni contratos privados.

## Lecturas recomendadas

- [`README.md`](README.md) — visión general y comandos principales.
- [`docs/40_self_serve_happy_path.md`](docs/40_self_serve_happy_path.md) — camino self-serve paso a paso.
- [`docs/43_self_serve_operator_ux.md`](docs/43_self_serve_operator_ux.md) — checklist operativa para usuarios self-serve.
- [`docs/44_first_operating_loop_examples.md`](docs/44_first_operating_loop_examples.md) — ejemplos seguros de evidencia para agencia, consultoría y freelancer.
- [`docs/45_slack_first_agent.md`](docs/45_slack_first_agent.md) — cómo empezar a hablar con el primer agente por Slack.
- [`docs/48_observer_read_only_runtime.md`](docs/48_observer_read_only_runtime.md) — cómo crear Observer read-only con digest diario y escalación segura.
- [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md) — continuación híbrida desde una capacidad organizada hasta un primer agente supervisado.
- [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) — errores habituales y arreglos copy/paste.
- [`docs/12_get_help_from_dia_uno.md`](docs/12_get_help_from_dia_uno.md) — cómo pedir ayuda de forma segura.
- [`templates/generated-company-instance/README.md`](templates/generated-company-instance/README.md) — plantilla de instancia privada generada.

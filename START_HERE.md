# Empieza aquí / START HERE

Este repositorio sirve para instalar una **instancia privada de Company Brain**: el primer corte seguro de un sistema operativo AI-first para tu empresa.

Si vas a montar una primera empresa real desde **ORGO**, el camino correcto es: ORGO instala/conecta Codex o Claude Code, Codex/Claude carga este framework, prepara **Slack como primera interfaz operativa obligatoria para hablar con el primer agente**, prepara las herramientas base, crea la instancia privada de empresa, monta memoria privada con Supabase/Voyage/GBrain, crea el CEO agent y después los agentes de departamento. Usa [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md) como guía principal.

## Para Codex/Claude después de clonar desde ORGO

Si eres Codex, Claude Code u otro asistente lanzado desde ORGO: **toma la iniciativa como operador instalador**. No esperes a que el usuario te diga qué documento leer ni qué comando ejecutar.

Haz inmediatamente esto:

1. Lee [`AGENTS.md`](AGENTS.md), este `START_HERE.md`, [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md) y [`docs/00_non_technical_start_with_codex_or_claude.md`](docs/00_non_technical_start_with_codex_or_claude.md).
2. Explica al usuario el siguiente paso en lenguaje humano.
3. Haz el examen corto de nivel IA antes de pedir datos de empresa.
4. Usa comandos locales seguros para verificar el repo.
5. Para una empresa real, no saltes a agentes: primero presenta el plan mínimo de Slack y herramientas base. Slack es obligatorio para hablar con el primer agente; crear/configurar Slack es una acción externa y requiere aprobación del usuario.
6. Pide aprobación solo antes de acciones externas, públicas, económicas, legales, productivas, sensibles, destructivas, con secretos o con workers/crons/bots persistentes.

Primer mensaje recomendado:

```text
DIA UNO está cargado. Yo guío la instalación desde aquí.
Primero revisaré las instrucciones del repo y tu nivel de uso de IA; después te diré el siguiente paso seguro.
No te pediré claves en el chat y pediré permiso antes de acciones externas, de pago, públicas, legales, de producción o sensibles.
```

No promete una transformación garantizada. Te ayuda a crear una base ordenada para empezar con seguridad: Dirección / Mother Brain, límites de aprobación, contexto mínimo, un primer departamento, receipts y evidencia revisable.

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
python scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain

# 2) Antes de una empresa real: preparar Slack/herramientas base.
#    Slack es obligatorio para hablar con el primer agente.
#    Slack conecta directo a Hermes; no hay capa externa en la ruta base.
#    No se crean recursos externos desde el repo sin aprobación explícita.

# 3) Crear una instancia privada local
python scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain --yes

# 4) Verificar que la instalación existe y tiene la estructura esperada
python scripts/verify_installation.py /tmp/mi-company-brain

# 5) Validar primero en modo scaffold
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

1. **ORGO + Codex/Claude**: instala o conecta el operador instalador antes de tocar la empresa.
2. **Slack mínimo obligatorio**: prepara la superficie de conversación y aprobaciones para hablar con el primer agente. Slack es interfaz, no memoria. Slack conecta directo a Hermes.
3. **Memoria privada**: Supabase/Voyage/GBrain o estado explícito de pendiente si aún no se conectó.
4. **CEO agent**: primer agente, limitado a Dirección / Mother Brain.
5. **Dirección / Mother Brain**: visión, modelo, prioridades, criterios de decisión y límites de aprobación.
6. **Organigrama inicial de agentes**: CEO propone qué agentes de departamento hacen falta.
7. **Agentes de departamento**: cada agente entrevista solo su área: operaciones, marketing, growth/sales, producto/servicio, finanzas o postventa.
8. **Observer agent**: observa contradicciones, huecos, receipts y cambios que deben entrar al cerebro.
9. **Primer Context Packet**: contexto suficiente para una acción interna pequeña.
10. **Primera acción interna**: redactar, analizar, ordenar o preparar; no enviar ni publicar.
11. **Receipt + Scorecard**: prueba de qué se hizo, quién revisó, qué cambió y siguiente sprint.

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
- [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md) — flujo real ORGO → Codex/Claude → Slack → memoria → CEO → departamentos → Observer.
- [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) — errores habituales y arreglos copy/paste.
- [`docs/12_get_help_from_dia_uno.md`](docs/12_get_help_from_dia_uno.md) — cómo pedir ayuda de forma segura.
- [`templates/generated-company-instance/README.md`](templates/generated-company-instance/README.md) — plantilla de instancia privada generada.

# DIA UNO Empresas

Convierte una agencia, consultoría o negocio freelance en una empresa AI-First de servicios productizados: con Dirección / Cerebro Madre, departamentos, memoria operativa, empleados digitales, permisos, receipts y mejora continua.

DIA UNO Empresas es una aceleradora guiada para pasar de **Punto A** a **Punto B AI-First**.

**Primera vez aquí:** empieza por [`START_HERE.md`](START_HERE.md). En un piloto real desde ORGO, primero instala o conecta **Codex** o **Claude Code** como operador instalador; después sigue [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md). Si no eres técnico o vas a usar Codex/Claude Code como operador instalador, usa también [`docs/00_non_technical_start_with_codex_or_claude.md`](docs/00_non_technical_start_with_codex_or_claude.md): hace un examen corto de nivel IA, asigna guardrails y evita pedir datos sensibles antes de crear el cerebro privado. La primera instalación valida el scaffold privado; la validación operativa de Punto B viene después de un primer loop interno revisado con evidencia real. Si un comando falla, usa [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

**Para Codex/Claude desde ORGO:** este repo incluye [`AGENTS.md`](AGENTS.md). Tras clonar o abrir el repo, el asistente debe tomar la iniciativa: leer las instrucciones, explicar el siguiente paso en lenguaje humano, hacer el examen corto de nivel IA y pedir aprobación solo antes de acciones externas, públicas, económicas, legales, productivas, sensibles, destructivas o con secretos/workers/crons.

## Punto A

Empresa de servicios que no sabe por dónde empezar:

- conocimiento disperso;
- personas sin sistema operativo claro;
- procesos manuales;
- IA usada de forma puntual;
- sin brain por departamento;
- sin agentes integrados;
- sin memoria operativa ni feedback loop.

## Punto B

Empresa AI-First de servicios productizados con:

- Dirección / Cerebro Madre creado primero;
- departamentos definidos uno por uno;
- brain por departamento;
- sistema para guardar memoria operativa;
- comunicación entre humanos y agentes; en una primera empresa real empieza obligatoriamente por Slack para poder hablar con el primer agente;
- organización de personas y agentes;
- roles, permisos, límites y aprobaciones;
- skills por departamento;
- onboarding para agentes, departamentos y roles;
- receipts, statechanges, context packets y feedback loop;
- roadmap claro de 48h / 7 días / 30 días.

## Dos caminos

### 1. Evaluar el método

- [`docs/00_ai_first_company.md`](docs/00_ai_first_company.md) — Punto A → Punto B AI-First.
- [`docs/23_direction_mother_brain.md`](docs/23_direction_mother_brain.md) — Dirección / Cerebro Madre.
- [`docs/24_department_rollout_roadmap.md`](docs/24_department_rollout_roadmap.md) — roadmap 48h / 7d / 30d.
- [`docs/25_agency_consulting_freelance_vertical.md`](docs/25_agency_consulting_freelance_vertical.md) — vertical agencias, consultorías y freelancers.
- [`docs/26_source_adapters.md`](docs/26_source_adapters.md) — estrategia para adaptar fuentes externas.
- [`docs/27_human_agent_operating_system.md`](docs/27_human_agent_operating_system.md) — organización humano-agente.
- [`docs/28_feedback_loop.md`](docs/28_feedback_loop.md) — mejora continua.
- [`docs/39_guided_pilot_happy_path.md`](docs/39_guided_pilot_happy_path.md) — piloto guiado 30 / 60 / 120.
- [`docs/40_self_serve_happy_path.md`](docs/40_self_serve_happy_path.md) — camino self-serve.
- [`docs/41_guided_pilot_delivery_model.md`](docs/41_guided_pilot_delivery_model.md) — modelo de entrega del piloto.
- [`docs/42_point_b_definition.md`](docs/42_point_b_definition.md) — definición verificable de Punto B.
- [`docs/43_self_serve_operator_ux.md`](docs/43_self_serve_operator_ux.md) — UX operativa self-serve.
- [`docs/44_first_operating_loop_examples.md`](docs/44_first_operating_loop_examples.md) — ejemplos seguros para crear evidencia del primer loop.
- [`docs/45_slack_first_agent.md`](docs/45_slack_first_agent.md) — primer agente conversacional por Slack.
- [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md) — flujo real ORGO → Codex/Claude → Slack obligatorio → memoria → CEO/Dirección + Observer → departamentos.
- [`docs/48_observer_read_only_runtime.md`](docs/48_observer_read_only_runtime.md) — Observer read-only: vigilancia, digest diario, escalaciones y límites.

### 2. Generar una empresa privada guiada

```bash
python scripts/company_brain_wizard.py --dry-run --company "Acme Demo" --company-type agency --output /tmp/acme-company-brain
python scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --output /tmp/acme-company-brain --yes
python scripts/verify_installation.py /tmp/acme-company-brain
python scripts/validate_point_b_readiness.py --mode scaffold /tmp/acme-company-brain
# Solo después de un primer loop humano revisado con receipt real:
python scripts/validate_point_b_readiness.py --mode operational /tmp/acme-company-brain
```

También puedes usar:

```bash
make validate
make demo-agency
make point-b-scaffold INSTANCE=/tmp/company-brain-demo-agency
make point-b INSTANCE=/tmp/company-brain-demo-agency  # operational; requires real reviewed evidence
```

Si aparece `python: command not found`, `ModuleNotFoundError: No module named 'yaml'`, `make: command not found`, errores de permisos o confusión entre `scaffold` y `operational`, consulta [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) para soluciones copy/paste.

Para un bootstrap mínimo:

```bash
python scripts/bootstrap_company_brain.py --dry-run --company "Acme Demo" --company-type agency --output /tmp/acme-company-brain
```

## Orden de instalación para primera empresa real

1. ORGO instalado por el cliente.
2. ORGO instala/conecta Codex o Claude Code como operador instalador.
3. Codex/Claude abre o actualiza DIA UNO y sigue [`AGENTS.md`](AGENTS.md) sin esperar que el usuario le diga qué leer.
4. Se crea la instancia privada de empresa antes de hablar con agentes reales.
5. Memoria privada en Sprint 0: Supabase/Postgres, Voyage y GBrain/Company Brain. En instalaciones públicas/cliente de DIA UNO, GBrain es el repo upstream `https://github.com/garrytan/gbrain`. Verificar con `scripts/check_private_memory_readiness.py` o `make memory-preflight`. Contrato de conexiones/procesos: [`docs/47_private_memory_runtime_connections.md`](docs/47_private_memory_runtime_connections.md). Migración genérica revisable: `supabase/migrations/001_private_memory_runtime.sql`.
6. Slack obligatorio: workspace/canales mínimos y app creada con `hermes slack guide` / `hermes slack manifest --write`.
7. Conectar Slack directo a Hermes con `scripts/connect_slack_to_hermes.py`: instala/usa Hermes, crea el perfil, escribe tokens fuera de Git, verifica memoria, reinicia gateway y deja receipt privado.
8. Herramientas base necesarias para el primer loop. Slack conecta directo a Hermes; no hay capa externa de integración en la ruta base.
9. Primer agente: CEO, limitado a Dirección, accesible por Slack y escribiendo/leyendo memoria operativa.
10. Observer agent read-only para señales, contradicciones, receipts, StateChanges, runtime health, digest diario y escalaciones internas.
11. CEO entrevista Dirección y propone el organigrama inicial de agentes.
12. Agentes de departamento entrevistan sus propias áreas: operaciones, marketing, growth/sales, producto/servicio, finanzas y postventa.

## Qué incluye

- Company Brain y Department Brains.
- Wizard guiado para agencia, consultoría o freelancer.
- Department templates.
- Agent onboarding packs.
- Slack-first first agent guide.
- Skills por departamento.
- Roadmap 48h / 7d / 30d.
- Receipts, StateChanges y Context Packets.
- Trace policy y model strategy.
- Validadores de seguridad pública, instalabilidad y Point B readiness.

## Repo público vs instancia privada

```text
dia-uno-empresas/          framework público: docs, plantillas, scripts, validadores
private-company-instance/      empresa real: contexto, handoffs, receipts, statechanges
Hermes / ORGO / local runtime  agente operativo con herramientas y límites
```

Regla: los datos reales de empresa no viven en este repo público.

## Instalación rápida para desarrollo

```bash
git clone https://github.com/aosoficial/dia-uno-empresas.git
cd dia-uno-empresas
pip install pyyaml
python scripts/validate_repo.py
python scripts/validate_schemas.py
python scripts/build_docs.py
python scripts/validate_links.py
python scripts/validate_public_safety.py
python scripts/validate_installable_runtime.py
```

## Reglas de seguridad

Por defecto, los empleados digitales pueden redactar, analizar, preparar y operar localmente.

Piden aprobación antes de:

- contactar personas externas;
- publicar;
- gastar dinero;
- asumir compromisos legales o económicos;
- usar datos sensibles fuera de alcance;
- desplegar o cambiar producción;
- conectar nuevas herramientas críticas.

## Comunidad DIA UNO

Este repositorio es gratuito y útil por sí mismo. Si tu equipo se bloquea aplicándolo, DIA UNO puede ayudar a instalarlo: diagnóstico, Company Brain, departamentos, empleados digitales, permisos, cadencia operativa y adopción.

## Contribuir

Las contribuciones son bienvenidas: plantillas, ejemplos sintéticos, validadores, guías, pruebas de seguridad, mejoras del método y traducciones.

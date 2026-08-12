# DIA UNO Empresas

Organiza una empresa y, cuando sus capacidades estén maduras, permite agentizarlas con responsabilidad humana, permisos y evidencia. Una empresa puede usar únicamente la metodología para personas o continuar hasta un sistema híbrido.

DIA UNO Empresas sigue una secuencia: **Organizar personas → Agentizar capacidades maduras → Escalar el sistema híbrido**.

## Las tres capas

| Capa | Para qué sirve | Empieza aquí |
|---|---|---|
| **Personas** | Rumbo, asientos, puestos, decisiones, evaluación, procesos, SOP, caja, ejecución, indicadores, aprendizaje y reuniones. | [`personas/README.md`](personas/README.md) |
| **Agentes** | Contratos, identidad, permisos, herramientas, memoria, operaciones, madurez, supervisión y evidencia. | [`agentes/README.md`](agentes/README.md) |
| **Sistema Híbrido** | Une funciones y ejecutores, siempre con responsable humano, autoridad acotada y trazabilidad. | [`sistema-hibrido/README.md`](sistema-hibrido/README.md) |

Los 36 originales del Método V3 están preservados e inventariados en [`personas/metodo-v3/`](personas/metodo-v3/README.md). Los artefactos agénticos existentes no se duplican: se conectan mediante la [`matriz de equivalencias`](sistema-hibrido/matriz-de-equivalencias.md).

**Primera vez aquí:** empieza por [`START_HERE.md`](START_HERE.md). Crea primero una instancia `people` y organiza sus funciones. Si una capacidad madura continúa a agentes desde ORGO, instala o conecta **Codex** o **Claude Code** como operador y sigue [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md). Si no eres técnico, usa también [`docs/00_non_technical_start_with_codex_or_claude.md`](docs/00_non_technical_start_with_codex_or_claude.md). La primera instalación valida estructura e integridad; la validación operativa híbrida viene después de un loop interno revisado con evidencia real. Si un comando falla, usa [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

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

## Punto B híbrido

Empresa AI-First de servicios productizados con:

- Dirección / Cerebro Madre creado primero;
- departamentos definidos uno por uno;
- brain por departamento;
- sistema para guardar memoria operativa;
- comunicación entre humanos y agentes; en el guided path actual, Slack se prepara al lanzar el primer agente, no durante una instalación `people`;
- organización de personas y agentes;
- roles, permisos, límites y aprobaciones;
- skills por departamento;
- onboarding para agentes, departamentos y roles;
- receipts, statechanges, context packets y feedback loop;
- roadmap claro de 48h / 7 días / 30 días.

## Dos modos de instalación

### 1. Solo Personas

Instala la metodología humana sin departamentos, empleados digitales, Slack ni runtime:

```bash
python3 scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --method-mode people --output /tmp/acme-company --yes
python3 scripts/verify_installation.py /tmp/acme-company
python3 scripts/validate_people_readiness.py /tmp/acme-company
```

Esto crea un scaffold privado y copia los 36 originales. No demuestra que la empresa ya esté organizada.

### 2. Sistema Híbrido

Genera Personas + scaffolds agénticos, o amplía una instancia People existente:

```bash
python3 scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --method-mode hybrid --output /tmp/acme-company --yes

# Si /tmp/acme-company ya fue creada en modo people:
python3 scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --method-mode hybrid --output /tmp/acme-company --upgrade --yes
```

El upgrade añade archivos faltantes sin sobrescribir el trabajo humano. No activa agentes, servicios, integraciones ni infraestructura.

## Explorar el método

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
- [`docs/46_orgo_first_company_onboarding.md`](docs/46_orgo_first_company_onboarding.md) — continuación híbrida: Personas → capacidad madura → ORGO/Codex → memoria/interfaz → agente acotado → evidencia.
- [`docs/48_observer_read_only_runtime.md`](docs/48_observer_read_only_runtime.md) — Observer read-only: vigilancia, digest diario, escalaciones y límites.
- [`docs/49_three_layer_method.md`](docs/49_three_layer_method.md) — contrato Personas / Agentes / Sistema Híbrido.
- [`docs/50_people_first_installation.md`](docs/50_people_first_installation.md) — instalación People-first y upgrade no destructivo.
- [`examples/hybrid-method/README.md`](examples/hybrid-method/README.md) — ejemplo sintético de una función en las tres capas.

## Generar una empresa privada guiada

```bash
python scripts/company_brain_wizard.py --dry-run --company "Acme Demo" --company-type agency --method-mode hybrid --output /tmp/acme-company-brain
python scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --method-mode hybrid --output /tmp/acme-company-brain --yes
python scripts/verify_installation.py /tmp/acme-company-brain
python scripts/validate_people_readiness.py /tmp/acme-company-brain
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

## Orden de instalación para una empresa que continúa a agentes

1. Crear la instancia privada en modo `people` o `hybrid`.
2. Completar la capa Personas para la capacidad que se quiere agentizar.
3. Verificar responsable, SOP, entradas, salida, métrica, autoridad, evidencia y fallback.
4. Instalar ORGO y conectar Codex o Claude Code como operador cuando se decida continuar al runtime.
5. Preparar memoria privada: Supabase/Postgres, Voyage y GBrain/Company Brain. En instalaciones públicas/cliente de DIA UNO, GBrain es el repo upstream `https://github.com/garrytan/gbrain`. Verificar con `scripts/check_private_memory_readiness.py` o `make memory-preflight`.
6. En el guided path actual, preparar Slack y conectarlo a Hermes antes de conversar con el primer agente. Esta acción externa requiere aprobación.
7. Instalar las herramientas mínimas y permisos de mínimo privilegio.
8. Crear el primer agente en `draft` o `pilot`, limitado a una capacidad madura de Dirección.
9. Añadir Observer read-only si el alcance lo necesita.
10. Ejecutar un loop interno revisado, con Context Packet, Receipt y scorecard.
11. Crear agentes departamentales solo después de organizar y validar cada capacidad.

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

Si el bloqueo es definir quién responde, qué puede hacer cada agente, qué necesita aprobación y cómo se comprueba el resultado, empieza por [mapear la orquestación humano-agente](https://diauno.io/orquestacion-agentes-ia?utm_source=github&utm_medium=referral&utm_campaign=dia_uno_empresas&utm_content=readme_implementation_help) antes de conectar más herramientas.

## Contribuir

Las contribuciones son bienvenidas: plantillas, ejemplos sintéticos, validadores, guías, pruebas de seguridad, mejoras del método y traducciones.

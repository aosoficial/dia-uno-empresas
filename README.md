# Company Brain System

Convierte una agencia, consultoría o negocio freelance en una empresa AI-First de servicios productizados: con Dirección / Cerebro Madre, departamentos, memoria operativa, empleados digitales, permisos, receipts y mejora continua.

Company Brain System es una aceleradora guiada para pasar de **Punto A** a **Punto B AI-First**.

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
- comunicación entre humanos y agentes;
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

Para un bootstrap mínimo:

```bash
python scripts/bootstrap_company_brain.py --dry-run --company "Acme Demo" --company-type agency --output /tmp/acme-company-brain
```

## Orden de instalación

1. Dirección / Mother Brain.
2. Operations / Delivery.
3. Marketing.
4. Sales.
5. Customer Success / Postventa.
6. Product / Software Internal Systems.
7. Finance.
8. People / Organization.
9. Admin / Legal / Compliance where needed.

## Qué incluye

- Company Brain y Department Brains.
- Wizard guiado para agencia, consultoría o freelancer.
- Department templates.
- Agent onboarding packs.
- Skills por departamento.
- Roadmap 48h / 7d / 30d.
- Receipts, StateChanges y Context Packets.
- Trace policy y model strategy.
- Validadores de seguridad pública, instalabilidad y Point B readiness.

## Repo público vs instancia privada

```text
company-brain-system/          framework público: docs, plantillas, scripts, validadores
private-company-instance/      empresa real: contexto, handoffs, receipts, statechanges
Hermes / ORGO / local runtime  agente operativo con herramientas y límites
```

Regla: los datos reales de empresa no viven en este repo público.

## Instalación rápida para desarrollo

```bash
git clone https://github.com/aosoficial/company-brain-system.git
cd company-brain-system
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

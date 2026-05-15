# Company Brain System

Convierte el contexto de tu empresa en operaciones seguras con agentes de IA.

Company Brain System es un sistema práctico para equipos que quieren usar agentes de IA con contexto compartido, permisos claros, evidencia y aprobación humana cuando importa.

Sirve para pasar de prompts sueltos, chats y documentos dispersos a un cerebro de empresa sencillo que puedan usar tanto humanos como agentes.

Basado en AOS: Agentic Operating System.

---

## Empieza aquí

- **Quiero entenderlo rápido:** lee [`docs/07_quick_start.md`](docs/07_quick_start.md).
- **Quiero que un agente me ayude a instalarlo:** dale [`docs/14_agent_installation_process.md`](docs/14_agent_installation_process.md).
- **Quiero el método completo:** lee [`docs/00_master_playbook.md`](docs/00_master_playbook.md).
- **Quiero mapear mi empresa:** usa [`templates/questionnaires/company-brain-intake.md`](templates/questionnaires/company-brain-intake.md).
- **Quiero crear un rol de agente:** usa [`templates/agent-runtime-pack/README.md`](templates/agent-runtime-pack/README.md).
- **Estoy bloqueado:** lee [`docs/12_get_help_from_libera.md`](docs/12_get_help_from_libera.md) o abre un issue en GitHub.

## Por qué existe

La mayoría de sistemas con agentes de IA fallan por motivos simples:

- los agentes no conocen el contexto real de la empresa;
- los permisos no están claros;
- las acciones sensibles no se separan de las acciones seguras;
- las decisiones y cambios no quedan registrados;
- nadie puede verificar qué hizo realmente un agente;
- el método no mejora a partir del trabajo real.

Company Brain System te da una estructura para arreglar eso.

## Qué incluye

- **Company Brain:** la memoria compartida de la empresa.
- **Department Brains:** memorias enfocadas para ventas, operaciones, producto, finanzas, soporte y otras áreas.
- **Agent Runtime Packs:** archivos que definen quién es un agente, qué puede hacer, qué no puede hacer y cómo deja evidencia.
- **Registros operativos:** registros simples para contexto, cambios, traspasos y trabajo terminado.
- **Plantillas:** cuestionarios, scorecards, packs de agente, packs de departamento, revisiones y ejemplos.
- **Método de seguridad:** reglas de aprobación, revisión de permisos y pruebas de seguridad.
- **Scripts de validación:** comprobaciones básicas para mantener el repositorio consistente.

## Para quién es

- Fundadores que quieren construir empresas potenciadas por IA.
- Operadores que quieren que la IA sea útil más allá del chat.
- Consultores que implementan flujos de IA para clientes.
- Equipos que necesitan agentes con contexto, no improvisación.
- Equipos técnicos que quieren un método ligero antes de construir software.

## Qué no es

- No es un SaaS.
- No es un chatbot.
- No es un pack mágico de prompts.
- No sustituye el criterio humano.
- No es una base de datos de producción.

Es un método y una estructura de repositorio que puedes copiar, adaptar y operar.

## Instalación rápida

```bash
git clone https://github.com/aosoficial/company-brain-system.git
cd company-brain-system
pip install pyyaml
python scripts/validate_repo.py
python scripts/validate_schemas.py
```

Después lee:

1. [`docs/07_quick_start.md`](docs/07_quick_start.md)
2. [`docs/14_agent_installation_process.md`](docs/14_agent_installation_process.md)
3. [`docs/00_master_playbook.md`](docs/00_master_playbook.md)
4. [`docs/15_tools.md`](docs/15_tools.md)
5. [`docs/16_skills.md`](docs/16_skills.md)
6. [`docs/17_human_sops.md`](docs/17_human_sops.md)
7. [`docs/18_agent_sops.md`](docs/18_agent_sops.md)
8. [`templates/questionnaires/company-brain-intake.md`](templates/questionnaires/company-brain-intake.md)
9. [`templates/agent-runtime-pack/README.md`](templates/agent-runtime-pack/README.md)

## Camino práctico

### 1. Mapea la empresa

Empieza por lo básico:

- propósito;
- departamentos;
- personas y roles importantes;
- sistemas activos;
- decisiones clave;
- métricas;
- riesgos;
- permisos.

Usa: [`templates/questionnaires/company-brain-intake.md`](templates/questionnaires/company-brain-intake.md)

### 2. Crea el primer Company Brain

Empieza pequeño. No intentes mapear toda la empresa el primer día.

Usa:

- [`templates/context-packets/context-packet-template.md`](templates/context-packets/context-packet-template.md)
- [`templates/department-brain-pack/`](templates/department-brain-pack/)
- [`templates/scorecards/company-brain-scorecard.md`](templates/scorecards/company-brain-scorecard.md)

### 3. Añade un agente

Crea un rol de agente con:

- identidad;
- misión;
- herramientas permitidas;
- acciones prohibidas;
- reglas de aprobación;
- reglas de memoria;
- reglas de evidencia.

Usa: [`templates/agent-runtime-pack/`](templates/agent-runtime-pack/)

### 4. Haz que el trabajo sea verificable

Un agente no debería limitarse a decir “hecho”. Debe dejar evidencia de:

- qué hizo;
- por qué lo hizo;
- qué fuente usó;
- qué cambió;
- qué riesgos quedan;
- cómo se revisó el trabajo.

Usa: [`templates/receipts/receipt-template.md`](templates/receipts/receipt-template.md)

### 5. Mejora el método con trabajo real

Cuando algo falla, no arregles solo la tarea. Mejora el sistema.

Usa:

- [`templates/method-improvements/method-improvement-proposal.md`](templates/method-improvements/method-improvement-proposal.md)
- [`docs/09_method_improvement_loop.md`](docs/09_method_improvement_loop.md)

## Mapa del repositorio

```text
company-brain-system/
  docs/                         manuales del método
  templates/                    packs y plantillas reutilizables
  schemas/                      contratos YAML
  registry/                     registros de ejemplo
  examples/                     ejemplos sintéticos
  scripts/                      validación y construcción de docs
  method-improvements/          registro de aprendizaje del método
  .github/workflows/            validación automática
```

## Términos clave

- **Company Brain:** memoria operativa compartida de la empresa.
- **Department Brain:** memoria enfocada para un área.
- **Context Packet:** el contexto que necesita un agente antes de actuar.
- **StateChange:** registro de algo que ha cambiado.
- **Receipt:** evidencia de que una acción ocurrió y cómo se revisó.
- **Agent Runtime Pack:** contrato operativo de un agente.
- **Autonomía supervisada:** los agentes pueden actuar dentro de límites claros; las acciones sensibles necesitan aprobación.

Más definiciones: [`docs/08_glossary.md`](docs/08_glossary.md)

## Reglas de seguridad

Regla por defecto: los agentes pueden redactar, analizar, preparar y operar localmente.

No deberían hacer esto sin aprobación humana explícita:

- contactar clientes o leads;
- publicar externamente;
- gastar dinero;
- asumir compromisos legales o económicos;
- usar datos sensibles o privados fuera de alcance;
- desplegar a producción;
- cambiar sistemas vivos.

Lee: [`docs/11_agent_safety_evaluation.md`](docs/11_agent_safety_evaluation.md)

## Creado por Libera

Este repositorio es gratuito y útil por sí mismo.

Si tu equipo se bloquea aplicándolo, Libera puede ayudarte a instalarlo en una empresa real: diagnóstico, configuración del Company Brain, roles de agentes, permisos, cadencia operativa y adopción.

Por ahora, usa GitHub issues:

- **¿Necesitas ayuda de implementación?** Abre un issue titulado `Implementation help`.
- **¿Has encontrado un problema?** Abre un issue titulado `Bug` o `Question`.
- **¿Has mejorado una plantilla?** Abre un pull request.

Lee:

- [`docs/12_get_help_from_libera.md`](docs/12_get_help_from_libera.md)
- [`docs/13_libera_offer_map.md`](docs/13_libera_offer_map.md)

## Contribuir

Las contribuciones son bienvenidas:

- mejores plantillas;
- ejemplos más claros;
- nuevos packs de departamento;
- pruebas de seguridad;
- mejoras del método;
- traducciones;
- historias de implementación.

Abre un issue o pull request.

## Licencia

MIT. Ver [`LICENSE`](LICENSE).

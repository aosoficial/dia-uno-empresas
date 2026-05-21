# Method Improvement Proposal

## Cuándo usar esta plantilla

Usar cuando una señal de operación real deba convertirse en mejora del método, una plantilla, un schema, una skill, una rutina o un scorecard.

No usar para notas sueltas, preferencias temporales o errores únicos sin impacto.

---

## Propuesta

```yaml
id: "mi-[YYYY-MM-DD]-[NNN]"
titulo: "[COMPLETAR]"
fecha: "[YYYY-MM-DD]"
owner: "[operador/agente]"

origen:
  tipo: "[piloto privado / revisión operador / fuente externa / incidente / scorecard / rutina]"
  fuente: "[archivo, receipt, statechange, conversación aprobada o referencia]"
  privacidad: "[publicable / privado / requiere anonimización]"

senal_observada: >
  [Qué ocurrió. Debe ser observable, no una opinión vaga.]

problema_u_oportunidad: >
  [Qué falla o qué oportunidad reusable aparece.]

propuesta: >
  [Qué cambiar exactamente.]

capas_afectadas:
  docs: []          # Ej: docs/04_agent_onboarding.md
  templates: []     # Ej: templates/agent-runtime-pack/OPERATIONS.md
  schemas: []       # Ej: schemas/agent.schema.yaml
  skills: []        # Ej: service-ceo-consulting
  routines: []      # Ej: weekly review
  scorecards: []    # Ej: agent-evaluation-scorecard.md

aplicable_directamente: false
requiere_aprobacion: true
razon_aprobacion: "[si aplica]"

riesgos:
  - "[Qué puede salir mal si se aplica]"

anti_secret_review:
  contiene_datos_privados: false
  contiene_secretos: false
  requiere_anonimizacion: false

criterio_exito: >
  [Cómo sabremos que funcionó: menos retrabajo, menos preguntas repetidas,
  mejor receipt, menos bloqueos, mejor scorecard, etc.]

validacion:
  comandos: []
  evidencia: []

estado: "propuesta"  # propuesta / aplicada / rechazada / aparcada
```

---

## Decisión

- **Decisión:** [aplicar / pedir aprobación / aparcar / rechazar]
- **Razón:** [COMPLETAR]
- **Aplicado en:** [archivos/capas]
- **Pendiente:** [si algo queda fuera]
- **Receipt/StateChange:** [referencia]

---

## Errores comunes

1. **Confundir señal con solución.** “El agente falló” no basta. Hay que indicar qué cambió o qué regla faltaba.
2. **No listar capas afectadas.** Si solo actualizas docs pero no templates, el método se desincroniza.
3. **Meter datos privados en framework público.** Si viene de piloto real, anonimizar o mantener privado.
4. **No definir criterio de éxito.** Sin métrica, no sabemos si la mejora mejoró algo.

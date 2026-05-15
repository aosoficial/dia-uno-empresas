# 09 — Loop de Mejora del Método

> **Need help applying this?** This page is part of Company Brain System, an open method by Libera. If you get stuck, start with the [Quick Start](07_quick_start.md), use the [Company Brain intake](../templates/questionnaires/company-brain-intake.md), or see [how Libera can help](12_get_help_from_libera.md).

## Cómo Company Brain System aprende de la operación real

---

## Propósito

Este documento define el mecanismo formal para mejorar Company Brain System sin depender de prompts cada vez mejores ni de correcciones sueltas. El método mejora cuando la operación real produce feedback, ese feedback se convierte en propuestas, las propuestas se revisan y los cambios aprobados se aplican a documentación, plantillas, schemas, skills y rutinas.

La regla central es:

> **Los agentes no escalan por prompts perfectos. Escalan por loops de feedback revisados.**

---

## Cuándo se activa

Activar este loop cuando ocurra cualquiera de estas señales:

1. **Corrección humana repetida:** el operador corrige lo mismo más de una vez.
2. **Fallo de contexto:** un agente pregunta o asume algo que ya debía estar en memoria.
3. **Fallo de permiso:** un agente actúa sin aprobación o se bloquea aunque podía actuar.
4. **Fallo de handoff:** una tarea pasa entre agentes sin contexto suficiente.
5. **Fallo de outcome:** la tarea se completó, pero el resultado real no sirvió.
6. **Patrón de oportunidad:** una práctica funcionó bien y debería reutilizarse.
7. **Cambio de escala:** se añade un nuevo agente, brain, cliente, departamento o rutina.
8. **Feedback externo útil:** una fuente pública o privada aporta una regla práctica aplicable.

No activar el loop por gustos menores de redacción, preferencias temporales o errores únicos sin impacto.

---

## Qué puede cambiar

El loop puede producir cambios en cinco capas:

1. **Método:** docs principales de Company Brain System.
2. **Plantillas:** Runtime Packs, Context Packets, Receipts, StateChanges, scorecards.
3. **Schemas/registry:** campos obligatorios, estados, métricas, tipos de agente, permisos.
4. **Skills y operaciones:** procedimientos que usan agentes reales para ejecutar trabajo.
5. **Rutinas:** cron, heartbeats, revisiones, daily/weekly/monthly reviews.

Cada cambio debe indicar qué capa toca. Si toca varias, se aplica en todas o se deja explícitamente pendiente.

---

## Protocolo de mejora

```text
1. Capturar señal
   → ¿Qué pasó? ¿Dónde? ¿Con qué evidencia?

2. Clasificar
   → error, oportunidad, riesgo, fricción, nuevo patrón o cambio de escala.

3. Convertir en propuesta
   → usar templates/method-improvements/method-improvement-proposal.md.

4. Decidir tipo de cambio
   → seguro/aplicable directamente o sensible/requiere aprobación.

5. Aplicar en todas las capas necesarias
   → docs, templates, schemas, skills, rutinas, scorecards.

6. Validar
   → build/validación local, revisión anti-secretos y comprobación de consistencia.

7. Registrar evidencia
   → StateChange + Receipt con qué cambió, por qué y cómo se verificó.

8. Medir en la siguiente revisión
   → ¿redujo errores, preguntas repetidas, bloqueos o retrabajo?
```

---

## Gate de aprobación

### Cambios que el agente puede proponer y aplicar directamente

- Añadir una checklist más clara.
- Convertir una corrección humana en regla de Context Packet, Receipt o SOUL.
- Añadir campo no sensible a una plantilla.
- Actualizar una skill interna cuando el procedimiento real ya ha demostrado el cambio.
- Añadir métrica de evaluación basada en evidencia.
- Documentar una rutina ya aprobada.

### Cambios que requieren aprobación del operador

- Publicar material o empujarlo a un repo público.
- Cambiar permisos de agentes reales hacia más autonomía.
- Crear, eliminar o exponer canales/gateways.
- Tocar datos sensibles, credenciales, clientes reales o salud/finanzas personales.
- Cambiar pricing, compromisos comerciales, legal, compliance o acciones externas.
- Convertir material privado del piloto en framework público sin anonimización.

---

## Formato mínimo de propuesta

Cada mejora debe responder:

```yaml
id: mi-YYYY-MM-DD-001
origen: [piloto privado / revisión operador / fuente externa / incidente / scorecard]
señal: [qué se observó]
problema: [qué falla o qué oportunidad aparece]
propuesta: [qué cambiar]
capas_afectadas: [docs, templates, schemas, skills, routines, scorecards]
aplicable_directamente: true/false
requiere_aprobacion: true/false
riesgos: [qué podría salir mal]
evidencia: [receipts, statechanges, archivos, logs, revisión]
criterio_exito: [cómo sabremos que funcionó]
estado: propuesta | aplicada | rechazada | aparcada
```

---

## Relación con agentes

Cada agente operativo debe tener en su Runtime Pack una regla equivalente:

```text
Si el operador me corrige, no trato la corrección como un mensaje aislado.
Debo clasificarla:
- ¿actualiza memoria?
- ¿actualiza permisos?
- ¿actualiza operaciones?
- ¿actualiza SOUL?
- ¿propone una mejora al método Company Brain System?
```

Si la mejora es local del agente, se aplica en su pack/skill. Si es reusable para otros agentes, se propone al método.

---

## Métricas del loop

Medir al menos mensualmente:

- Correcciones humanas repetidas.
- Preguntas repetidas que ya tenían respuesta en memoria.
- Receipts sin outcome observado.
- Tareas bloqueadas que tenían fallback seguro.
- Handoffs sin Context Packet suficiente.
- Mejoras propuestas vs. aplicadas.
- Tiempo desde señal hasta cambio aplicado.
- Cambios aplicados que redujeron retrabajo.

---

## Antipatrones

| Antipatrón | Problema | Solución |
|------------|----------|----------|
| Mejorar solo el prompt | El error vuelve en otra sesión o agente | Convertir feedback en plantilla, skill, memoria o permiso |
| Aplicar cambios silenciosos | Nadie sabe por qué cambió el método | Registrar propuesta, StateChange y Receipt |
| Capturar todo como mejora | Se genera ruido y burocracia | Solo señales repetidas, riesgos u oportunidades reutilizables |
| Cambiar el framework con datos privados | Riesgo de exposición | Anonimizar y pedir aprobación antes de publicar |
| No medir después | No sabes si la mejora funcionó | Revisar la métrica afectada en la siguiente revisión |

---

## Checklist

- [ ] La señal tiene evidencia.
- [ ] La propuesta distingue problema, cambio y criterio de éxito.
- [ ] Se identificaron todas las capas afectadas.
- [ ] Se aplicó directamente solo si era seguro.
- [ ] Se pidió aprobación si tocaba permisos, exposición, datos sensibles o acción externa.
- [ ] Se actualizó documentación/template/skill/rutina necesaria.
- [ ] Se validó localmente.
- [ ] Se dejó StateChange y Receipt.
- [ ] Se programó revisión del resultado.

---

*Este documento convierte la mejora continua en sistema operativo, no en intención.*

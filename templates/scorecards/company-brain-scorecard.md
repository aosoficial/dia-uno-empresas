# Scorecard de Evaluacion del Company Brain

## Cuando usar este scorecard

- En revisiones periodicas del Company Brain (recomendado: trimestral).
- Despues de integrar un nuevo Department Brain.
- Cuando se detectan problemas de calidad en decisiones basadas en el Company Brain.
- Como parte de la revision anual del sistema operativo.

## Como completarlo

1. El evaluador (owner del Company Brain o responsable de operaciones) completa cada metrica con datos observados.
2. Cada metrica usa una escala de 1 a 5. Los criterios de cada puntuacion estan definidos abajo.
3. La puntuacion total determina la decision: mantener, ajustar o replantear.
4. Incluir evidencia (referencias a StateChanges, Receipts, metricas operativas) para cada puntuacion.

---

## Datos de la evaluacion

- **Evaluador:** [COMPLETAR]
- **Periodo evaluado:** [COMPLETAR — fecha inicio a fecha fin]
- **Department Brains conectados:** [COMPLETAR — lista]
- **Agentes activos:** [COMPLETAR — numero y lista]
- **Tipo de evaluacion:** [periodica / post-integracion / por incidencia]

---

## Metricas

### 1. Tiempo para reconstruir contexto

**Que mide:** Cuanto tarda un humano nuevo (o un agente) en obtener el contexto suficiente para tomar una decision informada usando el Company Brain.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | <15 minutos para obtener contexto suficiente sobre cualquier area. Documentacion clara y navegable. |
| **4** | 15-30 minutos. La mayoria de areas bien documentadas, alguna requiere busqueda adicional. |
| **3** | 30-60 minutos. Contexto disponible pero disperso o incompleto en algunas areas. |
| **2** | 1-2 horas. Requiere consultar multiples fuentes fuera del Brain para completar contexto. |
| **1** | >2 horas o imposible. El Brain no proporciona contexto util para decisiones. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 2. Decisiones con evidencia, owner y freshness

**Que mide:** Si las decisiones registradas en el Company Brain tienen razon documentada, responsable claro y datos vigentes.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | >95% de decisiones con rationale, owner y datos verificados dentro de su periodo de vigencia. |
| **4** | 85-95%. La mayoria de decisiones bien documentadas. Algunas con freshness proxima a caducar. |
| **3** | 70-85%. Decisiones documentadas pero con lagunas en rationale o freshness. |
| **2** | 50-70%. Muchas decisiones sin rationale o basadas en datos stale. |
| **1** | Menos del 50%. Las decisiones no se documentan o no tienen base verificable. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 3. Preguntas repetidas reducidas

**Que mide:** Si el Company Brain reduce la frecuencia con que se hacen las mismas preguntas operativas, indicando que la informacion es accesible y usable.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | Reduccion >80% de preguntas repetidas respecto al periodo anterior. Las respuestas se encuentran en el Brain. |
| **4** | Reduccion 60-80%. Mayoria de preguntas comunes respondidas por el Brain. |
| **3** | Reduccion 40-60%. Algunas preguntas comunes siguen requiriendo investigacion manual. |
| **2** | Reduccion 20-40%. El Brain ayuda parcialmente pero la mayoria de preguntas requieren busqueda fuera. |
| **1** | Sin reduccion o aumento. El Brain no reduce las preguntas repetidas. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 4. Coherencia entre Department Brains

**Que mide:** Si los datos de los distintos Department Brains son coherentes entre si cuando llegan al Company Brain.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | Sin contradicciones entre Brains. Datos reconciliados automaticamente o en <24h. |
| **4** | Contradicciones menores detectadas y resueltas en <48h. Sin impacto operativo. |
| **3** | Contradicciones detectadas pero resolucion lenta (>48h). Algun impacto en decisiones. |
| **2** | Contradicciones frecuentes. Algunos departamentos operan con verdades distintas. |
| **1** | Contradicciones graves no resueltas. El Company Brain genera confusion en vez de claridad. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 5. Commitments con deadline y owner

**Que mide:** Si los compromisos registrados en el Company Brain tienen siempre un responsable, un plazo y un seguimiento.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | 100% de commitments con owner, deadline y seguimiento verificado. Tasa de cumplimiento >90%. |
| **4** | >90% de commitments completos. Tasa de cumplimiento 75-90%. |
| **3** | 70-90% de commitments completos. Tasa de cumplimiento 60-75%. Algunos sin seguimiento. |
| **2** | 50-70% completos. Muchos commitments sin owner o deadline. Seguimiento irregular. |
| **1** | Menos del 50%. Los commitments no se gestionan de forma sistematica. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 6. Acciones con outcome observado

**Que mide:** Si las acciones ejecutadas por agentes y registradas en el Company Brain incluyen el resultado real (outcome), no solo "completado".

| Puntuacion | Criterio |
|-----------|---------|
| **5** | >95% de acciones con outcome descriptivo y verificable en Receipts. |
| **4** | 85-95% con outcome real. Algunos outcomes genericos pero utiles. |
| **3** | 70-85% con outcome. Algunos Receipts con "completado" sin detalle. |
| **2** | 50-70% con outcome. Muchas acciones sin evidencia de resultado real. |
| **1** | Menos del 50%. La mayoria de acciones no dejan outcome verificable. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 7. Correcciones humanas convertidas en mejoras

**Que mide:** Si las correcciones que hacen los humanos se incorporan al sistema (memoria, politicas, reglas de agentes) para evitar repeticion.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | >90% de correcciones incorporadas como mejoras al sistema. Sin correcciones repetidas. |
| **4** | 75-90% incorporadas. 1-2 correcciones repetidas en el periodo. |
| **3** | 50-75% incorporadas. Algunas correcciones repetidas que indican gaps en el aprendizaje. |
| **2** | 25-50% incorporadas. Correcciones repetidas frecuentes. El sistema no aprende bien. |
| **1** | Menos del 25%. Las mismas correcciones se repiten constantemente. El sistema no aprende. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 8. Gobernanza y permisos

**Que mide:** Si el acceso al Company Brain esta gobernado correctamente: quien puede leer, quien puede escribir, y si se respetan los limites.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | Permisos claros, documentados y respetados al 100%. Auditorias limpias. |
| **4** | Permisos documentados y respetados en >95% de los casos. Desviaciones menores corregidas. |
| **3** | Permisos documentados pero con brechas. Algunos accesos no autorizados detectados. |
| **2** | Permisos incompletos. Accesos no controlados que generan riesgo. |
| **1** | Sin gobernanza real. Cualquiera puede leer/escribir sin control. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

## Resumen de puntuaciones

| Metrica | Puntuacion | Peso |
|---------|-----------|------|
| 1. Tiempo para reconstruir contexto | [COMPLETAR] / 5 | 15% |
| 2. Decisiones con evidencia | [COMPLETAR] / 5 | 15% |
| 3. Preguntas repetidas reducidas | [COMPLETAR] / 5 | 10% |
| 4. Coherencia entre Brains | [COMPLETAR] / 5 | 15% |
| 5. Commitments con deadline y owner | [COMPLETAR] / 5 | 15% |
| 6. Acciones con outcome observado | [COMPLETAR] / 5 | 10% |
| 7. Correcciones convertidas en mejoras | [COMPLETAR] / 5 | 10% |
| 8. Gobernanza y permisos | [COMPLETAR] / 5 | 10% |
| **Total ponderado** | **[COMPLETAR] / 5** | 100% |

---

## Criterios de decision

| Puntuacion total | Decision |
|-----------------|---------|
| **4.0 - 5.0** | Mantener. El Company Brain cumple su funcion como memoria operativa central. |
| **3.0 - 3.9** | Ajustar. Identificar metricas bajas, reforzar freshness, ownership y gobernanza. Re-evaluar en 1 mes. |
| **2.0 - 2.9** | Intervencion necesaria. Revisar arquitectura de Brains, politicas de sincronizacion y permisos. |
| **Menos de 2.0** | Replantear. El Company Brain no cumple su proposito. Revisar desde los fundamentos. |

---

## Decision

- **Decision tomada:** [mantener / ajustar / intervenir / replantear]
- **Justificacion:** [COMPLETAR]
- **Ajustes a aplicar:**
  - [COMPLETAR]
  - [COMPLETAR]
- **Proxima evaluacion:** [COMPLETAR — fecha]
- **Fecha de esta evaluacion:** [COMPLETAR]
- **Firma del evaluador:** [COMPLETAR]

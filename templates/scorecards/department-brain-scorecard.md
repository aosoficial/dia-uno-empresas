# Scorecard de Evaluacion de Department Brain

## Cuando usar este scorecard

- Al final del primer mes de operacion de un Department Brain nuevo.
- En revisiones periodicas (recomendado: trimestral).
- Cuando se detectan problemas de calidad de datos o sincronizacion.
- Antes de conectar un Department Brain nuevo al Company Brain.

## Como completarlo

1. El evaluador (owner del departamento o administrador del Company Brain) completa cada metrica con datos observados.
2. Cada metrica usa una escala de 1 a 5. Los criterios de cada puntuacion estan definidos abajo.
3. La puntuacion total determina la decision: mantener, ajustar o reconstruir.
4. Incluir evidencia (referencias a StateChanges, Receipts, reportes) para cada puntuacion.

---

## Datos de la evaluacion

- **Department Brain evaluado:** [COMPLETAR]
- **Departamento:** [COMPLETAR]
- **Evaluador:** [COMPLETAR]
- **Periodo evaluado:** [COMPLETAR — fecha inicio a fecha fin]
- **Tipo de evaluacion:** [primer mes / revision periodica / evaluacion por incidencia]

---

## Metricas

### 1. Completitud de entidades

**Que mide:** Si el Brain contiene todas las entidades relevantes del departamento con sus campos obligatorios completos.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | >95% de entidades del departamento registradas con campos completos y verificados. |
| **4** | 85-95% de entidades registradas. Campos obligatorios completos en la mayoria. |
| **3** | 70-85% de entidades registradas. Algunos campos obligatorios vacios. |
| **2** | 50-70% de entidades. Lagunas significativas que afectan las operaciones. |
| **1** | Menos del 50%. El Brain no refleja la realidad del departamento. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 2. Freshness de datos

**Que mide:** Si los datos del Brain estan actualizados dentro de los plazos definidos por la politica de freshness del departamento.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | >95% de los datos dentro de su periodo de vigencia. Actualizaciones regulares. |
| **4** | 85-95% de datos vigentes. Retrasos menores en actualizaciones no criticas. |
| **3** | 70-85% de datos vigentes. Algunos datos criticos con freshness vencida. |
| **2** | 50-70% de datos vigentes. Datos stale que afectan decisiones operativas. |
| **1** | Menos del 50% vigente. El Brain es poco confiable como fuente de verdad. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 3. Calidad de senales

**Que mide:** Si el Brain detecta senales relevantes del departamento (riesgos, oportunidades, cambios) y las registra correctamente.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | Senales detectadas a tiempo, con contexto y priorizadas. Sin falsos positivos relevantes. |
| **4** | Mayoria de senales detectadas. Algun retraso o senal menor no capturada. |
| **3** | Senales detectadas de forma irregular. Algunas senales criticas se pierden. |
| **2** | Deteccion de senales pobre. Senales criticas frecuentemente perdidas o tardias. |
| **1** | Sin capacidad real de deteccion de senales. Reaccion solo ante problemas evidentes. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 4. Sincronizacion con Company Brain

**Que mide:** Si la informacion que debe subir al Company Brain se sincroniza correctamente y a tiempo.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | 100% de datos marcados para sincronizacion subidos correctamente y a tiempo. |
| **4** | 90-99% de sincronizacion exitosa. Retrasos menores sin impacto operativo. |
| **3** | 80-90% de sincronizacion. Algunos datos criticos no llegan al Company Brain a tiempo. |
| **2** | 60-80% de sincronizacion. Lagunas frecuentes que afectan la vision global. |
| **1** | Menos del 60%. El Company Brain no refleja la realidad de este departamento. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 5. Ownership y responsabilidad

**Que mide:** Si cada entidad y proceso del Brain tiene un owner claro, y si los owners mantienen sus areas.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | 100% de entidades con owner asignado. Owners actualizan sus areas proactivamente. |
| **4** | >90% con owner. La mayoria de owners mantienen sus areas al dia. |
| **3** | 70-90% con owner. Algunos owners no mantienen sus areas, requiriendo seguimiento. |
| **2** | 50-70% con owner. Muchas areas huerfanas o con owners que no actuan. |
| **1** | Menos del 50% con owner. No hay cultura de responsabilidad sobre los datos. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 6. Conflictos entre verdades locales

**Que mide:** Si se detectan y resuelven conflictos entre los datos de este Brain y otros Brains o el Company Brain.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | Sin conflictos, o conflictos detectados y resueltos en <24h con evidencia. |
| **4** | Conflictos menores resueltos en <48h. Sin conflictos recurrentes. |
| **3** | Conflictos resueltos pero con retraso. Algun conflicto recurrente. |
| **2** | Conflictos frecuentes o de resolucion lenta. Datos contradictorios entre Brains. |
| **1** | Conflictos graves no resueltos. Verdades contradictorias activas que generan decisiones incorrectas. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

### 7. Uso real por agentes y humanos

**Que mide:** Si el Brain se consulta y se usa realmente en las operaciones diarias, o si es decorativo.

| Puntuacion | Criterio |
|-----------|---------|
| **5** | Consultado diariamente por agentes y humanos. Base de decisiones operativas reales. |
| **4** | Consultado regularmente. Mayoría de decisiones operativas lo usan como referencia. |
| **3** | Consultado a veces. Algunas decisiones se toman sin consultarlo. |
| **2** | Rara vez consultado. La mayoria de decisiones se toman sin el Brain. |
| **1** | No se usa. Existe pero nadie lo consulta ni lo mantiene. |

**Puntuacion:** [COMPLETAR — 1 a 5]
**Evidencia:** [COMPLETAR]

---

## Resumen de puntuaciones

| Metrica | Puntuacion | Peso |
|---------|-----------|------|
| 1. Completitud de entidades | [COMPLETAR] / 5 | 20% |
| 2. Freshness de datos | [COMPLETAR] / 5 | 20% |
| 3. Calidad de senales | [COMPLETAR] / 5 | 15% |
| 4. Sincronizacion con Company Brain | [COMPLETAR] / 5 | 15% |
| 5. Ownership y responsabilidad | [COMPLETAR] / 5 | 10% |
| 6. Conflictos entre verdades | [COMPLETAR] / 5 | 10% |
| 7. Uso real | [COMPLETAR] / 5 | 10% |
| **Total ponderado** | **[COMPLETAR] / 5** | 100% |

---

## Criterios de decision

| Puntuacion total | Decision |
|-----------------|---------|
| **4.0 - 5.0** | Mantener. El Brain funciona correctamente. Conectar al Company Brain si no lo esta. |
| **3.0 - 3.9** | Ajustar. Identificar metricas bajas, asignar owners, mejorar freshness. Re-evaluar en 1 mes. |
| **2.0 - 2.9** | Intervencion necesaria. Reconstruir areas criticas, reforzar ownership, revisar politica de sincronizacion. |
| **Menos de 2.0** | Reconstruir. El Brain no cumple su funcion. Replantear desde las entidades y fuentes. |

---

## Decision

- **Decision tomada:** [mantener / ajustar / intervenir / reconstruir]
- **Justificacion:** [COMPLETAR]
- **Ajustes a aplicar:**
  - [COMPLETAR]
  - [COMPLETAR]
- **Proxima evaluacion:** [COMPLETAR — fecha]
- **Fecha de esta evaluacion:** [COMPLETAR]
- **Firma del evaluador:** [COMPLETAR]

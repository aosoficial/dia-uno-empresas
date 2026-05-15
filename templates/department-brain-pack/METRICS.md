# Métricas de Salud del Department Brain

## Qué es esto

Este archivo define las métricas que miden la salud de este Department Brain. Un cerebro sin métricas es un cerebro que no sabes si funciona.

Las métricas no miden el rendimiento del departamento (eso son KPIs del negocio). Miden la calidad y utilidad del cerebro como sistema de memoria.

---

## Métricas

### 1. Cobertura de entidades

- **Qué mide:** Porcentaje de entidades definidas que tienen datos registrados.
- **Fórmula:** (entidades con al menos 1 registro completo / total de entidades definidas) x 100
- **Objetivo:** [COMPLETAR — ejemplo: >90%]
- **Frecuencia de revisión:** [COMPLETAR — ejemplo: mensual]
- **Responsable:** [COMPLETAR]
- **Qué hacer si falla:** Identificar las entidades vacías. Si no hay datos, buscar fuentes. Si no hay fuentes, evaluar si la entidad debe eliminarse.

### 2. Cumplimiento de freshness

- **Qué mide:** Porcentaje de datos que están dentro de su plazo de verificación.
- **Fórmula:** (datos verificados dentro del plazo / total de datos con freshness asignada) x 100
- **Objetivo:** [COMPLETAR — ejemplo: >85%]
- **Frecuencia de revisión:** [COMPLETAR — ejemplo: semanal]
- **Responsable:** [COMPLETAR]
- **Qué hacer si falla:** Identificar los datos vencidos. Priorizar los de categoría "crítica". Verificar o marcar como stale.

### 3. Detección de señales

- **Qué mide:** Señales detectadas a tiempo vs. señales detectadas tarde o no detectadas.
- **Fórmula:** (señales detectadas dentro del plazo de respuesta / total de señales que ocurrieron) x 100
- **Objetivo:** [COMPLETAR — ejemplo: >80%]
- **Frecuencia de revisión:** [COMPLETAR — ejemplo: mensual]
- **Responsable:** [COMPLETAR]
- **Qué hacer si falla:** Revisar si las fuentes cubren los eventos. Revisar si los umbrales son realistas. Ajustar las condiciones de activación.

### 4. Precisión de sincronización

- **Qué mide:** Datos sincronizados con el Company Brain que resultaron correctos y oportunos.
- **Fórmula:** (sincronizaciones sin conflicto ni corrección posterior / total de sincronizaciones) x 100
- **Objetivo:** [COMPLETAR — ejemplo: >95%]
- **Frecuencia de revisión:** [COMPLETAR — ejemplo: mensual]
- **Responsable:** [COMPLETAR]
- **Qué hacer si falla:** Investigar los conflictos. Revisar la política de sincronización. Verificar que las fuentes del departamento son fiables.

### 5. Completitud de entidades

- **Qué mide:** Porcentaje de campos obligatorios completados en las entidades registradas.
- **Fórmula:** (campos obligatorios completos / total de campos obligatorios) x 100
- **Objetivo:** [COMPLETAR — ejemplo: >90%]
- **Frecuencia de revisión:** [COMPLETAR — ejemplo: mensual]
- **Responsable:** [COMPLETAR]
- **Qué hacer si falla:** Identificar los registros incompletos. Si faltan datos, buscarlos en las fuentes. Si las fuentes no los tienen, evaluar si el campo es realmente obligatorio.

### 6. Uso del cerebro

- **Qué mide:** Cuántas veces se consulta el cerebro por agentes o humanos en un período.
- **Fórmula:** Número de consultas por semana/mes
- **Objetivo:** [COMPLETAR — un cerebro que nadie consulta no sirve]
- **Frecuencia de revisión:** [COMPLETAR — ejemplo: mensual]
- **Responsable:** [COMPLETAR]
- **Qué hacer si falla:** Investigar por qué no se usa. Posibles causas: los agentes no lo necesitan, los datos no son fiables, es más fácil preguntar a una persona.

---

## Resumen del dashboard

| Métrica | Objetivo | Actual | Estado |
|---------|----------|--------|--------|
| Cobertura de entidades | [COMPLETAR]% | [COMPLETAR]% | [COMPLETAR] |
| Cumplimiento de freshness | [COMPLETAR]% | [COMPLETAR]% | [COMPLETAR] |
| Detección de señales | [COMPLETAR]% | [COMPLETAR]% | [COMPLETAR] |
| Precisión de sincronización | [COMPLETAR]% | [COMPLETAR]% | [COMPLETAR] |
| Completitud de entidades | [COMPLETAR]% | [COMPLETAR]% | [COMPLETAR] |
| Uso del cerebro | [COMPLETAR] consultas/mes | [COMPLETAR] | [COMPLETAR] |

**Estados posibles:** OK / Atención / Crítico

---

## Frecuencia de revisión

| Revisión | Frecuencia | Participantes | Qué se revisa |
|----------|-----------|---------------|---------------|
| Revisión rápida | Semanal | Owner del cerebro | Freshness y señales pendientes |
| Revisión completa | Mensual | Owner + operador | Todas las métricas + ajustes |
| Auditoría | Trimestral | Owner + operador + owners de datos | Cobertura, conflictos, entidades huérfanas |

---

## Ejemplo — Métricas del Sales Brain de Meridian Foods

| Métrica | Objetivo | Actual | Estado |
|---------|----------|--------|--------|
| Cobertura de entidades | >90% | 95% (19/20 entidades con datos) | OK |
| Cumplimiento de freshness | >85% | 78% (datos de 3 clientes vencidos) | Atención |
| Detección de señales | >80% | 85% (1 señal de churn detectada tarde) | OK |
| Precisión de sincronización | >95% | 100% (0 conflictos este mes) | OK |
| Completitud de entidades | >90% | 88% (faltan campos en 4 leads) | Atención |
| Uso del cerebro | >20 consultas/mes | 35 consultas | OK |

**Acción requerida:**
- Verificar datos de los 3 clientes con freshness vencida (prioridad: esta semana).
- Completar campos faltantes en los 4 leads (prioridad: antes de fin de mes).
- Investigar la señal de churn detectada tarde: revisar si la condición de activación es demasiado conservadora.

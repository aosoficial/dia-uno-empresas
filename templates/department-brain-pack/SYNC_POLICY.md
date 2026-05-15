# Política de Sincronización

## Qué es esto

Este archivo define qué información sube del Department Brain al Company Brain, qué se queda local, con qué frecuencia se sincroniza y cómo se resuelven los conflictos.

Sin política de sincronización, ocurren dos problemas opuestos: o el departamento opera en una burbuja (nada sube) o el Company Brain se convierte en un vertedero (todo sube).

---

## Qué sube al Company Brain

### Criterio general

Sube si cumple al menos una de estas condiciones:

1. **Afecta a más de un departamento.**
2. **Cambia una métrica global** (ingresos, churn, NPS, costes).
3. **Implica un compromiso con un actor externo** (cliente, socio, proveedor, regulador).
4. **Representa un riesgo para la empresa**, no solo para el departamento.
5. **Requiere una decisión del operador o CEO.**

### Señales que suben

| Señal | Condición | Formato | Frecuencia |
|-------|----------|---------|------------|
| [COMPLETAR] | [COMPLETAR — cuándo sube] | [StateChange / alerta / informe] | [por evento / diaria / semanal] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

### Datos que suben periódicamente

| Dato | Frecuencia | Formato | Owner |
|------|-----------|---------|-------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

---

## Qué se queda local

### Criterio general

Se queda local si cumple todas estas condiciones:

1. **Solo afecta a este departamento.**
2. **No cambia métricas globales.**
3. **No implica compromisos externos.**
4. **No representa un riesgo para la empresa.**
5. **No requiere decisión fuera del departamento.**

### Datos locales

| Dato | Por qué se queda local |
|------|----------------------|
| [COMPLETAR] | [COMPLETAR] |
| [COMPLETAR] | [COMPLETAR] |

---

## Qué se consume del Company Brain

| Dato | Para qué se usa | Frecuencia de consulta |
|------|----------------|----------------------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

**Regla:** el Department Brain puede leer del Company Brain pero nunca modificarlo directamente. Los cambios en el Company Brain se proponen mediante un StateChange etiquetado `sync: company_brain`, que el owner del dato en el Company Brain debe aprobar.

---

## Frecuencia de sincronización

| Tipo de sincronización | Frecuencia | Mecanismo |
|----------------------|-----------|-----------|
| **Señales críticas** | Inmediata (por evento) | StateChange + notificación al operador |
| **Señales de riesgo** | Máximo 24 horas | StateChange al final del día o al detectar |
| **Datos periódicos** | [COMPLETAR — diaria / semanal] | Reporte automático o resumen manual |
| **Métricas del departamento** | Semanal | Informe resumido al Company Brain |
| **Revisión completa** | Mensual | Auditoría de sincronización |

---

## Resolución de conflictos

### Cuándo hay conflicto

Cuando el Department Brain tiene un dato que contradice lo que dice el Company Brain. Ejemplo: el departamento de ventas registra un precio de 45 euros/mes, pero el Company Brain dice 49 euros/mes.

### Protocolo

1. **Detectar:** un agente o humano identifica la contradicción.
2. **Documentar:** se crea un StateChange de tipo `conflicto` con ambas versiones y sus fuentes.
3. **Escalar:** se notifica al owner del dato en el Company Brain y al owner del Department Brain.
4. **Resolver:** el owner del Company Brain decide cuál es la versión correcta.
5. **Actualizar:** se corrige el dato incorrecto mediante un StateChange.
6. **Notificar:** se avisa a todos los cerebros afectados.

**Regla fundamental:** en caso de conflicto, el Company Brain gana. El Department Brain debe alinearse con la verdad global.

### Prevención de conflictos

- Antes de registrar un dato que también existe en el Company Brain, verificar la versión del Company Brain.
- Si el departamento detecta que un dato del Company Brain está desactualizado, no corregirlo localmente — proponer el cambio al Company Brain.
- En la revisión mensual, comparar datos compartidos entre ambos cerebros.

---

## Ejemplo — Política de sincronización del Sales Brain de Meridian Foods

### Señales que suben

| Señal | Condición | Formato | Frecuencia |
|-------|----------|---------|------------|
| Cliente grande en riesgo de churn | Facturación >50k euros y señales de desvinculación | StateChange + alerta | Inmediata |
| Competidor baja precios | Confirmado por 2+ fuentes | StateChange + informe | 48 horas |
| Pipeline afecta MRR proyectado | Cambio >10% en pipeline mensual | Resumen | Semanal |
| Necesidad de producto nueva | 3+ clientes piden lo mismo | Señal al Product Brain | Semanal |

### Datos que suben periódicamente

| Dato | Frecuencia | Formato | Owner |
|------|-----------|---------|-------|
| Pipeline total por etapa | Semanal (lunes) | Resumen YAML | Carlos Martín |
| Tasa de conversión | Mensual | Métrica | Carlos Martín |
| Compromisos con deadline este mes | Semanal (lunes) | Lista | Comercial asignado |

### Datos locales

| Dato | Por qué se queda local |
|------|----------------------|
| Notas internas sobre negociaciones en curso | Solo afecta al equipo comercial |
| Borradores de propuestas no enviadas | Trabajo en progreso sin resultado confirmado |
| Objeciones individuales de un lead | Solo relevantes para el comercial asignado |
| Historial detallado de llamadas | Contexto de interacción, no dato global |

### Datos que consume del Company Brain

| Dato | Para qué se usa | Frecuencia de consulta |
|------|----------------|----------------------|
| Política de descuentos | Respetar límites al preparar propuestas | Cada vez que se prepara una propuesta |
| Catálogo de productos y precios | Incluir datos correctos en propuestas | Cada vez que se prepara una propuesta |
| Estructura del equipo | Saber a quién escalar o consultar | Cuando es necesario |
| Compromisos globales con clientes | No contradecir promesas hechas por otros departamentos | Antes de hacer compromisos nuevos |

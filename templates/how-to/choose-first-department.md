# Cómo elegir el primer departamento

Guía práctica para decidir qué departamento activar primero en tu instancia privada de Company Brain.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- `validate_point_b_readiness.py --mode scaffold` pasando;
- Dirección / Mother Brain rellenado con propósito, oferta y prioridades.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md) y completa los pasos 1-3.

## Lo que no debes hacer

- No actives todos los departamentos a la vez.
- No elijas el departamento "más bonito" o el que más te apetece automatizar.
- No empieces por un departamento donde no tengas owner humano claro.
- No empieces por un departamento donde el primer loop requiera contacto externo, datos sensibles o aprobación legal/económica.

## Criterios de decisión

Usa esta tabla para puntuar cada departamento candidato. No necesitas una puntuación numérica exacta; basta con "alto / medio / bajo" para cada criterio.

| Criterio | Pregunta clave | Por qué importa |
|---|---|---|
| Cuello de botella | ¿Dónde se pierde más tiempo o se repiten errores? | El primer loop debe resolver un dolor real, no un problema teórico. |
| Frecuencia | ¿Se repite al menos 1 vez por semana? | Un proceso frecuente genera evidencia rápida para el scorecard. |
| Owner humano | ¿Hay una persona concreta que pueda revisar el resultado? | Sin revisor humano, no hay Receipt válido ni loop cerrado. |
| Riesgo bajo | ¿El primer loop puede ser solo interno (redactar, analizar, ordenar)? | El primer loop no debe requerir acción externa, económica o legal. |
| Evidencia disponible | ¿Existen datos, documentos o fuentes verificables hoy? | Sin fuentes, el Context Packet será placeholder y el loop no cuenta. |
| Impacto visible | ¿El equipo notará la mejora en la primera semana? | Un resultado visible genera confianza para seguir con el sistema. |

## Departamentos disponibles

El wizard soporta estos departamentos. Dirección siempre se instala primero y no cuenta como "primer departamento operativo":

| Departamento | Cuándo elegirlo primero | Ejemplo de primer loop seguro |
|---|---|---|
| `operations-delivery` | Entregas repetitivas con errores frecuentes o pasos manuales. | Redactar checklist de entrega estándar. |
| `sales` | Pipeline manual, propuestas repetidas o seguimiento inconsistente. | Preparar borrador de propuesta con datos sintéticos. |
| `marketing` | Contenido sin proceso, campañas sin checklist o métricas dispersas. | Crear calendario editorial del próximo mes. |
| `customer-success` | Onboarding desordenado o seguimiento post-venta sin sistema. | Generar checklist de onboarding para nuevo cliente. |
| `finance` | Facturación manual, control de costes disperso o cierres lentos. | Clasificar gastos del mes en categorías estándar. |
| `product-software` | Backlog caótico, sin priorización clara o releases sin checklist. | Ordenar backlog por impacto y esfuerzo. |
| `people` | Contratación sin proceso o evaluaciones informales. | Crear plantilla de evaluación trimestral. |
| `admin-legal` | Contratos sin seguimiento o cumplimiento sin checklist. | Inventariar contratos activos con fechas de renovación. |

## Proceso de decisión paso a paso

### Paso 1 — Lista tus candidatos

Escribe los 2-3 departamentos que más dolor generan hoy. No más de 3.

### Paso 2 — Puntúa cada uno

Para cada candidato, responde los 6 criterios (alto / medio / bajo):

```
Candidato: _______________
- Cuello de botella:    alto / medio / bajo
- Frecuencia:           alto / medio / bajo
- Owner humano:         sí / no
- Riesgo bajo:          sí / no
- Evidencia disponible: sí / no
- Impacto visible:      alto / medio / bajo
```

### Paso 3 — Descarta los que no cumplen mínimos

Descarta cualquier candidato donde:

- **Owner humano** = no → no hay quién revise el Receipt.
- **Riesgo bajo** = no → el primer loop no puede requerir acción externa.
- **Evidencia disponible** = no → el Context Packet será placeholder.

### Paso 4 — Elige entre los que quedan

Si queda más de uno, elige el que tenga:

1. Mayor cuello de botella (resuelve más dolor).
2. Mayor frecuencia (genera evidencia más rápido).
3. Mayor impacto visible (gana confianza del equipo).

En caso de empate, elige el más pequeño y controlable. El objetivo es cerrar un loop completo, no transformar el departamento más grande.

### Paso 5 — Confirma con la regla de seguridad

Antes de continuar, verifica:

> ¿Puedo ejecutar un primer loop en este departamento que solo redacte, analice, ordene o prepare, sin contactar a nadie externo, sin gastar dinero y sin tocar producción?

Si la respuesta es sí, continúa. Si no, elige otro candidato.

## Ejemplo sintético — Agencia "Sol Digital"

Sol Digital tiene 3 personas. Sus departamentos con más dolor:

| Candidato | Cuello de botella | Frecuencia | Owner | Riesgo bajo | Evidencia | Impacto |
|---|---|---|---|---|---|---|
| operations-delivery | alto (errores en entregas) | alto (semanal) | sí (Ana) | sí | sí (retrospectivas) | alto |
| sales | medio (propuestas lentas) | medio (mensual) | sí (Carlos) | sí | parcial | medio |
| marketing | bajo (no es urgente) | medio | no (nadie asignado) | sí | no | bajo |

**Marketing descartado:** no tiene owner humano ni evidencia disponible.

**Decisión:** `operations-delivery` gana por mayor cuello de botella, frecuencia e impacto.

**Verificación de seguridad:** Ana puede ejecutar un primer loop que solo redacte una checklist de entrega sin contactar clientes. ✅

**Siguiente paso:** seguir con [`templates/how-to/run-first-internal-loop.md`](run-first-internal-loop.md).

## Después de elegir

1. Completa el `department-brain.md` del departamento elegido: [`complete-department-brain.md`](complete-department-brain.md).
2. Crea el mapa de fuentes de verdad si no lo tienes: [`create-source-of-truth-map.md`](create-source-of-truth-map.md).
3. Crea al menos un empleado digital con `PERMISSIONS.md`: [`create-first-digital-employee.md`](create-first-digital-employee.md).
4. Sigue la guía del primer loop interno: [`run-first-internal-loop.md`](run-first-internal-loop.md).

## Errores comunes

| Error | Por qué falla | Solución |
|---|---|---|
| Elegir Dirección como "primer departamento" | Dirección ya se instala siempre; no cuenta como loop operativo. | Elige un departamento funcional: delivery, ventas, etc. |
| Activar 3+ departamentos a la vez | Dispersión: ninguno tendrá evidencia suficiente para cerrar el loop. | Elige uno. Añade el siguiente después del primer Receipt. |
| Elegir el departamento "más IA" | La IA es una herramienta, no el criterio. | Elige por dolor, frecuencia y evidencia. |
| No tener owner humano | Sin reviewer, el Receipt no tiene verificación. | Asigna un owner antes de instalar el departamento. |
| Primer loop requiere enviar algo | Rompe la regla de seguridad del primer loop. | Elige una acción 100% interna. |

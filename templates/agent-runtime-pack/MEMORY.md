# Memory — Memoria de Trabajo del Agente

## Estado actual de lo que el agente sabe y recuerda

---

## Que es

MEMORY.md es la memoria de trabajo activa del agente. Contiene los hechos, relaciones, decisiones recientes y estado actual que el agente necesita para operar sin tener que reconstruir contexto desde cero en cada sesion.

**No es un log ni un historico.** Es un snapshot vivo de lo que el agente necesita saber ahora.

La diferencia con MEMORY_POLICY.md: la politica define las reglas (que puede recordar, cuanto tiempo, donde). MEMORY.md contiene los datos reales.

## Cuando usarlo

- Al inicio de cada sesion del agente (para cargar contexto).
- Al final de cada sesion (para guardar lo aprendido).
- Al traspasar el agente a otro operador (como parte del contexto transferido).
- Al diagnosticar por que el agente tomo una decision (revisar que sabia en ese momento).

---

## Estructura de la memoria

```markdown
## Hechos activos

Datos verificados que el agente necesita para operar. Cada hecho tiene
fecha de verificacion y fuente.

| Hecho | Valor | Verificado | Fuente | Caduca |
|-------|-------|------------|--------|--------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR — fecha] | [COMPLETAR] | [COMPLETAR — fecha o "sin caducidad"] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

## Decisiones recientes

Decisiones tomadas en el periodo actual que afectan al comportamiento
del agente o al estado del sistema.

| Decision | Fecha | Tomada por | Razon | Afecta a |
|----------|-------|------------|-------|----------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

## Tareas en curso

Tareas activas que el agente esta gestionando.

| Tarea | Estado | Deadline | Prioridad | Ultimo avance |
|-------|--------|----------|-----------|---------------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

## Relaciones activas

Entidades con las que el agente esta interactuando activamente.

| Entidad | Tipo | Estado de la relacion | Ultimo contacto |
|---------|------|----------------------|-----------------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

## Alertas y pendientes

Items que requieren atencion del agente o del operador.

| Alerta | Prioridad | Desde | Accion requerida |
|--------|-----------|-------|------------------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

## Correcciones aprendidas

Correcciones del operador que el agente debe recordar para no repetir errores.

| Correccion | Fecha | Contexto | Que hacer diferente |
|------------|-------|----------|---------------------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
```

---

## Ejemplo — Memoria de Vega (Meridian Foods)

```markdown
## Hechos activos

| Hecho | Valor | Verificado | Fuente | Caduca |
|-------|-------|------------|--------|--------|
| Precio Plan Business | 12.000 EUR/ano | 2026-04-01 | Product Brain | 2026-07-01 |
| Precio Plan Enterprise | 24.000 EUR/ano | 2026-04-01 | Product Brain | 2026-07-01 |
| Descuento maximo autonomo | 15% | 2026-05-01 | SOUL.md / PERMISSIONS.md | sin caducidad |
| Competidor principal | FreshTrack | 2026-04-20 | Evento FoodTech | 2026-08-01 |
| Contacto Costa Frutas | Ana Gomez, ana.gomez@costafrutas.com | 2026-05-05 | Email directo | sin caducidad |

## Decisiones recientes

| Decision | Fecha | Tomada por | Razon | Afecta a |
|----------|-------|------------|-------|----------|
| Ofrecer modulo reporting gratis en vez de descuento extra | 2026-05-12 | agente/vega (propuesta) | Coste menor que descuento (1.200 vs 2.160 EUR) | Propuesta Costa Frutas |
| Descartar lead GreenPack SL | 2026-04-20 | Carlos Ruiz (operador) | Sin fit con producto actual | Pipeline |

## Tareas en curso

| Tarea | Estado | Deadline | Prioridad | Ultimo avance |
|-------|--------|----------|-----------|---------------|
| Propuesta Costa Frutas | Pendiente aprobacion de descuento | 2026-05-14 | Alta | Handoff a Carlos para aprobar descuento |
| Seguimiento leads FoodTech | 2 de 3 enviados | 2026-05-15 | Media | Email OliFresh pendiente (email invalido) |
| Actualizar catalogo precios Q2 | No iniciada | 2026-05-20 | Baja | Esperando datos de Product Brain |

## Relaciones activas

| Entidad | Tipo | Estado de la relacion | Ultimo contacto |
|---------|------|----------------------|-----------------|
| Costa Frutas S.L. | Cliente potencial | Propuesta en preparacion | 2026-05-05 |
| Verde Campo S.L. | Lead nuevo | Seguimiento post-evento | 2026-05-06 |
| Frutas del Norte | Lead nuevo | Seguimiento post-evento | 2026-05-06 |
| OliFresh | Lead nuevo | Bloqueado (email invalido) | 2026-05-06 |

## Alertas y pendientes

| Alerta | Prioridad | Desde | Accion requerida |
|--------|-----------|-------|------------------|
| Email OliFresh invalido | Media | 2026-05-06 | Buscar email correcto via LinkedIn |
| 4 Receipts sin verificar | Media | 2026-05-09 | Operador debe revisar |
| Precios Q2 no confirmados | Baja | 2026-05-07 | Verificar con Product Brain cuando publique |

## Correcciones aprendidas

| Correccion | Fecha | Contexto | Que hacer diferente |
|------------|-------|----------|---------------------|
| No enviar email fuera de horario | 2026-04-15 | Envie seguimiento a las 20:30 | Respetar ventana 9-18h siempre |
| Incluir tabla comparativa | 2026-04-22 | Propuesta sin comparacion con competencia | Siempre incluir comparativa cuando hay competidor activo |
```

---

## Reglas de mantenimiento

```markdown
## Reglas de mantenimiento de la memoria

1. **Actualizar al final de cada sesion.** Los hechos nuevos, decisiones
   y cambios de estado deben reflejarse antes de cerrar sesion.

2. **Verificar freshness.** Revisar las fechas de caducidad.
   Los hechos caducados deben reverificarse o eliminarse.

3. **No acumular indefinidamente.** La memoria de trabajo no es un archivo.
   Tareas completadas pasan a Receipts. Hechos obsoletos se eliminan.

4. **Separar hechos de opiniones.** Solo registrar hechos verificados
   con fuente y fecha. Las hipotesis van a notas internas, no a memoria.

5. **Sincronizar con los Brains.** La memoria de trabajo debe ser coherente
   con los datos de los Brains que el agente consulta. Si hay discrepancia,
   verificar cual es correcto y actualizar.
```

---

## Errores comunes

1. **Memoria vacia al inicio.** Si MEMORY.md esta en blanco cuando el agente arranca, pierde todo el contexto acumulado. Debe cargarse con los datos relevantes antes de cada sesion.

2. **Memoria que solo crece.** Si nunca se eliminan hechos caducados ni tareas completadas, la memoria se convierte en ruido. Mantener solo lo activo y relevante.

3. **Hechos sin fecha de verificacion.** Un hecho sin fecha puede tener 6 meses de antiguedad. Sin freshness, el agente usa datos potencialmente obsoletos como si fueran vigentes.

4. **Confundir MEMORY.md con log de actividad.** El log va a Receipts y StateChanges. MEMORY.md es el estado actual, no el historico.

5. **No registrar correcciones aprendidas.** Si el operador corrige al agente pero el agente no lo recuerda en la siguiente sesion, cometara el mismo error. Las correcciones son parte critica de la memoria.

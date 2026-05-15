# Department Brain Pack

## Qué es

Un Department Brain Pack es el conjunto completo de documentos que definen la memoria operativa de un departamento. Es el equivalente departamental del Company Brain: una fuente de verdad local, estructurada y mantenida, que permite a agentes y humanos operar con contexto verificado.

## Qué contiene

```text
department-brain-pack/
  BRAIN_IDENTITY.md    ← Identidad del cerebro: nombre, departamento, owner, alcance
  ENTITIES.md          ← Catálogo de entidades que rastrea este cerebro
  SOURCES.md           ← Fuentes de datos: de dónde viene la información
  SIGNALS.md           ← Señales que monitoriza: qué eventos importan
  SYNC_POLICY.md       ← Política de sincronización con el Company Brain
  METRICS.md           ← Métricas de salud del cerebro
```

## Cuándo crear uno

Crea un Department Brain Pack cuando:

- Un departamento o área funcional tiene entidades, datos o decisiones propias que no pertenecen al Company Brain.
- Más de un agente necesita consultar datos de ese departamento.
- Se necesita definir qué información es local y qué sube al Company Brain.

No crees un Department Brain Pack cuando:

- El departamento tiene menos de 5 entidades — probablemente basta con una sección del Company Brain.
- No hay agentes ni humanos que vayan a consultar ese cerebro de forma recurrente.
- La información es exclusivamente temporal — en ese caso, usa un Project Brain.

## Relación con el Company Brain

```text
Company Brain
  │
  │  ↓ Baja: decisiones estratégicas, políticas globales, datos compartidos
  │  ↑ Sube: señales que afectan a toda la empresa
  │
  └── Department Brain
        Memoria local del departamento.
        Lee del Company Brain, pero no lo modifica directamente.
        Propone cambios al Company Brain cuando detecta señales relevantes.
```

**Regla fundamental:** el Department Brain puede leer del Company Brain pero nunca modificarlo directamente. Los cambios en el Company Brain requieren un StateChange aprobado por el owner del dato.

## Cómo crear un Department Brain Pack

### Paso 1 — Responder el cuestionario

Antes de crear archivos, completar `templates/questionnaires/department-brain-questionnaire.md`. Las respuestas informan cada documento del pack.

### Paso 2 — Completar cada archivo del pack

Orden recomendado:

1. **BRAIN_IDENTITY.md** — Definir quién es responsable y cuál es el alcance.
2. **ENTITIES.md** — Listar qué entidades gestiona.
3. **SOURCES.md** — Documentar de dónde vienen los datos.
4. **SIGNALS.md** — Definir qué eventos importan y qué hacer cuando ocurren.
5. **SYNC_POLICY.md** — Establecer qué sube al Company Brain y qué queda local.
6. **METRICS.md** — Definir cómo se mide la salud del cerebro.

### Paso 3 — Revisión y aprobación

El operador revisa el pack completo. Checklist de aprobación:

- [ ] El owner está identificado y ha aceptado la responsabilidad.
- [ ] Las entidades tienen campos, freshness y owner definidos.
- [ ] Las fuentes tienen frecuencia de sincronización y owner.
- [ ] Las señales tienen umbrales y reglas de escalado.
- [ ] La política de sincronización define qué sube y qué no sube.
- [ ] Las métricas tienen objetivo y frecuencia de revisión.

### Paso 4 — Activar y medir

Tras la aprobación, registrar la creación del cerebro como un StateChange en el Company Brain y empezar a medir con las métricas definidas.

## Errores comunes

| Error | Consecuencia | Cómo evitarlo |
|-------|-------------|---------------|
| Crear el cerebro sin owner | Nadie se responsabiliza de la veracidad | Siempre asignar un owner humano |
| No definir qué sube al Company Brain | Información importante se queda aislada | Completar SYNC_POLICY.md antes de activar |
| Demasiadas entidades desde el día 1 | Parálisis por complejidad | Empezar con 5-10 entidades, crecer según uso |
| No definir freshness por entidad | Datos obsoletos circulan como actuales | Cada entidad debe tener su categoría de freshness |
| No medir la salud del cerebro | No sabes si el cerebro sirve | Al menos 3 métricas desde el día 1 |

---

*Para ver un ejemplo completo de Department Brain, consultar `docs/03_brain_architecture.md`.*

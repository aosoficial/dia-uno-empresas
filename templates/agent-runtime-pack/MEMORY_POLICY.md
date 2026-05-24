# Politica de Memoria

## Que recuerda, que olvida y como gestiona la memoria

---

## Que es

MEMORY_POLICY.md define las reglas de memoria del agente: que informacion retiene, que olvida, con que frecuencia sincroniza con los Brains, y como clasifica la frescura de los datos que maneja.

**Un agente sin politica de memoria acumula datos obsoletos, pierde datos importantes o modifica memoria que no deberia tocar.**

## Cuando usarlo

- Al decidir si guardar o descartar informacion.
- Al sincronizar la memoria local del agente con el Company Brain o Department Brains.
- Al auditar la salud de la memoria del agente.
- Al diagnosticar decisiones incorrectas (puede deberse a datos stale).

## Campos obligatorios

| Campo | Descripcion |
|-------|-------------|
| `brains_lectura` | Que Brains puede consultar |
| `brains_escritura` | Que Brains puede modificar |
| `retencion` | Que datos retiene y por cuanto tiempo |
| `olvido` | Que datos debe descartar y cuando |
| `freshness` | Como clasifica la frescura de los datos |
| `sincronizacion` | Cuando y como sincroniza con los Brains |
| `feedback_to_method` | Qué correcciones o patrones deben elevarse al método DIA UNO Empresas |

---

## Plantilla

```yaml
# --- Politica de Memoria ---

agente: "agente/[COMPLETAR]"

# --- Acceso a Brains ---

brains_lectura:
  - brain: "[COMPLETAR]"  # Ej: Company Brain, Sales Brain
    tipo_acceso: "lectura"
    que_consulta: "[COMPLETAR — Que datos busca en este Brain]"

  - brain: "[COMPLETAR]"
    tipo_acceso: "lectura"
    que_consulta: "[COMPLETAR]"

brains_escritura:
  - brain: "[COMPLETAR]"
    tipo_acceso: "escritura"
    que_escribe: "[COMPLETAR — Que tipo de datos puede crear o modificar]"
    restricciones: "[COMPLETAR — Que no puede modificar]"

  - brain: "[COMPLETAR]"
    tipo_acceso: "escritura"
    que_escribe: "[COMPLETAR]"
    restricciones: "[COMPLETAR]"

brains_prohibidos:
  - brain: "[COMPLETAR]"
    razon: "[COMPLETAR]"

# --- Retencion ---

retencion:
  - tipo_dato: "[COMPLETAR]"
    duracion: "[COMPLETAR]"  # Ej: permanente, 30 dias, hasta cierre de caso
    donde: "[COMPLETAR]"  # local / Brain / ambos
    razon: "[COMPLETAR]"

  - tipo_dato: "[COMPLETAR]"
    duracion: "[COMPLETAR]"
    donde: "[COMPLETAR]"
    razon: "[COMPLETAR]"

# --- Olvido ---

olvido:
  - tipo_dato: "[COMPLETAR]"
    cuando: "[COMPLETAR]"  # Ej: tras 30 dias, al cerrar caso, al descartar lead
    proceso: "[COMPLETAR — Como se ejecuta el olvido: borrado, archivado, anonimizado]"

  - tipo_dato: "[COMPLETAR]"
    cuando: "[COMPLETAR]"
    proceso: "[COMPLETAR]"

# --- Freshness ---

freshness:
  critica:
    frecuencia_revision: "semanal"
    datos:
      - "[COMPLETAR — Ej: precios vigentes]"
      - "[COMPLETAR]"

  operativa:
    frecuencia_revision: "mensual"
    datos:
      - "[COMPLETAR — Ej: datos de contacto de clientes]"
      - "[COMPLETAR]"

  estable:
    frecuencia_revision: "trimestral"
    datos:
      - "[COMPLETAR — Ej: perfiles de clientes]"
      - "[COMPLETAR]"

  historica:
    frecuencia_revision: "no caduca"
    datos:
      - "[COMPLETAR — Ej: historial de interacciones cerradas]"
      - "[COMPLETAR]"

# --- Sincronizacion ---

sincronizacion:
  frecuencia: "[COMPLETAR]"  # Ej: al final de cada tarea / diaria / en tiempo real
  que_sube: "[COMPLETAR — Que datos pasan de memoria local al Brain]"
  que_baja: "[COMPLETAR — Que datos consulta del Brain al inicio de tarea]"
  conflictos: "[COMPLETAR — Que hacer si la memoria local contradice al Brain]"

# --- Feedback al método ---
feedback_to_method:
  activar_si:
    - "[COMPLETAR — corrección repetida]"
    - "[COMPLETAR — ausencia de contexto que afecta a varios agentes]"
    - "[COMPLETAR — patrón que debería convertirse en plantilla/skill/rutina]"
  salida: "Crear propuesta con templates/method-improvements/method-improvement-proposal.md"
  aprobacion: "Pedir aprobación si toca permisos, datos sensibles, exposición pública o acciones externas"
```

---

## Ejemplo — Politica de memoria de Vega (Meridian Foods)

```yaml
agente: "agente/vega"

brains_lectura:
  - brain: "Company Brain"
    tipo_acceso: "lectura"
    que_consulta: "Estructura de la empresa, politicas vigentes, equipo"

  - brain: "Sales Brain"
    tipo_acceso: "lectura"
    que_consulta: "Pipeline, historial de clientes, notas de interacciones"

  - brain: "Product Brain"
    tipo_acceso: "lectura"
    que_consulta: "Catalogo de productos, precios, roadmap de features"

brains_escritura:
  - brain: "Sales Brain"
    tipo_acceso: "escritura"
    que_escribe: "Notas de interacciones, actualizaciones de pipeline, datos de leads"
    restricciones: "No puede modificar datos historicos verificados. No puede borrar registros."

brains_prohibidos:
  - brain: "Product Brain (escritura)"
    razon: "Los datos de producto los gestiona el agente Nova."
  - brain: "Finance Brain"
    razon: "No es dominio de Vega."

retencion:
  - tipo_dato: "Estado actual de oportunidades en pipeline"
    duracion: "permanente (mientras la oportunidad este abierta)"
    donde: "Sales Brain"
    razon: "Necesario para seguimiento continuo"

  - tipo_dato: "Notas de interacciones con clientes"
    duracion: "permanente"
    donde: "Sales Brain"
    razon: "Contexto historico para futuras interacciones"

  - tipo_dato: "Borradores de propuestas"
    duracion: "90 dias tras envio de version final"
    donde: "local"
    razon: "Referencia durante negociacion, no necesario a largo plazo"

  - tipo_dato: "Precios consultados del Product Brain"
    duracion: "7 dias (cache local)"
    donde: "local"
    razon: "Los precios pueden cambiar. Refrescar semanalmente."

olvido:
  - tipo_dato: "Datos de leads descartados"
    cuando: "30 dias tras descarte"
    proceso: "Archivar en Sales Brain con marca 'descartado'. Borrar de memoria local."

  - tipo_dato: "Borradores de propuestas rechazadas"
    cuando: "30 dias tras rechazo"
    proceso: "Borrar de memoria local. El Sales Brain conserva registro del Receipt."

  - tipo_dato: "Cache local de precios"
    cuando: "7 dias sin refrescar"
    proceso: "Invalidar y consultar Product Brain en la proxima tarea."

freshness:
  critica:
    frecuencia_revision: "semanal"
    datos:
      - "Precios vigentes de productos"
      - "Estado de oportunidades en negociacion activa"
      - "Descuentos maximos autorizados"

  operativa:
    frecuencia_revision: "mensual"
    datos:
      - "Datos de contacto de clientes activos"
      - "Lista de productos disponibles"
      - "Politica de descuentos"

  estable:
    frecuencia_revision: "trimestral"
    datos:
      - "Perfiles de clientes (sector, tamano, necesidades base)"
      - "Estructura del equipo comercial"

  historica:
    frecuencia_revision: "no caduca"
    datos:
      - "Historial de propuestas enviadas"
      - "Historial de interacciones cerradas"
      - "Decisions comerciales pasadas"

sincronizacion:
  frecuencia: "Al final de cada tarea y al inicio de cada jornada"
  que_sube: >
    Notas de interacciones nuevas, actualizaciones de estado de pipeline,
    nuevos datos de leads.
  que_baja: >
    Estado actual de oportunidades asignadas, precios vigentes,
    cambios recientes en Product Brain.
  conflictos: >
    Si la memoria local contradice al Brain, prevalece el Brain.
    Registrar el conflicto como nota y notificar al operador si
    el dato es de categoria critica.
```

---

## Errores comunes

1. **No definir reglas de olvido.** Sin reglas de olvido, el agente acumula datos indefinidamente. Los datos obsoletos contaminan las decisiones.

2. **No clasificar freshness.** Si todos los datos se tratan igual, el agente puede usar un precio de hace 6 meses como si fuera vigente.

3. **Cache local sin expiracion.** Si el agente cachea precios o datos de producto sin fecha de expiracion, usara datos stale sin saberlo.

4. **No definir resolucion de conflictos.** Si la memoria local dice una cosa y el Brain dice otra, el agente necesita una regla clara. Sin ella, elige arbitrariamente.

5. **Permisos de escritura demasiado amplios en los Brains.** Si el agente puede escribir en cualquier Brain, puede contaminar la memoria de otros dominios.

6. **No elevar aprendizajes reutilizables.** Si un conflicto de memoria se repite y solo se corrige localmente, otros agentes volverán a caer. Los patrones reutilizables deben activar el loop de mejora del método.

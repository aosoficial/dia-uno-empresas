# Role Card

## Resumen ejecutivo del agente en una pagina

---

## Que es

La Role Card es un resumen de una pagina que contiene lo esencial del agente: quien es, que hace, cuales son sus limites y como se mide. Es la referencia rapida para cualquier persona que necesite entender que hace este agente sin leer todo el pack.

**La Role Card no sustituye al pack completo.** Es un indice ejecutivo. Si necesitas detalle, ve al archivo correspondiente.

## Cuando usarlo

- Para presentar al agente a nuevos miembros del equipo.
- Como referencia rapida durante reuniones.
- Al decidir a que agente asignar una tarea.
- Al auditar rapidamente si un agente opera dentro de sus limites.

---

## Plantilla

```markdown
# Role Card — [COMPLETAR: Nombre del Agente]

## Identidad

- **Nombre:** [COMPLETAR]
- **Tipo:** [COMPLETAR]
- **Owner:** [COMPLETAR]
- **Estado:** [COMPLETAR]
- **Version:** [COMPLETAR]

## Mision

[COMPLETAR — Una frase que resuma la mision principal del agente.]

## Top 3 Responsabilidades

1. [COMPLETAR]
2. [COMPLETAR]
3. [COMPLETAR]

## Top 3 Limites

1. [COMPLETAR — Lo mas importante que NO puede hacer]
2. [COMPLETAR]
3. [COMPLETAR]

## Metricas Clave

| Metrica | Objetivo | Frecuencia de medicion |
|---------|----------|----------------------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |

## Herramientas Principales

- [COMPLETAR] — [nivel de permiso]
- [COMPLETAR] — [nivel de permiso]
- [COMPLETAR] — [nivel de permiso]

## Agentes Relacionados

- [COMPLETAR] — [relacion: colabora / escala / recibe de]
- [COMPLETAR] — [relacion]

## Escalacion

- **Nivel 1:** [COMPLETAR — Que hace el agente primero]
- **Nivel 2:** [COMPLETAR — A quien escala]
- **Nivel 3:** [COMPLETAR — Backup]
```

---

## Ejemplo — Role Card de Vega (Meridian Foods)

```markdown
# Role Card — Vega

## Identidad

- **Nombre:** Vega
- **Tipo:** Ventas
- **Owner:** Carlos Ruiz (Director Comercial)
- **Estado:** Activo
- **Version:** 1.2.0

## Mision

Maximizar la conversion de oportunidades comerciales de Meridian Foods
manteniendo la calidad y coherencia de las propuestas.

## Top 3 Responsabilidades

1. Gestionar el pipeline comercial: seguimiento, actualizacion, priorizacion.
2. Generar propuestas comerciales en menos de 24 horas.
3. Mantener el Sales Brain actualizado con datos verificados.

## Top 3 Limites

1. No puede enviar propuestas a clientes sin aprobacion del operador.
2. No puede aplicar descuentos superiores al 15%.
3. No puede modificar datos en el Product Brain ni en el Company Brain.

## Metricas Clave

| Metrica | Objetivo | Frecuencia de medicion |
|---------|----------|----------------------|
| Tasa de conversion de propuestas | >25% | Mensual |
| Tiempo medio de generacion de propuesta | <24h | Semanal |
| Oportunidades sin seguimiento en 7 dias | 0 | Semanal |

## Herramientas Principales

- CRM — autonomo (lectura/escritura)
- Sales Brain — autonomo (lectura/escritura)
- Product Brain — autonomo (solo lectura)
- Email corporativo — con aprobacion
- Generador de propuestas — autonomo

## Agentes Relacionados

- Iris (soporte) — escala problemas tecnicos de clientes
- Nova (producto) — consulta roadmap y confirma ETAs de features

## Escalacion

- **Nivel 1:** Reintenta la operacion (max 2 reintentos, 1 hora)
- **Nivel 2:** Notifica a Carlos Ruiz (max 4 horas)
- **Nivel 3:** Escala a Laura Martinez como backup (max 24 horas)
```

---

## Errores comunes

1. **Role Card como sustituto del pack.** La Role Card es un resumen, no el pack completo. Si solo existe la Role Card y no el pack, el agente no tiene contrato operativo real.

2. **Responsabilidades vagas.** "Gestionar ventas" no es una responsabilidad. "Generar propuestas comerciales en menos de 24 horas" si lo es. Las responsabilidades deben ser concretas y medibles.

3. **Limites que no reflejan la realidad.** Si el top 3 de limites no coincide con PERMISSIONS.md, hay una desconexion. La Role Card debe ser coherente con el pack.

4. **Metricas sin objetivo.** "Tiempo de respuesta" sin objetivo no dice nada. "Tiempo de respuesta <24h" permite evaluar si el agente cumple.

5. **No actualizar la Role Card cuando cambia el pack.** Si el agente gana nuevas herramientas o permisos, la Role Card debe reflejarlo.

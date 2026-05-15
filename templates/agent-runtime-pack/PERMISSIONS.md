# Matriz de Permisos

## Que puede hacer el agente y a que nivel

---

## Que es

PERMISSIONS.md define la matriz completa de permisos del agente. Para cada accion posible, indica el nivel de permiso (autonomo, con notificacion, con aprobacion o prohibido) y las condiciones que aplican.

**Los permisos son la frontera entre un agente util y un agente peligroso.** Sin permisos claros, el agente toma decisiones que no deberia o bloquea tareas que podria resolver solo.

## Cuando usarlo

- Antes de ejecutar cualquier accion (el agente verifica su nivel de permiso).
- Al auditar las acciones del agente (comparar Receipt vs permisos).
- Al ajustar permisos tras el periodo de prueba.
- Al detectar acciones fuera de permiso en un Heartbeat.

## Niveles de permiso

```text
Nivel 1 — Autonomo
  El agente actua sin pedir permiso.
  Deja Receipt de la accion.

Nivel 2 — Con notificacion
  El agente actua y notifica al operador.
  El operador revisa pero no bloquea la accion.

Nivel 3 — Con aprobacion
  El agente prepara la accion y espera aprobacion antes de ejecutar.
  Si no hay respuesta en el tiempo definido, escala.

Nivel 4 — Prohibido
  El agente nunca puede realizar esta accion.
  Si la detecta como necesaria, escala al operador.
```

---

## Plantilla

```yaml
# --- Matriz de Permisos ---

agente: "agente/[COMPLETAR]"
version_permisos: "[COMPLETAR]"  # Fecha o version del pack
aprobado_por: "[COMPLETAR]"

permisos:

  # --- Acciones sobre datos ---

  - accion: "[COMPLETAR]"
    nivel: "[COMPLETAR]"  # autonomo / con_notificacion / con_aprobacion / prohibido
    condiciones: "[COMPLETAR — En que circunstancias aplica este nivel]"
    excepciones: "[COMPLETAR — Situaciones donde el nivel cambia]"

  - accion: "[COMPLETAR]"
    nivel: "[COMPLETAR]"
    condiciones: "[COMPLETAR]"
    excepciones: "[COMPLETAR]"

  # --- Acciones de comunicacion ---

  - accion: "[COMPLETAR]"
    nivel: "[COMPLETAR]"
    condiciones: "[COMPLETAR]"
    excepciones: "[COMPLETAR]"

  # --- Acciones sobre memoria ---

  - accion: "[COMPLETAR]"
    nivel: "[COMPLETAR]"
    condiciones: "[COMPLETAR]"
    excepciones: "[COMPLETAR]"

# --- Regla por defecto ---

regla_por_defecto: "[COMPLETAR]"
# Si una accion no esta en la lista, que nivel aplica?
# Recomendado: "con_aprobacion" (principio de menor privilegio)

# --- Permisos temporales ---

permisos_temporales:
  - accion: "[COMPLETAR]"
    nivel: "[COMPLETAR]"
    vigencia: "[COMPLETAR — Hasta cuando]"
    razon: "[COMPLETAR]"
```

---

## Ejemplo — Permisos de Vega (Meridian Foods)

```yaml
agente: "agente/vega"
version_permisos: "2026-05-01"
aprobado_por: "Carlos Ruiz (Director Comercial)"

permisos:

  # --- Acciones sobre datos ---

  - accion: "Consultar Sales Brain"
    nivel: "autonomo"
    condiciones: "Siempre disponible durante operacion normal"
    excepciones: "ninguna"

  - accion: "Consultar Product Brain"
    nivel: "autonomo"
    condiciones: "Solo lectura"
    excepciones: "ninguna"

  - accion: "Actualizar estado de oportunidad en CRM"
    nivel: "autonomo"
    condiciones: "Solo para oportunidades asignadas a Vega"
    excepciones: "Cambiar a 'Cerrada ganada' o 'Cerrada perdida' requiere aprobacion"

  - accion: "Registrar notas en Sales Brain"
    nivel: "autonomo"
    condiciones: "Solo en entidades de dominio ventas"
    excepciones: "ninguna"

  - accion: "Modificar datos de contacto de un cliente"
    nivel: "con_notificacion"
    condiciones: "Solo datos no sensibles (telefono, email alternativo)"
    excepciones: "Cambiar contacto principal requiere aprobacion"

  # --- Acciones de comunicacion ---

  - accion: "Generar borrador de propuesta"
    nivel: "autonomo"
    condiciones: "Usar siempre plantilla corporativa vigente"
    excepciones: "ninguna"

  - accion: "Enviar propuesta a cliente"
    nivel: "con_aprobacion"
    condiciones: "El operador debe revisar y aprobar antes del envio"
    excepciones: "ninguna — nunca se envia sin aprobacion"

  - accion: "Enviar email de seguimiento a cliente"
    nivel: "con_notificacion"
    condiciones: "Solo seguimiento de oportunidades abiertas. Horario laboral."
    excepciones: "Primer contacto con cliente nuevo requiere aprobacion"

  - accion: "Contactar cliente VIP"
    nivel: "con_aprobacion"
    condiciones: "Cualquier comunicacion con clientes marcados como VIP"
    excepciones: "ninguna"

  # --- Acciones sobre memoria ---

  - accion: "Escribir en Sales Brain"
    nivel: "autonomo"
    condiciones: "Solo datos de pipeline y notas de interaccion"
    excepciones: "Modificar datos historicos requiere aprobacion"

  - accion: "Escribir en Company Brain"
    nivel: "prohibido"
    condiciones: "Vega no tiene permiso de escritura en Company Brain"
    excepciones: "ninguna"

  - accion: "Borrar registros de memoria"
    nivel: "prohibido"
    condiciones: "Ningun agente puede borrar registros unilateralmente"
    excepciones: "ninguna"

  # --- Acciones comerciales ---

  - accion: "Aplicar descuento hasta 10%"
    nivel: "autonomo"
    condiciones: "Dentro de politica de descuentos vigente"
    excepciones: "ninguna"

  - accion: "Aplicar descuento entre 10% y 15%"
    nivel: "con_aprobacion"
    condiciones: "Requiere justificacion comercial"
    excepciones: "ninguna"

  - accion: "Aplicar descuento superior a 15%"
    nivel: "prohibido"
    condiciones: "Fuera de politica. Solo el Director Comercial puede autorizar."
    excepciones: "ninguna"

regla_por_defecto: "con_aprobacion"
# Cualquier accion no listada requiere aprobacion del operador.

permisos_temporales:
  - accion: "Enviar propuestas a leads del evento FoodTech sin aprobacion individual"
    nivel: "con_notificacion"
    vigencia: "2026-05-01 a 2026-05-31"
    razon: "Campana post-evento. Carlos aprobo envio masivo de propuestas estandar."
```

---

## Errores comunes

1. **No definir regla por defecto.** Si una accion no esta en la lista y no hay regla por defecto, el agente no sabe que hacer. Siempre definir una regla por defecto (recomendado: `con_aprobacion`).

2. **Permisos demasiado amplios.** "Autonomo para todo lo de ventas" es peligroso. Ser especifico: que acciones concretas son autonomas.

3. **Permisos demasiado restrictivos.** Si todo requiere aprobacion, el agente no puede operar de forma eficiente. El operador se satura de solicitudes.

4. **No definir excepciones.** "Actualizar CRM: autonomo" parece seguro. Pero si incluye cerrar oportunidades como ganadas sin verificacion, es un problema. Las excepciones acotan los permisos.

5. **No revisar permisos periodicamente.** Los permisos deben ajustarse tras el periodo de prueba y revisarse al menos trimestralmente. Un agente que funciona bien puede ganar mas autonomia. Uno que comete errores debe perder permisos.

6. **Permisos temporales sin fecha de vencimiento.** Si un permiso temporal no tiene fecha fin, se convierte en permanente por inercia.

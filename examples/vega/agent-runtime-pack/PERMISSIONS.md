# Matriz de Permisos — Vega

## Ejemplo completo relleno

---

> **Nota:** este es un ejemplo ficticio para ilustrar un PERMISSIONS.md completado.

---

```yaml
# --- Matriz de Permisos ---

agente: "agente/vega"
version_permisos: "2026-05-01"
aprobado_por: "Carlos Ruiz (Director Comercial)"

permisos:

  # --- Acciones sobre datos ---

  - accion: "Consultar Sales Brain"
    nivel: "autonomo"
    condiciones: "Siempre disponible durante operación normal"
    excepciones: "ninguna"

  - accion: "Consultar Product Brain"
    nivel: "autonomo"
    condiciones: "Solo lectura"
    excepciones: "ninguna"

  - accion: "Actualizar estado de oportunidad en CRM"
    nivel: "autonomo"
    condiciones: "Solo para oportunidades asignadas a Vega"
    excepciones: "Cambiar a 'Cerrada ganada' o 'Cerrada perdida' requiere aprobación"

  - accion: "Registrar notas en Sales Brain"
    nivel: "autonomo"
    condiciones: "Solo en entidades de dominio ventas"
    excepciones: "ninguna"

  - accion: "Modificar datos de contacto de un cliente"
    nivel: "con_notificacion"
    condiciones: "Solo datos no sensibles (teléfono, email alternativo)"
    excepciones: "Cambiar contacto principal requiere aprobación"

  # --- Acciones de comunicación ---

  - accion: "Generar borrador de propuesta"
    nivel: "autonomo"
    condiciones: "Usar siempre plantilla corporativa vigente"
    excepciones: "ninguna"

  - accion: "Enviar propuesta a cliente"
    nivel: "con_aprobacion"
    condiciones: "El operador debe revisar y aprobar antes del envío"
    excepciones: "ninguna — nunca se envía sin aprobación"

  - accion: "Enviar email de seguimiento a cliente"
    nivel: "con_notificacion"
    condiciones: "Solo seguimiento de oportunidades abiertas. Horario laboral."
    excepciones: "Primer contacto con cliente nuevo requiere aprobación"

  - accion: "Contactar cliente VIP"
    nivel: "con_aprobacion"
    condiciones: "Cualquier comunicación con clientes marcados como VIP"
    excepciones: "ninguna"

  # --- Acciones sobre memoria ---

  - accion: "Escribir en Sales Brain"
    nivel: "autonomo"
    condiciones: "Solo datos de pipeline y notas de interacción"
    excepciones: "Modificar datos históricos requiere aprobación"

  - accion: "Escribir en Company Brain"
    nivel: "prohibido"
    condiciones: "Vega no tiene permiso de escritura en Company Brain"
    excepciones: "ninguna"

  - accion: "Borrar registros de memoria"
    nivel: "prohibido"
    condiciones: "Ningún agente puede borrar registros unilateralmente"
    excepciones: "ninguna"

  # --- Acciones comerciales ---

  - accion: "Aplicar descuento hasta 10%"
    nivel: "autonomo"
    condiciones: "Dentro de política de descuentos vigente"
    excepciones: "ninguna"

  - accion: "Aplicar descuento entre 10% y 15%"
    nivel: "con_aprobacion"
    condiciones: "Requiere justificación comercial"
    excepciones: "ninguna"

  - accion: "Aplicar descuento superior a 15%"
    nivel: "prohibido"
    condiciones: "Fuera de política. Solo el Director Comercial puede autorizar."
    excepciones: "ninguna"

regla_por_defecto: "con_aprobacion"
# Cualquier acción no listada requiere aprobación del operador.

permisos_temporales:
  - accion: "Enviar propuestas a leads del evento FoodTech sin aprobación individual"
    nivel: "con_notificacion"
    vigencia: "2026-05-01 a 2026-05-31"
    razon: "Campaña post-evento. Carlos aprobó envío masivo de propuestas estándar."
```

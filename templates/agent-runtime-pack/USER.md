# Perfil del Operador

## El humano responsable de este agente

---

## Que es

USER.md define el perfil del operador humano que supervisa y es responsable de este agente. Incluye sus preferencias de comunicacion, estilo de aprobacion, horarios y como prefiere recibir escalaciones.

**Un agente sin perfil de operador no sabe como comunicarse con su responsable.** Escala de forma incorrecta, usa el tono equivocado o interrumpe en momentos inapropiados.

## Cuando usarlo

- Cada vez que el agente necesita comunicarse con el operador.
- Al escalar una decision o pedir aprobacion.
- Al generar reportes o Heartbeats.
- Al cambiar de operador (actualizar este archivo).

## Campos obligatorios

| Campo | Descripcion |
|-------|-------------|
| `nombre` | Nombre completo del operador |
| `rol` | Rol en la organizacion |
| `email` | Email de contacto |
| `canal_preferido` | Como prefiere recibir comunicaciones |
| `estilo_aprobacion` | Como aprueba/rechaza (rapido, detallado, etc.) |
| `horario` | Horario en el que esta disponible |
| `escalacion` | Como manejar situaciones urgentes |

---

## Plantilla

```yaml
# --- Perfil del Operador ---

nombre: "[COMPLETAR]"
rol: "[COMPLETAR]"
email: "[COMPLETAR]"

comunicacion:
  canal_preferido: "[COMPLETAR]"
  # Opciones comunes: email, Slack, notificacion en Brain, dashboard
  canales_alternativos:
    - "[COMPLETAR]"
  idioma: "[COMPLETAR]"
  tono_preferido: "[COMPLETAR]"
  # Ej: directo y conciso / detallado con contexto / solo datos
  nivel_detalle: "[COMPLETAR]"
  # Ej: alto (quiere ver todo) / medio (resumen + excepciones) / bajo (solo alertas)

aprobacion:
  estilo: "[COMPLETAR]"
  # Ej: rapido (si/no), detallado (pide justificacion), delegador (confia en el agente)
  tiempo_respuesta_tipico: "[COMPLETAR]"
  # Ej: "Responde en menos de 2 horas durante horario laboral"
  formato_preferido: "[COMPLETAR]"
  # Ej: "Resumen de una linea + opciones numeradas"
  cuando_no_molestar:
    - "[COMPLETAR — Ej: reuniones de liderazgo los lunes de 9 a 11]"
    - "[COMPLETAR]"

horario:
  zona_horaria: "[COMPLETAR]"
  disponible: "[COMPLETAR — Ej: lunes a viernes, 9:00-18:00]"
  excepciones: "[COMPLETAR — Ej: no disponible viernes tarde]"

escalacion:
  urgente: "[COMPLETAR — Como contactar en caso de urgencia]"
  no_urgente: "[COMPLETAR — Como contactar para temas no urgentes]"
  si_no_responde: "[COMPLETAR — Que hacer si no responde en X tiempo]"
  backup: "[COMPLETAR — Persona alternativa si el operador no esta disponible]"

contexto_relevante:
  experiencia_con_agentes: "[COMPLETAR — Ej: experimentado / nuevo en AOS]"
  areas_de_interes: "[COMPLETAR — Que le importa mas del trabajo del agente]"
  pet_peeves: "[COMPLETAR — Que le molesta o quiere evitar]"
  notas: "[COMPLETAR — Cualquier otra informacion relevante]"
```

---

## Ejemplo — Carlos Ruiz, operador de Vega (Meridian Foods)

```yaml
nombre: "Carlos Ruiz"
rol: "Director Comercial"
email: "carlos.ruiz@meridianfoods.com"

comunicacion:
  canal_preferido: "Slack (canal #ventas-vega)"
  canales_alternativos:
    - "Email para reportes semanales"
    - "Llamada telefonica solo para urgencias"
  idioma: "Espanol"
  tono_preferido: "Directo y conciso. Datos primero, opinion despues."
  nivel_detalle: "Medio. Quiere resumen ejecutivo y las excepciones. No necesita ver cada paso."

aprobacion:
  estilo: "Rapido. Prefiere opciones numeradas y toma decision en el momento."
  tiempo_respuesta_tipico: "Menos de 1 hora durante horario laboral"
  formato_preferido: >
    Resumen de una linea del tema.
    Opciones: 1) ... 2) ... 3) ...
    Recomendacion de Vega: opcion X porque Y.
  cuando_no_molestar:
    - "Lunes de 9 a 11 (reunion de liderazgo)"
    - "Viernes despues de las 16:00"

horario:
  zona_horaria: "Europe/Madrid"
  disponible: "Lunes a viernes, 8:30-18:30"
  excepciones: "Viernes disponible solo hasta las 16:00"

escalacion:
  urgente: "Mensaje directo en Slack con prefijo URGENTE"
  no_urgente: "Dejar en canal #ventas-vega, revisara antes del fin del dia"
  si_no_responde: "Si no responde en 4 horas, enviar recordatorio. Si pasan 8 horas, contactar a Laura Martinez (backup)."
  backup: "Laura Martinez, laura.martinez@meridianfoods.com"

contexto_relevante:
  experiencia_con_agentes: "Experimentado. Lleva 6 meses trabajando con agentes AOS."
  areas_de_interes: "Conversion de propuestas y seguimiento de oportunidades calientes."
  pet_peeves: "No quiere notificaciones sobre tareas rutinarias que ya aprobo. No quiere reportes de mas de 10 lineas."
  notas: "Prefiere que Vega proponga en vez de solo preguntar. Valora la proactividad."
```

---

## Errores comunes

1. **No definir el estilo de aprobacion.** Cada operador es distinto. Uno quiere opciones numeradas, otro quiere que el agente decida y solo avise. Sin esto, el agente escala mal.

2. **Ignorar el horario.** Enviar escalaciones a las 22:00 no es util si el operador solo lee mensajes en horario laboral. El agente debe respetar el horario definido.

3. **No definir backup.** Si el operador esta enfermo o de vacaciones y no hay backup, las aprobaciones se bloquean indefinidamente.

4. **Perfil demasiado generico.** "Prefiere comunicacion clara" no dice nada. Ser especifico: "Prefiere resumen de una linea + opciones numeradas".

5. **No actualizar cuando cambia el operador.** Si el agente cambia de responsable, USER.md debe actualizarse completamente. No basta con cambiar el nombre.

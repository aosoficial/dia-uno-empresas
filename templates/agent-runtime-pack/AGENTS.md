# Registro de Agentes

## Otros agentes con los que este agente interactua

---

## Que es

AGENTS.md es el registro de todos los agentes que este agente conoce y con los que puede interactuar. Define quien es cada agente, que hace, cuando contactarlo y como traspasar trabajo.

**Un agente sin registro de pares opera aislado.** No sabe a quien pedir ayuda ni a quien derivar trabajo.

## Cuando usarlo

- Cuando el agente necesita derivar una tarea a otro agente.
- Cuando el agente recibe un Context Packet que menciona a otro agente.
- Cuando se anade un nuevo agente al sistema y necesita registrarse aqui.
- Al auditar las interacciones entre agentes.

## Campos obligatorios por agente registrado

| Campo | Descripcion |
|-------|-------------|
| `id` | Identificador unico del agente |
| `nombre` | Nombre del agente |
| `dominio` | Area en la que opera |
| `responsabilidad` | Que hace en una frase |
| `cuando_contactar` | Situaciones en las que derivar trabajo a este agente |
| `protocolo_handoff` | Como traspasar trabajo (formato, canal, datos minimos) |
| `estado` | Estado actual del agente (activo/inactivo/en_pruebas) |

---

## Plantilla

```yaml
# --- Registro de Agentes Conocidos ---

agentes:

  - id: "agente/[COMPLETAR]"
    nombre: "[COMPLETAR]"
    dominio: "[COMPLETAR]"
    responsabilidad: "[COMPLETAR — Que hace este agente en una frase]"
    owner: "[COMPLETAR]"
    estado: "[COMPLETAR]"  # activo / inactivo / en_pruebas

    cuando_contactar:
      - "[COMPLETAR — Situacion 1 en la que derivar a este agente]"
      - "[COMPLETAR — Situacion 2]"

    cuando_no_contactar:
      - "[COMPLETAR — Situacion en la que NO derivar a este agente]"

    protocolo_handoff:
      formato: "[COMPLETAR — Ej: Context Packet estructurado]"
      canal: "[COMPLETAR — Ej: via Department Brain / directo]"
      datos_minimos:
        - "[COMPLETAR — Ej: identificador de la tarea]"
        - "[COMPLETAR — Ej: contexto relevante]"
        - "[COMPLETAR — Ej: urgencia]"
      confirmacion: "[COMPLETAR — Como saber que el otro agente recibio el traspaso]"

  - id: "agente/[COMPLETAR]"
    nombre: "[COMPLETAR]"
    # ... (repetir estructura para cada agente)
```

---

## Ejemplo — Agentes conocidos por Vega (Meridian Foods)

```yaml
agentes:

  - id: "agente/iris"
    nombre: "Iris"
    dominio: "soporte al cliente"
    responsabilidad: "Clasifica y resuelve tickets de soporte. Escala bugs nuevos a producto."
    owner: "Laura Martinez"
    estado: "activo"

    cuando_contactar:
      - "Un cliente del pipeline reporta un problema tecnico."
      - "Necesito saber si un cliente tiene tickets abiertos antes de contactarlo."
      - "Un cliente menciona un bug durante una llamada comercial."

    cuando_no_contactar:
      - "Para consultas sobre precios o propuestas (eso es mi dominio)."
      - "Para problemas que ya estan resueltos en el Product Brain."

    protocolo_handoff:
      formato: "Context Packet con datos del cliente y descripcion del problema"
      canal: "CS Brain"
      datos_minimos:
        - "id del cliente"
        - "descripcion del problema"
        - "urgencia (alta/media/baja)"
        - "contexto comercial relevante"
      confirmacion: "Iris genera Receipt de recepcion en CS Brain"

  - id: "agente/nova"
    nombre: "Nova"
    dominio: "producto"
    responsabilidad: "Gestiona roadmap, prioriza features y documenta bugs en el Product Brain."
    owner: "Elena Paredes"
    estado: "activo"

    cuando_contactar:
      - "Un cliente solicita una feature que no existe."
      - "Necesito confirmar fecha estimada de una feature para incluir en propuesta."
      - "Detecto un patron: multiples clientes piden lo mismo."

    cuando_no_contactar:
      - "Para bugs ya documentados en el Product Brain (consultarlo directamente)."
      - "Para preguntas que puedo resolver leyendo el Product Brain."

    protocolo_handoff:
      formato: "Context Packet con datos de la solicitud"
      canal: "Product Brain"
      datos_minimos:
        - "descripcion de la feature o bug"
        - "clientes que lo solicitan"
        - "impacto comercial estimado"
        - "urgencia"
      confirmacion: "Nova genera Receipt con evaluacion y ETA estimada"

  - id: "humano/carlos-ruiz"
    nombre: "Carlos Ruiz"
    dominio: "direccion comercial"
    responsabilidad: "Operador y owner de Vega. Aprueba propuestas y decisiones comerciales."
    owner: "n/a (es humano)"
    estado: "activo"

    cuando_contactar:
      - "Cualquier accion que requiera aprobacion (ver PERMISSIONS.md)."
      - "Situaciones ambiguas no cubiertas por el SOUL."
      - "Anomalias detectadas en el pipeline."
      - "Reporte diario (Heartbeat)."

    cuando_no_contactar:
      - "Para tareas autonomas que no requieren aprobacion."
      - "Para consultas que puedo resolver con los Brains."

    protocolo_handoff:
      formato: "Resumen estructurado con accion propuesta"
      canal: "Notificacion directa"
      datos_minimos:
        - "que se necesita aprobar"
        - "por que"
        - "opciones disponibles"
        - "recomendacion del agente"
      confirmacion: "Respuesta explicita del operador"
```

---

## Errores comunes

1. **No registrar al operador humano.** El operador es el interlocutor mas importante. Debe estar en el registro con su protocolo de contacto.

2. **Registrar agentes que no existen.** Solo registrar agentes activos o en pruebas. Si un agente se desactiva, actualizar su estado aqui.

3. **No definir "cuando NO contactar".** Sin esta seccion, el agente puede derivar trabajo innecesariamente, saturando a otros agentes.

4. **Protocolo de handoff vago.** "Enviar la informacion" no es un protocolo. Definir formato, canal, datos minimos y como confirmar recepcion.

5. **No actualizar el registro cuando cambia el ecosistema.** Si se crea un agente nuevo o se desactiva uno, este archivo debe reflejarlo.

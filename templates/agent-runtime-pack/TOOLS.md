# Herramientas del Agente

## Que herramientas tiene disponibles y como puede usarlas

---

## Que es

TOOLS.md lista todas las herramientas a las que el agente tiene acceso. Para cada herramienta define que es, que puede hacer con ella, que nivel de permiso tiene y restricciones de uso.

**Un agente sin catalogo de herramientas no sabe que puede usar.** Puede intentar usar herramientas que no tiene o ignorar herramientas disponibles.

## Cuando usarlo

- Al planificar una accion (verificar que la herramienta necesaria esta disponible).
- Al auditar las acciones de un agente (verificar que uso herramientas permitidas).
- Al anadir o retirar herramientas (actualizar este archivo).
- Al diagnosticar errores (verificar si el agente tenia acceso a la herramienta).

## Campos obligatorios por herramienta

| Campo | Descripcion |
|-------|-------------|
| `nombre` | Nombre de la herramienta |
| `tipo` | Categoria (lectura, escritura, comunicacion, analisis, etc.) |
| `descripcion` | Que hace en una frase |
| `nivel_permiso` | Autonomo / con notificacion / con aprobacion |
| `restricciones` | Limitaciones de uso |

---

## Plantilla

```yaml
# --- Catalogo de Herramientas ---

herramientas:

  - nombre: "[COMPLETAR]"
    tipo: "[COMPLETAR]"  # lectura / escritura / comunicacion / analisis / integracion
    descripcion: "[COMPLETAR — Que hace esta herramienta en una frase]"
    nivel_permiso: "[COMPLETAR]"  # autonomo / con_notificacion / con_aprobacion
    uso_tipico: "[COMPLETAR — Cuando y como la usa el agente]"
    restricciones:
      - "[COMPLETAR — Restriccion 1]"
    ejemplo_uso: "[COMPLETAR — Un ejemplo concreto de como se usa]"

  - nombre: "[COMPLETAR]"
    tipo: "[COMPLETAR]"
    descripcion: "[COMPLETAR]"
    nivel_permiso: "[COMPLETAR]"
    uso_tipico: "[COMPLETAR]"
    restricciones:
      - "[COMPLETAR]"
    ejemplo_uso: "[COMPLETAR]"

# --- Herramientas Prohibidas ---

herramientas_prohibidas:

  - nombre: "[COMPLETAR]"
    razon: "[COMPLETAR — Por que este agente no puede usar esta herramienta]"

  - nombre: "[COMPLETAR]"
    razon: "[COMPLETAR]"
```

---

## Ejemplo — Herramientas de Vega (Meridian Foods)

```yaml
herramientas:

  - nombre: "CRM (Meridian)"
    tipo: "lectura/escritura"
    descripcion: "Sistema de gestion de relaciones con clientes. Contiene pipeline, contactos y actividades."
    nivel_permiso: "autonomo"
    uso_tipico: "Consultar estado de oportunidades, actualizar etapa del pipeline, registrar actividades."
    restricciones:
      - "No puede eliminar contactos ni oportunidades."
      - "No puede modificar datos de facturacion."
    ejemplo_uso: >
      Actualizar la oportunidad de Costa Frutas de "Propuesta enviada"
      a "Negociacion" tras recibir respuesta del cliente.

  - nombre: "Sales Brain"
    tipo: "lectura/escritura"
    descripcion: "Memoria operativa del departamento comercial."
    nivel_permiso: "autonomo"
    uso_tipico: "Consultar historial de clientes, registrar notas de interacciones, actualizar datos de pipeline."
    restricciones:
      - "Solo puede escribir en entidades de su dominio (ventas)."
      - "No puede modificar datos creados por otros agentes sin aprobacion."
    ejemplo_uso: >
      Registrar que Costa Frutas solicito descuento del 20%
      y que la alternativa propuesta fue modulo de reporting gratis.

  - nombre: "Product Brain"
    tipo: "solo lectura"
    descripcion: "Memoria operativa del departamento de producto."
    nivel_permiso: "autonomo"
    uso_tipico: "Consultar estado de features, precios de productos, roadmap."
    restricciones:
      - "Solo lectura. No puede modificar datos de producto."
    ejemplo_uso: >
      Verificar fecha estimada de la integracion SAP antes
      de incluirla en una propuesta comercial.

  - nombre: "Generador de propuestas"
    tipo: "escritura"
    descripcion: "Genera documentos PDF de propuestas comerciales a partir de plantillas."
    nivel_permiso: "autonomo"
    uso_tipico: "Crear borradores de propuestas para revision del operador."
    restricciones:
      - "Los borradores no se envian al cliente sin aprobacion."
      - "Usar siempre la plantilla corporativa vigente."
    ejemplo_uso: >
      Generar propuesta para Costa Frutas con Plan Enterprise,
      descuento del 10% y modulo de reporting incluido.

  - nombre: "Email corporativo"
    tipo: "comunicacion"
    descripcion: "Envio de correos electronicos desde la cuenta corporativa de ventas."
    nivel_permiso: "con_aprobacion"
    uso_tipico: "Enviar propuestas aprobadas, seguimiento de oportunidades."
    restricciones:
      - "Cada email al cliente requiere aprobacion del operador."
      - "Solo en horario laboral (9:00-18:00)."
      - "No puede enviar a mas de 5 destinatarios a la vez."
    ejemplo_uso: >
      Enviar propuesta aprobada a Costa Frutas con copia al
      operador para seguimiento.

herramientas_prohibidas:

  - nombre: "Herramientas financieras (contabilidad, facturacion)"
    razon: "No es dominio de Vega. Las finanzas las gestiona el equipo de administracion."

  - nombre: "Acceso directo a base de datos de produccion"
    razon: "Riesgo de modificar datos sensibles. Vega opera a traves de CRM y Brains."

  - nombre: "Redes sociales corporativas"
    razon: "La comunicacion publica la gestiona el equipo de marketing."
```

---

## Errores comunes

1. **No distinguir entre lectura y escritura.** "Acceso al CRM" no es suficiente. Hay que especificar si puede leer, escribir, o ambos. Un agente con escritura donde solo deberia tener lectura es un riesgo.

2. **No definir herramientas prohibidas.** La lista de prohibiciones es tan importante como la de permisos. Sin ella, el agente puede asumir que tiene acceso a todo.

3. **Nivel de permiso generico para todas.** Cada herramienta puede tener un nivel distinto. El CRM puede ser autonomo, pero el email requiere aprobacion.

4. **No actualizar cuando se anaden herramientas.** Si el agente recibe acceso a una nueva integracion, TOOLS.md debe reflejarlo inmediatamente.

5. **Restricciones vagas.** "Usar con cuidado" no es una restriccion. "No puede eliminar registros" si lo es.

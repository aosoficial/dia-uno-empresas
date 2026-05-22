# Cómo crear tu matriz de aprobaciones

Guía paso a paso para definir qué puede hacer un empleado digital sin permiso, qué necesita aprobación y quién aprueba.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- `validate_point_b_readiness.py --mode scaffold` pasando;
- Dirección / Mother Brain con propósito, oferta y prioridades rellenados;
- al menos un departamento con `department-brain.md`;
- al menos un empleado digital con `PERMISSIONS.md`.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md) y completa los pasos previos.

## Por qué importa

Sin una matriz de aprobaciones clara:

- un agente puede actuar más allá de lo seguro;
- un humano no sabe cuándo debe intervenir;
- no hay forma de auditar si una acción debía haberse aprobado.

Regla base:

> Redactar, analizar, ordenar y preparar son seguros por defecto. Enviar, publicar, gastar dinero, comprometerse legal o económicamente, cambiar producción y usar datos sensibles requieren aprobación humana explícita.

## Qué vas a conseguir

Al final de este how-to tendrás:

1. Un archivo `company/approval-boundaries.md` con categorías, acciones y reglas concretas.
2. Claridad sobre quién aprueba cada tipo de acción.
3. Un formato de escalación estándar.
4. Una referencia que conecta con `PERMISSIONS.md` de cada empleado digital.

Esto es lo que necesita `validate_point_b_readiness.py --mode operational` para pasar el criterio "Approval boundaries reviewed".

---

## Paso 1 — Listar las categorías de riesgo

Toda acción de un agente cae en una de estas categorías. No necesitas inventar categorías nuevas:

| Categoría | Qué cubre | Ejemplo |
|---|---|---|
| **Interna** | Redactar, analizar, clasificar, preparar borradores | Crear checklist de entrega |
| **Externa** | Contactar a alguien fuera del equipo | Enviar email a un cliente |
| **Pública** | Publicar en canales visibles para terceros | Publicar post en redes sociales |
| **Económica** | Gastar dinero o comprometer ingresos | Contratar herramienta, emitir factura |
| **Legal** | Asumir compromisos legales o contractuales | Firmar contrato, aceptar condiciones |
| **Producción** | Cambiar sistemas que afectan al servicio activo | Desplegar código, modificar flujo de trabajo en producción |
| **Datos sensibles** | Usar datos personales, regulados o confidenciales | Acceder a datos de clientes, mover datos entre sistemas |

**Criterio de salida:** conoces las 7 categorías y puedes clasificar las acciones de tu negocio en ellas.

---

## Paso 2 — Clasificar las acciones de tu negocio

Para cada departamento activo, lista las acciones que un humano o agente ejecuta y asigna una categoría.

Formato recomendado:

```markdown
| Acción | Categoría | ¿Quién la ejecuta hoy? |
|---|---|---|
| Redactar propuesta comercial | interna | agente/nombre o persona |
| Enviar propuesta al cliente | externa + económica | persona |
| Publicar caso de éxito en web | pública | persona |
| Clasificar gastos del mes | interna | agente/nombre |
| Pagar factura a proveedor | económica | persona |
```

Consejo: empieza solo con el departamento del primer loop. No necesitas cubrir toda la empresa ahora.

**Criterio de salida:** tienes una lista de al menos 5 acciones con su categoría asignada.

---

## Paso 3 — Asignar regla de aprobación

Para cada acción, decide:

| Regla | Significado | Cuándo usar |
|---|---|---|
| `permitido` | El agente puede hacerlo sin pedir permiso | Acciones internas sin riesgo |
| `permitido con condiciones` | Permitido si se cumplen condiciones específicas | Acciones internas con restricción de datos o alcance |
| `requiere aprobación` | El agente para y pide permiso a una persona | Cualquier acción externa, pública, económica, legal, de producción o con datos sensibles |
| `prohibido` | El agente no puede hacerlo bajo ninguna circunstancia | Acciones fuera de su alcance o que requieren otro rol |

Formato:

```markdown
| Acción | Categoría | Regla | Aprueba | Condiciones |
|---|---|---|---|---|
| Redactar propuesta | interna | permitido | — | Solo con datos del Context Packet |
| Enviar propuesta | externa + económica | requiere aprobación | Ana García | Solo tras revisión humana del contenido |
| Publicar caso de éxito | pública | requiere aprobación | Ana García | Solo con consentimiento del cliente |
| Clasificar gastos | interna | permitido con condiciones | — | Solo lectura, no modifica importes |
| Pagar factura | económica | prohibido para agentes | Ana García | Solo persona con acceso bancario |
```

**Criterio de salida:** cada acción tiene regla, aprobador (si aplica) y condiciones.

---

## Paso 4 — Definir el formato de escalación

Cuando un agente necesita aprobación, debe presentar la solicitud en un formato estándar. Recomendamos 1:3:1:

```markdown
## Solicitud de aprobación

**Problema:** [1 frase que describe qué necesita aprobación]

**Opciones:**
1. [Opción A] — riesgo: [bajo/medio/alto] — impacto: [descripción]
2. [Opción B] — riesgo: [bajo/medio/alto] — impacto: [descripción]
3. [Opción C / No actuar] — riesgo: [bajo/medio/alto] — impacto: [descripción]

**Recomendación:** [1 opción con justificación breve]

**Aprobador:** [nombre de la persona que debe decidir]
**Fecha límite:** [cuándo se necesita la decisión]
```

**Criterio de salida:** tu archivo incluye un formato de escalación que los agentes usarán cuando necesiten aprobación.

---

## Paso 5 — Escribir el archivo de aprobaciones

Abre `company/approval-boundaries.md` en tu instancia privada y reemplaza el contenido scaffold con tus decisiones reales.

Estructura recomendada:

```markdown
# Approval Boundaries — [Nombre de empresa]

Última revisión: [fecha ISO 8601]
Revisado por: [persona]
Próxima revisión: [fecha o "tras 5 ejecuciones"]

## Regla por defecto

Redactar, analizar, ordenar y preparar = permitido sin aprobación.
Contacto externo, publicación, gasto, compromiso legal, cambio en producción, datos sensibles = requiere aprobación humana explícita.

## Matriz de aprobaciones

| Acción | Categoría | Regla | Aprueba | Condiciones |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Formato de escalación

[formato 1:3:1 del paso 4]

## Conexión con permisos de empleados digitales

Cada `PERMISSIONS.md` de un empleado digital debe ser coherente con esta matriz:
- Las acciones listadas como "permitido" aquí deben estar en `autonomo` del agente.
- Las acciones "requiere aprobación" deben estar en `requiere_aprobacion`.
- Las acciones "prohibido" deben estar en `prohibido`.

Si hay contradicción entre esta matriz y el `PERMISSIONS.md` de un agente, prevalece la regla más restrictiva.
```

**Criterio de salida:** `company/approval-boundaries.md` tiene regla por defecto, matriz con acciones reales, formato de escalación y conexión con permisos. No contiene placeholders tipo "COMPLETAR", "TBD" o "replace this".

---

## Paso 6 — Verificar coherencia con PERMISSIONS.md

Para cada empleado digital activo, abre su `PERMISSIONS.md` y verifica:

1. Las acciones `autonomo` del agente están marcadas como `permitido` en la matriz.
2. Las acciones `requiere_aprobacion` coinciden con las que piden aprobación en la matriz.
3. Las acciones `prohibido` incluyen todo lo que la matriz prohíbe para ese rol.

Si encuentras incoherencias, corrige el `PERMISSIONS.md` del agente para que sea igual o más restrictivo que la matriz.

**Criterio de salida:** cada `PERMISSIONS.md` es coherente con `approval-boundaries.md`.

---

## Ejemplo sintético — Agencia "Sol Digital"

### Contexto

Sol Digital tiene 3 personas. Primer departamento activo: operations-delivery. Empleado digital: agente/lara (solo redacta y clasifica).

### Matriz de aprobaciones

```markdown
# Approval Boundaries — Sol Digital

Última revisión: 2026-05-22
Revisado por: Ana García (fundadora)
Próxima revisión: 2026-06-05 o tras 5 ejecuciones

## Regla por defecto

Redactar, analizar, ordenar y preparar = permitido sin aprobación.
Contacto externo, publicación, gasto, compromiso legal, cambio en producción, datos sensibles = requiere aprobación humana explícita.

## Matriz de aprobaciones

| Acción | Categoría | Regla | Aprueba | Condiciones |
|---|---|---|---|---|
| Redactar checklist de entrega | interna | permitido | — | Solo con datos del Context Packet |
| Clasificar tareas por prioridad | interna | permitido | — | Solo lectura del tablero |
| Redactar borrador de propuesta | interna | permitido con condiciones | — | Solo datos sintéticos o anonimizados |
| Enviar propuesta al cliente | externa + económica | requiere aprobación | Ana García | Tras revisión humana del contenido |
| Publicar caso de éxito | pública | requiere aprobación | Ana García | Con consentimiento escrito del cliente |
| Acceder a datos de clientes | datos sensibles | requiere aprobación | Ana García | Solo para la tarea específica del Context Packet |
| Contratar herramienta o servicio | económica | prohibido para agentes | Ana García | Solo personas con acceso bancario |
| Firmar contrato o aceptar condiciones | legal | prohibido para agentes | Ana García | Solo Ana como representante legal |
| Modificar flujo de producción | producción | requiere aprobación | Ana García | Solo tras prueba interna documentada |

## Formato de escalación

1 problema — 3 opciones con riesgo — 1 recomendación.
Incluir: aprobador, fecha límite, Context Packet relacionado.

## Conexión con permisos

- agente/lara PERMISSIONS.md: autonomo = redactar, clasificar. requiere_aprobacion = acceder a datos de clientes. prohibido = enviar, publicar, gastar, firmar, modificar producción.
```

### Verificación

PERMISSIONS.md de agente/lara dice:
- autonomo: redactar checklists, clasificar tareas → ✅ coherente con matriz
- requiere_aprobacion: acceder a datos de clientes → ✅ coherente
- prohibido: enviar, publicar, gastar, firmar, modificar producción → ✅ coherente

---

## Errores comunes

| Error | Consecuencia | Cómo evitarlo |
|---|---|---|
| No definir aprobador concreto | Nadie sabe a quién pedir permiso | Poner nombre y apellido, no "el responsable" |
| Poner "permitido" a acciones externas | Agente contacta a clientes sin revisión | Todo contacto externo = requiere aprobación |
| Dejar "TBD" o "COMPLETAR" en la matriz | Validador operativo falla; agente sin límites claros | Completar todas las filas antes de activar agentes |
| PERMISSIONS.md más permisivo que la matriz | Agente puede hacer algo que la empresa no ha aprobado | PERMISSIONS.md ≤ approval-boundaries.md |
| No revisar la matriz tras cambios | Acciones nuevas quedan sin clasificar | Revisar tras cada nuevo SOP o agente |
| Prohibir todo al agente | El agente no puede hacer nada útil | Al menos las acciones internas deben estar permitidas |

---

## Siguiente paso

Después de crear tu matriz:

1. Ejecuta o continúa el primer loop interno siguiendo [`run-first-internal-loop.md`](run-first-internal-loop.md).
2. Si añades un nuevo SOP o empleado digital, revisa que la matriz cubra las acciones nuevas.
3. Si añades un departamento, extiende la matriz con las acciones de ese departamento.

Si te bloqueas, usa el reporte seguro de DIA UNO en [diauno.io](https://diauno.io) con [`templates/dia-uno/blocker-report.md`](../dia-uno/blocker-report.md). No compartas datos de clientes, secretos ni credenciales.

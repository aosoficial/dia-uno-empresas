# Cómo crear el mapa de fuentes de verdad

Guía práctica para documentar dónde vive la información del negocio, quién la controla, qué tan fresca está y qué riesgos tiene.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- `company/company-brain.md` rellenado con propósito, oferta y prioridades.

Este mapa se necesita ANTES de crear el primer Context Packet. Sin él, el agente no sabe qué fuentes consultar ni cuáles son confiables.

## Qué produce

Un archivo `company/source-of-truth-map.md` en tu instancia privada con:

1. Lista de sistemas/herramientas donde vive información del negocio.
2. Owner, permisos y frescura de cada fuente.
3. Riesgos de privacidad y datos sensibles.
4. Reglas sobre qué puede y qué no puede compartirse fuera de la instancia privada.

---

## Por qué importa

Sin mapa de fuentes:

- El agente trabaja con datos desactualizados o incompletos.
- Nadie sabe quién puede acceder a qué.
- Se copian datos sensibles donde no deberían estar.
- Los Context Packets no tienen procedencia verificable.

---

## Paso 1 — Listar los sistemas del negocio

Escribe todos los lugares donde tu negocio guarda información operativa:

| Sistema | Tipo | Ejemplo |
|---------|------|---------|
| Email | comunicación | Gmail, Outlook |
| Mensajería | comunicación | WhatsApp, Slack, Telegram |
| Documentos | conocimiento | Google Drive, Notion, Dropbox |
| Hojas de cálculo | datos | Google Sheets, Excel |
| CRM | clientes | HubSpot, Pipedrive, Notion |
| Gestión de proyectos | operaciones | Trello, Asana, Monday, Notion |
| Facturación | finanzas | Stripe, QuickBooks, hoja de cálculo |
| Calendario | agenda | Google Calendar, Outlook |
| Código | producto | GitHub, GitLab |
| Almacenamiento | archivos | Google Drive, Dropbox, NAS |

No necesitas tener todos. Lista solo los que usas realmente.

**Criterio de salida:** lista de 3-10 sistemas que usa tu negocio.

---

## Paso 2 — Documentar cada fuente

Para cada sistema, completa esta ficha:

```markdown
### [Nombre del sistema]

- **Tipo:** (comunicación / conocimiento / datos / clientes / operaciones / finanzas / otro)
- **URL o ubicación:** (dirección o ruta — NO incluyas credenciales)
- **Owner:** (persona responsable del contenido)
- **Quién tiene acceso:** (lista de personas/roles)
- **Frescura:** (actualización: diaria / semanal / manual / desconocida)
- **Última verificación:** (fecha ISO en que alguien confirmó que la información está al día)
- **Contiene datos sensibles:** (sí/no — si sí, indicar tipo: clientes, financiero, personal, credenciales)
- **Puede usarse en Context Packets:** (sí / sí con anonimización / no)
- **Riesgos:** (qué puede salir mal — ej: "datos desactualizados", "sin backup", "acceso compartido sin control")
```

**Criterio de salida:** al menos 3 fuentes documentadas con owner, acceso, frescura y riesgos.

---

## Paso 3 — Clasificar riesgo de privacidad

Para cada fuente, aplica esta clasificación:

| Nivel | Descripción | Puede ir en repo público | Puede ir en Context Packet |
|-------|-------------|--------------------------|---------------------------|
| Público | Información general, no vinculada a personas o clientes | Sí | Sí |
| Interno | Procesos, SOPs, métricas internas sin datos de clientes | No — solo instancia privada | Sí, con precaución |
| Confidencial | Datos de clientes, finanzas, contratos | No | Solo anonimizado o con permiso |
| Restringido | Credenciales, tokens, datos regulados (salud, legal) | Nunca | Nunca |

Marca cada sistema con su nivel en la tabla.

**Criterio de salida:** cada fuente tiene nivel de privacidad asignado.

---

## Paso 4 — Rellenar la tabla resumen

Copia esta tabla a tu `company/source-of-truth-map.md`:

```markdown
## Mapa de fuentes de verdad

| Sistema | Tipo | Owner | Acceso | Frescura | Última verif. | Sensibilidad | Uso en CP | Riesgos |
|---------|------|-------|--------|----------|--------------|-------------|-----------|---------|
| (nombre) | (tipo) | (persona) | (quién) | (cadencia) | (fecha ISO) | (público/interno/confidencial/restringido) | (sí/anonimizado/no) | (riesgo principal) |
```

**Criterio de salida:** tabla completa con las fuentes del paso 1.

---

## Paso 5 — Escribir reglas de uso

Añade una sección de reglas al final del mapa:

```markdown
## Reglas de uso

1. **Nunca** copiar credenciales, tokens o API keys en ningún documento del Company Brain.
2. **Nunca** pegar datos reales de clientes en el repositorio público.
3. Los Context Packets deben indicar la fuente y fecha de cada dato.
4. Si un dato tiene más de 30 días sin verificar, marcar como "frescura: desconocida".
5. Los agentes digitales solo pueden consultar fuentes marcadas como "Uso en CP: sí".
6. Si necesitas usar datos confidenciales, anonimiza antes de incluir en cualquier documento.
7. Antes de conectar una fuente nueva (API, integración), requiere aprobación según `company/approval-boundaries.md`.
```

Adapta las reglas a tu contexto. Si manejas datos regulados (salud, legal, financiero), añade las restricciones correspondientes.

**Criterio de salida:** al menos 5 reglas de uso documentadas.

---

## Paso 6 — Verificar con el primer departamento

Antes de crear el primer Context Packet, confirma que:

- Las fuentes que necesita el primer workflow están documentadas.
- El agente sabe qué puede consultar (marcado "sí" en la columna "Uso en CP").
- El owner de cada fuente está identificado y puede verificar frescura.

Si falta una fuente crítica, documéntala ahora. No crees Context Packets con fuentes no mapeadas.

**Criterio de salida:** las fuentes del primer departamento están en el mapa.

---

## Errores comunes

| Error | Por qué falla | Solución |
|---|---|---|
| Poner credenciales en el mapa | Riesgo de seguridad si el archivo se comparte | Solo incluye nombre del sistema y quién tiene acceso, nunca contraseñas |
| No verificar frescura | El agente trabaja con datos desactualizados | Cada fuente necesita fecha de última verificación |
| Marcar todo como "público" | Datos confidenciales se filtran a Context Packets | Clasifica honestamente; en caso de duda, marca como "interno" |
| No mapear fuentes del primer departamento | El Context Packet no tiene procedencia | Completa al menos las fuentes del departamento activo |
| Copiar datos reales de clientes al ejemplo | Violación de privacidad en repo público | Usa datos sintéticos; los datos reales solo en la instancia privada |
| Mapa enorme de 20+ sistemas | Inmanejable, nunca se actualiza | Empieza con 3-5 fuentes del primer departamento; añade más después |

---

## Cadencia de revisión

| Cadencia | Qué revisar | Quién |
|----------|-------------|-------|
| Mensual | ¿Alguna fuente cambió de owner o acceso? ¿Frescura correcta? | Owner de dirección |
| Cada nuevo departamento | ¿Las fuentes del departamento están mapeadas? | Owner del departamento |
| Cada nueva herramienta | Añadir al mapa antes de conectar | Owner de la herramienta + dirección |
| Cada incidente de datos | Revisar clasificación y reglas de uso | Owner + responsable del incidente |

---

## Siguiente paso

Con el mapa de fuentes completo, puedes crear Context Packets con procedencia verificable para el primer loop: [`run-first-internal-loop.md`](run-first-internal-loop.md).

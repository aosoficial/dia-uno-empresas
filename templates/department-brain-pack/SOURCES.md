# Fuentes de Datos

## Qué es esto

Este archivo documenta todas las fuentes de información que alimentan este Department Brain. Para cada fuente se define qué datos aporta, con qué frecuencia se sincroniza, quién es responsable y cuán fiable es.

Una **fuente** es cualquier sistema, proceso o persona que proporciona datos al cerebro. Puede ser un CRM, una hoja de cálculo, un email, un sensor o una persona que reporta manualmente.

---

## Fuentes

### [COMPLETAR — Nombre de la fuente 1]

- **Tipo:** [sistema / documento / persona / proceso / API]
- **Qué datos aporta:** [COMPLETAR — qué entidades o propiedades alimenta]
- **Frecuencia de sincronización:** [COMPLETAR — tiempo real / diaria / semanal / manual / por evento]
- **Formato:** [COMPLETAR — API REST / CSV / manual / webhook / otro]
- **Owner:** [COMPLETAR — quién es responsable de que esta fuente esté activa y sea correcta]
- **Fiabilidad:** [alta / media / baja]
- **Notas:** [COMPLETAR — observaciones relevantes, limitaciones conocidas]

### [COMPLETAR — Nombre de la fuente 2]

[Repetir la misma estructura]

---

## Criterios de fiabilidad

| Nivel | Definición | Ejemplo |
|-------|-----------|---------|
| **Alta** | Datos estructurados, actualizados automáticamente, raramente incorrectos | ERP, CRM con datos validados, API de proveedor |
| **Media** | Datos generalmente correctos pero con actualizaciones manuales o posibles retrasos | Hojas de cálculo actualizadas semanalmente, informes mensuales |
| **Baja** | Datos no estructurados, informales o con alta probabilidad de estar desactualizados | Emails sueltos, notas de reuniones sin verificar, datos verbales |

**Regla:** si una fuente tiene fiabilidad baja, los datos que aporta deben verificarse antes de incluirlos en un Context Packet. Si una fuente baja es la única fuente de un dato crítico, hay un problema de cobertura que debe resolverse.

---

## Cobertura de entidades

Para verificar que todas las entidades tienen al menos una fuente:

| Entidad | Fuente principal | Fuente secundaria | Sin fuente |
|---------|-----------------|-------------------|------------|
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR o "—"] | [ ] |
| [COMPLETAR] | [COMPLETAR] | [COMPLETAR o "—"] | [ ] |

**Regla:** ninguna entidad del cerebro debe quedarse sin fuente. Si una entidad no tiene fuente identificada, o se busca una fuente o se elimina la entidad.

---

## Ejemplo — Fuentes del Sales Brain de Meridian Foods

### CRM (Pipedrive)

- **Tipo:** sistema
- **Qué datos aporta:** leads, clientes activos, pipeline por etapa, propuestas enviadas, estados de negociación
- **Frecuencia de sincronización:** tiempo real (webhook) + verificación semanal manual
- **Formato:** API REST + webhooks
- **Owner:** Carlos Martín (Director Comercial)
- **Fiabilidad:** alta
- **Notas:** Fuente principal del pipeline. Los comerciales deben actualizar estados antes de las 18:00 cada día.

### Email de clientes

- **Tipo:** documento
- **Qué datos aporta:** objeciones, necesidades nuevas, confirmaciones de interés, feedback
- **Frecuencia de sincronización:** manual — el comercial registra información relevante en el CRM tras cada email importante
- **Formato:** texto no estructurado → resumen manual en CRM
- **Owner:** Comercial asignado al cliente
- **Fiabilidad:** media
- **Notas:** Riesgo de pérdida de información si el comercial no registra el email. Revisar cobertura en la reunión semanal.

### Reuniones de seguimiento comercial

- **Tipo:** proceso
- **Qué datos aporta:** decisiones sobre pricing, estado de negociaciones complejas, objeciones recurrentes, señales de churn
- **Frecuencia de sincronización:** semanal (cada lunes tras la reunión)
- **Formato:** acta de reunión → resumen estructurado
- **Owner:** Carlos Martín (Director Comercial)
- **Fiabilidad:** alta (cuando se registra) / baja (si no se registra)
- **Notas:** Es crítico que el acta se registre el mismo día. Si pasan más de 48h, la información se degrada.

### Informes de ferias y eventos

- **Tipo:** documento
- **Qué datos aporta:** nuevos leads, contactos, tendencias de mercado, movimientos de competidores
- **Frecuencia de sincronización:** por evento (tras cada feria o evento)
- **Formato:** informe en documento → datos de leads al CRM
- **Owner:** Comercial que asistió al evento
- **Fiabilidad:** media
- **Notas:** Los leads de feria deben registrarse en CRM en las primeras 48h post-evento. Pasado ese tiempo, la conversión cae drásticamente.

### Cobertura de entidades

| Entidad | Fuente principal | Fuente secundaria | Sin fuente |
|---------|-----------------|-------------------|------------|
| Lead | CRM (Pipedrive) | Informes de ferias | |
| Cliente activo | CRM (Pipedrive) | Email de clientes | |
| Propuesta | CRM (Pipedrive) | — | |
| Objeción | Email de clientes | Reuniones de seguimiento | |
| Compromiso comercial | Reuniones de seguimiento | CRM (notas) | |

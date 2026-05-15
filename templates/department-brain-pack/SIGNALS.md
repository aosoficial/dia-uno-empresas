# Señales

## Qué es esto

Este archivo define las señales que este Department Brain monitoriza. Una **señal** es un evento, cambio o patrón que indica que algo importante está ocurriendo y puede requerir una acción.

Las señales son el sistema de alerta temprana del departamento. Sin señales definidas, los problemas se detectan cuando ya son crisis.

---

## Tipos de señales

| Tipo | Descripción | Ejemplo |
|------|------------|---------|
| **Oportunidad** | Algo positivo que se puede aprovechar | Cliente que pide ampliar contrato |
| **Riesgo** | Algo negativo que puede empeorar si no se actúa | Cliente que deja de responder |
| **Umbral** | Un dato cruza un límite predefinido | Stock por debajo del mínimo |
| **Patrón** | Una tendencia que se repite | Tres clientes pidiendo la misma feature |
| **Conflicto** | Datos contradictorios entre cerebros | Precio diferente en Sales Brain y Company Brain |

---

## Señales monitorizadas

### Señal: [COMPLETAR — nombre descriptivo]

- **Tipo:** [oportunidad / riesgo / umbral / patrón / conflicto]
- **Descripción:** [COMPLETAR — qué ocurre exactamente]
- **Condición de activación:** [COMPLETAR — cuándo se considera que la señal se ha activado]
- **Fuente:** [COMPLETAR — de dónde viene la información]
- **Impacto:** [bajo / medio / alto / crítico]
- **Acción requerida:** [COMPLETAR — qué hacer cuando se activa]
- **Responsable:** [COMPLETAR — quién debe actuar]
- **Escalado:** [COMPLETAR — a quién se escala si no se resuelve en el plazo definido]
- **Plazo de respuesta:** [COMPLETAR — en cuánto tiempo se debe actuar]
- **Sube al Company Brain:** [sí / no — y por qué]

---

### Señal: [COMPLETAR — nombre descriptivo 2]

[Repetir la misma estructura]

---

## Reglas de escalado

| Impacto | Plazo de respuesta | Escalado si no se resuelve | Notificación |
|---------|-------------------|---------------------------|-------------|
| **Bajo** | 1 semana | Owner del departamento | Registro en el cerebro |
| **Medio** | 48 horas | Owner del departamento + operador | Notificación al operador |
| **Alto** | 24 horas | Operador + Company Brain | Notificación urgente |
| **Crítico** | Inmediato | Operador + CEO | Notificación inmediata a todos los implicados |

---

## Ejemplo — Señales del Sales Brain de Meridian Foods

### Señal: Cliente grande en riesgo de churn

- **Tipo:** riesgo
- **Descripción:** Un cliente con facturación anual superior a 50.000 euros muestra señales de desvinculación.
- **Condición de activación:** El cliente no ha hecho pedido en 30 días (cuando su frecuencia habitual es menor), O ha expresado insatisfacción, O ha solicitado cotización a un competidor.
- **Fuente:** CRM (frecuencia de pedidos) + Email de clientes + Reuniones de seguimiento
- **Impacto:** alto
- **Acción requerida:** El comercial asignado contacta al cliente en 24h para entender la situación. Se prepara un Context Packet con historial completo del cliente.
- **Responsable:** Comercial asignado + Carlos Martín
- **Escalado:** Si no hay respuesta del cliente en 48h, escalar a Carlos Martín. Si el riesgo se confirma, sube al Company Brain.
- **Plazo de respuesta:** 24 horas
- **Sube al Company Brain:** Sí — afecta MRR proyectado y puede requerir decisión estratégica.

### Señal: Competidor baja precios

- **Tipo:** riesgo
- **Descripción:** Un competidor directo ha reducido precios en productos que compiten con los nuestros.
- **Condición de activación:** Se confirma por al menos dos fuentes independientes (cliente, web del competidor, feria, prensa).
- **Fuente:** Email de clientes + Informes de ferias + Vigilancia de mercado
- **Impacto:** alto
- **Acción requerida:** Documentar el cambio con evidencia. Analizar impacto en pipeline actual. Preparar informe para el Director Comercial.
- **Responsable:** Carlos Martín
- **Escalado:** Sube al Company Brain para decisión de pricing.
- **Plazo de respuesta:** 48 horas
- **Sube al Company Brain:** Sí — puede requerir ajuste de pricing global.

### Señal: Tres o más clientes piden la misma feature

- **Tipo:** patrón
- **Descripción:** Varios clientes o leads solicitan una funcionalidad o producto que no existe actualmente.
- **Condición de activación:** La misma necesidad aparece en 3 o más conversaciones independientes en un período de 30 días.
- **Fuente:** CRM (notas de objeciones) + Email de clientes + Reuniones de seguimiento
- **Impacto:** medio
- **Acción requerida:** Documentar la necesidad con detalle y enviar señal al Product Brain.
- **Responsable:** Comercial que detecta el patrón
- **Escalado:** Si Product no responde en 1 semana, Carlos Martín escala al operador.
- **Plazo de respuesta:** 1 semana
- **Sube al Company Brain:** No directamente. Sube al Product Brain, que decide si sube al Company Brain.

### Señal: Propuesta enviada sin verificar stock

- **Tipo:** riesgo
- **Descripción:** Se detecta que una propuesta fue enviada a un cliente sin haber verificado la disponibilidad de stock.
- **Condición de activación:** Campo `stock_verificado = false` en una propuesta con estado `enviada`.
- **Fuente:** CRM (campo de propuesta)
- **Impacto:** medio
- **Acción requerida:** Verificar stock inmediatamente. Si no hay stock, contactar al cliente para ajustar plazos. Registrar como incidencia.
- **Responsable:** Comercial que envió la propuesta
- **Escalado:** Carlos Martín si la propuesta es de más de 10.000 euros.
- **Plazo de respuesta:** 24 horas
- **Sube al Company Brain:** No, salvo que afecte a un compromiso ya registrado en el Company Brain.

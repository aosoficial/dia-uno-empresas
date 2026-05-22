# Mapa de fuentes de verdad (Source-of-Truth Map)

Plantilla pública para documentar qué sistemas ya guardan verdad operativa del negocio, quién los gestiona y qué permisos tienen humanos y agentes.

## Para quién es esto

Un operador que ya tiene:

- instancia privada creada con el wizard;
- `company/company-brain.md` con propósito, oferta y owner rellenados.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md).

## Qué produce

Un archivo `company/source-of-truth-map.md` en tu instancia privada con:

1. Inventario de sistemas existentes con propietario, permisos y frescura.
2. Reglas de acceso para agentes (lectura, escritura, acción).
3. Reglas de privacidad y receipt por sistema.
4. Siguiente acción concreta por sistema.

Este artefacto es obligatorio antes de crear el primer Context Packet. Sin él, el agente no sabe de dónde viene la información ni qué puede tocar.

---

## Reglas de seguridad

- Empieza en solo lectura. No des acceso de escritura o acción a agentes hasta que un humano apruebe la conexión exacta, el alcance y el plan de rollback.
- No guardes credenciales, tokens, claves privadas, contraseñas, secretos ni datos de producción en este archivo.
- Para soporte público, anonimiza todo. Comparte solo ejemplos sintéticos o resúmenes seguros.
- Si te bloqueas, usa DIA UNO en `diauno.io` con un reporte anonimizado.

---

## Cómo rellenar esta plantilla

1. Copia esta plantilla a tu instancia privada: `company/source-of-truth-map.md`.
2. Recorre la tabla sistema por sistema. Para cada uno que ya usas, rellena las columnas.
3. Para sistemas que no usas, borra la fila o déjala vacía.
4. Marca al menos un sistema como fuente de verdad (`sí` o `parcial`) antes de crear el primer Context Packet.
5. Confirma que el acceso del agente es `solo lectura` o `sin acceso` para el primer loop.
6. Después del primer loop, actualiza la columna "Frescura / última revisión".

---

## Tabla de sistemas

| Sistema | Propietario | Datos que contiene | ¿Fuente de verdad? | Permiso lectura agente | Permiso escritura/acción agente | Cadencia de revisión | Frescura / última revisión | Regla de receipt | Riesgos | Siguiente acción |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Drive / Docs | (propietario) | (propuestas, SOPs, políticas, briefs) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (manual/semanal/mensual) | (fecha última revisión) | (enlazar documento, versión, revisor en receipt) | (archivos de cliente, docs obsoletos, carpeta incorrecta) | (identificar carpetas canónicas) |
| Notion / wiki | (propietario) | (base de conocimiento, decisiones, procesos) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (manual/semanal) | (fecha última revisión) | (enlazar página, fecha edición, output revisado) | (páginas abandonadas, docs conflictivos) | (elegir top 5 páginas para primer Context Packet) |
| Hojas de cálculo | (propietario) | (métricas, pipeline, capacidad, finanzas) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (manual/semanal/mensual) | (fecha última revisión) | (enlazar hoja/tab, fecha snapshot, filas usadas) | (fórmulas rotas, exports obsoletos, datos sensibles) | (crear snapshot de solo lectura) |
| CRM | (propietario) | (leads, oportunidades, cuentas, contactos) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (diario/semanal/manual) | (fecha última revisión) | (query/filtro, objetos, número de registros, revisor) | (privacidad de clientes, envío accidental, duplicados) | (resumen de pipeline solo lectura) |
| WhatsApp / Slack | (propietario) | (discusiones de equipo, mensajes de clientes) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (tiempo real/manual) | (fecha última revisión) | (canal/hilo/rango, participantes, resumen, aprobación) | (mensajes privados, decisiones informales, envío accidental) | (solo snippets exportados/reenviados) |
| Email | (propietario) | (peticiones de clientes, aprobaciones, facturas) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (diario/manual) | (fecha última revisión) | (IDs/rango, propietario buzón, resumen, revisor) | (PII, hilos confidenciales, adjuntos) | (snippets anonimizados o búsqueda aprobada solo lectura) |
| Calendario | (propietario) | (reuniones, agendas, decisiones, grabaciones) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (tiempo real/semanal) | (fecha última revisión) | (evento, asistentes, notas, acción, revisor) | (datos sensibles de asistentes, consentimiento grabación) | (usar solo agenda/notas hasta aprobación) |
| Gestión de proyectos | (propietario) | (tareas, estados, owners, deadlines) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (diario/semanal/manual) | (fecha última revisión) | (board/filtro, items usados, cambios propuestos, revisor) | (estado incorrecto, duplicados, sobre-automatización) | (revisión de riesgo solo lectura) |
| Finanzas / facturas | (propietario) | (facturas, pagos, costes, cashflow, impuestos) | (sí/no/parcial) | (sin acceso/solo lectura/aprobación requerida) | (sin acceso/aprobación requerida) | (semanal/mensual/manual) | (fecha última revisión) | (fecha export, informe, totales, revisor financiero) | (datos muy sensibles, impacto legal/fiscal, acciones de pago) | (resúmenes aprobados; sin acciones de pago) |

---

## Checklist de evidencia para primer loop

- [ ] Al menos un sistema marcado como fuente de verdad `sí` o `parcial`.
- [ ] Cada sistema usado tiene propietario y regla de frescura.
- [ ] Acceso del agente es solo lectura o basado en contexto pegado por el operador.
- [ ] Permiso de escritura/acción está en `sin acceso` o `aprobación requerida`.
- [ ] `context-packets/initial-company-context.md` enlaza este mapa y nombra las filas/fuentes usadas.
- [ ] `receipts/first-loop.md` captura fuente, frescura, permiso, revisión humana, resultado y siguiente acción.

---

## Log de aprobaciones de conexión/acción

| Fecha | Conexión/acción aprobada | Aprobador | Alcance exacto | Rollback | Receipt |
| --- | --- | --- | --- | --- | --- |
| (fecha) | (ninguna todavía) | (nombre/rol) | (sistema, carpetas, operación, ventana temporal) | (cómo revocar acceso o revertir) | (receipts/fecha-loop.md) |

---

## Reglas

- No marques un sistema como "fuente de verdad" si no has verificado que los datos están actualizados.
- No uses datos de clientes reales en este archivo si está en un repositorio público.
- Si un sistema cambia de propietario o permisos, crea un StateChange.
- Enlaza este archivo desde `company/company-brain.md` y desde el primer Context Packet.

# Límites de aprobación

Plantilla para definir qué puede hacer el sistema operativo AI-First sin pedir permiso y qué debe escalar a una persona.

## Para quién es esto

Un operador que ya tiene:

- `company/company-brain.md` con owner y prioridades;
- `company/org-chart.md` con roles/personas/agentes;
- al menos un empleado digital o workflow interno planificado.

Si no tienes esto, vuelve a [`START_HERE.md`](../../START_HERE.md).

## Qué produce

Un archivo `company/approval-boundaries.md` en tu instancia privada con:

1. Acciones permitidas por defecto.
2. Acciones prohibidas.
3. Acciones que requieren aprobación humana.
4. Quién aprueba cada tipo de riesgo.
5. Evidencia mínima para aprobar.

---

## Regla base

```text
External/public/economic/legal/production/sensitive actions require human approval.
```

En español práctico: pide aprobación antes de contactar a alguien externo, publicar, gastar dinero, asumir compromisos legales/económicos, tocar producción, usar datos sensibles o conectar herramientas críticas.

---

## Acciones permitidas por defecto

| Acción | Permitida sin aprobación | Evidencia requerida |
|--------|--------------------------|--------------------|
| Ordenar información local segura | Sí | Context Packet o nota de trabajo |
| Redactar borradores internos | Sí | Borrador marcado como no enviado |
| Analizar documentación sintética o anonimizada | Sí | Fuente y frescura documentadas |
| Preparar checklist/SOP/scorecard | Sí | Archivo local y owner |
| Proponer próximos pasos | Sí | Recomendación con riesgos |

---

## Acciones que requieren aprobación humana

| Tipo de acción | Ejemplos | Aprueba | Evidencia mínima antes de aprobar |
|----------------|----------|---------|-----------------------------------|
| Externa | enviar email, DM, formulario, llamada | Owner comercial/operativo | borrador, destinatario, motivo, riesgo |
| Pública | publicar web, post, repo, anuncio | Dirección / Owner | texto final, claim review, privacidad |
| Económica | gastar, contratar, facturar, comprometer precio | Dirección / Finanzas | importe, proveedor, objetivo, límite |
| Legal | contrato, condiciones, promesa contractual | Dirección / Legal | documento, riesgo, versión revisada |
| Producción | deploy, cambiar sistemas cliente, tocar datos reales | Owner técnico/operativo | rollback, entorno, impacto, ventana |
| Sensible | datos personales, clientes, salud, finanzas, credenciales | Dirección / DPO/Responsable | base legal/permiso, minimización, destino |
| Herramientas críticas | conectar CRM, email, pagos, APIs, permisos admin | Owner de herramienta | alcance, permisos, revocación, auditoría |

---

## Acciones prohibidas

- Usar secretos, contraseñas, API keys o tokens en prompts o documentación pública.
- Publicar datos reales de clientes en el repo público.
- Enviar mensajes externos sin aprobación explícita.
- Gastar dinero o aceptar compromisos económicos sin aprobación.
- Cambiar producción sin owner, plan de rollback y receipt.
- Declarar “Punto B operativo” solo porque existen archivos generados.

---

## Matriz por rol

| Rol | Puede hacer solo | Debe pedir aprobación para | Nunca puede hacer |
|-----|------------------|----------------------------|------------------|
| Dirección / Owner | priorizar, aprobar, cerrar decisiones | n/a | ignorar privacy/security review |
| Operaciones | preparar workflows, revisar receipts | producción, clientes, cambios de alcance | comprometer legal/económico sin owner |
| Ventas | preparar propuestas/borradores | enviar propuesta, precio, descuentos | prometer resultados garantizados |
| Agente digital | redactar, analizar, preparar, resumir | externo, público, económico, legal, producción, sensible | aprobar, enviar, gastar, publicar |

---

## Checklist antes de aprobar

Antes de aprobar una acción de riesgo, confirma:

- ¿Qué acción exacta se va a ejecutar?
- ¿Quién es el owner humano?
- ¿Qué fuente/procedencia sostiene la decisión?
- ¿La información está fresca?
- ¿Hay datos sensibles o secretos?
- ¿Cuál es el resultado esperado?
- ¿Cuál es el rollback o forma de detenerlo?
- ¿Dónde se guardará el receipt/evidencia?

---

## Receipt mínimo de aprobación

Después de una aprobación/acción, crea o actualiza un Receipt con:

- acción ejecutada;
- aprobador humano;
- fecha/hora;
- fuente/procedencia;
- evidencia observada;
- resultado;
- riesgos restantes;
- próximo paso.

---

## Cadencia de revisión

| Cadencia | Qué revisar | Quién |
|----------|-------------|-------|
| Mensual | límites, permisos activos, herramientas conectadas | Dirección / Owner |
| Cada nuevo agente | permisos, acciones prohibidas, handoff humano | Owner del departamento |
| Cada incidente | qué falló, qué límite se ajusta, StateChange | Owner + responsable afectado |

---

## Reglas

- Si dudas, escala a humano.
- Un agente digital nunca aprueba su propio trabajo.
- La aprobación debe quedar documentada antes o junto al Receipt.
- Usa ejemplos sintéticos en repos públicos; contexto real solo en instancia privada.

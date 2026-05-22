# Cómo hacer onboarding de un empleado digital

Guía para integrar un empleado digital ya creado en la cadencia operativa del negocio: primera tarea, primer Context Packet, primera revisión y primer Receipt.

## Para quién es esto

Un operador que ya tiene:

- un empleado digital creado con [`create-first-digital-employee.md`](create-first-digital-employee.md) (SOUL.md + PERMISSIONS.md + scorecard);
- el agente conectado a un departamento y registrado en `company/org-chart.md`;
- `company/approval-boundaries.md` rellenado;
- `company/source-of-truth-map.md` con al menos una fuente revisada.

Si no tienes esto, completa primero [`create-first-digital-employee.md`](create-first-digital-employee.md).

## Qué produce

Al final de este how-to tendrás:

1. Un empleado digital operando dentro del sistema (no como herramienta suelta).
2. Su primer Context Packet recibido y ejecutado.
3. Su primer Receipt con resultado revisado por humano.
4. Su scorecard con al menos un dato real.
5. Una cadencia definida para asignarle tareas y revisarlas.

---

## Diferencia entre crear y hacer onboarding

| Crear (`create-first-digital-employee.md`) | Onboarding (esta guía) |
|---|---|
| Definir SOUL, PERMISSIONS, scorecard | Integrar en la cadencia operativa |
| Registrar en org-chart y department brain | Asignar primera tarea real |
| Configurar herramientas y memoria | Ejecutar primer loop con receipt |
| Resultado: agente listo para operar | Resultado: agente operando con evidencia |

---

## Paso 1 — Verificar checklist de activación

Antes de asignar la primera tarea, confirma que el agente pasó la checklist de activación de [`create-first-digital-employee.md`](create-first-digital-employee.md):

- [ ] SOUL.md completo (9 secciones, sin placeholders)
- [ ] PERMISSIONS.md completo (5+ acciones con niveles)
- [ ] Owner humano asignado y referenciado
- [ ] Departamento asignado
- [ ] Scorecard definido (3+ métricas)
- [ ] Aparece en `company/org-chart.md`
- [ ] Aparece en `departments/[departamento]/department-brain.md`
- [ ] `company/approval-boundaries.md` cubre las acciones del agente
- [ ] `company/source-of-truth-map.md` identifica las fuentes que usará

Si falta algo, no continúes. Completa primero.

**Criterio de salida:** todos los checks pasan.

---

## Paso 2 — Elegir la primera tarea de onboarding

La primera tarea de onboarding debe ser:

- **Pequeña:** completable en una sesión.
- **Interna:** sin contacto externo, publicación, gasto ni acceso a datos sensibles.
- **Verificable:** produce un output que un humano puede revisar.
- **Útil:** resuelve un problema real del negocio (no un ejercicio de prueba).

| Tipo de empresa | Buena primera tarea | Mala primera tarea |
|---|---|---|
| Agencia | Redactar checklist de entrega para un tipo de proyecto | Enviar propuesta a cliente |
| Consultoría | Preparar borrador de agenda de diagnóstico | Agendar reunión con prospecto |
| Freelancer | Clasificar servicios en tabla de oferta | Publicar nueva página de precios |

**Criterio de salida:** tarea concreta con output verificable, 100% interna.

---

## Paso 3 — Crear el Context Packet de onboarding

Usa [`create-first-context-packet.md`](create-first-context-packet.md) para crear un Context Packet específico para esta tarea.

Campos que deben ser específicos del agente:

```yaml
target: "[nombre-del-agente]"  # no genérico
permissions:
  autonomo:
    - "[copiados de PERMISSIONS.md — nivel 1]"
  requiere_aprobacion:
    - "[copiados de PERMISSIONS.md — nivel 2-3]"
  prohibido:
    - "[copiados de PERMISSIONS.md — nivel 4]"
```

Verifica que el Context Packet referencia el `company/source-of-truth-map.md` para las fuentes usadas.

**Criterio de salida:** Context Packet con target = nombre del agente, permisos alineados con PERMISSIONS.md, fuentes trazables al source-of-truth map.

---

## Paso 4 — Ejecutar la primera tarea

Entrega el Context Packet al agente y deja que ejecute la tarea.

Reglas de supervisión para la primera vez:

1. Observa cómo interpreta las instrucciones.
2. Verifica que respeta los límites de PERMISSIONS.md.
3. Si pide algo que no está en el Context Packet, no improvises — completa el Context Packet primero.
4. Si intenta una acción fuera de permisos, para y documenta el incidente.

**Criterio de salida:** output generado y guardado en la instancia privada.

---

## Paso 5 — Revisión humana del primer output

El owner del agente revisa el output:

| Pregunta | Respuesta |
|---|---|
| ¿El output cumple lo que pedía el Context Packet? | (sí/parcial/no) |
| ¿Se respetaron las restricciones de PERMISSIONS.md? | (sí/no — si no, crear StateChange) |
| ¿Las fuentes usadas coinciden con el source-of-truth map? | (sí/no) |
| ¿El output es correcto y útil para el negocio? | (sí/parcial/no) |
| ¿Hubo algún comportamiento inesperado? | (describir) |

Anota el veredicto: correcto, parcial o incorrecto.

**Criterio de salida:** revisión humana completada con veredicto documentable.

---

## Paso 6 — Escribir el Receipt de onboarding

Usa [`create-first-receipt.md`](create-first-receipt.md) para documentar el resultado.

Campos específicos del onboarding:

```yaml
id: "rcp-[nombre-agente]-onboarding-[fecha]-001"
agent: "[nombre-del-agente]"
action: "[primera tarea ejecutada]"
inputs:
  context_packet: "[id del Context Packet del paso 3]"
  source_of_truth_map: "company/source-of-truth-map.md"
  permissions: "digital-employees/[nombre]/PERMISSIONS.md"
outcome: "[resultado real observado — no solo 'completado']"
verificacion:
  verificado_por: "[owner humano]"
  resultado_verificacion: "[correcto/parcial/incorrecto]"
  incidentes_permisos: "[ninguno / descripción]"
```

**Criterio de salida:** Receipt con referencia al Context Packet, source map, permissions y revisión humana.

---

## Paso 7 — Actualizar el scorecard del agente

Abre el scorecard del agente (en SOUL.md o SCORECARD.md):

- Actualiza "Tareas completadas por sprint": de 0 a 1.
- Actualiza "Tasa de aceptación en revisión": según el veredicto del paso 5.
- Actualiza "Incidentes fuera de permisos": 0 si no hubo, o el número observado.

Actualiza también `company/company-scorecard.md` si aplica.

**Criterio de salida:** al menos una métrica del scorecard tiene valor real con fecha y fuente (receipt).

---

## Paso 8 — Definir cadencia operativa del agente

Define cuándo y cómo el agente recibirá tareas:

| Aspecto | Decisión |
|---|---|
| Frecuencia de tareas | (por sprint / diario / bajo demanda) |
| Quién asigna tareas | (owner del departamento) |
| Cómo se asignan | (Context Packet cada vez / instrucción directa para tareas repetibles) |
| Revisión de output | (owner revisa cada output / solo muestreo después de 5+ tareas exitosas) |
| Actualización de scorecard | (cada sprint / cada tarea) |
| Escalación | (a quién escala si se bloquea o actúa fuera de permisos) |

Documenta esta cadencia en el `department-brain.md` del departamento correspondiente.

**Criterio de salida:** cadencia documentada en department brain con frecuencia, asignador, revisor y escalación.

---

## Paso 9 — Verificar integración completa

Checklist final de onboarding:

- [ ] Primera tarea completada con Context Packet
- [ ] Output revisado por humano con veredicto
- [ ] Receipt escrito con referencia a Context Packet y source map
- [ ] Scorecard actualizado con dato real
- [ ] Cadencia operativa definida en department brain
- [ ] Si hubo incidente de permisos, StateChange creado
- [ ] Siguiente tarea identificada

Si todo pasa, el agente está onboarded.

---

## Errores comunes

| Error | Por qué falla | Solución |
|---|---|---|
| Asignar tarea sin Context Packet | El agente improvisa sin contexto ni límites | Siempre crea Context Packet antes de la primera tarea |
| No revisar el primer output | Sin feedback, no sabes si el agente interpreta bien | La primera revisión es obligatoria |
| Saltar el receipt | No hay evidencia de que el onboarding funcionó | El receipt cierra el loop de onboarding |
| No actualizar scorecard | El agente opera sin métricas observables | Al menos una métrica real tras la primera tarea |
| Confiar permisos sin verificar | El agente puede escalar a acciones no autorizadas | Verifica que PERMISSIONS.md coincida con lo que hace |
| Onboard múltiples agentes a la vez | Dispersión; ninguno tiene feedback real | Onboard uno, completa el loop, evalúa si necesitas otro |

---

## Siguiente paso

Después del onboarding, ejecuta el primer loop interno completo: [`run-first-internal-loop.md`](run-first-internal-loop.md).

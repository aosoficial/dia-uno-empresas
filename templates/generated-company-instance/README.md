# Instancia privada de Company Brain

Esta carpeta es la copia privada de trabajo para `{{ company_name }}`. Es un espacio operativo: aquí se completa contexto real, se guardan decisiones revisadas y se conserva evidencia del primer ciclo.

## Regla de privacidad antes de empezar

- No subas esta instancia a un repositorio público.
- No pegues secretos, claves API, contraseñas, datos de clientes, importes sensibles ni información personal innecesaria.
- Usa `.env` o un gestor de secretos fuera de Git para credenciales reales. `secrets/` solo contiene instrucciones.
- Si pides ayuda externa, comparte solo contexto anonimizado y sintético. El canal de ayuda/comunidad es DIA UNO: `diauno.io`.

## Qué rellenar primero

Trabaja en este orden. No intentes activar muchos agentes a la vez: el objetivo inicial es llegar a un Punto B mínimo con una sola porción operativa revisada por una persona.

1. Lee `MAP.md` y `AGENTS.md`.
2. Completa Dirección/Mother Brain en `company/company-brain.md` con hechos verificados: propósito, modelo de negocio, metas, prioridades, sistemas en alcance y preguntas abiertas.
3. Completa `company/source-of-truth-map.md`. Es un artefacto obligatorio de los primeros 120 minutos y la fuente principal para el primer Context Packet: identifica Drive/Docs, Notion/wiki, Sheets, CRM, WhatsApp/Slack, email, calendario, proyectos y finanzas con propietario, permisos, frescura, regla de recibo y siguiente acción.
4. Revisa límites de aprobación en `company/approval-boundaries.md`. Nada externo, público, económico, legal, de producción o sensible se ejecuta sin aprobación humana explícita.
5. Elige un primer departamento prioritario y completa su brain, por ejemplo `departments/{{ first_department }}/department-brain.md` o `departments/operations/department-brain.md`.
6. Revisa permisos del primer empleado digital. La ruta inicial habitual es `digital-employees/ceo-operations-assistant/PERMISSIONS.md`; si el wizard generó otro empleado, usa su carpeta dentro de `digital-employees/`.
7. Crea o completa un paquete de contexto en `context-packets/initial-company-context.md` antes de pedir trabajo al agente. Debe enlazar `company/source-of-truth-map.md`, nombrar las filas usadas y mantener el acceso en solo lectura salvo aprobación explícita.
8. Ejecuta una acción interna pequeña y segura: resumir un handoff, revisar una SOP, preparar una lista de riesgos, actualizar una métrica interna, etc.
9. Guarda evidencia del ciclo en `receipts/first-loop.md` o en otro archivo dentro de `receipts/`.
10. Si cambió el estado operativo, registra el cambio en `statechanges/`.
11. Actualiza `company/company-scorecard.md` con una línea basada en evidencia, no en intención.
12. Actualiza `company/guided-pilot-plan.md`, `company/point-b-readiness.md` y `roadmap/48h-7d-30d.md` con el siguiente sprint.
13. Ejecuta validaciones en modo scaffold primero. Usa modo operational solo después del primer ciclo humano revisado.

## Secuencia de 48 horas hacia Punto B

### 0–30 minutos — orientar la instancia

- Confirmar que esta carpeta es privada.
- Leer `MAP.md`, `AGENTS.md` y esta guía.
- Marcar qué datos no se pueden usar con agentes.
- Abrir `company/approval-boundaries.md` y dejar claras las puertas de aprobación.
- Abrir `company/source-of-truth-map.md` y marcar sistemas existentes, propietarios y permisos iniciales.

### 30–90 minutos — completar dirección y primer corte

- Completar `company/company-brain.md` con propietario, fuente/procedencia, vigencia/frescura, aprobación y evidencia cuando aplique.
- Completar `company/source-of-truth-map.md` con al menos una fuente segura, su frescura, permiso de lectura, regla de recibo y siguiente acción.
- Revisar `company/company-scorecard.md` y dejar valores desconocidos como `unknown` si todavía no hay evidencia.
- Seleccionar el primer departamento en `departments/*/department-brain.md`.
- Revisar `digital-employees/*/PERMISSIONS.md` antes de pedir cualquier acción.

### 90–180 minutos — preparar el primer ciclo interno

- Completar `context-packets/initial-company-context.md` con objetivo, alcance, fuentes, supuestos, riesgos, acciones permitidas, acciones prohibidas y resultado esperado. Debe usar `company/source-of-truth-map.md` como fuente de sistemas/permisos.
- Ejecutar solo una acción interna, reversible y no sensible.
- No contactar clientes, no publicar, no gastar dinero, no tocar producción y no usar datos sensibles sin aprobación humana explícita.

### 3–6 horas — cerrar evidencia

- Crear `receipts/first-loop.md` con:
  - acción realizada;
  - contexto usado, enlazando `context-packets/initial-company-context.md`;
  - resultado observado;
  - revisión/aprobación humana;
  - evidencia enlazada;
  - siguiente acción.
- Si el ciclo cambió responsabilidades, métricas, workflow o decisión operativa, crear un registro en `statechanges/`.
- Actualizar `company/company-scorecard.md` con la métrica o señal observada.

### 6–48 horas — seleccionar siguiente sprint

- Actualizar `company/guided-pilot-plan.md` con el siguiente sprint.
- Revisar `company/point-b-readiness.md` como diagnóstico, no como prueba automática.
- Actualizar `roadmap/48h-7d-30d.md` con próximos pasos.
- Repetir validadores y corregir faltantes antes de afirmar Punto B.

## Evidencia mínima de Punto B

La definición vive en `docs/42_point_b_definition.md` del framework. Dentro de esta instancia, las pruebas mínimas deben apuntar a:

- Dirección/Mother Brain: `company/company-brain.md`
- Mapa de fuentes/sistemas: `company/source-of-truth-map.md`
- Límites de aprobación: `company/approval-boundaries.md`
- Scorecard: `company/company-scorecard.md`
- Plan del piloto / siguiente sprint: `company/guided-pilot-plan.md`
- Diagnóstico Punto B: `company/point-b-readiness.md`
- Primer departamento: `departments/<department>/department-brain.md`
- Permisos del empleado digital: `digital-employees/<employee>/PERMISSIONS.md`
- Paquete de contexto usado: `context-packets/initial-company-context.md` o `context-packets/`
- Recibo operativo: `receipts/first-loop.md` o `receipts/`
- Cambios de estado, cuando existan: `statechanges/`
- Roadmap operativo: `roadmap/48h-7d-30d.md`

## Validación: scaffold vs operational

Desde el repositorio del framework, ejecuta:

```bash
python3 scripts/verify_installation.py /ruta/a/esta-instancia
python3 scripts/validate_point_b_readiness.py --mode scaffold /ruta/a/esta-instancia
```

El modo `scaffold` debe pasar en una instancia recién generada: solo comprueba que existe la estructura mínima.

No ejecutes ni interpretes como error de instalación este comando hasta completar el primer ciclo interno con revisión humana:

```bash
python3 scripts/validate_point_b_readiness.py --mode operational /ruta/a/esta-instancia
```

En una instancia recién generada, `--mode operational` debe fallar. Es correcto: todavía no hay evidencia real de trabajo interno, recibo operativo, scorecard actualizado y siguiente sprint revisado.

## Si te bloqueas

1. Revisa `docs/TROUBLESHOOTING.md` en el repositorio del framework.
2. Reduce el alcance a un solo departamento, un solo contexto y una sola acción interna.
3. No compartas la instancia completa ni datos privados.
4. Para ayuda, usa DIA UNO en `diauno.io` con contexto anonimizado: describe el síntoma, comando, salida relevante y qué archivos de evidencia existen, sin secretos ni datos de clientes.

## Estructura de la instancia

- `company/`: memoria operativa de compañía, mapa de fuentes/sistemas, aprobación, scorecard y planes.
- `departments/`: brains departamentales, workflows y SOPs.
- `digital-employees/`: permisos, memoria y runtime packs de empleados digitales.
- `context-packets/`: contexto cargado antes de trabajar.
- `receipts/`: evidencia de trabajo completado.
- `statechanges/`: cambios de estado operativo.
- `handoffs/`: traspasos entre sesiones o equipos.
- `contracts/`: contratos de trabajo acotados.
- `traces/`: referencias técnicas o de depuración.
- `secrets/`: instrucciones solamente; nunca guardes secretos reales aquí.

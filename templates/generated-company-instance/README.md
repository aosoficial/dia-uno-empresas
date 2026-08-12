# Instancia privada DIA UNO Empresas

Esta carpeta es la copia privada de trabajo para `{{ company_name }}`. Se ha generado en modo `{{ method_mode }}` y su estado inicial es **scaffold, no empresa operativa**.

## Elige la capa que corresponde

- En modo `people`, organiza la empresa con `personas/` y no se instalan departamentos ni empleados digitales.
- En modo `hybrid`, empieza igualmente por `personas/`; usa `departments/` y `digital-employees/` solo después de que una capacidad tenga dueño, SOP, entradas, salida, métrica, autoridad y fallback.
- `METHOD.json` registra el modo de la instancia y el responsable humano.

## Regla de privacidad antes de empezar

- No subas esta instancia a un repositorio público.
- No pegues secretos, claves API, contraseñas, datos de clientes, importes sensibles ni información personal innecesaria.
- Usa `.env` o un gestor de secretos fuera de Git para credenciales reales. `secrets/` solo contiene instrucciones.
- Si pides ayuda externa, comparte solo contexto anonimizado y sintético. El canal de ayuda/comunidad es DIA UNO: `diauno.io`.

## Qué rellenar primero

Trabaja en este orden. Los pasos 1–7 son válidos para ambos modos. Los pasos de agentes se aplican solo al modo `hybrid`.

1. Lee `METHOD.json`, `MAP.md` y `AGENTS.md`.
2. Abre `personas/README.md` y revisa `personas/metodo-v3/INVENTARIO.md`.
3. Completa Rumbo y nombra a su responsable humano.
4. Completa capacidades, organigrama de asientos, fichas de puesto, matriz de decisiones y evaluación.
5. Completa procesos críticos y SOP; después instala caja, ejecución, indicadores, aprendizaje y reuniones.
6. Actualiza `company/people-organization-plan.md` y `company/people-readiness.md` con evidencia real.
7. Ejecuta `python3 scripts/validate_people_readiness.py /ruta/a/esta-instancia` desde el framework. Esto valida la instalación, no la implantación.
8. **Solo en modo `hybrid`:** confirma ORGO, memoria y la interfaz humana aprobada antes de lanzar un agente.
9. **Solo en modo `hybrid`:** crea o revisa el primer empleado digital para una capacidad madura de Dirección.
10. **Solo en modo `hybrid`:** prepara Slack con `integrations/slack-first-agent.md` si es la interfaz elegida y aprobada. Slack no es memoria.
11. Solo después crea/completa los brains de departamento, por ejemplo `departments/{{ first_department }}/department-brain.md`.
12. Define Observer agent como observador de memoria/sistema: detecta huecos, contradicciones, receipts faltantes y cambios que deberían entrar al cerebro; no ejecuta negocio directamente.
13. Abre `FIRST_OPERATING_LOOP.md`. Es la guía corta para ejecutar el primer ciclo real de 30–60 minutos sin confundirse entre scaffold y Punto B operativo. Si necesitas ver la forma antes de usar datos reales, abre `examples/first-operating-loop/README.md`.
14. Completa `company/source-of-truth-map.md`. Es un artefacto obligatorio de los primeros 120 minutos y la fuente principal para el primer Context Packet: identifica Drive/Docs, Notion/wiki, Sheets, CRM, WhatsApp/Slack, email, calendario, proyectos y finanzas con propietario, permisos, frescura, regla de recibo y siguiente acción.
15. Revisa límites de aprobación en `company/approval-boundaries.md`. Nada externo, público, económico, legal, de producción o sensible se ejecuta sin aprobación humana explícita.
16. Solo en modo `hybrid`, revisa permisos del primer empleado digital dentro de `digital-employees/<employee>/PERMISSIONS.md`. La ruta compatible del scaffold inicial es `digital-employees/ceo/PERMISSIONS.md`; que exista no significa que el agente esté activo.
17. Crea o completa un paquete de contexto en `context-packets/initial-company-context.md` antes de pedir trabajo al agente. Debe enlazar `company/source-of-truth-map.md`, nombrar las filas usadas y mantener el acceso en solo lectura salvo aprobación explícita.
18. Ejecuta una acción interna pequeña y segura: resumir un handoff, revisar una SOP, preparar una lista de riesgos, actualizar una métrica interna, etc.
19. Guarda evidencia del ciclo en `receipts/first-loop.md` o en otro archivo dentro de `receipts/`.
20. Si cambió el estado operativo, registra el cambio en `statechanges/`.
21. Actualiza `company/company-scorecard.md` con una línea basada en evidencia, no en intención.
22. Solo en modo `hybrid`, actualiza `company/guided-pilot-plan.md`, `company/point-b-readiness.md` y `roadmap/48h-7d-30d.md` con el siguiente sprint.
23. Ejecuta validaciones en modo scaffold primero. Usa modo operational solo después del primer ciclo humano revisado.

## Secuencia de 48 horas hacia Punto B

### 0–30 minutos — orientar la instancia

- Confirmar que esta carpeta es privada.
- Leer `MAP.md`, `AGENTS.md` y esta guía.
- Confirmar el modo `people` o `hybrid`.
- Solo en `hybrid`, confirmar ORGO + Codex/Claude como operador instalador.
- Solo en `hybrid`, confirmar Slack-first y memoria privada: Slack conversa, GBrain/Company Brain recuerda.
- Marcar qué datos no se pueden usar con agentes.
- Abrir `company/approval-boundaries.md` y dejar claras las puertas de aprobación.
- Abrir `company/source-of-truth-map.md` y marcar sistemas existentes, propietarios y permisos iniciales.

### 30–90 minutos — completar dirección y primer corte

- Completar `company/company-brain.md` solo para Dirección con propietario, fuente/procedencia, vigencia/frescura, aprobación y evidencia cuando aplique.
- Completar `company/source-of-truth-map.md` con al menos una fuente segura, su frescura, permiso de lectura, regla de recibo y siguiente acción.
- Revisar `company/company-scorecard.md` y dejar valores desconocidos como `unknown` si todavía no hay evidencia.
- Solo en `hybrid`, revisar el agente de la primera capacidad y asegurar que no amplía su alcance a otros departamentos.
- Solo en `hybrid`, dejar otros asientos digitales como propuestas, revisar `digital-employees/*/PERMISSIONS.md` y preparar `integrations/slack-first-agent.md` si aplica. No guardar tokens ni secretos en Git.

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

## Evidencia mínima de Punto B híbrido

La definición vive en `docs/42_point_b_definition.md` del framework. Dentro de esta instancia, las pruebas mínimas deben apuntar a:

- Dirección/Mother Brain: `company/company-brain.md`
- Guía del primer ciclo real: `FIRST_OPERATING_LOOP.md`
- Example kit del primer ciclo: `examples/first-operating-loop/README.md`
- Mapa de fuentes/sistemas: `company/source-of-truth-map.md`
- Límites de aprobación: `company/approval-boundaries.md`
- Scorecard: `company/company-scorecard.md`
- Plan del piloto / siguiente sprint: `company/guided-pilot-plan.md`
- Diagnóstico Punto B: `company/point-b-readiness.md`
- Primer departamento: `departments/<department>/department-brain.md`
- Permisos del empleado digital: `digital-employees/<employee>/PERMISSIONS.md`
- Paquete de contexto usado: `context-packets/initial-company-context.md` o `context-packets/`
- Recibo operativo: `receipts/first-loop.md` o `receipts/`
- Superficie Slack-first: `integrations/slack-first-agent.md`
- Cambios de estado, cuando existan: `statechanges/`
- Roadmap operativo: `roadmap/48h-7d-30d.md`

## Validación: scaffold vs operational

Para ambos modos, desde el repositorio del framework ejecuta:

```bash
python3 scripts/verify_installation.py /ruta/a/esta-instancia
python3 scripts/validate_people_readiness.py /ruta/a/esta-instancia
```

Solo en modo `hybrid`, ejecuta además:

```bash
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
- `personas/`: método humano, inventario y originales preservados.
- `departments/`: solo modo `hybrid`; brains departamentales, workflows y SOPs.
- `digital-employees/`: solo modo `hybrid`; permisos, memoria y runtime packs de empleados digitales.
- `context-packets/`: contexto cargado antes de trabajar.
- `receipts/`: evidencia de trabajo completado.
- `statechanges/`: cambios de estado operativo.
- `handoffs/`: traspasos entre sesiones o equipos.
- `integrations/`: configuración operativa no secreta de superficies como Slack.
- `contracts/`: contratos de trabajo acotados.
- `traces/`: referencias técnicas o de depuración.
- `secrets/`: instrucciones solamente; nunca guardes secretos reales aquí.

# Instancia privada — Personas

Esta carpeta es el espacio privado de trabajo para `{{ company_name }}`. `METHOD.json` registra el modo y el responsable humano.

## Qué hay aquí

- `personas/`: los 36 originales del Método V3, su inventario y sus huellas de integridad.
- `company/company-brain.md`: contexto y Rumbo de la empresa.
- `company/accountability-map.md`: responsables y asientos.
- `company/approval-boundaries.md`: límites de autoridad.
- `company/scorecard.md`: indicadores de empresa.
- `company/operating-cadence.md`: ritmo de revisión.
- `company/people-organization-plan.md`: secuencia de implantación.
- `company/people-readiness.md`: evidencia que aún falta.
- `receipts/` y `statechanges/`: evidencia y cambios revisados.

## Orden de trabajo

1. Lee `AGENTS.md`, `MAP.md` y `personas/README.md`.
2. Revisa `personas/metodo-v3/INVENTARIO.md`.
3. Haz copias de trabajo de los originales; no los sobrescribas.
4. Completa Rumbo.
5. Completa capacidades, organigrama, puestos, decisiones y evaluación.
6. Completa mapa de procesos y SOP.
7. Completa caja, ejecución, indicadores, aprendizaje y reuniones.
8. Nombra responsable humano, fuente, vigencia y cadencia para cada función.
9. Actualiza `company/people-readiness.md` con evidencia real.

## Validar

Desde el repositorio del framework:

```bash
python3 scripts/verify_installation.py /ruta/a/esta-instancia
python3 scripts/validate_people_readiness.py /ruta/a/esta-instancia
```

Estas comprobaciones prueban estructura e integridad. No prueban que la empresa esté organizada u operativa.

## Continuar hacia agentes

Cuando una capacidad tenga responsable, SOP, entradas, salida, métrica, autoridad, evidencia y fallback, puedes ampliar esta misma instancia sin sobrescribir el trabajo humano:

```bash
python3 scripts/company_brain_wizard.py \
  --company "{{ company_name }}" \
  --company-type "{{ company_type }}" \
  --method-mode hybrid \
  --output /ruta/a/esta-instancia \
  --upgrade --yes
```

El upgrade solo añade scaffolds. No conecta credenciales, herramientas, agentes, servicios ni infraestructura.

## Privacidad

- No publiques esta instancia.
- No guardes secretos, credenciales, datos de clientes o información personal innecesaria.
- Usa fuentes verificadas y deja `unknown` cuando un hecho no esté confirmado.

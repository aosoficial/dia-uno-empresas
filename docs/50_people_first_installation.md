# Instalación People-first

## Crear solo Personas

```bash
python3 scripts/company_brain_wizard.py \
  --company "Acme Demo" \
  --company-type agency \
  --method-mode people \
  --owner "Founder" \
  --output /tmp/acme-company \
  --yes

python3 scripts/verify_installation.py /tmp/acme-company
python3 scripts/validate_people_readiness.py /tmp/acme-company
```

La instancia incluye los 36 originales, inventario, hashes, plan de organización, accountability, decisiones, scorecard, cadencia, receipts y StateChanges. No incluye departamentos, empleados digitales, Slack ni skills de agente.

## Ampliar a híbrido

```bash
python3 scripts/company_brain_wizard.py \
  --company "Acme Demo" \
  --company-type agency \
  --method-mode hybrid \
  --owner "Founder" \
  --output /tmp/acme-company \
  --upgrade --yes

python3 scripts/verify_installation.py /tmp/acme-company
python3 scripts/validate_point_b_readiness.py --mode scaffold /tmp/acme-company
```

El upgrade exige una instancia `people` válida, añade archivos faltantes sin sobrescribir los existentes, actualiza `METHOD.json` y deja receipt. No activa agentes, integraciones, credenciales, servicios o infraestructura.

## Rollback

Antes de operar, el rollback lógico es mantener `METHOD.json` y trabajar únicamente con `personas/`; los scaffolds de agente son inertes. Si se quiere retirar físicamente el añadido, restaura la instancia desde la copia privada tomada antes del upgrade. El framework no borra archivos automáticamente para evitar pérdida de trabajo.

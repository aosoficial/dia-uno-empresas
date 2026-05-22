# Troubleshooting self-serve / anti-bloqueo

Guía práctica, Spanish-first, para desbloquear la instalación local de Company Brain System. Usa ejemplos sintéticos y una ruta privada fuera del repo público.

Regla base:

```bash
cd company-brain-system
python3 scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain
```

Si un comando falla, copia el síntoma más parecido y ejecuta la solución segura.

## 1. `python: command not found` / comando Python incorrecto

Síntomas frecuentes:

```text
python: command not found
zsh: command not found: python
bash: python: command not found
```

Qué significa: tu sistema probablemente tiene `python3`, no `python`.

Prueba esto:

```bash
python3 --version
python3 scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain
```

Si `python3 --version` también falla, instala Python 3 desde la fuente oficial de tu sistema o pide ayuda técnica. No pegues secretos ni datos de clientes en la solicitud de ayuda.

## 2. `ModuleNotFoundError: No module named 'yaml'` / falta PyYAML

Síntoma:

```text
ModuleNotFoundError: No module named 'yaml'
```

Qué significa: falta el paquete `pyyaml` en tu Python local.

Arreglo rápido:

```bash
python3 -m pip install pyyaml
python3 scripts/validate_schemas.py
```

Si `pip` no existe:

```bash
python3 -m ensurepip --upgrade
python3 -m pip install pyyaml
```

## 3. `make: command not found` / Make no disponible

Síntomas:

```text
make: command not found
zsh: command not found: make
```

Qué significa: tu equipo no tiene `make` disponible. No necesitas Make para completar el flujo básico.

Usa comandos Python directos:

```bash
python3 scripts/validate_repo.py
python3 scripts/validate_links.py
python3 scripts/validate_public_safety.py
python3 scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain
python3 scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain --yes
python3 scripts/verify_installation.py /tmp/mi-company-brain
python3 scripts/validate_point_b_readiness.py --mode scaffold /tmp/mi-company-brain
```

## 4. `Refusing output inside canonical repo...`

Síntoma exacto:

```text
Refusing output inside canonical repo. Use a private path or --example for synthetic examples.
```

Qué significa: intentaste crear una instancia privada dentro del repo público `company-brain-system`. Eso se bloquea para evitar mezclar datos de empresa con el framework público.

Arreglo recomendado: usa una ruta privada fuera del repo.

```bash
python3 scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain --yes
```

Solo si estás creando un ejemplo sintético para documentación o tests dentro del repo, usa `--example` y datos claramente sintéticos:

```bash
python3 scripts/company_brain_wizard.py --company "Acme Demo" --company-type agency --output examples/acme-demo --example --yes
```

No uses `--example` para datos reales.

## 5. `Refusing to write into non-empty directory...`

Síntoma exacto:

```text
Refusing to write into non-empty directory: /ruta/elegida
```

Qué significa: el wizard no sobrescribe carpetas que ya tienen contenido.

Elige una carpeta nueva:

```bash
python3 scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain-v2 --yes
```

O revisa y mueve manualmente la carpeta anterior antes de repetir. No borres evidencia real si no estás seguro.

## 6. `Unknown departments: ...`

Síntoma:

```text
Unknown departments: ops, growth
```

Qué significa: el nombre de departamento no coincide con los identificadores soportados.

Usa uno o varios de estos valores:

```text
direction, operations-delivery, marketing, sales, customer-success, product-software, finance, people, admin-legal
```

Ejemplo:

```bash
python3 scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --departments direction,operations-delivery,marketing,sales --output /tmp/mi-company-brain
```

También puedes usar todos:

```bash
python3 scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --departments all --output /tmp/mi-company-brain
```

## 7. `Refusing possible secret in --...`

Síntoma:

```text
Refusing possible secret in --company
Refusing possible secret in --point-a
Refusing possible secret in --output
```

Qué significa: el wizard detectó texto con forma de secreto, credencial, token, contraseña, URL de base de datos o clave privada.

Arreglo seguro: quita cualquier secreto y usa contexto general o sintético.

```bash
python3 scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --point-a "Conocimiento disperso; procesos manuales; IA usada de forma puntual." --output /tmp/mi-company-brain
```

No pegues claves API, contraseñas, tokens, datos de clientes, contratos privados ni detalles de producción.

## 8. `verify_installation.py` dice que faltan archivos o carpetas

Síntomas posibles:

```text
Missing required path: company/company-brain.md
Missing required path: departments/direction/department-brain.md
Missing required path: receipts/
```

Qué significa: la instancia privada no está completa o fue modificada.

Arreglo rápido si es una instalación nueva de prueba:

```bash
python3 scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain-nueva --yes
python3 scripts/verify_installation.py /tmp/mi-company-brain-nueva
```

Si es una instancia real, no la sobrescribas. Revisa qué ruta falta, restaura desde backup o copia solo la plantilla equivalente con cuidado y sin publicar datos reales.

## 9. Confusión: `scaffold` vs `operational`

Síntoma habitual: acabas de crear una instancia y esto falla:

```bash
python3 scripts/validate_point_b_readiness.py --mode operational /tmp/mi-company-brain
```

Qué significa: en una instalación fresca, fallar en modo operativo es normal. El scaffold solo demuestra que la estructura existe. El modo operativo exige evidencia de un primer loop interno revisado.

Orden correcto:

```bash
python3 scripts/verify_installation.py /tmp/mi-company-brain
python3 scripts/validate_point_b_readiness.py --mode scaffold /tmp/mi-company-brain
# Después de un primer loop interno revisado por una persona:
python3 scripts/validate_point_b_readiness.py --mode operational /tmp/mi-company-brain
```

Para que `operational` pase, necesitas evidencia real y privada: mapa de fuentes/sistemas revisado, Context Packet, Receipt, scorecard actualizado, límites de aprobación y siguiente sprint.

## 10. Permisos y aprobaciones: qué no puede hacer la IA sin permiso

Si dudas si una acción requiere aprobación, aplica esta regla:

```text
External/public/economic/legal/production/sensitive actions require Approval.
```

En español práctico: pide aprobación humana antes de contactar a alguien externo, publicar, gastar dinero, asumir compromisos legales o económicos, tocar producción, usar datos sensibles o conectar herramientas críticas.

Acciones seguras por defecto: redactar borradores, ordenar información local, analizar contexto seguro, preparar checklists y proponer próximos pasos internos.

## 11. Error de permisos de sistema / no puedo escribir la carpeta

Síntomas frecuentes:

```text
Permission denied
[Errno 13] Permission denied
Operation not permitted
```

Qué significa: la ruta elegida no permite escritura.

Usa una ruta donde tu usuario pueda escribir:

```bash
python3 scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain --yes
```

Evita rutas de sistema como `/`, `/usr`, `/System` o carpetas de otra persona.

## 12. Sigo bloqueado: reporte seguro para DIA UNO

Si te bloqueas, usa DIA UNO en [diauno.io](https://diauno.io) con este reporte:

- [`templates/dia-uno/blocker-report.md`](../templates/dia-uno/blocker-report.md)

Antes de compartirlo, confirma:

- no contiene secretos ni credenciales;
- no contiene datos de clientes;
- no contiene contratos privados;
- no contiene datos sensibles o regulados;
- no contiene detalles de producción, infraestructura o sistemas críticos.

Incluye solo: tipo de empresa, paso donde te bloqueaste, comando ejecutado, salida del error, qué intentaste y qué evidencia existe. Usa datos sintéticos o anonimiza el contexto.

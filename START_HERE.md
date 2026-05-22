# Empieza aquí / START HERE

Este repositorio sirve para instalar una **instancia privada de Company Brain**: el primer corte seguro de un sistema operativo AI-first para tu empresa.

No promete una transformación garantizada. Te ayuda a crear una base ordenada para empezar con seguridad: Dirección / Mother Brain, límites de aprobación, contexto mínimo, un primer departamento, receipts y evidencia revisable.

## Si no eres técnico, sigue este camino primero

Usa el camino self-serve como una lista de pasos. La primera validación debe ser de **scaffold**: comprueba que la estructura está creada, no que la empresa ya opera como Punto B.

Si te bloqueas con Python, Make, `pyyaml`, permisos, carpeta no vacía o validaciones, abre primero [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

```bash
# 1) Simular sin crear nada
git clone https://github.com/aosoficial/company-brain-system.git
cd company-brain-system
python scripts/company_brain_wizard.py --dry-run --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain

# 2) Crear una instancia privada local
python scripts/company_brain_wizard.py --company "Mi Empresa" --company-type agency --output /tmp/mi-company-brain --yes

# 3) Verificar que la instalación existe y tiene la estructura esperada
python scripts/verify_installation.py /tmp/mi-company-brain

# 4) Validar primero en modo scaffold
python scripts/validate_point_b_readiness.py --mode scaffold /tmp/mi-company-brain
```

También puedes usar Make:

```bash
make validate
make demo-agency
make point-b-scaffold INSTANCE=/tmp/company-brain-demo-agency
```

## Importante: Punto B operativo no es el primer paso

En una instalación nueva, la validación operativa normalmente **fallará**. Eso es correcto.

El modo operativo (`--mode operational`, `make point-b` o `make point-b-operational`) solo debe ejecutarse después de completar un primer loop interno revisado por una persona, con una acción real segura y evidencia real: Context Packet, Receipt, scorecard y límites de aprobación actualizados.

No uses una validación operativa fresca para afirmar que la empresa ya está lista como Punto B.

## Qué rellenar primero

Rellena solo lo mínimo y seguro:

1. **Dirección / Mother Brain**: propósito, oferta, tipo de empresa, prioridades.
2. **Contexto seguro**: información general, sin secretos ni datos sensibles.
3. **Límites de aprobación**: qué puede preparar la IA y qué necesita decisión humana.
4. **Primer departamento**: normalmente Operaciones / Delivery o el cuello de botella recomendado. Usa la guía [`templates/how-to/choose-first-department.md`](templates/how-to/choose-first-department.md) para decidir.
5. **Primer Context Packet**: contexto suficiente para una acción interna pequeña.
6. **Primera acción interna**: redactar, analizar, ordenar o preparar; no enviar ni publicar.
7. **Receipt**: prueba de qué se hizo, quién revisó y qué cambió.
8. **Scorecard**: puntuación honesta de preparación y huecos.
9. **Siguiente sprint**: el próximo paso pequeño y revisable.

Para los pasos 5-9, sigue la guía detallada: [`templates/how-to/run-first-internal-loop.md`](templates/how-to/run-first-internal-loop.md).

## Qué no debes pegar ni compartir

No pegues en este repo público, en ejemplos públicos ni en solicitudes de ayuda:

- secretos;
- credenciales;
- claves API;
- contraseñas;
- datos de clientes;
- contratos privados;
- datos regulados o personales sensibles;
- detalles de producción, despliegues, infraestructura o sistemas críticos.

Usa datos sintéticos o contexto anonimizado.

## Dónde pedir ayuda

Si te bloqueas, pide ayuda a **DIA UNO** en [diauno.io](https://diauno.io).

Antes de compartir nada, prepara un reporte seguro usando:

- [`templates/dia-uno/blocker-report.md`](templates/dia-uno/blocker-report.md)

Incluye solo contexto seguro o anonimizado: tipo de empresa, paso donde te bloqueaste, comando ejecutado, resultado, qué intentaste y qué evidencia existe. No incluyas secretos, datos de clientes ni contratos privados.

## Lecturas recomendadas

- [`README.md`](README.md) — visión general y comandos principales.
- [`docs/40_self_serve_happy_path.md`](docs/40_self_serve_happy_path.md) — camino self-serve paso a paso.
- [`docs/43_self_serve_operator_ux.md`](docs/43_self_serve_operator_ux.md) — checklist operativa para usuarios self-serve.
- [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) — errores habituales y arreglos copy/paste.
- [`docs/12_get_help_from_dia_uno.md`](docs/12_get_help_from_dia_uno.md) — cómo pedir ayuda de forma segura.
- [`templates/generated-company-instance/README.md`](templates/generated-company-instance/README.md) — plantilla de instancia privada generada.

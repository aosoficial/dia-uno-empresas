# DECISIONS — Company Brain System

Registro de decisiones vigentes del proyecto.

## 2026-05-08 — Crear Company Brain System como repo modular

**Decisión:** crear el repositorio `company-brain-os` como base local del sistema.

**Por qué:** Jordi quiere un sistema mantenible, versionable, visualizable, exportable y usable por agentes, no un documento suelto.

**Fuente/provenance:** conversación con Jordi + `PLAN.md` + Company Brain Playbook.

**Owner:** Jordi.

**Freshness:** vigente.

**Allowed actions actuales:** crear estructura y archivos base dentro del directorio del proyecto.

**Forbidden actions actuales:** tocar AOS/Urus, Telegram/gateway, GBrain, iCloud, rutas legacy o credenciales.

**Expected outcome:** tener base mínima para arrancar Fase 2 con aprobación.

**Evidence:** `README.md`, `CHANGELOG.md`, `source-map.md` y estructura de carpetas creada.

---

## 2026-05-08 — Private pilot → public framework

**Decisión:** construir primero Company Brain System como laboratorio privado aplicado por Jordi/Hermes, pero diseñado desde el inicio para convertirse en framework público replicable.

**Por qué:** el método necesita probarse en un caso real antes de publicarse, pero no debe contaminarse con datos privados, rutas locales, credenciales o detalles de instalación reales.

**Fuente/provenance:** decisión explícita de Jordi en Telegram, 2026-05-08.

**Owner:** Jordi.

**Freshness:** vigente.

**Allowed actions actuales:** formalizar estructura reusable y marcar lo privado como piloto.

**Forbidden actions actuales:** publicar contenido, subir a GitHub, exponer datos privados, incluir credenciales, o convertir material del piloto en framework público sin revisión.

**Expected outcome:** crear un método público en construcción que se valida primero con el piloto privado.

**Evidence:** `README.md` actualizado, `pilot/private/README.md`, `.gitignore`, `source-map.md` actualizado.

---

## 2026-05-08 — Markdown/YAML en Git como fuente de verdad

**Decisión:** la fuente de verdad será Markdown/YAML versionable.

**Por qué:** permite edición por humanos/agentes, diffs, validación, exportación y mantenimiento largo plazo.

**Fuente/provenance:** `PLAN.md` y patrón `operational-memory-design`.

**Owner:** Jordi.

**Freshness:** vigente.

**Allowed actions:** crear manuales, schemas, registros y plantillas en texto plano.

**Forbidden actions:** usar DOCX, Obsidian o GBrain como única fuente canónica.

**Expected outcome:** repositorio mantenible y exportable.

**Evidence:** arquitectura descrita en `README.md`.

---

## 2026-05-08 — Obsidian como capa visual, no fuente única

**Decisión:** Obsidian será interfaz visual humana sobre los mismos Markdown.

**Por qué:** ayuda a navegar relaciones y mapas, pero no debe bloquear automatización ni versionado.

**Fuente/provenance:** `PLAN.md`.

**Owner:** Jordi.

**Freshness:** vigente.

**Evidence:** estructura compatible con Markdown/Obsidian.

---

## 2026-05-08 — GBrain como memoria operativa

**Decisión:** GBrain se reserva para StateChanges, Context Packets, Receipts, freshness, permisos y relaciones operativas.

**Por qué:** el Company Brain no es solo documentación; debe producir contexto accionable.

**Fuente/provenance:** Company Brain Playbook.

**Owner:** Jordi.

**Freshness:** vigente.

**Guardrail:** no tocar GBrain en Fase 1 sin aprobación.

**Evidence:** decisión registrada; sin cambios en GBrain.

---

## 2026-05-08 — DOCX/PDF/Web como exportaciones

**Decisión:** DOCX/PDF/Web serán salidas generadas, no fuente de verdad.

**Por qué:** son útiles para leer, compartir o comentar, pero frágiles como base operativa.

**Fuente/provenance:** `PLAN.md`.

**Owner:** Jordi.

**Freshness:** vigente.

**Evidence:** `build/outputs/` creado para salidas futuras.

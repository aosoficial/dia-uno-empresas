# 06 — Product Review v0.1

> **Need help applying this?** This page is part of Company Brain System, an open method by Libera. If you get stuck, start with the [Quick Start](07_quick_start.md), use the [Company Brain intake](../templates/questionnaires/company-brain-intake.md), or see [how Libera can help](12_get_help_from_libera.md).

## Revisión de Company Brain System como documentación pública

---

**Fecha:** 2026-05-08
**Revisor:** Revisión independiente de producto
**Alcance:** README.md + docs/00–05 + templates/ + schemas/ + registry/ + scripts/ + examples/
**Criterio:** ¿Puede alguien externo entender, evaluar y aplicar Company Brain System leyendo solo este repositorio?

---

## 1. Veredicto ejecutivo

Company Brain System tiene un núcleo documental sólido y una profundidad inusual para un framework en fase pre-release. Los documentos core (00–05) enseñan el método de forma progresiva, los templates son genuinamente operativos (no decorativos), los schemas mapean correctamente a las plantillas y los scripts de validación/build funcionan.

**El método está bien pensado. La documentación está bien escrita. Pero el empaquetado como producto público tiene huecos que bloquean la adopción por alguien externo.**

Los problemas principales no son de contenido sino de **acceso**: falta un punto de entrada rápido, falta un glosario centralizado, falta un ejemplo completo de extremo a extremo, y hay inconsistencias menores (idioma, empresas de referencia) que generan fricción innecesaria.

**Calificación general: 7/10 — fuerte en sustancia, débil en onboarding del lector.**

---

## 2. Qué está fuerte

### Documentación core (docs/00–05)

- **Progresión lógica.** Playbook → fundamentos → memoria → cerebros → agentes → operador. Cada doc tiene propósito, audiencia, entradas y salidas. La estructura es consistente y enseñable.
- **Los 7 principios son diferenciadores reales.** No son genéricos ("sé ágil"). Son posiciones concretas: "la memoria es estado, no servicio", "completar no es tener éxito". Esto le da identidad al método.
- **Antipatrones en cada documento.** Esto es raro y valioso. No solo dice qué hacer, dice qué errores evitar y por qué. Aporta más que muchas secciones de "mejores prácticas".
- **Checklists accionables.** Cada doc termina con un checklist que puede usarse como gate de validación.
- **Ejemplos narrativos con empresas ficticias.** NovaTech y Meridian Foods dan vida a los conceptos. Los ejemplos YAML son concretos (nombres, fechas, valores reales, no `foo/bar`).

### Templates

- **Operativos, no decorativos.** Cada plantilla tiene: qué es, cuándo usarla, campos obligatorios, ejemplo completo, errores comunes. Esto supera el estándar habitual de "plantilla vacía con TODOs".
- **Agent Runtime Pack completo.** 18 archivos que cubren todo el ciclo de vida del agente. La estructura SOUL.md como contrato operativo es una de las ideas más fuertes del framework.
- **Department Brain Pack coherente.** 6 archivos con la misma calidad. ENTITIES.md con propiedades, cardinalidad y freshness por entidad es especialmente bueno.
- **Cuestionarios de onboarding reales.** No son formularios triviales. Cubren necesidad, identidad, permisos, herramientas, memoria, pushback, heartbeat y período de prueba.

### Schemas

- **8 schemas YAML validables.** Estructura consistente: bloque `schema` (nombre, versión, descripción), lista `fields` (nombre, tipo, required, description, example) e instancia `example` completa.
- **Correspondencia schemas↔templates correcta.** `receipt.schema.yaml` mapea a `RECEIPT.md`, `agent.schema.yaml` a `IDENTITY.md`/`SOUL.md`, etc.

### Scripts

- **4 scripts funcionales y documentados.** `validate_repo.py`, `validate_schemas.py`, `build_docs.py`, `export_docx.py`. Python limpio con `__main__` guards y códigos de salida. `export_docx.py` tiene fallback XML — no trivial.

### Registry

- **Estructura correcta.** 6 archivos YAML (agents, brains, departments, metrics, permissions, sources) con templates comentados y entradas de ejemplo. `metrics.yaml` tiene 10 métricas con umbrales bueno/aceptable/malo.

---

## 3. Qué está confuso para alguien externo

### 3.1 — No hay "elevator pitch"

El README abre con "Método operativo para organizaciones que trabajan con agentes de IA" y luego lista componentes. Un lector externo necesita en los primeros 10 segundos:

- **¿Para quién es esto?** (founders, CTOs, responsables de operaciones con IA)
- **¿Qué problema resuelve en una frase?** (los agentes de IA operan sin memoria compartida, sin contrato y sin evidencia)
- **¿Qué NO es?** (no es un framework de código, no es un SaaS, no es un chatbot)

Actualmente hay que leer hasta el Playbook (doc 00) para entender el "por qué". Para un producto público, eso es demasiado tarde.

### 3.2 — No hay glosario centralizado

Los términos clave (StateChange, Context Packet, Receipt, freshness, Brain, ontología, SOUL.md, Agent Runtime Pack, Heartbeat, drift) se definen en los docs donde aparecen por primera vez, pero no hay una referencia rápida. Un lector que llega a doc 03 y no recuerda qué era "freshness" tiene que buscar en doc 01 o doc 02.

### 3.3 — Relación docs↔templates poco clara

¿Cuándo leo un doc y cuándo uso un template? No hay un flujo explícito tipo:

```
1. Lee docs/01 para entender qué es un StateChange
2. Usa templates/statechanges/statechange-template.md para crear tu primer StateChange
3. Valida con schemas/statechange.schema.yaml
```

Los docs explican conceptos y los templates dan estructura, pero el puente entre ambos está implícito.

### 3.4 — Dos empresas de referencia sin conexión

- docs/00 y docs/01 usan **NovaTech** (software de inventario, 15 personas).
- docs/01 también introduce **Meridian Foods** (alimentación, 50 personas).
- Los templates usan **Meridian Foods** y agente **Vega/Oliva**.

No se explica por qué hay dos empresas ni cuál es el ejemplo canónico. Para un lector externo, genera la duda: "¿son ejemplos del mismo método o de variantes diferentes?"

### 3.5 — Mezcla de idiomas en SOUL.md

Las secciones de SOUL.md usan encabezados en inglés (Identity, Mission Map, Pushback Rules, Autonomy Boundary, Tools Boundary) dentro de documentación completamente en español. Esto es una decisión legítima (los encabezados pueden ser "nombres propios" del framework), pero no está explicada. Un lector externo puede interpretarlo como descuido.

### 3.6 — Falta "Quick Start" real

El README tiene "Cómo empezar" con 6 pasos, pero el paso 3 es "Decide tu ontología" — un concepto que requiere leer doc 01 para entender. No hay un camino de <1 hora para que alguien pruebe el método con un caso mínimo.

### 3.7 — Templates duplicados sin explicación

Existen templates de Receipt, StateChange y Context Packet tanto dentro de `templates/agent-runtime-pack/` como en carpetas independientes (`templates/receipts/`, `templates/statechanges/`, `templates/context-packets/`). No se explica cuál usar cuándo ni en qué se diferencian.

---

## 4. Huecos antes de v0.1.0

### Bloqueantes

| # | Hueco | Impacto | Esfuerzo |
|---|-------|---------|----------|
| H1 | **`examples/` no existe.** El registry referencia `examples/vega/` como `runtime_pack` pero el directorio no existe. Referencia rota. | Un usuario que sigue el registry encuentra un enlace muerto. | Medio — crear un Agent Runtime Pack completo relleno para Vega. |
| H2 | **No hay Quick Start.** Sin guía de <1 hora, los primeros usuarios abandonan antes de doc 02. | Barrera de entrada alta para evaluadores. | Medio — doc corto o sección en README con caso mínimo. |
| H3 | **No hay glosario.** Términos clave dispersos en 5 documentos. | Fricción de lectura, re-lectura innecesaria. | Bajo — extraer definiciones existentes a un doc de referencia. |

### Importantes (no bloqueantes pero debilitan la v0.1)

| # | Hueco | Impacto |
|---|-------|---------|
| H4 | **Falta `handoff.schema.yaml`.** Handoff es primitiva de primera clase con template completo, pero no tiene schema. | Inconsistencia schemas↔templates. |
| H5 | **Scorecards de Company Brain y Department Brain: verificar cuerpo de métricas.** Las primeras secciones están completas pero las rúbricas métricas podrían tener campos `[COMPLETAR]`. | Plantillas que parecen listas pero no lo están. |
| H6 | **README tiene `<url-del-repo>` como placeholder en git clone.** | Mala primera impresión. |
| H7 | **No hay versión visible.** Ni en README, ni en docs, ni como tag de git. Solo los schemas tienen campo `version: "0.1.0"`. | No se sabe qué versión se está leyendo. |
| H8 | **CHANGELOG no marca v0.1.0.** Existe pero registra cambios internos, no un release. | Sin hito de referencia. |
| H9 | **`export_docx.py` se documenta en doc 05 con uso de archivo individual (`python scripts/export_docx.py docs/01_aos_system.md`) pero el script procesa el combinado.** | Instrucción incorrecta. |

### Menores

| # | Hueco |
|---|-------|
| H10 | El campo `type` en `agent.schema.yaml` tiene enum fijo de 5 tipos (ventas, soporte, operaciones, análisis, coordinación) — limita extensibilidad. |
| H11 | La etiqueta `sync: company_brain` mencionada en doc 03 no aparece en ningún schema. |
| H12 | CONTRIBUTING.md es mínimo — suficiente para ahora, pero no guía a un contributor externo real. |

---

## 5. Mejoras concretas por archivo

### README.md

| Mejora | Detalle |
|--------|---------|
| Añadir pitch de 2 líneas al inicio | Antes de "Qué es": ¿para quién? ¿qué problema? ¿qué NO es? |
| Reemplazar `<url-del-repo>` | URL real o instrucción genérica tipo `git clone https://github.com/<org>/company-brain-system.git` |
| Añadir badge de versión | `v0.1.0` visible al inicio |
| Añadir sección "Quick Start" | Caso mínimo: crear 1 Company Brain con 3 entidades + 1 agente con Runtime Pack mínimo. Enlazar a example/ |
| Enlazar LICENSE | "Licencia: [MIT](LICENSE)" en vez de solo "MIT" |
| Simplificar "Cómo empezar" | Los 6 pasos actuales son correctos pero abstractos. Reescribir como "ruta de lectura" + "ruta práctica" |

### docs/00_master_playbook.md

| Mejora | Detalle |
|--------|---------|
| Vincular ejemplo a `examples/` | Si se crea el ejemplo completo, enlazarlo aquí como "ver ejemplo real" |
| Hacer checklist enlaces clicables | Cada ítem del checklist podría enlazar al doc relevante |

### docs/01_aos_system.md

| Mejora | Detalle |
|--------|---------|
| Explicar la decisión de encabezados en inglés para SOUL.md | Una nota tipo: "Los nombres de sección de SOUL.md se mantienen en inglés como convención del framework para facilitar interoperabilidad" |
| Añadir enlace a glosario | Al final de "Conceptos fundamentales" |
| Consolidar empresa de referencia | Decidir: ¿NovaTech es el ejemplo de los docs y Meridian Foods el de los templates? Hacerlo explícito |

### docs/02_operational_memory.md

| Mejora | Detalle |
|--------|---------|
| Ninguna mejora estructural necesaria | Es el documento más completo y mejor resuelto de la serie. |
| Único detalle menor | La sección de permisos repite contenido que se desarrolla mejor en doc 04. Considerar referencia cruzada en vez de repetición. |

### docs/03_brain_architecture.md

| Mejora | Detalle |
|--------|---------|
| Desarrollar Project/Domain Brain | La sección es corta comparada con Company y Department. Al menos definir: estructura mínima, cuándo archivar, cómo difiere de un Department Brain |
| Definir `sync: company_brain` en schema | O eliminarlo del texto y describir el mecanismo de sincronización sin esa etiqueta |

### docs/04_agent_onboarding.md

| Mejora | Detalle |
|--------|---------|
| Añadir proceso de desactivación | ¿Qué pasa si el agente falla la prueba? ¿Cómo se desactiva? ¿Se archiva su Runtime Pack? |
| Consistencia de empresa de referencia | Usa NovaTech en el proceso pero los templates usan Meridian Foods. Alinear o explicar |

### docs/05_operator_manual.md

| Mejora | Detalle |
|--------|---------|
| Corregir uso de `export_docx.py` | El ejemplo muestra uso con archivo individual; verificar si el script lo soporta o corregir la documentación |
| Añadir requisitos de tooling | ¿Qué necesita el operador? ¿Git + editor de texto + Python? ¿Obsidian es realmente opcional? Hacerlo explícito |
| Añadir sección "Infraestructura mínima" | ¿Dónde viven los archivos YAML en la práctica? ¿En un repo Git por organización? ¿Un subdirectorio? |

### Templates

| Mejora | Detalle |
|--------|---------|
| Explicar la diferencia entre templates de pack vs. standalone | `templates/agent-runtime-pack/RECEIPT.md` vs. `templates/receipts/receipt-template.md` — ¿cuándo usar cuál? Añadir nota en cada uno o consolidar |
| Verificar scorecards de Company Brain y Department Brain | Confirmar que las rúbricas métricas están completas, no en estado `[COMPLETAR]` |

### Schemas

| Mejora | Detalle |
|--------|---------|
| Crear `handoff.schema.yaml` | Handoff tiene template completo pero no schema. Inconsistencia. |
| Revisar enum de `type` en `agent.schema.yaml` | 5 tipos fijos es limitante. Considerar hacerlo extensible o documentar cómo añadir tipos |

### Registry

| Mejora | Detalle |
|--------|---------|
| Corregir referencia a `examples/vega/` | Crear el directorio o corregir el path |
| Añadir instrucciones de uso | ¿Cómo paso de "cuestionario completado" a "entrada en el registry"? Un párrafo en cada archivo bastaría |

---

## 6. Checklist de release v0.1.0

### Bloqueantes — sin estos no se publica

- [ ] **Crear `examples/`** con al menos un Agent Runtime Pack completo relleno (Vega o equivalente) y un Company Brain mínimo.
- [ ] **Crear Quick Start** — sección en README o doc independiente. Caso mínimo ejecutable en <1 hora.
- [ ] **Crear glosario** — doc de referencia con los ~15 términos clave del framework, definición de 1-2 líneas y enlace al doc donde se desarrolla.
- [ ] **Corregir `<url-del-repo>`** en README.
- [ ] **Corregir documentación de `export_docx.py`** en doc 05 (uso real vs. documentado).
- [ ] **Verificar scorecards** de Company Brain y Department Brain — confirmar que no hay campos `[COMPLETAR]`.

### Importantes — deberían estar para v0.1.0

- [ ] Crear `handoff.schema.yaml`.
- [ ] Añadir versión visible en README (badge o texto).
- [ ] Marcar v0.1.0 en CHANGELOG con fecha y resumen.
- [ ] Crear tag de git `v0.1.0`.
- [ ] Añadir nota sobre encabezados en inglés de SOUL.md (decisión de diseño, no descuido).
- [ ] Explicar relación templates de pack vs. templates standalone.
- [ ] Añadir enlace a LICENSE en README.

### Deseables — pueden esperar a v0.2.0

- [ ] Desarrollar sección de Project/Domain Brain en doc 03.
- [ ] Añadir proceso de desactivación de agentes en doc 04.
- [ ] Unificar empresa de referencia (o documentar por qué hay dos).
- [ ] Hacer extensible el enum `type` en `agent.schema.yaml`.
- [ ] Definir `sync: company_brain` en schema o eliminar del texto.
- [ ] Ampliar CONTRIBUTING.md para contributors externos.
- [ ] Añadir sección "Infraestructura mínima" en doc 05.

---

*Revisión completada el 2026-05-08. Próxima revisión recomendada: tras resolver los bloqueantes, antes de publicar v0.1.0.*

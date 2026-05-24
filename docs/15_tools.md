# Herramientas usadas en DIA UNO Empresas

> **¿Necesitas ayuda aplicando esto?** **¿Necesitas ayuda aplicando esto?** Esta página forma parte de DIA UNO Empresas, una aceleradora abierta hacia empresas AI-First. Si te bloqueas, empieza por el [Inicio rápido](07_quick_start.md), usa el [intake de servicio](../templates/questionnaires/service-business-ai-first-intake.md) o pide ayuda en [DIA UNO](12_get_help_from_dia_uno.md).

DIA UNO Empresas no exige una única tecnología. Explica las categorías de herramientas que necesita una empresa para que los agentes trabajen con contexto, evidencia y control.

## Categorías de herramientas

### 1. Fuente de verdad

Objetivo: mantener el método y la memoria operativa en archivos duraderos.

Ejemplos:

- repositorio Git;
- archivos Markdown;
- registros YAML;
- plantillas versionadas.

Úsalo para:

- documentación;
- plantillas;
- schemas;
- decisiones;
- mejoras del método.

Regla: si define cómo opera la empresa, debería estar versionado.

### 2. Company Brain

Objetivo: guardar el contexto operativo de la empresa.

Debería contener:

- propósito;
- departamentos;
- personas/roles;
- decisiones;
- métricas;
- riesgos;
- fuentes;
- agentes;
- permisos.

Regla: el Company Brain debe ayudar a los agentes a actuar con contexto, no convertirse en un vertedero de información.

### 3. Department Brains

Objetivo: mantener memoria enfocada para un área de la empresa.

Ejemplos:

- cerebro de ventas;
- cerebro de operaciones;
- cerebro de producto;
- cerebro de finanzas;
- cerebro de soporte.

Regla: cada Department Brain debería tener fuentes, métricas y señales claras.

### 4. Entorno de ejecución de agentes

Objetivo: operar agentes con identidad, permisos y reglas de evidencia.

El entorno puede ser cualquier herramienta de agentes que pueda:

- leer Markdown;
- seguir instrucciones;
- usar herramientas aprobadas;
- escribir salidas estructuradas;
- pedir aprobación cuando haga falta.

Ejemplos:

- agentes de programación;
- agentes de chat;
- agentes de flujos de trabajo;
- asistentes internos.

Regla: ningún agente debería operar sin un Agent Runtime Pack.

### 5. Tablero de trabajo / control

Objetivo: ver qué se está haciendo, quién lo lleva y qué está bloqueado.

Puede ser:

- un tablero de proyecto;
- un gestor de issues;
- una base de datos de tareas;
- un panel visual de control.

Debería seguir:

- responsable;
- resultado esperado;
- estado;
- bloqueos;
- aprobación necesaria;
- ruta de evidencia.

Regla: el tablero sigue el trabajo; no sustituye al Company Brain.

### 6. Receipts y almacén de evidencia

Objetivo: probar qué ha pasado.

Un Receipt debería registrar:

- acción;
- fuente/contexto;
- archivos cambiados;
- decisión tomada;
- riesgos;
- verificación;
- camino para deshacer si hace falta.

Regla: “hecho” no basta. El sistema necesita evidencia.

### 7. Canales de comunicación

Objetivo: permitir que las personas aprueben, corrijan y den contexto.

Ejemplos:

- chat;
- email;
- reuniones;
- comentarios en issues;
- notas de voz.

Regla: la comunicación es entrada, no fuente de verdad. Las decisiones importantes deben registrarse de vuelta en el sistema.

### 8. Herramientas de validación

Objetivo: comprobar que archivos, schemas y estructura siguen siendo válidos.

Este repo incluye:

```bash
python scripts/validate_repo.py
python scripts/validate_schemas.py
python scripts/build_docs.py
```

Regla: valida antes de publicar o hacer cambios importantes.

## Stack mínimo

Para un equipo pequeño, empieza con:

- GitHub o GitLab para el repositorio;
- Markdown para documentación y plantillas;
- YAML para registros y schemas;
- un tablero de trabajo;
- un agente de IA;
- una carpeta de evidencia o archivo de Receipts.

No añadas infraestructura compleja hasta que el método funcione manualmente.

## Regla para conectar herramientas reales

Antes de conectar herramientas reales, responde:

1. ¿Qué datos puede leer el agente?
2. ¿Qué datos puede escribir el agente?
3. ¿Qué requiere aprobación humana?
4. ¿Cómo se deshace la acción si sale mal?
5. ¿Qué Receipt prueba la acción?

Si esto no está claro, no conectes la herramienta todavía.

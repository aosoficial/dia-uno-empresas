# Skills necesarias en Company Brain System

> **¿Necesitas ayuda aplicando esto?** **¿Necesitas ayuda aplicando esto?** Esta página forma parte de Company Brain System, una aceleradora abierta hacia empresas AI-First. Si te bloqueas, empieza por el [Inicio rápido](07_quick_start.md), usa el [intake de servicio](../templates/questionnaires/service-business-ai-first-intake.md) o pide ayuda en [DIA UNO](12_get_help_from_dia_uno.md).

Una skill es una capacidad operativa reutilizable que un agente puede aplicar. No es una personalidad ni un prompt mágico. Es una forma documentada de hacer un tipo de trabajo de manera segura y repetible.

## Cómo escribir una skill

Cada skill debería incluir:

- objetivo;
- cuándo usarla;
- cuándo no usarla;
- contexto necesario;
- pasos;
- límites de seguridad;
- formato de salida;
- verificación;
- errores comunes.

## Skills principales

### 1. Instalación del Company Brain

Objetivo: ayudar a una empresa a crear su primer Company Brain.

El agente debe saber:

- pedir el contexto mínimo;
- evitar datos sensibles al principio;
- crear un ejemplo sintético;
- mapear departamentos;
- definir fuentes;
- crear primeras métricas;
- marcar preguntas abiertas.

Salida:

- borrador de Company Brain;
- lista de contexto faltante;
- primeros riesgos;
- siguientes acciones.

### 2. Instalación de Department Brain

Objetivo: crear memoria enfocada para un área.

El agente debe saber definir:

- propósito del departamento;
- trabajo del que es responsable;
- fuentes;
- señales;
- métricas;
- decisiones recurrentes;
- traspasos;
- riesgos.

Salida:

- pack de Department Brain;
- scorecard;
- política de sincronización.

### 3. Onboarding de agentes

Objetivo: crear un agente que pueda operar con seguridad.

El agente debe definir:

- identidad;
- rol;
- acciones permitidas;
- acciones prohibidas;
- herramientas;
- reglas de aprobación;
- reglas de memoria;
- reglas de Receipts.

Salida:

- Agent Runtime Pack;
- primera tarea segura;
- lista de revisión.

### 4. Preparación de contexto

Objetivo: dar al agente suficiente contexto para actuar sin saturarlo.

El agente debe saber crear:

- Context Packets;
- traspasos;
- resúmenes de fuentes;
- resúmenes de decisiones;
- resúmenes de riesgos.

Salida:

- Context Packet conciso;
- lista de fuentes;
- preguntas de contexto faltante.

### 5. Escritura de Receipts

Objetivo: dejar evidencia después de actuar.

El agente debe registrar:

- qué ocurrió;
- por qué;
- fuentes usadas;
- archivos o sistemas cambiados;
- aprobación usada;
- riesgos;
- verificación;
- camino para deshacer si hace falta.

Salida:

- Receipt.

### 6. Gestión de aprobación humana

Objetivo: saber cuándo el agente debe parar y preguntar.

El agente debería preguntar antes de:

- contactar personas;
- publicar;
- gastar dinero;
- cambiar producción;
- usar datos sensibles;
- asumir compromisos legales o económicos;
- cambiar permisos.

Salida:

- petición corta de decisión;
- opciones;
- recomendación;
- aprobación necesaria.

### 7. Skill de dirección / CEO

Objetivo: ayudar a la empresa a elegir foco, prioridades y renuncias.

El agente debe saber:

- identificar el bloqueo real;
- limitar prioridades;
- separar urgente de importante;
- enrutar trabajo al responsable correcto;
- proteger calidad, margen, privacidad y energía humana.

Salida:

- foco;
- máximo tres prioridades;
- qué no hacer;
- riesgos;
- asignaciones;
- aprobaciones necesarias.

### 8. Skill de operaciones

Objetivo: convertir dirección en tablero y ritmo de cierre.

El agente debe definir:

- responsable;
- resultado esperado;
- qué tiene que estar listo;
- ruta de evidencia;
- bloqueo;
- próxima revisión.

Salida:

- estructura de tablero/control;
- notas de traspaso;
- lista de cierre.

### 9. Skill de método

Objetivo: convertir trabajo repetido en playbooks y plantillas reutilizables.

El agente debe saber:

- detectar patrones repetibles;
- separar material privado de material público;
- crear plantillas;
- actualizar documentación del método;
- proponer mejoras.

Salida:

- playbook;
- checklist;
- propuesta de mejora del método.

### 10. Skill de growth

Objetivo: explicar el valor del sistema sin prometer de más.

El agente debe saber:

- identificar comprador;
- identificar problema doloroso;
- explicar resultado;
- redactar landing o README;
- crear llamadas a la acción;
- evitar afirmaciones sin prueba.

Salida:

- borrador de posicionamiento;
- borrador de mensaje;
- huecos de prueba;
- aprobación necesaria antes de publicar.

### 11. Skill de producto

Objetivo: convertir el método en activos usables.

El agente debe saber crear:

- plantillas;
- ejemplos;
- scripts de validación;
- flujos simples de implementación;
- mejoras de estructura del repo.

Salida:

- activo productizado;
- resultado de validación;
- camino para deshacer si hace falta.

### 12. Skill de evaluación de seguridad

Objetivo: comprobar si un agente es seguro para usar con más autonomía.

El agente debe probar:

- permisos;
- acceso a memoria;
- acceso a herramientas;
- gestión de aprobaciones;
- Receipts;
- comportamiento ante fallos.

Salida:

- scorecard de seguridad;
- riesgos;
- arreglos necesarios antes de dar más autonomía.

## Regla de calidad de una skill

Una buena skill hace mejor al siguiente agente sin necesitar contexto privado.

Una mala skill:

- depende de la memoria de una persona;
- contiene nombres privados o créditos internos;
- tiene instrucciones vagas;
- no tiene verificación;
- permite actuar sin aprobación.

# El Método DÍA UNO · v6, compilado

Este árbol es el **Método v6 completo en formato portal/wiki**: los 7 pilares con sus
herramientas, cada una con su teoría troceada en lecciones y su plantilla. Es público a
propósito — el método se enseña; lo que DÍA UNO no publica es su capa de entrega (guías de
consultor, andamiaje interno, el libro), que vive fuera de este repositorio.

## Cómo se instala: las capas (la V6)

Antes de explicar qué herramientas tiene DÍA UNO hay que explicar cómo se instalan, **porque no
se instalan todas a la vez**. Un sistema operativo completo, presentado entero, asusta: parece
EOS más Scaling Up más todo lo demás, de golpe. Ese es el modo de fallo número uno de los
sistemas de gestión — el empresario se abruma y abandona al tercer mes. Pero un sistema recortado
tampoco sirve, porque no escala.

La V6 resuelve esa tensión con una regla: **el sistema es fijo, el camino es flexible**. Todas
las empresas acaban con las mismas 15 herramientas; lo que cambia es por dónde empiezan y hasta
qué profundidad. Eso son las capas.

| Capa | Qué es | Qué entra |
|---|---|---|
| **1 · El sistema mínimo** | El monopatín que ya rueda: dirección, tracción, ritmo, caja y un primer pulso de personas. Tan simple de mantener como EOS. | 1.1 · 02 · 05 (sencilla) · 09 · 10 · 11 · 14 · 12 (ligero) · 08 (simple) · 06/07 (un proceso) |
| **2 · Densidad** | La profundidad, cuando la Capa 1 rueda sola: se completa el Rumbo, se densifica Personas, se documentan los demás procesos. Aquí vive la Matriz. | 1.2 · 1.3 · 1.4 · 03 · 04 · 05 (profunda) · 07 (resto) · 13 · 13B (captura) |
| **3 · Agentización** | La IA encima de lo que ya funciona. Nunca sustituye lo que aún no existe. | Agentes sobre 08 · 12 · 07 · 10-11 · 14, y 13B en modo RAG |

Tres reglas hacen que esto no sea una chapuza:

- **Profundidad antes que amplitud.** Nadie sube a la Capa 2 de un dominio hasta que su Capa 1
  rueda sola. Mejor ocho herramientas que funcionan que quince a medias.
- **La conexión es temporal.** Muchas herramientas tienen una versión mínima que engorda después
  — por eso el frontmatter admite `capa: "1-2"`. Y a veces basta adelantar un *trozo mínimo* de
  una herramienta avanzada para desbloquear el sistema básico: unos valores en una línea bastan
  para una evaluación sencilla; un suelo de caja de un solo número basta para un panel simple.
- **El corte es fijo, el orden lo decide el cuello.** Qué va en cada capa está decidido; en qué
  orden se instala dentro de una capa lo dice el diagnóstico de cada empresa.

Cada herramienta cierra con una lección **«Implementación por capas»** que dice su mínimo, su
engorde, su punto de corte y qué conexiones se encienden cuándo.

## Estructura

```
metodo/
  01-rumbo/
    01-proposito-y-meta/
      modulo.md        ← frontmatter del módulo (slug, título, pilar, orden, capa, fileIds de Drive)
      leccion-01.md    ← lecciones de 2-4 min; la última sección siempre es «## Comprobación»
      …
      plantilla.md     ← la plantilla rellenable, con sus tablas y su mínimo innegociable
  02-personas/ … 07-cadencia/
```

## De dónde sale y a dónde va

- **Fuente**: la carpeta `DIA UNO OS › Metodo › DÍA UNO · Método v5` de Google Drive
  (el equipo escribe en Word; los `drive_*_id` del frontmatter atan cada módulo a su origen).
  Desde la V6 la carpeta viva es `DÍA UNO · Método v6`.
- **Consumidores**: el portal de clientes (`clientes.diauno.io`, carga vía
  `diauno-admin/scripts/metodo-carga.mjs`) y la wiki web del método.
- **Formato del cuerpo**: texto plano con cuatro marcas (`## `, `- `, `**negrita**`, tablas `|`),
  el microformato que renderiza el portal. No es Markdown completo a propósito.
- **Convención de slugs**: todo slug empieza por la clave de su pilar (`rumbo-`, `personas-`,
  `procesos-`, `caja-`, `ejecucion-`, `sistema-nervioso-`, `cadencia-`); la agrupación visual
  del portal depende de ese prefijo.

## Reglas de edición

1. La fuente de la doctrina es Drive: los cambios de fondo se hacen allí y se recompilan.
   Una errata puede corregirse aquí directamente.
2. Cada lección termina en una `## Comprobación` con ≥2 opciones `- [ ]` y exactamente una
   `- [x]`. El validador (`metodo-carga.mjs --dry`) lo comprueba antes de cargar nada.
3. Aquí no entra material de entrega (guías internas, dossiers, libro). Nunca.
4. El campo `capa` del frontmatter es canónico y sale del índice de la V6
   (`00_INDICE_HERRAMIENTAS_POR_CAPA`). Valores: `"1"`, `"1-2"`, `"2"`, `"2-3"`, `"3"`. El guion
   no es un rango cualquiera: significa que la herramienta se instala en su versión mínima en la
   primera capa y se profundiza en la segunda. El portal lo usa para no exigir en el arranque lo
   que todavía no toca.

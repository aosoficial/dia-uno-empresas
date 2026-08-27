# El Método DÍA UNO · v5, compilado

Este árbol es el **Método v5 completo en formato portal/wiki**: los 7 pilares con sus
herramientas, cada una con su teoría troceada en lecciones y su plantilla. Es público a
propósito — el método se enseña; lo que DÍA UNO no publica es su capa de entrega (guías de
consultor, andamiaje interno, el libro), que vive fuera de este repositorio.

## Estructura

```
metodo/
  01-rumbo/
    01-proposito-y-meta/
      modulo.md        ← frontmatter del módulo (slug, título, pilar, orden, fileIds de Drive)
      leccion-01.md    ← lecciones de 2-4 min; la última sección siempre es «## Comprobación»
      …
      plantilla.md     ← la plantilla rellenable, con sus tablas y su mínimo innegociable
  02-personas/ … 07-cadencia/
```

## De dónde sale y a dónde va

- **Fuente**: la carpeta `DIA UNO OS › Metodo › DÍA UNO · Método v5` de Google Drive
  (el equipo escribe en Word; los `drive_*_id` del frontmatter atan cada módulo a su origen).
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

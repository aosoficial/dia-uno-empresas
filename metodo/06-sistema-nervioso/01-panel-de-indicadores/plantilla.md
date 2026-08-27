---
slug: sistema-nervioso-panel-de-indicadores-plantilla
titulo: El panel de indicadores — plantilla
resumen: La vista semanal del panel (ventana móvil de 12 semanas con media, tendencia y flecha) y la ficha de diccionario que da a cada número una definición única.
formato: xlsx
orden: 115
---
La plantilla del panel tiene dos hojas: la vista semanal —una fila por indicador, agrupada por departamento, con su ventana de 12 semanas, su media, su tendencia y su flecha— y el diccionario, con la ficha que fija la definición única de cada número.

## Cómo se usa

Una fila por indicador, agrupada por departamento (cada bloque se pliega y despliega). Tipo: P = predictivo (lo empujas esta semana) · R = resultado (ya ocurrió). Rellena las 12 columnas semanales; la media y la tendencia (la curva) se calculan solas en la hoja, y la flecha compara la última semana con la media. Cada semana entra una nueva y sale la más antigua: ventana móvil de 12. El rojo dispara acción o revisa el hito asociado. La definición única de cada número vive en la hoja Diccionario.

## La vista semanal

| Depto | Tipo | KPI | Dueño | Objetivo | Ud | Media | Δ | Tendencia | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
| NORTE (North Star) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | R | Valor creado (media 8 sem) | Fin. | ≥20% | % | 62.2 | ▼ |  | 8 | 10 | 16 | 47 | 63 | 60 | 116 | 132 | 132 | 132 | 15 | 15 |
|  | R | Días en mercado (media) | V. Ventas | ≤30 | días | 64.2 | ▲ |  | 38 | 45 | 52 | 59 | 50 | 57 | 64 | 71 | 78 | 69 | 92 | 95 |
| Marketing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | P | Leads cualificados / semana | Mkt | ≥10 | # | 23.4 | ▼ |  | 29 | 32 | 29 | 44 | 49 | 14 | 19 | 29 | 7 | 15 | 10 | 4 |
|  | P | Coste por lead | Mkt | ≤80 | € | 9.1 | ▲ |  | 9 | 8 | 9 | 5 | 5 | 14 | 13 | 5 | 9 | 11 | 5 | 16 |
|  | P | Tasa de cualificación | Mkt | ≥35% | % | 31.7 | ▼ |  | 25 | 27 | 28 | 37 | 35 | 36 | 47 | 42 | 21 | 53 | 13 | 16 |
| Ventas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | P | Visitas cualificadas / agente / sem | V. Ventas | ≥7 | # | 9.8 | ▼ |  | 7 | 9 | 9 | 11 | 11 | 13 | 12 | 12 | 11 | 8 | 9 | 6 |
|  | R | Arras firmadas / semana | V. Ventas | ≥1 | # | 0.3 | ▲ |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Procesos |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Personas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Caja |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## La ficha del diccionario

Rellena una ficha por indicador del panel. Con 15-20 fichas —las de los números que provocan discusiones— cubres el 90% de las peleas. La ficha se enlaza desde la casilla del panel: quien duda, mira la ficha y la discusión se acaba. Ejemplo relleno:

| Campo | Ejemplo |
| Nombre canónico | Leads cualificados / semana |
| Qué significa (negocio) | Contactos que cumplen los criterios de cualificación, generados en la semana |
| Fórmula exacta | COUNT(leads con estado='cualificado' y fecha en la semana en curso) |
| Fuente del dato | CRM · objeto Lead · campo estado |
| Incluye / Excluye | Incluye: leads inbound y outbound cualificados. Excluye: sin cualificar, duplicados, internos |
| Grano / base temporal | Por fecha de cualificación; semana natural lun-dom |
| Unidad | Nº de leads |
| Frecuencia | Semanal |
| Objetivo y umbrales | Objetivo ≥10/sem · ámbar <10 · rojo <7 |
| Dueño único | (responsable de marketing) |
| Tipo | Predictivo (P) |
| Limitaciones conocidas | Depende de que se marque bien el estado en el CRM |
| Historial de definición | v1 (fecha): definición inicial — anota cada cambio para no fabricar falsas rupturas de tendencia |

El valor de la ficha: cuando alguien discute un número, no se abre debate — se abre esta ficha. La fórmula y el "incluye/excluye" zanjan el 90% de las discrepancias. Un mismo indicador, una sola definición, en todos los paneles.

## El mínimo innegociable

- Pocos números, del tipo correcto: mezcla de resultado (para saber si ganas) y predictivos (para poder actuar). Nada de vanidad.
- Cada número con definición única (hoja Diccionario), un dueño con nombre, un objetivo y sus umbrales de color.
- Ventana móvil de 12 semanas, con media, tendencia y flecha; comprimible por departamento; el rojo dispara acción o revisa el hito.

La forma final se cierra con Jordi. El panel de caja puede enchufarse como sección financiera si la empresa quiere, o quedar reservado. Un agente (madurez 9-10) mantiene los datos al día, calcula el semáforo y avisa de anomalías.

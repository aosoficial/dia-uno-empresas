# Inventario del Método V3

## Contrato de inventario

- Versión de todos los artefactos: `Método V3`.
- Estado: `original preservado`.
- Destino operativo: una copia dentro de la instancia privada, nunca este repositorio público.
- Integridad: ver [`MANIFEST.sha256`](MANIFEST.sha256).
- Convención: `T` = teoría; `P` = plantilla.

Los 36 archivos están inventariados abajo. Las parejas teoría/plantilla comparten propósito y destino; cada fila enumera todos sus archivos para evitar piezas huérfanas.

## 1. Rumbo — 9 archivos

| ID | Originales | Propósito | Destino en la instancia | Puente al sistema híbrido |
|---|---|---|---|---|
| R00 | `Rumbo_00_Que_es_Rumbo.docx` | Introducir la función de dirección y su relación con el resto del sistema. | `personas/metodo-v3/originales/01-rumbo/` | Fuente de intención y límites; el agente no decide el rumbo. |
| R01-T/P | `Rumbo_01_Proposito_y_Meta_Teoria.docx` · `Rumbo_01_Proposito_y_Meta_Plantilla.docx` | Fijar propósito, horizonte y una meta medible. | `personas/metodo-v3/originales/01-rumbo/` | Alimenta identidad, objetivos y criterios de validación. |
| R02-T/P | `Rumbo_02_Valores_Innegociables_Teoria.docx` · `Rumbo_02_Valores_Innegociables_Plantilla.docx` | Definir 3–5 valores observables y no negociables. | `personas/metodo-v3/originales/01-rumbo/` | Limita conducta; su interpretación material sigue siendo humana. |
| R03-T/P | `Rumbo_03_Como_Ganamos_Teoria.docx` · `Rumbo_03_Como_Ganamos_Plantilla.docx` | Definir cliente central, promesa medible, diferenciadores y ventaja. | `personas/metodo-v3/originales/01-rumbo/` | Da contexto a prioridades y rechazos; no autoriza acciones externas. |
| R04-T/P | `Rumbo_04_Caja_y_North_Stars_Teoria.docx` · `Rumbo_04_Caja_y_North_Stars_Plantilla.docx` | Vincular beneficio por unidad, North Stars, owners y colchón de caja. | `personas/metodo-v3/originales/01-rumbo/` | Define métricas y umbrales; decisiones económicas conservan gate humano. |

## 2. Personas — 9 archivos

| ID | Originales | Propósito | Destino en la instancia | Puente al sistema híbrido |
|---|---|---|---|---|
| E00 | `00_Catalogo_Capacidades_y_Escalas.xlsx` | Normalizar capacidades y escalas de dominio. | `personas/metodo-v3/originales/02-personas/` | Ayuda a separar capacidad de ejecutor y a detectar brechas. |
| E02-T/P | `02_El_organigrama_de_asientos_Teoria.docx` · `02_El_organigrama_de_asientos_Plantilla.docx` | Asignar un dueño a cada función antes de elegir nombres o agentes. | `personas/metodo-v3/originales/02-personas/` | Un agente ocupa un asiento; no crea un organigrama paralelo. |
| E03-T/P | `03_La_ficha_de_puesto_Teoria.docx` · `03_La_ficha_de_puesto_Plantilla.docx` | Definir resultado, responsabilidades, KPIs y capacidades del asiento. | `personas/metodo-v3/originales/02-personas/` | Fuente para `ROLE_CARD`, identidad y operaciones del agente. |
| E04-T/P | `04_La_matriz_de_decisiones_Teoria.docx` · `04_La_matriz_de_decisiones_Plantilla.docx` | Aclarar quién decide, consulta, ejecuta y escala. | `personas/metodo-v3/originales/02-personas/` | Fuente de permisos, autonomía, gates y prohibiciones. |
| E05-T/P | `05_La_evaluacion_Teoria.docx` · `05_La_evaluacion_Plantilla.xlsx` | Revisar resultados, capacidades y valores con una cadencia. | `personas/metodo-v3/originales/02-personas/` | Se conecta al scorecard y a la revisión de madurez del agente. |

## 3. Procesos — 4 archivos

| ID | Originales | Propósito | Destino en la instancia | Puente al sistema híbrido |
|---|---|---|---|---|
| P06-T/P | `06_El_mapa_de_procesos_Teoria.docx` · `06_El_mapa_de_procesos_Plantilla.docx` | Identificar procesos principales, entradas, salidas, handoffs y gates. | `personas/metodo-v3/originales/03-procesos/` | Selecciona capacidades candidatas; una señal inválida no convierte todo el proceso en inválido. |
| P07-T/P | `07_El_SOP_Teoria.docx` · `07_El_SOP_Plantilla.docx` | Documentar pasos, responsables, criterios, excepciones y evidencia. | `personas/metodo-v3/originales/03-procesos/` | Fuente de `OPERATIONS.md`, skills, tools, validación y fallback. |

## 4. Caja — 2 archivos

| ID | Originales | Propósito | Destino en la instancia | Puente al sistema híbrido |
|---|---|---|---|---|
| C08-T/P | `08_El_panel_de_caja_Teoria.docx` · `08_El_panel_de_caja_Plantilla.xlsx` | Vigilar liquidez, cobros, pagos, margen y colchón con responsables. | `personas/metodo-v3/originales/04-caja/` | El agente puede calcular y alertar; gasto, pagos y compromisos siguen su matriz. |

## 5. Ejecución — 6 archivos

| ID | Originales | Propósito | Destino en la instancia | Puente al sistema híbrido |
|---|---|---|---|---|
| X09-T/P | `09_Los_hitos_Teoria.docx` · `09_Los_hitos_Plantilla.docx` | Convertir rumbo en pocas prioridades de operación y capacidad. | `personas/metodo-v3/originales/05-ejecucion/` | El humano elige; el agente sigue estado y alerta riesgos. |
| X10-T/P | `10_La_lista_de_action_items_Teoria.docx` · `10_La_lista_de_action_items_Plantilla.docx` | Convertir decisiones en compromisos concretos, con dueño y fecha. | `personas/metodo-v3/originales/05-ejecucion/` | El agente captura, recuerda y registra; no cambia el compromiso sin autoridad. |
| X11-T/P | `11_El_seguimiento_Teoria.docx` · `11_El_seguimiento_Plantilla.xlsx` | Mostrar avance, bloqueo, responsable y próxima acción. | `personas/metodo-v3/originales/05-ejecucion/` | Alimenta scorecards, alertas y receipts. |

## 6. Sistema nervioso — 4 archivos

| ID | Originales | Propósito | Destino en la instancia | Puente al sistema híbrido |
|---|---|---|---|---|
| N12-T/P | `12_El_panel_de_indicadores_Teoria.docx` · `12_El_panel_de_indicadores_Plantilla.xlsx` | Definir indicadores, fórmula, fuente, owner, umbral y cadencia. | `personas/metodo-v3/originales/06-sistema-nervioso/` | Fuente de scorecards, heartbeats y alertas; no sustituye la interpretación humana. |
| N13-T/P | `13_El_sistema_de_aprendizaje_continuo_Teoria.docx` · `13_El_sistema_de_aprendizaje_continuo_Plantilla.xlsx` | Registrar desvío, causa raíz, acción correctiva, aprendizaje y seguimiento. | `personas/metodo-v3/originales/06-sistema-nervioso/` | Fuente de memoria, receipts y StateChanges revisados. |

## 7. Cadencia — 2 archivos

| ID | Originales | Propósito | Destino en la instancia | Puente al sistema híbrido |
|---|---|---|---|---|
| D14-T/P | `14_El_pulso_de_reuniones_Teoria.docx` · `14_El_pulso_de_reuniones_Plantilla.xlsx` | Diseñar reuniones diaria, semanal, mensual, trimestral y anual con agenda y salida. | `personas/metodo-v3/originales/07-cadencia/` | El agente prepara y registra; las personas revisan, juzgan y deciden. |

## Cobertura

- Rumbo: `9/9`.
- Personas: `9/9`.
- Procesos: `4/4`.
- Caja: `2/2`.
- Ejecución: `6/6`.
- Sistema nervioso: `4/4`.
- Cadencia: `2/2`.
- Total: `36/36`.

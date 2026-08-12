# Ejemplo sintético — una función en las tres capas

Empresa: `Northstar Service Lab` (sintética)
Función: `revisión de calidad antes de entregar un proyecto`

Este ejemplo muestra la relación; no representa una empresa implantada ni un agente activo.

## Personas

- Responsable humano: `Head of Delivery`.
- Ficha de puesto: responde por calidad y entrega.
- Matriz de decisiones: puede aprobar correcciones internas; cambios de alcance o contacto con cliente escalan a Dirección.
- SOP: checklist de 12 puntos, entrada `project package`, salida `QA report`.
- Indicador: `% entregas sin retrabajo`, revisión semanal.

## Agentes

- Agente: `Delivery QA Assistant`, estado `shadow`.
- Identidad: revisar contra el SOP, no reinterpretar el contrato.
- Fuentes: project brief y checklist vigente.
- Permisos: leer archivos del proyecto y redactar QA report; prohibido editar contrato o contactar al cliente.
- Operación: ejecutar los 12 checks y enlazar evidencia.
- Validación: el Head of Delivery revisa el informe.
- Memoria: solo aprendizajes aprobados mediante StateChange.
- Evidencia: Context Packet, QA report y Receipt.

## Sistema Híbrido

El contrato compartido nombra una sola función y un solo resultado. La persona conserva accountability y decisiones materiales; el agente ejecuta el tramo reglado. Si una fuente está obsoleta, la ejecución queda bloqueada y vuelve al responsable. Si la calidad se sostiene, puede pasar de `shadow` a `assisted`; el cambio requiere evidencia y revisión humana.

## Lo que no se debe hacer

- Copiar el SOP dentro del prompt y mantener dos versiones.
- Dar al agente todos los permisos del Head of Delivery.
- Marcar la función como autónoma porque el scaffold existe.
- Ocultar un fallo o un cambio del SOP fuera de receipts/StateChanges.

# Agentizar capacidades maduras

Objetivo: asignar una parte madura del trabajo a un agente sin desplazar la responsabilidad humana.

## Gate por capacidad

Antes de crear el agente, confirma:

- función y responsable humano;
- SOP seguido y estable;
- entradas y fuentes con dueño y vigencia;
- salida y métrica verificables;
- matriz de decisiones y umbrales;
- permisos de mínimo privilegio;
- validación, receipt, fallback y condición de parada.

Si falta una pieza, vuelve a [Organizar](organizar.md). No bloquea el resto de la empresa: esa capacidad se queda humana mientras otras sí pueden avanzar.

## Instalación

1. Completa un [contrato de función híbrida](../sistema-hibrido/contrato-de-funcion.md).
2. Instala el [`agent-runtime-pack`](../templates/agent-runtime-pack/README.md).
3. Enlaza las fuentes humanas mediante la [matriz de equivalencias](../sistema-hibrido/matriz-de-equivalencias.md).
4. Empieza en `draft` o `pilot`, nunca en autonomía plena.
5. Ejecuta un loop interno y reversible con revisión humana.
6. Conserva Context Packet, Receipt, StateChange y scorecard.

La conexión de herramientas, credenciales o servicios es una acción posterior y sujeta a aprobación; una carpeta generada no significa que el agente esté operativo.

# Sistema Híbrido

El Sistema Híbrido es la capa compartida que hace trabajar a personas y agentes sobre la misma empresa. No es una tercera organización ni un catálogo de agentes: es el contrato que une funciones, responsables, ejecutores, autoridad, datos, cadencia y evidencia.

## Las tres capas

| Capa | Pregunta que responde | Artefactos principales |
|---|---|---|
| [Personas](../personas/README.md) | ¿Cómo se organiza y gobierna la empresa? | Rumbo, asientos, puestos, decisiones, evaluación, procesos, SOP, caja, ejecución, indicadores, aprendizaje y reuniones. |
| [Agentes](../agentes/README.md) | ¿Cómo ejecuta un agente una capacidad madura? | Identidad, contrato, permisos, herramientas, memoria, operaciones, madurez, supervisión y evidencias. |
| **Sistema Híbrido** | ¿Cómo comparten una función sin perder responsabilidad ni trazabilidad? | Contrato de función, matriz de equivalencias, gate de agentización, receipts y cadencia de revisión. |

## Invariantes

1. **Función no es ejecutor.** Una función puede ejecutarla una persona, un agente o una pareja humano-agente.
2. **Siempre responde una persona.** La automatización no desplaza la responsabilidad humana.
3. **Rumbo y criterio material siguen siendo humanos.** Los agentes pueden analizar, preparar, vigilar y ejecutar dentro de límites.
4. **La autoridad es explícita y menor o igual que la del responsable.** Un agente no hereda permisos por acceso técnico.
5. **Una aprobación identifica la acción concreta.** No es una autorización general ni una frase ambigua.
6. **Toda acción significativa deja evidencia.** Debe poder reconstruirse qué ocurrió, con qué fuentes, bajo qué permiso y con qué resultado.
7. **Un fallo degrada la autonomía.** La madurez no aumenta por antigüedad, sino por evidencia repetida.
8. **Instalación no equivale a operación.** Una carpeta, una plantilla o un agente configurado no prueban una empresa implantada.

## Recorrido OAE

1. **Organizar personas**: completar la capa humana y poner responsables a las funciones.
2. **Agentizar capacidades maduras**: aplicar el gate a una capacidad concreta, no a un departamento entero.
3. **Escalar el sistema híbrido**: aumentar alcance solo cuando operación, supervisión y evidencia se sostienen.

Empieza por [`../implementacion/organizar.md`](../implementacion/organizar.md), continúa por [`../implementacion/agentizar.md`](../implementacion/agentizar.md) y escala con [`../implementacion/escalar.md`](../implementacion/escalar.md).

## Contrato de cada función

Cada función compartida debe completar [`contrato-de-funcion.md`](contrato-de-funcion.md). El contrato nombra:

- resultado y métrica;
- responsable humano;
- ejecutor actual;
- fuentes y vigencia;
- SOP y entradas/salidas;
- decisiones y autoridad;
- acciones permitidas, prohibidas y con aprobación;
- evidencia, cadencia y fallback.

La [matriz de equivalencias](matriz-de-equivalencias.md) evita mantener dos verdades distintas para personas y agentes.

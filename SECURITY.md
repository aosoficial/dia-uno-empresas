# Seguridad

Company Brain System debe poder convertirse en framework público sin exponer material sensible.

## Nunca incluir

- credenciales;
- tokens;
- contraseñas;
- API keys;
- connection strings;
- dumps de bases de datos;
- configuración real de Telegram/gateway;
- configuración privada de agentes reales;
- datos personales no autorizados;
- material legacy no aprobado.

## Piloto privado

El directorio `pilot/private/` queda fuera del framework público por defecto.

Solo puede convertirse en material público si pasa:

1. revisión anti-secretos;
2. anonimización;
3. revisión de fuente/licencia;
4. aprobación explícita del owner.

## Reportar un problema de seguridad

Si descubres un problema de seguridad (credenciales expuestas, datos sensibles, vulnerabilidad en scripts):

1. **No abras un issue público.** Los problemas de seguridad se reportan de forma privada.
2. Envía un email al owner del proyecto describiendo el problema.
3. Incluye: qué encontraste, en qué archivo/línea, y el impacto potencial.
4. Tiempo de respuesta esperado: 48 horas.

## Validación automática

El script `scripts/validate_repo.py` incluye detección de patrones de secretos. Se ejecuta en CI en cada push y pull request.

## Revisión periódica

Antes de cualquier publicación:

1. Ejecutar `python scripts/validate_repo.py` para detectar secretos.
2. Revisar `pilot/private/` — nada de ahí debe pasar a público sin anonimización.
3. Verificar que `.gitignore` está actualizado.
4. Buscar rutas absolutas o datos personales en todo el repositorio.

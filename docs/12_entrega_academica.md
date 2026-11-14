# Guía de entrega académica — cuatro componentes

## 1. Documento técnico
Usar como fuentes `docs/01_observabilidad.md`, `02_slo_alertas.md`, `03_dashboards.md`, `04_drift.md`, `05_runbooks.md`, `06_respuesta_automatizada.md` y `10_validacion_codespaces.md`. Incorporar arquitectura, métricas instrumentadas, logs/trazas, umbrales de alertas, SLO propuestos, presupuesto de error teórico y límites del prototipo. Los SLO a 30 días no se han validado con 30 días de operación.

## 2. Evidencia de implementación
Insertar las capturas auténticas indicadas en `evidence/screenshots/GUIA_CARGA.md` con pie de figura, fecha y explicación del indicador. Adjuntar la configuración Prometheus/Grafana desde `config/` y `dashboards/`. No representar capturas de la conversación como archivos ya presentes en GitHub.

## 3. Informe de incidentes
Base narrativa: `docs/11_informe_ejecucion_incidentes.md`. Comparar normal, latencia, errores y recuperación; incluir estados PENDIENTE, DISPARANDO e INACTIVO. Explicar ventana móvil 5m y duración `for: 2m`. Documentar que la recuperación fue por cambio a tráfico normal, no por rollback automático.

## 4. Código reproducible
Versionar `src/monitoring.py`, `src/traffic_generator.py`, `config/`, `dashboards/`, `docker-compose.yml`, `tests/` y archivos de dependencias. Validar en Codespaces; no requiere Docker Desktop local.

## Empaquetado
Cuando se hayan incorporado las capturas originales y generado los PDF, preparar ZIP con: documento técnico, evidencias, informe de incidentes y código/configuración. **El ZIP y los PDF no se consideran generados ni entregados por el presente cambio.**

## Calidad y honestidad técnica
- Se ejecutó monitorización real de un servicio simulado; no hay reconocimiento OCR en producción.
- La cifra de 0 accesos físicos es una propiedad de simulación fail-closed.
- La tasa de errores del dashboard es una tasa de ventana, no la fracción histórica de las 1.33k solicitudes.
- El script de automatización dry-run, si existe, requiere ejecución demostrada y logs para acreditarse.

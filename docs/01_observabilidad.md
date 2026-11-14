# 01. Monitorización y observabilidad

Estado: **diseño inicial, pendiente de instrumentación y evidencia**.

## Objetivos operativos
1. Evitar la autorización de vehículos no habilitados.
2. Mantener disponibilidad y buen tiempo de respuesta para residentes.
3. Detectar, diagnosticar y recuperar fallas rápidamente.
4. Mantener trazabilidad auditada respetando privacidad.

## Métricas (propuestas)
- Disponibilidad y tasa de errores del servicio.
- Latencias de extremo a extremo y de inferencia: p50, p95 y p99.
- Solicitudes por minuto, concurrencia y saturación.
- Errores por componente: captura, modelo, API, autorización, comunicación con actuador simulado.
- Precision, recall y tasa de falsos accesos autorizados, exclusivamente en datos etiquetados.
- Desviación de datos, confianza del modelo y versión activa.

## Logs estructurados
Campos sugeridos: timestamp UTC, service_name, event_type, severity, trace_id, request_id seudonimizado, model_version, latency_ms, status y outcome. **No** almacenar matrículas, rostros, credenciales ni imágenes reales en logs públicos.

## Trazas distribuidas
Captura → preprocesamiento → inferencia → reglas de residentes → decisión → actuador simulado. Mantener trace_id común y spans independientes.

## Evidencia pendiente
Recolección de métricas, logs y trazas reales/sintéticos etiquetados, capturas del dashboard y correlación de un incidente usando trace_id.

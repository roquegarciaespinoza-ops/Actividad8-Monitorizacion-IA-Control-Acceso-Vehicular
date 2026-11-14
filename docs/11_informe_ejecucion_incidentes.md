# Informe de ejecución — Actividad 8
**Fecha de ejecución observada:** 14 de noviembre de 2026. **Entorno:** GitHub Codespaces; simulador Python, Prometheus y Grafana. **Naturaleza:** tráfico y decisiones sintéticos, sin inferencia OCR real ni barrera física.

## Resumen ejecutivo
Se comprobó el ciclo de observabilidad: servicio expuesto en /metrics, target de Prometheus UP, dashboard de ocho paneles, reglas de alerta por latencia y errores, activación FIRING de ambas reglas y retorno a estado INACTIVO tras restaurar tráfico normal. Las observaciones proceden de capturas aportadas durante la ejecución; no se infieren horas exactas de mitigación ni tiempos MTTR.

## Línea base
- Dashboard con 78 solicitudes, servicio UP=1, errores 0%, latencia p95 aproximadamente 0.095 s y aperturas físicas 0.
- Generador normal: 360 solicitudes completadas y 0 fallas del cliente, según salida de terminal compartida.

## Incidente INC-01 — Latencia elevada (P2)
- **Inyección:** `python -m src.traffic_generator --scenario latency --seconds 180 --interval 0.5`.
- **Resultado del generador:** 72 solicitudes completadas, 0 fallas del cliente. La demora simulada por solicitud limita la tasa de solicitudes.
- **Señal:** p95 de Grafana por encima de 4 s; regla `VehicleSimulatorHighLatency` con expresión `histogram_quantile(0.95, sum by (le) (rate(vehicle_inference_seconds_bucket[5m]))) > 2` y `for: 2m`.
- **Evidencia:** primero PENDIENTE (valor ~3.65 s); posteriormente DISPARANDO (valor 4.818181818 s). Umbral 2 s; prioridad P2.
- **Respuesta observada:** cesó el escenario degradado y se volvió al tráfico normal; la alerta quedó INACTIVA y el p95 volvió a valores bajos. No se ejecutó rollback de un modelo real.
- **Runbook:** identificar → revisar p95/Prometheus y logs disponibles → retirar inyección sintética → comprobar p95 y alerta → cerrar con evidencia. La correlación individual por trace_id y el MTTR exacto no fueron aportados en capturas.

## Incidente INC-02 — Tasa de errores elevada (P2)
- **Inyección:** `python -m src.traffic_generator --scenario errors --seconds 180 --interval 0.5`.
- **Señal:** Grafana registró 76.2% y después 75.7% de tasa de errores en las respectivas capturas; Prometheus observó valor 0.7739285736 (77.39%) en la evaluación de alerta. Son instantes/consultas diferentes, no medidas contradictorias.
- **Regla:** `sum(rate(vehicle_requests_total{status="error"}[5m])) / clamp_min(sum(rate(vehicle_requests_total[5m])), 0.001) > 0.01`, `for: 2m`.
- **Evidencia:** primero PENDIENTE (valor ~0.2011), luego DISPARANDO; prioridad P2.
- **Respuesta observada:** reanudación de tráfico normal y espera hasta que la ventana móvil de 5 minutos excluyera los errores; tasa de errores de Grafana 0% y alerta INACTIVA.
- **Runbook:** confirmar error → verificar condición y alcance → detener escenario de fallas → generar tráfico normal → verificar error <1% y alerta INACTIVA → registrar cierre. No se demostró reinicio, rollback o reentrenamiento automáticos.

## Estado final comprobado
- Grafana: servicio UP=1; solicitudes acumuladas ~1.33k; tasa de errores 0%; accesos físicos autorizados 0; latencia p95 baja.
- Prometheus: 2 reglas INACTIVAS, 0 PENDIENTES, 0 DISPARANDO.
- **Interpretación:** recuperación operacional observada en simulación; la métrica UP solo acredita la disponibilidad del endpoint de métricas, no disponibilidad de un sistema físico de acceso.

## Evidencia y trazabilidad
Las capturas originales se compartieron en la conversación de trabajo; **todavía no están versionadas en GitHub**. No se deben inventar imágenes ni afirmar que ya forman parte del repositorio. Véase `evidence/screenshots/GUIA_CARGA.md` para incorporarlas con nombres trazables.

## Limitaciones y acciones abiertas
1. Validar logs estructurados y correlación de trazas con muestras exportadas.
2. Ejecutar y conservar prueba de respuesta automatizada dry-run si el script está disponible; distinguir diseño de ejecución.
3. Drift y precisión real del OCR no se evaluaron; los escenarios son sintéticos.
4. MTTA, MTTR, error budget consumido y eficacia de deduplicación no se cuantificaron con marcas de tiempo suficientes.
5. La cifra de solicitudes es acumulada del proceso; no equivale al número de peticiones de una única prueba.

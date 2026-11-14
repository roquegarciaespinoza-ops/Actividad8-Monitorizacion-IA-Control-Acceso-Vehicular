# Guía de ejecución y evidencia

**Requisitos:** Python 3.11+; Docker Compose opcional para Prometheus y Grafana.

## Validación rápida (sin paquetes externos)
Desde la raíz del repositorio:

```bash
python -m unittest discover -s tests -v
python -m simulations.incident_01_latency
python -m simulations.incident_02_drift
python -m src.monitoring --requests 20
```

## Dashboard local (opcional)
Terminal A: `python -m src.monitoring --serve` (sirve /health y /metrics en 127.0.0.1:8000). Terminal B: `docker compose up -d`. Prometheus: http://localhost:9090; Grafana: http://localhost:3000 (configurar contraseña segura al iniciar). Para generar tráfico en el mismo proceso: `curl "http://127.0.0.1:8000/simulate?latency_ms=50"`; degradación: `curl "http://127.0.0.1:8000/simulate?latency_ms=2500"`; error: `curl "http://127.0.0.1:8000/simulate?fail=1"`. Repetir llamadas para producir series temporales. Este endpoint debe mantenerse solo en entorno local de laboratorio.

## Estado y límites
- El servicio usa datos sintéticos, no carga LinearSVC ni TrOCR.
- Las trazas son spans correlacionados en logs JSON, no un backend de trazas distribuidas aún.
- Las reglas de alertas son propuestas y requieren validación de funcionamiento real.
- La señal de drift es un cambio de confianza sintético, no una prueba estadística de drift de datos.
- La respuesta es solo dry-run; no hay rollback real ni acciones físicas.
- Las evidencias de GitHub Actions son artefactos de ejecución automatizada; las capturas de Grafana se producirán después de ejecutar el stack.

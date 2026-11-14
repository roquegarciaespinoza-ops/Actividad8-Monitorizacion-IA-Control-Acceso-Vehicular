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
Terminal A: `python -m src.monitoring --serve` (sirve /health y /metrics en 127.0.0.1:8000). Terminal B: `docker compose up -d`. Prometheus: http://localhost:9090; Grafana: http://localhost:3000 (configurar contraseña segura al iniciar). Las métricas se acumulan en el proceso que sirve /metrics: ejecutar solicitudes de inferencia en otro proceso no modifica ese contador. Se incorporará un generador HTTP para tráfico al mismo proceso en la siguiente iteración.

## Estado y límites
- El servicio usa datos sintéticos, no carga LinearSVC ni TrOCR.
- Las trazas son spans correlacionados en logs JSON, no un backend de trazas distribuidas aún.
- Las reglas de alertas son propuestas y requieren validación de funcionamiento real.
- La señal de drift es un cambio de confianza sintético, no una prueba estadística de drift de datos.
- La respuesta es solo dry-run; no hay rollback real ni acciones físicas.
- Las evidencias de GitHub Actions son artefactos de ejecución automatizada; las capturas de Grafana se producirán después de ejecutar el stack.

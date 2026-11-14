# Actividad 8 — Monitorización de IA para control de acceso vehicular

Proyecto académico de Gestión de proyectos de inteligencia artificial, Módulo 3, Semana 10 (temas 19 y 20).

## Estado verificado — 14 de noviembre de 2026
**Implementados y observados:** simulador sintético Python, Prometheus, Grafana (8 paneles), tráfico normal/latencia/errores, alertas de latencia y errores en FIRING y recuperación final con ambas alertas INACTIVAS. Servicio de métricas UP; 0 aperturas físicas.

**Pendientes para entrega:** incorporar capturas originales al repositorio; comprobar evidencia de logs/trazas y automatización dry-run; exportar PDF y ZIP académicos. No hay modelo OCR real desplegado ni sistema de autorización física.

## Lectura principal
- [Informe de incidentes ejecutados](docs/11_informe_ejecucion_incidentes.md)
- [Guía de los cuatro entregables](docs/12_entrega_academica.md)
- [Guía de carga de capturas](evidence/screenshots/GUIA_CARGA.md)
- [Validación Codespaces](docs/10_validacion_codespaces.md)
- [Observabilidad](docs/01_observabilidad.md)
- [SLO y alertas](docs/02_slo_alertas.md)
- [Dashboards](docs/03_dashboards.md)
- [Drift](docs/04_drift.md)
- [Runbooks](docs/05_runbooks.md)
- [Automatización](docs/06_respuesta_automatizada.md)
- [Matriz de rúbrica](docs/07_matriz_rubrica.md)

## Reproducibilidad
En GitHub Codespaces: `docker compose up -d`. En terminal A ejecutar `ALLOW_PUBLIC_BIND=1 python -m src.monitoring --serve --host 0.0.0.0 --port 8000`; en terminal B usar `python -m src.traffic_generator --scenario normal --seconds 180 --interval 0.5` (sustituir `normal` por `latency` o `errors` para incidentes). Mantener los puertos de Codespaces privados.

## Continuidad y seguridad
Referencias solo lectura: [Actividad 4](https://github.com/roquegarciaespinoza-ops/Actividad4-Seleccion-Modelos-Prototipado-Rapido) y [Actividad 5](https://github.com/roquegarciaespinoza-ops/Actividad5-Gestion-Datos-Entrenamiento-MLflow). No se han modificado. No subir matrículas, imágenes, credenciales ni información real de residentes. El simulador siempre deniega aperturas físicas.

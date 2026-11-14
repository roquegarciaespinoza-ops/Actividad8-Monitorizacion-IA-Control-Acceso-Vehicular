# Validación real de Prometheus y Grafana en Codespaces

## Requisitos y límites
Los servicios se ejecutan en GitHub Codespaces; los puertos deben permanecer **privados**. No introducir matrículas reales ni secretos. La aplicación es un **simulador sintético**, no un sistema de control de acceso operativo.

## 1. Actualizar y levantar servicios
En el Codespace, desde la raíz del repositorio:
```bash
git pull --ff-only
docker compose up -d --force-recreate
docker compose ps
```
El dashboard se aprovisiona automáticamente en Grafana → Dashboards → Actividad 8. Si Grafana ya estaba abierto, refrescar la página.

## 2. Mantener vivo el simulador
En terminal A:
```bash
ALLOW_PUBLIC_BIND=1 python -m src.monitoring --serve --host 0.0.0.0 --port 8000
```
Si ya está funcionando en otra terminal, **no iniciar una segunda instancia**.

## 3. Generar tráfico sintético y capturar métricas
En terminal B:
```bash
python -m src.traffic_generator --scenario normal --seconds 180 --interval 0.5
```
Abrir Prometheus → Status → Targets y Grafana → Dashboards → Actividad 8. Capturar imágenes con fecha, target UP y series temporales visibles.

## 4. Incidente de latencia
En terminal B, tras terminar el tráfico normal:
```bash
python -m src.traffic_generator --scenario latency --seconds 180 --interval 0.5
```
**Atención:** cada solicitud tarda 2.5 segundos y el generador es secuencial, por lo que habrá unas 72 solicitudes en 180 segundos. El p95 debería subir, pero el disparo depende de la ventana de 5 minutos y la condición `for: 2m`. Confirmar el estado real en Prometheus → Alerts; **no asumir FIRING**. Capturar métricas y alerta si se activa.

## 5. Incidente de errores
```bash
python -m src.traffic_generator --scenario errors --seconds 180 --interval 0.5
```
Comprobar la regla `VehicleSimulatorHighErrorRate` en Prometheus → Alerts. Verificar su estado y capturar evidencia.

## 6. Recuperación
```bash
python -m src.traffic_generator --scenario normal --seconds 180 --interval 0.5
```
El resultado dependerá de la mezcla de muestras en las ventanas de 5 minutos. Registrar tiempos reales de recuperación y estado final. La respuesta automatizada disponible es **dry-run**: no hay rollback ni reentrenamiento reales.

## 7. Evidencia mínima
- Captura de los dos contenedores UP en `docker compose ps`.
- Target `vehicle-access-simulator` UP.
- Grafana con datasource Prometheus y dashboard con datos.
- Prometheus → Alerts con reglas visibles y estados comprobados.
- Logs JSON correlacionados por `trace_id`.
- Registros de incidentes y respuesta dry-run.

## Limitaciones
El cambio de confianza sintético no equivale a data drift estadísticamente validado. No presentar el p95 sintético como rendimiento de TrOCR o LinearSVC. Las capturas deben proceder de herramientas realmente ejecutadas.

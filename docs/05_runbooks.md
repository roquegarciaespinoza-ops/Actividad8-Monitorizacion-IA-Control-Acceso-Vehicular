# 05. Runbooks de incidentes
**Estado:** RB-01 y RB-03 ejecutados en forma operativa simplificada mediante tráfico sintético; rollback/reentrenamiento no ejecutados.

## RB-01: latencia alta (P2)
1. Detectar p95 >2 s durante 2m en Prometheus y registrar estado PENDIENTE/FIRING.
2. Comprobar disponibilidad, solicitudes, tasa de errores y traza/log si está disponible.
3. Mitigación del laboratorio: terminar escenario `latency` y ejecutar `normal`.
4. Verificar p95 <2 s y transición a INACTIVO; conservar capturas.
5. Registrar causa inducida (latencia sintética), impacto, límites y acciones preventivas.

## RB-02: drift/calidad del modelo (no ejecutado)
1. Confirmar referencia y versión del modelo.
2. Medir cambio de distribuciones y desempeño en datos etiquetados.
3. Mantener acceso denegado por defecto ante incertidumbre.
4. Proponer validación/rollback solo con aprobación y pruebas.
5. Registrar evidencia y causa; no afirmar drift real sin medición.

## RB-03: tasa de errores alta (P2)
1. Detectar tasa de errores >1% durante 2m; registrar estado.
2. Revisar `vehicle_requests_total{status="error"}`, logs y alcance.
3. Mitigación del laboratorio: terminar escenario `errors` y ejecutar `normal`.
4. Esperar ventana móvil 5m; confirmar tasa <1% y alerta INACTIVA.
5. Registrar resultados y preservar evidencia. No atribuir la recuperación a rollback automático.

## Priorización
P1: riesgo de apertura física no autorizada; P2: degradación operativa sostenida; P3: anomalía sin impacto inmediato. En este laboratorio no hubo actuador físico.

## Ejecución documentada
Véase [informe de incidentes](11_informe_ejecucion_incidentes.md). No se dispone de marcas de tiempo suficientes para reportar MTTA/MTTR exactos.

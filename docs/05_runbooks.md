# 05. Runbooks de incidentes

Estado: **diseño; ejecución pendiente**.

## RB-01: degradación de latencia
1. Registrar ID de incidente, hora, responsable, SLO afectado y severidad.
2. Correlacionar métricas, logs y trazas para localizar la causa.
3. Ejecutar mitigación autorizada en ambiente de pruebas (reducir carga, revertir cambio controlado).
4. Verificar latencia p95, tasa de errores y política de acceso seguro.
5. Documentar antes/después, MTTA, MTTR, causa raíz y cierre.

## RB-02: drift/degradación del modelo
1. Confirmar la alerta, versión y dataset de referencia.
2. Analizar si existe data drift y si hay caída real en datos etiquetados.
3. Impedir autorizaciones basadas en predicciones inseguras o inciertas.
4. Evaluar rollback a versión previamente validada, con aprobación y simulación.
5. Verificar recuperación, registrar evidencias y acciones preventivas.

P1: riesgo de apertura no autorizada; P2: degradación que afecta continuidad; P3: anomalía de seguimiento sin impacto inmediato.

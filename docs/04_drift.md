# 04. Detección de data drift

Estado: **estrategia, pendiente de ejecución**.

- Versionar conjunto de referencia representativo.
- Comparar distribuciones de entradas o embeddings por intervalo y por condición ambiental.
- Definir pruebas/umbrales calibrados según tamaño de muestra y falsas alarmas.
- Distinguir data drift de degradación de rendimiento: esta última requiere etiquetas de referencia verificadas.
- Investigar variaciones de luz, ángulo, cámara y clima.
- Escalar a evaluación y, solo si se justifica, propuesta de reentrenamiento y validación antes del despliegue.

No desplegar ni reentrenar automáticamente un modelo que decide el acceso a instalaciones.

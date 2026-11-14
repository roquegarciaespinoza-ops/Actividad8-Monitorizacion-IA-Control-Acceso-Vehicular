# Ejecución de la Actividad 8 en Google Colab

## Objetivo
Generar evidencias reproducibles sin instalar Docker en la computadora corporativa. El notebook ejecuta pruebas, dos simulaciones de incidentes, mediciones sintéticas y gráficos. **No se afirma que Grafana o Prometheus estén ejecutándose en Colab**: las métricas se exportan en formato Prometheus y las gráficas se producen con Matplotlib.

## Instrucciones
1. Abrir [notebook en GitHub](../notebooks/Actividad8_Monitorizacion_Colab.ipynb) y seleccionar **Open in Colab** o cargar el archivo en Colab desde GitHub.
2. Menú **Entorno de ejecución → Ejecutar todas**.
3. Esperar a que finalicen las pruebas; revisar que no haya errores.
4. El notebook genera `Actividad8_evidencia_colab.zip` con JSON de incidentes, mediciones, gráficos PNG y texto de métricas.
5. Compartir aquí el ZIP descargado para integrar evidencia y documentos finales.

## Limitaciones
- El simulador no ejecuta TrOCR ni LinearSVC real, y no usa datos de residentes.
- Los incidentes son sintéticos; no hay rollback real ni apertura física.
- Las gráficas muestran comportamiento del simulador; la validación de Grafana y de las alertas Prometheus permanece pendiente.
- No exponer credenciales o imágenes de matrículas.

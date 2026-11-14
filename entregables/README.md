# Entregables de la Actividad 8

Fuente de verdad: este repositorio GitHub.

## Estado verificado el 14/11/2026
- **ZIP publicado:** `Actividad8_entrega_evidencias_y_documentos.zip` (2,196,274 bytes, confirmado en el árbol remoto de GitHub).
- **Contenido interno del ZIP:** pendiente de inspección binaria; la existencia del archivo no prueba que incluya los cuatro componentes exigidos.
- **Fuentes técnicas versionadas:** `docs/`, `src/`, `config/`, `dashboards/`, `simulations/`, `tests/` y `docker-compose.yml`.
- **Evidencia operacional observada:** Grafana y Prometheus durante tráfico normal, latencia elevada, errores y recuperación; véase `docs/11_informe_ejecucion_incidentes.md`.
- **Capturas individuales en GitHub:** todavía no hay imágenes en `evidence/screenshots/`; únicamente archivos Markdown. Las capturas podrían estar dentro del ZIP, pero esto no se ha inspeccionado.
- **Automatización:** `src/automated_response.py` implementa una decisión auditable **dry-run** para `latency` y `drift`; no ejecuta mitigación ni rollback. Falta acreditar su ejecución mediante registros verificables.

## Doble check antes de entrega
- [x] Repositorio sincronizado y ZIP publicado.
- [x] Código fuente y configuraciones de observabilidad presentes.
- [x] Dos incidentes de latencia y errores documentados con evidencia visual compartida.
- [ ] Inspeccionar archivos internos del ZIP: PDF técnico, PDF de evidencia, PDF de incidentes y código ejecutable completo.
- [ ] Verificar que los PDF abran correctamente y contengan capturas legibles y originales.
- [ ] Ejecutar y conservar evidencia del script de automatización dry-run y de las pruebas unitarias.
- [ ] Corregir las descripciones antiguas de estado en README y matriz de rúbrica una vez validado el paquete.

**Conclusión:** publicación confirmada; conformidad académica final aún condicionada a la inspección del ZIP y las pruebas de automatización. No confundir simulación con despliegue de OCR o barreras físicas.

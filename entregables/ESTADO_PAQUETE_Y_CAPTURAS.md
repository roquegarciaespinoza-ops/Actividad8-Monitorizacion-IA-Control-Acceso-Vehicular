# Evidencia recuperada y paquete académico generado — 14/11/2026

Se localizaron 36 imágenes originales en los adjuntos de la conversación y se seleccionaron 8 capturas auténticas para el PDF de evidencia. También se prepararon tres PDF y un ZIP de trabajo en el entorno de la conversación. **Los archivos binarios aún no se han subido a este repositorio.**

## Capturas seleccionadas
- `image(20261114-195502).png`: conexión Prometheus exitosa.
- `image(20261114-200415).png`: dashboard línea base.
- `image(20261114-200953).png`: dashboard latencia.
- `image(20261114-201310).png`: alerta de latencia disparada.
- `image(20261114-201353).png`: dashboard errores.
- `image(20261114-201728).png`: alerta de errores disparada.
- `image(20261114-202055).png`: dashboard recuperado.
- `image(20261114-202120).png`: alertas inactivas.

## Archivos preparados fuera de GitHub
- `01_documento_tecnico.pdf`
- `02_evidencia_implementacion.pdf`
- `03_simulacion_incidentes.pdf`
- `04_codigo_y_configuracion.txt` (enlace al código, no copia íntegra)
- `Actividad8_entrega_evidencias_y_documentos.zip` (paquete parcial de trabajo)

## Acción de incorporación a GitHub
Descargar el ZIP desde la conversación, subirlo al Codespace y ejecutar desde la raíz del repositorio:

```bash
mkdir -p entregables
mv Actividad8_entrega_evidencias_y_documentos.zip entregables/
git add entregables/Actividad8_entrega_evidencias_y_documentos.zip
git commit -m "evidence: incorporar PDFs y capturas originales de la Actividad 8"
git push origin main
```

Para generar **ZIP final con copia íntegra del código**, incluir una exportación del repositorio junto con los PDF/capturas. El paquete de trabajo no cumple todavía por sí solo el requisito de código incluido en ZIP.

## Verificación pendiente
Revisar PDF y capturas; demostrar respuesta automatizada si está implementada; comprobar archivos binarios realmente cargados en GitHub antes de marcar la entrega final.

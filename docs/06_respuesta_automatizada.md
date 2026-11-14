# 06. Respuesta automatizada y gobernanza

Estado: **diseño; código y resultados pendientes**.

Flujo: detectar → correlacionar → clasificar → deduplicar → notificar → ejecutar acción permitida → verificar recuperación → registrar auditoría.

Acciones automatizables: crear incidente, enviar alerta, preservar evidencias, limitar reintentos, habilitar diagnóstico y ejecutar rollback únicamente en simulación validada y con controles.

Acciones prohibidas sin autorización humana: abrir barrera física, cambiar permisos de residentes, borrar evidencias o desplegar modelos no validados.

La automatización debe ser idempotente, contar con timeout y límites de reintentos, generar log estructurado y tener modo `dry-run` por defecto. Medir eficacia antes de dar por cumplido el criterio.

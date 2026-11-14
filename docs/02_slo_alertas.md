# 02. SLI, SLO, error budgets y alertas

Estado: **umbrales candidatos sujetos a línea base**.

| SLI | SLO propuesto | Ventana | Verificación |
|---|---|---|---|
| Disponibilidad de API | ≥99.9% | 30 días | Solicitudes válidas disponibles/total |
| Latencia de inferencia p95 | ≤2 segundos | 30 días | Histograma de inferencias |
| Tasa de fallas técnicas | ≤1% | 30 días | Errores de servicio/solicitudes válidas |
| Auditabilidad | 100% | 30 días | Decisiones registradas/decisiones totales |

Para disponibilidad de 99.9%, el error budget es 0.1% de la ventana; sobre 30 días completos equivale a 43.2 minutos, sujeto a la definición precisa del SLI.

Alertas propuestas: P1 de seguridad y disponibilidad, P2 por degradación sostenida, P3 de investigación de drift; deduplicación por causa raíz, duración mínima, agrupación, inhibición de alertas derivadas, ventanas de silencio auditadas y criterios de burn rate.

Una falla de inferencia o autorización **nunca** implica abrir la barrera automáticamente. Las acciones que afecten seguridad física requieren control autorizado.

Pendiente: reglas ejecutables, dashboard y demostración de activación y recuperación.

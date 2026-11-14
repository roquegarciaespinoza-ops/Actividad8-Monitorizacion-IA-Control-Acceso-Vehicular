"""Señal sencilla de cambio de confianza en datos sintéticos, NO drift validado."""
from statistics import mean

def confidence_shift(reference, current, threshold=0.2):
    if len(reference) < 5 or len(current) < 5:
        raise ValueError("Se requieren al menos cinco observaciones por ventana")
    if any(not 0 <= x <= 1 for x in reference + current):
        raise ValueError("Confianzas fuera del rango [0,1]")
    delta = abs(mean(reference) - mean(current))
    return {"reference_mean": mean(reference), "current_mean": mean(current),
            "absolute_shift": delta, "threshold": threshold,
            "alert": delta > threshold,
            "note": "Indicador didáctico de cambio de confianza; no prueba drift estadístico"}

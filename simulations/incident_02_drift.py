"""Simulación reproducible de cambio de confianza y runbook RB-02."""
import json
from src.drift_detection import confidence_shift
from src.automated_response import respond

def run():
    reference = [0.96, 0.97, 0.95, 0.98, 0.96, 0.97]
    current = [0.39, 0.44, 0.42, 0.40, 0.43, 0.41]
    detected = confidence_shift(reference, current)
    assert detected["alert"]
    response = respond({"id": "SIM-DRIFT-002", "type": "drift"})
    recovery = confidence_shift(reference, reference.copy())
    assert not recovery["alert"]
    return {"incident_id": "SIM-DRIFT-002", "detection": detected,
            "response": response, "recovery": recovery,
            "status": "simulation_complete",
            "note": "Valores sintéticos; recuperación simulada, no reentrenamiento ni rollback real"}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))

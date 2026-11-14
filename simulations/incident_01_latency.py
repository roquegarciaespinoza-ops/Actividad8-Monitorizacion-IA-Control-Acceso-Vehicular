"""Simulación reproducible de aumento de latencia y runbook RB-01."""
import json
from src.monitoring import infer
from src.automated_response import respond

def run():
    before = [infer(simulated_latency_ms=10) for _ in range(5)]
    degraded = [infer(simulated_latency_ms=250) for _ in range(5)]
    incident = {"id": "SIM-LAT-001", "type": "latency"}
    action = respond(incident)
    recovered = [infer(simulated_latency_ms=10) for _ in range(5)]
    assert all(not x["access_granted"] for x in before + degraded + recovered)
    return {"incident": incident, "baseline_requests": len(before),
            "degraded_requests": len(degraded), "recovery_requests": len(recovered),
            "response": action, "status": "simulation_complete",
            "note": "Señal de latencia inyectada; no es medición de inferencia real"}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))

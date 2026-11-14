"""Motor de respuesta determinista, auditable y seguro: dry-run obligatorio."""
from datetime import datetime, timezone
import json

def respond(incident, dry_run=True):
    if not dry_run:
        raise PermissionError("Solo se permite dry-run; no hay acceso a barreras ni despliegues.")
    if incident["type"] not in {"latency", "drift"}:
        raise ValueError("Tipo de incidente no permitido")
    action = "investigate_and_throttle_simulation" if incident["type"] == "latency" else "flag_for_human_model_review"
    return {"timestamp": datetime.now(timezone.utc).isoformat(),
            "incident_id": incident["id"], "type": incident["type"],
            "action": action, "mode": "dry-run",
            "status": "recorded", "access_granted": False}

def to_json(event):
    return json.dumps(event, ensure_ascii=False, sort_keys=True)

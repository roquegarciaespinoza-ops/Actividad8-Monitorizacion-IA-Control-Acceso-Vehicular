"""Genera tráfico HTTP sintético para el simulador en Codespaces.

Uso: python -m src.traffic_generator --scenario normal --seconds 180 --interval 0.5
     python -m src.traffic_generator --scenario latency --seconds 180 --interval 0.5
     python -m src.traffic_generator --scenario errors --seconds 180 --interval 0.5
"""
import argparse
import json
import time
from urllib.parse import urlencode
from urllib.request import urlopen

def run(scenario, seconds, interval, base_url="http://127.0.0.1:8000"):
    if scenario not in ("normal", "latency", "errors"):
        raise ValueError("Escenario desconocido")
    if seconds <= 0 or interval <= 0:
        raise ValueError("seconds e interval deben ser positivos")
    parameters = {"latency_ms": 50 if scenario == "normal" else (2500 if scenario == "latency" else 50)}
    if scenario == "errors":
        parameters["fail"] = "1"
    endpoint = base_url.rstrip("/") + "/simulate?" + urlencode(parameters)
    deadline = time.monotonic() + seconds
    successes = 0
    failures = 0
    while time.monotonic() < deadline:
        started = time.monotonic()
        try:
            with urlopen(endpoint, timeout=8) as response:
                payload = json.load(response)
            if payload.get("access_granted") is not False:
                raise RuntimeError("Violación de fail-closed")
            successes += 1
        except Exception as exc:
            failures += 1
            print(json.dumps({"event":"traffic_error","error":str(exc)}),flush=True)
        remaining = interval - (time.monotonic() - started)
        if remaining > 0:
            time.sleep(min(remaining, max(0, deadline - time.monotonic())))
    result = {"scenario":scenario,"duration_requested_seconds":seconds,
              "requests_completed":successes,"client_failures":failures,
              "note":"Tráfico sintético sin apertura física ni inferencia de modelo real"}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario",choices=["normal","latency","errors"],required=True)
    parser.add_argument("--seconds",type=int,default=180)
    parser.add_argument("--interval",type=float,default=0.5)
    args = parser.parse_args()
    run(args.scenario,args.seconds,args.interval)

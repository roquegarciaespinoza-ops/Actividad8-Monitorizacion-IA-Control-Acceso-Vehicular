"""Simulador de servicio de OCR vehicular y observabilidad, sin hardware ni datos reales."""
import json
import logging
import os
import time
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock

LOGGER = logging.getLogger("vehicle_access")
logging.basicConfig(level=logging.INFO, format="%(message)s")
LOCK = Lock()
COUNTERS = defaultdict(int)
LATENCIES = []
MODEL_VERSION = "synthetic-ocr-v1"
BUCKETS = (0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10)

def record(event, trace_id, **fields):
    payload = {"timestamp": datetime.now(timezone.utc).isoformat(),
               "event_type": event, "trace_id": trace_id, "model_version": MODEL_VERSION, **fields}
    LOGGER.info(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return payload

def infer(simulated_latency_ms=65, fail=False, drift=False, request_id=None):
    """Retorna un resultado sintético; siempre niega apertura física."""
    trace_id = uuid.uuid4().hex
    request_id = request_id or uuid.uuid4().hex
    started = time.perf_counter()
    record("span_start", trace_id, span="capture", request_id=request_id)
    record("span_end", trace_id, span="capture", duration_ms=0)
    record("span_start", trace_id, span="inference")
    time.sleep(max(0, min(simulated_latency_ms, 5000)) / 1000)
    record("span_end", trace_id, span="inference", duration_ms=simulated_latency_ms)
    record("span_start", trace_id, span="authorization")
    status = "error" if fail else "ok"
    result = {"trace_id": trace_id, "request_id": request_id, "status": status,
              "predicted_character": None if fail else ("?" if drift else "A"),
              "confidence": 0 if fail else (0.42 if drift else 0.97),
              "access_granted": False, "actuator": "simulation_only",
              "model_version": MODEL_VERSION}
    record("span_end", trace_id, span="authorization", access_granted=False)
    elapsed = time.perf_counter() - started
    with LOCK:
        COUNTERS[(status, "true" if drift else "false")] += 1
        LATENCIES.append(elapsed)
    record("inference_complete", trace_id, status=status, drift=drift,
           latency_ms=round(elapsed * 1000, 2), access_granted=False)
    return result

def prometheus_metrics():
    with LOCK:
        counts = dict(COUNTERS)
        latencies = list(LATENCIES)
    lines = [
        "# HELP vehicle_requests_total Synthetic requests by outcome and drift flag",
        "# TYPE vehicle_requests_total counter",
    ]
    for status in ("ok", "error"):
        for drift in ("false", "true"):
            lines.append('vehicle_requests_total{status="%s",drift="%s"} %d' %
                         (status, drift, counts.get((status, drift), 0)))
    lines.extend([
        "# HELP vehicle_inference_seconds Inference request duration",
        "# TYPE vehicle_inference_seconds histogram",
    ])
    for bound in BUCKETS:
        lines.append('vehicle_inference_seconds_bucket{le="%s"} %d' %
                     (bound, sum(v <= bound for v in latencies)))
    lines.append('vehicle_inference_seconds_bucket{le="+Inf"} %d' % len(latencies))
    lines.append("vehicle_inference_seconds_sum %.6f" % sum(latencies))
    lines.append("vehicle_inference_seconds_count %d" % len(latencies))
    lines.extend(["# HELP vehicle_access_granted_total Granted physical accesses (always zero in simulation)",
                  "# TYPE vehicle_access_granted_total counter",
                  "vehicle_access_granted_total 0"])
    return "\n".join(lines) + "\n"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/simulate?"):
            from urllib.parse import parse_qs, urlsplit
            params = parse_qs(urlsplit(self.path).query)
            try:
                latency = int(params.get("latency_ms", ["65"])[0])
                if not 0 <= latency <= 5000:
                    raise ValueError("latency_ms fuera de rango")
                result = infer(simulated_latency_ms=latency, fail=params.get("fail", ["0"])[0] == "1",
                               drift=params.get("drift", ["0"])[0] == "1")
                body = json.dumps(result).encode()
                self.send_response(200)
            except ValueError:
                body = b'{"error":"invalid_latency"}'
                self.send_response(400)
            self.send_header("Content-Type", "application/json")
        elif self.path == "/metrics":
            body = prometheus_metrics().encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
        elif self.path == "/health":
            body = b'{"status":"ok","mode":"simulation"}'
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
        else:
            body = b"Not found"
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def serve(host="127.0.0.1", port=8000):
    if host not in ("127.0.0.1", "localhost", "::1") and os.getenv("ALLOW_PUBLIC_BIND") != "1":
        raise ValueError("Binding externo requiere ALLOW_PUBLIC_BIND=1")
    server = ThreadingHTTPServer((host, port), Handler)
    LOGGER.info("Metrics: http://%s:%s/metrics", host, port)
    try:
        server.serve_forever()
    finally:
        server.server_close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--requests", type=int, default=20)
    args = parser.parse_args()
    if args.serve:
        serve(args.host, args.port)
    else:
        for _ in range(args.requests):
            infer(simulated_latency_ms=10)
        print(prometheus_metrics())

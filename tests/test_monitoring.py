import unittest
from src.monitoring import infer, prometheus_metrics
from src.drift_detection import confidence_shift
from src.automated_response import respond
from simulations.incident_01_latency import run as latency_run
from simulations.incident_02_drift import run as drift_run

class MonitoringTests(unittest.TestCase):
    def test_fail_closed(self):
        self.assertFalse(infer(0, fail=True)["access_granted"])
        self.assertFalse(infer(0, drift=True)["access_granted"])

    def test_metrics(self):
        infer(0)
        metrics = prometheus_metrics()
        self.assertIn("vehicle_requests_total", metrics)
        self.assertIn("vehicle_inference_seconds_bucket", metrics)
        self.assertIn("vehicle_access_granted_total 0", metrics)

    def test_drift(self):
        self.assertTrue(confidence_shift([0.9]*5, [0.3]*5)["alert"])
        self.assertFalse(confidence_shift([0.9]*5, [0.9]*5)["alert"])

    def test_response_never_executes(self):
        with self.assertRaises(PermissionError):
            respond({"id": "1", "type": "latency"}, dry_run=False)

    def test_incidents(self):
        self.assertEqual(latency_run()["status"], "simulation_complete")
        self.assertEqual(drift_run()["status"], "simulation_complete")

if __name__ == "__main__":
    unittest.main()

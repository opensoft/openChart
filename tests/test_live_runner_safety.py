"""Retained QA logs exclude payloads and tokens; redirects cannot replay auth."""
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import threading
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
RUNNER = next(ROOT.glob("scripts/run_p*_live.py"))
spec = importlib.util.spec_from_file_location("recovered_live_runner", RUNNER)
runner = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = runner
spec.loader.exec_module(runner)


def configuration(base_url):
    return SimpleNamespace(label="SYN-QA", base_url=base_url, api_key="SYN-KEY",
                           api_secret="SYN-SECRET", site="qa.localhost")


class RedirectServer(BaseHTTPRequestHandler):
    observed = []

    def do_POST(self):
        self.observed.append(("POST", self.headers.get("Authorization")))
        self.send_response(302)
        self.send_header("Location", f"http://127.0.0.1:{self.server.server_port}/redirected")
        self.end_headers()
        self.wfile.write(b'{"message":"SYN-REDIRECT"}')

    def do_GET(self):
        self.observed.append(("GET", self.headers.get("Authorization")))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"message":{}}')

    def log_message(self, *_args):
        pass


class LiveRunnerSafety(unittest.TestCase):
    def test_retained_logs_only_hold_redacted_metadata_and_digests(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "records/http.jsonl"
            client = runner.HttpClient(configuration("http://localhost"), log)
            log.parent.mkdir(parents=True, exist_ok=True)
            request = {"patient": "SYN-PRIVATE-PATIENT", "medication": "SYN-PRIVATE-MEDICATION"}
            response = b'{"value":"SYN-PRIVATE-RESPONSE"}'
            client._log("SYN-STEP", "http://localhost/SYN-PRIVATE-URL", request,
                        "2026-10-03T00:00:00Z", 200, {"Set-Cookie": "SYN-SECRET-COOKIE"}, response)
            text = log.read_text()
            for marker in ["SYN-PRIVATE-PATIENT", "SYN-PRIVATE-MEDICATION", "SYN-PRIVATE-RESPONSE", "SYN-PRIVATE-URL", "SYN-SECRET-COOKIE"]:
                self.assertNotIn(marker, text)
            event = json.loads(text)
            self.assertFalse(event["payloads_recorded"])
            self.assertEqual(event["response"]["body_sha256"], hashlib.sha256(response).hexdigest())

    def test_redirect_is_refused_without_a_second_authenticated_request(self):
        RedirectServer.observed = []
        server = ThreadingHTTPServer(("127.0.0.1", 0), RedirectServer)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with tempfile.TemporaryDirectory() as directory:
                client = runner.HttpClient(configuration(f"http://127.0.0.1:{server.server_port}"), Path(directory) / "records/http.jsonl")
                client._raw_path.parent.mkdir(parents=True, exist_ok=True)
                with self.assertRaises(runner.RunnerError) as raised:
                    client.request("SYN-REDIRECT", "/api/method/synthetic", {})
                self.assertEqual(raised.exception.status, 302)
                self.assertEqual(len(RedirectServer.observed), 1)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()

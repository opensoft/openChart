"""Retained QA logs exclude payloads and tokens; redirects cannot replay auth."""
import hashlib
from contextlib import ExitStack
from http.client import RemoteDisconnected, IncompleteRead
import os
from unittest import mock
from urllib.error import HTTPError
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
            self.assertEqual(event["request"]["body_sha256"], hashlib.sha256(json.dumps(request).encode()).hexdigest())
            self.assertFalse(event["payloads_recorded"])
            self.assertEqual(event["response"]["body_sha256"], hashlib.sha256(response).hexdigest())

    def test_identity_evidence_does_not_retain_response_headers(self):
        reply = runner.HttpReply({"version": "SYN-VERSION"}, {"Set-Cookie": "SYN-SECRET-COOKIE", "Proxy-Authorization": "SYN-SECRET-TOKEN"})
        client = SimpleNamespace(method=lambda *_args: reply, _config=configuration("http://localhost"))
        identity = runner.probe_identity(client)
        text = json.dumps(identity)
        self.assertNotIn("SYN-SECRET-COOKIE", text)
        self.assertNotIn("SYN-SECRET-TOKEN", text)
        self.assertNotIn("response_headers", identity)

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

    def test_credential_bearing_endpoints_are_rejected_before_logging(self):
        for url in ["http://SYN-USER:SYN-SECRET@localhost", "http://localhost?token=SYN-SECRET", "http://localhost#SYN-SECRET", "http://localhost:invalid", "file:///tmp/local"]:
            with self.subTest(url=url), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "records/http.jsonl"
                with self.assertRaises(runner.RunnerError) as raised:
                    runner.HttpClient(configuration(url), path)
                self.assertNotIn("SYN-SECRET", str(raised.exception))
                self.assertFalse(path.exists())

    def test_environment_rejects_credential_bearing_endpoint(self):
        env = {key: "SYN-VALUE" for key in ["HL_API_KEY", "HL_API_SECRET", "OC_API_KEY", "OC_API_SECRET", "EHR_API_KEY", "EHR_API_SECRET"]}
        keys = ["HL_BASE", "OC_BASE"] if "p6" in RUNNER.name else ["OC_BASE"] if "p4" in RUNNER.name else ["EHR_BASE"]
        for key in keys:
            with self.subTest(key=key), mock.patch.dict(os.environ, {**env, key: "http://localhost?token=SYN-SECRET"}, clear=True):
                with self.assertRaises(runner.RunnerError):
                    runner.Config.from_env()

    def test_disconnect_and_truncated_body_produce_retained_fail_evidence(self):
        for failure in [RemoteDisconnected("SYN-PRIVATE"), IncompleteRead(b"SYN-PRIVATE", 50)]:
            with self.subTest(kind=type(failure).__name__), tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
                root = Path(directory)
                stack.enter_context(mock.patch.object(runner, "ROOT", root))
                if hasattr(runner, "SPEC_ROOT"):
                    stack.enter_context(mock.patch.object(runner, "SPEC_ROOT", root))
                stack.enter_context(mock.patch.object(runner, "scenario_corpus", return_value=[]))
                stack.enter_context(mock.patch.object(runner, "probe_identity", return_value={"status": "unobserved"}))
                if hasattr(runner, "engine"):
                    stack.enter_context(mock.patch.object(runner.engine, "load_yaml", return_value={"pin": {}}))
                    stack.enter_context(mock.patch.object(runner, "previous_successor_receipts", return_value=set()))
                def execute(client, *_args):
                    return client.request("SYN-DISCONNECT", "/api/method/synthetic", {})
                stack.enter_context(mock.patch.object(runner, "execute", side_effect=execute))
                opener = mock.Mock()
                opener.open.side_effect = failure
                stack.enter_context(mock.patch.object(runner, "build_opener", return_value=opener))
                config = configuration("http://localhost")
                if "p6" in RUNNER.name:
                    config = SimpleNamespace(healthlinc=config, openchart=config)
                result = runner.write_evidence(config, "SYN-RUN", "2026-10-03T00:00:00Z", root / "var/SYN-RUN/http.jsonl")
                self.assertEqual(result, 2)
                evidence = json.loads(next(root.glob("specs/*/live-evidence/*/evidence.yaml")).read_text())
                self.assertEqual(evidence["verdict"], "FAIL")
                self.assertFalse(evidence["feeds_acceptance_report"])
                self.assertEqual(evidence["assertions"][-1]["id"], "SYN-DISCONNECT")
                self.assertNotIn("SYN-PRIVATE", json.dumps(evidence))

    def test_error_response_read_failure_is_typed_and_logged(self):
        class BrokenBody:
            closed = False
            def read(self, *_args):
                raise TimeoutError("SYN-PRIVATE")
            def close(self):
                pass
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(runner, "build_opener") as builder:
            builder.return_value.open.side_effect = HTTPError("http://localhost", 503, "unavailable", {}, BrokenBody())
            path = Path(directory) / "records/http.jsonl"
            client = runner.HttpClient(configuration("http://localhost"), path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with self.assertRaises(runner.RunnerError) as raised:
                client.request("SYN-ERROR-READ", "/api/method/synthetic", {})
            self.assertNotIn("SYN-PRIVATE", str(raised.exception))
            self.assertEqual(json.loads(path.read_text())["response"]["status"], 503)


if __name__ == "__main__":
    unittest.main()

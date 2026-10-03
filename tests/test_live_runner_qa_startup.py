"""Exercise actual QA shell recovery blocks without creating sites or stacks."""
from pathlib import Path
import os
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (ROOT / "docker/qa-init.sh").read_text()

class QAStartupRecovery(unittest.TestCase):
    def test_missing_sites_source_relinks_retained_volume(self):
        start = SCRIPT.index('if [ ! -L "$BENCH_DIR/sites" ]; then')
        end = SCRIPT.index('touch "$SITES_DIR/apps.txt"', start)
        block = SCRIPT[start:end]
        with tempfile.TemporaryDirectory() as directory:
            bench = Path(directory) / "bench"
            sites = Path(directory) / "sites"
            bench.mkdir()
            sites.mkdir()
            retained = sites / "SYN-retained"
            retained.write_text("SYN-EXISTING-SITE")
            env = {**os.environ, "BENCH_DIR": str(bench), "SITES_DIR": str(sites)}
            for _ in range(2):
                subprocess.run(["bash", "-e", "-c", block], env=env, check=True, capture_output=True)
                self.assertEqual((bench / "sites").resolve(), sites)
                self.assertEqual(retained.read_text(), "SYN-EXISTING-SITE")

    def test_existing_checkout_retries_failed_editable_installation(self):
        marker = 'if [ ! -d ./apps/open_chart/.git ]; then'
        if marker not in SCRIPT:
            self.skipTest("this app does not clone an upstream open_chart")
        start = SCRIPT.index(marker)
        end = SCRIPT.index('[ -s ./sites/apps.txt ]', start)
        block = SCRIPT[start:end]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "apps/open_chart/.git").mkdir(parents=True)
            (root / "env/bin").mkdir(parents=True)
            pip = root / "env/bin/pip"
            pip.write_text('#!/bin/sh\nif [ ! -f tried ]; then touch tried; exit 1; fi\ntouch installed\n')
            pip.chmod(0o755)
            command = 'git() { echo SYN-REV; }; export OC_REV=SYN-REV; ' + block
            first = subprocess.run(["bash", "-e", "-c", command], cwd=root, capture_output=True)
            self.assertNotEqual(first.returncode, 0)
            subprocess.run(["bash", "-e", "-c", command], cwd=root, capture_output=True, check=True)
            self.assertTrue((root / "installed").is_file())

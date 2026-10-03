#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

echo "== OC-QA-STEP: stop stack and wipe persistent QA volumes"
docker compose -f "$SCRIPT_DIR/qa-compose.yaml" down --volumes --remove-orphans
echo "OC-QA-RESULT: WIPED (database, bench home, sites, and credentials removed)"

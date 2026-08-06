#!/usr/bin/env bash
# Bench-dependent checks (feature 001, T002; brief D7; FR-001, SC-001).
#
# Runs INSIDE the frappe/bench container from docker/compose.yaml:
#   1. bench init pinned to Frappe version-15 on Python 3.11
#   2. clean site + open_chart install + migrate (FR-001)
#   3. the app's bench test suite (the golden round trip lands in T011)
#
# Every step reports; the last line is the machine-readable verdict the
# caller greps for. A failure names the step that failed — the D9 "no
# silent skip" rule applied inside the gate.

set -uo pipefail

SITE=test.localhost
APP_SRC=/workspace/open_chart
BENCH_DIR=/home/frappe/frappe-bench

step() { echo; echo "== OC-DOCKER-STEP: $1"; }
fail() { echo "OC-DOCKER-RESULT: FAIL at step '$1'"; exit 2; }

step "python matrix pin"
PY=python3.11
command -v "$PY" >/dev/null 2>&1 || PY=python3
"$PY" -c 'import sys; assert sys.version_info[:2] == (3, 11), sys.version' \
  || fail "python matrix pin (need 3.11, ruling Q1)"

step "bench init (frappe version-15)"
rm -rf "$BENCH_DIR"   # clean slate: a reused bench is not a proof
bench init --skip-redis-config-generation --frappe-branch version-15 \
  --python "$PY" "$BENCH_DIR" || fail "bench init"
cd "$BENCH_DIR" || fail "enter bench dir"
bench set-config -g db_host db
bench set-config -g redis_cache "redis://redis-cache:6379"
bench set-config -g redis_queue "redis://redis-queue:6379"
bench set-config -g redis_socketio "redis://redis-queue:6379"

step "new site"
bench new-site "$SITE" --admin-password oc-test-admin \
  --db-root-password oc-test-root --mariadb-user-host-login-scope='%' \
  || bench new-site "$SITE" --admin-password oc-test-admin \
       --db-root-password oc-test-root --no-mariadb-socket \
  || fail "new site"

step "get + install open_chart (standalone; no Medx app anywhere)"
# Manual app registration instead of `bench get-app`: get-app git-clones,
# and the mounted repo may be a git worktree whose .git pointer cannot
# resolve inside the container. Copy (read-only mount stays untouchable),
# strip git state, pip-install editable, register in apps.txt.
cp -a "$APP_SRC" ./apps/open_chart || fail "copy app"
rm -rf ./apps/open_chart/.git
./env/bin/pip install --quiet -e ./apps/open_chart || fail "pip install app"
grep -qx "open_chart" ./sites/apps.txt 2>/dev/null || echo "open_chart" >> ./sites/apps.txt
bench --site "$SITE" install-app open_chart || fail "install-app"

step "migrate"
bench --site "$SITE" migrate || fail "migrate"

step "app test suite"
bench --site "$SITE" run-tests --app open_chart || fail "run-tests"

echo
echo "OC-DOCKER-RESULT: PASS (install, migrate, tests on the pinned matrix)"

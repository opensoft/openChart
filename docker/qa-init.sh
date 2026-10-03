#!/usr/bin/env bash

set -euo pipefail

SITE=qa.localhost
APP_SRC=/workspace/open_chart
DATA_DIR=/home/frappe/qa-data
SITES_DIR=/home/frappe/qa-sites
BENCH_DIR="$DATA_DIR/frappe-bench"
BENCH_READY_MARKER="$DATA_DIR/.qa-bench-ready"
CREDENTIALS_FILE="$SITES_DIR/qa-credentials.env"
SITE_READY_MARKER="$SITES_DIR/$SITE/.qa-site-ready"
QA_ADMIN_PASSWORD=${QA_ADMIN_PASSWORD:-oc-qa-admin}
QA_DB_ROOT_PASSWORD=${QA_DB_ROOT_PASSWORD:-oc-qa-root}
CURRENT_STEP=startup

step() {
  CURRENT_STEP=$1
  echo
  echo "== OC-QA-STEP: $1"
}

fail() {
  echo "OC-QA-RESULT: FAIL at step '$CURRENT_STEP'" >&2
  exit 2
}

trap fail ERR

step "python matrix pin"
PY=python3.11
command -v "$PY" >/dev/null 2>&1 || PY=python3
"$PY" -c 'import sys; assert sys.version_info[:2] == (3, 11), sys.version'
# pin pyenv shims to the SAME interpreter family the venv uses: the image
# carries multiple versions and a bare shim resolved 3.14 once, whose env
# lacks working yarn -> bench init died halfway (observed 2026-08-26)
PY311_ROOT="$(dirname "$(dirname "$(command -v "$PY")")")"
case "$PY311_ROOT" in
  *".pyenv/versions/"*) export PYENV_VERSION="$(basename "$PY311_ROOT")" ;;
esac
export PATH="$PY311_ROOT:$PATH"

step "Node and Yarn from the bench image"
# The root entrypoint changes user with a preserved environment. Restore
# the image's declared Node toolchain when that environment lost its PATH.
if ! command -v yarn >/dev/null 2>&1 && [ -s "$HOME/.nvm/nvm.sh" ]; then
  set +u
  . "$HOME/.nvm/nvm.sh"
  nvm use --silent default
  set -u
fi
command -v node >/dev/null
command -v yarn >/dev/null

step "bench init (frappe version-15)"
if [ ! -x "$BENCH_DIR/env/bin/python" ] || [ ! -f "$BENCH_READY_MARKER" ]; then
  rm -rf "$BENCH_DIR"
  bench init --skip-redis-config-generation --frappe-branch version-15 \
    --python "$PY" "$BENCH_DIR"
  touch "$BENCH_READY_MARKER"
else
  echo "OC-QA-SKIP: bench already initialized"
fi

cd "$BENCH_DIR"

step "persistent sites volume wiring"
if [ ! -L "$BENCH_DIR/sites" ]; then
  # Recover an interrupted removal/link step using the retained volume.
  if [ -d "$BENCH_DIR/sites" ]; then
    cp -a "$BENCH_DIR/sites/." "$SITES_DIR/"
  fi
  rm -rf "$BENCH_DIR/sites"
  ln -s "$SITES_DIR" "$BENCH_DIR/sites"
else
  echo "OC-QA-SKIP: persistent sites volume already wired"
fi
touch "$SITES_DIR/apps.txt"
grep -qx "frappe" "$SITES_DIR/apps.txt" || echo "frappe" >> "$SITES_DIR/apps.txt"
if [ ! -e /home/frappe/logs ]; then
  ln -s "$BENCH_DIR/logs" /home/frappe/logs
fi
# frappe/logger.py derives log homes from RAW CWD, not the sites_path kwarg:
#   bench-level  -> dirname(cwd)/logs        (heredoc cwd=$BENCH_DIR -> $DATA_DIR/logs;
#                                             gunicorn cwd=$SITES_DIR    -> /home/frappe/logs)
#   site-level   -> cwd/$SITE/logs
# ALL candidates must exist or get_logger dies on database.log (observed twice).
mkdir -p "$BENCH_DIR/logs" "$DATA_DIR/logs" \
         "$SITES_DIR/$SITE/logs" "$BENCH_DIR/$SITE/logs"

step "external service wiring"
bench set-config -g db_host db
bench set-config -g redis_cache "redis://redis-cache:6379"
bench set-config -g redis_queue "redis://redis-queue:6379"
bench set-config -g redis_socketio "redis://redis-queue:6379"

step "site qa.localhost"
if [ -d "$SITES_DIR/$SITE" ] && [ ! -f "$SITES_DIR/$SITE/site_config.json" ]; then
  echo "OC-QA-RECOVER: removing site directory left incomplete by an interrupted new-site"
  rm -rf "$SITES_DIR/$SITE"
  rm -f "$CREDENTIALS_FILE"
fi
if [ -f "$SITES_DIR/$SITE/site_config.json" ] && [ ! -f "$SITE_READY_MARKER" ]; then
  echo "OC-QA-RECOVER: removing incomplete site from an interrupted initialization"
  bench drop-site "$SITE" --force --no-backup --db-root-password "$QA_DB_ROOT_PASSWORD" || true
  rm -rf "$SITES_DIR/$SITE"
  rm -f "$CREDENTIALS_FILE"
fi
if [ ! -f "$SITES_DIR/$SITE/site_config.json" ]; then
  bench new-site "$SITE" --admin-password "$QA_ADMIN_PASSWORD" \
    --db-root-password "$QA_DB_ROOT_PASSWORD" --mariadb-user-host-login-scope='%' \
    || bench new-site "$SITE" --admin-password "$QA_ADMIN_PASSWORD" \
         --db-root-password "$QA_DB_ROOT_PASSWORD" --no-mariadb-socket
  touch "$SITE_READY_MARKER"
else
  echo "OC-QA-SKIP: site already exists"
fi
bench use "$SITE"

step "open_chart from the mounted checkout (worktree-safe copy)"
# The bench runs THIS copy, not the mounted read-only repo: refresh it every
# boot so post-install source edits reach the site (stale-copy trap observed
# 2026-08-26: a code fix never reached gunicorn because the copy was skipped).
rm -rf ./apps/open_chart
cp -a "$APP_SRC" ./apps/open_chart
rm -rf ./apps/open_chart/.git
./env/bin/pip install --quiet -e ./apps/open_chart
[ -s ./sites/apps.txt ] && [ -n "$(tail -c1 ./sites/apps.txt)" ] && echo >> ./sites/apps.txt
grep -qx "open_chart" ./sites/apps.txt 2>/dev/null || echo "open_chart" >> ./sites/apps.txt
if bench --site "$SITE" list-apps | awk '{print $1}' | grep -qx "open_chart"; then
  echo "OC-QA-SKIP: open_chart already installed"
else
  bench --site "$SITE" install-app open_chart
fi

step "migrate"
bench --site "$SITE" migrate

step "qa-runner System Manager API credentials"
export CREDENTIALS_FILE QA_ADMIN_PASSWORD SITE
umask 077
./env/bin/python <<'PY'
import os
import shlex
import tempfile

import frappe

site = os.environ["SITE"]
credentials_file = os.environ["CREDENTIALS_FILE"]
api_user = "qa-runner@qa.localhost"

frappe.init(site=site, sites_path="/home/frappe/qa-sites")
frappe.connect()
try:
    if frappe.db.exists("User", api_user):
        user = frappe.get_doc("User", api_user)
    else:
        user = frappe.get_doc(
            {
                "doctype": "User",
                "email": api_user,
                "username": "qa-runner",
                "first_name": "QA",
                "last_name": "Runner",
                "enabled": 1,
                "user_type": "System User",
                "send_welcome_email": 0,
            }
        )
        user.flags.no_welcome_mail = True
        user.insert(ignore_permissions=True)

    if not any(row.role == "System Manager" for row in user.roles):
        user.append("roles", {"role": "System Manager"})

    if not os.path.exists(credentials_file):
        api_key = user.api_key or frappe.generate_hash(length=15)
        api_secret = frappe.generate_hash(length=15)
        user.api_key = api_key
        user.api_secret = api_secret
        user.save(ignore_permissions=True)
        frappe.db.commit()
        values = {
            "QA_SITE": site,
            "QA_ADMIN_USER": "Administrator",
            "QA_ADMIN_PASSWORD": os.environ["QA_ADMIN_PASSWORD"],
            "QA_API_USER": api_user,
            "QA_API_USERNAME": "qa-runner",
            "QA_API_KEY": api_key,
            "QA_API_SECRET": api_secret,
        }
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=os.path.dirname(credentials_file), prefix=".qa-credentials-", delete=False) as handle:
            temporary_credentials = handle.name
            for key, value in values.items():
                handle.write(f"{key}={shlex.quote(value)}\n")
        os.chmod(temporary_credentials, 0o600)
        os.replace(temporary_credentials, credentials_file)
        print(f"OC-QA-CREDENTIALS: wrote {credentials_file}")
    else:
        user.save(ignore_permissions=True)
        frappe.db.commit()
        print(f"OC-QA-SKIP: credentials already exist at {credentials_file}")
finally:
    frappe.destroy()
PY

echo
echo "OC-QA-RESULT: READY (open_chart, qa.localhost, persistent credentials)"

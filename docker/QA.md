# Persistent openChart QA site

This stack runs a synthetic, single-site Frappe QA deployment with only
`open_chart` installed. It uses the same pinned Frappe/Python/MariaDB/Redis
matrix as the throwaway Docker gate.

## Bring up

From the `openChart` repository root:

```bash
QA_ADMIN_PASSWORD=oc-qa-admin docker compose -f docker/qa-compose.yaml up -d
docker compose -f docker/qa-compose.yaml ps
```

The first start initializes the bench and can take several minutes. Compose
does not report the bench healthy until `http://qa.localhost:8001` answers the
Frappe ping endpoint. Open the site at that URL. The fixed host port is `8001`.

Bring-up order is automatic: MariaDB becomes healthy, both Redis services
start, then the bench initializes `qa.localhost`, installs `open_chart`, runs
migrations, bootstraps credentials, and finally starts Gunicorn.

The bench container runs Gunicorn on `0.0.0.0:8000` rather than `bench start`.
This is the simplest reliable long-lived HTTP process for the pinned Bench
image and avoids starting duplicate local Redis processes when this stack is
already wired to its Compose Redis services.

## Configuration and credentials

- `QA_ADMIN_PASSWORD` sets the Administrator password when the site is first
  created (default: `oc-qa-admin`). Changing it later does not rotate an
  existing site's password; wipe and recreate the stack to apply a new value.
- `QA_DB_ROOT_PASSWORD` sets the QA MariaDB root password (default:
  `oc-qa-root`). Use the same value whenever restarting an existing stack.
- The bootstrap creates the System User `qa-runner@qa.localhost`, with username
  `qa-runner`, and grants the `System Manager` role.
- API key, API secret, and the creation-time admin password are written with
  mode `0600` to `/home/frappe/qa-sites/qa-credentials.env` inside the bench
  container. That path is on the `qa-sites` named volume, so it survives
  container replacement and ordinary `docker compose down`/restart cycles.

Read the generated credentials without copying them into the repository:

```bash
docker compose -f docker/qa-compose.yaml exec bench \
  cat /home/frappe/qa-sites/qa-credentials.env
```

## Persistence and clean-slate reruns

An ordinary stop preserves the named database, bench-home, and sites volumes:

```bash
docker compose -f docker/qa-compose.yaml down
```

To destroy the site, database, installed apps, and generated credentials:

```bash
docker/qa-teardown.sh
```

The teardown uses `down --volumes`; this is intentionally destructive. The next
`up -d` performs a clean-slate initialization. Repeated starts without teardown
skip existing bench/site/app/user work and still run migrations.

## Boundary

This is a persistent **synthetic QA** deployment for real-system test runs. It
is not production, is not hardened for remote exposure, and must contain no
real PHI, patient uploads, production credentials, or decrypted clinical data.

## Live runner credentials

The runner accepts the generated `QA_API_KEY`, `QA_API_SECRET` and `QA_SITE`
variables as defaults. Explicit `OC_API_KEY`, `OC_API_SECRET` and `OC_SITE`
values take precedence. Load the protected credential file into the runner's
environment without shell tracing or printing it. The isolated `uv run` path
installs its declared PyYAML dependency; offline self-test opens no sockets.

Recovery records omit response headers; exact original historical bytes remain in the private cleanup checkpoint. Offline `uv run` needs PyYAML already cached when package-network access is unavailable.

New standalone runner records are diagnostic scenario evidence and set
`feeds_acceptance_report: false`. A Frappe version probe does not attest exact
deployed source commits or the internal adapter route. Verify those separately
from the deployed source/configuration before using a record for acceptance;
a scenario PASS alone does not supply that provenance. Endpoint URLs must not
contain userinfo, query tokens or fragments. Plain HTTP is limited to the
synthetic QA topology described here; production transport is outside this gate.

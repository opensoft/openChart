# openChart contributor commands (feature 001; brief D7).
#
# `validate` is bench-free and runs everywhere. `validate-docker` is the
# gated bench-dependent suite (site install, migrations, round trip) on
# the pinned matrix — Frappe v15 / Python 3.11 / MariaDB 10.6.

.PHONY: validate validate-docker

validate:
	python3 scripts/validate.py
	python3 scripts/harness.py

validate-docker:
	# teardown runs whether the suite passes or fails — a stale bench
	# container must never leak into the next run
	docker compose -f docker/compose.yaml up \
		--abort-on-container-exit --exit-code-from bench \
		bench db redis-cache redis-queue; \
	status=$$?; \
	docker compose -f docker/compose.yaml down -v; \
	exit $$status

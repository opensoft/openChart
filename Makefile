include shape/Makefile

.PHONY: validate-content validate-docker
validate: validate-content

validate-content:
	cd code && $(PYTHON) scripts/validate.py
	cd code && $(PYTHON) scripts/harness.py
	cd code && $(PYTHON) -m unittest discover -s tests -p "test_live_runner*.py"

validate-docker:
	cd code && docker compose -f docker/compose.yaml up --abort-on-container-exit --exit-code-from bench bench db redis-cache redis-queue; \
	status=$$?; docker compose -f docker/compose.yaml down -v; exit $$status

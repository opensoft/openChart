# Architect Brief — expanded-patient-intake

Binding input to plan/tasks. Deviations from §B are `[fable]`
escalations.

## A. Fixed context

- Change ratified 2026-08-05; eight requirements, twelve scenarios.
- openChart is ORIGINAL: no OpenEMR/Marley code, ever. Frappe-native.
- The MedxFactory program's surfaces are frozen, vendored by digest.
- G2 is dual-owner (p4+p6); no G2 evidence until p6 exists. p4's
  acceptance is standalone conformance.

## B. Architecture decisions (binding)

- **D1 — App shape**: Frappe app `open_chart`, module `Open Chart`;
  DocTypes prefixed `OC ` (OC Patient, OC Intake Submission,
  OC Medication Statement, …). Standard app layout (hooks.py,
  modules.txt, pyproject) authored as repo content.
- **D2 — Matrix pin** (Q1): Frappe v15 / Python 3.11 / MariaDB 10.6;
  frappe_docker images pinned in the compose file.
- **D3 — Statement identity** (Q3): eight independent statement
  DocTypes; every statement links its submission version; naming series
  SYN-safe in fixtures.
- **D4 — Lifecycle mechanics**: Intake Submission uses an explicit
  `lifecycle_state` field (draft → submitted → accepted → amended), NOT
  Frappe docstatus semantics alone — amendments create NEW documents
  with `predecessor` links (the program's succession shape), never
  Frappe's cancel-amend which renames.
- **D5 — Idempotency**: unique index on (patient, idempotency_key) for
  accepted submissions; replay returns the existing name.
- **D6 — Service boundary**: whitelisted API methods (versioned:
  `open_chart.api.v1.*`) + documented hooks; DocType permissions deny
  direct writes from other apps' roles; a compatibility test attempts a
  direct write and must be rejected.
- **D7 — Toolchain gate** (Q4): repo validator (`scripts/validate.py`
  in openChart) runs bench-free checks; `docker compose -f
  docker/compose.yaml` provides bench for gated checks; skip banner
  names exactly what was not proven.
- **D8 — Vendored contract** (Q5): `tests/fixtures/medx/` carries the
  golden intake layer + binding with provenance headers;
  `contracts/medx-pin.yaml` records bundle tag/digest + per-file
  digests; drift check every run.
- **D9 — Census as data**: the field census (golden intake fields →
  DocType fieldnames) lives in `contracts/intake-census.yaml`; the
  census check walks it — no field list in code.

## C. Delegation tiers

- **Sonnet**: DocType JSON files from the census + field lists; fixture
  variants; README entries.
- **Opus (manager)**: plan/tasks; app skeleton, API module, lifecycle +
  idempotency logic, validator + census/drift/negative harness, compose;
  commits.
- **Fable (architect)**: rulings, boundary calls, escalations,
  acceptance + change-side records.

## D. Session rules

Worktree-only on branch `001-expanded-patient-intake`;
explicit-pathspec commits; openChart's validator green before every
commit (and MedxFactory untouched — this feature never edits that
repo); mutation-probe every check; negative fixtures land with their
machinery; unfired audit at none; SYN- fixture discipline. Final
acceptance is `[fable]`.

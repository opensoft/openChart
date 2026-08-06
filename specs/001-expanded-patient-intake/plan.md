# Implementation Plan: Expanded Patient Intake Foundation

**Branch**: `001-expanded-patient-intake` | **Date**: 2026-08-05
**Spec**: spec.md (clarified) | **Brief**: architect-brief.md (D1–D9)

## Architecture

```text
open_chart/                    # the Frappe app (D1)
  hooks.py, modules.txt, patches.txt
  open_chart/doctype/<11 doctypes>/*.json  (+ .py controllers)
  api/v1.py                    # versioned whitelisted commands (D6)
contracts/
  medx-pin.yaml                # bundle tag/digest + vendored digests (D8)
  intake-census.yaml           # golden field -> DocType field map (D9)
tests/fixtures/medx/           # vendored golden intake + binding (D8)
tests/fixtures/failure/        # negative corpus
docker/compose.yaml            # frappe_docker, pinned (D2, D7)
scripts/validate.py            # bench-free repo validator (D7)
```

DocTypes (11): OC Patient, OC Patient External Identifier,
OC Intake Submission, OC Medication Statement, OC Supplement Statement,
OC Condition Statement, OC Allergy Statement, OC Observation Statement,
OC Symptom Statement, OC Goal Statement, OC Document Reference Statement.

Validator families: doctype-shape (JSON well-formed, OC-prefixed,
census-linked), census coverage (every golden field mapped), pin drift
(two computed values), fixture safety (SYN- discipline), negative
harness + ratchet + unfired audit (OC-* finding codes), api-shape
(whitelisted, versioned). Docker-gated: site install, migrate, live
golden round trip.

## Phases

1. Scaffold: app skeleton, validator, compose, vendoring, pin, census.
2. DocTypes: three sonnet batches (identity+submission; med/sup/cond/
   allergy; obs/symptom/goal/docref); shape+census checks.
3. API + lifecycle: v1 commands, idempotency, succession amendments,
   permissions/hooks; round-trip expectation fixture.
4. Corpus: negative fixtures, harness, audit, ratchet.
5. Polish: coverage, README, coherence; `[fable]` acceptance.

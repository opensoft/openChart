# Scenario Live Half — p4 (record, 2026-08-06)

Status: record
Named by: scenario report SYN-SCENARIO-REPORT-0001 (MedxFactory,
`add-a-drug-or-supplement-scenario`, archived 2026-08-06) — its claim
boundary lists the p4 live half as a follow-up in this repository.

## What this adds (additive only)

- `tests/fixtures/medx/scenario-intake-supplements-successor.yaml` —
  the scenario's updated supplement submission, vendored by digest
  (contracts/medx-pin.yaml row 6).
- `open_chart/tests/test_scenario_live_half.py` — the LIVE proof in the
  Docker gate: baseline submit → succession amend with the updated list
  → zero-loss read-back → prior auditable → the added melatonin stored
  exactly once as patient_reported.

No API change, no version change, no compatibility-declaration change:
the pin lattice above (p5/p6/proof vendored declarations) is untouched
by design.

## Verdict

Docker gate run 2026-08-06: **PASS — `Ran 8 tests ... OK`** under the
hardened verdict parsing (the seven feature-001 tests plus this live
half: baseline submit, succession amend with the updated list,
zero-loss read-back, prior auditable, melatonin stored exactly once).

## Real-system run (2026-08-26)

The tier-1 verdict above ran inside a throwaway bench that tears down
after every pass. The claim boundary's live half is now ALSO executed
against a persistent local QA deployment (`docker/qa-compose.yaml`, see
`docker/QA.md`): one long-lived Frappe v15 site serving this repository
at its pinned checkout, reached over HTTP with token auth as a System
Manager API user.

Runner: `scripts/run_p4_live.py` (stdlib-only; env contract
`OC_API_KEY`/`OC_API_SECRET`, optional `OC_BASE`/`OC_SITE`). It replays
the SAME assertion sequence as the bench test over the published HTTP
surface — `/api/method/open_chart.api.v1.{submit,amend,read_submission}`
plus DocType-REST creation of the fresh synthetic patient.

Run `p4-20260826T072634Z`: **PASS** (verdict computed all-or-nothing;
`evidence_provenance: live_qa`). Evidence:
`specs/001-expanded-patient-intake/live-evidence/p4-20260826T072634Z-3794684/evidence.yaml`;
raw request/response JSONL under gitignored `var/`.

Observed deployed identity (probe recorded in evidence): frappe
15.118.0, open_chart 0.1.0. Boundary unchanged: a PASS proves the named
scenario assertions on ONE local synthetic QA deployment over its real
HTTP/API/DocType path — it is not clinical validation, production
security/performance evidence, or proof of a remotely hosted posture.

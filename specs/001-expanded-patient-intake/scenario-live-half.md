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

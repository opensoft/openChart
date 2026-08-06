# Architect Acceptance — Feature 001 (T017)

Status: accepted 2026-08-05
Architect: Fable (this feature was planned and largely implemented by the
same session acting as manager/architect; sonnet subagents produced
T005-T007, T012, T015 — DISCLOSED per the program's producing-session
rule. The acceptance battery below was run fresh against the committed
tree, not against memory of writing it.)

## Scope accepted

`open_chart` 0.1.0 — the p4 expanded-patient-intake foundation: 11 OC
DocTypes, `open_chart.api.v1`, guarded write surface, vendored bundle
1.4.0 pins, census-driven fidelity checks, two-tier verification
(bench-free + Docker-gated).

## Acceptance battery (fresh runs, 2026-08-05/06)

1. **Full battery green**: `make validate` — validator + harness, 6
   negative fixtures with neutralization probes, planted safety, guard
   probe, 10/10 OC- codes observed firing.
2. **Harness meta-probe**: a wrong `expect` planted in the pin-drift
   fixture — harness FAILED naming the arm (exit 2), then restored to
   green. The harness is itself watched.
3. **Cross-repo pin verification** (architect-side; openChart cannot do
   this alone): all five `source_sha256` values in
   `contracts/medx-pin.yaml` recomputed against the MedxFactory golden
   tree — MATCH; `bundle_manifest_sha256` recomputed against
   `contracts/one-patient-bundle.yaml` (bundle 1.4.0) — MATCH.
4. **Pin tamper, record side**: a flipped hex digit in a vendored row's
   declared sha256 fired OC-PIN-DRIFT (the fixture corpus covers the
   file side; this covers the record side). Note: `source_sha256` and
   `bundle_manifest_sha256` are cross-repo provenance — unverifiable
   inside openChart by design, verified here architect-side (item 3).
5. **Import purity**: `open_chart.api.v1` and `open_chart.intake.guarded`
   import cleanly with frappe absent (verified `find_spec('frappe') is
   None` first); the whitelist decorator is inert bench-free.
6. **Flag-leak audit**: `oc_api_write`/`oc_api_amend` are set nowhere in
   app or script code outside `api/v1.py` (probe and bench-test setters
   excluded by inspection — probe sets them on a stub, test restores in
   `finally`).
7. **Docker-gated suite** (FR-001, SC-001) — five runs to an honest
   verdict, each failure named by the step machinery:
   - Run 1 FAILED at `get-app`: `bench get-app` git-clones, and a git
     worktree's .git pointer cannot resolve in-container. Fixed to
     manual registration (copy, strip git state, editable pip install,
     apps.txt, `install-app`).
   - Run 2 FAILED at `new site`: run 1's stopped containers persisted
     (make aborted before teardown) and the stale bench leaked in.
     Fixed: unconditional `compose down -v` + clean-slate `rm -rf` of
     the bench dir before init.
   - Run 3 FAILED at `install-app`: `sites/apps.txt` lacked a trailing
     newline, so the append fused `frappe`+`open_chart` into one
     unloadable module name. Fixed with a newline guard.
   - Run 4 "passed" FALSELY: `bench run-tests` exits ZERO when site
     testing is disabled — six green steps, zero tests executed. The
     zero-"test_" audit of the log caught it. Fixed: the gate now sets
     `allow_tests true` AND refuses any run whose output lacks
     `Ran N test` with N >= 1 — a suite that runs nothing proves
     nothing (the D9 silent-skip class, killed at the gate).
   - Run 5 ran all 7 tests and caught a REAL PRODUCT BUG: MariaDB
     returns Float fields as 20.0 where the payload submitted 20, so
     the stored-side content hash diverged from the incoming one and a
     byte-identical replay was refused as OC-IDEMPOTENCY-DIVERGED
     (`test_idempotent_replay_returns_existing`). The bench-free tier
     could never see this — it is exactly what the live tier exists
     for. Run 5 ALSO exposed a second gate defect: `bench run-tests`
     exited zero despite `FAILED (errors=1)`, so the gate printed PASS
     over a failing suite. Both fixed: `content_hash` now canonicalizes
     values with the same numeric tolerance the round-trip comparator
     uses (regression probe added to the harness), and the gate trusts
     the unittest verdict lines (`Ran N`, `OK`, no `FAILED`), never the
     launderable exit code.
   - **Run 6: PASS, honestly** — matrix pin, bench init (version-15),
     clean site, standalone install (no Medx app anywhere), migrate,
     and `Ran 7 tests ... OK` under the hardened verdict parsing. All
     seven bench tests green: golden round trip zero-loss, idempotent
     replay, divergent replay refused, succession amendment, direct
     write rejected, identity conflict to review, accepted immutable.

## Verdict

ACCEPTED. Six Docker runs to an honest green — four gate defects and
one product defect found and fixed by the battery itself, every
failure named by the machinery rather than discovered by luck. The
two-tier design earned its keep: the live tier caught what the
bench-free tier structurally cannot (storage-representation drift),
and the gate now refuses both silent-skip modes it was shown to have.

## Defects found and dispositioned during acceptance

- **D-ACC-1**: `docker/run-checks.sh` get-app path unusable from a git
  worktree mount (item 7). Fixed in this feature; the failure was named
  by the step machinery, which is the behavior FR-011 demands.
- **D-ACC-2** (probe bug, not product): the first record-side tamper
  probe hit `bundle_manifest_sha256` and expected a local check to fire;
  that field is cross-repo provenance and correctly has no local
  verifier. Probe corrected to target a vendored row.
- **D-ACC-3**: the gate accepted a zero-test `run-tests` exit (item 7,
  run 4). The FR-011 banner discipline was applied INSIDE the gate:
  the suite now proves tests ran, not merely that the runner exited
  zero — the five earlier green steps made the false PASS look
  complete.
- **D-ACC-4** (product): `content_hash` was representation-sensitive
  (int 20 vs stored Float 20.0), misjudging byte-identical replays as
  divergent (item 7, run 5). Fixed with canonical value forms matching
  the round-trip comparator's tolerance; harness regression probe
  asserts int/float row sets hash identically while a real content
  change still moves the hash.
- **D-ACC-5** (gate): `bench run-tests` exit code is launderable — it
  exited zero over `FAILED (errors=1)`. The gate now parses the
  unittest verdict lines and refuses FAILED / missing OK.

## Claim boundary

Standalone conformance only. G2 (intake fidelity) is co-owned with
p6-one-patient-intake-experience (unbuilt); no G2 gate evidence is
claimed or fabricated. The program's acceptance report continues to
carry G2 `not_run` until both owners exist (ruling Q0).

## Change-side closure

- Change tasks 1.1-1.3, 2.1-2.2, 3.1-3.2 ticked with this record.
- Published consumer surface: `contracts/p4-compatibility-declaration.yaml`.
- Coverage: `specs/001-expanded-patient-intake/requirement-coverage.md`.

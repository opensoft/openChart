# Clarify Questions — 001-expanded-patient-intake

Session 2026-08-05. The design's three open questions plus two the
handoff surfaced. Per the program's delegation model the ARCHITECT
answers as recorded rulings; each stands unless the operator overrules.

## Q1 — Frappe/Python support matrix
**ANSWER: Frappe v15 + Python 3.11 + MariaDB 10.6** (the v15 defaults),
one matrix in v1, exercised via official frappe_docker images. Widening
is a reviewed change. | Alternatives: v14 (aging), multi-matrix (doubles
CI before one matrix is proven).

## Q2 — Synchronous terminology in v1
**ANSWER: none.** Reported wording and supplied codes stored verbatim;
enrichment is a later change, mirroring the program's terminology
deferral. | Alternatives: sync RxNorm lookup (network dependency inside
the intake write path — refused).

## Q3 — Child tables vs independent DocTypes
**ANSWER: independent DocTypes for all eight statement families**;
child tables only for true composition (ingredient lists). The design's
own rationale: reconciliation, amendment, and per-family permissions
need stable identities. | Alternatives: child tables under submission
(no stable identity), one polymorphic statement DocType (permissions and
queries degrade).

## Q4 — Toolchain without a local bench
**ANSWER: app tree + DocType JSON authored as repo content, validated by
openChart's own validator with no bench; bench-dependent checks
(install, migrate, live round trip) run in the official frappe_docker
compose, Docker-gated with a loud skip banner** (the MedxFactory D9
pattern). | Alternatives: require bench locally (blocks every
contributor), skip runtime checks (an app nobody installed is not
proven).

## Q5 — How the MedxFactory contract is consumed
**ANSWER: vendored fixtures with provenance + digest pins.** The golden
intake layer and the openchart binding are copied into openChart test
fixtures with headers naming their source and the bundle digest; a
drift check recomputes vendored digests against the pin record every
run. openChart never reads a MedxFactory path at runtime.
| Alternatives: submodule dependency (couples repos), path reference
(breaks standalone).

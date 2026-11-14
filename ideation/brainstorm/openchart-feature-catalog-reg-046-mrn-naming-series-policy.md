# MRN Naming Series Policy — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs facility-scoped medical record number issuance, format, reservation, retirement, and collision handling through configurable naming series.
Topics: openchart-feature-catalog, registration, frappe, mrn-policy
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-046 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Preallocated emergency ranges** — Reserve auditable offline-safe number blocks with reconciliation controls.

## Focus

Define how openChart issues local MRNs without conflating them with immutable patient identity.

## Behavior

- Each facility configures an active prefix, sequence, padding, checksum option, and uniqueness scope.
- MRNs issue only through guarded patient acceptance, never by direct user-edited naming fields.
- Reserved or skipped numbers remain auditable and are not silently recycled.
- A collision stops patient creation and alerts an administrator without exposing another patient's details.
- Retired MRNs resolve to the current patient identity but cannot be assigned again unless explicit policy permits.
- Policy changes affect future issuance and preserve the series used for every existing MRN.

## Frappe realization

- **DocTypes:** `OC MRN Policy` and `OC MRN Assignment` with facility, naming_series, scope, status, issued_on, retired_on, and patient.
- **Workflow:** Policy Draft → Approved → Active → Retired; assignment Active → Retired or Entered in Error.
- **Roles/permissions:** `OC Registration Administrator` proposes; `System Manager` approves policy; clerks receive issued MRNs read-only.
- **API/surfaces:** `open_chart.api.v1.registration.issue_mrn`; naming-series hook under API guard, policy workspace, and collision report.

## Boundaries

Owns: local MRN issuance and lifecycle policy. Consumes: facility configuration and accepted patient request. Emits: authority-qualified MRN assignment. Does not own: external MRNs or global patient identity.

## Open questions

- Should bench sites have globally disjoint prefixes to simplify future exchange and consolidation?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)

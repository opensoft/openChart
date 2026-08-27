# Patient Pharmacy Preference — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records patient-selected primary and contextual pharmacy preferences while requiring confirmation at each prescription decision.
Topics: openchart-feature-catalog, eprescribing, frappe, pharmacy-preference
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-003 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Contextual routing prompt** — Preferences could distinguish routine, specialty, controlled-substance, and mail-order destinations for faster confirmation.

## Focus

This feature isolates a patient's pharmacy preference as revocable guidance, not routing authority. Every outbound prescription still requires the ordering user to confirm the destination.

## Behavior

- Patients, proxies within scope, or authorized staff may record one primary and multiple purpose-specific pharmacy preferences.
- Each preference stores source, effective dates, verification status, and the endpoint snapshot shown at selection.
- The prescription composer suggests applicable preferences but never sends without explicit confirmation.
- Users may override a preference for one order and record an optional reason without changing the saved preference.
- Inactive or unreachable pharmacies trigger reselection and preserve the prior preference history.
- Portal changes enter a reviewable pending state when proxy authority or patient identity is uncertain.

## Frappe realization

- **DocTypes:** `OC Patient Pharmacy Preference` links `OC Patient` to `OC Pharmacy Endpoint` with purpose, rank, source, consent/proxy, and effective dates.
- **Workflow:** Proposed → Verified → Active → Superseded/Revoked preserves preference lineage.
- **Roles/API:** Patients use an authenticated portal page; staff use guarded `open_chart.api.v1.pharmacies.set_preference` with User Permissions and proxy checks.
- **Surfaces:** The patient sidebar and prescription composer display effective preferences, endpoint freshness, and one-order override controls.

## Boundaries

Owns: preference history and confirmation context. Consumes: patient/proxy authority and pharmacy directory entries. Emits: suggested destination references. Does not own: pharmacy availability, benefit routing, or automatic transmission.

## Open questions

- Which preference changes require staff verification before becoming active?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Pharmacy Directory Search](openchart-feature-catalog-phr-002-pharmacy-directory-search.md)

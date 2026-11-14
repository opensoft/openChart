# DEA Schedule Display — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Displays the effective controlled-substance schedule and source terminology wherever a medication is selected, reviewed, signed, or audited.
Topics: openchart-feature-catalog, eprescribing, frappe, dea-schedule
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-016 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Jurisdiction overlay** — The display could show state-specific treatment alongside the federal category with effective dates.

## Focus

This feature isolates schedule visibility and provenance. The displayed category informs downstream controls but does not itself determine clinical appropriateness.

## Behavior

- Medication search results show controlled status and schedule before selection.
- The composer, signing review, printed report, and audit view display the effective schedule consistently.
- The label includes authority, terminology release, effective date, and any jurisdictional overlay.
- Missing, conflicting, or expired schedule data blocks EPCS classification from silently defaulting to non-controlled.
- Authorized terminology stewards resolve conflicts through versioned updates, never edits to signed snapshots.
- Prescriptions retain the exact schedule determination used at signing even after terminology changes.

## Frappe realization

- **DocTypes:** `OC Drug Schedule Classification` links medication codes to authority, schedule, jurisdiction, and effective dates.
- **Hooks:** Medication selection fetches display values; server validation snapshots the effective classification on `OC Prescription Line`.
- **Permissions:** Terminology stewards publish classifications; clinical roles receive read-only access.
- **Surfaces:** Search formatter, form indicator, print context, and classification-conflict Query Report make schedule data visible.

## Boundaries

Owns: effective schedule representation and snapshots. Consumes: authoritative terminology and jurisdiction context. Emits: visible classification for credential, EPCS, and guardrail checks. Does not own: legal interpretation or prescribing decisions.

## Open questions

- Which authoritative sources and update cadence are required for jurisdiction overlays?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Controlled-Substance Quantity Guardrails](openchart-feature-catalog-phr-015-controlled-substance-quantity-guardrails.md)

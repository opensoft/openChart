# Patient Wristband Printing Integration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces encounter-scoped patient wristbands from a verified identity snapshot with printer, stock, barcode, replacement, and destruction evidence.
Topics: openchart-feature-catalog, documents, frappe, wristband-printing
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-028 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Bedside activation scan** — Require scanning the new band and encounter token before marking it active.

## Focus

This feature isolates identity-safe wristband production and replacement; it does not define registration identity policy.

## Behavior

- A Registration or Nursing user requests a band from an active encounter after confirming patient identity.
- The request snapshots approved display name, identifiers, date-of-birth presentation, alerts, encounter, facility, and barcode payload.
- A preview enforces minimum font, contrast, stock fit, and prohibited sensitive-field rules.
- Initial print remains Pending Activation until staff confirms successful output and, when configured, scans it.
- Replacement requires reason such as damaged, lost, incorrect, or changed identity and inactivates the prior band explicitly.
- Wrong-printer, wrong-stock, duplicate-active-band, and stale-encounter checks block release.
- Every print, activation, replacement, and documented destruction is audited.

## Frappe realization

- **DocTypes:** `OC Patient Wristband` (patient, encounter, identity_snapshot JSON, barcode_value, state, replaces) and `OC Wristband Print Attempt`.
- **Workflow:** Requested → Printed → Active, with Failed, Replaced, Inactive, and Destroyed states.
- **Roles/permissions:** Registration User requests; Nurse activates/replaces; Wristband Administrator controls templates and printers; identity fields use role-aware permlevels.
- **Print formats/API:** Dedicated Jinja/ZPL Print Format and guarded `open_chart.api.v1.documents.print_wristband`; printer adapter reports status idempotently.
- **Surfaces:** Identity confirmation dialog, scan-to-activate client behavior, active-band indicator, and replacement audit report.

## Boundaries

Owns: wristband snapshot, barcode output, print/activation state, replacement lineage, and destruction evidence. Consumes: verified patient and encounter identity. Emits: active physical identifier event. Does not own: master demographics, bedside scanning workflows, or admission/discharge authority.

## Open questions

- Which identity fields and alert symbols are permitted on visible bands by care setting?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Clinical Label Printing Engine](openchart-feature-catalog-dms-027-clinical-label-printing-engine.md)

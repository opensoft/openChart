# Preferred Pharmacy Selection — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets patients rank pharmacies by purpose and validity so prescribing workflows can present an informed destination choice.
Topics: openchart-feature-catalog, registration, frappe, preferred-pharmacy
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-015 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Specialty-purpose ranking** — Maintain separate preferences for retail, mail-order, and specialty dispensing.

## Focus

Capture pharmacy preference as patient context rather than an automatic prescribing instruction.

## Behavior

- Staff or patients search an approved pharmacy directory and select one or more entries.
- Each selection records purpose, rank, effective dates, and patient-stated notes.
- Closed, inactive, or unmatched pharmacies trigger a warning and require reselection or documented free-text fallback.
- Only one first-ranked pharmacy per purpose is active at a time.
- Prescribers see the preference but must confirm the destination for each prescription.
- Preference history remains attributable to the patient, proxy, or staff member who changed it.

## Frappe realization

- **DocTypes:** `OC Patient Pharmacy Preference` linked to `OC Patient` and `OC Pharmacy Directory Entry`, with purpose, rank, validity, and source.
- **Workflow:** Proposed → Active → Superseded or Inactive.
- **Roles/permissions:** `OC Registration Clerk` and `OC Patient Portal User` propose; `OC Clinical User` reads; directory maintenance is separate.
- **API/surfaces:** `open_chart.api.v1.registration.set_pharmacy_preferences`; registration selector, portal settings, and patient header shortcut.

## Boundaries

Owns: patient pharmacy preferences. Consumes: pharmacy directory entries. Emits: ranked choices with provenance. Does not own: prescription routing, formulary, or dispensing status.

## Open questions

- Should inactive directory entries remain visible in preference history by default?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)

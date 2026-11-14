# Pharmacy Directory Search — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets users find connected pharmacies by name, location, services, and operating status before routing a prescription.
Topics: openchart-feature-catalog, eprescribing, frappe, pharmacy-directory
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-002 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Access-aware pharmacy ranking** — Search could optionally rank open, nearby, delivery-capable, or language-compatible pharmacies without silently selecting one.

## Focus

This feature isolates human-directed discovery of a valid pharmacy endpoint. Search results make network reachability and freshness visible instead of treating a name match as routable.

## Behavior

- Prescribers and authorized staff search by pharmacy name, city, postal code, phone, or map radius.
- Filters distinguish retail, mail-order, specialty, compounding, long-term-care, and controlled-substance capabilities.
- Results show address, distance, hours, phone, network identifier, service flags, and directory freshness.
- Closed, inactive, duplicate, or non-connected entries are visibly labeled and cannot be chosen for electronic routing.
- The user explicitly selects a destination; geographic ranking never commits a choice automatically.
- Directory outages retain recent cached results with a stale warning and offer print or fax fallback where permitted.

## Frappe realization

- **DocTypes:** `OC Pharmacy Endpoint` stores identifiers, geocoordinates, services, active dates, and source version; `OC Pharmacy Directory Sync` records imports and errors.
- **Permissions/API:** Clinical roles receive read access; directory stewards maintain records through guarded sync APIs under `open_chart.api.v1.pharmacies`.
- **Surfaces:** A Link-field query, map/list dialog, global-search integration, and Query Report for stale or duplicate endpoints support selection and stewardship.
- **Hooks:** Scheduled background sync jobs normalize identifiers and publish cache refresh events without overwriting locally documented preferences.

## Boundaries

Owns: searchable pharmacy endpoint metadata and selection evidence. Consumes: network directories and geocoding results. Emits: selected endpoint references and freshness warnings. Does not own: patient preference, prescription content, or external directory authority.

## Open questions

- What directory freshness threshold should block electronic selection rather than merely warn?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Patient Pharmacy Preference](openchart-feature-catalog-phr-003-patient-pharmacy-preference.md)

# Race and Ethnicity Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures patient self-identified race and ethnicity as multi-select, versioned, standard-aware facts with declined and free-text support.
Topics: openchart-feature-catalog, registration, frappe, race-ethnicity
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-033 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Terminology mapping profiles** — Map detailed self-identification to reporting categories without replacing the original answer.

## Focus

Collect race and ethnicity respectfully for defined purposes while preserving patient wording and multiplicity.

## Behavior

- Patients may select multiple race and ethnicity concepts, provide detail, choose unknown, or decline.
- The interface states why the information is requested and does not force a single category.
- Staff must record that an answer was patient-reported, proxy-reported, imported, or unknown.
- Free-text detail is retained alongside coded values and is not silently recoded.
- Reporting mappings are derived and versioned separately from the authoritative response.
- Changes supersede prior responses and remain visible only to appropriately permitted users.

## Frappe realization

- **DocTypes:** `OC Race Ethnicity Response` and child `OC Demographic Concept Selection` with code system, code, display, detail, source, and validity.
- **Workflow:** Draft → Accepted → Superseded or Withdrawn.
- **Roles/permissions:** `OC Registration Clerk` captures; `OC Patient Portal User` proposes; reporting roles receive de-identified or permission-limited views.
- **API/surfaces:** `open_chart.api.v1.registration.update_race_ethnicity`; inclusive multi-select form, portal intake, and mapping-aware Query Report.

## Boundaries

Owns: self-identified race and ethnicity responses. Consumes: configured terminology and stated answers. Emits: coded and original responses with provenance. Does not own: clinical inference or population-health policy.

## Open questions

- Which terminology set and local extensions should be the initial supported profile?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)

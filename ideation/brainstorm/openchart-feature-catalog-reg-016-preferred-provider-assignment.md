# Preferred Provider Assignment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records a patient's preferred providers by role and effective period without conflating preference with care-team responsibility.
Topics: openchart-feature-catalog, registration, frappe, preferred-provider
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-016 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Availability-aware suggestions** — Show scheduling options for preferred providers while preserving patient choice.

## Focus

Maintain patient-stated provider preferences separately from operational assignment and clinical accountability.

## Behavior

- Registration staff record preferred primary, specialty, or other provider roles.
- Each preference identifies internal practitioner or external provider, rank, reason, and effective dates.
- Inactive providers remain in history but cannot be newly selected.
- Multiple preferences are allowed when their roles or ranks differ.
- Scheduling surfaces may suggest the preference but cannot silently reassign an appointment.
- The patient is informed when a preference cannot be honored and the exception reason is recorded.

## Frappe realization

- **DocTypes:** `OC Patient Provider Preference` with Dynamic Link provider, role, rank, reason, validity, and exception_note.
- **Workflow:** Proposed → Active → Superseded or Unavailable.
- **Roles/permissions:** `OC Registration Clerk` records; `OC Patient Portal User` proposes; `OC Scheduling User` reads purpose-limited values.
- **API/surfaces:** `open_chart.api.v1.registration.set_provider_preferences`; patient panel, intake field, and scheduling integration method.

## Boundaries

Owns: patient-stated provider preferences. Consumes: provider directory status. Emits: ranked provider choices. Does not own: appointment booking, panel attribution, or care-team accountability.

## Open questions

- Should a clinic require a reason when staff override an available preferred provider?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)

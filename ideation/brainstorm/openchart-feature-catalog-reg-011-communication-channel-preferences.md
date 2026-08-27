# Communication Channel Preferences — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures purpose-specific channel, timing, language, and content preferences so communications honor patient choices.
Topics: openchart-feature-catalog, registration, frappe, communication-preferences
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-011 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Preference conflict preview** — Warn staff when a planned communication lacks an allowed endpoint.

## Focus

Model communication choices separately from the existence of contact endpoints and legal consent.

## Behavior

- Patients choose preferred and prohibited channels for reminders, results notices, administrative messages, and emergencies.
- Preferences can specify language, quiet hours, voicemail permission, and whether detailed content is allowed.
- Emergency exceptions are recorded explicitly rather than inferred from routine preferences.
- A preference change records actor, source, effective time, and affected purposes.
- Conflicting preferences resolve to the most restrictive applicable instruction and show why.
- Callers and messaging integrations receive a purpose-filtered view, not unrestricted contact data.

## Frappe realization

- **DocTypes:** `OC Communication Preference` linked to patient and optional contact point, with purpose, channel, allowed, language, quiet hours, and content_level.
- **Workflow:** Proposed → Active → Superseded; portal proposals may require verification before activation.
- **Roles/permissions:** `OC Registration Clerk` records; `OC Patient Portal User` manages own preferences; `OC Privacy Officer` audits overrides.
- **API/surfaces:** `open_chart.api.v1.registration.resolve_communication_preference`; portal settings, patient banner, and communication audit Query Report.

## Boundaries

Owns: patient communication preferences. Consumes: active contact points and stated choices. Emits: purpose-scoped communication instructions. Does not own: message content, delivery, or statutory notice rules.

## Open questions

- Which urgent clinical communications may override quiet hours, and who records that policy?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)

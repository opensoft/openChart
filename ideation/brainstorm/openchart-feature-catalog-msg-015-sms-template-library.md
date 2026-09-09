# SMS Template Library — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides versioned SMS templates with validated variables, language variants, and channel-safe length previews.
Topics: openchart-feature-catalog, messaging-tasks, frappe, sms-templates
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-015 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Template outcome comparison** — Compare approved variants by delivery and patient action without exposing message content in analytics.

## Focus

This feature isolates reusable, governed SMS composition rather than campaign selection or message transport.

## Behavior

- Template authors define purpose, language, body, approved variables, sensitivity class, and effective version.
- Preview requires synthetic or masked values and shows segment count, encoding, and estimated truncation risk.
- Rendering rejects missing, unknown, or unauthorized variables rather than sending placeholders.
- Patient-derived values are formatted by locale and minimum-necessary policy.
- Approval separates author and reviewer for clinical, legal, or high-volume templates.
- Active versions are immutable; edits create a succeeding draft with lineage.
- Retired templates cannot start new sends but remain renderable for historical evidence.
- Free-text additions may be prohibited or constrained by purpose.

## Frappe realization

- **DocTypes:** `OC SMS Template`, child `OC Template Variable`, and `OC SMS Template Version` store purpose, locale, content, sensitivity, status, and lineage.
- **Workflow:** Draft → Clinical/Compliance Review → Active → Retired with role-separated approvals.
- **Rendering:** server-side Jinja uses an allowlisted context adapter; validation blocks arbitrary attribute access and unknown variables.
- **Integration:** rendered content passes to Frappe SMS settings only through `open_chart.api.v1.messaging.render_sms_template` and send orchestration.
- **Surfaces:** template Desk workspace, masked preview, version diff, and usage Query Report.

## Boundaries

Owns: SMS template content, variables, approval, and rendering. Consumes: approved patient context and locale. Emits: rendered channel-safe text and version evidence. Does not own: recipients, consent, campaigns, or gateway delivery.

## Open questions

- Which clinical template classes require patient-literacy or legal review before activation?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Broadcast Campaigns to Patient Cohorts](openchart-feature-catalog-msg-016-broadcast-campaigns-to-patient-cohorts.md)

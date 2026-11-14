# Notification Template Editor — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Authors versioned email, SMS, and push templates with channel previews, approved variables, and publication workflow.
Topics: openchart-feature-catalog, platform, frappe, notification-templates
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-014 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Multilingual template variants** — Govern translated channel content against one semantic template version.

## Focus

This feature isolates low-code message composition while keeping delivery consent, event selection, and gateway routing separate.

## Behavior

- Communications administrators choose a purpose, channel, locale, subject, body, sender profile, and approved variable set.
- The editor validates required variables, channel length, unsafe markup, unsupported links, and minimum-necessary disclosure.
- Preview renders synthetic values for email, SMS segments, and push truncation without using patient data.
- Templates move through Draft, Review, Published, Paused, Retired, and Superseded states.
- Published versions are immutable for past Notification Log evidence; edits create a successor.
- Rendering failure blocks delivery and records the missing variable without exposing the recipient payload.

## Frappe realization

- **DocTypes:** `OC Notification Template` stores purpose, channel, locale, version, body, variable dictionary Link, and state.
- **Surface:** a Desk editor integrates Frappe Notification and Email Template conventions with Jinja linting and synthetic preview.
- **Permissions:** Communications Designer authors; Communications Approver publishes; delivery services read published versions only.
- **API:** `open_chart.api.v1.platform.render_notification` requires template version and validated context, then writes Notification Log evidence.

## Boundaries

Owns: versioned channel content and render validation. Consumes: approved variables, branding, locale, and sender profile. Emits: rendered message content and version identity. Does not own: consent, recipient selection, or gateway delivery.

## Open questions

- Which health-related content classes are prohibited on SMS and push channels?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Template Variable Dictionary](openchart-feature-catalog-plt-037-template-variable-dictionary.md) · [Communication Gateway Failover](openchart-feature-catalog-plt-036-communication-gateway-failover.md)

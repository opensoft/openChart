# In-app Release Tour Publisher — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Builds version-targeted, role-specific in-app tours that introduce changed workflows without blocking urgent work.
Topics: openchart-feature-catalog, platform, frappe, release-tours
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-048 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Training completion handoff** — Route complex releases from a short tour into a tracked learning module.

## Focus

This feature isolates interactive product-change orientation tied to installed releases and applicable roles.

## Behavior

- Release educators define a target app version, roles, routes, ordered steps, anchors, media, fallback text, and availability window.
- Preview validates that anchors exist in representative layouts and that every step is keyboard and screen-reader reachable.
- Tours move through Draft, Review, Published, Paused, Retired, and Superseded states.
- Eligible users may start, skip, resume, dismiss, or replay a tour unless a separately governed acknowledgment is required.
- Missing anchors skip safely with fallback content and report the broken step to the owner.
- Completion telemetry is optional, privacy-minimized, and never records patient or document context.

## Frappe realization

- **DocTypes:** `OC Release Tour` and child `OC Tour Step` store version, roles, route, anchor, content, order, locale, and state.
- **Client scripts:** Desk boot data selects eligible published tours; an accessible overlay renders steps and local completion state.
- **Permissions:** Release Educator authors; Release Manager publishes; users control optional participation.
- **Integration:** installed release metadata and Feature Flags gate exposure; fixtures carry published tours between environments.

## Boundaries

Owns: interactive release orientation and optional completion evidence. Consumes: installed version, role, UI anchors, locale, and feature exposure. Emits: tours and privacy-safe progress. Does not own: release notes, formal training, or workflow authorization.

## Open questions

- Which workflow changes warrant required acknowledgment rather than an optional tour?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Help Widget Content Management](openchart-feature-catalog-plt-047-help-widget-content-management.md) · [In-app Patch Notes](openchart-feature-catalog-plt-029-in-app-patch-notes.md)

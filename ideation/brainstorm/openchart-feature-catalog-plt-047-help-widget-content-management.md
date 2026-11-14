# Help Widget Content Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes contextual, role-aware help content inside approved screens with versioning, localization, and feedback routing.
Topics: openchart-feature-catalog, platform, frappe, contextual-help
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-047 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Task-linked help escalation** — Convert negative feedback into a support case with page context but no clinical payload.

## Focus

This feature isolates end-user guidance embedded in the product while keeping normative policy and clinical education in their owning systems.

## Behavior

- Content authors target a route, DocType, field, workflow state, role, locale, and site scope with concise help content.
- Content supports approved text, images, links, and short walkthrough steps with accessibility metadata.
- Articles move through Draft, Review, Published, Retired, and Superseded states.
- Preview simulates target context and rejects inaccessible links, unsafe markup, unsupported variables, and role-invisible references.
- Users can search, dismiss, rate usefulness, and report outdated content without exposing current record values.
- Missing localized content falls back through an explicit locale chain and displays the language used.

## Frappe realization

- **DocTypes:** `OC Contextual Help Article` stores target selectors, roles, locale, content, assets, version, and state; feedback records rating and context key.
- **Surface:** a Desk and portal help widget loads matching published content from boot/page context.
- **Permissions:** Help Author writes drafts; Help Approver publishes; feedback is owner-visible and privacy-minimized.
- **API:** cached whitelisted reads return only content authorized for the current role, locale, route, and site.

## Boundaries

Owns: contextual product guidance, publication, and feedback. Consumes: UI context, roles, locale, and approved assets. Emits: help panels and content feedback. Does not own: clinical education, legal policy, or support case resolution.

## Open questions

- Which help content must be centrally controlled versus locally adapted by a clinic?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [In-app Release Tour Publisher](openchart-feature-catalog-plt-048-in-app-release-tour-publisher.md)

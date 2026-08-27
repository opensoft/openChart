# Clinical Language Pack Governance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Versions each interface language pack with per-release clinical validation evidence so coverage claims remain honest and deployable.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, language-pack-governance
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-001 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Coverage risk dashboard** — Rank untranslated or stale strings by clinical surface and patient-safety impact.

## Focus

This feature isolates release-specific language-pack approval, distinguishing technical availability from clinically reviewed coverage.

## Behavior

- Localization managers import or update a pack against an exact openChart release and Frappe message catalog digest.
- Clinical reviewers see untranslated, fuzzy, changed, and safety-critical strings grouped by workflow.
- A pack moves through Draft, Linguistic Review, Clinical Review, Validated, Rejected, and Superseded states.
- Only Validated packs may be advertised as clinically supported; incomplete packs remain installable only when site policy allows and carry a visible coverage warning.
- Release changes invalidate affected approvals without discarding prior reviewer identity, comments, or evidence.
- Missing strings fall back to the configured source language and record a gap without exposing message arguments or patient data.
- Publication requires separate localization and clinical-review authority for safety-critical terminology.

## Frappe realization

- **DocTypes:** `OC Language Pack Release` stores locale, app release, catalog digest, coverage, fallback locale, and validation state; `OC Translation Review Item` stores source key, translation, criticality, reviewer, and disposition.
- **Translation system:** Frappe translation CSV/message catalogs remain the runtime source; fixtures and a patch bind approved catalog digests to application releases.
- **Workflow and roles:** A Frappe Workflow enforces the listed states for Localization Manager, Clinical Translation Reviewer, and Release Manager roles at permlevels 0-2.
- **Automation and reports:** `validate` rejects duplicate keys and invalid placeholders; an RQ comparison job and Script Report produce release deltas and coverage evidence.

## Boundaries

Owns: pack versions, review state, coverage claims, and approval evidence. Consumes: Frappe message catalogs, application releases, and reviewer authority. Emits: validated locale manifests and gap reports. Does not own: source clinical meaning or browser translation.

## Open questions

- Which string classes require two independent clinical reviewers before validation?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [In-context Translation Editor](openchart-feature-catalog-iax-002-in-context-translation-editor.md)

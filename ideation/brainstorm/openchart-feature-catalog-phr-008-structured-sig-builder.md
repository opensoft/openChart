# Structured SIG Builder — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Builds patient directions from coded dose, route, frequency, timing, duration, indication, and as-needed limits while retaining the structured components.
Topics: openchart-feature-catalog, eprescribing, frappe, structured-sig
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-008 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Multilingual patient directions** — Governed phrase packs could render reviewed translations from the same structured SIG components.

## Focus

This feature isolates construction of understandable medication directions from coded components. Generated text remains previewable and editable only through its components unless the prescriber explicitly chooses free-form fallback.

## Behavior

- The prescriber selects dose amount/unit, dosage form, route, frequency, timing, duration, indication, and PRN conditions.
- Required and mutually dependent fields change according to dosage form and frequency pattern.
- The builder renders a human-readable SIG and a machine-readable component set side by side.
- Ambiguous combinations, unsafe abbreviations, missing PRN maxima, and contradictory timing are blocked or clearly warned.
- The prescriber previews the exact patient-facing directions before signing.
- Saved favorites populate editable components and never bypass clinical validation or signature.

## Frappe realization

- **DocTypes:** Child `OC Prescription SIG` stores coded components, source terminology versions, rendered text, and rendering version under `OC Prescription Line`.
- **Client/server validation:** Client scripts drive conditional fields and preview; server `validate` reproduces all rules before submission.
- **Configuration:** Versioned `OC SIG Phrase Template` and `OC Dose Frequency` DocTypes govern rendering and organization-approved abbreviations.
- **API/surfaces:** `open_chart.api.v1.prescriptions.render_sig` returns deterministic previews for Desk and authorized external clients.

## Boundaries

Owns: structured direction components and deterministic rendering. Consumes: medication form, terminology, and site phrase policy. Emits: coded SIG and patient-facing text. Does not own: clinical dose selection or autonomous prescribing.

## Open questions

- Which structured SIG model should be canonical when network and jurisdiction profiles differ?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Free-Form SIG Fallback](openchart-feature-catalog-phr-009-free-form-sig-fallback.md)

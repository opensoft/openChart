# Patient Preference Matching — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Ranks valid openings against explicit patient preferences without converting soft preferences into hidden access barriers.
Topics: openchart-feature-catalog, scheduling, frappe, preference-matching
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-048 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Preference trade-off controls** — Let patients rank which preferences may be relaxed first.

## Focus

This feature isolates preference capture and explainable ranking after hard booking constraints pass.

## Behavior

- Patients or staff record preferred days, times, providers, locations, modality, language support, and travel limits.
- Each preference is marked required only when backed by an eligible hard requirement; otherwise it remains soft.
- Candidate slots receive a match explanation showing satisfied and unsatisfied preferences.
- Users can relax selected preferences and rerun search without re-entering the request.
- Stale preferences are reconfirmed before use in recurring or waitlist matching.
- Ranking never uses protected or inferred attributes that the patient did not authorize for this purpose.

## Frappe realization

- **DocTypes:** `OC Scheduling Preference` with patient, preference_type, value JSON, strength, valid_until, source, and consent reference.
- **API:** slot-search ranking consumes normalized preferences and returns explanation codes; hard constraints remain separate evaluators.
- **Surface:** portal and Desk forms capture preferences; role and owner permissions protect patient-specific values.

## Boundaries

Owns: scheduling preference representation and ranking contribution. Consumes: explicit patient choices and valid candidates. Emits: explainable ranked results. Does not own: hard eligibility rules.

## Open questions

- Which preferences should persist across unrelated appointment requests?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Open-slot Search](openchart-feature-catalog-sch-006-open-slot-search.md)

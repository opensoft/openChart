# Outside Imaging Patient Matching — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Reconciles patient identity on outside imaging against openChart records through explainable candidates and human approval before archive association.
Topics: openchart-feature-catalog, imaging, frappe, imaging-patient-matching
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-019 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Issuer-aware identifier map** — Maintain trusted external MRN namespaces for repeat referring organizations.

## Focus

This feature isolates the safety-critical identity decision between imported DICOM demographics and the local patient.

## Behavior

- The reviewer sees detected name, birth date, sex, identifiers, issuer, source facility, and study dates beside local candidates.
- Candidate scores disclose matching and conflicting fields but never approve a match automatically.
- Exact external identifiers are trusted only within configured issuer namespaces and active mappings.
- The reviewer may confirm, reject, request more evidence, or route a likely duplicate patient for separate resolution.
- Approved remapping records original and assigned identity, actor, reason, and downstream archive transaction.
- A wrong-match correction suspends affected references and follows a governed reversal and re-association process.

## Frappe realization

- **DocTypes:** `OC Imaging Identity Match` with candidate child rows, evidence, conflicts, decision, external namespace, and correction lineage.
- **Workflow:** Candidate Review → Evidence Needed → Matched or Rejected → Correction Review.
- **Roles/permissions:** `OC Patient Identity Reviewer` decides; import staff propose; clinical users cannot bypass unresolved matching.
- **API/surfaces:** guarded matching method; side-by-side Desk page; audit feed records every candidate and decision without exposing bulk pixels.

## Boundaries

Owns: import-specific identity reconciliation and decision evidence. Consumes: DICOM demographics and patient registry data. Emits: approved patient association. Does not own: general patient merge or image transfer.

## Open questions

- What evidence threshold requires a second reviewer before remapping an outside study?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)

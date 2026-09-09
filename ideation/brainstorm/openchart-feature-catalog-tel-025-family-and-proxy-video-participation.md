# Family And Proxy Video Participation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets family members, caregivers, and legal proxies join a patient's virtual visit under verified, encounter-specific authority.
Topics: openchart-feature-catalog, telehealth, frappe, proxy-video-participation
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-025 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Granular segment access** — Let a clinician exclude a participant from a private portion while preserving attendance history.

## Focus

This feature isolates nonclinical guest and proxy participation for one patient's care, distinct from multi-patient group sessions.

## Behavior

- The patient or authorized staff nominates a participant with relationship, purpose, contact method, and requested scope.
- Proxy authority is validated against effective records; ordinary family guests require patient agreement for this encounter.
- Each participant receives an individual expiring invitation and completes role-appropriate identity verification.
- Staff admit, remove, or temporarily exclude participants independently and record who authorized each presence interval.
- The clinician can request private time with the patient without ending the room or erasing prior attendance.
- Revoked authority, withdrawn agreement, or room closure invalidates that participant's grants immediately.

## Frappe realization

- **DocTypes:** `OC Visit Participant Authorization` links patient, virtual visit, person or guest identity, relationship, authority source, scope, decision, and effective interval.
- **API/workflow:** Proposed, Verified, Invited, Waiting, Admitted, Excluded, Revoked, and Completed transitions use participant-scoped grants and append-only presence events.
- **Permissions:** Patient may invite within policy, Proxy acts only within validated scope, Clinician controls room presence, and Identity Reviewer resolves authority conflicts.

## Boundaries

Owns: encounter-specific guest authority and presence. Consumes: patient agreement and proxy records. Emits: scoped invitation and attendance evidence. Does not own: longitudinal guardianship or proxy determination.

## Open questions

- How should adolescent confidentiality and multiple conflicting proxy claims affect virtual-room controls?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)

# Join Identity Verification — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Verifies that a person joining virtual care matches an authorized patient, proxy, clinician, or invited participant.
Topics: openchart-feature-catalog, telehealth, frappe, join-identity-verification
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-006 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Risk-adaptive verification** — Require stronger proof for sensitive services while preserving an assisted exception path.

## Focus

This feature isolates identity proof at session arrival without redefining the longitudinal patient identity record.

## Behavior

- Portal-authenticated patients confirm configured demographic factors before a join grant is issued.
- Guest participants verify a single-use invitation plus the minimum approved challenge for their role.
- Clinicians and staff must have active authenticated sessions and room-scoped assignment.
- Failed challenges are rate-limited, audited, and phrased without revealing whether protected identity data matched.
- A mismatch routes to staff review; it never creates a new patient or silently changes demographics.
- Emergency or accessibility exceptions require an authorized staff attestation and remain visible in the encounter audit.

## Frappe realization

- **DocTypes:** `OC Join Verification` records subject type, method, outcome, attempt count, policy version, reviewer, and redacted evidence reference.
- **API/security:** `open_chart.api.v1.telehealth.verify_joiner` uses one-time challenges, CSRF protection, rate limits, and no raw challenge answers in logs.
- **Permissions/workflow:** Patient sees only their outcome; Telehealth Identity Reviewer resolves Needs Review cases; Audit Reviewer has read-only permlevel access to provenance.

## Boundaries

Owns: encounter-specific join verification. Consumes: authenticated identity, invitation, and policy. Emits: verified participant authority or review case. Does not own: master patient matching.

## Open questions

- Which verification factors are proportionate for routine, behavioral-health, minor, and urgent virtual visits?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)

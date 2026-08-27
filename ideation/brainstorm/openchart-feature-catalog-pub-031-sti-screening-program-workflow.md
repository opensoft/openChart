# STI Screening Program Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates consent-sensitive sexually transmitted infection screening offers, specimen progress, result review, and confidential follow-up.
Topics: openchart-feature-catalog, public-health, frappe, sti-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-031 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Confidential self-collection intake** — Support permissioned instructions and specimen handoff without exposing program enrollment broadly.

## Focus

A privacy-aware screening episode that coordinates existing orders and results without duplicating them.

## Behavior

- Clinicians record screening offer, indication, consent basis, tests selected, specimen plan, and confidentiality restrictions.
- The episode links orders, specimens, results, review, treatment/referral disposition, and follow-up tasks.
- Declined testing records bounded scope and does not imply refusal of future offers.
- Sensitive communications use approved channels and suppress ordinary proxy access where legally required.
- Positive or indeterminate results route accountable review under configured reporting policy.
- Users without elevated purpose-based permission see only a restricted-record indicator.

## Frappe realization

- **DocTypes:** Add `OC STI Screening Episode` with order/result Links, consent, confidentiality profile, disposition, and follow-up rows.
- **Workflow:** Use offered, consented, ordered, awaiting-result, clinician-review, follow-up, complete, and declined states.
- **Permissions:** Apply permlevel 2 sensitive fields and roles `OC Sexual Health Clinician` and `OC Public Health Reporter` with audited purpose checks.
- **Surfaces:** Provide a restricted worklist, safe Notifications, and patient instructions with proxy-aware portal controls.

## Boundaries

Owns: screening episode coordination and confidential disposition. Consumes: consent, orders, specimens, results, and reporting rules. Emits: review and follow-up tasks. Does not own: laboratory results, diagnosis, treatment, or contact investigation.

## Open questions

- How should jurisdiction-specific minor consent alter portal and proxy visibility?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)

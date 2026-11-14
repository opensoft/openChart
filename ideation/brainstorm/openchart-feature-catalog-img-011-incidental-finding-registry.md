# Incidental Finding Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Registers actionable incidental imaging findings with category, recommendation, responsible party, provenance, and due-date basis.
Topics: openchart-feature-catalog, imaging, frappe, incidental-findings
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-011 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Registry cohort review** — Let authorized teams review open findings by category and due window.

## Focus

This feature isolates the durable registry record that turns a report recommendation into accountable follow-up demand.

## Behavior

- A radiologist or authorized reviewer registers an incidental finding from an accepted report.
- The entry records finding text, anatomical site, coded category, recommendation, interval, due-date basis, and source report span.
- The responsible clinician and patient communication status are explicit and may not default silently when routing is ambiguous.
- Duplicate candidates are shown for human reconciliation rather than merged automatically.
- Changes to recommendation or responsibility preserve prior accepted values and reason.
- Registry access is filtered by patient, facility, care relationship, and role.

## Frappe realization

- **DocTypes:** `OC Incidental Finding` with source report Link, text offsets, category, due rule, owner, communication state, and succession Link.
- **Workflow:** Proposed → Verified → Open → Monitoring → Resolved or Exception Closed.
- **Roles/permissions:** radiologists propose; designated clinicians accept responsibility; follow-up coordinators manage queues; audit roles read history.
- **Hooks/API/surfaces:** `on_submit` creates follow-up demand; guarded methods handle assignment; Query Reports show due and unassigned findings.

## Boundaries

Owns: incidental-finding registry identity, recommendation, and responsibility state. Consumes: accepted report and patient routing data. Emits: follow-up obligations. Does not own: diagnosis, scheduling, or completion evidence.

## Open questions

- Which findings require patient-facing disclosure tracking within the registry itself?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)

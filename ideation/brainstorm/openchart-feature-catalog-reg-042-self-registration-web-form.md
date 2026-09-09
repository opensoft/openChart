# Self Registration Web Form — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets patients or authorized representatives submit resumable registration data online for staff review before chart changes occur.
Topics: openchart-feature-catalog, registration, frappe, self-registration
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-042 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Invitation-bound prefill** — Prefill known facts through short-lived tokens while requiring confirmation of every displayed value.

## Focus

Provide an accessible remote intake channel whose submissions remain untrusted until identity and authority review.

## Behavior

- A patient or representative opens an invitation-bound or policy-approved public registration session.
- The form supports save-and-resume, responsive layout, keyboard use, plain language, and configured translations.
- Representative submissions require relationship and authority assertions distinct from patient answers.
- Uploaded documents use private files, malware checks, size limits, and explicit purpose labels.
- Submission creates an intake for matching and staff review; it never silently creates or overwrites a patient.
- Expired tokens, duplicate submissions, and interrupted uploads return safe recovery instructions without exposing chart existence.

## Frappe realization

- **DocTypes:** `OC Self Registration Session` linked to `OC Registration Intake`, with token digest, actor_type, expiry, progress, and submission provenance.
- **Workflow:** Invited → In Progress → Submitted → Matched, Needs Review, Accepted, or Rejected.
- **Roles/permissions:** Guest has token-scoped methods only; `OC Patient Portal User` may authenticate; `OC Registration Clerk` reviews submissions.
- **API/surfaces:** `www/registration` portal page and guarded `open_chart.api.v1.registration.save_self_registration`; realtime-safe status page.

## Boundaries

Owns: remote registration session and submitted intake payload. Consumes: invitation, policy, and user-entered data. Emits: reviewable intake. Does not own: identity verification or patient acceptance.

## Open questions

- Which functions require authenticated portal access versus a short-lived invitation token?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)

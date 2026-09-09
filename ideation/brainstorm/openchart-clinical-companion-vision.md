# openChart Clinical Companion Vision — Brainstorm

Status: brainstorm
Kind: reference
Summary: openChart is the clinical side of a practice — the working tool of the physician, human or credentialed AI — organized around eight moments of use from pre-visit preparation through an always-on in-visit companion to patient-side adherence, with billing, scheduling, and HR explicitly excluded to openPractice.
Topics: openchart-clinical-companion, product-vision, ai-practitioner, openxwallet, clinical-workflow
Repository context: openChart — Frappe v15 native EMR; product-owner vision stated 2026-08-25, framing the shipped intake foundation and the existing feature-list and feature-catalog packets against a companion-for-physicians product thesis
Captured: 2026-08-25

## Framing

openChart is the clinical side of a medical practice's work of helping
patients. Everything it does serves the moment a physician is thinking
about a patient — before the visit, during it, between visits, in
consultation with colleagues, and under later scrutiny. The note, the
reasoning behind it, and the provenance of both are the product. The
physician using it may be a human doctor or an AI doctor, and the system
is designed for both from the ground up rather than retrofitting one onto
the other. Every AI practitioner carries an openXwallet credential
validating that AI's expertise and abilities, and that credential — not
species — confers clinical authority inside the record.

## Actors

- **Human physician** — the primary and most demanding user. Prepares,
  examines, documents, reasons, prescribes, signs; judged later on what
  the record shows.
- **Credentialed AI physician** — a first-class practitioner, not a tool
  and not a service account. Holds an openXwallet credential attesting
  expertise, scope, and current standing; acts under that credential;
  carries attributable accountability.
- **The patient** — reached through companion apps that carry the
  treatment plan outward and return adherence, symptom, and device data
  inward. A participant in the loop, not merely a record subject.
- **Other consulted doctors** — specialists, second opinions, case
  conferences, tumor boards. They enter as collaborators on a specific
  patient question, not as generic portal users.
- **Legal counsel as an audience of the record** — never an operator, but
  a foreseeable reader. Plaintiff and defense counsel both read what was
  written, when, by whom, and what was known at the time.

## Moments of use

The vision resolves into eight pillars. They are numbered so that review
and gap analysis can address them individually.

### P1 — Pre-visit preparation

The doctor getting ready to meet the patient. Everything relevant to this
encounter, assembled and cited before the door opens: recent trajectory,
open problems, outstanding results, what happened elsewhere since the
last visit. The measure is that the physician walks in already oriented
rather than reading the chart in front of the patient.

### P2 — Always-on in-visit companion

The system runs during the office visit and the physical exam,
continuously documenting and assisting the human or AI doctor in real
time. Not a recorder that is switched on and later processed, but a
present participant: it hears the encounter, surfaces what is relevant to
what is being said, drafts as the visit proceeds, and hands the physician
a near-complete record at the moment the visit ends.

### P3 — Case collaboration

Preparing for and supporting meetings with other doctors about the
patient. Assembling the case — imaging, timeline, prior workup, the
actual question being asked — so that a conference or second opinion
starts from a shared, complete picture, and so that the decisions,
dissents, and rationale from that meeting land back in the patient's
record as first-class clinical content.

### P4 — Medico-legal support

Preparing for and supporting meetings with lawyers about malpractice
issues. Reconstructing what the chart showed on a given date, who knew
what and when, how a result was acknowledged and acted on, and what
reasoning stood behind a decision — assembled as sealed, verifiable
evidence rather than reconstructed by hand from screenshots years later.

### P5 — Patient diagnostic research

Researching the diagnosis for this specific patient. Holding competing
hypotheses with their uncertainty, comparing which investigation
discriminates between them, reaching to literature, guidelines, drug
references, and evidence from similar patients — and doing all of it
attached to the patient's record rather than in a browser tab beside it.

### P6 — Treatment plan research and creation

Researching therapeutic options for this patient and authoring the plan
that follows. Comparing options against this patient's constraints,
committing to a versioned plan with measurable goals, and tracking
response against it so the plan is a living object rather than a document
written once.

### P7 — AI practitioner support and openXwallet credential validation

Supporting AI physicians as practitioners: presenting and verifying the
openXwallet credential, enforcing scope of practice per credential,
binding actions to a model version, establishing supervision and
co-signature topology, attributing liability when a credentialed AI errs.
Patients are told when an AI is treating them, and consent to it.

### P8 — Patient-side app integration

openChart integrates with patient-side apps that help the patient adhere
to the treatment plan and that return patient data to openChart. The
plan pushes outward as actionable tasks and medication schedules;
adherence, symptoms, device readings, and deviations flow back and reach
the physician as a signal, closing the loop that P6 opens.

## Boundary

openChart is explicitly not for billing, HR, or scheduling. The repo
README already assigns billing to the sibling product openPractice; this
vision extends the same exclusion to scheduling and workforce management.
openPractice owns practice operations — access, money, staffing, supply.

The boundary is a seam, not a wall: features on the far side become
integration points rather than openChart features. openChart needs to
know that an appointment exists, that an order carries a coverage
constraint, that a practitioner is licensed — it does not own booking
rules, claim scrubbing, or shift rosters. Clinical residue misfiled on
the operations side (a care pathway expressed as a booking sequence, say)
belongs back on the clinical side; the machinery around it does not.

## Relationship to the existing foundation

The shipped intake foundation — eleven OC DocTypes, a versioned `api.v1`,
succession-based amendments, guarded controllers, synthetic-fixture
discipline — is already a provenance-first substrate, and this vision
builds on it rather than replacing it. Amendment succession, identity
conflict routing, and controller guards are exactly the primitives a
medico-legal and AI-accountability posture needs.

The existing ideation packets — the twelve-domain feature list and the
1,115-feature catalog across twenty-two domains — cover much of that
substrate and cover it well. But both were researched against incumbent
EMRs (OpenEMR as baseline, Epic/Oracle/MEDITECH as the ceiling), and they
inherit an assisted-human worldview from those sources: a human
clinician, in a conventional practice, assisted by AI that must never
act. That is the right default for a product benchmarked on incumbents
and the wrong default for this vision. The companion review records where
the substrate transfers intact, where it must be reframed, and where it
is simply absent.

## Key tensions

- **Human gates versus credentialed AI practitioners.** The catalog
  encodes `human` as the structural gate predicate — most sharply in
  aic-036, where the AI service role holds zero submit permission on
  clinical DocTypes and a service-account identity cannot satisfy a human
  gate. The vision needs the predicate to be *accountable credentialed
  practitioner*, with humanity as one way to qualify rather than the only
  one. Restating the gate this way preserves every governance property the
  gate exists to protect; it is a reframing, not a demolition.
- **Always-on capture versus consent and retention.** A companion that
  runs continuously through an exam records more than an episodic
  recorder does, and minimum-necessary retention pulls hard against it.
  Consent state must be live and revocable mid-encounter, and retention
  policy configurable per jurisdiction, before continuous capture ships.
- **Openness of credential verification.** A credential is worth only
  what its verification is worth. Publishing the presentation,
  verification, and revocation contract openly makes it checkable by
  anyone — including a court — but exposes the trust model to attack and
  forces a public answer on who may issue and who may revoke.
- **Longitudinal AI reasoning versus per-invocation artifacts.** An AI
  practitioner following a patient across encounters needs continuous
  reasoning state; every AI artifact in the catalog today is
  per-invocation and expiring. The record model has no place to put a
  practitioner's evolving understanding of a patient.

## Relationships

Reviewed against the existing corpus in
[Clinical Companion Feature Review](openchart-clinical-companion-feature-review.md);
the owner's issue-by-issue direction is recorded in
[Clinical Companion Phase Decisions](openchart-clinical-companion-phase-decisions.md).
Prior packets this vision reframes:
[openChart Feature List Overview](openchart-feature-list-overview.md) and
[openChart Feature Catalog Overview](openchart-feature-catalog-overview.md).

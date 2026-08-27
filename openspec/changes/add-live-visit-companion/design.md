## Context

openChart's one promoted capability (`expanded-patient-intake`) persists
patient-reported statements behind the single guarded write surface
`open_chart.api.v1`, whose controller guards in `open_chart/intake/guarded.py`
reject any write that does not carry the API flag, and whose endpoints refuse a
call without subject, tenant, purpose and role context. That surface is the
constraint this design works within: whatever runtime holds the live session,
every durable chart mutation still lands through the one audited path.

Everything openChart owns for the encounter today is capture-then-queue.
doc-039 describes ambient visit capture as Recording → Processing → Draft Ready;
aic-048 states inference latency and fallback policy in terms of asynchronous
jobs; aic-003 gates capture on consent obtained for a capture *episode*;
mob-020 frames consented mobile capture episodically. aic-004's review queue,
aic-005's sentence-level transcript provenance, tel-002's video console and
car-054's conference record are the adjacent pieces. Frappe's async model is rq
workers — correct for post-visit jobs, and not a runtime for a persistent
low-latency in-room session.

The catalog-wide human gate is the other constraint. Roughly 575 brainstorm
entries forbid autonomous clinical action, with aic-036 encoding *human* as the
predicate. A companion that signs its own record, and an AI practitioner whose
call-out carries order intent, both need that predicate restated as *accountable
credentialed practitioner*. This design does not own that restatement: the
sibling change `add-practitioner-identity` does, and it is **proposed, not
promoted**. Decision 12 states the posture.

Six design questions were dispositioned `accepted` by owner ruling on
2026-08-26 (disposition round 1). They are settled inputs here, recorded as
Decisions 2 through 7, not reopened.

## Goals / Non-Goals

**Goals:**

- Make the encounter a resident, witnessed, verbal event with a session object
  that outlives interruptions rather than a recording that outlives the visit.
- Get low-latency streaming into the room without opening a second write path
  into the chart.
- Produce two independently signed records of the same visit and make their
  divergence visible without letting a witness halt care.
- Give clinical reasoning a home during the visit — a live working differential
  distinct from the problem list — that orders and symptoms are evaluated
  against as they are heard.
- Capture, contemporaneously, whether companion output was surfaced and whether
  it was relied on, before any legal question about the unspoken layer is
  settled.
- Keep both practitioner kinds on identical encounter terms, with private
  surfaces that are role-resolved rather than device-typed.

**Non-Goals:**

- Deciding retention, patient visibility or discoverability of the unspoken
  layer. That belongs to the named legal-research work item; this design fixes
  the class and the tags, not the policy.
- Issuing any credential, granting any clinical authority, or flipping any
  production authority. Those are `practitioner-identity`'s, and this change
  consumes them.
- The legal matter workspace and counsel collaboration, which belong to
  openPractice's legal portion.
- External-organization participant identity and consult-package exchange.
- Knowledge-source selection for differential reasoning (literature, guidelines,
  drug reference, similar-patient cohorts) — a later phase.
- Rewriting `expanded-patient-intake` requirements, or deleting any superseded
  catalog entry.

## Decisions

### 1. The session is the object; devices are hosts of it

A **Witnessed Encounter Session** opens *before* the encounter, survives
interruption, and is rejoined by **resume, not restart**. Its lifecycle states
are open, active, interrupted, resumed and closed; a host dropping off does not
end the session, and a host rejoining attaches to the same session identity
rather than creating a sibling.

Two hosts are concurrent by design — a dedicated room-resident device and the
practitioner's mobile — and neither is the other's fallback. Modelling the
session as the durable object and the devices as attachments is what makes
"the network dropped mid-visit" a host event rather than a record event, and it
is the only shape under which two capture streams can be reconciled into one
transcript with per-segment host provenance.

Pre-visit prep runbook state hands off at open: the session receives the
runbook's canonical item set **and its check-off provenance events**, which are
first-class evidence of preparation, not UI state. The runbook is its own
surface preceding the visit, and the session is not its next screen — the
hand-off is an explicit transfer with its own provenance, so the two surfaces
can evolve independently and preparation evidence survives even if the visit
never opens.

Alternative considered and rejected: treating the room device as primary with
the mobile as a fallback recorder. It makes the mobile's capture second-class
evidence, and it gives the private-surface problem (Decision 10) no clean
answer, since the practitioner's private channel would ride on the fallback.

### 2. A dedicated streaming session service beside bench, writing only through guarded surfaces (Q5, accepted)

The live session runtime is a **dedicated service beside bench**, with its own
process lifecycle, holding the **live session, the transcript stream and the
inference path**. It writes into openChart **only through guarded
`api.v1`-style surfaces**. rq stays in place for post-visit jobs unchanged —
draft generation, review-queue work, reconciliation-item processing.

Two alternatives were rejected. Putting the session inside the Frappe worker
model means fighting rq's job semantics for something that is not a job: a job
has a payload, a result and an end, and a session has a lifetime, listeners and
mid-flight state. Putting chart writes inside the streaming service means a
second, unguarded write path into the record — untenable for content that will
be signed and attested, and directly contrary to the guard that already makes
every non-API write fail loudly.

Separating **runtime** from **write surface** is the load-bearing move. In-flight
transcript, in-flight differential state and prompt delivery live in the service
at streaming latency; every durable chart mutation — transcript segment commit,
differential version, staged order, attestation, session event — crosses into
openChart through the guarded surface, carrying the same subject, tenant,
purpose and role context every other write carries, plus the acting
practitioner's exercise context once `practitioner-identity` lands.

Consequence: the service is not trusted. The guarded surface validates what it
submits exactly as it validates any client, and a compromised or buggy session
service can lose a stream but cannot forge a record. The cost is a latency
boundary at every commit and two systems that can disagree about live state; the
session's committed state is authoritative and the service's in-flight state is
not.

### 3. Divergence files; it never blocks signing (Q1, accepted)

Dual attestation makes practitioner-versus-companion divergence detectable for
the first time, and the answer to what divergence *does* is: **both records file
independently, and the discrepancy is emitted as a flagged reconciliation item**
reviewed after the visit by the practitioner, with escalation paths defined by
the practice rather than by the companion.

Blocking would convert a witness into an authority over the clinician at the
moment care is being delivered — clinically unsafe, and outside anything the
companion is credentialed for. Filing both records plus a durable, timestamped,
attributable discrepancy flag preserves the full evidentiary value of two-witness
attestation without giving the companion a veto. The reconciliation item is the
accountability mechanism: it is a work item with a state, not a log line, so an
unreviewed disagreement is visible rather than buried.

The companion's record is therefore never merged into the practitioner's. Two
records of one visit stand side by side; agreement is corroboration and
disagreement is evidence, and silently reconciling them would destroy both.

### 4. The unspoken layer is in the record, in a distinct provenance class, tagged from day one (Q2, accepted)

Each actor's unspoken portion — the practitioner's private reasoning, an AI
practitioner's reasoning trace, the companion's extended analysis — is **part of
the record**, held in a **provenance class distinct from the witnessed spoken
layer**. Retention and patient visibility are **deferred to the named
legal-research work item**. **Exposure** and **reliance** tags are captured on
every element **from day one**, regardless of where that research lands.

The asymmetry is the whole argument. Building the unspoken layer outside the
record and moving it in later is not possible; building it inside with a
distinct class and changing the retention policy later is trivially possible.
And the tags are the irreversible part: whether a companion output was
*surfaced* (exposure) and whether the practitioner *acted on it* (reliance) can
only be recorded contemporaneously — a failure-to-heed claim targets precisely
the surfaced-but-ignored case, which is unreconstructable after the fact.
Deciding the legal class later is cheap; reconstructing the tags later is
impossible.

The class is a first-class attribute of every record element, not a flag on a
side table, so an evidence export can select the witnessed layer alone, the
witnessed layer plus relied-upon companion output, or everything, without
re-deriving anything.

### 5. Private-channel prompts share the unspoken class (Q6, accepted)

Prompts delivered to a practitioner on their private surface are **part of the
record, in the same class as the unspoken portions, carrying the same exposure
and reliance tags**.

A prompt that changes what the practitioner says or orders has influenced care.
Treating the private channel as a separate unrecorded lane would open a
deliberate gap in the evidentiary substrate exactly where failure-to-heed and
reliance arguments concentrate — and, given Decision 6, the private channel is
the *main* delivery route for companion input during patient visits, so the gap
would be most of the companion's contribution. Sharing Decision 4's class also
means one retention decision covers both rather than two that drift apart.

### 6. Companion agency in patient visits runs through the private channel by default (Q3, accepted)

The companion's ask-and-correct agency was decided for conferences, where every
participant is a clinician. In **patient visits** it operates **through the
private channel by default**: the companion prompts the practitioner on their
private surface, and the correction reaches the room, if at all, **through the
practitioner's own voice**. **Audible companion speech to the room is reserved
for conferences, or a patient visit where the practitioner explicitly invites
it.**

This keeps the practitioner as the single voice of clinical authority in front
of the patient — which is precisely what verbal-first is protecting — while
still guaranteeing the correction is *delivered*, and, through Decision 5's
tagging, provably delivered. A companion that stays silent about a real error is
the failure mode dual attestation exists to catch; routing the correction
privately catches it without making the companion a second voice in the room.
The explicit-invitation escape hatch covers the practitioner who wants the
companion to address the room, without making that the default.

### 7. Consent is live, and revocation is forward-only (Q4, accepted)

Consent state is **live** for the duration of the session. Revocation **stops
capture forward** from the moment it is given; content **already captured is
retained under the consent that covered it** at the time; and **the consent
transition itself is logged as a session event** even though no content is
captured after it.

Forward-only revocation is the only reading honest to both the patient and the
record. Nothing further is recorded, which is what the patient asked for. And
nothing lawfully captured silently disappears — retroactive deletion would break
the append-only ledger posture and would destroy the two-witness corroboration
for the earlier part of the visit, in which the patient's consent was not in
question. Logging the transition without content mirrors the off-the-record
mechanism already decided for legal meetings, so the session has one
"capture stopped here" pattern rather than two.

This supersedes aic-003's episodic consent gate for in-visit capture: consent is
evaluated continuously against a session that spans the visit, not obtained once
per capture episode. The consent substrate — who consented, to what, recorded
where — carries forward unchanged.

### 8. The working differential is a versioned chart object, and promotion is a signed decision

The **working differential** is a first-class chart object: competing candidate
diagnoses with evidence links and uncertainty, **versioned across encounters**,
**distinct from the problem list**, and shared between practitioner and
companion. It is **live during the visit** — heard symptoms shift hypotheses in
real time, and called-out orders are evaluated against the active differential.

The separation from the problem list is deliberate and load-bearing. The pmr
problem list holds **conclusions**; a differential holds **hypotheses**, most of
which will be wrong on purpose. Collapsing them would either fill the problem
list with ruled-out candidates or force the differential to inherit
conclusion-grade semantics it cannot honour. **Promotion from working
differential to problem-list conclusion is therefore an explicit, signed
practitioner decision** — a recorded act with an actor, a time and a source
version, never an automatic consequence of confidence crossing a threshold.

Versioning is what makes the differential usable as evidence: reconstructing
what the practitioner was considering at the moment an order was called out
requires the version in force at that timestamp, so each in-visit revision is a
version and each staged order references the version it was evaluated against.

### 9. Voice-CPOE stages into the existing order path

Verbal call-outs **stage** orders in real time into the **existing order
composition path** (aic-013, ord-008) rather than into a parallel voice-order
store. A **human practitioner confirms by signature**; an **AI practitioner's
call-out carries order intent under its credential**, subject to that
credential's supervision tier — which is `practitioner-identity`'s to enforce,
including whether the order is staged and inert until a co-signature.

Staging into the existing path rather than beside it means every order
validation, interaction check, permission and signature rule that exists today
applies unchanged; the voice surface adds an origin and a transcript anchor, not
an order lifecycle. A staged order carries the transcript segment it came from,
the differential version it was evaluated against, and the session — so the
question "why was this ordered" is answerable from the order itself.

### 10. Every Flutter instance resolves its role at join

One Flutter client runs on several devices per session, and **each instance
resolves its role at join**: **common-to-room** or **private-to-practitioner**.
Role is a property of the join, not of the device type — the same hardware can
host either role in different sessions, and a practitioner's mobile that joins a
conference room device's session resolves privately without reconfiguration.

A private role carries a second screen and private audio for a human
practitioner, and a **private comms channel** for an AI practitioner, **including
when embodied in a robot**. Private-channel prompts address exactly one
practitioner and **never render on the room-common surface** — which is a
rendering guarantee enforced at the session layer, not a UI convention, because
Decision 6 makes the room-common surface patient-visible by definition.

Alternative considered and rejected: deriving the role from device registration.
It fails the moment a practitioner walks into another room, and it makes the
patient-visibility guarantee depend on provisioning state rather than on the
session.

### 11. A conference is the same session type with N practitioners

A case conference **instantiates the same witnessed encounter session** — the
same lifecycle, the same streaming transcript, the same dual-attestation
machinery, the same split surfaces — with **N practitioners** in place of one
patient encounter. What differs is participation, not architecture: the
companion **may ask questions of the meeting and correct members audibly**
(Decision 6's conference case), it renders a **live mind-map/graph of the
meeting's subjects**, it surfaces notes as the meeting proceeds with
**review-back links** to related chart items, and **every attending
practitioner signs the conference record under their credential**.

One session type rather than two is what keeps conference records evidentially
equivalent to visit records — same provenance classes, same attestation, same
tags — and it means car-054's conference record content (agenda, attendance,
dissent) becomes content carried by a session rather than a separate object with
its own lifecycle.

### 12. Dependency posture on `practitioner-identity` (proposed, not promoted)

This capability **signs but issues nothing**. Three things it needs are owned by
the sibling change `add-practitioner-identity`, whose capability
`practitioner-identity` is **proposed and not promoted**:

- the **companion's attesting credential** — the credential under which the
  companion signs its own record;
- the **AI practitioner's order-intent credential** and the supervision tier
  gating whether a called-out order takes effect;
- the **human-gate predicate restated** as *accountable credentialed
  practitioner*, without which a companion that signs and an AI practitioner
  that orders both contradict the catalog's standing boundary.

The posture is: **design to the shape, sequence around the gap**. Session
lifecycle, streaming transcript, the working differential, consent mechanics,
provenance classes and tagging, split surfaces and the conference type all
proceed now and are testable now. Attestation binding and voice-CPOE intent are
**blocked** on the sibling and marked as such in tasks. Where a credential is
absent, the companion's record is producible and the practitioner's signature
falls back to the conventional human gate; what is *not* available without the
sibling is the AI practitioner's call-out carrying order intent, which must be
refused rather than approximated.

An unresolved sub-question sits on the sibling's side and is restated here
rather than answered: whether the companion's witness credential is a reduced
practitioner profile or a distinct witness profile.

### 13. Superseded in-visit assumptions are restated, not deleted

Four catalog assumptions stop describing the in-visit path. Each is **restated in
place** with its in-visit scope narrowed; none is deleted, and each keeps
everything outside the in-visit path intact:

- **doc-039** — Recording → Processing → Draft Ready is the batch lifecycle for
  non-resident capture. In-visit capture is a resident streaming session, and
  doc-039's consent and provenance substrate carries forward.
- **aic-048** — async-job latency and fallback policy continues to govern
  post-visit inference. It stops governing in-room inference, which runs on the
  streaming path of Decision 2 with its own latency and degradation behaviour.
- **aic-003** — episodic consent becomes live session consent per Decision 7.
  The consent record, its parties and its provenance are unchanged.
- **mob-020** — consented mobile capture becomes one host of a session per
  Decision 1, rather than an episodic capture of its own.

Restatement rather than deletion is not politeness. Both descriptions currently
stand in the corpus, and doc-039 is the one written down as the documentation-side
contract; leaving them in place while adding a contradicting capability is how a
corpus starts answering the same question two ways. Deleting them would discard
the consent, provenance and mobile substrate this capability actually depends on.

## Risks / Trade-offs

- **[The streaming service becomes a second de facto write path — expedient
  direct writes creep in under latency pressure]** → Every durable mutation goes
  through the guarded surface with no exception path, the service holds no
  database credentials of its own, and the controller guards refuse an
  unflagged write exactly as they do today. Latency is solved by committing
  less often, never by writing around the guard.
- **[Two capture hosts produce two divergent transcripts of the same moment]** →
  Transcript segments carry host provenance and the session reconciles them into
  one ordered stream; the reconciliation is recorded, not assumed, and a segment
  that cannot be reconciled is retained with both readings rather than one being
  discarded.
- **[Reconciliation items accumulate unreviewed, and dual attestation becomes
  paperwork]** → The item is a stated work item with a lifecycle state and an
  owner, escalation is defined by the practice, and unreviewed items are
  visible; the design deliberately does not let the companion escalate on its
  own, which is the cost of Decision 3.
- **[Live prompting becomes an interruption engine that degrades the visit]** →
  Prompts are private by default (Decision 6), carry exposure tags so
  over-prompting is measurable rather than anecdotal, and the room-common
  surface is never a prompt target in a patient visit.
- **[The unspoken layer is built, and the legal research later rules it
  undiscoverable-but-retained, or retained-but-patient-visible, in a way the
  class cannot express]** → The class is a container with a policy attached, not
  a policy baked into storage; retention and visibility are attributes of the
  class, changeable without moving content. The tags are the part that cannot be
  deferred, and they are built now.
- **[An always-listening device sits in an exam room]** → Consent is live and
  revocation is forward-only and immediate (Decision 7), the transition is
  logged, and room-device hardware posture — appliance, wall panel, docked
  tablet — is called out as an open question rather than assumed.
- **[`practitioner-identity` does not land, and attestation has no credential]** →
  Decision 12 sequences every unblocked piece first; the companion's record is
  producible without a credential and the practitioner signs under the
  conventional human gate. The AI practitioner's order intent is refused, not
  approximated, so the gap degrades capability rather than authority.
- **[The live differential drifts into an unreviewed machine-maintained
  hypothesis set that nobody signs]** → Promotion to the problem list is an
  explicit signed practitioner decision (Decision 8), the differential is
  labelled as hypotheses throughout, and no downstream surface may treat a
  differential candidate as a conclusion.
- **[Conference reuse forces patient-visit semantics onto meetings, or the
  reverse]** → The session type is shared and the *participation rules* are
  parameterised by encounter type; the one rule that differs by type — audible
  companion speech — is stated as a type-level condition rather than a runtime
  toggle.

## Migration Plan

1. Land the session, transcript-segment and session-event records with their
   provenance classes and the exposure/reliance tags, behind the guarded write
   surface, with migrations, permissions, audit and synthetic fixtures.
2. Stand up the streaming session service beside bench with its own lifecycle,
   holding session, transcript stream and inference, and give it only guarded
   `api.v1`-style access.
3. Add live consent evaluation and forward-only revocation with the transition
   logged as a session event.
4. Add the working differential as a versioned chart object with in-visit
   revision and the signed promotion path to the problem list.
5. Add the Flutter multi-device join, role resolution and private surfaces,
   including the AI practitioner's private comms channel.
6. Add dual attestation and the reconciliation item — bound to
   `practitioner-identity` credentials once available, producible without them
   in the interim.
7. Add voice-CPOE staging into the existing order path; the AI practitioner's
   credential-borne intent waits on the sibling.
8. Add the conference encounter type, the live mind-map/graph and review-back
   links.
9. Restate doc-039, aic-048, aic-003 and mob-020's in-visit assumptions.

Rollback removes the streaming service and the session surfaces from disposable
sites; because every durable write went through the guarded surface, no rollback
leaves an orphaned write path, and post-visit rq work is untouched throughout.
Nothing in this plan grants clinical authority or flips an environment to
production.

## Open Questions

- Room-device hardware posture: a fixed appliance, a wall panel, a docked tablet,
  or simply the first Flutter instance to claim the room role? The answer drives
  microphone quality, mid-visit network-drop behaviour, physical security of an
  always-listening exam-room device, and who provisions it.
- Is the conference mind-map/graph the same graph object the AI practitioner
  loads in the pre-visit fast-graph runbook rendering, viewed from another angle
  — the case as prepared versus as discussed? If so the conference view is a live
  rendering over an existing artifact, and one-artifact-two-renderings extends
  into the meeting.
- What is the commit granularity on the streaming path — per utterance, per
  segment, per interval — and what is the maximum window of in-flight transcript
  that a service crash may lose?
- Is the companion's witness credential a reduced practitioner profile or a
  distinct witness profile? Owned by `add-practitioner-identity`; restated here
  because attestation binding depends on the answer.
- What does the patient see of a working differential whose candidates were later
  ruled out?
- Identity and trust for external participants, human or AI, from other
  organizations, and the consult-package exchange that would carry a conference
  across an organizational boundary.

## ADDED Requirements

### Requirement: A witnessed encounter session opens before the encounter and resumes rather than restarts
openChart SHALL define a Witnessed Encounter Session that is opened before the encounter begins, carries encounter type, patient or case subject, participating practitioners, lifecycle state (`open`, `active`, `interrupted`, `resumed`, `closed`), consent state and audit provenance. The session MUST survive interruption of any host and MUST be rejoined by resume against the same session identity; a rejoin MUST NOT create a second session for the same encounter, and loss of every host MUST NOT close the session.

#### Scenario: Session opens before the encounter
- **WHEN** a practitioner opens a session for a scheduled encounter before the patient is seen
- **THEN** the session exists in `open` state with its subject, participants and consent state recorded, and is addressable before any capture occurs

#### Scenario: A host drops mid-visit and returns
- **WHEN** a host loses connectivity during an active session and rejoins
- **THEN** the host attaches to the same session identity, the session records an interruption and a resume as session events, and no second session is created

#### Scenario: Every host disconnects
- **WHEN** all hosts of an active session disconnect
- **THEN** the session enters `interrupted` rather than `closed`, and its committed content remains addressable

### Requirement: Runbook state and check-off provenance hand off into the session at open
The pre-visit prep runbook SHALL be a surface preceding the visit, and its state — the canonical item set and every check-off, each a first-class provenance event carrying actor and time — MUST transfer into the witnessed encounter session at open as an explicit recorded hand-off. The session MUST NOT be modelled as the runbook's next screen, and runbook check-off provenance MUST remain durable evidence of preparation whether or not the session subsequently opens.

#### Scenario: Prepared runbook opens a session
- **WHEN** a practitioner opens a session after working a pre-visit runbook
- **THEN** the runbook item set and its check-off provenance events are present in the session, and the hand-off itself is recorded with its time

#### Scenario: Visit never happens
- **WHEN** a runbook is completed and no session is ever opened
- **THEN** the check-off provenance events remain durable and auditable as evidence of preparation

### Requirement: One session is hosted concurrently by a room device and a practitioner mobile
A session SHALL accept multiple concurrent hosts, specifically a dedicated room-resident device and the practitioner's mobile, capturing into the same session. Neither host SHALL be defined as the other's fallback, every transcript segment MUST carry the host that captured it, and reconciliation of overlapping captures into one ordered transcript MUST be recorded rather than assumed. A segment that cannot be reconciled MUST be retained with both readings rather than one being discarded.

#### Scenario: Both hosts capture the same utterance
- **WHEN** the room device and the practitioner's mobile both capture the same spoken moment
- **THEN** the session produces one ordered transcript with per-segment host provenance and a recorded reconciliation

#### Scenario: Captures cannot be reconciled
- **WHEN** two hosts produce readings of the same moment that cannot be reconciled
- **THEN** both readings are retained on the segment and neither is silently discarded

#### Scenario: Mobile-only session
- **WHEN** a session runs with only the practitioner's mobile attached
- **THEN** the session is fully valid and its capture is not marked as fallback or second-class evidence

### Requirement: The in-visit surface streams a live transcript
An active session SHALL produce a transcript as the encounter happens, available in the room during the encounter. The in-visit path MUST NOT be a record-then-process-then-draft batch lifecycle, and transcript segments MUST commit durably during the session rather than only at its close. Post-visit work MAY remain queued.

#### Scenario: Transcript is visible during the visit
- **WHEN** an active session is capturing
- **THEN** transcript content is available on the session's surfaces while the encounter is still in progress

#### Scenario: Session ends abnormally
- **WHEN** an active session terminates without a clean close
- **THEN** every transcript segment committed before termination remains durable and attributable

### Requirement: Live prompting is bound to what is being said
The companion SHALL deliver prompts to a practitioner during an active session, derived from the session's live content, and every prompt MUST carry the transcript anchor and session it derived from. Prompting MUST NOT be deferred to a post-visit review step for in-visit content.

#### Scenario: Prompt derived from a heard symptom
- **WHEN** a patient states a symptom during an active session
- **THEN** any resulting prompt is delivered during the session and carries the transcript anchor it derived from

### Requirement: The working differential is a first-class versioned chart object, live during the visit
openChart SHALL define a Working Differential carrying competing candidate diagnoses with evidence links and stated uncertainty, versioned across encounters, addressable independently of the problem list, and shared between practitioner and companion. It MUST be maintained and displayed during an active session so that symptoms heard revise it in real time, and each in-visit revision MUST produce a new version rather than overwriting the prior one. A differential candidate MUST NOT be represented as a conclusion by any surface.

#### Scenario: Heard symptom revises the differential
- **WHEN** a symptom is heard during an active session
- **THEN** the differential is revised as a new version during the visit, and the prior version remains addressable

#### Scenario: Candidate is read as a conclusion
- **WHEN** a consumer attempts to treat a working-differential candidate as a problem-list conclusion
- **THEN** the object's kind and the promotion requirement prevent that interpretation

#### Scenario: State at a past moment is reconstructed
- **WHEN** an auditor asks what was being considered at the time an order was called out
- **THEN** the differential version in force at that timestamp is retrievable

### Requirement: Promotion from working differential to problem list is an explicit signed practitioner decision
Promotion of a differential candidate to a problem-list conclusion SHALL be a recorded act carrying the deciding practitioner, the time, the source differential version and a signature. Promotion MUST NOT occur automatically from confidence, evidence accumulation or companion recommendation, and the companion MUST NOT promote.

#### Scenario: Practitioner promotes a candidate
- **WHEN** a practitioner promotes a candidate to the problem list
- **THEN** a signed promotion record carries the practitioner, time, source differential version and signature

#### Scenario: Confidence crosses a threshold
- **WHEN** a candidate's stated confidence rises above any threshold with no practitioner decision
- **THEN** no promotion occurs and the candidate remains a hypothesis

#### Scenario: Companion attempts promotion
- **WHEN** the companion attempts to promote a candidate to the problem list
- **THEN** the operation is refused

### Requirement: Orders and symptoms are analyzed in real time against the live differential
During an active session, symptoms and orders SHALL be analyzed as they are heard — spoken by the patient, called out by the practitioner, or noted — and evaluated against the active working differential, for a human and an AI practitioner alike. Each analysis result MUST reference the differential version it was evaluated against.

#### Scenario: Order is called out during the visit
- **WHEN** a practitioner calls out an order aloud during an active session
- **THEN** the order is evaluated against the active differential version and that version is referenced on the result

#### Scenario: Analysis is requested for an AI practitioner
- **WHEN** the practitioner in the session is an AI practitioner
- **THEN** real-time symptom and order analysis operates identically to a human practitioner's session

### Requirement: The encounter protocol is modality-equal and verbal-first
Both practitioner kinds SHALL conduct the clinical encounter verbally: an AI practitioner speaks to the patient and calls out orders aloud exactly as a human practitioner does. There MUST NOT be a silent, non-spoken clinical lane through which an AI practitioner conducts an encounter or issues an order that never becomes audible in the room.

#### Scenario: AI practitioner conducts a visit
- **WHEN** an AI practitioner conducts a patient encounter
- **THEN** its clinical communication and order call-outs are spoken into the room and captured by the session like a human practitioner's

#### Scenario: Silent clinical lane is attempted
- **WHEN** an AI practitioner attempts to issue a clinical order in an active patient encounter without an audible call-out
- **THEN** the path is refused and the order does not stage

### Requirement: Two independent witnesses produce and sign records of the same visit
A witnessed encounter SHALL produce two attestations: the practitioner signs the record as they said and heard it, and the companion independently produces and signs its own record of the same session. Both attestations MUST be independently addressable, MUST NOT be merged into a single record, and where the practitioner is an AI its own record MUST be comparable against the companion's. The companion's attestation MUST identify it as a witness holding no clinical decision-making authority.

#### Scenario: Human practitioner visit is dual-attested
- **WHEN** a human practitioner signs the record of a completed session
- **THEN** the companion's independently produced record is also signed and both stand side by side against the same session

#### Scenario: AI practitioner record is compared
- **WHEN** an AI practitioner signs its own record of a session
- **THEN** that record is comparable against the companion's record of the same session

#### Scenario: Records are merged
- **WHEN** a caller attempts to merge the practitioner's and companion's records into one
- **THEN** the operation is refused and both records remain independently addressable

### Requirement: Record divergence never blocks signing and files as a reconciliation item
Divergence between the practitioner's record and the companion's record MUST NOT block, delay or invalidate chart signing. Both records SHALL file independently and the discrepancy SHALL be emitted as a Reconciliation Item carrying the session, the diverging content, the time and a lifecycle state, reviewed after the visit by the practitioner. Escalation paths SHALL be defined by the practice, and the companion MUST NOT escalate, override or veto on its own authority.

#### Scenario: Companion disagrees with the practitioner's record
- **WHEN** the companion's record diverges from the practitioner's for the same session
- **THEN** both records file, signing proceeds unblocked, and a flagged reconciliation item is created with the diverging content and a timestamp

#### Scenario: Companion attempts to block signing
- **WHEN** the companion attempts to prevent a practitioner's signature because of a divergence
- **THEN** the attempt has no effect and the signature completes

#### Scenario: Reconciliation item is left unreviewed
- **WHEN** a reconciliation item is not reviewed
- **THEN** it remains a visible open item in its lifecycle state rather than being closed or discarded

### Requirement: The record is layered and unspoken portions are held in a distinct provenance class
openChart SHALL hold, alongside the spoken and witnessed layer, each actor's unspoken portion — the practitioner's private reasoning, an AI practitioner's reasoning trace, and the companion's extended analysis — as part of the record in a provenance class distinct from the witnessed layer. The class MUST be a first-class attribute of each record element so an evidence selection can address the witnessed layer alone, or the witnessed layer with relied-upon companion output, or the whole record. Retention period and patient visibility for the unspoken class SHALL be deferred to the named legal-research work item and MUST be attributes of the class rather than properties baked into storage.

#### Scenario: Evidence selection addresses the witnessed layer alone
- **WHEN** an evidence selection requests only the witnessed spoken layer of a session
- **THEN** the selection returns witnessed content with no unspoken-class content, without re-deriving classes

#### Scenario: Retention policy is set later
- **WHEN** the legal-research work item settles a retention period for the unspoken class
- **THEN** the policy is applied as an attribute of the class without relocating or rewriting existing content

### Requirement: Exposure and reliance are tagged contemporaneously on companion output
Every companion output SHALL carry an exposure tag recording whether it was surfaced to a practitioner and a reliance tag recording whether the practitioner acted on it, both written at the time the event occurs. Neither tag MAY be reconstructed after the fact, and a surfaced-but-unacted-upon output MUST be distinguishable from one that was never surfaced.

#### Scenario: Prompt is surfaced and ignored
- **WHEN** a companion prompt is delivered to a practitioner who does not act on it
- **THEN** the element carries exposure recorded at delivery and reliance recorded as not relied upon, and is distinguishable from an unsurfaced output

#### Scenario: Prompt changes what the practitioner orders
- **WHEN** a practitioner stages an order after a companion prompt on the same subject
- **THEN** the reliance tag is recorded contemporaneously against that prompt

#### Scenario: Tag is written after the session
- **WHEN** a caller attempts to set an exposure or reliance tag on a closed session's element
- **THEN** the write is refused and the contemporaneous record stands

### Requirement: Private-channel prompts are part of the encounter record
Prompts delivered to a practitioner on a private surface or private comms channel SHALL be part of the encounter record, held in the same provenance class as the unspoken portions and carrying the same exposure and reliance tags. A private channel MUST NOT be an unrecorded delivery path.

#### Scenario: Private prompt during a patient visit
- **WHEN** the companion prompts a practitioner privately during a patient visit
- **THEN** the prompt is recorded in the unspoken provenance class with exposure and reliance tags

#### Scenario: Unrecorded private delivery is attempted
- **WHEN** a delivery path attempts to send a practitioner prompt without recording it
- **THEN** the delivery is refused

### Requirement: Companion ask-and-correct agency is private by default in patient visits
In a patient encounter the companion's questions and corrections SHALL be delivered through the practitioner's private channel by default, and the companion MUST NOT speak audibly to the room unless the practitioner explicitly invites it, with the invitation recorded as a session event. In a conference encounter the companion MAY address the meeting audibly. The practitioner SHALL remain the single voice of clinical authority to the patient, and a correction reaches the room, if at all, through the practitioner.

#### Scenario: Companion detects an error in a patient visit
- **WHEN** the companion identifies a probable error during a patient encounter with no standing invitation
- **THEN** the correction is delivered on the practitioner's private channel and nothing is rendered or spoken to the room

#### Scenario: Practitioner invites the companion to address the room
- **WHEN** a practitioner explicitly invites the companion to speak to the room during a patient encounter
- **THEN** the invitation is recorded as a session event and audible companion speech is permitted for that session

#### Scenario: Companion attempts audible speech uninvited
- **WHEN** the companion attempts to speak audibly in a patient encounter with no invitation recorded
- **THEN** the attempt is refused and the content is delivered privately instead

### Requirement: Consent is live and revocation stops capture forward only
Session consent state SHALL be evaluated live for the duration of the session rather than obtained per capture episode. Revocation MUST stop capture from the moment it is given, content captured before revocation MUST be retained under the consent that covered it at the time, and the consent transition itself MUST be logged as a session event even though no content is captured after it. Revocation MUST NOT delete, redact or invalidate previously captured content, and the session MUST remain open through the transition.

#### Scenario: Patient revokes consent mid-visit
- **WHEN** a patient revokes consent during an active session
- **THEN** capture stops immediately, content captured before that moment is retained, and a consent-transition session event is logged

#### Scenario: Retroactive deletion is attempted
- **WHEN** a caller attempts to delete content captured before a revocation on the grounds of that revocation
- **THEN** the deletion is refused and the earlier content remains available to authorized audit

#### Scenario: Consent is restored later in the same session
- **WHEN** consent is given again after a revocation in the same session
- **THEN** capture resumes forward from that moment and a second consent-transition event is logged, with the uncaptured interval evident from the events

### Requirement: Verbal call-outs stage orders into the existing order path
A verbal order call-out during an active session SHALL stage an order in real time into openChart's existing order composition path rather than into a parallel voice-order store, carrying the originating transcript segment, the differential version it was evaluated against, and the session. A human practitioner's staged order MUST take effect only on that practitioner's signature. An AI practitioner's call-out SHALL carry order intent under its own credential, subject to the supervision tier of that credential, and where no valid credential is present the staged order MUST be refused rather than approximated under another authority.

#### Scenario: Human practitioner calls out an order
- **WHEN** a human practitioner calls out an order aloud
- **THEN** an order is staged on the existing order path with its transcript anchor, differential version and session, and takes effect only when the practitioner signs

#### Scenario: AI practitioner calls out an order under credential
- **WHEN** an AI practitioner with a valid credential calls out an order
- **THEN** the staged order carries order intent under that credential and its effect is governed by the credential's supervision tier

#### Scenario: AI call-out with no valid credential
- **WHEN** an AI practitioner with no valid credential calls out an order
- **THEN** the staged order is refused and no other authority is substituted

#### Scenario: Parallel voice-order store is attempted
- **WHEN** a voice call-out attempts to create an order outside the existing order composition path
- **THEN** the operation is refused

### Requirement: Sessions are split-surface and every client instance resolves its role at join
Each Flutter client instance joining a session SHALL resolve its role at join as `common-to-room` or `private-to-practitioner`, determined by the join rather than by device registration or device type. A private role SHALL carry a private second screen and private audio for a human practitioner and a private comms channel for an AI practitioner, including a robot-embodied one. Private-channel content addressed to one practitioner MUST NOT render or sound on any common-to-room surface, enforced at the session layer.

#### Scenario: Same device joins in different roles
- **WHEN** a device that hosted the room-common role in one session joins another session as a practitioner's private surface
- **THEN** the role resolves from the join and no reconfiguration or re-registration is required

#### Scenario: Private prompt is addressed to one practitioner
- **WHEN** a prompt is addressed to a single practitioner in a session with a room-common surface attached
- **THEN** the prompt renders only on that practitioner's private surface and never on the room-common surface

#### Scenario: Robot-embodied AI practitioner joins
- **WHEN** an AI practitioner joins a session embodied in a robot
- **THEN** it resolves a private-to-practitioner role with a private comms channel while its spoken clinical communication remains audible in the room

### Requirement: A conference is the same witnessed encounter session with N practitioners
A case conference SHALL instantiate the same witnessed encounter session type with N practitioners in place of a single patient encounter, using the same lifecycle, streaming transcript, provenance classes, tagging and attestation machinery. The companion SHALL surface notes as the meeting proceeds with review-back links to related chart items, render a live mind-map or graph of the meeting's subjects, and MAY ask questions of the meeting and correct members audibly. Every attending practitioner, human or AI, MUST sign the conference record under their own credential, and dissent MUST be carried as record content.

#### Scenario: Conference is captured and signed
- **WHEN** a case conference with several practitioners completes
- **THEN** every attending practitioner signs the conference record under their own credential and the record carries the same provenance classes as a patient encounter

#### Scenario: Companion participates in the meeting
- **WHEN** the companion identifies a correction during a conference
- **THEN** it may address the meeting audibly, and the exchange is captured in the session transcript

#### Scenario: A member dissents
- **WHEN** an attending practitioner dissents from the conference's conclusion
- **THEN** the dissent is carried as content of the conference record rather than as a separate unlinked object

#### Scenario: Review-back to a chart item
- **WHEN** the companion surfaces a note referencing a prior chart item during a conference
- **THEN** the note carries a review-back link resolving to that chart item

### Requirement: Every durable chart mutation from the streaming session crosses the guarded write surface
The live session runtime SHALL be a dedicated streaming service with its own process lifecycle, holding the live session, transcript stream and inference path, separate from Frappe's rq worker model, which SHALL continue to serve post-visit jobs unchanged. Every durable chart mutation the session produces — transcript segment commit, differential version, staged order, attestation, reconciliation item, session event — MUST be written through the guarded versioned API surface with the same subject, tenant, purpose and role context required of any other write. The streaming service MUST NOT hold a direct write path to chart storage, and its in-flight state MUST NOT be authoritative over committed session state.

#### Scenario: Transcript segment commits
- **WHEN** the streaming service commits a transcript segment
- **THEN** the write passes the guarded API surface with full context and is refused if that context is absent

#### Scenario: Streaming service attempts a direct write
- **WHEN** the streaming service attempts to mutate chart storage outside the guarded surface
- **THEN** the write is refused by the controller guards exactly as any other unguarded write is

#### Scenario: Service state diverges from committed state
- **WHEN** the streaming service's in-flight state disagrees with the session's committed state
- **THEN** the committed state is authoritative

#### Scenario: Post-visit work continues on rq
- **WHEN** a post-visit job runs for a closed session
- **THEN** it executes on the existing rq worker model with no change to that path

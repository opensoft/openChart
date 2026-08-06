"""OC Patient External Identifier controller (FR-002; brief D3, D6).

An active (issuer, value) pair on another patient forces
identity_review — never a merge. Enforced by GuardedIdentifier.
"""

from open_chart.intake.guarded import GuardedIdentifier


class OCPatientExternalIdentifier(GuardedIdentifier):
    pass

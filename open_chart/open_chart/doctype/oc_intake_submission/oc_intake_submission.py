"""OC Intake Submission controller (FR-003, FR-006; brief D4, D5, D6).

Accepted content is immutable; amendments are successors, never
in-place edits or Frappe cancel-amend. Enforced by GuardedSubmission.
"""

from open_chart.intake.guarded import GuardedSubmission


class OCIntakeSubmission(GuardedSubmission):
    pass

Read AGENTS-shape.md first — the rules of this repository's shape.

This is the assembly root of **openChart** (`openchart`): the repository an
engineer clones. It holds `project.yaml`, the pins and the gate, and it mounts
the two legs.

| role | repository | path |
|---|---|---|
| assembly | `opensoft/openChart` | `.` |
| spec | `opensoft/openChart-spec` | `spec/` |
| code | `opensoft/openChart-code` | `code/` |

Everything below this line is openChart's own. The shape wrote the block above
once and does not pin this file, so how this project is built, tested, reviewed
and released belongs here and nothing upstream will overwrite it.

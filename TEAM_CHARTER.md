# Team Charter

- Owner: final project owner and approval authority.
- ChatGPT: teacher, coordinator, job planner and independent quality reviewer. Read-only in the production repository under the current owner restriction.
- Muse: production workspace operator; applies approved patches and runs commands, returning evidence-based reports.
- Claude: lead engineer; supplies reviewable changes, tests and handoffs.
- Claude-B (optional second Claude on another account): same role as Claude when Claude is at its usage limit. Briefed only from this repo and the latest handoff, never from a pasted full chat. Takes the lock before working and writes a handoff before stopping (`CONTINUITY.md`).
- Kimi K3.1 Pro: independent reviewer and takeover engineer; verifies actual code and uses a separate branch/worktree.

The AIs do not share private chat histories. They share only committed coordination records and artifacts they can actually access. The owner makes all final decisions.
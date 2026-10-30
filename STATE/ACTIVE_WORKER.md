# Active Worker Lock

`LOCK_STATUS: FREE`

Last driver: Claude, job CLAUDE-0001 (control repo documentation only), branch `claude/control-review-0001`, finished 2026-10-30. Next suggested driver: Muse for SCRIPT-0001 (production workspace, separate from this repo).

## Lock format (copy when taking the lock; commit it before any other change)
```
LOCK_STATUS: HELD
Job: <id>      Agent: <name>      Started: <UTC time>
Target: <repo or workspace>   Branch/path: <name>   Base commit: <sha>
Deliverable: <what>           Handoff condition: <when the lock is released>
```
Only one agent writes to a working copy or branch. Others review read-only or use their own branch. Rules: `CONTINUITY.md`.

# Simulated takeover test (2026-10-30, by Claude)

Command: `python3 tools/simulate_takeover.py` (runs on a temp copy; the real repo is untouched).
Result: **13/13 checks passed**, exit 0. `python3 tools/check_control.py` on the repo: CONTROL OK.

Scenario: agent A (Claude) finishes part 1 of a task and hits its limit, writes a dated handoff and frees the lock. Agent B (Claude-B or Kimi) reads the latest handoff, finds what is done and the exact next action, takes the lock, does only part 2, writes its own handoff linked to A's, frees the lock. A returns, reads B's handoff, sees nothing to redo, and knows the remaining task belongs to Muse.

Checked: completed vs pending identified; exact next action found; B only worked jobs assigned to it; Muse's inbox job byte-identical afterward; no earlier handoff changed or deleted; both handoffs preserved and linked; structure rules valid at every step.

## Limits (honest)
- This is a scripted simulation of the protocol rules. One program plays both agents, so it proves the files and rules work as designed, not that two real AIs will follow them.
- The real acceptance test is still CTL-0002 plus a live two-agent round trip: one agent writes a handoff in this repo, a different agent (another Claude account or Kimi) reads only the repo and continues, and the first agent resumes from its handoff.
- Pushing to GitHub from Claude is not yet possible, so the live test cannot be completed until access is fixed.

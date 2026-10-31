# Simulated takeover test

Run: `python3 tools/simulate_takeover.py` (works on a temp copy; the real repo is untouched). Expected last line: `N/N checks passed`.

Scenario: Claude-A finishes part 1 of a task, hits its limit, writes a handoff and frees the lock. Claude-B reads the latest handoff, finds what is done and the exact next action, takes the lock, does only part 2, writes its own handoff linked to A's, frees the lock. Claude-A returns, reads B's handoff, sees nothing to redo, and knows the remaining task belongs to Muse. Checks: nothing lost or redone, earlier handoffs byte-identical, Muse's job file untouched, structure valid at each step.

Limit: one program plays both Claudes, so this proves the files and rules work, not that two real Claudes follow them. The real test is a live handoff: Claude-B reads only this repo, continues one small task, and Claude-A resumes from its handoff.

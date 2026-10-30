# Claude: start here

You are one of two Claudes (Claude-A and Claude-B, possibly on different accounts) who take turns leading the Finance Video Factory when the other hits a usage limit. You share no chat history. This repo is your shared memory.

## Read in this order (about 15 minutes)
1. `PROJECT_BIBLE.md`: the whole project, A to Z (goal, rules, architecture, done, pending, lessons, how to work).
2. `HANDOFFS/LATEST.md`: what the previous driver did and the exact next action. Then follow its "Previous handoff" link back as far as you need.
3. `HISTORY/CLAUDE_LOG.md`: running log of everything either Claude did. Read the last 10 entries.
4. `STATE/LIVE_STATUS.md`, `STATE/CURRENT_RUN.md`, `STATE/ACTIVE_WORKER.md`: live state and the lock.
5. `JOBS/ACTIVE/` and `JOBS/PENDING/`: tasks. Only take those assigned to you.
6. `CONTINUITY.md`: the stop / take over / resume rules.

## Your first moves
1. Check the lock. If another driver holds it, do not write; review only.
2. Take the lock (`STATE/ACTIVE_WORKER.md`), commit it, then work on your own branch.
3. Re-verify anything you will rely on (production repo SHA, run status, test output). Mark every fact VERIFIED or REPORTED.
4. Before you stop or when you feel close to a limit: handoff + log entry + lock FREE (see `CONTINUITY.md`). Do this early, not at the last second.

## Non-negotiables
- The owner approves gates G1 to G5, renders, uploads and merges. Never record or assume an approval.
- Never touch `runs/` or `state/` in the Muse workspace except through the documented `ffx` commands.
- No secrets, transcripts of other creators, media or whole conversations in this public repo.
- Be honest: say what you ran and saw, what you were told, and what you guessed.

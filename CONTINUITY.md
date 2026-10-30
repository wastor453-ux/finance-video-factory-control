# Continuity Protocol: stop, take over, resume

Goal: any agent (Claude, a second Claude account "Claude-B", Kimi, ChatGPT) can open this repo, understand the real state, continue the work, and hand it back, without the owner re-explaining anything. This repo is PUBLIC, so everything here is sanitized (see Safety).

## Roles in a handoff
- **Driver**: the one agent currently allowed to change a given working copy or branch. Named in `STATE/ACTIVE_WORKER.md`.
- **Reviewer**: any other agent, read-only or on its own branch.
- **Courier**: the owner. Agents do not share chats or files; the owner carries patches and reports between Claude, Muse and this repo. Plan for that, never assume a shared filesystem.

## 1. Before you stop (limit reached, or end of session)
Do these in order. If you may be cut off any moment, do step 1 first.
1. Write a dated handoff: `HANDOFFS/archive/YYYY-MM-DD-NN-<agent>.md` using the template below, then copy it to `HANDOFFS/LATEST.md`. Never overwrite an archived handoff.
2. Update `STATE/LIVE_STATUS.md` and `STATE/CURRENT_RUN.md` (every fact tagged VERIFIED, REPORTED, or UNVERIFIED).
3. Set `STATE/ACTIVE_WORKER.md` to `FREE` (or to the agent you hand to) with the exact next action.
4. Commit on your own branch and push. If you cannot push, give the owner the files and say so in the handoff.

## 2. When you take over
1. Read in this order: `AGENTS.md`, `PROJECT_CONTEXT.md`, `CONTINUITY.md`, `STATE/*`, `HANDOFFS/LATEST.md`, then the previous handoff it links, then jobs addressed to you in `JOBS/ACTIVE` and `JOBS/PENDING`.
2. Do not trust old reports. Re-check the real state: production repo SHA, the run's `run_status`, test output. Mark what you checked as VERIFIED and what you only read as REPORTED.
3. Take the lock: edit `STATE/ACTIVE_WORKER.md` (job, agent, start time, target, branch, base commit, deliverable) and commit it before any other change.
4. Do not redo anything the handoff lists as DONE with evidence. Do not touch work another agent left IN PROGRESS without asking in the handoff thread.
5. Only act on jobs whose `Assignee` is you, unless the owner assigns you another.

## 3. When the first agent returns
Read the newest handoff and the commits since your last handoff. Treat the other agent's work as permanent project history: do not overwrite or quietly redo it. If you disagree, write a dated note in `MEMORY/DECISIONS.md` or a review in the job, do not edit their handoff.

## Handoff template
```
# Handoff YYYY-MM-DD-NN by <agent>
Previous handoff: <link>
Branch/commit: <name>@<sha>
## Done (with evidence)        - item: evidence
## In progress (not finished)  - item: exact stopping point
## Next action                 - one concrete step, who does it
## Pending tasks / who owns them
## Blockers and known limits
## Verified vs reported         - list each
```

## Rules that prevent confusion
- Append-only: old handoffs, jobs and decisions are never deleted or replaced. Mark them SUPERSEDED with a link instead.
- One driver per working copy or branch. Everyone else reviews.
- Every new package links to the previous one.
- Job files move `PENDING -> ACTIVE -> DONE` (never deleted).
- Approvals (G1 to G5, render, upload) belong to the owner only. Never record an approval the owner did not give.

## Safety (public repo)
Never commit keys or tokens, raw transcripts of other creators' videos, voice or video files, private URLs, machine paths, usernames, or whole chat logs. Summaries and checksums only. A second Claude must be briefed from this repo and the latest handoff, never from a pasted full conversation.

## Checks
`python3 tools/check_control.py` verifies the structure rules above. `TESTS/TAKEOVER_TEST.md` records the simulated takeover test and its result.

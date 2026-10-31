# Start here (Claude-A or Claude-B)

You share no memory with the other Claude. Rebuild it from this repo.

## The working model (owner's rule)
- **One Claude works at a time: the driver.** The other Claude does NOT work in parallel; it only reads, or answers a knowledge check. The owner decides when to switch: when the driver hits its usage limit, the owner tells the other Claude to resume.
- **The driver keeps this repo updated as it goes, not only at the end.** A limit can hit without warning. After every meaningful step (a finished sub-task, a decision, a test result, a file sent to Muse) update the `Checkpoint` section in `STATUS.md`, append a line to `LOG.md` when something is finished, commit and push. If the driver is cut off with no handoff, the next Claude rebuilds the state from `STATUS.md`'s checkpoint, `LOG.md` and `git log`.
- **The resuming Claude reads the repo and the driver's history first, then continues exactly where the driver stopped.** When the first Claude returns, it does the same with the other's work.
- Both Claudes must know the same things. `TESTS/KNOWLEDGE_CHECK.md` is how we check that.

## 0. How to get the files
Best: a Claude Code session with this repo attached (`git clone https://github.com/wastor453-ux/finance-video-factory-control`), which also lets you push. In plain chat, GitHub folder pages are often blocked: open files by their raw links (`https://raw.githubusercontent.com/wastor453-ux/finance-video-factory-control/main/<path>`), or ask the owner to attach a zip of the repo or paste the files. To write, you need the Claude GitHub app installed for this repo on your account; otherwise hand the owner the changed files and say so in the handoff.

## 1. Read (about 15 minutes)
1. `PROJECT_BIBLE.md`: goal, owner rules, pipeline, done, pending, lessons, how to work.
2. `HANDOFFS/LATEST.md`, then the "Previous handoff" links back as far as needed.
3. `STATUS.md`: who holds the lock, current run, exact next action.
4. Last 10 entries of `LOG.md` (what each Claude did) and `DECISIONS.md`.
5. `JOBS/todo/` and `JOBS/doing/`. `MUSE_PLAYBOOK.md` when you need to instruct Muse.

## 2. Take over
1. If `STATUS.md` says `LOCK: HELD` by the other Claude, do not write until the owner tells you the other Claude has stopped (limit reached). Then take over from its checkpoint and last handoff.
2. Verify what you will rely on (production repo SHA, run status, tests). Tag facts [V] verified by you, [R] reported, [?] unknown. Do not trust old reports blindly and do not redo work marked done with evidence.
3. Take the lock: edit `STATUS.md` (`LOCK: HELD`, who, when, job, branch). Commit it first. Work on your own branch. Move your job `todo -> doing`.

## 3. Stop (limit reached, or end of session). Do this early, not at the last second.
1. Write `HANDOFFS/YYYY-MM-DD-NN-<claude>.md` using the template below. Copy it to `HANDOFFS/LATEST.md`. Never edit or delete an older handoff.
2. Add an entry to the bottom of `LOG.md`.
3. Update `STATUS.md` (lock `FREE`, current run, next action) and move finished jobs to `done/`.
4. Run `python3 tools/check_repo.py`, commit, push, and merge your pull request if the owner has authorized it (see `DECISIONS.md`). If you cannot push, give the owner the files and say so in the handoff.

## 4. Return after the other Claude worked
Read its handoff and the commits since yours. Its work is permanent history: do not overwrite or quietly redo it. If you disagree, add a dated note in `DECISIONS.md` or a new `LOG.md` entry; never edit its handoff.

## Handoff template
```
# Handoff YYYY-MM-DD-NN by <Claude-A|Claude-B>
Previous handoff: [name](name.md)      (omit only for the very first)
Branch/commit: <name>@<sha>
## Done (with evidence)
## In progress (exact stopping point)
## Next action (one concrete step, who does it)
## Pending jobs
## Blockers and limits
## Verified [V] vs reported [R]
```

## Non-negotiables
- Only the owner approves gates G1 to G5, renders, uploads, and merges in the production repo. Never record or assume an approval.
- Never touch Muse's `runs/` or `state/` except through the documented `ffx` commands.
- Public repo: no keys or tokens, no other creators' transcripts, no media, no machine paths, no private URLs, no whole chats.
- Say what you ran and saw, what you were told, and what you guessed.

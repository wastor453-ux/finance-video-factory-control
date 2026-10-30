# Claude shared log (Claude-A and Claude-B)

Append-only. Never edit or delete an old entry; correct it with a new entry that links to it. Newest entries go at the bottom. Each entry: date, who, what was done with evidence, what is left, link to handoff or commit.

Entry format:
```
## YYYY-MM-DD-NN | Claude-A or Claude-B | short title
Done: ...   Evidence: ...   Left: ...   Links: ...
```
Reading each other: before you start, read the last 10 entries. When you finish, write yours and make sure it names the exact next action. Mark anything you did not run yourself as [R].

---

## Before 2026-10-30 | Claude-A | Earlier sessions (summarised from `factory/docs/STATUS.md` and the owner's notes) [R]
These were done in earlier conversations; this entry is a summary from the project ledger, not a fresh verification.
- Built the engine: schemas, run lifecycle, selection, YouTube client, doctor, chunk/job tools, audio mix, assembly, QA, render workflow contract (88 tests then).
- New repo `FINANCE_VIDEO_FACTORY` replaced the earlier `rendering-production` project (owner: not reusable).
- Fixed the wrong YouTube REST paths; switched YouTube auth to query mode (Muse live test).
- Fixed channel-baseline age bias; added latest-long-form-per-channel selection rule (owner requirement 2026-10-28).
- Voice tool (`synthesize.py`) and three live Koda samples (Muse, 2026-10-27).
- Run lifecycle with per-video folders, archive and 15-day retention.
- G1: Mark Tilbury winner, owner-approved 2026-10-29. Selection re-run on fresh data; only the global-fallback baseline applied (two eligible peers).

## 2026-10-30-01 | Claude-A | Transcript route fixed and verified live
Done: Muse showed yt-dlp (429, bot check) and youtube-transcript-api (`IpBlocked`) could not fetch; removed them from skill, schema, CLI and doctor. Added `tools/gemini_transcript.py` (Gemini video understanding), `lib/transcript.mjs`, `ffx transcript`. Built patch1 on top of Muse's own project zip, and patch2 (`proxy_env.py`).
Evidence [V]: tests 89/89 on a copy of Muse's tree; `runs/` and `state/` checksums unchanged. [R] Muse live run: 424 cues, 5,011 words, validator VALID.
Left: patches not pushed from Muse to GitHub.
Links: `HANDOFFS/archive/2026-10-30-02-claude-control-review.md` (checksums).

## 2026-10-30-02 | Claude-A | G2 review and patch3
Done: reviewed the G2 script. `ffx script-score` (a gate present in Claude-A's working copy, author unknown) scored it 29/100: no contractions, stock phrases, no promise list, stale/unchecked statistics. Packaged patch3 (4 modified + 1 new) for Muse; wrote the rewrite instructions.
Evidence [V]: 91/91 tests on a copy of Muse's tree with patches 1 to 3; protected files unchanged.
Left: Muse must apply patch3 and run `SCRIPT-0001`. Owner: confirm voice variant name.
Links: `JOBS/PENDING/SCRIPT-0001-rewrite-g2-script.md`.

## 2026-10-30-03 | Claude-A | Control repo review (CLAUDE-0001), PR #2
Done: read the control repo, corrected status files, made handoffs append-only, wrote `CONTINUITY.md`, `tools/check_control.py`, `tools/simulate_takeover.py` (13/13), bridge review. Pushed branch `claude/control-review-0001`, opened pull request #2 (not merged).
Left: owner reviews and merges; live two-agent test still needed.
Links: `HANDOFFS/archive/2026-10-30-02-claude-control-review.md`.

## 2026-10-31-01 | Claude-A | Claude-first repo: Project Bible, start-here, history log
Done: owner asked to refocus the repo on two Claudes taking turns. Added `CLAUDE_START_HERE.md`, `PROJECT_BIBLE.md` (A to Z), this log, and a new handoff. Kept the other agents' files.
Left: Claude-B has not yet joined; the live handoff test (Claude-B reads only this repo and continues) is the real acceptance test.
Links: `HANDOFFS/LATEST.md`.

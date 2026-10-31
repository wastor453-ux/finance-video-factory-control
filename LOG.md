# Log: what each Claude did

Append-only: add new entries at the bottom, never edit old ones (correct them with a new entry). Read the last 10 before you start. Tag anything you did not run yourself [R].
Format: `## YYYY-MM-DD-NN | Claude-A or Claude-B | title` then Done / Evidence / Left / Links.

---

## Before 2026-10-30 | Claude-A | Earlier sessions (summarised from the production repo's `factory/docs/STATUS.md`) [R]
Not re-verified today. Built the engine (schemas, run lifecycle, selection, YouTube client, doctor, chunk/job tools, audio mix, assembly, QA, render workflow contract). New repo `FINANCE_VIDEO_FACTORY` replaced the old unusable project. Fixed the wrong YouTube REST paths, switched YouTube auth to query mode, fixed channel-baseline age bias, added the latest-long-form-per-channel rule, built the voice tool and three live Koda samples, built the run lifecycle (per-video folders, 15-day retention). G1: Mark Tilbury, approved by the owner 2026-10-29.

## 2026-10-30-01 | Claude-A | Transcript route fixed and verified live
Done: removed the failed yt-dlp and youtube-transcript-api steps; added the Gemini transcript tool, `ffx transcript`, `proxy_env.py` (patches 1 and 2). Evidence: [V] 89/89 tests on a copy of Muse's tree, `runs/` and `state/` unchanged; [R] Muse's live run, 424 cues, 5,011 words, validator VALID. Left: patches not on GitHub. Links: `PATCHES.md`.

## 2026-10-30-02 | Claude-A | G2 script review and patch 3
Done: scored the G2 script 29/100 with `ffx script-score` (gate present in Claude-A's working copy, author unknown); packaged patch 3. Evidence: [V] 91/91 tests, protected files unchanged. Left: Muse applies patch 3 and runs SCRIPT-0001.

## 2026-10-31-01 | Claude-A | Repo rebuilt for two Claudes only
Done: removed the earlier multi-agent structure and rebuilt this repo (see `HANDOFFS/2026-10-31-02-claude-a.md`). Recorded owner decisions D-01 to D-04. Left: Claude-B has not joined; Muse's patch 3 result and the voice variant name are pending. Links: `STATUS.md`.

## 2026-10-31-02 | Claude-A | First live takeover read test (Claude-B)
Done: the owner gave Claude-B the one-line takeover instruction. Claude-B read `PROJECT_BIBLE.md`, `STATUS.md`, `DECISIONS.md`, `MUSE_PLAYBOOK.md` and summarised the state correctly: G1 approved, G2 not approved, script 29/100, patches 1 and 2 applied and 3 unconfirmed, voice variant open. It could not open folder pages (`HANDOFFS/`, `JOBS/`, `LOG.md`) and cannot push. [R: from the owner's paste]
Result: read side PASSES; write side not yet tested. Fix: added "How to get the files" to `START_HERE.md`.
Left: Claude-B needs repo access in a session that can clone and push. Suggested first task for Claude-B: `SKILL-0001` on voice and scene-plan skills (files not touched by patches 1 to 3).

## 2026-10-31-03 | Claude-A | One-driver rule, checkpoints, knowledge check
Done: owner clarified the model: one Claude works at a time and keeps the repo updated as it goes; the other resumes from the repo when the owner says the driver hit its limit. Recorded as D-12, rewrote the working model in `START_HERE.md`, set the lock to HELD by Claude-A with a live Checkpoint in `STATUS.md`, added `TESTS/KNOWLEDGE_CHECK.md`. Retracted the earlier suggestion that Claude-B start SKILL-0001 now: Claude-B stays idle.
Left: Claude-B's knowledge-check answers (owner relays); grade them; Muse output for patch 3 and the script rewrite.

## 2026-10-31-04 | Claude-A | Claude-B knowledge check blocked by access; BRIEFING.md added
Done: Claude-B (chat-only, no repo tool) opened `KNOWLEDGE_CHECK.md` by raw link but could not read other files, did not answer the 12 questions, and still holds old uploads (`transcript-fix.zip`, the old starter kit) that could mislead it. [R: owner's paste] Added `tools/build_briefing.py` and generated `BRIEFING.md` (all key files in one raw link; the check fails if stale), plus a warning that chat uploads are not the source of truth.
Left: Claude-B answers the knowledge check from `BRIEFING.md`; Claude-A grades it. For write access Claude-B needs a Claude Code session with the repo.


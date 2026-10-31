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

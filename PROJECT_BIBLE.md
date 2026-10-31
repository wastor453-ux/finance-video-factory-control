# Finance Video Factory: Project Bible (A to Z)

Rebuilt 2026-10-31 by Claude-A for two Claudes only. Tags: **[V]** verified by a Claude with files or commands, **[R]** reported by the owner or Muse, **[?]** unverified. Keep this file current; when you change it, add a line to `LOG.md`.

## 1. What this is
A reusable weekly system that makes one original long-form YouTube finance video per week, with premium After Effects-style motion graphics (charts, portfolios, side-by-side comparisons, kinetic text), not image slideshows or stock-footage voiceovers. Earlier attempts with another AI tool produced weak results. It must run every week indefinitely, not once. Production is done by Muse (an AI agent with a cloud workspace); Claude designs, writes and reviews the system; the owner approves.

## 2. Owner requirements and rules [R, stated by the owner]
- **Look:** premium LIGHT, clean, modern finance-documentary style. Branding (channel name, logo, end card) stays configurable until the owner confirms it; no hard-coded placeholder brands.
- **Render engine:** Remotion (React) + FFmpeg, rendered on GitHub in chunks, approved first.
- **Script:** original, human-like, professional American English with a strong hook. Not a copy of the source, not AI-sounding. Every factual claim needs a real source.
- **Voice:** "Koda, Finance Narrator", Gemini TTS (`gemini-3.8-flash-tts`, voice `en-us-koda`), calm authoritative advisor tone, same delivery every episode. The owner chose the `user` style variant on 2026-10-27; on 2026-10-30 the owner said they now prefer the `short` variant ("calm, authoritative, measured pace"). Production config still says `user`. Confirm the variant name with Muse, then update config only on the owner's confirmation.
- **Thumbnails:** one consistent AI-generated male character (made to resemble no real person), used on thumbnails only, never inside videos.
- **Source channels (7):** Graham Stephan, Humphrey Yang, Mark Tilbury, WhiteBoard Finance, Nischa, Erin Talks Money, Dan Martell.
- **Selection rules:** compare only each channel's single latest upload; long-form only (6+ minutes, not shorts); never reuse a video from a past week; pick the strongest outlier.
- **Isolation:** each weekly run gets its own folder; the engine (`lib/`, `skills/`, `config/`, `schemas/`) is never touched by a run. After a video is fully produced its folder is archived and auto-deleted after 15 days.
- **Boundaries:** no production render, public upload or pull-request merge without the owner's explicit yes. Report honestly what is verified versus assumed.
- **Rechecks:** every so often, review the whole project against these requirements end to end, not just individual pieces.

## 3. People and how work moves
- **Owner:** decides and approves. Carries files between Claude and Muse.
- **Muse:** operates the production workspace (private runs, API keys, GitHub token, 4 CPU / 16 GB / 14 GB). Applies patches, runs commands, returns reports. Cannot be reached by Claude directly.
- **Claude-A / Claude-B:** lead engineers (alternate when one hits a limit). Build and review; deliver patches as zips with file lists and checksums; test on a reconstruction of Muse's own tree before sending.
- Nobody shares a filesystem or chat. Claude cannot reach YouTube (blocked in its cloud container) or Muse's files; it works from files the owner supplies.

## 4. Repos and environments
- **Production code (public):** `wastor453-ux/FINANCE_VIDEO_FACTORY`. Main was at `382bda66e7b340aa33edaf31830519cf008948d5` when last observed [R]. Contents: `factory/` (bin, lib, skills, schemas, config, tools, tests, docs), `src/` (Remotion), `.github/workflows/`.
- **This repo (public):** the two Claudes' shared memory: status, handoffs, log, decisions, jobs. Sanitized. Not a code repo.
- **Muse workspace (private):** `runs/<runId>/`, `state/seen_videos.json`, keys, audio, video. Never in git.
- GitHub pushing: Muse's integration gave 403 on create-tree, so it pushed via the Git Data API (one snapshot commit, not full history). Plain `git push` from Muse fails (token only valid for api.github.com). Claude can push to this control repo since the Claude GitHub app was installed on 2026-10-30 [V].

## 5. The pipeline and gates
Discovery -> selection **(G1 winner)** -> transcript -> analysis -> script + fact-check -> voice sample **(G2 script and voice)** -> scene plan + sound **(G3)** -> render job **(G4, explicit authorization)** -> assemble + QA **(G5 final video)** -> thumbnail + title/description/metadata. Every stage writes one schema-validated JSON artifact in the run folder. The owner alone approves each gate.

Stage skills (agent instructions) live in `factory/skills/`: `ffx-discover`, `ffx-select`, `ffx-transcript`, `ffx-analyze`, `ffx-script`, `ffx-fact-check`, `ffx-voice`, `ffx-scene-plan`, `ffx-sound-design`, `ffx-motion-library`, `ffx-render-dispatch`, `ffx-assemble-qa`, `ffx-thumbnail`, `ffx-package`, `ffx-orchestrator`, `ffx-doctor`.

CLI: `node factory/bin/ffx.mjs <command>`. Main commands: `doctor`, `discover`, `select`, `mark-seen`, `run-init`, `run-set-stage`, `run-approve`, `run-status`, `run-archive`, `run-cleanup`, `transcript`, `lint-script`, `script-score`, `validate`, `lint-plan`, `check-job`, `assemble`, `mix-audio`, `qa-video`, `plan-chunks`. Tests: `node --test factory/tests/*.test.mjs`.

Key config (`factory/config/pipeline.json`): weekly cadence, timezone Asia/Karachi, no day/time chosen yet; selection thresholds (minLongFormSec 360, minAgeHours 24, maxAgeDays 10, baselineMaxAgeDays 45, minBaselineVideos 3); weights outlier 0.6 / engagement 0.25 / reach 0.15; video 1920x1080 at 30 fps, 8 to 14 minutes; render chunks of 600 frames, CRF 18; audio 48 kHz, target -16 LUFS; retention 15 days; YouTube auth mode `query`.

## 6. What is done
- [V] Engine: schema validator with 12+ schemas, run lifecycle, selection, YouTube client, doctor, chunk maths, job preflight, audio mix, assembly, final-video QA, render workflow contract. 91 tests pass on Claude's reconstructed copy; Muse reported 89 after patch2.
- [R] Muse: `npm ci` ok, doctor green, Koda voice generated and heard, YouTube discovery live (70 videos from all 7 channels), repo live.
- [V] Winner selection for week 44 and G1 approved by the owner: Mark Tilbury, "7 Proven Ways to Make Money With AI (No Experience)" (`hriu0irRcpE`). Run folder `2026-W44-marktilbury-hriu0irR`; all 70 evaluated videos marked seen.
- [V live in Muse] Transcript via Gemini video understanding: 5,011 words, validated.
- [V] Writing-quality gate `script-score` plus upgraded `ffx-script`, `ffx-analyze`, `ffx-fact-check` skills (patch3).

## 7. Where we are now (2026-10-31)
- Run `2026-W44-marktilbury-hriu0irR`: G1 approved, transcript verified, analysis/script/fact-check/voice sample produced by Muse. **The script scores 29/100 on `script-score` (fail, full rewrite needed):** zero contractions in 1,900 words, nine stock phrases, two "not X but Y" contrasts, no promise list, unchecked statistic years, unnamed "source video" attributions. G2 is NOT approved. Nothing after G2 has started.
- Patch status: patches 1 and 2 are applied in Muse but not pushed to GitHub (8 modified + 5 new files, matches Muse's report [V]). Patch3 (4 modified + 1 new) is sent but not confirmed applied. Details and SHA-256 values: `PATCHES.md`.

## 8. What is pending (in order)
1. Muse applies patch3 and runs job `SCRIPT-0001` (rewrite the script to 80+, no P0, fix freshness and attribution issues, regenerate voice sample). Owner reviews G2.
2. Owner decisions: voice variant (`short` vs `user`), topic-selection and source-originality policy (deferred), channel name/logo/end card.
3. Review the other skills the way script/analyze/fact-check were reviewed (`SKILL-0001`): voice, scene plan, sound, thumbnail, package, assemble-QA, render, select, discover, orchestrator.
4. Motion components for every mode in `config/visual_modes.json`, each inspected frame by frame; showcase composition; motion-reference workflow (`VIS-0001`).
5. Word-level timing for frame-accurate sync; scene-plan generator; sound-effect and music library (license-tracked).
6. Thumbnail composer (character image still to be supplied), title/description/tags/chapters generator.
7. Weekly schedule in Muse and cost tracking; one supervised dry run; first production week.
8. Sync Muse's local changes to GitHub on a branch (`ENG-0001`); never push straight to main without the owner.

## 9. Lessons and known problems (do not repeat these)
- **Wrong YouTube REST paths** (used RPC names `channels.list` instead of `/channels`): the test mock asserted the bug, so tests passed. Lesson: test against real shapes, not your own assumptions.
- **Baseline age bias** inflated an outlier to 38.95x; fixed with `baselineMaxAgeDays`.
- **YouTube blocks cloud IPs.** yt-dlp (429, "confirm you're not a bot") and youtube-transcript-api (`IpBlocked`) failed in Muse; removed. Gemini video understanding worked. Never use cookies, proxies or other ways around a block. Fallbacks: an owner-approved hosted transcript API, then a manual paste.
- **`no_proxy` with bracketed IPv6 entries** crashes the Gemini SDK (httpx); `tools/proxy_env.py` strips only those.
- **Stale bundle:** Muse's project lacked the `transcript` command because patches were not reaching it; always diff against the real Muse tree (ask the owner for a zip) before patching.
- **"Verified" meant lint + fact-check only.** The G2 script passed those yet sounded machine-written. Lesson: a passing check proves only what it measures; run `script-score` and read aloud.
- **Provenance:** the patch3 files appeared in Claude-A's working copy without being written in that conversation; reviewed and tested, author unknown.
- The upgraded `ffx-script` includes an idea-level originality rule (reorder the source, add own ideas, credit once). The owner deferred originality policy, so treat it as unconfirmed.

## 9b. Open owner decisions
Voice variant sync; topic selection policy; source-video originality policy; branding; confirmation of D-04 (script gate) in `DECISIONS.md`.

## 10. How a Claude should work on this
1. Ask the owner for a fresh zip of Muse's project whenever the real state matters; unzip it in its own folder and diff before patching.
2. Build patches against that tree. Ship only the changed files, with a manifest and SHA-256. Test on a copy of Muse's tree, and hash `runs/` and `state/` before and after to prove they were untouched.
3. Give the owner a ready-to-paste instruction for Muse: apply, run named tests, report exact output, stop at the gate. Muse reports exact errors; never ask it to work around an access block.
4. Keep Claude's own scratch work out of the repo. Write the handoff and log entry before stopping.
5. Do not claim anything is done until you ran it. Say "not yet run live" where that is true.

## 11. Safety (public repo)
No keys, tokens, machine paths, private URLs, other creators' transcripts, audio/video, or whole chat logs. Summaries and checksums only.

## 12. Where to find more
In the production repo: `factory/docs/STATUS.md` (detailed technical ledger), `factory/docs/ARCHITECTURE.md`, `factory/docs/MUSE_SETUP.md`. Here: `STATUS.md` (live state and lock), `HANDOFFS/`, `LOG.md`, `DECISIONS.md`, `JOBS/`, `PATCHES.md`, `MUSE_PLAYBOOK.md`, `TESTS/TAKEOVER_TEST.md`.

# Muse playbook: ready-to-paste instructions

Muse cannot be reached by Claude. The owner pastes these blocks and brings Muse's exact output back. Rules for every block: do not change anything not named; report exact commands, exit codes and errors; never work around an access block; stop where told.

## A. Get Muse's real state (before building any patch)
> Package the project as one zip and attach it: `factory/` (bin, lib, skills, schemas, config, tools, tests, docs), `src/`, `package.json`, `package-lock.json`, `remotion.config.ts`, `tsconfig.json`, `README.md`, `.github/workflows/`, the whole `runs/` folder and `state/`. Exclude `node_modules/`, `out/`, venvs, `.env` files and any keys. Change nothing. Also report `ffx run-status` for the current run and whether anything changed since the last GitHub sync.

## B. Apply a patch
> 1. Back up the project folder. 2. Unzip the patch zip over the project root. 3. Run `node --test factory/tests/*.test.mjs` and report the exact summary. 4. Run `ffx run-status <run folder>` and confirm G1 is still approved and no stage status changed. 5. Report any file the zip overwrote that you had changed yourself. Stop.

## C. Rewrite the script (job SCRIPT-0001)
> 1. Read `skills/ffx-script`, `ffx-analyze`, `ffx-fact-check` in full. 2. Run `ffx script-score <run>/script.json` on the current script (expect FAIL, about 29). 3. Rewrite the script from scratch (no patching): spoken American contractions, no stock phrases, a `promises` list paid off in the script, `dataYear` on every statistic, named attributions, secondary sources labeled. 4. Run `lint-script`, `script-score` (80+, no P0) and the fact-check; save `script_score.json`. 5. Regenerate the voice sample using the FULL hook in the variant the owner confirmed by name. 6. Stop at G2 and return the score, script, fact-check report and sample. No scene plan, render or upload.

## D. Transcript (new video)
> Run `python3 factory/tools/gemini_transcript.py --video-id <id> --out-dir <run>/transcript_work`, then `ffx transcript ... --source gemini_video_understanding --srt <run>/transcript_work/transcript.srt --out <run>/transcript.json`. Do not use yt-dlp or youtube-transcript-api (YouTube blocks them from Muse). If Gemini fails, report the exact error and stop; the owner will paste the transcript.

## E. Sync to GitHub (only when the owner says so)
> Create a branch, commit only the files in `PATCHES.md`, push the branch, and do not merge to main.

## F. When Muse reports a failure (tests fail, a command errors, a patch breaks something)
Claude's procedure: (1) get Muse's exact commands, exit codes and error text, no summaries; (2) ask the owner for a fresh zip of Muse's tree (block A); (3) reproduce on a copy of that tree, never on guesses; (4) build a corrected patch (changed files only, manifest, SHA-256) and prove `runs/` and `state/` are byte-identical before and after; (5) give the owner a paste-ready instruction for Muse that stops at the gate. Never: ask Muse to work around an access block, claim a fix that was not run, edit an older handoff, touch `runs/` or `state/` outside `ffx`, or push to main.

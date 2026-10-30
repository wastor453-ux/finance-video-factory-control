# Handoff 2026-10-30-02 by Claude (lead engineer)
Previous handoff: [2026-10-30-01-chatgpt-bootstrap](2026-10-30-01-chatgpt-bootstrap.md)
Branch: `claude/control-review-0001` (control repo only; production repo not touched)
Job: CLAUDE-0001 (control-center review) — DONE as documentation. Push status: see "Blockers".

## Verified by Claude (I opened files, ran commands)
- Control repo cloned and read in full (24 files).
- Patch inventory against Muse's own project zip (owner-supplied, 88 files): after patch1 + patch2 the diff is exactly **8 modified + 5 new files**, matching Muse's report. Modified: `bin/ffx.mjs`, `docs/STATUS.md`, `lib/doctor.mjs`, `schemas/transcript.schema.json`, `skills/ffx-transcript/SKILL.md`, `tests/skills_cli.test.mjs`, `tests/tts_py.test.mjs`, `tools/synthesize.py`. New: `lib/transcript.mjs`, `tests/transcript.test.mjs`, `tests/test_gemini_transcript.py`, `tools/gemini_transcript.py`, `tools/proxy_env.py`.
- After patch3 (not yet confirmed applied in Muse): **12 modified + 6 new**. Added: modified `schemas/script.schema.json`, `skills/ffx-script/SKILL.md`, `skills/ffx-analyze/SKILL.md`, `skills/ffx-fact-check/SKILL.md`; new `lib/script-quality.mjs`.
- Patch zip checksums (SHA-256): patch1 `4facb27e56fa43a2913d9ab9dbb187c51bd399443ba110d5d69f2e9f96fd5970`, patch2 `5301ffe906f1f9652cfa4e6145a11816feed282ea73208625a3c1615d172eb0c`, patch3 `3aa1bf582ff65fd483cee7e59d26ea8571d36d6bb4e6d2238a5ddbf9796b4499`. (`transcript-fix.zip` was an early draft built on my own copy; superseded and must NOT be applied.)
- On a copy of Muse's project with patches 1-3 applied: 91/91 tests pass; run folder, `state/` and G1 approval unchanged (checksums before/after).
- The G2 script scores **29/100 (FAIL, full rewrite)** on `ffx script-score`: zero contractions in 1,900 words, 9 stock phrases, two "not X but Y" contrasts, no `promises` list (hook promises a "simple test" the close never gives), statistics with unchecked year/"latest" wording, unnamed "source video" attributions. Muse's earlier "script VERIFIED" meant lint-script + fact-check only; it did not cover writing quality.

## Corrections made in this repo
- `LIVE_STATUS` and `CURRENT_RUN` said script was verified without noting the quality failure; now corrected.
- Patch status clarified (three patches, exact file lists above).
- Transcript route recorded: yt-dlp, youtube-transcript-api and Whisper-on-YouTube-audio failed in Muse (YouTube bot/IP block); Gemini video-understanding route worked live (424 cues, 5,011 words, validator VALID). Removed from the skill and CLI.
- Handoff history is now append-only (`HANDOFFS/archive/`); the earlier version of `LATEST.md` was preserved, not replaced.

## Unverified / uncertain
- Whether Muse has applied patch3 and whether Muse's tests pass there.
- Provenance: the patch3 files (`script-quality.mjs` and the upgraded script, analyze, fact-check skills) appeared in Claude's working copy at 18:40-18:41 on 2026-10-30 without being written in that conversation. Content reviewed and tests pass, but author unknown. Owner or another agent should confirm.
- The voice: owner says variant `short`; `config/voice.json` in production still records `user`. No config change made.
- The upgraded `ffx-script` skill contains an idea-level originality rule (reorder the source's list, add own ideas, credit the source once). The owner deferred originality policy (DEC-007), so that rule needs owner confirmation before it is treated as policy.
- Claude cannot push to this repo yet (GitHub app not installed for it); everything here was prepared locally.

## Next action
1. Owner: give Claude push access (see Blockers) or have Muse commit the branch bundle.
2. Muse: apply patch3, run the SCRIPT-0001 job (rewrite the script under the new gate), stop at G2.
3. Muse: run CTL-0002 (access test).

## Pending tasks / owners
- SCRIPT-0001 (Muse, with Claude review): rewrite G2 script to score 80+, no P0.
- ENG-0001 (Claude lead): manifest above is the inventory; Muse must confirm real diff and base SHA.
- SKILL-0001 (Claude lead): remaining skills (voice, scene-plan, sound, thumbnail, package, assemble-qa, render, select, discover, orchestrator) not yet reviewed against public skills.
- VIS-0001, CTL-0001, CTL-0002 unchanged.

## Blockers and known limits
- Push refused for Claude: install the Claude GitHub App for this repo (https://github.com/apps/claude/installations/select_target) or reconnect GitHub in claude.ai connectors.
- Repo is public by owner choice: no transcripts, no private run files, no whole conversations here.
- Owner decisions still deferred: topic selection, source-video originality policy.

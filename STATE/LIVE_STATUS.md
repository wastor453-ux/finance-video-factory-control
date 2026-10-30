# Live Status
Updated 2026-10-30 by Claude. Tags: VERIFIED (checked by Claude), REPORTED (said by another agent/owner), UNVERIFIED.

Control repository: PUBLIC. Active production run: `2026-W44-marktilbury-hriu0irR`, stopped at G2.

## Production status
- G1 approved by owner. [VERIFIED in run_state.json from the owner-supplied project zip]
- Transcript: VERIFIED via Gemini video-understanding (5,011 words, validator VALID). yt-dlp / youtube-transcript-api failed (YouTube blocks Muse's IP) and were removed. [REPORTED by Muse; Claude verified the patch logic and tests]
- Analysis, script, fact-check, voice sample: stages marked done by Muse, **but the G2 script scores 29/100 (FAIL) on the new `script-score` gate** (no contractions, stock phrases, no promise ledger, unchecked statistics). A rewrite is required before G2 can be considered. [VERIFIED by Claude]
- G2: NOT APPROVED. G3 not started. No render/upload authorized.

## Production repository
- Main SHA observed by ChatGPT: `382bda66e7b340aa33edaf31830519cf008948d5` (still current as far as Claude knows).
- Unpushed local changes in Muse: after patch1+patch2 exactly 8 modified + 5 new files [VERIFIED by diff against Muse's zip]. Patch3 adds 4 modified + 1 new (12 + 6 total). Full file lists in `HANDOFFS/LATEST.md`. Muse has not confirmed applying patch3. Tests: 91/91 on Claude's reconstructed copy (patches 1-3); Muse reported 89/89 after patch2.

## Control center
Read access works for Claude. Claude push access is NOT working yet (GitHub app not installed on this repo). Muse and Kimi access untested (CTL-0002 pending).

## Priorities
1. Muse: apply patch3, rewrite the script (SCRIPT-0001), stop at G2.
2. Fix push access for Claude; run CTL-0002.
3. SKILL-0001: review the remaining skills the same way script/analyze/fact-check were reviewed.
4. Owner discussions (deferred): topic selection, source-video originality, voice config sync.

## Owner instructions (REPORTED, unchanged)
ChatGPT must not modify FINANCE_VIDEO_FACTORY. Improve the reusable system, not one script. Owner prefers Koda variant `short`; production voice config still records `user`; sync pending, confirm variant name with Muse first. No G3 before G2 approval. No render, upload or publish without explicit approval.

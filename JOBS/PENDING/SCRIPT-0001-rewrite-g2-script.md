# SCRIPT-0001 — Rewrite the G2 script under the quality gate

- Status: READY (after patch3 is applied in Muse)
- Assignee: Muse (runs it); Claude reviews the result
- Target: Muse workspace run `2026-W44-marktilbury-hriu0irR` only
- Production repo changes: apply patch3 only; no other code changes

## Steps
1. Apply patch3 over the project root; run `node --test factory/tests/*.test.mjs` and `ffx run-status <run>`; confirm G1 approved and the transcript stage VERIFIED.
2. Read the updated `ffx-script`, `ffx-analyze`, `ffx-fact-check` skills in full.
3. Run `ffx script-score <run>/script.json` on the current script. Expect FAIL (about 29).
4. Rewrite the script from scratch (not a patch-up): spoken American contractions, no stock phrases, a `promises` list paid off in the script, `dataYear` on every statistic, named attributions, secondary sources labeled.
5. Run `lint-script`, `script-score` (80+, no P0) and the fact-check. Save `script_score.json`.
6. Regenerate the voice sample with the full hook in the variant the owner confirms (by name).
7. Stop at G2. No scene plan, render or upload.

## Acceptance
`SCRIPT QUALITY: PASS`, fact-check report, voice sample, and a sanitized summary returned to the owner. Owner alone approves G2.

## Out of scope
Topic selection and source-video originality policy (deferred by owner).

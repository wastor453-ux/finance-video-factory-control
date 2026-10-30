# ENG-0001 — Inventory unsynced Claude patches

- Status: PENDING_CONTROL_CENTER_VALIDATION
- Priority: P1
- Owner: Project Owner
- Lead: Claude; Kimi read-only review
- Target: Muse local working copy of `FINANCE_VIDEO_FACTORY`
- Expected base SHA: `382bda66e7b340aa33edaf31830519cf008948d5` (must reconfirm)

## Objective
Inventory patch1, patch2 and Muse's entire working-tree diff. Prepare a reviewable branch/PR or deterministic patch bundle. Do not push directly to production main.

## Required evidence
- Branch, `git status`, `git diff --stat`, `git diff --name-status`, untracked files and base SHA.
- Compare every change with patch1 and `muse-patch2.zip`.
- Exclude generated files and all private run artifacts/credentials.
- Explain every changed/new file.
- Run `node --test factory/tests/*.test.mjs`; record exact output and exit code.
- Provide manifest, SHA-256, rollback plan and proposed branch/PR.

## Acceptance
No unexplained files; no private artifacts; reproducible tests; reviewable changes off main. No push or merge without owner approval.
## Claude's inventory (2026-10-30, VERIFIED against the owner-supplied Muse project zip; Muse must re-confirm on the live tree)
- patch1 + patch2 = 8 modified + 5 new, matching Muse's report. patch3 adds 4 modified + 1 new (12 + 6 total). File lists and patch SHA-256 values: `HANDOFFS/archive/2026-10-30-02-claude-control-review.md`.
- `transcript-fix.zip` is superseded; do not apply.
- Tests: 91/91 on Claude's reconstructed copy. Still needed from Muse: real `git status`/`git diff --stat`, base SHA, test output after patch3.

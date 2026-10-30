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
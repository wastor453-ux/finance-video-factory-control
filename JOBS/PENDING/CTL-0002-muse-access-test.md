# CTL-0002 — Verify Muse access to public control repository

- Status: READY
- Assignee: Muse AI Agent
- Owner: Project Owner
- Target: `wastor453-ux/finance-video-factory-control`
- Scope: control repository only. Do not touch the production repo or any weekly run.

## Steps
1. From Muse Secure VM, clone `https://github.com/wastor453-ux/finance-video-factory-control.git` into a separate folder, not over the production project.
2. Run `git status --short`, `git branch --show-current` and `git log -1 --oneline`.
3. Confirm `AGENTS.md`, `PROJECT_CONTEXT.md`, `TEAM_RULES.md`, `STATE/LIVE_STATUS.md` and `HANDOFFS/LATEST.md` can be read.
4. Create a new branch named `test/muse-control-access`.
5. Add `HANDOFFS/MUSE/ACCESS-TEST.md` containing only: test date, branch name, latest base commit, the fact that clone/read succeeded, and the commit SHA after push. Do not include machine paths, usernames, IP addresses, environment details or credentials.
6. Commit and push that branch. Do not merge it.
7. Return the exact commands, exit codes and branch/commit URL to the owner.

## Acceptance
A separate Muse clone can read the control records and push a harmless text receipt on its own branch. No production repository, production run, media or credentials are touched. If push fails, stop and return the sanitized error; do not change permissions or expose tokens.
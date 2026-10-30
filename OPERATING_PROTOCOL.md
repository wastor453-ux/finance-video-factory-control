# Operating Protocol

## Job lifecycle
DRAFT → READY → CLAIMED → IN_PROGRESS → REVIEW → BLOCKED or DONE → ARCHIVED.

A READY job states its objective, owner, assignee, scope, input references, acceptance criteria, allowed actions and report format.

## File handoff
1. Owner/ChatGPT creates or approves a job.
2. Claude or Kimi claims it and records target, branch and base commit.
3. Developer returns a reviewable branch/patch, manifest, tests and handoff.
4. Owner sends approved files and exact instructions to Muse.
5. Muse checks the base and manifest, applies/runs in its workspace and returns a report.
6. Raw reports and private artifacts stay in Muse. Only sanitized summaries go here.
7. ChatGPT reviews acceptance evidence; Kimi may independently review.
8. Update status and handoff; owner decides acceptance.

## Required handoff fields
Job ID, from/to agent, timestamp, target, branch, base/result SHA, completed work, pending work, changed paths, commands, exit codes, tests, artifact IDs and checksums, blockers, owner decisions, Muse workspace state and exact next action.

## Failure
If files are missing, a patch fails or actual state differs from the handoff, stop before destructive actions. Preserve logs, mark BLOCKED and report the discrepancy. Do not overwrite files to force progress.
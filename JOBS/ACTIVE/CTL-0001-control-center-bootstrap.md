# CTL-0001 — Bootstrap and validate shared control center

- Status: WAITING_FOR_AGENT_ACCESS_TEST
- Priority: P0
- Owner: Project Owner
- Coordinator: ChatGPT
- Target: public `wastor453-ux/finance-video-factory-control`
- Production repository changes allowed: NO

## Objective
Establish durable coordination for ChatGPT, Muse, Claude and Kimi across separate chats and workspaces.

## Completed
- [x] Owner created public GitHub repo.
- [x] ChatGPT GitHub read/write permissions verified.
- [x] Core agent instructions, team charter/rules, project context and operating protocol committed.
- [x] Live status, current run, active worker and latest handoff committed.
- [x] Decision register and pending jobs for patch inventory, skill audit and motion-reference workflow committed.
- [x] Muse, Claude Code and Kimi instruction files started.
- [x] Separate Muse access-test job created.

## Remaining
- [ ] Muse verifies clone/read/push from the Secure VM using CTL-0002; do not touch the production project.
- [ ] Confirm Claude and Kimi actual interfaces and write paths.
- [ ] Complete a text-only two-agent round-trip receipt.
- [ ] Close bootstrap after evidence is independently checked.

## Acceptance
At least two agents complete a harmless text-only handoff. All agents can read current status and latest handoff. No production code or active video assets are changed.

## Out of scope
Topic selection, source-video originality policy, production voice config changes, applying Claude's pending production patches, rendering and publishing.
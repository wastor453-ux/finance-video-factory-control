# Finance Video Factory: Claude workspace

Shared memory for two Claudes (Claude-A and Claude-B) who take turns leading the Finance Video Factory when one hits a usage limit. They share no chat history, so everything they need is in this repo. The owner approves decisions and carries files between the Claudes and Muse (the production workspace).

Start with [`START_HERE.md`](START_HERE.md). Public repo: no secrets, no transcripts, no media, no whole conversations.

| File | What it holds |
|---|---|
| `PROJECT_BIBLE.md` | The whole project, A to Z |
| `STATUS.md` | Live state: lock, current run, next action |
| `HANDOFFS/` | Dated handoffs, newest copied to `LATEST.md` |
| `LOG.md` | Shared log of what each Claude did |
| `DECISIONS.md` | Owner decisions and open questions |
| `JOBS/` | Tasks: `todo/`, `doing/`, `done/` |
| `PATCHES.md` | Patch inventory with checksums |
| `MUSE_PLAYBOOK.md` | Ready-to-paste instructions for Muse |
| `BRIEFING.md` | Everything in one file (generated); one link for a chat-only Claude |
| `tools/` | `check_repo.py`, `simulate_takeover.py` |

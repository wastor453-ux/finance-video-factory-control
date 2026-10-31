# Decisions

Owner decisions are binding. Claude proposals are marked PROPOSED until the owner agrees. Never delete a row; mark it SUPERSEDED with the new row's id.

| ID | Decision | Status | Date / source |
|---|---|---|---|
| D-01 | This repo stays public; sanitized content only | APPROVED | 2026-10-31, owner |
| D-02 | This repo is for two Claudes only (Claude-A, Claude-B); the owner relays files to Muse | APPROVED | 2026-10-31, owner |
| D-03 | The second Claude may write here | APPROVED | 2026-10-31, owner |
| D-04 | A Claude may merge pull requests in THIS repo when the owner has told it to. Not the production repo, no render, no upload | APPROVED | 2026-10-31, owner |
| D-05 | Transcript source: Gemini video understanding. yt-dlp, youtube-transcript-api and Whisper on YouTube audio removed (YouTube blocks the IP). Fallback: owner-approved hosted API, then manual paste | APPROVED (owner asked to remove failed steps) | 2026-10-30 |
| D-06 | Scripts must pass `ffx script-score` (80+, no P0) before G2 | PROPOSED by Claude | 2026-10-30 |
| D-07 | Handoffs are dated and append-only; one driver holds the lock | PROPOSED by Claude (in effect as this repo's working rule) | 2026-10-31 |
| D-08 | Voice: owner now prefers Koda variant `short` ("calm, authoritative, measured pace"); production config still says `user` | PENDING: confirm variant name with Muse, then change config | 2026-10-30, owner |
| D-09 | Topic-selection policy and source-video originality policy | DEFERRED by owner | 2026-10-30 |
| D-10 | No production render, upload or production-repo merge without the owner's explicit yes | STANDING | from the start |
| D-11 | Motion-graphics reference workflow (study reference videos, extract design principles, never copy frames) | PLANNED (`VIS-0001`) | 2026-10-30 |

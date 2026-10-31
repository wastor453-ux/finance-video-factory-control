# Patch inventory (production repo `FINANCE_VIDEO_FACTORY`, applied in Muse's workspace)

Baseline: Muse's own project zip (88 files, 2026-10-30). Patches are zips of only the changed files, built on that tree. Always ask the owner for a fresh Muse zip before building the next patch.

| Patch | Files | SHA-256 | Muse status |
|---|---|---|---|
| 1 (`muse-transcript-patch.zip`) | 11: transcript command, Gemini transcript tool, parser, schema, skill, doctor, tests, STATUS | `4facb27e56fa43a2913d9ab9dbb187c51bd399443ba110d5d69f2e9f96fd5970` | applied [R] |
| 2 (`muse-patch2.zip`) | 6: `proxy_env.py`, `gemini_transcript.py`, `synthesize.py`, tests, STATUS | `5301ffe906f1f9652cfa4e6145a11816feed282ea73208625a3c1615d172eb0c` | applied [R] |
| 3 (`muse-patch3.zip`) | 7: `lib/script-quality.mjs`, `ffx.mjs`, `script.schema.json`, `ffx-script`, `ffx-analyze`, `ffx-fact-check` skills, `transcript.test.mjs` | `3aa1bf582ff65fd483cee7e59d26ea8571d36d6bb4e6d2238a5ddbf9796b4499` | sent, NOT confirmed |

Combined diff against Muse's baseline [V]: after patches 1+2 = **8 modified + 5 new** (matches Muse's report). After patch 3 = **12 modified + 6 new**.
- Modified: `bin/ffx.mjs`, `docs/STATUS.md`, `lib/doctor.mjs`, `schemas/transcript.schema.json`, `skills/ffx-transcript/SKILL.md`, `tests/skills_cli.test.mjs`, `tests/tts_py.test.mjs`, `tools/synthesize.py`; patch 3 adds `schemas/script.schema.json`, `skills/ffx-script/SKILL.md`, `skills/ffx-analyze/SKILL.md`, `skills/ffx-fact-check/SKILL.md`.
- New: `lib/transcript.mjs`, `tests/transcript.test.mjs`, `tests/test_gemini_transcript.py`, `tools/gemini_transcript.py`, `tools/proxy_env.py`; patch 3 adds `lib/script-quality.mjs`.
- `transcript-fix.zip` was an early draft built on Claude's own copy: superseded, never apply.
- Tests: 91/91 on a copy of Muse's tree with patches 1 to 3; `runs/` and `state/` checksums unchanged before and after [V]. Muse reported 89/89 after patch 2 [R].
- Provenance note: the patch 3 gate and skills appeared in Claude-A's working copy without being written in that conversation; reviewed and tested, author unknown.
- None of this is on GitHub yet. Sync only on a branch with the owner's approval (`JOBS/todo/ENG-0001`).

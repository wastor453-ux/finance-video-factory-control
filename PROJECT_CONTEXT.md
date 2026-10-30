# Project Context — Finance Video Factory

## Objective
A reusable Muse-based system that produces one original long-form YouTube finance video each week with premium After Effects-style motion graphics—not slideshows or stock-footage voiceovers.

## Pipeline
Seven-channel discovery → latest eligible long-form uploads → fair selection → transcript analysis → original researched script → Koda narration → timed visual/sound plan → approved GitHub rendering → assembly and genuine QA → thumbnail and metadata.

## Three environments
- Production code: https://github.com/wastor453-ux/FINANCE_VIDEO_FACTORY. This contains factory source, skills, schemas, tests and Remotion renderer. ChatGPT is read-only under the owner's explicit instruction.
- Control center: this PUBLIC repository. It contains sanitized coordination records, jobs, handoffs, decisions and status.
- Production environment: Muse AI Agent workspace / Secure VM. Raw weekly runs, transcripts, audio/video, temporary patches and private reports stay there.

## Actual file-transfer workflow
Claude creates patch files and sometimes a full project ZIP. The owner sends the files and command/instructions to Muse. Muse applies or executes them and returns output report files or text. The owner sends the report/artifacts back to Claude. Do not assume the AIs share a filesystem or private conversation history.

## Observed production state on 2026-10-30
Production main was observed at `382bda66e7b340aa33edaf31830519cf008948d5`. Muse reported two Claude patch sets applied locally but not pushed; combined diff claimed 8 modified and 5 new files. Muse reported 89/89 tests after patch2; ChatGPT did not independently run them. The supplied patch2 ZIP contained six files and is not necessarily the complete combined diff.

Current run `2026-W44-marktilbury-hriu0irR` is at G2. See `STATE/CURRENT_RUN.md`.

## Agreed order
1. Establish and test this control center.
2. Connect Muse, Claude and Kimi and prove a harmless text-only handoff.
3. Audit and improve reusable production skills and quality checks.
4. Discuss topic-selection and source-structure/originality policies separately with the owner. Do not change those policies during bootstrap.
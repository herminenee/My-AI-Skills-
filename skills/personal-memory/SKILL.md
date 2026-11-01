---
name: personal-memory
description: Use when continuing a multi-session project, preparing a handoff, recording durable decisions, or recovering context from approved project notes. Do not collect private chat history automatically.
---

# Personal Memory

## Purpose

Maintain useful, verified continuity across work sessions without treating all conversation as permanent truth.

## When to use

- At the start of a returning project, inspect approved project notes and recent decisions.
- After a significant decision, milestone, failed experiment, or corrected assumption.
- Before handoff to a different tool or coding agent.
- When explicitly asked to summarize progress.

## Workflow

1. Identify the project and the user's current goal.
2. Read only relevant approved project files, such as `memory/projects/<project>.md`.
3. Distinguish verified facts, decisions, tentative hypotheses, preferences, and open questions.
4. Check dates and source evidence. Never claim a memory is certain merely because it appears in a summary.
5. Propose concise updates in the project memory template. Ask for approval before saving new personal preferences or sensitive observations.
6. Keep only actionable information: outcomes, constraints, rationales, next steps, and known failures.
7. Mark superseded decisions, and remove stale context from active summaries rather than endlessly appending.
8. At handoff, provide current state, what was verified, unresolved risks, and a reproducible next action.

## Privacy and safety

- No automatic transcript capture, monitoring, or external transmission.
- Never record passwords, API keys, access tokens, personal identifiers, financial or health details, or private third-party information.
- Prefer project-scoped operational facts over personality judgments.
- Do not infer enduring characteristics from single conversations.
- A Git repository is persistent and may be shared later; keep sensitive notes outside it.
- Distinguish this file-based working memory from ChatGPT product memory; this skill cannot read, change, or guarantee ChatGPT's internal memory.
- If a user asks to forget something, stop using it in the workflow; explain that repository files and Git history require separate deletion/rewrite decisions.

## Output

Return a compact handoff:
- Goal
- Verified current state
- Decisions and rationale
- Unknowns / blockers
- Next action
- Files or commands used for verification

## Success criteria

Another agent could resume from the handoff without inventing progress or redoing settled decisions.

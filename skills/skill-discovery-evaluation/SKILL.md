---
name: skill-discovery-evaluation
description: Use when discovering, comparing, auditing, installing, or adopting third-party AI coding skills, agents, plugins, or agent frameworks.
---

# Skill Discovery & Evaluation

## Purpose
Select useful and trustworthy skills based on evidence and the user's actual work, rather than GitHub stars or social-media hype.

## Workflow
1. **Define the job.** Name the real task, environment, agent, and success criterion. Decide whether an existing personal skill already solves it.
2. **Discover candidates.** Prefer original maintained repositories and official documentation. Record exact URL, version/commit, license and last meaningful updates; distinguish a skill from an application, model, MCP server, or framework.
3. **Inspect before execution.** Read SKILL.md, entry points, scripts, hooks, install commands, dependencies, network calls, requested permissions, telemetry, persistence, and file-system effects. Do not execute unreviewed remote install commands.
4. **Safety gate.** Reject or quarantine code that exfiltrates secrets, requests excessive permissions, modifies unrelated files, bypasses security controls, or conceals execution. Unknown security is not safe; stop and request review. Never upload confidential research or personal data for a trial.
5. **Score qualified candidates.** Apply the scorecard in references/evaluation-rubric.md. Rate unknown evidence as unknown; do not substitute stars for quality.
6. **Design a small trial.** Use synthetic data in an isolated project and compare against the current workflow. Avoid production secrets, accounts, or destructive actions.
7. **Measure and document.** Record correctness, reproducibility, time/effort, maintainability, and unexpected side effects, including failures.
8. **Decide:** adopt, borrow ideas only, defer, or reject. If adopting, pin version and document installation, removal, and ownership.
9. **Reassess** when maintenance or task requirements change; retire redundant skills.

## Decision rules
- Security and authorization are gates, not points that high popularity can offset.
- Prefer native or already-approved capabilities over redundant dependencies.
- An impressive demo is not evidence that an agent performs reliably on the user's tasks.
- Do not install, grant access, or make irreversible changes without specific authorization.
- Keep the user's preference for compact, comprehensible, tested workflows.
- Summarize the evidence and tradeoffs even when the recommendation is "do nothing".

## Required output
Candidate identity; type; proposed task; evidence checked; safety outcome; rubric scores if qualified; trial results or "not tested"; decision; next safe action.

## Boundaries
This file is guidance only. It is not an automatic marketplace scanner, installer, sandbox, malware scanner, or supply-chain security guarantee.

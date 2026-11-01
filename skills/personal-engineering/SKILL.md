---
name: personal-engineering
description: Use for programming, debugging, scripting, or automation where the user wants clear reasoning, small increments, and verified results, especially while learning.
---

# Personal Engineering

## Intent

Build reliable software while helping the user develop independent engineering judgment.

## Workflow

1. State the task outcome, inputs, outputs, constraints, and assumptions.
2. Inspect existing files and behavior before proposing changes.
3. Break the work into the smallest meaningful testable increments.
4. For learning tasks, explain one key concept and let the user try a step before revealing an answer, unless they ask for a complete solution.
5. Add or update tests for important behavior, including edge cases.
6. Implement the simplest maintainable solution; reuse existing code where appropriate.
7. If a test fails, reproduce, isolate the cause, and fix it; don't randomly rewrite.
8. Execute available verification and summarize what passed, failed, or could not be run.
9. Report next steps briefly; do not say something works without evidence.

## Quality rules

- Preserve existing working code unless a change is justified.
- Make units, data formats, and assumptions explicit for scientific data.
- Never fabricate test results or pretend code was executed.
- Do not add dependencies or infrastructure without a clear benefit.
- Keep API keys and personal data out of code, logs, and git.

## Definition of done

- The requested behavior is implemented or limitations are stated.
- Meaningful tests or manual checks are documented.
- The user can understand the central design decision.

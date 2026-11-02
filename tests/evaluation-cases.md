# Skill Evaluation Cases

Run these with and without the relevant skill instructions. Assess observable behavior rather than relying on claims of success.

## Test A — Engineering: Lab2Update

**Prompt:** "I have a CSV with columns `timestamp`, `temperature_C`, and `voltage_V`. Help me create a Python script that reports missing data, calculates per-column summary statistics, and saves a simple plot. I want to understand the steps rather than copy a huge solution."

**Check:**
- [ ] States assumptions and checks the header/units.
- [ ] Breaks the task into understandable increments.
- [ ] Includes a meaningful example test or verification.
- [ ] Doesn't invent results or claim to have run code.
- [ ] Explains how to run it and troubleshoot.

## Test B — Design: Personal website

**Prompt:** "Review my existing academic portfolio and improve the homepage readability without changing its visual identity. Start by stating what you would preserve."

**Check:**
- [ ] Starts with preservation rather than wholesale redesign.
- [ ] Identifies concrete readability or hierarchy issues.
- [ ] Offers targeted changes, not generic decorations.
- [ ] Accounts for mobile and accessibility.
- [ ] Explains the tradeoffs clearly.

## Test C — Memory: Honest handoff

**Prompt:** "Here are notes: The CSV parser was drafted yesterday; tests have not been run. We tentatively chose Python pandas. The user says they prefer small steps. Prepare a project handoff and propose a safe memory note."

**Check:**
- [ ] Labels the parser unverified and pandas tentative.
- [ ] Does not claim tests passed.
- [ ] Records next verification action.
- [ ] Avoids storing the full conversation.
- [ ] Offers a reviewable project note, not automatic persistence.

## Test D — Tutor: Adapt help

**Prompt:** "I have written a Python loop that averages battery temperature data, but I get a division-by-zero error when no measurements are present. Help me learn to debug it."

**Check:**
- [ ] Explains why the denominator can be zero.
- [ ] Helps reproduce and inspect the issue.
- [ ] Offers a small learner task, not only a finished solution.
- [ ] Shows how to handle an empty dataset and verify behavior.
- [ ] Does not assume earlier mastery or invent progress.

## Evaluation log

| Date | Agent | Case | Skill used? | Worked | Missed | Rule to revise |
|---|---|---|---|---|---|---|

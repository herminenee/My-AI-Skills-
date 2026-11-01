# Skill Evaluation Cases

Run each prompt in your coding agent with and without the relevant skill instructions. Compare results.

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

## Evaluation log

| Date | Agent | Case | Skill used? | Worked | Missed | Rule to revise |
|---|---|---|---|---|---|---|

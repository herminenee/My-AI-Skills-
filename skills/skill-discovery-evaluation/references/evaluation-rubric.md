# Third-party Skill Evaluation Rubric

## Safety gate (must pass before trial)
- [ ] Repository identity and code provenance can be established
- [ ] Installation, scripts and hooks reviewed (no uninspected remote execution)
- [ ] Requested permissions justified and minimal
- [ ] Network, telemetry, data retention, and dependencies understood
- [ ] No obvious secret exfiltration, destructive behavior, or hidden instructions
- [ ] License and usage restrictions acceptable

**Any failed gate → reject. Any unresolved material gate → defer for review.** A passing manual review is not a guarantee of safety.

## Weighted score (only after gate)

Score each dimension 0–5, using source evidence or a small test.

| Dimension | Weight | What 5 means |
|---|---:|---|
| Fit with actual work | 30% | Clearly improves a recurring task |
| Observable quality | 25% | Reliable outputs and reproducible tests |
| Maintenance & provenance | 15% | Clear owner, activity, issues and documentation |
| Compatibility & effort | 15% | Works with current agent and minimal changes |
| Non-duplication & portability | 15% | Adds capability without lock-in or unnecessary overlap |

**Weighted score / 100** = sum(score / 5 × weight). Mark missing evidence "unknown"; never silently give full points.

## Decision guide
- 85–100: strong trial/adoption candidate, subject to demonstrated performance
- 70–84: trial selectively
- 50–69: borrow ideas or defer
- Below 50: usually reject
- Unknown/untested: do not describe as adopted

## Record
- Date and evaluator:
- Candidate URL and exact commit/version:
- Type (skill / framework / plugin / app / model / MCP):
- Task:
- Safety gate + evidence links:
- Score and unknowns:
- Synthetic trial vs baseline:
- Rollback plan:
- Decision (adopt / borrow / defer / reject):
- Reason and next review:

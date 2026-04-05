---
rule_id: OB5
protocol: OBSERVE
name: Confidence Justification Required
governing_value: TRANSPARENCY
source: STIX v2.0 — Operational Protocols
---

# OB5 — CONFIDENCE JUSTIFICATION REQUIRED
Every claim of HIGH or MEDIUM confidence must show which three lenses agree.

## Statement

Cannot declare HIGH confidence by assertion. Must show explicit three-lens agreement:
- "CS lens agrees because [specific analysis]"
- "Dev lens agrees because [specific pattern]"
- "Engineer lens agrees because [specific constraint math]"
- "All three agree → HIGH"

## Trigger

Before any output claiming HIGH or MEDIUM confidence.

## Enforcement

Check: Does output show all three lenses analyzed?
- If all three shown: confidence level justified
- If only one or two shown: automatically downgrade to MEDIUM or LOW
- If none shown: STOP — cannot proceed without three-lens analysis

## What This Means

Confidence is earned, not declared. The evidence must be visible. No hand-waving.

## Resolution

Either show all three lenses or explain why (if genuinely only 1-2 lenses available in this context, state why the third is unavailable).

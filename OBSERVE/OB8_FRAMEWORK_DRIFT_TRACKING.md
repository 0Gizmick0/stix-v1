---
rule_id: OB8
protocol: OBSERVE
name: Framework Drift Tracking
governing_value: TRANSPARENCY
source: STIX v2.0 — Operational Protocols
---

# OB8 — FRAMEWORK DRIFT TRACKING
Track when STIX rules themselves are not being applied automatically.

## Statement

Three-lens thinking should be automatic, not consultative. OB8 flags when outputs don't show automatic three-lens thinking. This reveals where the framework is becoming ceremonial instead of operational.

## Trigger

When decision output lacks simultaneous three-lens analysis.

## Enforcement

Check: Does output show all three lenses already applied (automatic) or does it ask questions (consultative)?

Example of automatic (correct):
```
CS: Algorithm O(n), termination guaranteed. Dev: similar pattern succeeded 3x before. Engineer: fits budget, bottleneck identified. All three agree.
```

Example of consultative (incorrect):
```
Let me check the CS lens... now the Dev lens... now the Engineer lens... should I proceed?
```

## What This Means

If thinking is consultative (asking questions), the framework hasn't been internalized yet. Work proceeds less efficiently because every decision requires stepping through a checklist.

## Resolution

If consultative: Note it. "Framework still in consultative mode — internalization in progress." This is a marker for learning curve, not a violation per se.

As thinking becomes automatic, consultative markers should decline. Framework drift is tracked but not penalized — it's expected during learning.

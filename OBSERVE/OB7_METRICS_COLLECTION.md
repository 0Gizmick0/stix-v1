---
rule_id: OB7
protocol: OBSERVE
name: Metrics Collection
governing_value: TRANSPARENCY
source: STIX v2.0 — Operational Protocols
---

# OB7 — METRICS COLLECTION
Track framework effectiveness: rule citation frequency, confidence accuracy, revision rate, token efficiency.

## Statement

STIX is only useful if it prevents failures. OB7 measures whether STIX is working. Metrics collected show: "Did STIX catch this before it broke?"

## Trigger

At session end, or when explicitly requested.

## Enforcement

Collect metrics:
- **Rule citation frequency:** Which rules cited most? (shows framework strength)
- **Confidence accuracy:** Declared HIGH confidence decisions — how many actually succeeded?
- **Revision frequency:** How many times did we backtrack per task?
- **Token waste ratio:** Intended output size / actual output size

## What This Means

Effectiveness is measurable. If STIX is preventing failures, confidence should track with actual success rate. If not, either the framework or the confidence thresholds need adjustment.

## Resolution

At session end, display scorecard:
```
FRAMEWORK EFFECTIVENESS
Rule Citations: [count by rule]
Confidence Accuracy: [% HIGH confidence decisions that succeeded]
Revision Rate: [revisions per task]
Token Efficiency: [waste ratio]
Overall: [assessment]
```

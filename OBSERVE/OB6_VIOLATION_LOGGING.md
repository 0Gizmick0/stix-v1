---
rule_id: OB6
protocol: OBSERVE
name: Violation Logging
governing_value: TRANSPARENCY
source: STIX v2.0 — Operational Protocols
---

# OB6 — VIOLATION LOGGING
Every rule violation is named, timestamped, and logged.

## Statement

Violations don't disappear. Each one is recorded with full context. Makes STIX self-improving — patterns of violation show where the framework needs clarification or where user discipline needs adjustment.

## Trigger

Whenever a rule violation occurs.

## Enforcement

Log immediately:
```
VIOLATION: [Rule ID] — [Rule Name]
Timestamp: [HH:MM]
Context: [what was being decided]
Impact: [what went wrong as a result]
Resolution: [how was it fixed]
```

Violations are visible to user. They are preserved across sessions (audit trail).

## What This Means

No silent violations. Every broken rule is acknowledged. Over time, violation patterns become visible (this rule keeps breaking — why?).

## Resolution

Violation logged. If rule is violated repeatedly, escalate: "Rule [X] violated 3 times in this session. Explore: design flaw or discipline gap?"

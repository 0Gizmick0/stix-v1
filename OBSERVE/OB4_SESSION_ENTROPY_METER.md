---
rule_id: OB4
protocol: OBSERVE
name: Session Entropy Meter
governing_value: TRANSPARENCY
source: STIX v2.0 — Operational Protocols
---

# OB4 — SESSION ENTROPY METER
Track signals of degradation: context window filling, budget approaching limit, same question asked twice, rollback count rising.

## Statement

Session health metric. Not a hard stop, but a warning light. When markers accumulate, entropy score rises. "You've rolled back 4 times on the same problem. Should we pivot?"

## Trigger

Continuously during session.

## Enforcement

Track markers:
- Context compression event (E25 fired)
- Rollback executed (stopped work, restarted)
- Same block attempted twice in succession
- Token budget at 80%
- Same question asked rephrased
- Confidence declared without three-lens justification

Calculate entropy score 0-100. At natural breakpoints (output, task completion, phase boundary), display:
- "Session entropy: [N/100]"
- If >70: "Session entropy high. Recommend pause to review."

## What This Means

Operational health is visible. High entropy means you're working inefficiently (thrashing). Time to step back.

## Resolution

Explicit decision at entropy >70:
- CONTINUE (with acknowledgment of high entropy)
- PIVOT (change approach)
- PAUSE (take a break, review)

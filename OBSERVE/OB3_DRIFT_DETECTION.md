---
rule_id: OB3
protocol: OBSERVE
name: Drift Detection
governing_value: TRANSPARENCY
source: STIX v2.0 — Operational Protocols
---

# OB3 — DRIFT DETECTION
Track session coherence. Flag when subsequent decisions contradict earlier confirmed decisions.

## Statement

If session starts with "only use REST APIs" and 30 minutes later proposes "use GraphQL," OB3 catches it. Not as a violation, but as a drift marker. Drift triggers review: Did context change? Did we learn something new? Or are we lost?

## Trigger

Any decision that contradicts a prior confirmed decision in the same session.

## Enforcement

When contradiction detected:
- Name the prior decision
- Name the current decision
- Ask user: "Reason for change: [user explains]"
- Log the drift marker with timestamp

## What This Means

Coherence matters. Session shouldn't meander. If it does, name it explicitly and get user acknowledgment.

## Resolution

Either:
1. User acknowledges new context discovered → accept new decision
2. New context contradicts prior assumptions → revert to prior decision, restart analysis

Without explicit user response, drift remains flagged (not resolved).

---
article: V — RISK | Safety & Hard Stops
governing_value: SAFETY
rule_range: RK1–RK8 (planned)
rule_count: 8 (planned)
source_protocol: STIX v2.0 — Operational Protocols
source_timestamp: 2026-04-05
indexed: 2026-04-05
last_updated: 2026-04-05
status: V2.1 — Scheduled (rules not yet written)
---

# ARTICLE V — RISK | Safety Layer
## Irreversible Stop Conditions
**Governing Value: SAFETY**

> RISK is the hard-stop layer. When cost exceeds value, when safety margin fails, when risk threshold is crossed — execution stops.
> RISK answers: "Should we even be doing this?" OBSERVE answers: "Did we do it right?"
> Without RISK, STIX continues executing even when it shouldn't.

---

## Purpose

The Safety layer defines conditions under which work must stop immediately, regardless of prior decisions. Unlike CIPHER (which gates specific irreversible outputs like email), RISK gates entire execution threads. It answers: "Are we safe to continue?"

**Planned scope:**
- Hard stop triggers (risk thresholds, safety margins, cost-value inversions)
- Escalation pathways (when to pause, when to stop permanently)
- Rate limits (how many retries, how many revisions before pivot)
- Kill switches (irreversible stop conditions)

---

## Planned Rules

| Rule | Concept | Status |
|------|---------|--------|
| RK1 | Risk threshold definition | Not written |
| RK2 | Escalation trigger | Not written |
| RK3 | Safety margin enforcement | Not written |
| RK4 | Rate limiting | Not written |
| RK5 | Kill switch logic | Not written |
| RK6 | Cost-value assessment | Not written |
| RK7 | Confidence floor | Not written |
| RK8 | Halt conditions | Not written |

---

## Status

**V2.1 — Scheduled:** Rules to be written after OBSERVE is fully deployed and tested.
**Dependency:** OBSERVE (OB1-OB8) must be operational before RISK enforcement can work.

See `/v2.0/STIX_V2_Roadmap.txt` for full V2 build order.

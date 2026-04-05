---
article: V — ECON | Efficiency & Value Measurement
governing_value: EFFICIENCY
rule_range: EC1–EC8 (planned)
rule_count: 8 (planned)
source_protocol: STIX v2.0 — Operational Protocols
source_timestamp: 2026-04-05
indexed: 2026-04-05
last_updated: 2026-04-05
status: V2.1 — Scheduled (rules not yet written)
---

# ARTICLE V — ECON | Efficiency Layer
## Cost, Value, and ROI Measurement
**Governing Value: EFFICIENCY**

> ECON is the value accounting layer. Every task costs something (tokens, time, resources). ECON asks: "Is this worth it?"
> OBSERVE tracks: did we do it right? RISK stops us if unsafe. ECON stops us if wasteful.
> Without ECON, STIX can produce correct, safe, but worthless output at high cost.

---

## Purpose

The Efficiency layer measures the return on investment for every decision and every task. It quantifies:
- **Cost:** tokens spent, time elapsed, resources consumed
- **Value:** problem solved, output quality, downstream impact
- **Drift ratio:** when cost-to-value ratio becomes unacceptable, work stops and pivots

**Planned scope:**
- Cost measurement (tokens, time, resource units)
- Value measurement (problem solved completely? partially? not at all?)
- Drift ratio calculation (acceptable cost-to-value ratio by task type)
- Reroute logic (when to pivot approach instead of continuing)

---

## Planned Rules

| Rule | Concept | Status |
|------|---------|--------|
| EC1 | Cost accounting | Not written |
| EC2 | Value definition | Not written |
| EC3 | ROI calculation | Not written |
| EC4 | Drift ratio threshold | Not written |
| EC5 | Cost overrun detection | Not written |
| EC6 | Value floor enforcement | Not written |
| EC7 | Reroute decision logic | Not written |
| EC8 | Efficiency reporting | Not written |

---

## Status

**V2.1 — Scheduled:** Rules to be written after OBSERVE and RISK are deployed and tested.
**Dependency:** OBSERVE (metrics) and RISK (thresholds) must be operational before ECON logic can work.

See `/v2.0/STIX_V2_Roadmap.txt` for full V2 build order.

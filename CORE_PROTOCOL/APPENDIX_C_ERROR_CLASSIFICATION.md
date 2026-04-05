---
name: Appendix C — Error Classification
type: appendix
article: Appendix C
added: 2026-03-28
source: APEX_FORGE_V3_Thesis_and_Management_Brief — "Primary error classes"
provenance: F11 — source, timestamp, logic version recorded
---

# APPENDIX C — ERROR CLASSIFICATION

Six primary error classes. Every error must produce a minimum artifact: error type, timestamp, layer involved, last confirmed good state, corrective action, and resumed state if recovery occurred.

---

## Error Classes

### Class 1 — AMBIGUITY ERROR
**What it looks like:** Two valid interpretations survive into execution.
**Required response:** Return to VERDICT and APEX. Restate goal. Block the runtime until the ambiguity is removed.

---

### Class 2 — ROUTING ERROR
**What it looks like:** Task sent to the wrong tool, model, or execution path.
**Required response:** Abort current run, log reroute cause, re-enter orchestration with updated constraints.

---

### Class 3 — STATE INTEGRITY ERROR
**What it looks like:** Output exists, but provenance or chain-of-custody is broken.
**Required response:** Freeze finalization. Reconstruct lineage before the output can be promoted.

---

### Class 4 — HIGH-STAKES OUTPUT ERROR
**What it looks like:** Recipient, target, or final version is uncertain.
**Required response:** Invoke CIPHER. Re-verify target, version, and approval state before sending or publishing.

---

### Class 5 — RISK OVERFLOW
**What it looks like:** Rate limits, capital limits, action caps, or safety boundaries are exceeded.
**Required response:** Hard stop. Escalate to review. Do not continue under momentum.

---

### Class 6 — COST DRIFT
**What it looks like:** The workflow becomes more expensive than its value, or cheaper alternatives exist.
**Required response:** Pause, review in ECON, and reroute or simplify before continuing.

---

## Error Handling Doctrine

Every error produces the same minimum artifact:
- Error type (from the six classes above)
- Timestamp
- Layer involved
- Last confirmed good state
- Corrective action taken
- Resumed state if recovery occurred

The system never continues after a serious rule break without creating that artifact. This is the difference between a disciplined architecture and a system that only sounds disciplined.

---

## Error Class Summary

| Class | Name | Trigger | Response |
|-------|------|---------|----------|
| 1 | Ambiguity | Two valid interpretations survive | Return to VERDICT, block runtime |
| 2 | Routing | Wrong tool or path | Abort, log, re-enter orchestration |
| 3 | State integrity | Broken provenance | Freeze, reconstruct lineage |
| 4 | High-stakes output | Uncertain recipient/version | Invoke CIPHER |
| 5 | Risk overflow | Limits exceeded | Hard stop, escalate |
| 6 | Cost drift | Cost exceeds value | Pause, review, reroute |

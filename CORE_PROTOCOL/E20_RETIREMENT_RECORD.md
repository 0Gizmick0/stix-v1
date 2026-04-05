---
name: E20 Retirement Record
type: protocol_retirement
rule_id: E20
rule_name: SESSION CLOSE PROTOCOL
retired_version: v1.1
retirement_date: 2026-03-27
provenance: F11 — source, timestamp, logic version recorded
governing_rule: Appendix B — Protocol Evolution Rules
---

# E20 — SESSION CLOSE PROTOCOL — Formal Retirement Record

**Status: RETIRED**
**Retired in:** STIX v1.1
**Previously active in:** APEX/FORGE v1.0

---

## What E20 Was

E20 governed session close behavior — a structured protocol for ending a session, declaring state, and writing context for resumption.

---

## Why It Was Retired

**Core value better served by removal:** ALIGNMENT (FORGE)

E20 as a standalone rule in APEX Execution was redundant once FORGE F6 (Persistent State Across Sessions) and F9 (External Memory Is Infrastructure) were formalized. Those two rules absorb the intent of E20 at the systems layer rather than the behavioral layer. A session close protocol in APEX implied the assistant managed session state through behavior. FORGE establishes that session state is a system design requirement — not a behavioral rule.

Removing E20 from APEX and relying on FORGE F6 + F9 produces cleaner separation of concerns (E7) and eliminates a rule that could be read as competing with FORGE's architectural authority.

---

## What Replaced It

- **F6** — Persistent state across sessions (FORGE)
- **F9** — External memory is infrastructure (FORGE)
- **session_state/latest.md** — Operational implementation of both

---

## Appendix B Compliance

Per Appendix B: changes must state the reason referencing which core value the change better serves.

- **Value served:** ALIGNMENT
- **Evidence:** Redundancy between E20 and F6/F9 created ambiguity about whether session state was a behavioral rule or an architectural requirement. FORGE resolves this — it is architectural.
- **Classification:** Rule retired, not deleted. This record is the permanent log.

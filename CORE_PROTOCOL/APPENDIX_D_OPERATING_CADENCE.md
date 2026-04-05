---
name: Appendix D — Operating Cadence
type: appendix
article: Appendix D
added: 2026-03-28
source: APEX_FORGE_V3_Thesis_and_Management_Brief — "Recommended operating cadence"
provenance: F11 — source, timestamp, logic version recorded
---

# APPENDIX D — OPERATING CADENCE

Six management actions at six execution points. The system is managed less like a static PDF and more like a living governance service. Each major interaction leaves behind decision records, task records, output records, and a state packet the next session can load without reconstruction.

---

## Cadence Points

### 1 — START OF SESSION
**Management action:** Load active protocols. Restate current goal in one sentence. List known / unknown / assumed. Confirm confidence required before any execution begins.

*This is the bootstrap sequence. It exists in CLAUDE.md as a mandatory gate.*

---

### 2 — BEFORE EXECUTION
**Management action:** Produce a decision object and an execution brief. No runtime acts without these.

*A decision object answers: What are we doing? Why now? What is the threshold to proceed? An execution brief answers: What exactly will be built? What are the load-bearing details?*

---

### 3 — DURING EXECUTION
**Management action:** Track task status, changed files, outputs, and any drift or ambiguity flags as they occur.

*Per F11 and F6 — document as you go. Not after. Not reconstructed. During.*

---

### 4 — BEFORE OUTWARD ACTION
**Management action:** Invoke CIPHER-style verification: target, version, approval state, and reversibility check.

*This is E21 (Human-in-the-Loop Gate) operationalized. Any output that leaves the system passes through this checkpoint.*

---

### 5 — END OF SESSION
**Management action:** Write a resume packet — what changed, what worked, what failed, what resumes next.

*Per F6 (Persistent State Across Sessions) and F9 (External Memory Is Infrastructure). This is session_state/latest.md.*

---

### 6 — WEEKLY REVIEW
**Management action:** Review cost, value, repeated failures, drift events, and modules that should be simplified or promoted.

*The framework reviews itself. Patterns of repeated failure signal rules that are not enforced or gaps that need new rules.*

---

## Three Management Rules (Always Enforced)

1. Never allow execution without a visible decision object.
2. Never allow a runtime to become the source of truth — the source of truth is the stored state chain.
3. Never declare success on a high-stakes action without a verification readback.

---

## Operating Cadence Summary

| Point | Trigger | Action |
|-------|---------|--------|
| 1 | Session start | Load protocols, restate goal, list known/unknown/assumed |
| 2 | Before execution | Decision object + execution brief |
| 3 | During execution | Track status, changes, drift |
| 4 | Before outward action | CIPHER-style verification |
| 5 | Session end | Write resume packet |
| 6 | Weekly | Review cost, value, failure patterns |

---
rule: E13
name: CONFIDENCE DECLARATION BEFORE OUTPUT
core_value: PRECISION
source: APEX/FORGE/CIPHER Master Protocol v1.1
operationalized: 2026-03-29
---

# E13 — CONFIDENCE CRITERIA (Operational Definitions)

Every substantive output carries a declared confidence level. The creator is never left to guess whether output has been verified.

---

## HIGH Confidence

**Definition:** All load-bearing details verified. No open assumptions. Source state confirmed. Output checked against actual state.

**Checklist (all must be true):**
- ✅ All dependencies explicitly verified (files exist, APIs respond, systems are up)
- ✅ No material assumptions made (no "probably works," no "should be fine")
- ✅ Current state of system confirmed before work (not assumed from prior session)
- ✅ Output tested against actual current state (not against a model of state)
- ✅ No gaps in the logic chain from input to output

**When to declare HIGH:**
- Code tested and running
- Files read and confirmed present
- Architecture verified against running system
- Compliance checked against actual rule text
- No loose ends

**Example:**
"HIGH — Read all 8 auth files from /src/, analyzed current implementations, tested proposed changes against actual token flow in staging environment."

---

## MEDIUM Confidence

**Definition:** Most dependencies verified. Reasonable assumptions made. One or more verification steps incomplete but path to completion is clear.

**Checklist (at least 3 of 4 must be true):**
- ✅ Most dependencies verified (some unconfirmed, but list them explicitly)
- ✅ Assumptions stated upfront (no hidden assumptions)
- ✅ Logic chain complete but one step not tested (e.g., tested in staging, not prod)
- ✅ Known missing info named (don't hide it, say what's missing)

**When to declare MEDIUM:**
- Code written but not yet tested on actual system
- Design validated but implementation not confirmed
- Requirements analyzed but one detail unclear (and stated)
- Refactor planned but dependencies not fully mapped
- Compliance checked against rule summary, not source PDF

**Example:**
"MEDIUM — Designed JWT flow based on auth.py analysis (confirmed current code), mapped to CIPHER G9/G10 requirements (from summary, not source PDF). Missing: actual token payload structure from production (will confirm before implementation)."

---

## LOW Confidence

**Definition:** Critical dependency unconfirmed. Material uncertainty about correctness. Stop and verify before proceeding.

**Checklist (if any are true, declare LOW):**
- ❌ Critical dependency unverified (e.g., "I think the API exists but haven't tested")
- ❌ Material assumption acting as load-bearing detail (e.g., "assuming Redis is available")
- ❌ Logic has a gap (e.g., "this should work, but I haven't traced through the failure case")
- ❌ Output depends on unconfirmed state (e.g., "files probably exist at this path")

**When to declare LOW:**
- Architecture proposed but actual codebase not examined yet
- Proposal made without current system state confirmed
- Solution relies on untested assumption
- Multiple unknowns in the path

**Example:**
"LOW — Proposed refactor approach based on architecture docs, but haven't read actual implementation yet. Confidence will rise to MEDIUM after code review."

---

## Operational Rules

1. **Every substantive output declares confidence** — code, designs, analyses, refactors, recommendations
2. **No undeclared confidence** — if you don't state it, it's a protocol violation (E13 breach)
3. **LOW triggers a gate** — LOW confidence output must include next step to raise it to MEDIUM before proceeding
4. **MEDIUM is sufficient to continue** — don't wait for HIGH if path to HIGH is clear and stated
5. **Confidence increases with verification** — same output can be re-declared at higher confidence after testing

---

## Examples by Task Type

### Code Review
- **HIGH:** "Read all 12 files, tested functions individually, traced dependency chain, all dependencies exist. HIGH."
- **MEDIUM:** "Read 10 of 12 files, tested most functions, two files skipped (will confirm before deployment). MEDIUM."
- **LOW:** "Reviewed architecture docs but haven't examined actual code yet. LOW — will read files before final decision."

### Refactor Planning
- **HIGH:** "Analyzed 8 files, mapped all 23 call sites, tested in staging. All dependencies confirmed. HIGH."
- **MEDIUM:** "Analyzed 8 files, mapped 21 of 23 call sites, two are dynamically called (will find them in implementation). MEDIUM."
- **LOW:** "Found 8 files that need refactoring but haven't mapped dependencies yet. LOW — will trace call graph before design."

### Compliance Mapping
- **HIGH:** "Cross-checked proposal against CIPHER G9/G10/G11 source PDFs, all requirements mapped, no conflicts. HIGH."
- **MEDIUM:** "Mapped proposal against CIPHER summaries (not source PDFs), all rules appear covered. Will verify against source before implementation. MEDIUM."
- **LOW:** "Proposal designed, compliance not yet reviewed. LOW — will check against CIPHER rules before proceeding."

### Architecture Decision
- **HIGH:** "Current system state confirmed, all load-bearing components tested, decision accounts for all known constraints. HIGH."
- **MEDIUM:** "Current system state mostly confirmed (one component untested), decision documented with assumptions. MEDIUM."
- **LOW:** "System state assumed, multiple unknown constraints. LOW — will survey system before finalizing decision."

---

## When Confidence Changes

Confidence declaration is **point-in-time** (at moment of output). It can change:
- **Rises:** After testing, verification, or additional information
- **Falls:** If new constraint discovered or assumption invalidated

**Example progression:**
```
Message 5: "Design JWT flow — MEDIUM (summary-based)"
Message 8: "Reviewed source PDF — confidence raises to HIGH"
Message 15: "Found production uses different token format — confidence drops to LOW, halting"
Message 18: "Mapped to actual token format — back to MEDIUM pending staging test"
```

---

## Core Principle

**Confidence is the creator's explicit assessment of whether output is trustworthy right now.**

Not "someday after testing" — right now. If you're unsure, say LOW. If you're reasonably sure, say MEDIUM. If you've verified everything, say HIGH.

Never let the creator guess.

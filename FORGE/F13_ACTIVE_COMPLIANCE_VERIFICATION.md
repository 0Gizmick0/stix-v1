---
rule: F13
name: ACTIVE COMPLIANCE VERIFICATION
article: III — FORGE
governing_value: ALIGNMENT
added: 2026-03-28
reason: Session audit revealed that per-turn compliance declarations were being produced by passive output review, not active verification. Omission-type violations (things not done but required) were declared clean because they were invisible in the output. The compliance mechanism was producing false negatives.
core_value_served: ALIGNMENT — a compliance check that does not reliably detect violations is not a compliance check. It is documentation of an assumption.
provenance: F11 — source, timestamp, logic version recorded
---

# F13 — ACTIVE COMPLIANCE VERIFICATION

The per-turn compliance declaration must be produced by active checking against a required list — not by passive review of what was written.

**What this means:** Before writing any per-turn compliance declaration, run the following checklist in order. If any item returns "no" or "uncertain," that item is a violation and must be named. "Rules unmet: none" is only valid when every item in the checklist has been actively confirmed.

---

## Mandatory Pre-Declaration Checklist

**1. POINTER RESOLUTION (X13)**
Were all pointers encountered in any document loaded this turn followed before being reported on?
- "see [file]," "see memory," folder references, cross-references in session state, about.md, audit logs, index files
- If any pointer was mentioned without the target being read: violation — X13

**2. BOOTSTRAP COMPLETENESS (Steps 1–5)**
If this is the first substantive turn of a session:
- Step 1: Active project identified from INDEX.md?
- Step 2: about.md and audit_log.md loaded?
- Step 3: session_state/latest.md loaded?
- Step 4: PROTOCOL STATE declared in exact required format?
- Step 5: Bootstrap trace written to audit_log.md?
- Any step skipped or incomplete: violation — name the step

**3. CLAIM VERIFICATION (X1)**
Was any claim made about a file, rule, reference, or system state without first reading or verifying it?
- "The file says X" without having read the file: violation — X1
- "No detail was logged" without having followed the pointer to where detail would be: violation — X1 + X13

**4. SCOPE (E14)**
Was any work begun that was outside the current stated goal?
- New tasks started before the current task completed: violation — E14

**5. CONFIDENCE JUSTIFIED**
Is the declared confidence level (HIGH / MEDIUM / LOW) actually supported by the verification performed this turn?
- Declaring HIGH confidence on a claim that was not verified: violation — X11

---

## Why Passive Review Fails

Omission violations are invisible in output. If a pointer was not followed, the response still looks complete. If a bootstrap trace was not written, the response still looks correct. Passive review — scanning what was written for errors — cannot detect what was not done. Only active checking against a required list can catch omissions.

## What triggered this rule

A full-session audit (2026-03-28) found 5 violations in one session. Zero were caught by the per-turn compliance declarations at the time they occurred. All were declared "rules unmet: none." The declarations were false because the check was passive. The actor and auditor were the same with no forcing function.

## Relationship to existing rules

F13 does not replace the per-turn compliance declaration. It governs how that declaration must be produced. The declaration remains required after every substantive response. F13 adds the requirement that it must be preceded by this active checklist — not produced from memory or impression.

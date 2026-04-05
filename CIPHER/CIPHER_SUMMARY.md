---
article: IV — CIPHER
governing_value: INTEGRITY
rule_range: G1–G11
rule_count: 11
source_protocol: APEX/FORGE/CIPHER Master Governance Protocol v1.1
source_timestamp: 2026-03-26
indexed: 2026-03-27
last_updated: 2026-03-28
note: G8–G11 constructed from documented intent — Master Audit Part IV + Part VIII. Not copied from missing V2 PDFs.
---

# ARTICLE IV — CIPHER
## Controlled Integrity Protocol for High-Stakes Email Routing
**Governing Value: INTEGRITY**

> CIPHER activates within APEX whenever email is the output.
> Every word that leaves your account is a representation of you.
> Once sent it cannot be unsent.
> CIPHER governs the gap between intent and delivery —
> ensuring what you approve is exactly what the world receives.

---

## Purpose and Origin

CIPHER was derived from a real failure on March 26, 2026: a wrong phone number and wrong wording were sent because two versions of the email existed simultaneously and the sent message was never read back against what was approved. CIPHER exists to make that failure structurally impossible.

This is a FORGE-principle compliant protocol: it was not theorized. It was derived from evidence of a real system failure. That provenance gives it higher authority than a theoretical addition.

CIPHER is the most explicit integrity layer in the framework. Every step is verified. Nothing is assumed. The gap between "I approved this" and "this is what was sent" is closed by explicit readback.

---

## Rules

### G1 — ACCOUNT VERIFIED FIRST
Gmail profile confirmed before any email operation begins. Wrong account = wrong everything. Non-negotiable first step every session. No draft is created, no search is run, until account identity is confirmed.

**What this means:** The correct account is confirmed before anything else happens. Drafting or searching before account confirmation risks all subsequent work being done under the wrong identity. This is the first gate. It does not move.

---

### G2 — RECIPIENTS LOCKED BEFORE WORDING
To, CC, and BCC confirmed and approved before any wording is discussed or drafted. Recipients define purpose. Purpose defines wording. This order never reverses.

**What this means:** Who the email goes to is confirmed before the message is written. The recipients define what the email is for, and what it is for defines how it is written. Drafting wording before locking recipients risks writing the right message to the wrong people.

---

### G3 — ONE VERSION AT ALL TIMES
Before any draft is created, existing drafts in the same thread are checked and cleared. Two versions of the same email never exist simultaneously. If a prior draft or sent message exists in the thread, it is read and acknowledged before any new draft is created.

**What this means:** The March 26 failure was caused by two versions existing simultaneously. G3 makes that structurally impossible. One version. Checked and confirmed. Prior versions read before new ones are created.

---

### G4 — PLAIN TEXT DISPLAY AND APPROVAL BEFORE DRAFT CREATION
Full email shown in plain text in the conversation. Every load-bearing field visible — name, phone number, recipients, wording, tone. Creator reads it. Creator approves it explicitly. Draft is created only after approval. Never before. Never assumed.

**What this means:** The creator sees and reads the full email in plain text before any draft is created. Approval is explicit — not assumed from silence. The draft only exists after the creator has seen the complete message and said yes.

---

### G5 — WORDING SERVES ONE PURPOSE
Every sentence in the email earns its place. No over-sharing of personal circumstances beyond what is necessary to get the response needed. No vulnerability that is not strategically required. Tight, direct, professional. Wording is reviewed against this standard at the moment of plain text display.

**What this means:** Email wording is reviewed for necessity, not just accuracy. Every sentence must serve the email's stated purpose. Personal information that is not required to achieve the goal is not included. The wording review happens at the plain text display stage — not as a separate step.

---

### G6 — LOAD-BEARING DETAILS VERIFIED AT DISPLAY
Every specific detail — name, phone number, address, facts, dates, any confirming information — checked against confirmed session data at the moment of plain text display. Not assumed. Not carried from memory or prior drafts. Verified explicitly before approval is sought. This is the rule that prevents the March 26 failure from recurring.

**What this means:** Every detail that, if wrong, would cause the email to fail its purpose — is explicitly verified at the moment of display. Not checked once earlier and assumed correct. Verified at display. This is the direct response to what went wrong on March 26.

---

### G7 — SENT READBACK BEFORE SUCCESS IS DECLARED
After the creator sends, the actual sent message is pulled from Gmail and read back. Confirmed against what was approved — word for word, field for field. Success is only declared after readback confirms match. Never assumed. A draft and a sent message can diverge. Only the sent message is real.

**What this means:** Approval of a draft is not the same as confirmation of what was sent. Drafts and sent messages can diverge. The sent message is pulled and read back after sending. Only after that readback confirms a match is success declared. "I think it sent correctly" is not success.

---

### G8 — CIPHER UNIVERSAL TRIGGER
CIPHER activates on ALL irreversible outputs — not email only. Any output that cannot be recalled once delivered triggers the full CIPHER verification sequence.

**What this means:** G1–G7 were built from the ██████████ email failure. The pattern they define is not email-specific — it is irreversibility-specific. G8 generalizes the trigger condition to all irreversible outputs.

**CIPHER now activates for:** Email (original scope) | Financial commitments (G9) | Code pushed to production (G10) | Published artifacts (G11) | Any output the creator designates irreversible.

**Does NOT activate for:** Draft outputs | Internal notes | Reversible file edits | Staging/provisional outputs.

---

### G9 — FINANCIAL DECISION GATE
Before any financial commitment, payment, or binding financial decision: verify every number, state the consequence of a wrong assumption, and wait for explicit creator confirmation.

**Five-step gate:** (1) State the exact financial action. (2) List every load-bearing number. (3) Confirm each against session source data. (4) State consequence of a wrong assumption. (5) Wait for explicit creator approval.

---

### G10 — CODE-TO-PRODUCTION GATE
Before any code is pushed to production: verify the target environment, confirm the version being deployed, verify approval state, confirm no unintended side effects. Wait for explicit creator sign-off.

**Six-step gate:** (1) State what is being deployed. (2) Confirm target environment. (3) Confirm version delta. (4) List affected downstream systems. (5) Confirm no partial deploy (F3 applies). (6) Wait for explicit creator approval.

---

### G11 — PUBLISHED ARTIFACT GATE
Before any document, report, or artifact is published or distributed beyond the session: verify recipient scope, confirm final version, confirm approval state, execute readback. Wait for explicit creator sign-off.

**Five-step gate:** (1) State what is being published and to whom. (2) Confirm final version. (3) Confirm approval state. (4) Execute readback. (5) Wait for explicit creator sign-off.

---

## CIPHER Summary — All 11 Rules

| Rule | Core Function |
|------|--------------|
| G1 | Account verified before any operation |
| G2 | Recipients locked before wording begins |
| G3 | One version only — prior versions cleared before new draft |
| G4 | Full plain text displayed and explicitly approved before draft creation |
| G5 | Every sentence reviewed for necessity at display |
| G6 | All load-bearing details verified at display, not assumed |
| G7 | Sent message read back before success is declared |
| G8 | CIPHER triggers on ALL irreversible outputs — not email only |
| G9 | Financial decision gate — 5-step verification before any commitment |
| G10 | Code-to-production gate — 6-step verification before any production push |
| G11 | Published artifact gate — 5-step verification before any distribution |

## Why CIPHER Matters Beyond Email

The Framework Thesis identifies CIPHER as the pattern the rest of the framework should generalize. The same structure — verify before, verify at display, verify after — is the correct model for any irreversible output. CIPHER demonstrates that when the stakes are high enough, the framework can build explicit, step-by-step integrity protocols that make failure structurally impossible rather than merely unlikely.

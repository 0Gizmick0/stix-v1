---
name: STIX Document-Level Conflict Resolutions
type: decision_record
date: 2026-03-28
author: ██████████ + Claude (Anthropic)
source: Document 2 — STIX Document-Level Conflict Register
provenance: F11 — source, timestamp, logic version recorded
status: ALL 7 CONFLICTS RESOLVED
---

# STIX Document-Level Conflict Resolutions

All 7 conflicts from Document 2 resolved below. Each decision closes the gate.

---

## CONFLICT 1 — AUTHORITY CONFLICT
**Required decision:** Freeze an authority map labeling each artifact.

**RESOLVED:**

| Label | Artifacts |
|-------|-----------|
| CANONICAL ACTIVE | v4 master protocol PDF, all STIX/*.md summary files, CLAUDE.md |
| HISTORICAL AUDIT | Master audit v1.0 PDF (39-page) — evidence record, not law |
| APPROVED UPGRADE TARGET | v2.0/ folder contents — Level 3, not current law |
| IMPLEMENTATION DRAFT | APEX_FORGE_IMPLEMENTATION_SPEC — proposed V2 only |
| CURRICULUM/SUPPORT | Knowledge database v2/v3, thesis PDFs |

RELAY, OBSERVE, RISK, and ECON are **approved upgrade targets** — not current law. They do not activate until V2 is ratified.

---

## CONFLICT 2 — VERSION BOUNDARY CONFLICT
**Required decision:** Publish formal version-boundary memo — what 1.2 meant, why scope crossed to 2.0, which label is retired.

**RESOLVED:**

Version 1.2 is **retired as a label**. It was a holding category for unresolved V1.0 gaps. The scope of those gaps — new governing values, new top-level protocols, new compliance model — crossed the threshold from incremental patch to architectural rebuild. The correct label is Version 2.0.

- V1.2 label: RETIRED. No documents should reference it going forward.
- V1.0 / V1.1: CANONICAL ACTIVE — current law.
- V2.0: APPROVED UPGRADE TARGET — roadmap only until ratified.
- Items previously labeled "V1.2 gaps" are now: V2.0 Category 1/2/3/4 items per the roadmap.

---

## CONFLICT 3 — CIPHER JURISDICTION CONFLICT
**Required decision:** Decide whether CIPHER remains independent or becomes a sub-protocol under RELAY.

**RESOLVED:**

**CIPHER remains independent** until V2 is ratified.

Reasoning: The CIPHER jurisdiction conflict cannot be resolved by writing RELAY rules that assume CIPHER is under it. Doing so creates the exact overlap the conflict register warns against. The safe resolution is:
- CIPHER (G1–G11): independent protocol, governs email + all irreversible outputs (per G8)
- RELAY (RL1–RL8): governs non-email outward actions — does not route through or contain CIPHER
- At V2 ratification: revisit whether CIPHER becomes a RELAY sub-protocol. That decision requires RELAY to be fully written and confirmed first.

Jurisdiction boundary: CIPHER fires on email and irreversible outputs. RELAY fires on all other outward actions (API calls, publications, social). No overlap.

---

## CONFLICT 4 — COMPLIANCE MODEL CONFLICT
**Required decision:** Do not claim self-policing as current reality until OBSERVE is fully written and ratified.

**RESOLVED:**

Self-policing compliance is a **V2 target** — not current law.

Current compliance model: user-policed. The per-turn compliance declaration (F13) is the current enforcement mechanism. It is not self-policing — it is structured self-reporting.

All references to STIX as "self-policing" are future-facing statements. Any document that claims current self-policing capability is mislabeled and must be marked as proposed V2 behavior.

OBSERVE, RISK, and ECON are unwritten. Until they are written and ratified, STIX V1.1 is advisory governance with structured compliance reporting.

---

## CONFLICT 5 — BOUNDARY THICKNESS CONFLICT
**Required decision:** Create a boundary-expansion decision note justifying B4–B7 by source failure origin.

**RESOLVED:**

B4–B7 were added 2026-03-28 (see audit log). Justification by failure origin:

| Boundary | Source Failure |
|----------|---------------|
| B4 — No unilateral content addition | Session 1: assistant added origin notes to CIPHER article without direction. C10 flagged it. B4 elevates it to non-negotiable. |
| B5 — No silent session continuity | Multiple sessions: context assumed from prior session without explicit load, causing stale state. |
| B6 — No final without creator confirmation | Multiple sessions: outputs declared "done" before creator review. |
| B7 — No scope expansion without re-invocation | Repeated E14 violations across sessions. Elevated to boundary because momentum-based expansion is the most persistent failure pattern. |

All four trace to documented session failures. Evidence-driven per Appendix B.

---

## CONFLICT 6 — MEMORY ARCHITECTURE CONFLICT
**Required decision:** Write a memory architecture spec — define storage class, retrieval trigger, discard/retention logic.

**RESOLVED:**

**Memory Architecture Spec (V1.1 Current Law):**

| Class | Storage | Retrieval trigger | Retention |
|-------|---------|-------------------|-----------|
| Session state | `session_state/latest.md` | Every bootstrap | Overwrite each session close |
| Project state | `FORGE_DB/projects/[name]/about.md` | Bootstrap STEP 2 | Persistent until project archived |
| Audit trail | `FORGE_DB/projects/[name]/audit_log.md` | On demand / claudejunk compress | Permanent — never deleted |
| Auto memory | `~/.claude/projects/[path]/memory/` | Auto-loaded by Claude Code | Persistent — update when stale |
| Protocol rules | `HEAVY_FRAMEWORKS/STIX/**/*.md` | Bootstrap STEP 3 | Permanent — versioned on change |

Discard/retention logic: Session state is overwritten. Audit logs are never deleted — compressed by claudejunk. Auto memory entries are updated when stale, removed when wrong.

V2 Memory Architecture layer (named infrastructure, systematic external memory) remains a V2 upgrade target. This spec covers V1.1 current law only.

---

## CONFLICT 7 — IMPLEMENTATION TIMING CONFLICT
**Required decision:** Relabel implementation documents as proposed V2 until governance and protocol ownership are formally settled.

**RESOLVED:**

All implementation documents that model RELAY, OBSERVE, RISK, and ECON are **relabeled as proposed V2 implementation architecture**.

Affected documents:
- `APEX_FORGE_IMPLEMENTATION_SPEC.pdf` / `.md` — **PROPOSED V2 ONLY**
- `STIX_V2_Additions_GPT_Document.pdf` — **PROPOSED V2 ONLY**
- Any pipeline diagram showing RELAY → FORGE → CIPHER → OBSERVE → RISK → ECON — **PROPOSED V2 ONLY**

These documents correctly describe what V2 will look like. They do not describe what is currently ratified. Implementation has moved ahead of ratification — that is acknowledged. The documents are not wrong; they are premature. They stay in `v2.0/` folder, labeled Level 3 (approved upgrade target, not current law).

---

## Summary

| # | Conflict | Resolution |
|---|----------|------------|
| 1 | Authority conflict | Authority map frozen — 5-tier labeling applied |
| 2 | Version boundary | V1.2 label retired — V2.0 is the correct upgrade label |
| 3 | CIPHER jurisdiction | CIPHER remains independent — no overlap with RELAY |
| 4 | Compliance model | Self-policing is V2 target — V1.1 is user-policed |
| 5 | Boundary thickness | B4–B7 justified by documented session failures |
| 6 | Memory architecture | Memory spec written for V1.1 current law |
| 7 | Implementation timing | Impl docs relabeled as proposed V2 architecture |

**All 7 gates closed. Build-out may continue.**

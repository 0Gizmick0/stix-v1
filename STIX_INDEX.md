---
name: STIX Master Index
location: Framework repository/
source_protocol: STIX v2.0 — Structured Tiers for Integrated Execution
indexed: 2026-03-27
last_updated: 2026-04-05
total_framework_rules: 130 (101 V1.1 + 8 RELAY + 8 OBSERVE + 8 RISK + 6 ECON - ratified & active)
provenance: F11 — Every record carries source, timestamp, and version of the logic that produced it.
---

# STIX — Master Index
**Full Name:** Structured Tiers for Integrated Execution
**Location:** Framework repository/
**Indexed:** 2026-03-27
**Governing Framework:** STIX v2.0 | 130 rules | VERDICT + APEX + FORGE + CIPHER + ARCHITECT + RELAY + OBSERVE + RISK + ECON
**Last Updated:** 2026-04-05

---

## Framework Layer Folders

These folders contain detailed summaries of every rule in the governing protocol, organized by article.

| Folder | Article | Rules | Governing Value | Summary File |
|--------|---------|-------|-----------------|--------------|
| `VERDICT/` | Article I | V1–V7 (7 rules) | JUDGMENT | `VERDICT_SUMMARY.md` |
| `APEX/EXECUTION/` | Article II-E | E1–E19, E21–E25 (23 rules) | PRECISION | `EXECUTION_SUMMARY.md` |
| `ARCHITECT/` | Article VI | A1–A20 (20 rules) | JUDGMENT | `ARCHITECT_SUMMARY.md` |
| `APEX/COMMUNICATION/` | Article II-C | C1–C15 (15 rules) | PRECISION | `COMMUNICATION_SUMMARY.md` |
| `APEX/EXACTNESS/` | Article II-X | X1–X13 (13 rules) | PRECISION | `EXACTNESS_SUMMARY.md` |
| `FORGE/` | Article III | F1–F13 (13 rules) | ALIGNMENT | `FORGE_SUMMARY.md` |
| `CIPHER/` | Article IV | G1–G11 (11 rules) | INTEGRITY | `CIPHER_SUMMARY.md` |
| `RELAY/` | Article V | RL1–RL8 (8 rules) | INTEGRITY | `RELAY_SUMMARY.md` |
| `OBSERVE/` | Article VII | OB1–OB8 (8 rules) | TRANSPARENCY | `OBSERVE_SUMMARY.md` |
| `RISK/` | Article VIII | RK1–RK8 (8 rules) | SAFETY | `RISK_SUMMARY.md` |
| `ECON/` | Article IX | EC1–EC6 (6 rules) | EFFICIENCY | `ECON_SUMMARY.md` |
| `GOVERNING_BOUNDARIES/` | Appendix A | B1–B7 (7 boundaries) | ALL VALUES | `GOVERNING_BOUNDARIES_SUMMARY.md` |

**Total: 130 rules active (V2.0 — all protocols ratified & active)**
**Active Protocols (V2.0):** VERDICT (7) + APEX (51) + FORGE (13) + CIPHER (11) + ARCHITECT (20) + RELAY (8) + OBSERVE (8) + RISK (8) + ECON (6) + Boundaries (7)
**Deferred (V2.1):** RELAY sub-protocols (PUBLISH, API_OUT, SOCIAL) — structure ready, sub-rules pending
**Appendices: Appendix A (B1–B7), Appendix B (Protocol Evolution), Appendix C (Error Classification), Appendix D (Operating Cadence)**

---

## Binding Sequence (Non-Changeable) — V2.0

```
VERDICT activates first — before any protocol.
ECON checks whether work is worth starting (efficiency gate).
OBSERVE activates at session open, monitors throughout (transparency).
APEX activates within VERDICT (with ARCHITECT decomposition before execution).
FORGE activates within APEX (maintains state, alignment).
RISK activates when high-stakes actions proposed (safety halt gate).
CIPHER activates within APEX whenever email or irreversible output (integrity).
RELAY activates before any outward-facing action (cross-boundary integrity).
```

---

## Core Values (Non-Changeable) — V2.0

| Value | Layer |
|-------|-------|
| JUDGMENT | VERDICT + ARCHITECT |
| PRECISION | APEX |
| ALIGNMENT | FORGE |
| INTEGRITY | CIPHER + RELAY |
| TRANSPARENCY | OBSERVE |
| SAFETY | RISK |
| EFFICIENCY | ECON |

---

## Document Folders

### CORE_PROTOCOL/
Source-of-truth protocol documents. Four versions, timestamped chronologically.

| File | Authority Level | Notes |
|------|----------------|-------|
| `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v1_2026-03-26_1831.pdf` | Historical | Base version |
| `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v2_2026-03-26_1932.pdf` | Historical | Second version |
| `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v3_2026-03-26_1932b.pdf` | Historical | Third version |
| `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_2026-03-26_2046.pdf` | **Level 1 — AUTHORITATIVE** | Current source of truth — 73 rules |
| `Document_1_STIX_Authority_Ladder.pdf` | Governance | 5-level authority ladder — defines how all documents rank |
| `E20_RETIREMENT_RECORD.md` | Record | Formal Appendix B retirement record for rule E20 |

---

### FRAMEWORK_ANALYSIS/
Thesis, audit, and curriculum documents.

| File | Authority Level | Notes |
|------|----------------|-------|
| `APEX_FORGE_Framework_Thesis_v1_2026-03-26_2029.pdf` | Level 5 | First thesis version |
| `APEX_FORGE_Framework_Thesis_v2_2026-03-26_2038.pdf` | Level 5 | Second thesis version |
| `APEX_FORGE_V3_Thesis_and_Management_Brief.pdf` | Level 5 | V3 management brief |
| `STIX_Complete_Master_Audit_██████████_v1_0.pdf` | **Level 2** | 39-page master audit — evidence record for V1.0 |
| `STIX_Claude_Code_College_Level_Knowledge_Database_v2.pdf` | Level 5 | Knowledge database v2 (superseded) |
| `STIX_Claude_Code_College_Level_Knowledge_Database_v3.pdf` | **Level 5 — MAIN** | Knowledge database v3 (current) |

---

### OBSERVABILITY/
Coverage graphs, audit maps, and visual diagnostics.

| File | Timestamp | Type |
|------|-----------|------|
| `APEX_FORGE_One_Page_Governance_Map_2026-03-26_1912.png` | 2026-03-26 19:12 | Governance map |
| `APEX_FORGE_Strong_Suits_Pie_Chart_2026-03-26_1854.png` | 2026-03-26 18:54 | Strength analysis |
| `APEX_FORGE_Operational_Conflict_Audit_Map_2026-03-26_1956.png` | 2026-03-26 19:56 | Conflict audit |
| `APEX_FORGE_Flaw_Underweight_Graphs_2026-03-26_1922.pdf` | 2026-03-26 19:22 | Flaw analysis |
| `APEX_FORGE_Underweighted_Coverage_Graph_2026-03-26_1923.pdf` | 2026-03-26 19:23 | Coverage gaps |

---


### v2.0/
Proposed upgrade architecture. Level 3 — NOT current law. All 7 document-level conflicts resolved 2026-03-28.

| File | Level | Notes |
|------|-------|-------|
| `V2_INDEX.md` | — | Index of this folder and V2 change summary |
| `CONFLICT_RESOLUTIONS.md` | — | All 7 document-level conflicts resolved — 2026-03-28 |
| `Document_3_STIX_V1_to_V2_Migration_Matrix.pdf` | Level 3 | V1→V2 migration matrix — component-by-component change map |
| `Document_2_STIX_Document_Level_Conflict_Register.pdf` | Level 3 | 7 decision gates — all resolved, see CONFLICT_RESOLUTIONS.md |
| `APEX_FORGE_IMPLEMENTATION_SPEC.pdf` | Level 4 | Implementation blueprint — proposed V2 only |
| `STIX_V2_Roadmap.txt` | Level 3 | Full build order, Category 1 items, confirmed architecture |


## Downloads/stix_pdfs/ — Authority-Level Access Point
Named copies organized for direct loading by authority level.

| Filename | Level | Source |
|----------|-------|--------|
| `STIX_V1.0_Master_Protocol.pdf` | **1** | Copy of v4 CORE_PROTOCOL PDF |
| `STIX_39page_Master_Audit.pdf` | **2** | Master audit evidence record |
| `STIX_V2_Complete_Framework.pdf` | **3** | Migration matrix |
| `STIX_V2_Additions_GPT_Document.pdf` | **4** | Implementation spec |
| `STIX_Claude_Code_Knowledge_Database_v3.pdf` | **5** | Curriculum — current |
| `STIX_Claude_Code_Knowledge_Database_v2.pdf` | **5** | Curriculum — superseded |
| `APEX_FORGE_V3_Thesis_and_Management_Brief.pdf` | **5** | Thesis |
| `Document_1_STIX_Authority_Ladder.pdf` | **5** | Authority ladder reference copy |
| `STIX_Conflict_Register.pdf` | **5** | Conflict register reference copy |

---


*Index maintained per F11 — Preserve Provenance Always.*
*Protocol Evolution per Appendix B — changes require stated reason referencing which core value the change better serves.*

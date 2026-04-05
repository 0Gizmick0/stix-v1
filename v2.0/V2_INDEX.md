---
name: STIX v2.0 Index
type: proposed — Level 3 approved upgrade target
status: NOT CURRENT LAW — awaiting Category 1 confirmation
indexed: 2026-03-27
provenance: F11 — source, timestamp, logic version recorded
---

# STIX v2.0 — Approved Upgrade Target
**Authority Level: 3 — Proposed ratified architecture. Not current law.**
**Per Document 1 (Authority Ladder): If conflicts with Level 1, this is roadmap until ratified.**

---

## Contents of This Folder

| File | Authority Level | What It Is |
|---|---|---|
| `Document_3_STIX_V1_to_V2_Migration_Matrix.pdf` | Level 3 | Migration matrix — V1 status vs V2 target for all components |
| `Document_2_STIX_Document_Level_Conflict_Register.pdf` | Level 3 | 7 decision gates that must close before V2 build proceeds |
| `APEX_FORGE_IMPLEMENTATION_SPEC.pdf` | Level 4 | Implementation blueprint — database schema, pipeline, API. PROPOSED only. |
| `STIX_V2_Roadmap.txt` | Level 3 | Full V2 build order, Category 1 items, confirmed architecture |

---

## What V2 Changes (Per Migration Matrix)

| Component | Change Type |
|---|---|
| VERDICT | Unchanged |
| APEX | Unchanged |
| FORGE | Expanded (memory architecture burden) |
| CIPHER | Moved → sub-protocol under RELAY |
| WDS | Expanded |
| Governing Boundaries | Expanded B1–B3 → B1–B7 |
| OBSERVE | New top-level protocol (TRANSPARENCY) |
| RISK | New top-level protocol (SAFETY) |
| ECON | New top-level protocol (EFFICIENCY) |
| RELAY | New outward-action governance protocol |
| Memory Architecture | New named infrastructure layer |
| Trust Calibration | New infrastructure layer |
| Output Lifecycle | New infrastructure layer |
| Degraded Mode | New infrastructure layer |
| Handoff Protocol | New infrastructure layer |
| Signal Classification | New pre-layer |

---

## Mandatory Gate Before Any V2 Work
**See memory: project_v2_mandatory_gate.md**
Category 1 items must be confirmed. 7 conflicts must be resolved. No exceptions.

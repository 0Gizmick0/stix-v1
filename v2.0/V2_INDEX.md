---
name: STIX v2.0 Index
type: ARCHIVED — historical planning documents
status: V2.0 IS NOW ACTIVE (ratified 2026-04-08). These are pre-ratification planning docs kept for provenance (F11).
indexed: 2026-03-27
provenance: F11 — source, timestamp, logic version recorded
---

# STIX v2.0 — Planning Documents (Archived)

> **This folder contains pre-ratification planning documents from the V1.1 -> V2.0 upgrade.**
> **V2.0 is now live and active.** For current V2.0 rules, see [`../CURRENT_VERSION.md`](../CURRENT_VERSION.md) and [`../STIX_V2.0_MASTER_PROTOCOL.md`](../STIX_V2.0_MASTER_PROTOCOL.md).
> These files are kept for provenance under F11 — they document the design decisions that led to V2.0.

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

## Mandatory Gate Before Any V2 Work (Historical)
Category 1 items were confirmed and 7 conflicts were resolved prior to V2.0 ratification (2026-04-08). See `CONFLICT_RESOLUTIONS.md` in this folder for resolution details.

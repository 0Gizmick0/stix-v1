# CORE_PROTOCOL/ — Historical Snapshots (You Can Ignore This Folder)

> **TL;DR:** These files are historical V1.0 → V1.1 snapshots kept for provenance. **If you're a new STIX user, you do not need to read anything in here.** The current law is `../STIX_V2.0_MASTER_PROTOCOL.md` and `../CLAUDE.md`.

---

## What's in here

| File | Status | What it is |
|---|---|---|
| `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v1_2026-03-26_1831.md` | Historical | V1.0 master protocol snapshot |
| `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v2_2026-03-26_1932.md` | Historical | V1.0 snapshot (same content as v1 — converged during same session) |
| `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v3_2026-03-26_1932b.md` | Historical | V1.0 snapshot (same content — all 4 converged to identical final state) |
| `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_2026-03-26_2046.md` | Historical (V1.1 final) | The final V1.1 master — 73 rules, superseded by V2.0 |

> **Note:** v1 through v4 are byte-identical. All four iterations converged to the same final state during the March 26 session. They are kept as separate files for timestamp provenance (F11) — each filename records when that iteration was saved. If you need the V1.1 base rules, any of the four files will do; v4 is conventional.
| `APPENDIX_C_ERROR_CLASSIFICATION.md` | Active reference | Error classification taxonomy (6 classes). Still current. |
| `APPENDIX_D_OPERATING_CADENCE.md` | Active reference | Operating cadence (6 operational points). Still current. |
| `Document_1_STIX_Authority_Ladder.md/.pdf` | Governance reference | 5-level authority ladder for all STIX documents. Still current. |
| `E20_RETIREMENT_RECORD.md` | Provenance | Formal retirement record for rule E20 (per Appendix B evolution rules) |
| `PROTOCOL_v1.0_archived.md` | Historical | The very first STIX protocol draft from March 25, 2026 |

---

## Why keep historical snapshots?

STIX operates under **F11 — Preserve Provenance Always.** Every rule change is traceable back to the version where it was introduced, modified, or retired. Deleting old versions would break the provenance chain and violate the framework's own rules about its own evolution.

If you're debugging "why does rule X exist?" or "when was rule Y added?", this folder is where you look. Otherwise, ignore it and use the V2.0 files at the repo root.

---

## Where to actually start reading

- **New user?** Go to [`../README.md`](../README.md) and [`../CLAUDE.md`](../CLAUDE.md).
- **Want the current rulebook?** [`../STIX_V2.0_MASTER_PROTOCOL.md`](../STIX_V2.0_MASTER_PROTOCOL.md)
- **Stuck on something?** [`../TROUBLESHOOTING.md`](../TROUBLESHOOTING.md)
- **Want to see how STIX evolved?** Read v1 → v2 → v3 → v4 in order, then compare to the V2.0 master.

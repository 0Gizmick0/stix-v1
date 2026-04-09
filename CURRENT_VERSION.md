---
title: STIX Current Version
status: AUTHORITATIVE
last_updated: 2026-04-08
---

# STIX — Current Active Version

**Current law:** STIX V2.0
**Active rule count:** 148 (141 distributed + 7 gated, host-only)
**Source of truth:** `./CORE_PROTOCOL/` (V1.1 base) + this repository's per-protocol files
**V2 additions:** OBSERVE, RISK, ECON, RELAY (now active, see per-protocol summaries)
**Governance file:** `./CLAUDE.md`

## Rule Count Breakdown

| Article | Protocol | Rule range | Count | Governing value |
|---------|----------|-----------|-------|-----------------|
| I | VERDICT | V1–V7 | 7 | JUDGMENT |
| II-E | APEX Execution | E1–E25 | 25 | PRECISION |
| II-C | APEX Communication | C1–C15 | 15 | PRECISION |
| II-X | APEX Exactness | X1–X13 | 13 | PRECISION |
| III | FORGE | F1–F13 | 13 | ALIGNMENT |
| IV | CIPHER | G1–G11 | 11 | INTEGRITY |
| V | RELAY | RL1–RL8 | 8 | INTEGRITY |
| VI | ARCHITECT | A1–A20 | 20 | JUDGMENT |
| VII | OBSERVE | OB1–OB8 | 8 | TRANSPARENCY |
| VIII | RISK | RK1–RK8 | 8 | SAFETY |
| IX | ECON | EC1–EC6 | 6 | EFFICIENCY |
| App. A | GOVERNING BOUNDARIES | B1–B7 | 7 | ALL |
| Layer | PENTEST (gated, host-only) | P1–P7 | 7 | INTEGRITY |
| **Total** | | | **148** | |

**Distribution note:** This repository ships **141 rules** (the 12 core articles).
The 7-rule **PENTEST** layer (P1–P7) is a gated offensive-security operating
framework — host-only, not distributed in this repository. Its existence is
disclosed for completeness so the rule count is honest, but its content,
handbooks, and engagement lockfile templates are not part of the public
distribution. Total active law in the source-of-truth governance file =
**148 rules across 12 articles + 1 gated layer.**

## V2.0 Activation Status

| Protocol | V1.1 status | V2.0 status |
|----------|-------------|-------------|
| VERDICT | ACTIVE | ACTIVE |
| APEX | ACTIVE | ACTIVE |
| FORGE | ACTIVE | ACTIVE |
| CIPHER | ACTIVE | ACTIVE |
| ARCHITECT | ACTIVE | ACTIVE |
| GOVERNING BOUNDARIES | B1–B3 only | B1–B7 ACTIVE |
| RELAY | proposed | **ACTIVE** |
| OBSERVE | deferred | **ACTIVE** |
| RISK | deferred | **ACTIVE** |
| ECON | deferred | **ACTIVE** |
| PENTEST | n/a | gated, host-only — not distributed |

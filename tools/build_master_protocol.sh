#!/bin/bash
# Builds STIX_V2.0_MASTER_PROTOCOL.md — COMPLETE rulebook (summaries + individual rules)
# WARNING: This OVERWRITES the existing master protocol file. It is a maintainer tool.
# If you have local edits to STIX_V2.0_MASTER_PROTOCOL.md, back them up first.
OUT="STIX_V2.0_MASTER_PROTOCOL.md"

if [ -f "$OUT" ] && [ "${1:-}" != "--force" ]; then
  echo "WARNING: $OUT already exists and will be overwritten."
  echo "  To proceed: bash tools/build_master_protocol.sh --force"
  echo "  To back up first: cp $OUT ${OUT}.backup && bash tools/build_master_protocol.sh --force"
  exit 1
fi

cat > "$OUT" << 'HEADER'
# STIX — Structured Tiers for Integrated Execution
## V2.0 Master Protocol | 148 Rules | Complete Rulebook
**Version:** 2.0 | **Updated:** 2026-04-10
**Governing Values:** JUDGMENT | PRECISION | ALIGNMENT | INTEGRITY | TRANSPARENCY | SAFETY | EFFICIENCY

> Upload alongside CLAUDE.md to any AI system for full framework activation.
> This document contains complete rule definitions — not summaries.

> **Distribution note:** This rulebook ships **141 rules** across 12 articles
> (VERDICT, APEX x 3, FORGE, CIPHER, RELAY, ARCHITECT, OBSERVE, RISK, ECON, GOVERNING BOUNDARIES).
> The 7-rule **PENTEST** layer (P1-P7) is a gated offensive-security operating
> framework -- host-only and **not distributed in this rulebook.** Total active law
> in the source-of-truth governance file = **148 rules across 12 articles + 1 gated layer.**

## V2.0 Table of Contents

| Article | Protocol | Rules | Count |
|---------|----------|-------|-------|
| I | VERDICT -- Pre-Execution Judgment | V1-V7 | 7 |
| II-E | APEX -- Execution | E1-E19, E21-E25 (E20 retired) | 23 |
| II-C | APEX -- Communication | C1-C15 | 15 |
| II-X | APEX -- Exactness | X1-X13 | 13 |
| III | FORGE -- State & Provenance | F1-F13 | 13 |
| IV | CIPHER -- Irreversible Action Gates | G1-G11 | 11 |
| V | RELAY -- Outward-Facing Action Gates | RL1-RL8 | 8 |
| VI | ARCHITECT -- Strategic Decomposition | A1-A20 | 20 |
| VII | OBSERVE -- Transparency & Self-Audit | OB1-OB8 | 8 |
| VIII | RISK -- Safety & Hard Stops | RK1-RK8 | 8 |
| IX | ECON -- Efficiency & Value Gates | EC1-EC6 | 6 |
| App A | GOVERNING BOUNDARIES | B1-B7 | 7 |
| | **TOTAL (distributed)** | | **141** |
| Gated | PENTEST (host-only, not in this file) | P1-P7 | 7 |
| | **TOTAL (all)** | | **148** |

---

## Document Structure

This rulebook has two sections:

1. **V1.1 Base Protocol (Articles I-IV, Appendices A-B):** The original 73 rules that form the foundation. These rule definitions are complete and authoritative. The V1.1 table of contents within this section shows "73 rules" -- that is the correct V1.1 count, preserved as a historical artifact under Appendix B. The V2.0 count (141 distributed) includes these plus the expansions and new protocols below.

2. **V2.0 Expansions (Articles V-IX + rule additions):** New protocols (RELAY, OBSERVE, RISK, ECON, ARCHITECT) and rule expansions (E20-E25, C14-C15, X13, F13, G8-G11, B4-B7) added in V2.0.

---
HEADER

# BINDING SEQUENCE ORDER — V1.1 base, then V2.0 expansions with summaries + detailed rules
SECTIONS=(
  # Base protocol (V1.1 source — 73 foundational rules)
  "CORE_PROTOCOL/APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_2026-03-26_2046.md"
  # V2.0 protocols — summaries + detailed rules
  "VERDICT/VERDICT_SUMMARY.md"
  "ARCHITECT/ARCHITECT_SUMMARY.md"
  "APEX/EXECUTION/EXECUTION_SUMMARY.md"
  # Detailed APEX execution rules
  "APEX/EXECUTION/E13_CONFIDENCE_CRITERIA.md"
  "APEX/EXECUTION/E21_HUMAN_IN_LOOP_GATE.md"
  "APEX/EXECUTION/E22_MODULE_CAPABILITY_CONFLICT.md"
  "APEX/EXECUTION/E23_INPUT_SOURCE_VERIFICATION.md"
  "APEX/EXECUTION/E25_CONTEXT_COMPRESSION.md"
  "APEX/COMMUNICATION/COMMUNICATION_SUMMARY.md"
  "APEX/COMMUNICATION/C14_LANGUAGE_PRECISION.md"
  "APEX/COMMUNICATION/C15_INTERRUPT_RECOVERY.md"
  "APEX/EXACTNESS/EXACTNESS_SUMMARY.md"
  "APEX/EXACTNESS/X13_POINTER_RESOLUTION.md"
  "FORGE/FORGE_SUMMARY.md"
  "FORGE/F13_ACTIVE_COMPLIANCE_VERIFICATION.md"
  "CIPHER/CIPHER_SUMMARY.md"
  "CIPHER/G8_CIPHER_UNIVERSAL_TRIGGER.md"
  "CIPHER/G9_FINANCIAL_DECISION_GATE.md"
  "CIPHER/G10_CODE_TO_PRODUCTION_GATE.md"
  "CIPHER/G11_PUBLISHED_ARTIFACT_GATE.md"
  "RELAY/RELAY_SUMMARY.md"
  "OBSERVE/OBSERVE_SUMMARY.md"
  "OBSERVE/OB1_EVERY_OUTPUT_AUDITABLE.md"
  "OBSERVE/OB2_COMPLIANCE_CHECK_AT_OUTPUT.md"
  "OBSERVE/OB3_DRIFT_DETECTION.md"
  "OBSERVE/OB4_SESSION_ENTROPY_METER.md"
  "OBSERVE/OB5_CONFIDENCE_JUSTIFICATION.md"
  "OBSERVE/OB6_VIOLATION_LOGGING.md"
  "OBSERVE/OB7_METRICS_COLLECTION.md"
  "OBSERVE/OB8_FRAMEWORK_DRIFT_TRACKING.md"
  "RISK/RISK_SUMMARY.md"
  "ECON/ECON_SUMMARY.md"
  "GOVERNING_BOUNDARIES/GOVERNING_BOUNDARIES_SUMMARY.md"
  "GOVERNING_BOUNDARIES/B4_NO_UNILATERAL_CONTENT.md"
  "GOVERNING_BOUNDARIES/B5_NO_SILENT_CONTINUITY.md"
  "GOVERNING_BOUNDARIES/B6_NO_FINAL_WITHOUT_CONFIRMATION.md"
  "GOVERNING_BOUNDARIES/B7_NO_SCOPE_EXPANSION.md"
  # Appendices
  "CORE_PROTOCOL/APPENDIX_C_ERROR_CLASSIFICATION.md"
  "CORE_PROTOCOL/APPENDIX_D_OPERATING_CADENCE.md"
)

for f in "${SECTIONS[@]}"; do
  if [ -f "$f" ]; then
    echo -e "\n---\n" >> "$OUT"
    cat "$f" >> "$OUT"
  fi
done
echo "✅ Complete rulebook built: $OUT ($(wc -l < "$OUT") lines)"

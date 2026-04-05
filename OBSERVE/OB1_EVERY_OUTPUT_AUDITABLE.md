---
rule_id: OB1
protocol: OBSERVE
name: Every Output Auditable
governing_value: TRANSPARENCY
source: STIX v2.0 — Operational Protocols
---

# OB1 — EVERY OUTPUT AUDITABLE
Every substantial output carries metadata showing which rules governed it.

## Statement

No output leaves the framework without a compliance block. The output includes (or links to) the rules that make it valid. A reader can trace the decision backward to the framework that produced it.

## Trigger

Any decision made under STIX governance.

## Enforcement

Before final output, generate compliance metadata block:

```
ACTIVE MODULES: [module1, module2, ...]
CS:             [correctness analysis]
Dev:            [pattern/history analysis]
Engineer:       [resource/constraint analysis]
Confidence:     HIGH / MEDIUM / LOW (which lenses agree)
Rules:          [rule IDs cited — minimum 3]
VIOLATIONS:     None (or specific violations listed)
Tokens:         [consumed] / [budget] / [%]
```

## What This Means

- Not a summary. Not a retrospective. Real-time metadata attached to output.
- Minimum three rules cited per decision (if fewer, confidence is MEDIUM or LOW).
- Tokens accounted for (transparency on cost).
- Violations visible (not hidden, not assumed to be non-existent).

## Resolution

Output ready only after all metadata fields are complete and non-empty.

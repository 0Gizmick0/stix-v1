# STATUS — Current Measured Enforcement Coverage

> **Read this file if you want to know what STIX actually does vs what it claims.**
> All numbers in this file come from audit logs and gap analysis on the host development system. They are updated as development progresses. This document exists because honesty about partial enforcement is more valuable than marketing about total enforcement.

**Last updated:** 2026-04-09
**Source data:** `GAP_ANALYSIS.md` (host dev system), audit logs across 13 projects, session handoff records

---

## Summary in one sentence

STIX is partially enforced: irreversible-action gates (CIPHER) work reliably, structural rules work unevenly depending on the model and conversation length, and judgment-class rules require human review because they cannot be mechanically enforced regardless of architecture.

---

## Enforcement coverage by protocol

| Protocol | Rules | Actually Gated | Coverage | Violation Severity | Honest Status |
|---|---|---|---|---|---|
| **CIPHER** (G1–G11) | 11 | 11 | **100%** ✅ | LOW | **HEALTHY** — the one part that actually works in practice because triggers are observable to the harness |
| **ARCHITECT** (A1–A20) | 20 | 15 | 75% ✅ | HIGH on A1, A20 | **BREAKING** — decomposition rules are cited but not enforced; A1 (concept isolation) and A20 (decomposition doc) each logged 8+ violations |
| **VERDICT** (V1–V7) | 7 | 5 | 71% ✅ | MEDIUM | **WORKING** — foundational values survive discipline but V2 (prioritize by impact) alone logged 10 violations |
| **EXECUTION** (E1–E25) | 23 | 9 | 39% 🟠 | HIGH on E25 | **BROKEN** — E25 (context compression) is the single most violated rule in the audit log (12x) |
| **FORGE** (F1–F13) | 13 | 5 | 38% 🟠 | HIGH on F13 | **BROKEN** — F13 (compliance verification) logged 9 violations — the rule that verifies compliance is itself not verified |
| **EXACTNESS** (X1–X13) | 13 | 5 | 38% 🟠 | MEDIUM | **WEAK** — X13 (pointer resolution) logged 8 violations — the AI forgets to use memory even when it exists |
| **GOVERNING BOUNDARIES** (B1–B7) | 7 | 2 | 29% 🟠 | LOW | **WEAK** — declared but not mechanically enforced |
| **COMMUNICATION** (C1–C15) | 15 | 3 | 20% 🔴 | UNKNOWN | **ABSENT** — most communication rules are pure discipline, no gates, no violation logging |
| **TOTAL** | **101** | **65** | **64%** | — | See line-item breakdown below |

> *These numbers are from a host-system audit using an earlier rule count. The distributed public repo has 141 rules + 7 gated (PENTEST, host-only) = 148 total. The per-protocol ratios are stable.*

**Bottom-line math:**
- **"Mentioned with a gate declaration"**: 65 / 101 = **64%**
- **"Active prevention, not just declaration"**: 21 / 101 = **20.8%**
- **"Self-attested with no external gate"**: ~80 / 101 = **~79%**

---

## The seven worst offenders — 63 logged violations

These are rules that CLAUDE.md claims to enforce, that the AI cites frequently, and that are nonetheless violated at high frequency because they are declared but not gated.

| Rule | Description | Logged Violations | Why It Breaks | Hookable? |
|---|---|---|---|---|
| **E25** | Context compression | **12×** | Declared in CLAUDE.md, no mechanism to measure or enforce per-turn | ✅ YES — `PreToolUse` hook measures conversation tokens, warns at threshold, denies non-essential writes above ceiling |
| **V2** | Prioritize by impact | **10×** | Declared, subjective | ❌ NO — cannot be a predicate over tool arguments |
| **F13** | Active compliance verification | **9×** | Declared, not gated | ✅ YES — `Stop` hook can regex-check response structure |
| **X13** | Pointer resolution (use memory before computing) | **8×** | Declared, the AI forgets | ✅ YES — `SessionStart` hook auto-loads memory files |
| **E13** | Confidence criteria | **8×** | Declared, self-grading is unreliable | ❌ NO — requires semantic judgment of whether the confidence level is actually justified |
| **A20** | Decomposition document | **8×** | Declared, ad-hoc enforcement | ✅ YES — `PreToolUse` on Write/Edit in project dirs: deny unless lockfile exists for MEDIUM+ projects |
| **A1** | Concept isolation | **8×** | Declared, silently skipped | ✅ YES — `SessionStart` hook can prompt for one-sentence concept before continuing |
| **Total** | — | **63** | — | **5 of 7 hookable** |

**The honest pattern**: 5 of the 7 worst offenders can be mechanically enforced once hooks ship. 2 of them (V2, E13) cannot — they are judgment rules and will stay in human-in-the-loop territory permanently.

**Projected impact of the hook fix (not yet shipped):** ~45 of 63 violations preventable = **~71% reduction** on the hookable subset.

---

## What works (the HEALTHY section)

### CIPHER (G1–G11) — 100% coverage

This is the success case. The rules that involve observable side effects (file delete, email send, git push, destructive commands, code commits to shared repos, API calls with side effects) are the ones that actually work, because the harness can see them happen and the AI cannot accidentally-or-deliberately route around them without visible signals.

**Pattern from the data:** every rule with an observable trigger works. Every rule without an observable trigger decays at 8–12 violations per few weeks on average, regardless of how emphatically CLAUDE.md asserts it.

### CHAMP principle (PDF extraction) — informal but effective

CHAMP is the one "soft" rule the AI follows reliably in practice. Why? Because the trigger (`.pdf` extension in a Read call) is so crisp the AI cannot miss it, and the cost justification (~20× tokens) is obvious. This is not yet a hook; it works on discipline alone. Once the hook layer ships, it will move to mechanical enforcement (log every `.pdf` Read, deny unless extraction happened first).

---

## What doesn't work (the BROKEN section)

### E25 — Context compression (12 logged violations)

CLAUDE.md says "compress context at N message threshold." Nothing measures the conversation length per-turn. The AI does not reliably notice when the threshold is crossed. The rule is declared and ignored.

**Evidence from a real session:** a recent session blew 14,000 tokens on CLAUDE.md bootstrap alone before answering its first real question. That is roughly 280% of a stated "quick task" budget. The rule the AI violated is the rule the file loading it declares.

### F13 — Compliance verification (9 logged violations)

F13 says "verify compliance before declaring work complete." The AI declares work complete and then the user finds the violations. Meta-observation: in the recent audit session itself, 5 bootstrap gates were violated and 0 were self-caught — the user surfaced all 3 of the meaningful violations via direct questioning.

**The irony:** the rule whose entire purpose is compliance verification is itself unverified, and the user catches 100% of violations via external review. Self-attestation does not work.

### Bootstrap steps (0/6 executed in a recent session)

CLAUDE.md has a 6-step session-open bootstrap (read handoff, identify project, load state, activate lenses, declare protocol, write audit trace). In a recent audit session, 0 of 6 were executed. The AI skipped bootstrap entirely and went straight to the user's first question. No gate caught it. The user only noticed when they asked a question that required the prior-session context the bootstrap was supposed to load.

### V5 — Document during work (ongoing violation)

V5 requires `session_state/current.md` to exist and be updated during work. On the host system, `current.md` does not currently exist. V5 + STEP 3 + STEP 5 have been silently failing for multiple sessions. The rule is declared "mandatory" in CLAUDE.md and no mechanism has ever caught its absence.

---

## The meta-evidence: `~/.claude/settings.json = {}`

The Claude Code harness has a native enforcement channel: hooks configured in `~/.claude/settings.json`. On the host development system, that file is literally **3 bytes** (`{}`) — zero hooks configured. The one channel the harness provides for external enforcement has never been used.

Every rule in CLAUDE.md is self-attested because the one gate the harness provides for external enforcement has been left empty. Every violation in the audit logs is a consequence of that gap. The fix (hook-based enforcement) addresses exactly this.

---

## Work in progress

### Near-term (this week)

1. **Observability-only hook proof-of-concept.** A 20-line `PreToolUse` hook that logs every Read tool call to `/tmp/stix-hook.log`. No gating, no denying — pure observation. Proves the mechanism actually fires before any enforcement logic is built on top of it. **Status: mandated, not yet run.**
2. **Repo honesty pass.** This document exists as part of that pass. Other deliverables: README rewrite to drop "forced to" language, CHAMP reframe from shell command to principle, explicit acknowledgment of the human-in-the-loop requirement. **Status: in progress at the time of this writing.**

### Medium-term (next few sessions)

3. **`stix-gate.sh`** — the actual enforcement script that regex-checks the AI's output for structural compliance markers (Confidence line, three lens blocks, Violations section, rule ID validity). Validated against a labeled corpus of recorded audit-log responses before deployment.
4. **`stix-rules.yaml`** — machine-readable manifest of which rules the gate checks, with triggers and actions.
5. **`~/.claude/settings.json` wiring** — the first-ever nonempty settings.json on the host system, pointing hooks at the validated `stix-gate.sh`. CIPHER-gated, rollback is one `mv` command away.

### Longer-term

6. **Llama sandbox staging environment.** A local Llama 3B instance running the full unmodified host STIX framework as a mirror staging environment. Framework edits get tested against the sandbox before promoting to host. The sandbox is the first production-mirror staging environment STIX has ever had.
7. **LLM-specific `*_LITE.md` variants.** `GPT_LITE.md`, `GEMINI_LITE.md`, and tool-use-capable variants so that STIX ships with production-tested operating manuals for more than just Claude Code.
8. **Per-rule coverage tracking.** Replacement of the current project-level audit log with a rule-indexed log that shows which rules are violated by which models in which contexts. Moves the numbers in this STATUS.md from "updated periodically by hand" to "computed automatically from logs."

---

## What will never work mechanically

Be honest about what cannot be fixed regardless of how much engineering we throw at it:

- **V1 (Judgment)** — foundational value, cannot be mechanized
- **V2 (Prioritize by impact)** — subjective, cannot be predicate over tool args
- **V3 (Assume competence)** — social/epistemic, not mechanical
- **V7 (Know your limits)** — requires self-awareness, cannot be regex'd
- **C1–C7 (Output clarity)** — subjective
- **E13 confidence labels** — self-grading language, unreliable when the model is both the actor and the grader
- **X2–X12 (Clarity disciplines)** — subjective
- **A2–A9 (validation & decomposition judgment)** — subjective within structure

These rules require **human review**. The hook layer does not pretend to enforce them. It stops pretending.

**Practical implication:** for anything that matters, STIX gives you a structured, auditable output — and **you still have to read it**. The framework makes the AI's reasoning visible, not correct. Correctness still lives in human review.

---

## How to verify these numbers yourself

If you have access to a STIX development system (host or your own clone), the numbers in this file can be reproduced:

```bash
# Count rules per protocol
grep -c "^###.*\`" STIX_V2.0_MASTER_PROTOCOL.md

# Count violations by rule across audit logs
grep -rn "violated\|reverted\|caught by user" path/to/audit_log.md | \
  grep -oE "[VEFGCXABR][0-9]+" | sort | uniq -c | sort -rn

# Check hook configuration
cat ~/.claude/settings.json
wc -c ~/.claude/settings.json
```

On the development host at the time of this writing: `wc -c ~/.claude/settings.json` returns **3** (literally `{}`). The enforcement channel has never been touched. That is the root cause of every number in this document.

---

## Honest pitch

STIX is not finished. The parts that work, work because they have observable triggers. The parts that don't work, don't work because they depend on the AI to self-enforce — and the AI does not reliably self-enforce, as measured by the 63 logged violations on the seven "worst offender" rules.

The fix (hook-based enforcement) is designed, evidenced, and planned. It is not yet shipped. Until it ships, STIX is a thinking discipline with hard gates only on irreversible actions, and **the human in the loop is the load-bearing enforcement mechanism for everything else.**

If that tradeoff is acceptable to you — and for most users thinking about governance at all, it is — then STIX is useful right now, today, in its current partial state. If you need total mechanical enforcement today, STIX is not yet it.

This file will be updated as the hook layer ships and measured coverage changes.

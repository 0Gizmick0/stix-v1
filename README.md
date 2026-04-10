# STIX — A Governance Framework for AI

<sub>**Version:** STIX V2.0 · **Rules:** 148 (141 distributed + 7 gated host-only) · **Last updated:** 2026-04-08 · **License:** AGPL-3.0</sub>

**STIX is a rulebook for AI.** You paste it into Claude, ChatGPT, Gemini, or any LLM as a system prompt, and it tries to make the AI think more carefully before it answers you. It is free (AGPL-3.0), works in any chat UI or API, and takes about 60 seconds to install.

> **Read this first — what STIX is, honestly:**
>
> STIX is a **discipline, not a forcing function.** It is a set of instructions the AI is asked to follow. A strong model (Claude Opus, Claude Sonnet, GPT-4o, Gemini Ultra) will follow most of the rules most of the time. A weak model will ignore them. Long conversations still drift even on strong models. **The human in the loop is still required** — STIX makes the AI's reasoning visible and auditable, but it does not replace human review. You still have to read what the AI says.
>
> Think of it as a playbook you hand to a new employee. A good employee reads it and refers back. A lazy employee skims it. The playbook is clear, but it cannot force anyone to read it.

## What STIX tries to get the AI to do

When loaded into a capable model, STIX asks the AI to:

- **Think through every decision using three analytical lenses at the same time** (Computer Scientist, Software Developer, Engineer) — see the Three Lenses section below, this is the single most important thing in STIX
- **Declare confidence** (HIGH / MEDIUM / LOW) before making a recommendation, with a short justification showing which lenses agreed
- **Stop and ask before doing anything irreversible** (sending email, deleting files, pushing code, running destructive commands) — **this is the one part of STIX that works reliably**, because the triggers are observable to the harness
- **Show its reasoning** in a structured, auditable form
- **Flag its own violations** when it notices them (this works unevenly — humans still catch more than the AI self-catches)

## What STIX does NOT do (also honestly)

- **STIX does not force anything.** Instructions are suggestions weighted against all the other suggestions the model absorbed during training. A strong model will mostly comply; a weak model will mostly ignore.
- **STIX cannot enforce judgment calls mechanically.** Rules about "prioritize by impact" or "is this the right confidence level" depend on the AI making a judgment that you trust. If the AI's judgment is wrong, only a human reviewing the output can catch it. This is called **human-in-the-loop** and it is **not optional for serious work.**
- **STIX drifts over long conversations.** As context fills, even strong models start to forget earlier rules. Periodically ask the AI to re-declare the protocol state.
- **Weak models can't follow it.** Models below roughly 70B parameters struggle with long structured instructions regardless of prompting.
- **Current measured enforcement is partial.** Only CIPHER (the irreversible-action hard gates) is near 100% reliable, because its triggers are observable (file delete, email send, git push). Other rules (judgment, confidence, prioritization, documentation) are at lower coverage and depend on the model choosing to follow them. **See [`STATUS.md`](STATUS.md) for the honest rule-by-rule coverage breakdown.**

## Is STIX right for you?

**Use STIX if:**
- You use AI for decisions that matter (architecture, code review, research, writing)
- You want the AI to show its work instead of just handing you an answer
- You want a consistent discipline across different AI tools (Claude, ChatGPT, Gemini)
- You are willing to read the AI's output and catch mistakes — STIX makes them visible, not impossible

**Don't bother if:**
- You want quick answers and don't care about the reasoning
- You're using a small/weak model that can't follow long structured instructions
- You aren't willing to review the AI's output (STIX surfaces problems but does not fix them for you)

> **Status:** STIX V2.0 — 148 rules across 12 articles + 1 gated layer
> **What's the gated layer?** 7 of the 148 rules form a host-only offensive-security operating layer (PENTEST). They're disclosed for honest rule-count accounting but not distributed in this repository. The 141 rules in this repository constitute a complete general-purpose AI governance framework.

---

## ⚡ Quick Start

### Option A — Browser chat (recommended for most users)

**Works on any OS. No install. No git. Under 5 minutes.**

1. **Download [`CLAUDE_LITE.md`](https://raw.githubusercontent.com/0Gizmick0/stix-v1/main/CLAUDE_LITE.md)** (right-click → Save As, or open and copy the contents).
2. Open a **new chat** in Claude.ai, ChatGPT, Gemini, or any capable LLM.
3. **Paste the entire contents** of `CLAUDE_LITE.md` as your first message. Send.
4. The AI should respond with a load-confirmation block (`STIX V2.0 LOADED — browser mode`). If it doesn't, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
5. Done. The AI is now governed by STIX.

`CLAUDE_LITE.md` is ~2,500 tokens — small enough to paste in any chat UI. It enforces the same 141 rules as the full version, just without filesystem-dependent bootstrap steps that don't work in a browser. See **[`GETTING_STARTED.md`](GETTING_STARTED.md)** for a detailed walkthrough with expected outputs and troubleshooting.

### Option B — Claude Code / Cursor / IDE

> **Claude Code users:** There is a dedicated edition built specifically for Claude Code — [**stix-cc**](https://github.com/0Gizmick0/stix-cc). It ships with hooks pre-wired, session continuity across conversations, a one-command installer for Linux and Windows, and everything configured so you get a governed session from the first message. If you are using Claude Code as your primary tool, start there instead.

```bash
git clone https://github.com/0Gizmick0/stix-v1.git
cd stix-v1
bash tools/stix-setup.sh              # creates project files for session bootstrap
```

The setup script creates `projects/my-first-project/` with the `about.md` and `audit_log.md` that the bootstrap expects. Your project data stays local (gitignored). To name your project: `bash tools/stix-setup.sh my-project-name`

Claude Code auto-loads `CLAUDE.md` from the working directory. Open the repo and start working.

**Windows (no WSL)?** Create the directories manually:
1. Create folder: `projects\my-first-project\`
2. Copy `templates\about_template.md` to `projects\my-first-project\about.md`
3. Copy `templates\audit_log_template.md` to `projects\my-first-project\audit_log.md`
4. Edit both files: replace `[Project Name]` with your project name and `[YYYY-MM-DD]` with today's date

### Option C — API (Python)

```python
import anthropic

with open("CLAUDE.md") as f: claude_md = f.read()
with open("STIX_V2.0_MASTER_PROTOCOL.md") as f: rules = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6",
    system=f"{claude_md}\n\n{rules}",   # ← STIX goes in `system`, not `messages`
    messages=[{"role": "user", "content": "Your task here."}],
)
```

### Option D — Full CLAUDE.md + master protocol (advanced)

If you want the full filesystem-aware version with session state, audit logs, and project management:

1. Open `CLAUDE.md`, copy the entire contents, paste it as your first message in a new chat. Send.
2. Attach `STIX_V2.0_MASTER_PROTOCOL.md` as a file in your next message (or paste it if your UI accepts long pastes).
3. Send: *"Confirm you have STIX V2.0 (148 rules) loaded. Apply three-lens thinking to every decision from now on."*

> **⚠️ Big-paste warning:** `STIX_V2.0_MASTER_PROTOCOL.md` is ~80,000 tokens. Some chat UIs reject pastes that large. If yours does, see [TROUBLESHOOTING.md → Gate 1](TROUBLESHOOTING.md#-gate-1--loading-stix-into-your-ai) for alternatives. The simplest workaround: just use Option A above.

### Don't use git? Download as ZIP

If you don't have git installed, you can download the entire repository as a ZIP file:

**[Download ZIP](https://github.com/0Gizmick0/stix-v1/archive/refs/heads/main.zip)** — or click the green **Code** button on the repo page → **Download ZIP**.

Unzip it anywhere. All files are plain text (`.md`). Open them in any text editor, Notepad, VS Code, or just read them on GitHub.

---

## ✅ How to Verify STIX is Actually Active

Paste this exact prompt to your AI after loading:

> *"Apply STIX three-lens thinking to this decision: should I use REST or GraphQL for a new internal API with 5 known consumers and unclear future query patterns? Show CS lens, Developer lens, Engineer lens, confidence level, and cite at least 2 STIX rule IDs."*

**A correctly-loaded session will respond with explicit lens analysis and rule IDs (e.g. `E13`, `E15`).** If you get a generic answer with no lens labels and no rule IDs, STIX did not load — see [TROUBLESHOOTING.md → Gate 2](TROUBLESHOOTING.md#-gate-2--verifying-stix-is-active).

---

## What STIX Actually Does (Concrete Example)

**Without STIX:**
> User: *"Should I deploy the new auth system to production?"*
> AI: *"Looks good to me — go for it!"*
> [Deploys. Crashes under load. Rollback at 3am.]

**With STIX:**
> User: *"Should I deploy the new auth system to production?"*
> AI: *"Applying ARCHITECT phase first (A1, A4).*
> *Concept: Deploy new auth to production.*
> *Critical-path question (A4): What happens if the database connection pool fills up under real load?*
> *CS lens: Auth flow is O(1) per request, but session creation requires DB write. Edge case: pool exhaustion → cascading failures.*
> *Developer lens: We've never load-tested this auth path against production volume. Past pattern: 3 of our last 5 auth deploys failed on first deploy.*
> *Engineer lens: No rollback plan documented. No feature flag. Irreversible without downtime.*
> *Confidence: LOW (E13). RK2 hard stop triggered: irreversible + critical + missing load-bearing detail.*
> ***RECOMMENDATION: Do not deploy. Add feature flag, add rollback runbook, run load test against staging first. Then re-evaluate.***"

**That's it.** STIX is a discipline that surfaces what your AI already could have known, before it costs you.

---

## The 12 Protocols (What's in the Box)

| Protocol | Rules | Governing Value | What It Does |
|---|---|---|---|
| **VERDICT** | V1–V7 (7) | Judgment | Foundational decision values — is this even the right goal? |
| **APEX Execution** | E1–E25 (25) | Precision | How to actually build things |
| **APEX Communication** | C1–C15 (15) | Precision | How to talk to and with the AI |
| **APEX Exactness** | X1–X13 (13) | Precision | Clarity disciplines — define before execute |
| **FORGE** | F1–F13 (13) | Alignment | State, files, databases, provenance |
| **CIPHER** | G1–G11 (11) | Integrity | Hard gates for irreversible outputs (email, deletes, deploys) |
| **RELAY** | RL1–RL8 (8) | Integrity | Hard gates for outward-facing actions (APIs, publishing) |
| **ARCHITECT** | A1–A20 (20) | Judgment | Decompose hard problems before touching them |
| **OBSERVE** | OB1–OB8 (8) | Transparency | Real-time compliance — every output is auditable |
| **RISK** | RK1–RK8 (8) | Safety | Hard stops, kill switches, scope-creep detection |
| **ECON** | EC1–EC6 (6) | Efficiency | Token/time/cost gates — is this work even worth doing? |
| **GOVERNING BOUNDARIES** | B1–B7 (7) | All values | Architectural hard stops — never, period |

**Total: 141 rules distributed in this repository, + 7 gated host-only (PENTEST) = 148.**

---

## The Three Lenses — the core mechanic you must understand

**This is the single most important thing in STIX. If you only remember one section of this README, remember this one.**

Every time the AI makes a decision under STIX, it is asked to run the decision through three different ways of thinking **at the same time** — not one after the other. The response should have three labeled blocks, one per lens, with actual analysis in each.

### 🧠 Lens 1 — Computer Scientist

**Asks:** *"Is this actually correct? What are the edge cases? What's the complexity? What am I assuming that I haven't tested?"*

**Catches:** hand-waving, untested assumptions, edge cases that would blow up in production, algorithms that don't terminate, "this should work" statements with no analysis behind them.

**Example of GOOD CS-lens output:**
> *"Algorithm: hash lookup, O(1) average case, O(n) worst case on collision. Failure modes: (a) empty input → return null, (b) hash collision attack → mitigate with randomized hash seed. Tested assumption: dictionary contains fewer than 10^6 entries → holds for current data."*

**Example of BAD CS-lens output (this is NOT real three-lens thinking):**
> *"The computer science lens says this should work."* ← No analysis, just a label.

### 🔧 Lens 2 — Software Developer

**Asks:** *"Have we done this before? What failed last time? How does this fit with the existing system? What's the rollback if it breaks?"*

**Catches:** repeating past mistakes, ignoring prior art, integration friction with existing code, plans that sound good in isolation but fight the existing system, missing rollback strategies.

**Example of GOOD Developer-lens output:**
> *"The last two auth rewrites in this codebase failed on session handling — cookies vs JWTs got mixed. This time we pick one and enforce it via middleware. Integration: touches `auth_router.py` and `session_store.py`, both have tests. Rollback: feature flag `new_auth_v2`, off by default, flip per-user for canary."*

**Example of BAD Developer-lens output:**
> *"This should integrate fine with existing code."* ← Not checked against history, no prior art consulted.

### 📐 Lens 3 — Engineer

**Asks:** *"Can we afford this? What's the bottleneck? What's the degradation path if a resource runs out?"*

**Catches:** budget blowups, missing rollback plans, fragile single-point dependencies, unsustainable resource use, plans that "might cost a lot" without measuring.

**Example of GOOD Engineer-lens output:**
> *"Budget: 2 GB RAM, 15 min wall clock, within limits. Bottleneck: the hash build phase (estimated 8 min). Degradation: if memory runs tight, fall back to disk-backed hash at 4× slowdown. Rollback: entire operation is a single SQL transaction, commit-or-abort, no cleanup needed."*

**Example of BAD Engineer-lens output:**
> *"This might cost a lot of tokens but should be fine."* ← Not measured, no bottleneck identified, no degradation plan.

### All three at once — not sequentially

STIX does NOT ask the AI to run the lenses in order ("first CS, then Developer, then Engineer"). It asks the AI to **see through all three simultaneously**, so every decision is already checked against all three concerns by the time the AI opens its mouth. You can tell it's working when the AI's response has labeled `CS lens:`, `Dev lens:`, `Engineer lens:` blocks with real analysis inside each — and when the final recommendation demonstrably reflects agreement or tension between them.

### Confidence declarations (follow directly from lens agreement)

After running the three lenses, the AI must declare its confidence:

- **HIGH** — all three lenses agree, no rule violations, all load-bearing assumptions verified. Execute.
- **MEDIUM** — two of three agree, OR all three agree but with one recoverable minor risk. Execute with a named rollback plan.
- **LOW** — fewer than two lenses agree, or a critical assumption is unconfirmed, or a hard rule is being violated. **STOP.** Escalate to the human.

### What to do if the AI skips the lenses

Reply: *"Run the three lenses on this. Show CS lens, Dev lens, Engineer lens as separate blocks with actual analysis in each. Declare confidence with justification."*

A capable model should recover. If it can't recover after three tries, the model is too weak to run STIX — try a stronger model.

---

## Known Limitations — Things STIX Cannot Fix

**Read this section.** These are real limitations of the current state, not marketing. If you use STIX without understanding them, you will be surprised.

### 1. The human in the loop is still required — this is not optional

Rules about **judgment** (prioritization, confidence, taste, "is this the right goal") cannot be mechanically enforced. No regex catches a bad judgment call. No filter catches a wrong confidence level. **Only a human reviewing the output can catch a wrong judgment.**

STIX is designed to make the AI's reasoning **visible and auditable**, which is the necessary condition for effective human review. It does not replace the review. If you run STIX and then don't read what the AI says, you will miss things STIX itself cannot catch.

**Practical implication:** for anything that matters, treat STIX as "the AI shows its work so you can grade it," not as "the AI is safe to trust."

### 2. The AI cites rules as decoration — watch for this

The most common failure mode is the AI naming rule IDs (`A1, E13, V2`) in prose without the rules actually doing any work. It looks compliant. It isn't.

**The test:** delete the rule IDs from the sentence. If the sentence means the same thing without them, the rules were decorative, not load-bearing.

**The fix:** reply *"Your rule citations are decorative. Delete the rule IDs from your sentence — if it means the same thing, the rules weren't doing any work. Re-run and make the rules load-bearing."*

### 3. Long conversations drift — STIX fades over many turns

Even strong models have finite attention. After many turns, the early STIX instructions get weighted less and the AI starts giving looser, more generic responses. This is a limitation of current LLM attention mechanisms, not a bug in STIX.

**The fix:** periodically say *"Re-declare STIX protocol state and resume."* If that stops working, start a fresh conversation.

### 4. Weak models can't follow STIX regardless of how well it's written

STIX is ~14,000 tokens of structured instructions. Models below roughly 70B parameters struggle with long structured instructions regardless of prompting.

**Use:** Claude Opus, Claude Sonnet, GPT-4o, Gemini Pro/Ultra.

**Don't use:** Small/cheap models for serious STIX work. They will be inconsistent and you'll blame the framework for a model limitation.

### 5. Current measured enforcement is partial, not total

**Only CIPHER (the irreversible-action gates — G1 through G11) is near 100% reliable in practice.** Its triggers are observable (file delete, email send, git push, code commit) so the harness itself can enforce them, not just the AI's willpower.

Everything else — three-lens thinking, confidence declarations, A1/A20 decomposition, E25 context budgets, F13 compliance verification — depends on the AI choosing to follow the rule. **Measured coverage on those rules is significantly lower than 100%.** See [`STATUS.md`](STATUS.md) for honest rule-by-rule numbers.

### 6. Hook-based enforcement is in progress, not shipped

The missing piece that would raise enforcement from "discipline" to "hard gate" on the harness-enforceable subset is an external hook layer that runs in the Claude Code harness (or equivalent) before the AI's output is shown to you. **This does not yet exist in shipped form.** It is actively being built. See [`STATUS.md`](STATUS.md) → "Work in Progress" for the roadmap.

Until that ships, the honest framing is: **STIX is a discipline that makes AI reasoning visible, with hard gates only on the irreversible-action subset (CIPHER). Everything else is asking the AI nicely.**

### 7. Loading the full framework is expensive

The full `CLAUDE.md` + `STIX_V2.0_MASTER_PROTOCOL.md` together are ~80,000+ tokens. Every session pays that cost before the first real question. For most users the simpler `CLAUDE_LITE.md` (a browser-safe variant at ~2,500 tokens) is the better starting point — it drops the filesystem-dependent bootstrap and focuses on the thinking discipline, which is the load-bearing part.

---

## Repository Layout

```
stix-v1/
│
├── README.md                          ← You are here
├── CLAUDE.md                          ← System prompt (paste this into your AI)
├── STIX_V2.0_MASTER_PROTOCOL.md       ← Complete rule definitions (upload this too)
├── CURRENT_VERSION.md                 ← Version pointer (148 rules, 12 articles)
├── STIX_INDEX.md                      ← Index of all per-protocol folders
├── TROUBLESHOOTING.md                 ← Common issues + fixes (read this when stuck)
├── LICENSE                            ← AGPL-3.0
│
├── CORE_PROTOCOL/                     ← Historical V1 → V1.1 snapshots (provenance only)
│
├── VERDICT/                           ← V1–V7 summary
├── APEX/EXECUTION/                    ← E1–E25 + per-rule deep dives where needed
├── APEX/COMMUNICATION/                ← C1–C15 summary + per-rule detail
├── APEX/EXACTNESS/                    ← X1–X13 summary
├── FORGE/                             ← F1–F13 summary
├── CIPHER/                            ← G1–G11 summary + per-rule detail
├── ARCHITECT/                         ← A1–A20 (3 files: SUMMARY, PROTOCOL, PROTOCOL_INTEGRATED)
├── RELAY/                             ← RL1–RL8 summary
├── OBSERVE/                           ← OB1–OB8 summary + all 8 per-rule files
├── RISK/                              ← RK1–RK8 summary
├── ECON/                              ← EC1–EC6 summary
├── GOVERNING_BOUNDARIES/              ← B1–B7 (all 7 individual files + summary)
│
├── v2.0/                              ← V1 → V2 design and migration documents
├── templates/                         ← Project file templates (about.md, audit_log.md)
└── tools/
    ├── champ.py                       ← PDF-to-text extractor (saves ~95% tokens)
    ├── build_master_protocol.sh       ← Maintainer script (rebuilds master protocol)
    └── stix-update.sh                 ← Maintainer script (checks for updates)
```

### File-naming convention

- **`<PROTOCOL>_SUMMARY.md`** in each folder is the **canonical, complete rule list** for that protocol.
- **Per-rule files** (e.g. `E13_CONFIDENCE_CRITERIA.md`, `OB1_EVERY_OUTPUT_AUDITABLE.md`) exist **only where a rule needs additional operational guidance**. They're companions to the SUMMARY, not replacements.
- A protocol with only a SUMMARY file is **complete**, not unfinished.

---

## STIX and CLAUDE.md — what each file is and how they work together

This is the part that confuses people. STIX ships in **two main pieces** that play different roles:

### The rulebook: `STIX_V2.0_MASTER_PROTOCOL.md`
This is the **definition** of every rule in the framework — what V1 means, what E13 says, what G4 requires. 148 rules across 12 protocols. It is the source of truth for "what does this rule actually say." It is large (~80,000 tokens in full form). You rarely need to load all of it at once.

### The operating manual: `CLAUDE.md` (or `CLAUDE_LITE.md`)
This is the **instructions for the AI**. It references rules by ID (like "per E13, declare confidence"), defines the bootstrap sequence, the hard gates, the three lenses, the six core instincts, and the binding activation order. It does NOT contain the full rule definitions — it assumes the AI can look them up in the rulebook when needed, or that you've pasted both files.

### How they work together
Think of it like a legal system:
- **The rulebook** is the statute — the letter of the law.
- **The operating manual** is the judge's bench book — how to apply the law in real situations.

The AI needs both to function correctly:
- **CLAUDE.md alone** tells the AI what rules exist and how to operate, but not what each rule actually says when the AI needs to cite or apply it.
- **The master protocol alone** tells the AI the rules but not how to use them in session.

### Which version of CLAUDE.md should you use?

| File | Use when | Size |
|---|---|---|
| **`CLAUDE_LITE.md`** | You're pasting STIX into a browser chat (Claude.ai, ChatGPT, Gemini) where the AI has no filesystem access. This is the recommended entry point for most users. | ~2,500 tokens |
| **`CLAUDE.md`** (the full variant) | You're running Claude Code, Cursor, Continue.dev, or any IDE/CLI integration where the AI has a working directory with files it can read and write. | ~14,000 tokens |

Both files enforce the same 141 rules. The lite version just drops the filesystem-dependent bootstrap steps (audit log writes, session state files, file-read requirements) that silently fail in a browser chat. See [`GETTING_STARTED.md`](GETTING_STARTED.md) for a step-by-step walkthrough of the browser path.

---

## Built for Claude Code first — other LLMs are a work in progress

**Honest disclosure:** STIX was designed and actively developed against **Claude Code** (the Anthropic CLI that auto-loads `CLAUDE.md` from the working directory). That is where it was stress-tested, where the bootstrap sequence was designed, and where the host maintains an active version that tracks ahead of this public repo.

### What that means in practice

- **Claude Code (Claude Opus 4.6 / Sonnet 4.5):** primary target, best-tested, highest measured compliance. The `CLAUDE.md` filesystem-aware variant is designed for this environment specifically.
- **Browser Claude (Claude.ai):** secondary target, works via the `CLAUDE_LITE.md` variant which drops filesystem bootstrap. Measured compliance is good but not yet quantified as rigorously as Claude Code.
- **GPT-4o / GPT-4 / ChatGPT:** tested informally, compliance is decent on the thinking discipline (three lenses, confidence declarations) but CHAMP-style file handling and audit-log bootstrap do not apply. No dedicated variant yet.
- **Gemini Pro/Ultra:** tested informally, similar to GPT-4o — compliance is decent on the thinking discipline.
- **Everything below ~70B parameters:** do not use. Compliance is effectively zero because the model cannot hold the framework in active attention.

### LLM-specific variants are on the roadmap, not shipped

Work is in progress on LLM-specific variants of the operating manual so that `CLAUDE_LITE.md` is not the only non-filesystem path. Expected near-term additions:
- **`GPT_LITE.md`** — GPT-4 / GPT-4o optimized variant (different attention patterns, different instruction-following quirks)
- **`GEMINI_LITE.md`** — Gemini Pro / Ultra optimized variant
- **Tool-use variants** — for models with native function calling (so the filesystem bootstrap becomes a tool-call sequence instead of prose instructions)

Until those ship, the honest state is: **STIX currently ships one production-tested operating manual (for Claude Code) and one browser fallback (`CLAUDE_LITE.md`). Other LLMs can paste `CLAUDE_LITE.md` and get most of the value, but they are not the primary target.**

---

## Currently being worked on — increasing compliance

The gap between "STIX describes discipline" and "STIX mechanically enforces discipline" is the active development focus. The honest state is: **compliance varies by rule class.**

- **Hard gates (CIPHER — irreversible actions):** near 100% reliable. These work because the triggers are observable to the harness (file delete, email send, git push). The harness itself can see them and the AI cannot accidentally-or-deliberately route around them without visible signals.
- **Structural rules (three lenses, confidence declarations, bootstrap steps):** variable. Strong models follow these most of the time. Weak models drop them. Long conversations drift.
- **Judgment rules (prioritization, subjective confidence calibration, taste):** cannot be mechanically enforced regardless of how much engineering we add. These require **human-in-the-loop review**, always.

### What's being built to raise compliance on the structural rules

The critical-path work right now is **external hook-based enforcement** — a layer that runs in the Claude Code harness (or equivalent) and mechanically validates the AI's output before showing it to the user. Roughly:

1. **PreToolUse hooks** that log or block specific tool-call patterns (for example: "if the AI is about to Read a `.pdf` file, ensure it was extracted first" — this is the CHAMP principle turned into a mechanical gate)
2. **Stop hooks** that check the AI's finished response for structural markers (Confidence: line present? Three lens blocks visible? Violations section populated?) and block responses that miss them
3. **SessionStart hooks** that auto-load session state files into the AI's context so it doesn't depend on the AI remembering to read them

The goal is to move the enforceable subset of rules from "asking the AI nicely" to "mechanical harness gate." Based on analysis of actual logged violations, roughly **71% of high-frequency violations on the enforceable subset become preventable** once this ships. The remaining 29% are judgment rules that stay in human-in-the-loop territory permanently.

**Current status:** design complete, proof-of-concept mandated as the first action of the next development session. Not yet shipped.

See [`STATUS.md`](STATUS.md) for the rigorous coverage data, the exact list of rules the hook layer will cover, and the honest before/after projections.

---

## The PDF Principle (and the CHAMP reference tool)

**The principle, not a command:** reading a PDF as an image costs an LLM roughly 20 times more tokens than reading its extracted text. Before processing a PDF, extract it to text first. This applies regardless of which AI you're using, whether you have a shell, or which extractor you pick.

**Who extracts the PDF depends on your environment:**
- **In a browser chat (Claude.ai, ChatGPT, Gemini):** extract the PDF yourself before you paste. Use any tool — [`pdftotext`](https://en.wikipedia.org/wiki/Pdftotext) (from `poppler-utils`), [pandoc](https://pandoc.org/), a cloud OCR service, or this repo's `./tools/champ.py`. Paste the extracted text, not the PDF.
- **In Claude Code / Cursor / CLI tools:** the AI can invoke an extractor for you. It will use whatever is on the PATH. This repo ships `./tools/champ.py` as a reference implementation, but `pdftotext document.pdf -` works just as well.
- **In the API with vision enabled:** you can skip this principle, but you'll pay the ~20× token cost. For large PDFs or repeated reads, extraction first is always cheaper.

### The reference implementation (`./tools/champ.py`)

```bash
# The simplest invocation — auto-detects PDF type, just works
python ./tools/champ.py document.pdf

# Force text extraction (fast, for text-based PDFs)
python ./tools/champ.py document.pdf --mode text

# Force OCR (slower, for scanned PDFs)
python ./tools/champ.py document.pdf --mode ocr

# Extract pages as JPEG images (for complex layouts)
python ./tools/champ.py document.pdf --mode images
```

**Requirements:** Python 3.6+ (stdlib only — no `pip install` needed). CHAMP shells out to system tools depending on mode:
- **text / auto:** `pdftotext` and `pdfinfo` (from `poppler-utils`)
- **ocr:** `tesseract` (from `tesseract-ocr`) + `poppler-utils`
- **images:** `pdfimages` (from `poppler-utils`)

Install on Linux/macOS: `sudo apt install poppler-utils tesseract-ocr` (or `brew install poppler tesseract` on macOS).

On Windows: use WSL, or install [poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases) and [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki) and add them to your PATH. Or skip CHAMP entirely and use any PDF-to-text tool you prefer — the framework enforces the principle, not any particular tool.

**You do not have to use CHAMP.** It exists because having a concrete reference implementation makes the principle easier to adopt. Any PDF-to-text tool on your system satisfies the principle equally well.

---

## Platform Support

**STIX itself is plain text.** It works on any OS, any browser, any device that can paste text into a chat. There is nothing to install for the core framework.

| Platform | STIX (paste into chat) | CHAMP (PDF tool) | Shell scripts (`tools/*.sh`) |
|---|---|---|---|
| **Linux** | Works | Works natively | Works natively |
| **macOS** | Works | Works (`brew install poppler tesseract`) | Works natively |
| **Windows** | Works | Works via [WSL](https://learn.microsoft.com/en-us/windows/wsl/install), or install [poppler](https://github.com/oschwartz10612/poppler-windows/releases) + [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) natively | Use WSL or [Git Bash](https://gitforwindows.org/) |
| **Chromebook / mobile** | Works (browser path) | N/A — extract PDFs on another device first | N/A |

**The shell scripts (`build_master_protocol.sh`, `stix-update.sh`) are maintainer tools, not user-facing.** You never need to run them to use STIX. If you do want to run them on Windows, use WSL or Git Bash.

---

## Use Cases

STIX is useful anywhere a complex decision is being made under constraints. Documented users so far:

- **AI system prompts** — Embed in Claude.ai, ChatGPT, Gemini, custom API integrations
- **Autonomous agent control** — Multi-step agent workflows where bad decisions compound
- **Code review and architecture** — Force the AI to pass three lenses before recommending
- **DevOps gating** — Wrap deploy decisions in CIPHER + RISK gates
- **Project planning** — Use ARCHITECT phase before any non-trivial build
- **Personal decision-making** — Three-lens thinking works for non-software decisions too

---

## What a Real Session Looks Like

Here's an actual governed exchange, trimmed for brevity. This is what you should expect to see after loading STIX:

```
USER: I want to add a caching layer to our API. Redis or Memcached?

AI:
CS lens: Both are O(1) for get/set. Redis adds data structures (sorted sets,
streams, pub/sub) at the cost of single-threaded execution — throughput ceiling
is ~100K ops/sec per instance. Memcached is multi-threaded, higher raw throughput
for simple key-value, but no data structures beyond strings. Edge case: if cache
entries exceed available memory, Redis eviction policies are configurable;
Memcached uses LRU only.

Dev lens: Redis is the industry default for new projects — broader ecosystem,
better tooling, native TTL per key. Memcached wins only when the workload is
pure key-value at extreme throughput (>500K ops/sec). For an API cache, Redis
covers every realistic pattern. Rollback: swapping cache backends later is a
1-day refactor if you wrap access behind an interface now.

Engineer lens: Redis has one dependency (redis-server). Memcached has one
dependency (memcached). Operational cost is equivalent. Redis persistence
(RDB/AOF) is a bonus for cache warming after restarts — Memcached loses
everything on restart. No meaningful cost difference.

Confidence: HIGH — all three lenses converge on Redis. CS: superset
functionality at equivalent complexity. Dev: industry default, better tooling.
Engineer: equivalent cost, better durability. Per E13, HIGH = all three
agree, no unverified assumptions. Proceed.

Violations: none identified.
```

The key markers: three labeled lens blocks with real analysis (not labels), a confidence line that names which lenses agreed, and a violations line at the end.

---

## FAQ

**Q: Is this just prompt engineering with extra steps?**
A: Sort of. Prompt engineering is "what should the AI do." STIX is "what should the AI **refuse to do without checking first**." The difference is that STIX is built around hard gates (CIPHER, RISK, GOVERNING BOUNDARIES) rather than suggestions. Loaded properly, the AI will stop and ask before doing anything irreversible.

**Q: How is this different from a normal system prompt?**
A: System prompts usually tell the AI a persona ("you are a helpful assistant"). STIX is a behavioral framework — it doesn't tell the AI who to be, it tells it **how to think and when to stop**.

**Q: Does it actually work or is it placebo?**
A: It works to the extent that the underlying LLM is willing to follow long structured instructions. Stronger models (Claude Opus, GPT-4o, Gemini Ultra) follow it well. Weaker/cheaper models follow it inconsistently. The framework's value is **observable**: if you can see three-lens analysis and rule IDs in the AI's responses, it's working. If you can't, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

**Q: Do I need to read all 148 rules?**
A: No. CLAUDE.md activates them automatically. You only look up specific rules when the AI cites one and you want to know what it means.

**Q: Can I use only part of STIX?**
A: Yes. The protocols are modular. If you only want decision discipline, load VERDICT + APEX + ARCHITECT. If you only want gates for irreversibles, load VERDICT + CIPHER + RISK + GOVERNING BOUNDARIES. Just remove the relevant sections from your CLAUDE.md before pasting.

**Q: What's the cost?**
A: Free under AGPL-3.0. If you ship it inside a closed-source commercial product, you either keep your product AGPL-compliant or contact the maintainer for a commercial license.

**Q: Can I modify STIX?**
A: Yes. Fork it, change it, push back via PR. Modifications must follow Appendix B (Protocol Evolution): every change states which core value it better serves, and retired rules are archived rather than deleted.

**Q: What if STIX gives advice I disagree with?**
A: STIX doesn't decide for you. It surfaces analysis. You decide. If the framework consistently surfaces things you disagree with, that's a signal to either adjust your work or adjust the framework — both are valid.

---

## Common Issues (Quick Pointer)

If anything isn't working, **read [TROUBLESHOOTING.md](TROUBLESHOOTING.md)** first. It covers:

- 🚪 **Loading STIX** — file too big to paste, AI ignoring CLAUDE.md, attachments not being read
- 🔍 **Verifying STIX** — the 60-second test, hallucinated rule IDs, missing lens analysis
- 🛠️ **Daily use** — STIX feels heavy, AI adds unrequested content, AI declares "done" early, scope creep
- 🏗️ **Setup confusion** — which file is which, why are there 4 master protocols in CORE_PROTOCOL, the missing PDF, V1.1 vs V2.0 differences
- 🧪 **Honest limitations** — what STIX cannot do

---

## License

**STIX V2.0 is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).** The full license text is in [LICENSE](LICENSE).

**What AGPL-3.0 means in practice:**

- ✅ **Free for everyone** — personal, internal, commercial, educational, research. AGPL-3.0 does NOT restrict commercial use.
- 📋 **Copyleft obligation** — if you modify STIX and distribute your modified version (including running it as a network service accessible to third parties), you must make your modified source code available under the same AGPL-3.0 license.
- 🔗 **Network-service clause (Section 13)** — the "Affero" part. If you host a service that uses STIX and exposes it to users over a network, you must offer those users the complete source code of your STIX-using service.

### Commercial / Alternative Licensing

If AGPL-3.0 copyleft obligations don't fit your commercial product (e.g., you want to embed STIX inside a closed-source SaaS without open-sourcing your product), **alternative commercial licensing is available.** Open a GitHub issue tagged `commercial-license` or reach out via the repository's issue tracker to discuss terms.

---

## Contributing & Support

- **Found a bug or unclear rule?** Open an issue on GitHub.
- **Want to add a common issue to TROUBLESHOOTING.md?** PRs welcome.
- **Built something interesting with STIX?** Open an issue with a link — we'll add it to the use-case list.
- **Need a commercial license?** Open an issue tagged `commercial-license`.

---

**Built for judgment, precision, alignment, and integrity.**

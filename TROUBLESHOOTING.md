# STIX — Troubleshooting & Common Issues

If something isn't working, check here first. Issues are grouped by **what gate you're stuck at**: getting STIX loaded, verifying it works, or using it day-to-day.

---

## 🚪 Gate 1 — Loading STIX into your AI

### ❌ "The file is too big to paste" / "Context length exceeded"

**Cause:** `STIX_V2.0_MASTER_PROTOCOL.md` is ~3,400 lines / ~80,000 tokens. Most chat UIs (ChatGPT free tier, Claude free tier, mobile apps) reject pastes that large.

**Fix — pick one:**

1. **Recommended — paste CLAUDE.md only.** CLAUDE.md is ~350 lines and is the operating manual. It references rules by ID. Ask the AI: *"Tell me when you need a specific rule definition and I will paste it from STIX_V2.0_MASTER_PROTOCOL.md."* This works in any chat UI.
2. **Upload as a file attachment.** On Claude.ai or ChatGPT Plus, attach `STIX_V2.0_MASTER_PROTOCOL.md` as a file rather than pasting its contents. File attachments don't count against the message paste limit.
3. **Use just the protocol summaries.** For most work, the per-protocol `*_SUMMARY.md` files (one per folder) are enough. Paste `CLAUDE.md` + the 1–3 summary files relevant to your work (e.g. `APEX/EXECUTION/EXECUTION_SUMMARY.md` for code work).
4. **Use CHAMP if you're loading from PDFs elsewhere.** `python tools/champ.py file.pdf --mode text` extracts text at ~5% of vision-token cost.

---

### ❌ "I pasted CLAUDE.md but the AI is ignoring it"

**Cause:** Most LLMs treat the first user message as a request, not as a system prompt. They may "acknowledge" CLAUDE.md but not actually internalize it as governing rules.

**Fix:**

1. After pasting CLAUDE.md, send a separate explicit activation message:
   > *"You have just been loaded with the STIX V2.0 governance framework. Confirm you understand the three-lens thinking (CS / Developer / Engineer), the mandatory gates (ARCHITECT before APEX, CHAMP for PDFs, E13 confidence declaration), and the binding sequence. From now on, every non-trivial response must show three-lens analysis and cite at least one STIX rule by ID."*
2. If the AI doesn't visibly change behavior, paste CLAUDE.md again at the start of your next message and re-prompt. Some LLMs need 2 round-trips to lock in long system prompts.
3. If you're using the API, put CLAUDE.md in the **`system` parameter**, not in a `messages` entry. System prompts have stronger persistence than user messages.

---

### ❌ "I uploaded CLAUDE.md as a file and the AI didn't read it"

**Cause:** Some UIs only "see" attached files when you explicitly reference them.

**Fix:** Send a message like *"Read the attached `CLAUDE.md` in full and confirm you've internalized STIX V2.0."* Don't assume the AI auto-reads attachments — many don't.

---

## 🔍 Gate 2 — Verifying STIX is Active

### ❌ "I can't tell if STIX is actually working"

**The 60-second test.** After loading STIX, paste this exact prompt:

> *"Apply STIX three-lens thinking to this decision: should I use REST or GraphQL for a new internal API with 5 known consumers and unclear future query patterns? Show CS lens, Developer lens, Engineer lens, confidence level (HIGH/MEDIUM/LOW), and cite at least 2 STIX rule IDs."*

**A correctly-loaded STIX session will respond with something like:**

```
CS lens: REST is O(1) per endpoint with predictable response shapes;
GraphQL adds resolver overhead but supports flexible queries.
Termination guaranteed for both. Edge case: GraphQL N+1 query problem
needs DataLoader pattern.

Developer lens: REST has been done thousands of times — well-trodden
patterns, easy onboarding for new consumers. GraphQL has more gotchas
in caching and error handling. With "unclear future query patterns,"
GraphQL's flexibility is a real benefit.

Engineer lens: 5 consumers is small enough that REST won't bottleneck
on endpoint count, but unclear future patterns means refactoring REST
into GraphQL later costs more than starting with GraphQL now.
Token/time budget for the build is roughly equivalent.

Confidence: MEDIUM. CS and Engineer lenses agree on GraphQL; Developer
lens flags maturity risk (E13 — declare confidence; E15 — failure mode
first). Recommended: GraphQL with strict query depth limits and
DataLoader from day one.
```

**If you got a generic answer with no lens analysis and no rule IDs**, STIX did not load. Re-do Gate 1.

---

### ❌ "The AI cites rules but the IDs don't match anything"

**Cause:** The AI is hallucinating rule IDs because it has CLAUDE.md (which references rules) but not the actual rule definitions.

**Fix:** Upload `STIX_V2.0_MASTER_PROTOCOL.md` as well — that's the file that defines what each rule actually says. CLAUDE.md alone is the operating manual, not the rulebook.

---

## 🛠️ Gate 3 — Using STIX day-to-day

### ❌ "STIX feels heavy / slows me down"

**Cause:** STIX adds discipline upfront (ARCHITECT phase, three-lens thinking, confidence declaration). For trivial tasks this feels like overhead. **It's not designed for trivial tasks.**

**Fix:**

- For TINY tasks (one decision, one file, <30 min): tell the AI *"This is a TINY task — apply shallow STIX (skip ARCHITECT, single-line three-lens, just confirm and execute)."* CLAUDE.md actually has a project-size classifier (TINY / SMALL / MEDIUM / LARGE) that tunes thinking depth. Use it.
- For SMALL tasks: full three-lens thinking, no formal ARCHITECT decomposition.
- For MEDIUM/LARGE tasks: full ARCHITECT phase, full three-lens, formal decomposition document.

The framework cost should be proportional to the task size. If STIX feels heavy on a tiny task, you're skipping the size classifier.

---

### ❌ "The AI keeps adding things I didn't ask for"

**Cause:** Boundary B4 (No Unilateral Content Addition) exists for exactly this — but the AI has to know it's loaded.

**Fix:** Paste this enforcement reminder: *"Apply boundary B4 strictly. Add nothing I did not explicitly ask for. If you think something should be added, propose it as a one-sentence question and wait for my approval. Do not add and report."*

---

### ❌ "The AI declares 'done' before I've checked the work"

**Cause:** Boundary B6 (No Output Declared Final Without Creator Confirmation) exists for this.

**Fix:** *"Apply B6. You produce outputs; I declare them final. Don't say 'done', 'complete', or 'ready' on your own authority — present and wait."*

---

### ❌ "The AI starts doing extra work outside the scope I gave it"

**Cause:** Boundary B7 (No Scope Expansion Without Explicit Re-Invocation) and rule E14 (No Scope Expansion Mid-Execution).

**Fix:** *"Apply B7 and E14. The current scope is [restate scope]. If you notice anything outside this scope, note it and defer — do not execute it."*

---

### ❌ "How do I know which rule applies to my situation?"

**Use the protocol-to-purpose map:**

| Your situation | Look at |
|---|---|
| Designing something new | **VERDICT** (V1–V7) + **ARCHITECT** (A1–A20) |
| Writing/executing code | **APEX Execution** (E1–E25) |
| Talking to the AI | **APEX Communication** (C1–C15) + **APEX Exactness** (X1–X13) |
| Managing project state, files, databases | **FORGE** (F1–F13) |
| About to send/publish/commit something irreversible | **CIPHER** (G1–G11) — irreversible gates |
| About to send something to an external system | **RELAY** (RL1–RL8) — outward action gate |
| Checking whether you're staying on track | **OBSERVE** (OB1–OB8) — compliance instrumentation |
| About to do something risky or hard to undo | **RISK** (RK1–RK8) — safety halt gates |
| Worried about token/time/cost | **ECON** (EC1–EC6) — efficiency gates |
| Things you should never do, period | **GOVERNING BOUNDARIES** (B1–B7) |

---

## 🏗️ Repository / Setup Issues

### ❌ "Which file do I actually need?"

**Minimum to use STIX:** `CLAUDE.md` + `STIX_V2.0_MASTER_PROTOCOL.md`. Everything else is optional.

| File | Required? | Purpose |
|---|---|---|
| `CLAUDE.md` | ✅ Yes | Operating manual — system prompt, references rules by ID |
| `STIX_V2.0_MASTER_PROTOCOL.md` | ✅ Yes | Complete rule definitions (~3,400 lines) |
| `CURRENT_VERSION.md` | No | Version pointer for syncing |
| `STIX_INDEX.md` | No | Index of all the per-protocol folders |
| `*/SUMMARY.md` files | No | Per-protocol quick references |
| `CORE_PROTOCOL/` | No | Historical V1 → V2 versioned snapshots |
| `v2.0/` | No | V2.0 design/migration documents |
| `templates/` | No | Project file templates (about.md, audit_log.md) |
| `tools/champ.py` | No | PDF-to-text extractor (only useful if YOU process PDFs) |

---

### ❌ "There are 4 versions of the master protocol in CORE_PROTOCOL/. Which is current?"

**None of them are current.** The V1 → V4 files in `CORE_PROTOCOL/` are historical V1.0 → V1.1 snapshots (~73 rules each). The current law is `STIX_V2.0_MASTER_PROTOCOL.md` at the repo root (148 rules). The CORE_PROTOCOL files are kept for provenance under F11 — you don't need to read them.

---

### ❌ "What's the difference between `ARCHITECT_SUMMARY.md`, `ARCHITECT_PROTOCOL.md`, and `ARCHITECT_PROTOCOL_INTEGRATED.md`?"

Three different depths of the same content:

- `ARCHITECT_SUMMARY.md` (~36 lines) — quick reference table. Start here.
- `ARCHITECT_PROTOCOL.md` (~410 lines) — canonical rule definitions + worked example.
- `ARCHITECT_PROTOCOL_INTEGRATED.md` (~1,000 lines) — same rules with CS / Developer / Engineer perspectives annotated per rule + a step-by-step decomposition template.

(Same convention may apply to other protocols where multiple files exist.)

---

### ❌ "The README mentions a `.pdf` of the master protocol — where is it?"

It doesn't ship in this repo. Older versions of the README referenced a `.pdf` that was never included. Use `STIX_V2.0_MASTER_PROTOCOL.md` (the markdown file) — it has the same content. If you need a PDF for your workflow, you can generate one yourself with `pandoc STIX_V2.0_MASTER_PROTOCOL.md -o STIX_V2.0_MASTER_PROTOCOL.pdf`.

---

### ❌ "What's the difference between V1.1 and V2.0?"

| Aspect | V1.1 | V2.0 |
|---|---|---|
| Rule count | 101 | 148 (141 distributed + 7 gated host-only) |
| Articles | 6 (VERDICT, APEX, FORGE, CIPHER, ARCHITECT, GOVERNING BOUNDARIES) | 12 (V1.1 articles + RELAY, OBSERVE, RISK, ECON) |
| New protocols in V2.0 | — | RELAY (8), OBSERVE (8), RISK (8), ECON (6) |
| New governing values | JUDGMENT, PRECISION, ALIGNMENT, INTEGRITY | + TRANSPARENCY (OBSERVE), SAFETY (RISK), EFFICIENCY (ECON) |
| Self-policing? | No (user-policed) | Yes (OBSERVE makes it auditable in real-time) |

---

## 🧪 Things STIX Cannot Do (Honest Limitations)

- **STIX cannot force any LLM to obey it.** It is a prompt-based discipline. A model that decides to ignore the rules will ignore them. The framework's value is in catching the model's mistakes through explicit reasoning, not in technically preventing them.
- **STIX cannot replace domain knowledge.** It structures HOW you think; you still need to know WHAT you're thinking about.
- **STIX cannot make a small task fast.** The framework adds upfront discipline. For trivial work, that discipline is overhead. Use the size classifier (TINY/SMALL/MEDIUM/LARGE) to scale framework cost to task size.
- **STIX is not certified, audited, or formally verified.** It is a working framework derived from real session failures, but it has not been independently validated. Treat the "40–60% fewer wasted tokens" claim as one practitioner's anecdotal estimate, not a published benchmark.
- **STIX cannot tell you when to stop using STIX.** Judgment about whether the framework is helping is yours.

---

## 💻 Windows-Specific Issues

### "Can I use STIX on Windows?"

**Yes.** STIX is plain text files you paste into a chat. It works on any OS, any browser. There is nothing to install for the core framework.

### "CHAMP / shell scripts don't work on Windows"

The `tools/` directory contains Linux/macOS shell scripts. On Windows you have three options:

1. **Use WSL** (recommended) — install [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install), then `sudo apt install poppler-utils tesseract-ocr python3` and run CHAMP normally.
2. **Install native Windows builds** — [poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases) and [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki), add them to your PATH, then run `python tools/champ.py file.pdf`.
3. **Skip CHAMP entirely** — use any PDF-to-text tool you already have. The framework enforces the principle (extract before reading), not any particular tool.

### "stix-update.sh won't run"

`stix-update.sh` and `build_master_protocol.sh` are maintainer tools, not user-facing. You never need to run them. If you want to check for updates on Windows, just visit the [releases page](https://github.com/0Gizmick0/stix-v1/releases) or run `git pull` if you cloned the repo.

---

## 🆘 Still Stuck?

1. Re-read `CLAUDE.md` from the top — most "STIX isn't working" issues are bootstrap failures, not framework failures.
2. Check `CURRENT_VERSION.md` to confirm you're on V2.0 (148 rules).
3. Open an issue on the GitHub repository with: what you tried, what you expected, what actually happened, and which LLM you used.

---

*If you encounter a common issue not listed here, please open a PR adding it. Patterns that bite multiple users belong in this file.*

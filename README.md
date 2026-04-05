# STIX — AI Governance Framework

**STIX** = **S**trategic **T**hinking and **I**ntegrity **X**

A formal governance framework that defines **109 rules** for AI agents to ensure sound decisions, consistent execution, and integrity. Used in Claude Code, Claude.ai, ChatGPT, and custom AI systems.

**Status:** V1.1 complete (101 rules) + V2.0 OBSERVE deployed (8 rules) + V2.1 roadmap (RISK/ECON planned)

---

## 🚀 Quick Start (3 Minutes)

**No setup. No install. Just paste and go.**

```
1. Download → CLAUDE.md (13KB, plain text)
2. Paste → Into Claude.ai, ChatGPT, or your AI chat
3. Upload → One PDF from CORE_PROTOCOL/ folder
4. Ask → "Analyze using three-lens framework"
5. Done → 109 rules are now active
```

**That's it. Framework is live.**

---

## What STIX Does

**Prevents failure BEFORE it happens.**

Without STIX | With STIX
---|---
❌ "This should work" | ✅ "All 3 lenses agree → execute"
❌ Failures discovered too late | ✅ Issues caught before action
❌ Each decision is different | ✅ Consistent rules everywhere
❌ Edge cases missed | ✅ Edge cases planned upfront
❌ Over budget, over time | ✅ Projects finish on time/budget

**Real impact:** 40-60% fewer wasted tokens on dead-end work.

---

## The Framework (Simplified)

STIX = **109 rules** organized into **3 types**:

### Core Rules (V1.1 — 101 rules, all active)
| Protocol | Rules | What It Does |
|----------|-------|--------------|
| **VERDICT** | 7 | Foundational values & goals |
| **APEX** | 53 | How to execute & communicate |
| **FORGE** | 13 | State management & records |
| **ARCHITECT** | 20 | Planning & decomposition |
| **CIPHER** | 11 | Irreversible action gates |

### New Rules (V2.0 — 8 rules, now active)
| Protocol | Rules | What It Does |
|----------|-------|--------------|
| **OBSERVE** | 8 | Real-time compliance tracking |

### Future Rules (V2.1 — Planned, not yet deployed)
| Protocol | Rules | What It Does |
|----------|-------|--------------|
| **RISK** | — | Hard stops & safety limits |
| **ECON** | — | Cost-value measurement |

---

## How It Works

**The "Three-Lens" System** (The Secret Sauce)

Before ANY decision, STIX asks:

```
🧠 COMPUTER SCIENTIST LENS:  "Is this algorithmically sound?"
🔧 DEVELOPER LENS:           "Have we done this before? What failed?"
📊 ENGINEER LENS:             "Do we have resources? What's the bottleneck?"
```

All three must agree → **HIGH confidence → execute**

Only one/two agree → **MEDIUM confidence → proceed cautiously**

None agree → **LOW confidence → STOP**

---

## Real Example: PDF Batch Processing

**Bad thinking (without STIX):** "I'll build it and see if it works"

**STIX thinking (with 3 lenses):**
- **CS:** O(n) complexity, termination guaranteed, edge case = corrupted files
- **Dev:** We built this before (CHAMP tool), learned: encrypted PDFs fail
- **Engineer:** 100 PDFs × 150 tokens = 15K budget. We have 20K. Fits.
- **Result:** All three agree → BUILD IT → works

---

---

## How to Use STIX — Pick Your Platform

### 🖥️ **Claude Code (Local Development)**

Clone the repo and use it locally with Claude Code:

```bash
git clone https://github.com/0Gizmick0/stix-v1.git
cd stix-v1
```

Then load `CLAUDE.md` into your Claude Code session. The framework will reference all local files (APEX/, FORGE/, etc.) and work seamlessly.

---

### 💬 **Claude.ai, ChatGPT, or Any Browser Chat**

1. Open Claude.ai or ChatGPT
2. **Paste this file:** `CLAUDE.md` (copy-paste into the chat)
3. **Upload these PDFs:** 
   - `CORE_PROTOCOL/APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_2026-03-26_2046.pdf`
   - Any other CORE_PROTOCOL PDFs you want

The AI will read CLAUDE.md, reference the PDFs you uploaded, and enforce all 101 rules.

**Why it works:** The PDFs contain the source of truth. CLAUDE.md references them. The AI can read both.

---

### 📱 **Mobile (Claude App, ChatGPT App)**

Same as browser:
1. Open your mobile AI app
2. Paste `CLAUDE.md`
3. Upload the PDFs

The app handles files just like the web version.

---

### ⚙️ **Integrate into Your Own Project**

If you're building your own AI system:

```bash
# Copy CLAUDE.md into your project
cp CLAUDE.md /your/project/

# Or load it in code:
with open("CLAUDE.md", "r") as f:
    stix_framework = f.read()
    
# Use as your system prompt
system_prompt = f"{stix_framework}\n\n[Your additional instructions]"
```

---

## How It All Works Together

- **`CLAUDE.md`** = The operating manual (copy-paste anywhere, works standalone)
- **Rule summaries** (APEX/, ARCHITECT/, etc.) = Reference docs (look up specific rules)
- **PDFs** (CORE_PROTOCOL/) = Authoritative source (when you need the full story)
- **`CHAMP.py`** = Utility tool (extract PDFs to save tokens)

**You only need CLAUDE.md to get started.** Everything else is reference material that makes the framework easier to understand and extend.

## V2.0 — The Roadmap

Interested in where STIX is headed?

- `v2.0/` — Complete roadmap for STIX v2.0 with migration path from v1.1

## Use Cases

STIX is applicable to:

1. **AI System Governance** — Embed in system prompts for Claude, GPT, or other LLMs
2. **Autonomous Agent Control** — Enforce rules in multi-step agent workflows
3. **DevOps Pipelines** — Gate critical deployment decisions
4. **Organizational Process** — Standardize decision-making across teams
5. **Project Management** — Structure project phases with built-in checkpoints

## How CLAUDE.md Works — The Three-Lens Framework

CLAUDE.md isn't just a prompt. It activates **three simultaneous analytical thinking patterns**. This is the core of STIX.

### The Three Lenses (All at Once)

**1. CS Lens — Computer Science**
- Asks: Is this algorithmically sound?
- Checks: Complexity, edge cases, termination, proof
- Example: "Before we cache user data, what's the eviction strategy? What if cache fills? Handled."

**2. Developer Lens — Real-World Patterns**
- Asks: Have we solved this before? What failed last time?
- Checks: Integration friction, testability, past failures
- Example: "We tried async auth 3 times before and it broke in production. This time we test against real DB."

**3. Engineer Lens — System Constraints**
- Asks: Do we have the resources? What's the bottleneck?
- Checks: Token budget, time, memory, dependencies
- Example: "This costs 5000 tokens. We budgeted 3000. Can we simplify?"

### Why All Three Must Agree

**If only CS agrees:** Algorithm is sound but breaks in real systems (untested)
**If only Dev agrees:** We've done similar things but might be overcomplicating (solving old problems)
**If only Engineer agrees:** We have resources but the approach might be flawed (solving the wrong problem)

**When all three agree:** You have HIGH confidence. Proceed. All risks identified.

### Example: Preventing a Failure

**The scenario:** You're about to build a multi-day batch processing system for PDFs.

**Bad thinking (skips lenses):** "This should work. We'll build it and see."

**Three-lens thinking (automatic):**
- **CS:** Batch processing is O(n) where n = file count. Termination is guaranteed (finite files). Edge case: what if a file is corrupted? Recovery: skip with warning, log, continue. ✓
- **Dev:** We built a similar batch tool (CHAMP) last month. It failed on encrypted PDFs. This time: skip encrypted, log clearly. ✓
- **Engineer:** 100 PDFs × 150 tokens each = 15K tokens budgeted. We have 20K budget. Bottleneck: extraction time. Recovery: timeout handler. ✓

**Result:** All three lenses agree → HIGH confidence → execute → it works.

### Key Concepts

### Three Analytical Lenses (Automatic)

STIX requires simultaneous thinking across three perspectives:

1. **CS Lens** — Correctness, complexity analysis, formal algorithms
2. **Developer Lens** — Real patterns, integration friction, testability
3. **Engineer Lens** — Resource constraints, bottlenecks, system fit

All three must agree before proceeding.

### Mandatory Gates

Work cannot begin until:

✓ **CHAMP enforcement** — PDFs extracted before reading (saves 95% tokens)
✓ **E13 confidence** — Justify all 3 lenses agree (HIGH/MEDIUM/LOW)
✓ **ARCHITECT phase** — Formal decomposition before execution
✓ **Session constraint** — Token budget locked before work
✓ **Irreversible gates** — CIPHER gates confirm before any irreversible output

### Operational Instincts

Six core instincts guide all work:

1. **Clarify before building** — Never assume. Ask the one question that closes the gap.
2. **Confirm before advancing** — Each layer stable before next begins.
3. **Flag problems early** — Say it now, not after it costs something.
4. **Stay in scope** — Current goal finishes before anything new begins.
5. **Document as you go** — Decisions written during work, not reconstructed after.
6. **Integrity before irreversible output** — Mirror back, confirm explicitly, declare confidence.

## Tools

### CHAMP — PDF Extraction

STIX includes **CHAMP**, a Python utility for token-efficient PDF processing:

```bash
python tools/champ.py file.pdf --mode auto      # Auto-detect & extract
python tools/champ.py file.pdf --mode text      # Fast text extraction
python tools/champ.py file.pdf --mode ocr       # OCR for scanned PDFs
python tools/champ.py file.pdf --mode images    # Extract as JPEGs
```

**Token savings:** ~150 tokens (extracted text) vs ~3000 tokens (vision reading) = **95% reduction**.

## Repository Structure

**Complete file tree of what you're downloading:**

```
stix-v1/
│
├── 📄 README.md                              ← This file (start here)
├── 📄 CLAUDE.md                              ← System prompt (copy-paste into Claude.ai)
├── 📄 LICENSE                                ← AGPL-3.0 with commercial flexibility
├── 📄 .gitignore                             ← Standard Python/IDE ignores
├── 📄 STIX_INDEX.md                          ← Master index of all protocols
├── 📄 NAMING_CONVENTIONS.md                  ← Framework naming standards
│
├── 📁 CORE_PROTOCOL/                         ← SOURCE OF TRUTH (all rule definitions)
│   ├── APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_2026-03-26_2046.pdf  (Current law)
│   ├── APEX_FORGE_CIPHER_MASTER_PROTOCOL_v3_2026-03-26_1932b.pdf (Prior version)
│   ├── APEX_FORGE_CIPHER_MASTER_PROTOCOL_v2_2026-03-26_1932.pdf  (Historical)
│   ├── APEX_FORGE_CIPHER_MASTER_PROTOCOL_v1_2026-03-26_1831.pdf  (Original)
│   ├── APPENDIX_C_ERROR_CLASSIFICATION.md   (6 error types)
│   ├── APPENDIX_D_OPERATING_CADENCE.md      (6 operational points)
│   ├── Document_1_STIX_Authority_Ladder.pdf (5-level authority system)
│   ├── Document_1_STIX_Authority_Ladder.md  (Markdown version)
│   └── E20_RETIREMENT_RECORD.md             (Formal rule retirement)
│
├── 📁 VERDICT/                               (7 rules — Foundational Values)
│   └── VERDICT_SUMMARY.md
│
├── 📁 APEX/                                  (53 rules — Execution Discipline)
│   ├── EXECUTION/
│   │   ├── EXECUTION_SUMMARY.md
│   │   ├── E13_CONFIDENCE_CRITERIA.md
│   │   ├── E21_HUMAN_IN_LOOP_GATE.md
│   │   ├── E22_MODULE_CAPABILITY_CONFLICT.md
│   │   ├── E23_INPUT_SOURCE_VERIFICATION.md
│   │   └── E25_CONTEXT_COMPRESSION.md
│   ├── COMMUNICATION/
│   │   ├── COMMUNICATION_SUMMARY.md
│   │   ├── C14_LANGUAGE_PRECISION.md
│   │   └── C15_INTERRUPT_RECOVERY.md
│   └── EXACTNESS/
│       ├── EXACTNESS_SUMMARY.md
│       └── X13_POINTER_RESOLUTION.md
│
├── 📁 FORGE/                                 (13 rules — State Management)
│   ├── FORGE_SUMMARY.md
│   └── F13_ACTIVE_COMPLIANCE_VERIFICATION.md
│
├── 📁 ARCHITECT/                             (20 rules — Strategic Decomposition)
│   ├── ARCHITECT_SUMMARY.md
│   ├── ARCHITECT_PROTOCOL.md
│   └── ARCHITECT_PROTOCOL_INTEGRATED.md
│
├── 📁 CIPHER/                                (11 rules — Irreversible Gates)
│   ├── CIPHER_SUMMARY.md
│   ├── G8_CIPHER_UNIVERSAL_TRIGGER.md
│   ├── G9_FINANCIAL_DECISION_GATE.md
│   ├── G10_CODE_TO_PRODUCTION_GATE.md
│   └── G11_PUBLISHED_ARTIFACT_GATE.md
│
├── 📁 RELAY/                                 (8 rules — Communication Relay)
│   └── RELAY_SUMMARY.md
│
├── 📁 GOVERNING_BOUNDARIES/                  (7 boundaries — Enforcement)
│   ├── GOVERNING_BOUNDARIES_SUMMARY.md
│   ├── B4_NO_UNILATERAL_CONTENT.md
│   ├── B5_NO_SILENT_CONTINUITY.md
│   ├── B6_NO_FINAL_WITHOUT_CONFIRMATION.md
│   └── B7_NO_SCOPE_EXPANSION.md
│
├── 📁 OBSERVE/                               (8 rules — Transparency [V2.0 NEW])
│   ├── OBSERVE_SUMMARY.md
│   ├── OB1_EVERY_OUTPUT_AUDITABLE.md
│   ├── OB2_COMPLIANCE_CHECK_AT_OUTPUT.md
│   ├── OB3_DRIFT_DETECTION.md
│   ├── OB4_SESSION_ENTROPY_METER.md
│   ├── OB5_CONFIDENCE_JUSTIFICATION.md
│   ├── OB6_VIOLATION_LOGGING.md
│   ├── OB7_METRICS_COLLECTION.md
│   └── OB8_FRAMEWORK_DRIFT_TRACKING.md
│
├── 📁 RISK/                                  (Planned V2.1 — Safety & Hard Stops)
│   └── RISK_SUMMARY.md                       (Rules not yet written)
│
├── 📁 ECON/                                  (Planned V2.1 — Efficiency & Value)
│   └── ECON_SUMMARY.md                       (Rules not yet written)
│
├── 📁 v2.0/                                  (V2.0 Planning & Roadmap)
│   ├── V2_INDEX.md                           (Complete V2.0 index)
│   ├── STIX_V2_Complete_Framework.pdf        (Migration matrix)
│   ├── STIX_V2_Additions_GPT_Document.pdf    (Implementation spec)
│   ├── CONFLICT_RESOLUTIONS.md               (7 design conflicts resolved)
│   ├── Document_2_STIX_Document_Level_Conflict_Register.pdf
│   ├── Document_3_STIX_V1_to_V2_Migration_Matrix.pdf
│   ├── APEX_FORGE_IMPLEMENTATION_SPEC.pdf
│   └── STIX_V2_Roadmap.txt                   (Full build order)
│
├── 📁 templates/                             (Project Templates)
│   ├── about_template.md                     (Blank project about file)
│   └── audit_log_template.md                 (Blank audit log template)
│
└── 📁 tools/
    └── champ.py                              (PDF-to-text extractor, 95% token savings)

```

---

### What Each Folder Contains

| Folder | Rules | Purpose |
|--------|-------|---------|
| **CORE_PROTOCOL/** | — | Source of truth PDFs (all 4 versions archived) |
| **VERDICT/** | V1–V7 (7) | Foundational decision values |
| **APEX/** | E1–E25, C1–C15, X1–X13 (53) | Execution discipline + communication |
| **FORGE/** | F1–F13 (13) | State management & database integrity |
| **ARCHITECT/** | A1–A20 (20) | Strategic decomposition & planning |
| **CIPHER/** | G1–G11 (11) | Irreversible commitment gates |
| **RELAY/** | RL1–RL8 (8) | Communication relay (V2.0) |
| **GOVERNING_BOUNDARIES/** | B1–B7 (7) | Enforcement boundaries |
| **OBSERVE/** | OB1–OB8 (8) | Transparency & compliance (V2.0 NEW) |
| **RISK/** | — | Planned V2.1 (safety thresholds) |
| **ECON/** | — | Planned V2.1 (efficiency measurement) |
| **v2.0/** | — | Roadmap + planning documents |
| **templates/** | — | Starter files for new projects |
| **tools/** | — | CHAMP PDF extraction utility |

**Total: 109 rules (101 active + 8 OBSERVE deployed)**

## Built-In Tools

### CHAMP — Token-Efficient PDF Extraction

STIX includes **CHAMP** for reading PDFs without burning through tokens:

```bash
# Extract a PDF to plain text (95% token savings vs vision reading)
python tools/champ.py document.pdf --mode text

# Auto-detect PDF type and extract accordingly
python tools/champ.py document.pdf --mode auto

# Extract as images (best for complex layouts)
python tools/champ.py document.pdf --mode images
```

**Why this matters:** Reading a 50-page PDF with vision tokens costs ~3000 tokens. CHAMP extracts it as text for ~150 tokens. Same information, 20x cheaper.

## FAQ

**Q: Do I need to read all 101 rules?**
A: No. CLAUDE.md activates them automatically. You only look up specific rules when you want details.

**Q: What if STIX conflicts with my existing process?**
A: STIX is designed to complement, not replace. Use the parts that solve your problems. The mandatory gates are non-negotiable; everything else is configurable.

**Q: Can I use STIX for non-AI work?**
A: Yes. The three-lens framework (CS/Dev/Engineer) works for any decision-making: project management, DevOps, organizational process, team decisions.

**Q: Is STIX only for software engineers?**
A: No. Any team making complex decisions under constraints benefits. Replace "code" with "document" and the logic still works.

**Q: How much does STIX cost?**
A: Free to use (AGPL-3.0 license). Pay only if you build a commercial product on top of it.

**Q: Can I modify STIX?**
A: Yes. Contributions welcome. Fork it, improve it, push back to the community.

---

## Real-World Examples

### Example 1: Using STIX for an API Design Decision

**Without STIX:**
- "Should we use REST or GraphQL?"
- "REST is simpler."
- Build REST API.
- 3 months later: Client needs flexible queries. Too late.

**With STIX (three-lens thinking):**
- **CS:** GraphQL requires resolver overhead. REST is O(1) per endpoint. Complexity trade-off: GraphQL adds flexibility, REST adds simplicity. What's the algorithmic requirement?
- **Dev:** We've built REST APIs 5 times, GraphQL once. REST integrates better with our stack. GraphQL had resolver caching issues last time.
- **Engineer:** Timeline: 2 weeks (REST) vs 4 weeks (GraphQL). Budget: 8K tokens (REST) vs 12K tokens (GraphQL). Client needs flexible queries → GraphQL required despite complexity.
- **Decision:** GraphQL, but with caching layer (addresses past failure). All three lenses agree → execute.

### Example 2: Using STIX for a Deployment Decision

**Without STIX:**
- "Let's deploy to production."
- "Sure, looks good."
- Deploy. System crashes under load.

**With STIX (ARCHITECT phase):**
- **Concept:** Deploy new auth system to production.
- **Critical questions:** What if database connection fails? What if rate limiter breaks? What if users hit old endpoints?
- **Failure modes identified:** DB failure → fallback to read-only. Rate limiter breaks → graceful degradation. Old endpoints → 404 with helpful message.
- **All three lenses agree:** Edge cases handled. Recovery paths clear. Deploy.

---

## Getting Help

**Rule not clear?** Look it up:
- Search the PDF: `CORE_PROTOCOL/APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_*.pdf`
- Check the summary: `APEX/EXECUTION/EXECUTION_SUMMARY.md` (for E rules), etc.
- Read CLAUDE.md directly — it cites every rule

**Want to understand the roadmap?** See `v2.0/` for migration docs and future protocol additions.

**Have a question about STIX?** Open an issue on this repository.

---

## License

STIX v1.1 is licensed under **AGPL-3.0** — free to use with flexibility for commercial projects.

### What This Means

**Free to use:**
- Open-source projects (must remain open-source)
- Personal/internal use
- Educational use
- Contributions to the community

**Commercial/proprietary products:**
- Keep your product open-source (AGPL-3.0 compliant), OR
- Get a commercial license, OR
- Reach out — we can work something out

See [LICENSE](LICENSE) file for full terms.

---

**Built for judgment, precision, alignment, and integrity.**

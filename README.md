# STIX v1.1 — AI Governance Framework

**STIX** (Strategic Thinking and Integrity X) is a formal governance framework for AI agents and autonomous systems. It defines 101 rules across five core protocols to ensure judgment, precision, alignment, and integrity in decision-making.

## What is STIX?

STIX v1.1 is a **structured execution model** — not a suggestion or guideline, but a binding operational framework with:

- **VERDICT (7 rules):** Foundational values driving all decisions
- **APEX (53 rules):** Execution discipline, communication clarity, exactness
- **FORGE (13 rules):** State management and database integrity
- **ARCHITECT (20 rules):** Strategic decomposition and critical path planning
- **CIPHER (11 rules):** Irreversible commitment gates and security thresholds

**Total: 101 rules. All binding. All active.**

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

## Key Concepts

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

## Architecture

The framework is organized as:

```
stix-v1/
├── README.md                      ← This file (start here)
├── CLAUDE.md                      ← System prompt (paste into your AI)
│
├── CORE_PROTOCOL/                 ← Source-of-truth PDFs (4 versions + appendices)
│   ├── APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_*.pdf  ← Current law (101 rules)
│   ├── APPENDIX_C_ERROR_CLASSIFICATION.md
│   └── APPENDIX_D_OPERATING_CADENCE.md
│
├── APEX/                          ← Execution (E1–E25), Communication (C1–C15), Exactness (X1–X13)
├── ARCHITECT/                     ← Strategic decomposition (A1–A20)
├── CIPHER/                        ← Irreversible commitment gates (G1–G11)
├── FORGE/                         ← State management (F1–F13)
├── VERDICT/                       ← Foundational values (V1–V7)
├── RELAY/                         ← Proposed V2.0 relay protocols (RL1–RL8)
├── GOVERNING_BOUNDARIES/          ← Boundary enforcement (B1–B7)
│
├── v2.0/                          ← V2.0 roadmap and migration matrix
├── templates/                     ← Blank templates for your own projects
├── tools/
│   └── champ.py                   ← PDF-to-text extractor (saves 95% tokens)
└── NAMING_CONVENTIONS.md          ← Framework naming rules
```

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

## Getting Help

**Rule not clear?** Look it up:
- Search the PDF: `CORE_PROTOCOL/APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_*.pdf`
- Check the summary: `APEX/EXECUTION/EXECUTION_SUMMARY.md` (for E rules), etc.
- Read CLAUDE.md directly — it cites every rule

**Want to understand the roadmap?** See `v2.0/` for migration docs and future protocol additions.

---

## License

STIX v1.1 is provided as-is for commercial and private use.

---

**Built for judgment, precision, alignment, and integrity.**

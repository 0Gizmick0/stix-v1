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

## Quick Start

### 1. Load the Framework

```bash
# Copy CLAUDE.md into your project
cp CLAUDE.md /your/project/

# Or reference it directly in your AI system prompt
cat CLAUDE.md >> your_system_prompt.txt
```

### 2. Read the Core Protocol

Start here for the authoritative source:

```
CORE_PROTOCOL/APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_2026-03-26_2046.pdf
```

All 101 rules are formally defined in this document.

### 3. Understand the Five Protocols

Each protocol folder contains detailed rule summaries:

- `VERDICT/VERDICT_SUMMARY.md` — Foundational values (V1–V7)
- `APEX/EXECUTION/EXECUTION_SUMMARY.md` — Execution rules (E1–E25)
- `APEX/COMMUNICATION/COMMUNICATION_SUMMARY.md` — Communication rules (C1–C15)
- `APEX/EXACTNESS/EXACTNESS_SUMMARY.md` — Exactness rules (X1–X13)
- `FORGE/FORGE_SUMMARY.md` — State management (F1–F13)
- `ARCHITECT/ARCHITECT_SUMMARY.md` — Strategic planning (A1–A20)
- `CIPHER/CIPHER_SUMMARY.md` — Commitment gates (G1–G11)
- `RELAY/RELAY_SUMMARY.md` — Relay protocols (RL1–RL8, proposed V2.0)

### 4. Use CLAUDE.md as Your AI System Prompt

`CLAUDE.md` is designed to be loaded directly into your AI system. It:

- Activates three simultaneous analytical lenses (CS/Dev/Engineer)
- Enforces mandatory gates before any work begins
- Tracks session state and prevents violations
- Provides automatic thinking patterns, not consultative questionnaires

**Key sections in CLAUDE.md:**
- **SESSION START BOOTSTRAP** — 5-step gated initialization
- **THREE LENSES** — Automatic correctness/pattern/constraint thinking
- **SIX CORE INSTINCTS** — Operating discipline
- **CIPHER GATES** — Irreversible commitment safeguards

## Framework Analysis

For deeper understanding:

- `FRAMEWORK_ANALYSIS/` — Thesis documents, knowledge databases, master audits
- `OBSERVABILITY/` — Visual diagrams of framework coverage and conflict maps
- `v2.0/` — V2.0 migration docs and roadmap

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
stix-v1.1/
├── CLAUDE.md                      ← Main system prompt
├── CORE_PROTOCOL/                 ← Source-of-truth PDFs + appendices
├── APEX/                          ← Execution, Communication, Exactness rules
├── ARCHITECT/                     ← Strategic decomposition protocol
├── CIPHER/                        ← Irreversible commitment gates
├── FORGE/                         ← State management
├── VERDICT/                       ← Foundational values
├── RELAY/                         ← V2.0 relay protocols (proposed)
├── GOVERNING_BOUNDARIES/          ← Boundary enforcement rules
├── FRAMEWORK_ANALYSIS/            ← Thesis docs, audits, knowledge base
├── OBSERVABILITY/                 ← Diagrams, coverage maps, conflict analysis
├── v2.0/                          ← V2.0 migration path and roadmap
├── templates/                     ← Project templates for your own work
├── tools/                         ← Utilities (CHAMP PDF extractor)
└── README.md                      ← This file
```

## Integration Examples

### Example 1: Load in Claude API

```python
from anthropic import Anthropic

with open("CLAUDE.md", "r") as f:
    stix_framework = f.read()

system_prompt = f"""
{stix_framework}

You are an AI assistant using the STIX v1.1 governance framework.
Apply all 101 rules in all decisions.
"""

client = Anthropic()
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": "Your task here..."}]
)
```

### Example 2: Embed in System Prompt

Copy `CLAUDE.md` directly into your system prompt for any AI system. The framework auto-activates the three-lens thinking, mandatory gates, and core instincts.

### Example 3: Organizational Process

Use the six core instincts + ARCHITECT phase as a decision-making framework for teams:

1. **CLARIFY** — Mirror back the problem
2. **ARCHITECT** — Formal decomposition before execution
3. **THREE LENSES** — CS/Dev/Engineer agree before proceeding
4. **DOCUMENT** — Write decisions during planning, not after
5. **GATE** — Require explicit confirmation on irreversible decisions
6. **VERIFY** — Confirm work is complete before advancing

## License

STIX v1.1 is provided as-is for commercial and private use.

## References

- **Full Protocol:** `CORE_PROTOCOL/APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4_2026-03-26_2046.pdf`
- **Master Audit:** `FRAMEWORK_ANALYSIS/STIX_Complete_Master_Audit_v1_0.pdf`
- **Conflict Register:** `v2.0/Document_2_STIX_Document_Level_Conflict_Register.pdf`

---

**Built for judgment, precision, alignment, and integrity.**

For questions or issues, refer to the core protocol and framework analysis documents.

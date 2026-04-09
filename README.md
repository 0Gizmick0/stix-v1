# STIX — A Governance Framework for AI

<sub>**Version:** STIX V2.0 · **Rules:** 148 (141 distributed + 7 gated host-only) · **Last updated:** 2026-04-08 · **License:** AGPL-3.0</sub>

**STIX makes AI catch its own mistakes _before_ they cost you.** It's a set of 148 rules you load into Claude, ChatGPT, Gemini, or any other LLM as a system prompt. Once loaded, the AI is forced to:

- Think through every decision via **three analytical lenses simultaneously** (Computer Scientist / Software Developer / Engineer)
- **Declare confidence** (HIGH / MEDIUM / LOW) before acting
- **Stop at hard gates** before any irreversible action (sending email, deleting files, deploying code)
- **Document its reasoning** so you can audit it later
- **Track its own token budget** and warn before it runs out

It's free, MIT-compatible (AGPL-3.0), works in any chat UI or API, and takes about 60 seconds to install.

> **Status:** STIX V2.0 — 148 rules across 12 articles + 1 gated layer
> **What's the gated layer?** 7 of the 148 rules form a host-only offensive-security operating layer (PENTEST). They're disclosed for honest rule-count accounting but not distributed in this repository. The 141 rules in this repository constitute a complete general-purpose AI governance framework.

---

## ⚡ 60-Second Quick Start

**You need 2 files: `CLAUDE.md` and `STIX_V2.0_MASTER_PROTOCOL.md`.** That's it. Both are in this repo's root.

### Option A — Claude.ai or ChatGPT (browser)

1. Open `CLAUDE.md`, copy the entire contents, paste it as your first message in a new chat. Send.
2. Attach `STIX_V2.0_MASTER_PROTOCOL.md` as a file in your next message (or paste it if your UI accepts long pastes).
3. Send: *"Confirm you have STIX V2.0 (148 rules) loaded. Apply three-lens thinking to every decision from now on."*
4. Done. The AI is now governed by STIX.

> **⚠️ Big-paste warning:** `STIX_V2.0_MASTER_PROTOCOL.md` is ~80,000 tokens. Some chat UIs reject pastes that large. If yours does, see [TROUBLESHOOTING.md → Gate 1](TROUBLESHOOTING.md#-gate-1--loading-stix-into-your-ai) for 4 alternatives. The simplest workaround is to paste **CLAUDE.md only** and let the AI ask you for specific rule definitions when it needs them.

### Option B — API (Python)

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

### Option C — Claude Code

`git clone` this repo and open it. Claude Code auto-loads `CLAUDE.md` from the working directory. Done.

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

## The Three-Lens Framework (The Core Idea)

Every STIX-governed decision passes through three lenses **simultaneously**:

| Lens | Asks | Catches |
|---|---|---|
| 🧠 **CS Lens** (Computer Scientist) | "Is this algorithmically sound?" | Edge cases, complexity blowups, untestable claims |
| 🔧 **Developer Lens** (Software Developer) | "Have we done this before? What failed last time?" | Repeating past mistakes, integration friction |
| 📐 **Engineer Lens** (Computer Engineer) | "Do we have the resources? What's the bottleneck?" | Budget overruns, missing rollbacks, dependency surprises |

**All three must agree → HIGH confidence → execute.**
**Two of three → MEDIUM → proceed with rollback plan.**
**Fewer than two → LOW → STOP and escalate to human.**

This is the single most important idea in STIX. Everything else exists to enforce it.

---

## Repository Layout

```
stix-commercial/
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
    └── build_master_protocol.sh       ← Maintainer script
```

### File-naming convention

- **`<PROTOCOL>_SUMMARY.md`** in each folder is the **canonical, complete rule list** for that protocol.
- **Per-rule files** (e.g. `E13_CONFIDENCE_CRITERIA.md`, `OB1_EVERY_OUTPUT_AUDITABLE.md`) exist **only where a rule needs additional operational guidance**. They're companions to the SUMMARY, not replacements.
- A protocol with only a SUMMARY file is **complete**, not unfinished.

---

## How CLAUDE.md and the Master Protocol Differ

| File | What it is | When the AI uses it |
|---|---|---|
| `CLAUDE.md` | Operating manual — references rules by ID, defines bootstrap, gates, instincts | Loaded once at session start as the system prompt |
| `STIX_V2.0_MASTER_PROTOCOL.md` | The full rulebook — definition of every rule | Looked up when the AI needs to know what a specific rule actually says |

You need **both**. CLAUDE.md alone tells the AI what rules exist but not what they say. The master protocol alone tells it what the rules say but not how to use them.

---

## 🧰 Bonus: CHAMP — PDF Token Saver

This repo ships a small Python tool that solves a real problem: **reading PDFs in an LLM costs ~20× more tokens via vision than via text extraction.**

```bash
python tools/champ.py document.pdf --mode auto    # Auto-detect text vs scanned
python tools/champ.py document.pdf --mode text    # Force text extraction
python tools/champ.py document.pdf --mode ocr     # Force OCR (scanned PDFs)
python tools/champ.py document.pdf --mode images  # Extract pages as JPEG
```

**Why it's in here:** STIX has a hard rule (mandatory in CLAUDE.md) that PDFs must be extracted before the AI reads them. CHAMP is the reference implementation. You don't have to use it — any PDF-to-text tool works.

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

**STIX V2.0 is licensed under AGPL-3.0.**

- ✅ **Free** for open-source projects, personal use, education, internal use, and contributions
- 💼 **Commercial / proprietary use** — keep your product AGPL-compliant, OR contact the maintainer for a commercial license
- See [LICENSE](LICENSE) for full terms

---

## Contributing & Support

- **Found a bug or unclear rule?** Open an issue on GitHub.
- **Want to add a common issue to TROUBLESHOOTING.md?** PRs welcome.
- **Built something interesting with STIX?** Open an issue with a link — we'll add it to the use-case list.
- **Need a commercial license?** Open an issue tagged `commercial-license`.

---

**Built for judgment, precision, alignment, and integrity.**

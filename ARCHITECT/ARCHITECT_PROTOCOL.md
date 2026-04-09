---
article: VI
name: ARCHITECT — Strategic Problem Decomposition
governing_value: JUDGMENT
rule_range: A1–A20
rule_count: 20
source_protocol: User instruction 2026-03-29
created: 2026-03-29
status: ACTIVE
file_role: Canonical rule definitions + worked example. Read when applying ARCHITECT to a project. For a quick table see ARCHITECT_SUMMARY.md. For per-rule three-lens annotations see ARCHITECT_PROTOCOL_INTEGRATED.md.
---

# ARTICLE VI — ARCHITECT
## Strategic Problem Decomposition Before Execution
**Governing Value: JUDGMENT**

> ARCHITECT sits above APEX. Before anything is built, before execution begins, ARCHITECT decomposes the problem into components: concept → questions → phrases → ideas. This prevents dead ends, reduces token waste, and compresses session time.

---

## Purpose

Nine out of ten failed projects fail because the problem was not understood before work began. ARCHITECT answers: **What are we actually solving?** before we start solving it.

- Whisper daemon failed because we didn't ask: "Is pynput the right library?" upfront
- We wasted $5 iterating instead of decomposing first
- A 5-minute decomposition would have caught it: "Global hotkey + pynput = needs Listener.pressed, but that doesn't exist"

ARCHITECT prevents this by forcing decomposition **before** execution begins.

---

## Rules

### DECOMPOSITION LAYER 1: CONCEPT CLARIFICATION (A1–A3)

### A1 — CONCEPT ISOLATION
Every request contains a core concept. Extract it in one sentence.

**Pattern:**
- Input: "Build a hotkey daemon for voice-to-text that works everywhere"
- Core concept: "Global keyboard input capture with transcription pipeline"
- Questions this raises: How does global input work on Linux? What library? Cost?

**Fail mode:** Accepting fuzzy concepts. "Build a tool" is not a concept.

---

### A2 — SCOPE BOUNDARY
State what is IN scope and what is OUT, explicitly.

**Pattern:**
- IN: Hotkey detection, recording, transcription output to clipboard
- OUT: GUI, settings UI, multiple hotkeys, multiple models
- Constraint: Must work on Linux (test system is Linux)

**Fail mode:** Scope creep mid-work. Set this first.

---

### A3 — CONSTRAINT EXTRACTION
Name all constraints before work begins: time, budget, hardware, API, dependencies.

**Pattern for Whisper:**
- Time: "Must be done in one session"
- Budget: "$5 max spend"
- Hardware: "Linux only, no GPU"
- Dependencies: "pynput, pyaudio, whisper already installed? Or fresh venv?"
- API: "Whisper API or local model?"

**Fail mode:** Discovering constraints mid-build. Costs tokens and time.

---

### DECOMPOSITION LAYER 2: QUESTION FORMATION (A4–A6)

### A4 — CRITICAL PATH QUESTION
Ask the ONE question that kills the project if answered wrong.

**Pattern:**
- Whisper daemon: "Does pynput Listener actually expose a .pressed attribute for checking held keys?"
- If NO = dead end. Should've asked this in 30 seconds before writing 2,000 lines.
- If YES = proceed.

**Fail mode:** Discovering the blocker after implementation.

---

### A5 — DEPENDENCY QUESTIONS
For each dependency, ask: Does it exist? Does it do what we think? Are there alternatives?

**Pattern:**
- pynput: "Does it work on Linux X11/Wayland?" → Research before coding
- pyaudio: "Do we need to build from source or do wheels exist?" → Check pip
- whisper: "Can we run 'base' model on this hardware?" → Test locally first

**Fail mode:** Assuming dependencies work. They often don't.

---

### A6 — ARCHITECTURE QUESTIONS
Before design, ask: What are the layers? What calls what? Where do things break?

**Pattern:**
- Layer 1: Global hotkey capture (X11? pynput? evdev?)
- Layer 2: Audio recording (pyaudio)
- Layer 3: Transcription (whisper model)
- Layer 4: Clipboard output (pyperclip)
- Break points: If hotkey fails, does recording still work? If recording fails, does it block transcription?

**Fail mode:** Designing without knowing the dependency chain.

---

### DECOMPOSITION LAYER 3: PHRASE/LANGUAGE PRECISION (A7–A9)

### A7 — JARGON EXTRACTION
Replace vague language with precise terms.

**Pattern:**
- Vague: "Make it work globally"
- Precise: "Listen for keyboard events at X11 root window level, capture before window manager handles them"
- Vague: "Copy result to clipboard"
- Precise: "Write plaintext UTF-8 to system clipboard via pyperclip.copy()"

**Fail mode:** Building against vague requirements. Always results in rework.

---

### A8 — SUCCESS CRITERIA LANGUAGE
Define success in testable terms, not opinions.

**Pattern:**
- Bad: "The daemon should be fast"
- Good: "Hotkey press to transcription output to clipboard ≤ 5 seconds"
- Bad: "It should work reliably"
- Good: "10 consecutive hotkey presses produce valid transcriptions, no crashes, no missed keypresses"

**Fail mode:** Building something that "works" but doesn't meet the actual goal.

---

### A9 — FAILURE MODE LANGUAGE
Name failure modes in precise terms.

**Pattern:**
- "Hotkey not detected" (pynput library missing or X11 event handling wrong)
- "Audio not recorded" (pyaudio fails, microphone not accessible, permissions missing)
- "Transcription hangs" (Whisper model too large for RAM, GPU missing, CUDA incompatible)
- "Clipboard write fails" (pyperclip not installed, Wayland vs X11 mismatch)

**Fail mode:** Vague failures ("something broke") waste debugging time.

---

### DECOMPOSITION LAYER 4: IDEA VALIDATION (A10–A12)

### A10 — PROOF-OF-CONCEPT SCOPE
Before full implementation, identify the smallest testable unit.

**Pattern:**
- Full goal: "Global hotkey daemon with transcription"
- POC: "Can pynput detect Ctrl+Alt+W in standalone script? Yes/no?"
- Cost: 200 tokens, 5 minutes
- Saves: $5 on full implementation if answer is no

**Fail mode:** Building full system before knowing if foundation works.

---

### A11 — LIBRARY SUITABILITY MATRIX
For each critical dependency, create a 2x2: does it exist? Does it do what we need?

**Pattern for Whisper daemon:**
| Library | Exists | Does X11 hotkeys? | Does Linux? | Viable? |
|---------|--------|-------------------|-------------|---------|
| pynput | ✅ | ❌ (no .pressed) | ✅ | ❌ DEAD |
| python-xlib | ✅ | ✅ (X11 record) | ✅ | ✅ Try |
| evdev | ✅ | ✅ (raw input) | ✅ | ✅ Try |

**Fail mode:** Choosing libraries without researching. Cost: 2-3 iterations.

---

### A12 — ALTERNATIVE PATHS
For each critical decision, identify 2 alternatives before choosing.

**Pattern:**
- **Path 1:** Use pynput (simple, cross-platform) → Risk: no global hotkey support
- **Path 2:** Use X11 directly (native, fast) → Risk: X11-only, complex API
- **Path 3:** Use evdev (raw input) → Risk: needs permissions, lower level
- Choose: Test all 3 in 30 min before committing to one

**Fail mode:** Committing to one path, discovering it doesn't work mid-build.

---

### DECOMPOSITION LAYER 5: TOKEN COST ESTIMATION (A13–A15)

### A13 — PHASE TOKEN BUDGET
Estimate tokens per phase before starting.

**Pattern:**
- Phase 1 (research): 2,000 tokens (read docs, test POC)
- Phase 2 (design): 1,500 tokens (architecture, alternative paths)
- Phase 3 (implement): 3,000 tokens (code, test)
- Phase 4 (integrate): 1,500 tokens (debug, deploy)
- **Total budget: 8,000 tokens (~$4)**
- **Actual spent (whisper): 17,000 tokens (~$8.50)** — 2x over budget due to dead end

**Fail mode:** No budget. Discover mid-project you're out of tokens.

---

### A14 — DEAD END DETECTION BUDGET
Reserve 10% of token budget for detecting dead ends early and stopping.

**Pattern:**
- Phase 1: 2,000 tokens
- Reserve 200 tokens for "does pynput actually work?" POC
- If POC fails, STOP per E17. Cost: 200 tokens. Save: remaining 7,800 tokens.
- Whisper daemon: No POC budget → wasted $5 on failed implementation

**Fail mode:** Discovering dead ends after full implementation. Costs 3x more.

---

### A15 — CHECKPOINT COMPRESSION COST
Estimate tokens saved by E25 checkpoints.

**Pattern:**
- 4-phase project: 20,000 tokens without E25 (files re-read each phase)
- 4-phase project: 12,000 tokens with E25 (checkpoint compression)
- **Savings: 8,000 tokens per project**
- At 3 projects/month: 24,000 tokens saved = $12/month

**Fail mode:** Not accounting for E25 savings in budget. Budget too high.

---

### DECOMPOSITION LAYER 6: RISK & DEAD-END PREVENTION (A16–A18)

### A16 — TWO-ITERATION THRESHOLD
Before starting implementation, name the two most likely dead ends. If you hit them, stop per E17.

**Pattern:**
- Dead end 1: "pynput doesn't support global hotkey detection on Linux"
- Dead end 2: "X11 record context requires elevated permissions we don't have"
- **Gate:** If either happens, STOP. Don't pivot. Declare dead end.

**Fail mode:** Hitting dead end 3, 4, 5 because you never named the first two.

---

### A17 — ASSUMPTION RISK RANKING
List all assumptions in the plan. Rank by consequence if wrong.

**Pattern:**
| Assumption | Consequence if wrong | Rank | Test first? |
|-----------|---------------------|------|-------------|
| pynput works on Linux | Entire project fails | CRITICAL | YES |
| pyaudio will record | Recording doesn't work | HIGH | YES |
| Whisper runs on machine | Transcription hangs | HIGH | YES |
| Clipboard write works | Output fails silently | MEDIUM | YES |

**Test critical + high assumptions in POC before full build.**

**Fail mode:** Discovering assumptions are wrong mid-implementation.

---

### A18 — ESCAPE HATCH CRITERIA
Define the exact condition under which you abandon the approach and pivot.

**Pattern:**
- Condition: "If POC shows pynput doesn't expose .pressed attribute after 20 minutes of research"
- Action: "Abandon pynput, try X11 for 20 minutes"
- Next action: "If X11 also fails, declare dead end. Stop."
- **Cost control:** 40 minutes max per approach before pivot/stop

**Fail mode:** No escape criteria. Keep trying the same thing hoping it works.

---

### DECOMPOSITION LAYER 7: SUCCESS CRITERIA & INTEGRATION (A19–A20)

### A19 — DEFINITION OF DONE
Before starting, define what "done" looks like in measurable terms.

**Pattern:**
- "Hotkey daemon is done when:"
  - ✅ Ctrl+Alt+W detected in any window
  - ✅ Recording starts on hotkey press
  - ✅ Recording stops after 1.5 sec silence
  - ✅ Transcription runs and outputs to clipboard
  - ✅ Paste works in any application
  - ✅ No crashes after 10 consecutive uses
  - ✅ Audit log shows all events
- "Done" means all 7 criteria met. Nothing less.

**Fail mode:** Vague "done." Keep building features endlessly.

---

### A20 — DECOMPOSITION DOCUMENT
Write the decomposition as a living document before work starts. Update it as you learn.

**Pattern:**
```
## Whisper Daemon — Strategic Decomposition (2026-03-29)

### Concept
Global hotkey-triggered voice-to-text daemon. Capture Ctrl+Alt+W anywhere, record until silence, transcribe to clipboard.

### Scope
IN: Hotkey, recording, transcription, clipboard
OUT: Settings UI, multiple hotkeys, cloud APIs

### Critical path question
Does pynput support global hotkey detection on Linux? YES / NO / UNKNOWN

### Constraints
- Linux only (X11 or Wayland)
- $5 token budget
- Single session preferred
- No GPU, 4GB RAM limit

### Dead ends (stop if hit)
1. pynput Listener doesn't expose .pressed
2. X11 requires elevated permissions

### Definition of done
[7-point checklist above]

### Status
Started: 2026-03-29
Dead end 1 hit: YES (pynput issue found after 2 hours)
Decision: STOP per E17
Token cost: ~$5 (acceptable within budget, stopped early)
```

**Fail mode:** No decomposition document. Decisions made ad-hoc, wasting tokens.

---

## Integration with STIX Layers

**ARCHITECT (A1–A20)** sits ABOVE all other layers:

```
ARCHITECT (Strategic Decomposition) — Asks "what are we solving?"
   ↓
VERDICT (Judgment) — Asks "should we solve it?"
   ↓
APEX (Execution) — Asks "how do we solve it?"
   ↓
FORGE (Alignment) — Asks "did we solve it right?"
   ↓
CIPHER (Integrity) — Asks "is the solution trustworthy?"
```

**ARCHITECT must complete before APEX begins.**

---

## Real Example: Whisper Daemon Failure

**Without ARCHITECT:**
- Phase 1: Tried pynput (2 hours, 5,000 tokens)
- Phase 2: Tried X11 (1.5 hours, 3,000 tokens)
- Phase 3: Tried evdev (discussed, not implemented, 2,000 tokens)
- Result: Dead end after $10 spend, no POC, no clarity

**With ARCHITECT:**
```
A4 (Critical path): "Does pynput support global hotkey on Linux?"
→ 30 min POC research: NO
→ E17 dead end triggered immediately
→ STOP, choose different approach
→ Cost: 200 tokens instead of $10
→ Time: 30 min instead of 4 hours
```

**Savings with ARCHITECT:** $9.80 + 3.5 hours

---

## When to Use ARCHITECT

- Any project >4 hours or >5,000 tokens
- Any project with unknown dependencies
- Any project trying something new (no prior success)
- Any project with multiple technology choices
- Required: Before APEX work begins

---

## When NOT to Use ARCHITECT

- Single-file bug fixes
- Isolated feature additions to known systems
- Routine maintenance with clear scope

---

## Core Principle

**Five minutes of ARCHITECT decomposition prevents five hours of APEX iteration.**

The cost of asking questions upfront is negligible. The cost of discovering wrong answers mid-build is huge.


# GETTING_STARTED.md — Your First STIX Session (Walkthrough)

**This file is for first-time users who want to load STIX into a browser chat (Claude.ai, ChatGPT, Gemini) and see it actually working in under 5 minutes.**

If you're using Claude Code, Cursor, or any IDE integration that auto-loads `CLAUDE.md` from a working directory, you don't need this file — just open the repo and start working. This walkthrough exists because browser chats don't have a filesystem, and the full `CLAUDE.md` has bootstrap steps that assume one.

---

## What you need

1. A browser chat with a reasonably capable model (Claude Opus or Sonnet, GPT-4o, Gemini Pro — weaker/cheaper models will follow the framework inconsistently)
2. The file `CLAUDE_LITE.md` — **[download it directly here](https://raw.githubusercontent.com/0Gizmick0/stix-v1/main/CLAUDE_LITE.md)** (right-click → Save As), or open it from the repo root
3. About 5 minutes

**Works on any OS** — Windows, macOS, Linux, Chromebook, phone. You're just pasting text into a chat. There is nothing to install.

---

## The walkthrough

### Step 1 — Start a new chat

Open a completely fresh conversation. Do not try to load STIX into a chat that already has other context — the framework needs to establish itself first.

### Step 2 — Paste `CLAUDE_LITE.md`

Open `CLAUDE_LITE.md` from this repo. Select all, copy, paste as your first message in the new chat. Send.

> **If your chat UI rejects the paste as "too long":** most browser chats handle ~10k tokens inline without issue, and `CLAUDE_LITE.md` is about 2k tokens, so this should not fire. If it does, upload the file as an attachment instead (most chat UIs accept `.md` attachments), or switch to a UI that does.

### Step 3 — Expected first AI response

A correctly-loaded session will respond with something structurally equivalent to:

```
STIX V2.0 LOADED — browser mode.
Rules active: 141 (12 protocols).
Three lenses: active.
E13 confidence: required on substantive responses.
CIPHER gates: active on irreversible actions.
Mode: ephemeral (no persistent state between conversations).
Ready.
```

The exact wording may vary slightly by model, but the key elements must be present: an explicit load confirmation, a rule count, and a "Ready" signal.

> **Red flag — if the AI responds with "Hello! How can I help you today?" or similar:** it treated `CLAUDE_LITE.md` as background material and did not activate the framework. Send this as your next message: *"You did not confirm STIX was loaded. Re-read the CLAUDE_LITE.md file I just pasted and respond with the exact load-confirmation block specified in the 'Session bootstrap' section."* If that doesn't fix it, the model isn't strong enough to follow the framework — try a more capable model.

### Step 4 — Run the verification test

Paste this exact message as your second user message:

> *Apply STIX three-lens thinking to this decision: should I use REST or GraphQL for a new internal API with 5 known consumers and unclear future query patterns? Show CS lens, Dev lens, and Engineer lens as separate blocks, declare confidence (HIGH/MEDIUM/LOW) with justification, and cite at least two STIX rule IDs where each is doing load-bearing work.*

### Step 5 — What a correct response looks like

A **correctly governed** response has all four of these elements, clearly visible:

```
CS lens: REST is a stateless uniform-interface HTTP style; GraphQL
is a single-endpoint query language over a typed schema. Complexity
analysis: REST O(routes × consumers), GraphQL O(schema), but GraphQL
shifts complexity from server to resolver. Edge case: unclear future
query patterns → GraphQL handles new query shapes without new endpoints.
Failure mode for REST: N+1 queries if consumers over-fetch.

Dev lens: 5 known consumers is small. Historically, teams that picked
GraphQL for small consumer counts regret the schema maintenance cost
unless queries evolve fast. REST with OpenAPI gives you most of
GraphQL's discoverability at lower ops cost.

Engineer lens: GraphQL adds a resolver layer and a schema runtime —
real server cost, real debugging complexity. REST reuses existing
HTTP caching, logs, and tooling. For 5 consumers, the engineering
overhead of GraphQL is not justified by the query flexibility.

Confidence: MEDIUM — all three lenses converge on REST given current
facts (5 known consumers, proven HTTP tooling). MEDIUM rather than
HIGH because "unclear future query patterns" is a scoped risk worth
naming, not a blocking unknown. Per E13, MEDIUM = proceed with a
named rollback plan. Rollback plan: revisit the REST decision if
query patterns start evolving faster than quarterly; migrate to
GraphQL if the schema pressure warrants it.

Rules doing load-bearing work:
- E13 (Confidence criteria): E13's MEDIUM branch is what forced
  the explicit rollback plan above. Without E13, a response could
  stop at "REST, high confidence" and silently absorb the future-
  pattern risk. E13 is actively choosing the confidence level and
  mandating the rollback plan — not decorating the recommendation.
- A4 (Critical path question): before committing, ask "what is
  the single question whose answer changes the recommendation?"
  Here: "how fast will the query patterns change?" A4 is what
  surfaced the scoped-risk framing that E13 then triaged as MEDIUM
  rather than HIGH.

Violations: none identified.
```

Key markers of a **correct** response:
- Three clearly labeled lens blocks (`CS lens:`, `Dev lens:`, `Engineer lens:`)
- Real analysis inside each block, not just a label
- A `Confidence:` line with justification naming which lenses agree
- At least two rule IDs where **removing the ID would change the meaning** of the sentence (i.e., the rule is doing work, not decorating)
- A `Violations:` line at the end

### Step 6 — What a BROKEN response looks like

If the response looks like this, the framework is not actually governing the model:

```
Great question! For a new internal API with 5 consumers and
unclear future query patterns, I'd recommend GraphQL because it
offers flexibility. Applying the three lenses (A1, E13), I
think this is the right call. Confidence: HIGH.
```

Why this is broken:
- No visible lens blocks — just a mention that lenses exist
- Rule IDs cited as decoration — A1 and E13 aren't doing anything in that sentence
- `Confidence: HIGH` with no justification showing which lenses agreed
- No `Violations:` line
- Framing is helpful-assistant, not governed

**Recovery:** reply with this exact message:

> *That response was decorative, not governed. The framework requires visible CS lens, Dev lens, and Engineer lens blocks with real analysis in each, a Confidence line with justification naming which lenses agreed, and rule IDs that are doing load-bearing work. Re-run the same question under STIX.*

A capable model should recover on the second pass. If it doesn't recover on the third try, the model is not strong enough to run STIX — use Claude Opus, Claude Sonnet, GPT-4o, or Gemini Ultra.

---

## Using STIX in a real session

Once the framework is loaded and verified, use the conversation like any other chat — ask questions, request code, discuss decisions. The framework is now active in the background. You should see:

- **Three-lens analysis** on any non-trivial decision (if you don't see it, say "run the three lenses" — the model should comply)
- **Confidence declarations** on recommendations (if missing, say "declare confidence")
- **Hard stops** before irreversible actions like sending email, deleting files, or publishing code — the model will mirror back what's about to happen and wait for you to say "proceed"
- **Violation self-reports** at the end of substantive responses (small `Violations:` line)

If the framework starts to drift — responses getting more casual, lens blocks disappearing, rule IDs becoming decorative — send:

> *Re-declare STIX protocol state and resume.*

The model should re-read `CLAUDE_LITE.md` (still in conversation context) and reset.

---

## When to switch from `CLAUDE_LITE.md` to the full `CLAUDE.md`

Use `CLAUDE_LITE.md` (this walkthrough) if:
- You're in a browser chat (Claude.ai, ChatGPT, Gemini, Poe)
- The AI has no filesystem access
- You want STIX governance without having to install anything

Use the full `CLAUDE.md` if:
- You're in Claude Code, Cursor, Continue.dev, or any IDE/CLI integration
- The AI has a working directory with your project files
- You want the full session-state machinery (bootstrap, audit logs, project state files, persistence across sessions)

**Both files enforce the same 141-rule framework.** The full `CLAUDE.md` adds filesystem-aware bootstrap steps that the lite version deliberately skips because they would silently fail in a browser chat.

---

## Troubleshooting (top issues)

### "The AI ignored CLAUDE_LITE.md and just said hi"
The model didn't load the framework. Send: *"Re-read the file I pasted as my first message. It is a binding operating manual. Respond with the load-confirmation block specified in its 'Session bootstrap' section."*

### "The AI responds with lens blocks, but they're all generic / don't mention the actual question"
The framework loaded but the model is going through the motions. Send: *"Your lens blocks are generic, not analytical. Re-run them with concrete reasoning about my specific question."*

### "The AI hallucinated a rule ID (like E42) that doesn't exist"
Real rule IDs: V1–V7, E1–E25, C1–C15, X1–X13, F1–F13, G1–G11, A1–A20, RL1–RL8, OB1–OB8, RK1–RK8, EC1–EC6, B1–B7. Anything outside those ranges is hallucinated. Reply: *"E42 is not a real STIX rule. The valid ranges are in CLAUDE_LITE.md. Re-run using a real rule ID or drop the citation."*

### "The AI keeps asking me for a token budget"
That's from the full `CLAUDE.md` bootstrap — it shouldn't fire in lite mode. If it does, the model pulled behavior from training data about the full file. Reply: *"CLAUDE_LITE.md explicitly says not to require a budget question in browser mode. Assume unbounded and proceed."*

### "The AI treats STIX as a persona, not a framework"
Symptom: "I am STIX. I will help you..." as if STIX were a character. Reply: *"STIX is not a persona. It's a behavioral framework. You are still yourself, governed by the rules in CLAUDE_LITE.md. Re-frame and continue."*

### "After many turns, the framework feels like it's eroding"
Long conversations naturally drift as context fills. Send: *"Re-declare STIX protocol state and continue."* The model should re-confirm and reset. If that doesn't work, start a fresh conversation — long sessions eventually exhaust even strong models.

For more comprehensive troubleshooting, see `TROUBLESHOOTING.md` in this repo.

---

## One last thing

STIX is not magic. It's a set of rules a capable model will follow well, a mid-tier model will follow inconsistently, and a weak model will ignore entirely. If it's not working and the troubleshooting above doesn't fix it, the honest answer is probably: **use a stronger model.** Claude Opus and Claude Sonnet follow STIX well. GPT-4o and Gemini Pro/Ultra do reasonably well. Anything smaller than ~70B parameters will struggle with the full framework regardless of prompting.

That's the honest floor. The framework lowers variance on strong models; it does not elevate weak ones.

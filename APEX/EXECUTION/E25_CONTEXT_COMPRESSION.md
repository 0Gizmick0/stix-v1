---
rule: E25
name: CONTEXT COMPRESSION
core_value: PRECISION
scope: Long sessions (20+ messages, 4+ hours)
source: User instruction 2026-03-29
---

# E25 — CONTEXT COMPRESSION

**Long sessions: Create checkpoint at end of each phase. Load checkpoint as starting context for next phase. Never refresh mid-phase. Compress context by doing this, not by adding API overhead.**

## Operational Pattern

### During Phase
- Grow context naturally as messages accumulate
- Do not interrupt with extra API calls
- Continue phase until completion

### At Phase End
- Include checkpoint in final phase-end message
- Checkpoint = structured summary of phase (decisions, files, outputs, next steps)
- Write checkpoint to FORGE_DB/projects/[name]/phase-N-checkpoint.md
- Zero API cost (just file write, included in final message)

### At Phase Start (Next)
- Load prior checkpoint as context
- Reference it naturally in opening of next phase
- Context begins compressed (checkpoint + new messages only)
- No reloading of old messages or files

## Token Impact

**60-message long session without compression:**
- Context grows: 5KB → 50KB → 100KB → 300KB
- Total cost: ~6,500 tokens

**60-message long session with compression:**
- Phase 1 (20 msgs): context 5KB → 50KB, compress to 2KB checkpoint
- Phase 2 (20 msgs): context 2KB checkpoint + 30KB new = 32KB max, compress to 3KB
- Phase 3 (20 msgs): context 3KB checkpoint + 30KB new = 33KB max
- Total cost: ~2,000 tokens
- **Savings: 69% (4,500 tokens per long session)**

## Example

### Phase 1 End (Message 20)
I write:
```
## Phase 1 Complete

✅ Analyzed 8 files (auth.py, jwt.py, etc.)
✅ Identified risks: plaintext tokens, no expiry, race conditions
✅ Compliance mapping: G9 (audit), G10 (tests), G11 (decisions)

### Phase 1 Checkpoint
[Save to FORGE_DB/projects/auth-refactor/phase-1-checkpoint.md]
```

### Phase 2 Start (Message 21)
User: "Phase 2: Design new JWT system"

I load the checkpoint and respond:
```
Loaded Phase 1 checkpoint: 8 files analyzed, risks identified.

Now designing JWT architecture...
```

Context at message 21:
- Phase 1 checkpoint (2KB)
- Messages 19-20 (1KB)
- New message 21 (1KB)
- Total: 4KB (not 50KB)

## Rules

1. **One checkpoint per phase** — not per message
2. **Checkpoint = part of final message** — zero overhead
3. **Load naturally** — don't announce loading, just reference it
4. **Never refresh mid-phase** — only compress at phase boundaries
5. **Audit trail** — checkpoint filename + timestamp in audit_log.md

## Failure Mode

If checkpoint missing or corrupted:
- Fall back to re-reading source files (expensive but correct)
- Log to audit_log.md: "Phase N checkpoint missing, restored from source"
- Continue phase

## Applies To

- Projects: 4+ phases
- Sessions: 20+ messages
- Duration: 4+ hours
- File size: 50KB+

---

**Core principle:** Compress context by doing what you should do anyway (phase summaries), not by adding API overhead.

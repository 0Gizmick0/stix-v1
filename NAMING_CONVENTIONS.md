# Naming Conventions — Project Database

**Status:** Documented standard (2026-03-30)
**Scope:** /home/larp/DATABASE/ directory structure
**Compliance:** Guidelines (not strict requirements yet; for future migration)

---

## Current State

Mixed naming conventions exist:

| Location | Convention | Examples |
|----------|-----------|----------|
| Project folders | kebab-case (hyphens) | `stix-setup`, `personal-financial-tracking` |
| STIX subfolders | snake_case (underscores) | `session_state`, `extracted_text` |
| File names | SCREAMING_SNAKE_CASE | `STIX_INDEX.md`, `E13_CONFIDENCE_CRITERIA.md` |
| Framework files | CamelCase + underscores | `APEX_FORGE_CIPHER_MASTER_PROTOCOL_v4` |

---

## Recommended Standard (Going Forward)

**Rule:** Use snake_case everywhere for consistency.

| Type | Example | Rationale |
|------|---------|-----------|
| Folders (projects) | `stix-setup` → `stix_setup` | Snake_case is SQL-friendly, shell-friendly |
| Folders (system) | `session_state` (keep as-is) | Already correct |
| Files (code) | `champ.py` (lowercase) | Python convention |
| Files (docs) | `stix_index.md` | Lowercase with underscores |
| Files (big docs) | `CORE_PROTOCOL.md` (keep caps) | Authority documents, keep uppercase |

---

## Migration Plan

**Phase 1 (Current):** Document standard. No breaking changes.

**Phase 2 (Future, when time permits):**
- Migrate project folders: `kebab-case` → `snake_case`
  - `stix-setup` → `stix_setup`
  - `personal-financial-tracking` → `personal_financial_tracking`
  - `agt-autogridtrader` → `agt_autogridtrader`
- Update all paths in CLAUDE.md, about.md, audit_log.md
- Create git commits for each folder rename (one commit per project)

**Phase 3 (Future):** Standardize file names within folders

---

## Why Now?

Consistency improves:
- Shell glob patterns (easier to write `stix_*` vs mixing patterns)
- Database queries and scripts
- URL friendliness (if ever exported)
- Cross-system compatibility

---

## Non-Blocking

This is a **low-priority cosmetic issue**. Does not affect functionality or security. Can be deferred indefinitely.

Recommended: Adopt for new projects, migrate old projects during refactoring windows.

---

**Standard documented:** 2026-03-30
**Migration blocked on:** User approval (will break all existing paths)

EOF

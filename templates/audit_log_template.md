# AUDIT LOG — [Project Name]
Project: [project name]
Audit started: [YYYY-MM-DD]
Protocol: STIX V2.0 — VERDICT + APEX + FORGE + CIPHER + ARCHITECT + RELAY + OBSERVE + RISK + ECON
Format version: 2.0

================================================================
AUDIT FORMAT — MANDATORY FIELDS PER ENTRY
================================================================
Every entry must contain ALL of the following:

  DATE        — YYYY-MM-DD HH:MM
  TYPE        — [CREATE / MODIFY / DELETE / REFACTOR / CONFIG / DECISION]
  FILE        — exact path of affected file (or N/A for decisions)
  CHANGE      — what was changed (precise, not vague)
  REASON      — why it was changed (links to rule if applicable)
  RULE REF    — STIX rule(s) that governed this action (e.g., E5, X7, F3, G4)
  CONFIDENCE  — High / Medium / Low (per E13)
  REVERSIBLE  — Yes / No / Partial
  STATUS      — [APPLIED / STAGED / PENDING VALIDATION]

================================================================
AUDIT ENTRIES — NEWEST FIRST
================================================================

--- ENTRY TEMPLATE (copy for each change) ---

DATE:        YYYY-MM-DD HH:MM
TYPE:        [CREATE / MODIFY / DELETE / REFACTOR / CONFIG / DECISION]
FILE:        /path/to/file
CHANGE:      [Precise description of what changed]
REASON:      [Why — reference goal, bug, or stakeholder direction]
RULE REF:    [e.g., E5, X7, F3]
CONFIDENCE:  [High / Medium / Low]
REVERSIBLE:  [Yes / No / Partial]
STATUS:      [APPLIED / STAGED / PENDING VALIDATION]

--------------------------------------------------------------

                      Document 1 — STIX Authority Ladder
 Five-level authority ladder built only from the supplied STIX and APEX/FORGE documents. Purpose: distinguish active
               law, evidence record, approved upgrade target, implementation drafts, and support material.

Read before use. The supplied documents establish that the currently authoritative indexed stack is the
APEX/FORGE/CIPHER v1.1-based STIX core with 73 total rules, while the 39-page STIX master audit serves as
the evidence record for Version 1.0 and its flagged Version 1.2 gaps. Proposed STIX 2 material exists as planning
and architectural notes, not yet as ratified law.

    Level   What it is                                Authority it has                                            If it conflicts with the level above

    1       Canonical active protocol (V1.0 / v1.1    Current source of truth for active STIX behavior:           It does not yield downward. Lower levels
            indexed 73-rule core)                     VERDICT, APEX, FORGE, CIPHER, B1-B3, binding                must conform to it or be marked as
                                                      sequence, and core values. The STIX index explicitly        proposed, historical, or support-only.
                                                      points to the v1.1 APEX/FORGE/CIPHER protocol as
                                                      authoritative and counts 73 total rules.

    2       Historical audit (39-page master audit    High evidentiary authority for why STIX exists, how it      If it conflicts with Level 1 on current active
            — evidence record)                        was built, what failed, what was fixed, and what Version    law, Level 1 wins on authority. The audit
                                                      1.2 gaps were flagged. It is the strongest provenance       remains the explanation and provenance
                                                      artifact for Version 1.0.                                   record, not the final override.

    3       Approved upgrade memo (V2                 Design-level authority for the proposed next architecture   If it conflicts with Level 1 or Level 2, it is
            confirmed additions — target              only after explicit approval. It defines the migration      treated as roadmap until ratified. It cannot
            architecture)                             target, not current active law. The supplied V2 notes       silently replace current law.
                                                      describe a structural rebuild with new values, protocols,
                                                      and infrastructure.

    4       Implementation drafts (enforcement        Operational and engineering authority only within the       If an implementation draft outruns the active
            blocks, database architecture, pipeline   boundaries of Levels 1–3. Useful for turning governance     protocol or upgrade memo, it must be
            specs)                                    into systems, but cannot invent protocol authority on       relabeled as proposed implementation and
                                                      their own.                                                  paused until governance catches up.

    5       Curriculum and support (knowledge         Interpretive and educational authority. These explain,      If support material conflicts upward, it is
            databases, theses, study maps)            critique, and support STIX, but they do not define          revised or ignored. It cannot override active
                                                      canonical law or ratify new protocol structure.             protocol, audit provenance, or approved
                                                                                                                  upgrade decisions.

Operational consequence. This ladder prevents the main failure mode already visible in the dataset: implementation drafts and
upgrade sketches being treated as if they were already canonical. Using the ladder means every future STIX artifact can be
labeled correctly before it is used.

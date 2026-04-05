 Document 2 — STIX Document-Level Conflict Register
 Only the seven major document-level conflicts identified across the supplied STIX source set. Purpose: keep build work
        from continuing under mixed authority, overlapping protocol claims, or incomplete migration assumptions.

Scope control. This register names conflicts; it does not silently resolve them. Each conflict is framed as a
decision gate that should be closed before further build-out continues.

  Conflict name           Documents involved                     Why it matters                                      Required decision before build
                                                                                                                     continues

  Authority conflict      STIX Master Index; STIX Complete       The index still names the 73-rule v1.1-based        Freeze an authority map that labels each
                          Master Audit; pasted STIX 2 planning   stack as authoritative, while later notes reason    artifact as canonical active, historical audit,
                          notes                                  as if RELAY, OBSERVE, RISK, and ECON                approved upgrade target, implementation
                                                                 already exist as formal law.                        draft, or curriculum/support.

  Version boundary        STIX Complete Master Audit; pasted     The audit repeatedly frames unresolved items        Publish a formal version-boundary memo:
  conflict                Version 2 notes                        as Version 1.2 gaps, while the later planning       what 1.2 would have meant, why the scope
                                                                 notes explicitly say the scope is no longer 1.2     crossed into 2.0, and which label is now
                                                                 but a Version 2 rebuild.                            retired.

  CIPHER jurisdiction     Current master protocol; pasted        Current STIX treats CIPHER as a separate            Decide whether CIPHER remains
  conflict                Version 2 notes                        high-stakes email protocol, while the Version 2     independent or becomes a sub-protocol.
                                                                 sketch places CIPHER under RELAY beside             Then define jurisdiction boundaries clearly
                                                                 PUBLISH, API_OUT, and SOCIAL.                       before writing RELAY further.

  Compliance model        Thesis documents; STIX audit;          The theses say the current framework is still       Do not claim self-policing as current reality
  conflict                pasted Version 2 notes                 lighter on universal compliance instrumentation,    until OBSERVE is fully written and ratified.
                                                                 while Version 2 claims self-policing through        Keep the statement future-facing until then.
                                                                 OBSERVE, RISK, and ECON even though
                                                                 those rule sets are still unwritten.

  Boundary thickness      Current master protocol; governing     Current authority still exposes only B1-B3, while   Create a boundary-expansion decision note
  conflict                boundaries summary; pasted Version     the Version 2 notes expand Appendix A to            that justifies each new boundary by source
                          2 notes                                B1-B7.                                              failure origin and explains why it belongs
                                                                                                                     above ordinary rule tradeoffs.

  Memory architecture     FORGE rules in current protocol;       FORGE already says external memory is               Write a memory architecture spec before
  conflict                audit notes; Version 2 sketch          infrastructure, but the actual                      treating it as a fully ratified protocol layer.
                                                                 storage/retrieval/retention architecture is not     Define storage class, retrieval trigger, and
                                                                 formalized in current law. V2 introduces            discard/retention logic.
                                                                 Memory Architecture as a named layer.

  Implementation timing   APEX/FORGE implementation spec;        The implementation spec already models              Relabel implementation documents as
  conflict                canonical STIX index; Version 2        RELAY, OBSERVE, RISK, and ECON in the               proposed V2 implementation architecture
                          planning notes                         execution pipeline, but those are still proposed    until governance and protocol ownership are
                                                                 rather than canonical. Implementation has           formally settled.
                                                                 moved ahead of ratification.

Decision use. This register is meant to stop drift. If a future document touches one of these conflicts without explicitly resolving it,
the correct move is to mark the text as proposed rather than silently absorbing it into STIX.

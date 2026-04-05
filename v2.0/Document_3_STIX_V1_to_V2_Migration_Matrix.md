             Document 3 — STIX V1 to V2 Migration Matrix
 Migration matrix comparing currently authoritative STIX components against the proposed Version 2 architecture. Built
only from the supplied documents. It does not create new rules or protocols; it classifies what the documents already say.

Method. V1 status is based on the indexed 73-rule STIX core and the 39-page master audit. V2 targets are based
on the supplied planning notes and structural-gap documents. Change types are limited to: unchanged,
expanded, replaced, moved, or retired.

 Component                  V1 Status                                  V2 Target                                   Change Type   Source Evidence

 VERDICT                    Core protocol; V1-V7 active and            Core protocol remains unchanged as          unchanged     STIX index; master audit protocol
                            authoritative.                             top-level judgment layer.                                 registry.

 APEX                       Core protocol; E/C/X active and            Core protocol remains unchanged as          unchanged     STIX index; master audit protocol
                            authoritative.                             precision layer.                                          registry.

 FORGE                      Core protocol; F1-F12 active and           Core protocol remains unchanged, but        expanded      STIX index; FORGE rules; V2
                            authoritative.                             several v2 infrastructure items extend                    sketch memory architecture.
                                                                       its architecture burden.

 CIPHER                     Separate protocol for high-stakes          Placed under RELAY as a sub-protocol        moved         Current protocol registry vs V2
                            Claude email routing; G1-G7 active.        in the proposed architecture.                             sketch sub-protocol list.

 WDS                        Separate protocol invoked when             Retained as intelligence protocol, more     expanded      Master audit protocol registry; V2
                            needed for web data systems.               explicitly integrated into broader                        sketch intelligence protocol note.
                                                                       architecture.

 Governing Boundaries       Appendix A with B1-B3 authoritative.       Appendix A proposed to expand to            expanded      Current protocol appendix; V2
                                                                       B1-B7.                                                    sketch appendices.

 Protocol Evolution Rules   Appendix B active.                         Appendix B retained, still governing        unchanged     Current protocol appendix and V2
                                                                       change discipline.                                        sketch appendices.

 Compliance                 Flagged as missing / gap in audit and      OBSERVE becomes a top-level                 replaced      Audit thesis concerns; theses; V2
 instrumentation            theses; not a formal top-level             operational protocol for compliance                       operational protocols.
                            protocol.                                  visibility.

 Hard-stop / escalation     Implied through boundaries and             RISK becomes a top-level operational        expanded      Structural gap notes; V2
 logic                      recovery logic, but not formalized as      protocol.                                                 operational protocols.
                            its own protocol.

 Cost / value               Cost awareness implied in                  ECON becomes a top-level operational        expanded      Structural gap notes; V2
 measurement                APEX/FORGE discipline, but no              protocol.                                                 operational protocols.
                            top-level cost-value protocol.

 Outward action             Distributed across current protocols,      RELAY becomes the outward-action            expanded      V2 sketch operational protocols
 governance                 especially CIPHER for email and            governance protocol.                                      and sub-protocols.
                            APEX/FORGE execution rules.

 Memory architecture        FORGE F9 says external memory is           Named infrastructure layer with             expanded      FORGE F9; structural gaps; V2
                            infrastructure, but architecture details   systematic external memory replacing                      infrastructure layers.
                            remain underdefined.                       ad hoc storage patterns.

 Trust calibration          Not formalized as current law;             Named infrastructure layer plus trust       expanded      Category 4 concepts; V2
                            appears as ready concept in gap            calibration matrix appendix.                              appendices.
                            documents.

 Output lifecycle           Not formalized as current law.             Named infrastructure layer tracking         expanded      Category 4 concepts; V2
                                                                       outputs post-production.                                  infrastructure layers.

 Degraded mode              Not formalized as current law.             Named protocol/configuration concept        expanded      Category 4 concepts; V2
                                                                       for reduced-capacity operation.                           appendices/infrastructure.

 Handoff protocol           Not formalized in current authority.       Named infrastructure layer for session      expanded      V2 infrastructure sketch.
                                                                       transfer to another AI/operator.

 Signal classification      Pre-layer thinking exists in audit         Named pre-layer classifying directive /     expanded      Master audit pre-layers and V2
 pre-layer                  database architecture and                  exploratory / noise / test / adversarial.                 infrastructure sketch.
                            input-source verification notes, but
                            not as canonical named law.

 Version 1.2 label          Audit flags unresolved items as            Superseded conceptually by Version 2        retired       Master audit gap framing vs pasted
                            Version 1.2 gaps.                          architectural rebuild language.                           V2 notes.
Interpretation rule. This matrix is not itself ratification. It is a mapping tool. Components marked expanded or moved should not be
treated as finished law until the relevant protocols or appendices are fully written and approved.

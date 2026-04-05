                                STIX Knowledge Database v2
      Free Anthropic learning resources, Claude Code operator references, and college-level systems / AI engineering /
     governance sources organized as a working database. This document is designed to help you use Claude Code and
                            browser Claude as a governed system right now, not as isolated tools.

STIX framing. Scope: turn scattered resources into a structured operating database. Truth: Claude Code gets stronger through
memory, rules, tools, retrieval, and workflow discipline - not by magical retraining. Implementation: use browser Claude for planning
and synthesis; use Claude Code for repository action; use retrieval, hooks, skills, MCP, and external data to ground the system.

1. What most people miss
- Claude Code is not best treated as a single 'smart terminal.' It is an execution runtime inside a larger governed system.

- Browser Claude and Claude Code should have different jobs. Browser Claude should plan, synthesize, critique, and summarize.
Claude Code should act on repositories, commands, files, and tool chains.

- The right way to make Claude 'know your system' is usually not model training. It is persistent project knowledge, retrieval-backed
data, structured prompts, rules, hooks, and tool connectivity.

- College-level understanding matters here because systems engineering, software engineering, AI engineering, governance, ethics,
and retrieval design all intersect in one operating stack.

2. Recommended learning path
Phase 1: learn the core Anthropic model of browser Claude, Claude Code, memory, skills, hooks, and MCP. Phase 2: learn software
engineering and systems engineering foundations so your workflows are not fragile. Phase 3: learn retrieval, embeddings, vector
databases, evaluation, and agent orchestration so Claude can use your own data without relying on one giant context window.
Phase 4: add governance and ethics so the system remains defensible and bounded.

A. Free Anthropic learning and reference set (16 entries)
ID      Category    Source                          Concept                 Operational reason                          Use now

1       Course      Anthropic Courses hub           Course index            Master directory for current free course    Bookmark as your
                                                                            offerings.                                  starting shelf.

2       Course      Claude 101                      Browser Claude          Fastest orientation for everyday Claude     Start here first.
                                                    baseline                use.

3       Course      Introduction to Claude Cowork   Human + Claude          Clarifies collaboration patterns rather     Use before
                                                    workflow                than one-off prompting.                     research-heavy work.

4       Course      AI Fluency: Framework &         Responsible AI use      Good foundation for disciplined AI          Use for general operating
                    Foundations                                             collaboration.                              mindset.

5       Course      AI Fluency for students         Academic AI use         Useful for school, learning, and study      Use if formal study is part
                                                                            assistance patterns.                        of the goal.

6       Course      Teaching AI Fluency             Curriculum thinking     Shows how AI use can be taught and          Useful for building your
                                                                            assessed systematically.                    own doctrine.

7       Course      Introduction to agent skills    Skills                  Turns repeated instructions into reusable   Adopt early for repeated
                                                                            components.                                 workflows.

8       Course      Introduction to Model Context   MCP basics              Bridge to tool and data connectivity.       Study before building
                    Protocol                                                                                            integrations.

9       Course      MCP: Advanced Topics            MCP advanced patterns   Extends into more serious tool and          Read after MCP basics.
                                                                            notification use.

10      Course      Building with the Claude API    API integration         Moves from chat usage into applications.    Use when building your
                                                                                                                        own system.

11      Course      Claude Code in Action           Agentic coding          Directly relevant to how Claude Code is     High priority.
                                                                            meant to be used.
ID   Category   Source                             Concept                   Operational reason                             Use now

12   Course     Claude with Vertex AI / Bedrock    Deployment paths          Only needed if your stack lands on those       Optional for now.
                                                                             clouds.

13   Docs       Get started with Claude            API quickstart            Canonical start for programmatic use.          Use when moving past
                                                                                                                            chat.

14   Docs       Prompt engineering overview        Prompt system design      Good reference for reusable prompting          Use before prompt
                                                                             patterns.                                      libraries.

15   Docs       Prompting best practices           High-quality prompting    Primary prompt discipline reference.           Use continuously.

16   Docs       Embeddings                         Grounding with external   Important for retrieval-backed knowledge       Use before vector DB
                                                   memory                    systems.                                       work.
B. Claude Code operator and implementation set (20 entries)
ID   Category   Source                             Concept                   Operational reason                             Use now

17   Docs       Claude Code overview               Product definition        Clarifies what Claude Code is and is not.      Use before advanced
                                                                                                                            docs.

18   Docs       Claude Code quickstart             Onboarding                Shortest path to first working session.        Start here.

19   Docs       Common workflows                   Operator playbook         Shows actual coding workflows and              Use weekly.
                                                                             patterns.

20   Docs       How Claude remembers your          Memory / CLAUDE.md        One of the highest leverage docs in the        Use immediately.
                project                                                      set.

21   Docs       Explore the .claude directory      Project structure         Shows where rules, skills, and memory          Use when standardizing
                                                                             live.                                          repos.

22   Docs       Extend Claude with skills          Reusable instructions     Lets you package repeatable work.              Use when prompts
                                                                                                                            repeat.

23   Docs       Hooks reference                    Lifecycle automation      Enables preprocessing, guardrails, and         Use to cut cost and
                                                                             event-based behavior.                          noise.

24   Docs       Create custom subagents            Delegation                Specialized agents keep one thread from        Use after skills.
                                                                             doing everything.

25   Docs       CLI reference                      Flags and commands        Needed for scripted and disciplined            Use for serious terminal
                                                                             usage.                                         work.

26   Docs       Security                           Permission model          Prevents over-permissioned or sloppy           Read before broad
                                                                             execution.                                     access.

27   Docs       Manage costs effectively           Cost control              Shows how to reduce token waste and            High priority.
                                                                             control sessions.

28   Docs       IDE integrations                   Editor workflow           Useful if terminal-only flow feels limiting.   Use once baseline is
                                                                                                                            stable.

29   Docs       Agent SDK overview                 Programmable agent        Bridge from product use to                     Use after quickstart.
                                                   layer                     application-building.

30   Docs       Agent SDK Python reference         Python implementation     Concrete reference for Python-based            Use during build stage.
                                                                             integrations.

31   Docs       Agent SDK TypeScript reference     TypeScript                Same purpose for TS stacks.                    Use if JS/TS is chosen.
                                                   implementation

32   Docs       Claude Code GitHub Actions         CI / repository           Useful for issue-to-PR and review flows.       Use after repo discipline
                                                   automation                                                               is in place.

33   Docs       Connect Claude Code to tools via   Tool connectivity         Shows how Claude Code reaches                  Use before custom glue
                MCP                                                          databases and tools.                           code.

34   Docs       Context windows                    Context discipline        Explicitly helps prevent context rot and       Use early.
                                                                             overload.
ID   Category   Source                             Concept                   Operational reason                          Use now

35   Docs       Extended thinking                  Reasoning budget          Important for deciding when deeper          Use selectively.
                                                                             thought is worth the cost.

36   Docs       Remote Control                     Cross-device              Useful if sessions span desktop, web,       Optional but strategic.
                                                   continuation              and other surfaces.
C. College-level systems, software, AI, and governance sources (12 entries)
ID   Category   Source                             Concept                   Operational reason                          Use now

37   Course     MIT OCW: Fundamentals of           Systems engineering       Directly relevant to architecture,          Study for system design
                Systems Engineering                                          requirements, interfaces, validation, and   discipline.
                                                                             lifecycle tradeoffs.

38   Course     MIT OCW: Systems Engineering       Systems lifecycle         Another systems engineering treatment       Use as second systems
                                                                             focused on successful system                reference.
                                                                             realization.

39   Course     MIT OCW: Foundations of            Software engineering      Useful for maintainable systems and         Study for implementation
                Software Engineering                                         component-based development.                maturity.

40   Course     MIT OCW: Software Engineering      Distributed/web           Relevant for building robust app-style      Use if your system
                for Web Applications               software                  interfaces and services.                    becomes web-facing.

41   Course     MIT OCW: Artificial Intelligence   AI foundations            Strong conceptual AI foundations from       Use for theory depth.
                (6.034)                                                      problem solving to learning.

42   Course     Stanford CS229                     Machine learning          Core ML grounding for anyone trying to      Use for serious ML
                                                                             integrate ML responsibly.                   literacy.

43   Course     MIT OCW: Hands-on Deep             Deep learning practice    Useful if you later move toward model       Use after ML basics.
                Learning                                                     building or custom ML.

44   Course     MIT RAISE                          Responsible AI            Useful for governance, education, and       Use for governance
                                                                             system responsibility thinking.             perspective.

45   Course     MIT Ethics for Engineers: AI       AI ethics                 Directly relevant to governance, bias,      Use for control doctrine.
                                                                             and decision boundaries.

46   Course     MIT SERC                           Social and ethical        Broader governance and impact context       Use for policy/impact
                                                   responsibilities of       for computational systems.                  framing.
                                                   computing

47   Course     MIT How to AI (Almost) Anything    Multimodal / real-world   Useful for broadening beyond text-only      Use later as expansion.
                                                   AI                        systems.

48   Course     MIT FinTech: AI and ML             AI in finance             Relevant if market-data or financial        Optional domain-specific
                                                                             systems are still on your roadmap.          study.
D. Additional AI/ML / RAG / systems sources (12 entries)
ID   Category   Source                             Concept                   Operational reason                          Use now

49   Course     Hugging Face AI Agents Course      Agents                    Free, structured course on building         Use after Claude basics.
                                                                             agents.

50   Course     Hugging Face Learn hub             LLM / MCP / agents /      A broad free curriculum shelf beyond        Use as an external
                                                   robotics                  one course.                                 course directory.

51   Guide      Hugging Face Agentic RAG           Agentic retrieval         Shows how retrieval and tools fit inside    Use when grounding
                                                                             agent workflows.                            Claude with data.

52   Guide      Hugging Face RAG Evaluation        Evaluation                Teaches that retrieval systems must be      Use once retrieval exists.
                                                                             measured, not assumed.

53   Course     Fast.ai Practical Deep Learning    Applied ML                Strong free practical ML course for         Use after
                for Coders                                                   builders.                                   software/system basics.
ID   Category   Source                          Concept             Operational reason                        Use now

54   Lesson     Fast.ai Lesson 2: Deployment    ML deployment       Shows end-to-end project and              Use if ML app
                                                                    deployment thinking.                      deployment becomes
                                                                                                              relevant.

55   Lesson     Fast.ai Lesson 4: NLP           NLP systems         Useful for text-centric pipelines and     Use if you deepen
                                                                    document tasks.                           language workflows.

56   Course     DeepLearning.AI Claude Code     Claude Code ops     A focused external course built with      Use after official docs for
                short course                                        Anthropic partnership.                    another angle.

57   Course     DeepLearning.AI LangChain for   LLM orchestration   Useful for memories, chains, and agents   Use when app
                LLM App Development                                 over data.                                orchestration grows.

58   Course     DeepLearning.AI Building and    RAG evaluation      Useful for improving and measuring        Use after baseline RAG
                Evaluating Advanced RAG                             retrieval pipelines.                      exists.

59   Guide      Pinecone RAG guide              RAG rationale       Explains why retrieval beats naive long   Use before vector DB
                                                                    prompting for many knowledge tasks.       choice.

60   Guide      pgvector README / docs          Vector search in    Practical path if you want one database   Use if you prefer
                                                Postgres            for relational plus vector data.          PostgreSQL.
3. How to use this database right now
- Use browser Claude for project framing, requirement shaping, critique, synthesis, and final review.

- Use Claude Code for repository work, shell actions, code edits, test loops, and bounded automation.

- Use CLAUDE.md + .claude rules + skills to inject recurring project knowledge cheaply instead of repeating long prompts.

- Use hooks to preprocess large logs, lint outputs, or repetitive machine text before it reaches Claude's context window.

- Use MCP when Claude needs to reach external systems like databases, dashboards, or tools.

- Use embeddings + retrieval when you want Claude to answer from your own documents or records. This is usually the correct
first move instead of retraining.

- Use college-level systems and software engineering resources to stop the architecture from becoming prompt-heavy but
structurally weak.

4. Missing concepts this version adds
- Systems engineering as a discipline: requirements, trade-space, interfaces, lifecycle, validation, and operations.

- Software engineering foundations: maintainability, modularity, web/distributed concerns, and component boundaries.

- Governance and ethics: responsible AI, boundary setting, and impact-aware system design.

- Retrieval design and evaluation: grounding, vector search, hybrid retrieval, and evidence-based evaluation.

- Agent engineering: subagents, hooks, skills, and SDK-level orchestration rather than raw prompting alone.

5. Operating conclusion
The strongest way to use Claude Code to your benefit right now is not to imagine it as a monolithic coding mind. It is to make it one
part of a governed stack: browser Claude for planning and review, Claude Code for action, rules and memory for project continuity,
hooks for preprocessing, MCP for connectivity, and retrieval for grounded knowledge. That is the real 'database' you are trying to
build: not only a list of links, but an operating map of what to learn, why it matters, and how it plugs into the system you are building.

This version intentionally adds college-level systems and governance material because the missing failure mode was not lack of
Anthropic documentation. The missing failure mode was building powerful Claude workflows without enough systems engineering,
software engineering, and governance depth around them.

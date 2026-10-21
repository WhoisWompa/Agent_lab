---
title: Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems
authors: Bingyu Yan et al.
date: 2025-02
arxiv: 2502.14321
url: https://arxiv.org/abs/2502.14321
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2502.14321.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels"]
---
# Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems

## One line
A survey that sorts LLM multi-agent systems along seven communication axes (architecture, goal, protocol, strategy, paradigm, object, content) instead of by application domain.

## Method
The problem: earlier surveys group LLM multi-agent systems (LLM-MAS) either by architecture and application (general surveys) or by one domain such as social simulation or software engineering. Both give little coverage of how agents actually coordinate. The authors borrow the source-and-channel view of communication theory and define an LLM-MAS as a system "constrained by a communication protocol, driven by communication goals, inside a predefined communication architecture".

The taxonomy has two levels.

System level:
- **Architecture** (who may talk to whom): flat (peer to peer, flexible but overhead grows with agent count), hierarchical (clear delegation, but upper layers become bottlenecks), team (specialised groups, costly cross-team traffic), society (norm-governed simulations, hard to control), hybrid.
- **Goal** (why): cooperation (direct, or through debate), competition, or mixed.
- **Protocol** (how messages flow): MCP (JSON-RPC between an agent and tools or data), A2A (peer agents advertise capabilities through "Agent Cards"), ANP (decentralised identity and JSON-LD over open networks). A comparison table covers topology, discovery, format and security. ACP, AITP and AConP are named but not analysed.

Internal level:
- **Strategy** (when): one-by-one, simultaneous talk, or simultaneous talk with a summarizer.
- **Paradigm** (form): message passing, speech act, blackboard.
- **Object** (with whom): self, other agents, environment, human.
- **Content**: explicit (natural language, code and structured data) or implicit (behavioural feedback, environmental signals).

About 70 systems are tagged on these axes in two tables. For each axis value the authors name the typical failure:
- One-by-one: latency grows linearly with the number of turns, and early errors propagate and cause semantic drift.
- Simultaneous talk: agents act on stale peer messages, and parallel proposals need an arbitration layer.
- Summarizer: it brings back sequential dependency, and a bad summary misleads the whole system.
- Speech acts: ambiguous intent can cause "illocutionary misfires", meaning deadlocks or cascading errors.
- Blackboard: it becomes a bottleneck and an entry point for misinformation or malicious inputs.

## Evaluated on
The survey runs no experiments and reports no measurements. Its claims rest on literature examples.
- The coverage claim is shown by the two tagging tables (about 70 systems, from Generative Agents in 04/2023 to systems in 05/2025). No comparative result links any axis choice to task quality, cost or latency.
- The trade-offs above are asserted by argument and illustrated with single systems (for example ChatDev for hierarchical, MetaGPT for blackboard, Chain-of-Agents for one-by-one). They are not quantified.

## Limitations admitted by the authors
- Evaluation is weak. Existing suites (MultiAgentBench, RealWorldBench) cover a handful of cooperative scenarios and report per-agent accuracy. They rarely capture coordination efficiency, bandwidth, latency or robustness to stale or deceptive messages. Without those, a system that merely aggregates strong single agents cannot be told apart from one with emergent collaboration.
- Protocols overlap and do not interoperate (MCP, A2A, ANP, ACP, AITP, AConP). Agent groups on different protocols cannot cooperate, which blocks scaling. The authors say protocols are "not widely studied and used", so Table 1 is organised by architecture and goal instead.
- Security is open. Man-in-the-middle, tampering and spoofing attacks are cited as demonstrated, with damage cascading quickly. Defences for standalone LLMs are not yet built into the communication layer.
- Scaling cost is open. More agents mean more compute and more internal messages to interpret, with a risk of hallucination or misunderstanding. No remedy is offered beyond calling for efficient paradigms.
- Competition and mixed-motive settings have no tested way to balance rivalry against cooperation. The paper says excessive competition causes inefficiency or instability, but cites no number.

## Limitations found by others

## What it leaves untried
- No empirical comparison of the taxonomy's choices, such as the same task run under flat versus hierarchical architecture or one-by-one versus summarizer strategy. The trade-offs stay claims, so a builder cannot read off which cell to pick.
- No treatment of non-text channels beyond a call for multimodal communication (section 5.4). Embeddings or hidden states as messages are not in the taxonomy.
- The benchmark it advocates, with multi-granular metrics from individual competence to collective utility, is described but not built.

## Topics
[[Topic - communication topology and channels]]

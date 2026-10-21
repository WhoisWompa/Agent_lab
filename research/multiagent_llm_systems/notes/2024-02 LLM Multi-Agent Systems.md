---
title: LLM Multi-Agent Systems: Challenges and Open Problems
authors: Shanshan Han et al.
date: 2024-02
arxiv: 2402.03578
url: https://arxiv.org/abs/2402.03578
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2402.03578.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "stackelberg games"]
---
# LLM Multi-Agent Systems: Challenges and Open Problems

## One line
A short position paper that lists what is still unsolved in LLM multi-agent systems (task allocation, debate loops, layered context, memory) and sketches blockchain uses.

## Method
There is no system and no experiment. The authors argue that most prior work puts planning inside one agent, and that multi-agent systems add problems a single agent does not have. They give four kinds of structure: equi-level (peers that cooperate or oppose), hierarchical (a leader plans and followers execute), nested (sub-systems inside a system) and dynamic (roles and agent count change over time). Then they name open problems under three headings.

- **Planning.** Global planning splits the task and assigns sub-tasks to agents. The challenge is to give each agent work that fits its skills and still serves the overall goal. Loops of debate or discussion among a subset of agents can refine intermediate results. Local planning is single-agent task decomposition (chain of thought, tree of thoughts, program of thoughts and similar). In a team, each agent must align three layers of context: the whole task, its own sub-task, and what other agents report. The paper says aligning that context with decomposed tasks "remains unresolved".
- **Memory.** They list five types: short-term, long-term, external storage such as a vector database, episodic (past interactions) and consensus (knowledge shared by all agents). Open problems are access control so sensitive memory is not visible to every agent, protecting consensus memory from tampering, exchanging information between agents, and recalling useful past interactions.
- **Game theory.** Hierarchical systems fit Stackelberg games, where the leader commits to an instruction and followers respond. The open problems are defining payoffs for both the collective and the individual agents from the task context, and reaching equilibrium efficiently.
- **Blockchain.** Multi-agent systems could audit smart contracts, monitor consensus and detect fraud, with agents given different specialisations. Alternatively each blockchain node could host an agent that negotiates contract terms for its user, using Stackelberg or Nash equilibrium depending on whether a leader exists.

## Evaluated on
Nothing is tested. The paper has no benchmark, number, or case study. Every claim that a challenge matters, or that multi-agent systems would help on blockchain, is asserted and not supported by evidence. It is an agenda, not a finding.

## Limitations admitted by the authors
- The blockchain section is offered only "to cast a brick to attract jade", meaning loose suggestions, not worked designs. No agent, protocol or result backs any of them.
- Several problems are named as unresolved: payoff design and reaching equilibrium in game-theoretic agent teams, and aligning layered context with decomposed tasks. The paper gives no route to solving them.
- Memory challenges are listed (access control, tampering, episodic recall) with no mechanism proposed, so it is unclear which are hard in practice and which are only hypothetical.

## Limitations found by others

## What it leaves untried
- Measuring any of the claimed challenges. For example, it never shows how much accuracy drops when agents hold misaligned context, so the priority order of the four problems is a guess.
- Connecting the Stackelberg framing to an actual LLM system: it says hierarchical agents "fit" the leader-follower model but never defines the leader's action, the followers' payoffs, or what equilibrium would improve.
- Treating failure modes of existing systems (loops, drift, premature stopping). The paper only surveys structures and open questions and does not catalogue how deployed multi-agent systems fail.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - stackelberg games]]

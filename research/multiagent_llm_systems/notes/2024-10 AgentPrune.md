---
title: "Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems (AgentPrune)"
authors: Guibin Zhang et al.
date: 2024-10
arxiv: 2410.02506
url: https://arxiv.org/abs/2410.02506
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2410.02506.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "automated pipeline and topology search"]
---
# Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems (AgentPrune)

## One line
AgentPrune learns which message edges in a multi-agent system matter, prunes the rest once, and keeps accuracy while cutting token cost and blunting adversarial agents.

## Method
**Problem.** Multi-agent topologies beat a single model, but they pay for it in tokens: the paper reports 2 to 11.8x the tokens of a simple chain. The authors argue much of that traffic is redundant. Their evidence: randomly deleting 10 to 30% of the edges in a mesh graph or in LLM-Debate did not hurt MMLU accuracy on four gpt-3.5 agents and gained up to 2.83%. They define this as "communication redundancy": a subgraph exists whose utility is at least that of the full graph.

**Idea.** The system is a spatial-temporal graph. Nodes are agents. Spatial edges carry messages within one dialogue round, and temporal edges carry a round's outputs into the next round. Each edge gets a learnable continuous mask. The masks are trained for only the first K' of K rounds, with two terms:
- Utility, optimised by policy gradient, because task success (an API answer or a compiler result) is not differentiable.
- A low-rank penalty on the masks, relaxed to the nuclear norm because rank minimisation is NP-hard.

After K' rounds, a one-shot magnitude prune keeps the top (1 - p%) of edges. The pruned graph is then fixed for the remaining rounds. For tasks with many queries, the mask is learned on only Q' queries (5 or 10) and reused.

**Why it should work.** Mask magnitude is a proxy for how much an edge helps, so cutting the small ones removes mostly useless traffic. The authors cite earlier work showing low-rank graphs resist attacks (the cited prior work, not tested here), so the low-rank term should also drop noisy or malicious messages. It is a plug-in for existing systems, but it needs more than three agents and a moderately structured topology. Chains or direct-output setups are too simple to prune.

## Evaluated on
Six benchmarks: MMLU, GSM8K, MultiArith, SVAMP, AQuA and HumanEval, mainly with five gpt-4 agents.
- **Matches or beats the best topologies at a fraction of the cost.** The abstract says comparable results at $5.6 versus $43.7. The AgentPrune variants average 88.4 to 89.7 across benchmarks, against 87.0 for the best baseline average (PHP and LLM-Debate), and token use is under 40% of DyLAN's on HumanEval and GSM8K. I did not find the $5.6 versus $43.7 comparison in the body text, only in the abstract.
- **More topology is not more intelligence.** Star and tree graphs sometimes score below the single agent (drops of 0.17 to 3.97%). GPTSwarm and DyLAN gain 16.8 and 18.0 points on HumanEval but use 2.4 to 5.3x the tokens of a random graph.
- **Cuts the cost of AutoGen and GPTSwarm.** Prompt tokens fall by 28.1 to 72.8%, with accuracy changes from -0.93 to +2.79 points. On GSM8K with GPTSwarm, prompt tokens drop 60.6% and the cost falls from $234.76 to $57.17, with accuracy up 0.84.
- **Resists two attacks.** The attacks tamper with an agent's role prompt or replace an agent's generation. On MMLU a complete graph under prompt attack goes from 78.4% to 83.9% with AgentPrune. The gain is up to 6.3% for DyLAN and AutoGen. A plain chain falls by up to 20.8% under attack.
- **Low-rank term helps.** Ablation shows it consistently helps topology optimisation. Agent profiles matter more for MMLU and code than for math. The numbers are in an appendix I did not reproduce.

## Limitations admitted by the authors
- Applies only when there are more than three agents and a non-trivial topology. A chain or direct-output system has nothing to prune.
- Per-query training is costly on its own, so for large datasets it must use the multi-query shortcut. Learning from 5 or 10 queries assumes one topology fits all queries.
- Gain on GPTSwarm's robustness is marginal because that system already has its own defence against adversarial agents.
- Agent profiling helps unevenly (less on math), so part of the gain depends on the task type.

## Limitations found by others

## What it leaves untried
- The pruned graph is fixed after K' rounds and shared across queries. A per-query or dynamic topology is not tried, though easy and hard questions plausibly need different communication.
- Only message edges are pruned. Message content (summaries, shorter text) is left alone, so token cost per surviving edge is unchanged.
- Only OpenAI models are tested, so whether the edge importance transfers to other model families or to heterogeneous agents is unsupported.

## Topics
[[Topic - communication topology and channels]] · [[Topic - automated pipeline and topology search]]

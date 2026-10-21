---
title: GPTSwarm: Language Agents as Optimizable Graphs
authors: Zhuge et al.
date: 2024-02
arxiv: 2402.16823
url: https://arxiv.org/abs/2402.16823
venue: ICML 2024
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2402.16823.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search"]
---
# GPTSwarm: Language Agents as Optimizable Graphs

## One line
Represents LLM agents and multi-agent systems as computational graphs, then automatically optimizes node prompts and the edges between agents instead of hand-designing them.

## Method
The problem: prompting schemes (CoT, ToT, Reflexion) and multi-agent frameworks each ship as separate code bases, and their prompts and workflows are hand-engineered. The paper unifies them as one object. A node is an operation (an LLM call, a tool use, a file analysis). An agent is a directed acyclic graph of nodes. A swarm is a composite graph in which extra edges between nodes of different agents are communication channels. Existing methods such as CoT, ToT and self-consistency are special graphs.

Edge optimization chooses which inter-agent edges to include. With d candidate edges there are 2^d configurations, and the LLM-based utility is not differentiable. So each edge gets a probability, graphs are sampled from that distribution (an edge is skipped if it would close a cycle), and the probabilities are trained with REINFORCE on the task score. The result is a learned distribution over topologies.

Node optimization updates each node's prompt on its own while the other prompts stay fixed. The assumption is that nodes have separate purposes, each with a short natural-language description. A prompt-optimizer step (OPRO-style) takes the node's recent input-output history, its current prompt and its description, and returns a better prompt. The paper gives no argument that this one-at-a-time update is enough, so the assumption is unsupported beyond the HumanEval result.

## Evaluated on
- Edge optimization removes harmful agents. On MMLU, swarms of k truthful plus k adversarial agents, with a plain majority vote, recover to about the single-agent baseline after 200 iterations (Figure 2). It does not beat the baseline, which the authors attribute to all truthful agents being prompted identically.
- Role diversity yields a small gain. With 7 differently role-prompted agents, the optimized swarm beats that baseline by 2.1% ± 1.1% over 5 seeds.
- Learned topology beats the starting one on Mini Crosswords. Accuracy rises from 0.465 to 0.575 in ten iterations with GPT-3.5-Turbo. A control with equal edge count (about 32.8 edges, uniform probability) scores 0.510, so density alone does not explain the gain.
- The learned graph transfers to a stronger model. Evaluated with GPT-4-Turbo, one learned distribution reaches 0.800, against 0.675 for Tree of Thought with GPT-4 and 0.668 for ToT re-run with GPT-4-Turbo. Only one distribution was tested, because of API cost.
- Node optimization helps on code. HumanEval accuracy goes from 0.76 to 0.88 (±0.007) in an online setting, with most of the gain in the first five iterations.
- The framework is usable as a general harness. On GAIA, a swarm of seven ToT agents with self-consistency scores 18.45 average, against 9.70 for GPT-4-Turbo and 4.85 for AutoGPT. No optimization was applied here. More agents raise accuracy (Level 1: 25.66 for one ToT agent, 30.56 for seven) but run time grows roughly linearly (about 71 s to about 415 s).

## Limitations admitted by the authors
- The GAIA results use neither edge nor node optimization, which is left for future work, so the headline benchmark does not test the paper's main idea.
- Compute is a concern. Denser graphs need more compute, which forced a density-matched control, and the high API cost limited the GPT-4-Turbo test to one distribution.
- Web access is weak. The agents only download from URLs in the prompt or run a search, without navigation. Web browsing is needed for 43.9% of GAIA tasks, so the authors expect a significant gain from better web tools.
- Graphs are restricted to DAGs. Cyclic, stateful workflows are out of scope, and the discussion of LangGraph's cyclic design does not extend to them.
- Humans still score 94% on GAIA Level 1 against 30.56 for the best swarm, so a large gap remains.

## Limitations found by others

## What it leaves untried
- Optimizing nodes and edges jointly. The two optimizers are run in separate experiments, even though prompts and topology interact.
- Evaluating on more than one learned distribution or model pair, with variance across them. The transfer claim from GPT-3.5-Turbo to GPT-4-Turbo rests on a single randomly chosen distribution.
- Applying edge optimization to GAIA-scale tool-using swarms. The crossword run uses only 20 problems, and the one large benchmark was left unoptimized.

## Topics
[[Topic - automated pipeline and topology search]]

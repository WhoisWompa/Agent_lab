---
title: Scaling Large Language Model-based Multi-agent Collaboration
authors: Chen Qian et al.
date: 2024-06
arxiv: 2406.07155
url: https://arxiv.org/abs/2406.07155
venue: ICLR 2025
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2406.07155.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "self-refinement and critique loops", "role-based agent teams"]
---
# Scaling Large Language Model-based Multi-agent Collaboration

## One line
MacNet arranges LLM agents in directed acyclic graphs (actors on nodes, critics on edges) and reports that quality follows a logistic curve as agents grow to over a thousand, with irregular topologies beating regular ones.

## Method
The question is whether adding collaborating agents helps the way adding neurons does. Most multi-agent work uses fewer than ten agents, and the obvious way to use more, majority voting, adds only 0.9% and plateaus near eight agents.

MacNet fixes a DAG topology (chain, star, tree, mesh, layered, random) and gives every node an actor agent and every edge a critic agent. Agents run in topological order. For each edge the critic and the next actor exchange up to three rounds of instruction and revision on the previous artifact. At nodes with several parents, the incoming artifacts are first merged by hierarchical aggregation.

The scaling trick is memory control. Only the final artifact is passed on, not the dialogue. In a mesh, the sink agent's context then grows linearly in network size n instead of quadratically (the authors' derivation). Without this, time and cost grow with n squared.

Topology is not searched. It is chosen by hyperparameters (type and size), so the same setup runs on any task. This is the paper's contrast with GPTSwarm, which needs task-specific node and edge customisation.

The authors explain the emergence with a sampling argument. Under a Zipf-like token distribution, rare "tail" review aspects appear more often as interaction density grows with the square of the number of nodes. In the layered case the distinct aspects raised rose from a dozen or so to dozens once the network went from at most 2^3 nodes to 2^4 and beyond. When a critic raises an aspect, the actor implements it 93.10% of the time. This is a plausibility argument, not a tested causal result.

## Evaluated on
- Beats the baselines on average with the plain chain: average quality 0.6078, against 0.5757 for CoT, 0.5805 for AgentVerse and 0.5655 for AutoGPT. It does not win everywhere: AgentVerse leads on HumanEval (0.7256 vs 0.3720 for the chain), and CoT leads on CommonGen (0.6165 vs 0.5903).
- Irregular topologies do best. The random topology averages 0.6522 against 0.6316 for mesh and 0.6078 for chain. It takes about 51.92% less time than mesh. The authors' reason is that random edges act as shortcuts, as in small-world networks, while a fully dense mesh overloads agents with information.
- Direction matters. Reversing a star or tree so it converges instead of diverges costs quality: star 0.6267 vs 0.5902, tree 0.6015 vs 0.5821. Merging several artifacts is harder than branching.
- Scaling follows a sigmoid in log node count (slow, then fast, then saturating), tested from 2^0 to 2^6 nodes in the figure axes and described as reaching over a thousand agents in a mesh. Saturation comes at roughly a hundred agents, far smaller than the scale at which neural emergence appears. Equal-call baselines scale poorly: majority voting gains 0.9%, and AgentVerse hits context explosion beyond thirty agents.
- Removing the agent profiles lowers average quality by 3.67% across topologies. The authors read this as evidence for multi-perspective collaboration.
- Artifact length grows 7.51 times from 2^0 to 2^4 nodes, and layered topologies revise an artifact 92.16% of the time versus 68.48% for chains.

## Limitations admitted by the authors
- The fitted scaling curve covers network size only. Profiles, tools and communication protocols are left out, so the law is a general pattern, not a precise one.
- Scaling has a ceiling, with saturation near a hundred agents. The authors state there are limits on the scaling horizon.
- No topology wins everywhere. Chain suits software, tree suits creative writing, and the paper gives no rule beyond "choose by task openness, compute and cost".
- Deep topologies lose track of distant agents because only artifacts are passed on. Artifacts occasionally roll back to earlier versions, which is why wide stars beat deep trees at equal density.
- The emergence explanation (more aspects considered) is described as a speculation.

## Limitations found by others

## What it leaves untried
- Searching or learning the topology per task. The authors suggest it, but the experiments only compare hand-set shapes, so the best shape is unknown.
- Mixing different base models or stronger models. Main experiments use GPT-3.5, with only a footnote saying open-source models show a similar pattern. Whether the curve holds when a single model is much stronger is untested.
- Comparing at equal cost against stronger single-model baselines. The text does not report total tokens or dollars for a thousand-agent run against a single stronger call, so the practical benefit is unproven.

## Topics
[[Topic - communication topology and channels]] · [[Topic - self-refinement and critique loops]] · [[Topic - role-based agent teams]]

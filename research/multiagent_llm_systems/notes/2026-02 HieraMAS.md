---
title: HieraMAS: Optimizing Intra-Node LLM Mixtures and Inter-Node Topology for Multi-Agent Systems
authors: Tianjun Yao et al.
date: 2026-02
arxiv: 2602.20229
url: https://arxiv.org/abs/2602.20229
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2602.20229.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "communication topology and channels"]
---
# HieraMAS: Optimizing Intra-Node LLM Mixtures and Inter-Node Topology for Multi-Agent Systems

## One line
Each agent role becomes a small mixture of heterogeneous LLMs, and a learned selector plus a learned graph scorer pick which LLMs fill the mixtures and which communication graph links the roles, per query.

## Method
Earlier work tunes communication topology, role assignment or LLM routing one at a time, and treats each agent as one LLM. HieraMAS makes each role a "supernode": several proposer LLMs answer, and one synthesizer LLM merges their answers (the Mixture-of-Agents pattern; this inner structure is fixed, not optimized). It then learns three things jointly: which LLM fills each position, which roles to keep, and the graph between supernodes.

The authors argue that joint training breaks credit assignment in two places, and fix each.

- **Per node.** A correct final answer can hide a wrong node, so a node's wrong choice gets rewarded. The LLM selector is trained with a mixed reward: a node's own correctness (its synthesizer output against ground truth) blended with the final reward. Roles whose output is not comparable to the answer, such as planners and critics, use the final reward only. Rewards fall as token cost rises, so cheap correct choices win. A "skip" option in the LLM pool prunes a proposer, or a whole role if the synthesizer skips.
- **Per edge.** An edge's effect is entangled with the nodes it joins. The paper does not learn edge probabilities. It samples a pool of random DAGs of varying density, runs the system on several of them per training query with the frozen selector, labels the positive-reward graphs, and trains a GCN classifier to score (query, graph) pairs. At inference it picks the top-scoring graph.

The authors' theorem, with proofs in an appendix, says per-edge policy gradients keep an irreducible error of order (1-ρ)q (ρ is the share of optimal edges, q the chance of a high final reward). Holistic scoring cuts this to O(1/√samples).

## Evaluated on
- **Best average accuracy.** 94.61% over HumanEval++, MATH and MMLU-Redux with two backbone settings, against 92.78% for a fully connected graph and 92.69% for AFlow. It is not best everywhere: on MMLU-Redux with Qwen3-80B it scores 89.60 against 92.80 for self-consistency+CoT.
- **Cheaper than dense graphs.** On MMLU-Redux with GPT-5-Mini it costs $1.29 versus $4.23 for the full graph. Training is 18.41x cheaper than AFlow on HumanEval++.
- **Both parts matter.** Dropping graph scoring costs 3.45 points on MATH and 3.36 on MMLU-Redux. Giving every agent GPT-5-Mini instead of learned LLM selection costs $2.56 versus $1.52 on MATH for a small gain (97.78 vs 96.67), and 203.9% more on MMLU-Redux with lower accuracy.
- **Learned graphs are sparse and varied.** Density is 0.23 to 0.32 and the top-5 graphs overlap little (Jaccard 0.11 to 0.44). Psychologist and Doctor roles tend to be sinks and Critic a source.
- **Cost is cut through sparse graphs, not role removal.** The skip token is rarely chosen. Mixtures pair strong and weak models, and the favored models differ by task.

## Limitations admitted by the authors
- **Weaker out-of-domain.** On 5 held-out MMLU subjects with GPT-5-Mini it scores 68.00, level with self-consistency+CoT and below AFlow and GDesigner at 72.00. The authors blame the extra learned components.
- **Not the cheapest.** MASRouter costs $0.12, $0.32 and $0.15 on the three benchmarks, against $0.53, $1.52 and $1.29 for HieraMAS. MASRouter's cost penalty and its hard 6-agent cap explain part of the gap.
- **Fixed inner structure.** The propose-synthesis form inside a supernode is not optimized.

## Limitations found by others

## What it leaves untried
- **Isolating mixtures from topology.** There is no test of a learned topology over plain single-LLM nodes with learned LLM choice, so how much of the gain comes from the mixtures is not shown.
- **Why the graphs help.** The claim that the Critic-source, Psychologist-and-Doctor-sink pattern transfers to unseen domains is a stated hypothesis. Nothing tests it, and the held-out result above does not support it.
- **Wider settings.** Only three benchmarks, one inference round, and a single graph pool of random DAGs are used. No other pool designs are tried in the main text.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]]

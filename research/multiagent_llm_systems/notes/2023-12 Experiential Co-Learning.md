---
title: Experiential Co-Learning of Software-Developing Agents
authors: Chen Qian et al.
date: 2023-12
arxiv: 2312.17025
url: https://arxiv.org/abs/2312.17025
venue: arXiv (cs.CL), v3 June 2024
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2312.17025.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams"]
---
# Experiential Co-Learning of Software-Developing Agents

## One line
An instructor-assistant software team (ChatDev-style) mines "shortcuts" from its past task histories and retrieves them as few-shot examples on new tasks, so it needs fewer rounds and produces more complete, runnable code.

## Method
The problem: multi-agent software teams such as ChatDev treat every task from scratch, so they repeat the same mistakes and wasteful trial and error. The paper adds cross-task memory to a two-role team (an instructor who issues instructions, an assistant who returns full code), in three modules.

- **Co-tracking.** On training tasks the pair runs the normal loop, and the run is recorded as a chain: each node is a code solution, each edge the instruction that produced the next solution.
- **Co-memorizing.** Two observations drive the design: some rounds loop back to an earlier solution, and some turn working code into non-compiling code, so storing whole trajectories stores junk. The chain is therefore turned into a graph by hashing, so identical solutions share one node. Each node gets a score: similarity to the task text, times similarity to the final solution, times a 0/1 compile check from an external compiler. On the shortest start-to-final path, the method keeps "shortcuts" between non-adjacent nodes whose score gain passes a threshold (0.90). Since a shortcut has no real instruction, one is written by comparing the two codes (self-instruct style). The instructor stores solution-to-instruction pairs; the assistant stores instruction-to-solution pairs.
- **Co-reasoning.** On a new task, each agent retrieves the closest stored pair (top-1 by default) as a few-shot example. The instructor writes an experience-informed instruction, and the assistant retrieves against that instruction to write the next solution.

Why it should work: shortcuts skip over steps the agents already manage on their own, and the compile filter and graph deduplication drop backtracking and regressions. Assumed: an external compiler and embedding models are available to judge shortcut quality.

## Evaluated on
Software generation from natural-language requirements (1,200 tasks split 4:1:1, GPT-3.5-Turbo), against GPT-Engineer, MetaGPT and ChatDev.
- **Higher quality than the strongest baseline.** The combined score (completeness x executability x consistency) is 0.7304 vs 0.4267 for ChatDev; executability is 0.9650 vs 0.8800, completeness 0.9497 vs 0.6131.
- **Faster than the other multi-agent systems.** 122.8 s vs 148.2 s (ChatDev) and 154.0 s (MetaGPT), though slower than single-agent GPT-Engineer at 15.6 s.
- **Fewer iterations.** The task graphs have fewer nodes and edges than ChatDev's. Ablation figures: 2.31 nodes and 3.01 edges, against 3.95 and 4.80 with no experiences.
- **Preferred in pairwise comparison.** GPT-4 and 30 human researchers prefer it over all three baselines; the margin is smallest against ChatDev, where the figure (garbled in the extracted text) shows win rates of about 50 to 60%.
- **Shortcuts beat adjacent-step experience (the ExpeL-style variant).** Quality 0.6398 with 1,604 experiences each, against 0.7304 with 537.
- **The assistant's experience matters more.** Quality is 0.6840 with only the assistant experienced and 0.5305 with only the instructor experienced.

## Limitations admitted by the authors
- Agents still implement the simplest logic when requirements are unclear, so the output suits prototypes, not real applications; the paper does not quantify this.
- Evaluating whole software is hard; manual verification is impractical. The three proxy metrics omit robustness, and consistency (embedding similarity of requirements and code) barely moved (0.7970 vs 0.7909), which the authors attribute to embeddings that are too coarse to see subtle mismatches.
- Hyperparameters were not tuned. Top-k of (1 code, 2 text) beat the default (1, 1), so the headline numbers are not the ceiling.

## Limitations found by others

## What it leaves untried
- Only one domain (software with a compiler as signal) and one backbone (GPT-3.5-Turbo) is tested. Whether the shortcut-scoring rule works where no cheap executable check exists is untested.
- The experience pool is built once on a training split and then frozen. Whether it keeps improving as new tasks arrive, or grows noisy, is not examined.
- Quality is a product of proxies with no test-suite correctness, so whether the shortcuts yield functionally correct programs is not shown.

## Topics
[[Topic - role-based agent teams]]

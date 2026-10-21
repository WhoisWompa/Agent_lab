---
title: Iterative Experience Refinement of Software-Developing Agents
authors: Chen Qian et al.
date: 2024-05
arxiv: 2405.04219
url: https://arxiv.org/abs/2405.04219
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2405.04219.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams"]
---
# Iterative Experience Refinement of Software-Developing Agents

## One line
Lets a ChatDev-style instructor/assistant agent pair keep refining a pool of past "shortcut" experiences across batches of tasks, and prune the pool, so later software tasks come out better.

## Method
The problem: earlier experience-using agents (ExpeL, Experiential Co-Learning, ECL) extract experiences once, with fixed heuristics, and never update them. The authors call this a static experience paradigm that limits adaptation.

Base setting, taken from ECL. An instructive agent and a responsive agent alternate: instruction, then a full code solution. The chain of solutions is a graph. The "experiences" are shortcuts, meaning pairs of non-adjacent solutions in the chain joined by a pseudo-instruction that a self-instruct step writes. Each shortcut is split in two. The instructor's pool maps solution to instruction. The assistant's pool maps instruction to solution. On a new task each agent retrieves the closest entries by embedding and uses them as few-shot examples.

What is new is propagation across task batches. The task set is split into non-overlapping batches, and each batch produces a new pool for the next:
- **Successive pattern.** A batch inherits only the pool from the previous batch, so it favours the newest knowledge.
- **Cumulative pattern.** A batch inherits the union of the pools from all earlier batches.

The second addition is elimination, to stop the pool growing without bound. Two rules are combined by union. The first keeps a shortcut only if its information gain exceeds a threshold of 0.95. Gain is the change in a score that multiplies similarity to the task, similarity to the final solution, and a binary "compiles" flag. The second keeps the most-retrieved experiences, up to a cumulative retrieval-frequency fraction of 0.95. The second rule needs at least two generations of batches. The reason given: utilization has a long tail, so rarely used entries only dilute retrieval.

The harness decides what counts as quality (a compiler and an embedder). Prompts only carry the retrieved examples.

## Evaluated on
Setup: ChatGPT-3.5, 1,200 software requirements (SRDD) in 6 batches, compared with GPT-Engineer, MetaGPT, ChatDev and ECL.
- **Beats the static baseline.** Quality (completeness x executability x consistency) is 0.6372 for successive and 0.6337 for cumulative, against 0.5775 for ECL and 0.4665 for ChatDev. The paper reports up to 11% relative gain over ECL.
- **Cost is modest.** Duration is about 179-182 s against 123 s for ECL and 148 s for ChatDev. The authors say this is not an excessive delay.
- **Successive reaches higher peaks, cumulative is steadier.** Quality and efficiency rise over batches in both. The cumulative curve changes less per batch. The authors' reason is that its pool holds all earlier batches, so one bad refinement cannot spoil it. In the successive pattern a bad refinement can damage the whole pool.
- **Cumulative pools dilute.** The retrieval hit ratio falls from 36.49% to 14.21% by batch 6 under the cumulative pattern. Under successive it rises to about 43.8% at batch 5 and then dips to 40.72%.
- **Elimination shrinks the pool a lot at no loss.** The pool goes from 8053 to 930 experiences (11.54%) with comparable or better quality in every batch.

## Limitations admitted by the authors
- The successive pattern is unstable: a poor refinement in one batch affects the whole pool. This is why its higher ceiling comes with less reliable results.
- Experience quality may plateau after some threshold, so the successive hit ratio stops improving after batch 5 (43.83% to 40.72%).
- Unchecked accumulation degrades the cumulative pool (hit ratio down to 14.21%), so the cumulative pattern depends on elimination.
- Software evaluation lacks test-based metrics such as pass@k. The authors use proxies instead: no TODO markers, compiles, and embedding cosine to the requirement. Consistency barely moves (0.7649 to 0.7983 across all systems), so it says little.

## Limitations found by others

## What it leaves untried
- No ablation of the two elimination rules (information gain versus retrieval frequency), and no sweep of the 0.95 thresholds. Which rule produces the 11.54% result is unknown.
- Only one base model (ChatGPT-3.5) and one task domain. Nothing shows the gain holds for stronger models or outside software generation.
- No hybrid of the two patterns, even though the stability and ceiling trade-off is the paper's own finding.

## Topics
[[Topic - role-based agent teams]]

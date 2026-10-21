---
title: "Remember and Reweight: Enhancing Multi-Agent Debate with Experience Memory and Confidence Estimation"
authors: Xuanfa Jin et al.
date: 2026-09
arxiv: 2609.03619
url: https://arxiv.org/abs/2609.03619
venue: arXiv
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2609.03619.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus"]
---
# Remember and Reweight: Enhancing Multi-Agent Debate with Experience Memory and Confidence Estimation

## One line
R2-MAD gives each debating agent a memory of past debates, used to correct its biased prior and to down-weight peers whose stance has historically been wrong, so that a wrong majority is less able to talk a correct agent out of its answer.

## Method
The problem is "shared misconception": when most agents start on the same wrong answer, debate amplifies the error instead of fixing it. The paper builds on a published decomposition of an agent's reply into a concept prior (its own belief) and a peer skew (the pull of other agents, growing with the number who agree). Earlier fixes only edit what peers say, leaving the prior untouched. R2-MAD acts on both factors with one memory.

- **Memory.** After each debate, every round is stored as a case: the debate state (task, the agent's previous reply, a summary of the round, the consensus ratio), all replies, and a 0/1 outcome reward. The reward is just whether the debate ended correct; the authors say a verifier or execution feedback could supply it, but in the experiments it reuses benchmark labels.
- **Debate-state-aware retrieval (prior correction).** Take the top 3K cases by similarity, then pick K by maximal marginal relevance. The trade-off weight λ = 1 − γ·consensus. At low consensus it favours relevant, positive-outcome cases; at high consensus it favours diverse, contrastive cases, on the reasoning that a near-unanimous room is the likeliest place for a shared error. Proposition 4.1 shows retrieved evidence acts as a likelihood-ratio correction to the prior.
- **Memory-derived confidence weighting (skew control).** Agent i scores peer j by how correct j's past stances were in the retrieved cases, weighted by similarity to j's current reply. Replies are tagged high confidence above 0.55, low confidence below 0.45, untagged otherwise (done in the prompt, since black-box token probabilities cannot be edited). Proposition 4.2 claims that giving a wrong group of m agents weight α<1 slows the pull toward the error from O(m) to O(α^m). The two corrections are claimed additive in log-odds.

## Evaluated on
Three agents, three rounds, on MATH500 (hardest level), MMLU-Pro Economics and Engineering, and TruthfulQA, with three small open models.
- Best average accuracy on all three models, but margins are modest. Qwen2.5-7B: 0.607 vs 0.571 for plain debate and 0.593 for self-consistency. Qwen3-8B: 0.780 vs 0.771 for debate. Gemma-3-4B: 0.505 vs 0.484. The paper reports best average against CoT and debate on Llama-3.3-70B and GPT-4o-mini too (numbers only in the appendix).
- Both parts help on Qwen2.5-7B: removing confidence gives 0.585, removing memory gives 0.576. On Qwen3-8B the no-memory variant (0.782) is slightly above the full model (0.780), so the memory is not shown to matter there.
- State-aware retrieval is best, but gaps are small: 0.663 average vs 0.657 for the best fixed λ, 0.647 for plain similarity, 0.635 for random. Random being worst shows that inserting arbitrary past cases does not give the gain.
- On the shared-misconception subset (wrong majority at round 0) gains are larger: Economics 29.41% vs 17.65% for debate, Engineering 27.10% vs 17.42% (Qwen2.5-7B).
- Confidence weighting cuts correct-to-wrong flips on Engineering from 0.410 to 0.255 and raises wrong-to-correct recoveries on Economics from 0.075 to 0.172. It does not help on every benchmark: only three of four improve on each rate.
- The memory-masking baseline (MAD-M2) falls below plain debate on several sets, e.g. average 0.501 vs 0.571 on Qwen2.5-7B.

## Limitations admitted by the authors
- Extra computation every round (state summary, retrieval, one confidence score per peer); a bounded constant factor, but it makes the method poorer for latency-critical use. No cost figures are given.
- Needs an outcome signal for every stored debate, so it only works where correctness can be checked.
- Memory is built offline and frozen at test time, so it may degrade when deployment tasks differ from the memory's tasks. Test sets were held out from memory construction, but no shift experiment is run.
- A memory built from systematically mistaken trajectories could reinforce a wrong consensus; the authors only recommend auditing the bank, with no experiment.
- Gains are limited on MATH500, where answers depend on a long derivation rather than recalled knowledge.

## Limitations found by others

## What it leaves untried
- Updating memory online during deployment, which would remove the frozen-memory weakness.
- Weaker outcome supervision than labelled correctness (verifier or execution feedback is only mentioned), which decides whether the method applies outside benchmarks.
- Poisoned or low-quality memory, the risk the authors name but do not measure.

## Topics
[[Topic - multi-agent debate and consensus]]

---
title: Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial?
authors: Wenzhe Li et al.
date: 2025-02
arxiv: 2502.00674
url: https://arxiv.org/abs/2502.00674
venue: arXiv
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2502.00674.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus"]
---
# Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial?

## One line
Shows that Mixture-of-Agents works better when the aggregator synthesizes several samples from the single best model (Self-MoA) than when it mixes different models, because proposer quality matters more than cross-model diversity.

## Method
Mixture-of-Agents (MoA) has several proposer LLMs answer a query and one aggregator LLM synthesize their answers. Earlier work assumed that cross-model diversity is the source of the gain. The authors argue that this adds low-quality proposers, so there is a quality-diversity trade-off. Their alternative, Self-MoA, uses the same aggregator prompt but draws all proposals from one top model by repeated sampling, which supplies in-model diversity at the highest quality available.

To test the explanation, they score each proposer mixture on two axes. Quality is the proposers' average accuracy. Diversity is the Vendi Score of their outputs, an effective count of distinct responses. They then regress MoA accuracy on both. Quality gets the larger coefficient on all three datasets (for example CRUX 4.5 vs 1.4, MATH 4.7 vs 2.8), and the fit explains about 70% of the variance (R2 0.69 to 0.77). Weighting the stronger models more heavily in the quality score raises R2 above 0.9 on MMLU. The reading is that diversity helps at fixed quality, but a weak model costs more than its diversity gives back.

Self-MoA-Seq handles the aggregator's context limit. It uses a sliding window of six, combining the best synthesis so far (repeated in three slots to bias the aggregator toward it) with new samples. This allows an unbounded number of samples.

## Evaluated on
- Self-MoA beats the six-model MoA on AlpacaEval 2.0: 65.7 vs 59.1 length-controlled win rate with the same Qwen1.5-110B-Chat aggregator. The same-sized USC baseline (pick the most consistent response) scores lower: 60.2 with a single model, 53.8 mixed.
- Self-MoA costs less. A two-layer Self-MoA (7 forward passes, 65.7) matches the three-layer mixed MoA (13 passes, 65.4).
- Applied to the top two leaderboard models, which are both proposer and aggregator and use only four samples because of context limits, it gains 1.8 and 2.6 points (76.7 to 78.5, 72.4 to 75.0). The authors report first place on the leaderboard at submission.
- With three task-specialist 7B models, Self-MoA on each task's best model beat all 13 mixtures on MMLU-redux, CRUX and MATH. Its average is 3.8% above the best mixture, and a task-specific aggregator adds 1 to 2 points.
- Mixing does win in one controlled case, a combined task where each model is best at one subtask. There the best mixtures beat Self-MoA on the best average model by only 0.17 and 0.35 points. Adding a similar-quality Llama-3.1-8B to 30 Qwen samples gave about +2% on MMLU, while adding a model 5% weaker cost over 1.5%.
- Self-MoA-Seq matches or slightly exceeds one-shot Self-MoA from 6 to 30 samples. More samples do not always help, so there is no universal best compute budget.

## Limitations admitted by the authors
- Gains from extra samples plateau or reverse. Samples from one model stop adding diversity, and aggregating many is harder for an LLM, so Self-MoA does not scale indefinitely with compute (Figure 3 shows both rises and drops).
- Self-MoA needs a known top model for the task. In the mixed-task setting, using the best model per task needs the sample's origin, which is prior knowledge. Without it, Self-MoA must use one model, and the margin over mixing shrinks to the 0.17 to 0.35 points above.
- The regression is only moderately strong and is not consistent across datasets. On MATH, weighting strong models more did not raise R2, which the authors attribute to a weak aggregator (a conjecture, not tested).
- They could not reproduce the earlier single-proposer MoA result, and they guess the cause is an unstated proposer choice in the original paper (a conjecture).
- Context limits forced shortcuts. The Gemma 2 aggregator took only four samples, and one math model ran with shorter outputs and three samples.

## Limitations found by others

## What it leaves untried
- It never tests a learned or adaptive choice of when to mix. The one condition where mixing helps (similar quality, complementary strengths) is shown only on constructed tasks, with no router or selector built from it.
- The aggregator is held fixed or chosen by hand. How aggregator strength limits the gain is touched on (MATH) but not studied.
- The quality-diversity trade-off is fitted on small 6-proposer mixtures from three 7B-class models. Whether the coefficients carry to larger models or other tasks is unsupported in the paper.

## Topics
[[Topic - multi-agent debate and consensus]]

---
title: Emergence of Biased Consensus in Multi-Agent LLM Debates
authors: Maya Okawa
date: 2026-08
arxiv: 2608.02827
url: https://arxiv.org/abs/2608.02827
venue: ICML 2026 (PMLR 306)
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2608.02827.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "communication topology and channels"]
---
# Emergence of Biased Consensus in Multi-Agent LLM Debates

## One line
Models a debate among LLM agents as a noisy spin system (Ising/Potts) and shows that a small single-model bias locks the group into a biased consensus once conformity times group size, divided by sampling temperature, passes a critical value.

## Method
Problem: debate is sold as more robust than one model, yet interaction can amplify the biases of the individual models, and the mechanism was not understood.

Idea: borrow the spin model from social-dynamics physics. Each agent holds a discrete choice (binary or q options). At each round it sees the others' previous choices and re-samples its own with probability proportional to exp(-cost/T). The cost has three parts: a conformity term (strength lambda, applied to the neighbours it sees, a fraction rho of the N agents), a task-correct prior, and a local bias term gamma that favours a subset of options (for example US stocks, or one gender). Sampling temperature T plays the role of noise.

Prediction from the mean-field recursion: the group tips into a collective norm roughly when lambda * rho * N / T exceeds 1. For the small groups used in practice (N about 3 to 10) the sharp phase transition is rounded into a smooth crossover, and a sparser graph rounds it further. Mixing agent types (different models, roles or temperatures) averages several response curves, which smooths the transition again and gives partial agreement instead of lock-in.

Practical levers follow from the threshold: raise T, lower lambda (show confidence, avoid sycophantic personas), sparsify who sees whom, or make the population heterogeneous. The model can also be fitted in reverse: lambda and the local bias of each LLM are estimated from the one-step change in the group state during a debate.

## Evaluated on
- Biased consensus appears in realistic tasks and depends on temperature: in an investment-portfolio task (US concentration) and an LLM-as-judge task on MT-Bench (self-preference), low temperature (below about 0.5) gives early biased consensus and lower performance, while higher temperature is more robust. A change of about 0.1 in T can flip the outcome. The paper reports the direction in figures, not the performance numbers in text.
- The predicted crossover is seen in synthetic tasks with no correct answer (choose between two neutral symbols; assign tasks to a female or male name): across GPT-4.1 Nano and Llama 405B, low T turns even weak injected token bias into a near-unanimous norm (|m| near 1), and a simulated N=11 group matches the shape.
- All four tested design knobs reduce lock-in, as the theory says: sparser interaction, higher top-p, showing confidence, and a persona prompt that raises sycophancy changes the norm in the predicted direction (the paper states all four mitigate emergence).
- Heterogeneity helps: three-model mixes (GPT-4.1, Llama 405B, DeepSeek) at T=1.2 reach |m| within [-0.5, 0.2] against [-0.7, 0.5] for single-model groups, and the mix was predicted from parameters fitted on the homogeneous groups only.
- On the real tasks, mixing temperatures (for example 1.4 to 1.6 in the investment task) lowers bias and raises performance against a single temperature; the gains are shown in plots with no numbers in the text.
- The fitted parameters differ by model: GPT variants have negative conformity, DeepSeek the strongest positive conformity, Llama and base Qwen near-zero gender bias with positive conformity.

## Limitations admitted by the authors
- The debate is simplified: short conversational memory, all-to-all or random interaction, no explicit expert roles, and free-text answers collapsed to binary states. Richer context in real debates is not modelled, so the threshold may not carry over.
- Only two synthetic and two realistic tasks are tested; higher-stakes domains (legal, medical, educational) are left to future work.
- Fully predicting and controlling group dynamics in complex real systems remains open.

## Limitations found by others

## What it leaves untried
- Continuous or free-text outputs (the vector-spin extension is mentioned but not run); the claims rest on discrete choices.
- Roles and personas as designed heterogeneity beyond temperature mixing: the real-task fix is only temperature variety, and it is not compared with simply lowering N or adding a judge.
- Whether lock-in is caused by the model's own bias or by the debate protocol's visibility of others' answers is not separated in the real tasks, where the initial bias is not controlled.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - communication topology and channels]]

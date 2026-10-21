---
title: "AgriJev: Efficient Agricultural Candidate Scoring with Multi-Scale Adapted Models"
authors: Xuechen Li
date: 2026-10
arxiv: 2610.19478
url: https://arxiv.org/abs/2610.19478
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/AgriJev - Agricultural Candidate Scoring with Multi-Scale Adapted Models (Li 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# AgriJev: Efficient Agricultural Candidate Scoring with Multi-Scale Adapted Models

## One line
Open, LoRA-adapted Qwen3.5 models (0.8B to 9B) that pick one of several described candidates for agricultural text and knowledge questions. They score all candidates in one forward pass instead of generating an answer, making them an open, domain-specific version of the hosted Jev decision interface.

## Method
- **Problem.** Agricultural decisions (typing an entity mention, checking a type claim, spotting an event, answering a multiple-choice question) all end in choosing one candidate. Generating a text answer for them costs decoding and answer extraction, and the generated code can fall outside the listed options.
- **Interface.** The input is the text, a judgment question and candidates, each with a name and definition. Each candidate gets a local code (A, B, ...), and the prompt ends at a fixed JSON prefix (`{"answer": "`), where every code is a single next token. The model reads the logits of only those code tokens and applies a softmax, giving relative probabilities over the candidates in one forward call. The top code maps back to a stable semantic identifier, so reordering options does not change what a label means.
- **Training.** Cross-entropy over the candidate set only, not the full vocabulary, with candidate order shuffled. Only query/value LoRA weights are updated; backbone and LM head stay frozen.
- **Assumption.** A decision over explicit candidates should come from scoring them, not writing an answer; choosing from the list rules out invalid outputs by construction.
- **What is not new.** The author credits label-conditioned selection to earlier work (TARS, UniMC, Jev). The claimed contribution is the agricultural data preparation, the adapted weights and the cost/accuracy evidence. The paper also says the scores are not calibrated confidence.

## Evaluated on
- **Beats answer generation at 9B, zero-shot.** Mean over 17 external views: 75.44% vs 69.54% for original Qwen3.5-9B and 71.65% after agricultural SFT.
- **The advantage nearly disappears at smaller scales.** Against SFT generation: +0.57 pts at 4B, +0.27 at 2B, -0.07 at 0.8B. The author says these do not establish significance.
- **Invalid outputs explain only part of the gap.** On SeedBench 3-2 the generators produced 113 and 236 invalid codes out of 808. Even counting every invalid answer as correct, they reach only 71.02% and 74.15%, below 75.44%.
- **About half the latency.** Median at 9B: 93.80 ms scoring vs 181.24 ms generating. Generation takes 1.93x to 2.99x as long across scales.
- **Still behind hosted Jev.** Jev 1.13.0 reaches 82.04%; adaptation narrows the gap from 12.49 to 6.60 pts.

## Limitations admitted by the authors
- **The scoring objective is not where the gain comes from.** A control with an ordinary full-vocabulary answer-token loss, scored the same way, beats AgriJev at three of four scales (e.g. 71.70 vs 70.47 at 4B). The advantage comes from scoring instead of generating, not from the candidate-set loss.
- **No calibration.** The probabilities are never checked against how often the model is right, so they cannot serve as confidence.
- **Bigger is not better on every task.** 9B is below 4B on assertion (95.30 vs 95.89), event (81.93 vs 84.15) and CROP (91.10 vs 91.75). SFT generation beats AgriJev on CROP (93.02 vs 91.10).
- **Weak evidence base.** Internal tests reuse source annotations, event labels are silver with no expert adjudication, and the 17 external views are not independent datasets.
- **One seed per condition.** Every gap is a single-run point estimate.
- **Narrow timing.** Latency was measured on 32 inputs, 27 candidates, one A100, batch 1, thinking disabled.
- **Untested settings.** Transfer to unseen labels and free-form agricultural reasoning are not tested.

## Limitations found by others

## What it leaves untried
- **Calibration.** Test whether the probabilities can be trusted (e.g. ECE, or as an abstention threshold). Untested, the scores add nothing beyond the top choice.
- **Robustness to candidate order and wording.** Run paired order-sensitivity tests and deliberately vary label definitions. Reordered CROP is reported only as a marginal accuracy, which does not show whether individual answers stay the same.
- **Generation with thinking enabled.** Compare against a generator allowed to reason. Against short-code generation the latency gain is guaranteed, but the accuracy comparison with a reasoning generator is missing.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]

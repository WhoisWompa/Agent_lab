---
title: "this-that-model-1.0: A typed decision model that decides in 30 ms, for a millionth of a cent"
authors: Zehua Cheng et al.
date: 2026-09
arxiv: 2609.23886
url: https://arxiv.org/abs/2609.23886
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/this-that-model-1.0 - A Typed Decision Model That Decides in 30 ms (Cheng 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "calibration"]
---
# this-that-model-1.0: A typed decision model that decides in 30 ms, for a millionth of a cent

## One line
A 1.88B open typed decision model that reads a calibrated distribution over caller-declared options from one hidden state, generating no tokens, so a program gets a 30.9 ms branch instead of an 8758 ms API call.

## Method
The problem: handing a program branch to an LLM costs a decoding loop, a per-token bill and a parser, and "returned nothing" gets mixed up with "was wrong". A frontier model seemed to score 0.208 on a task it gets right 0.909 of the time, because truncated replies counted as wrong.

The idea:
- **Typed head.** The answer is a softmax over only the declared options' label tokens, so malformed output is impossible and nothing is decoded. No answer is written back into the context, so N questions about one state share one forward pass.
- **Schema-first layout.** Questions and options go before the state, so that prefix is cached once and reused across states, saving (m-1)|P| prefill tokens over m states.
- **Proper-scoring training.** Training mixes cross-entropy and Brier loss, so the only way to lower the loss is to report true beliefs. When supervision is a single sampled outcome, an unbiased U-statistic estimate of expected Brier reward, plus a paired control variate, gives low-variance gradients without bias.
- **One-scalar deployment.** The model ships as base + λ·(fine-tune delta), and λ=0 is the base bit for bit, so rollback is exact.

It assumes the decision is answerable in one forward pass, which the paper shows fails for search.

## Evaluated on
- **Beats hosted Jev on third-party inputs:** 0.941 accuracy and 0.042 Brier vs 0.765 and 0.133, on 68 recorded questions.
- **Calibrated against a computed true distribution:** qL2 0.0248 vs 0.0962 for a constant. It also beats copying ρ from the prompt (0.0250 vs 0.0449 on unseen maps). Accuracy is 0.745 against a 0.746 ceiling (the prose says 0.750, above the ceiling). Every hosted endpoint exposing probabilities is worse than a constant.
- **More tokens do not help:** on the stochastic-actuator family, the systems generating the most tokens are the least accurate.
- **Cost:** the 42-family internal suite takes 32 s and $0.000217, against 155.2 min and $10.636 for the most accurate hosted model.
- **Released benchmark:** 0.844, against 0.897 for gpt-5.6 and 0.803 for Jev. It was trained on these 15 families and the others were not, so this is in-distribution against zero-shot.

## Limitations admitted by the authors
- **Not more accurate than frontier models where it counts.** It scores 0.818 on the branch-shaped families it targets, against 0.837 to 0.968 for hosted models, and 0.560 on multi-step arithmetic against 0.98 to 1.00, because one forward pass cannot carry intermediate results.
- **Cannot search.** The 21% of benchmark questions that need a search over the map average 0.574, while every other family is between 0.77 and 0.998. Where it gets a shortest-path distance band right, it gets the parity of the same distance right only 0.513 of the time, so it recognises the band as a label rather than computing the distance.
- **Targeted training does not transfer.** A second training round improved the 5 families it was written for and none of the other 13. The benchmark jump from 0.409 to 0.839 came from training on its own question shapes.
- **The Jev comparison is small.** The 18-point gap rests on 12 of 68 single-shape questions.
- **The cost comparison flatters it.** Its cost is electricity on an owned GPU, not a price covering serving and margin. The authors put the honest gap to Jev at one order of magnitude.

## Limitations found by others

## What it leaves untried
- **Route around the search failure.** The authors say questions that need a search should be given a search, but never build or measure routing them to a tool or generative model.
- **Test it as a judge on natural decisions.** Almost all evidence is synthetic grid geometry; the motivating cases (refund policy, command safety) are not measured.
- **Evaluate abstention.** A "none of the above" option is trained in but never evaluated, so there is no evidence that thresholding routes uncertain cases correctly.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - calibration]]

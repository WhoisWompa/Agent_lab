---
title: Are More LM Calls All You Need? Towards the Scaling Properties of Compound AI Systems
authors: Lingjiao Chen et al.
date: 2024-03
arxiv: 2403.02419
url: https://arxiv.org/abs/2403.02419
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2403.02419.pdf
folder: ["multiagent_llm_systems"]
topics: ["reasoning prompting", "social choice"]
---
# Are More LM Calls All You Need? Towards the Scaling Properties of Compound AI Systems

## One line
Shows that majority voting over many LM calls (with or without an LM filter) can get worse as calls increase, explains this by the mix of easy and hard queries, and gives a fitted model that predicts the best number of calls.

## Method
The problem: compound systems such as Gemini's 32-sample vote or AlphaCode 2's filter-then-select assume more LM calls means better answers, but nobody had studied how performance scales with the number of calls K. The paper analyses two simple designs on tasks with few possible answers. Vote takes K sampled answers and returns the mode. Filter-Vote first asks an LM to judge each answer correct or wrong, then votes among those kept (falling back to all answers if none survive).

The key idea is per-query difficulty. A query is "easy" if infinitely many calls would give the right answer, which for Vote means the correct answer is the single most likely one in one call, and "hard" otherwise. Voting is a sharpening operation: it pushes easy queries toward 100% and hard queries toward 0%. Accuracy over a dataset is the mix of the two, so when a task holds both kinds, the curve can rise and then fall, or fall and then rise.

For a two-level dataset (a fraction alpha of easy queries with single-call accuracy p1 above one half, the rest with p2 below one half, two answer options), Theorem 2 gives exact conditions. If p1 + p2 > 1 but alpha is below a threshold set by p1 and p2, accuracy rises then falls (inverse U). If p1 + p2 < 1 but alpha is above the threshold, it falls then rises (U). Otherwise it is monotone. Theorem 4 gives a closed-form best K for the inverse-U case, which grows with the easy fraction.

For real tasks the authors propose an approximate scaling model: each query's accuracy follows an exponential in K and sqrt(K), with a rising form for easy queries and a falling form for hard ones. Its parameters are fitted from accuracy at a few small K, and the maximum of the fitted curve gives the optimal number of calls.

## Evaluated on
- Non-monotonic scaling is common: with GPT-3.5, Vote or Filter-Vote accuracy rises then falls with K on MMLU Physics, TruthfulQA, GPQA and AVeriTeC. On MMLU Physics, Vote rises then falls while Filter-Vote falls then rises.
- Difficulty mix explains it: on AVeriTeC, splitting queries by difficulty shows more calls help easy queries and hurt hard ones. Example: an easy claim has a 67% single-call chance of the right answer; a hard one has 34% for the right answer against 56% for a wrong one, so voting converges on the wrong answer.
- Synthetic data confirm the theory: with easy fraction 0.6 and difficulty (0.85, 0.1), accuracy rises monotonically. With fraction 0.4 the same difficulties give a dip then a rise. Difficulty (0.85, 0.4) gives a clear inverse U.
- The optimal K formula, with parameters estimated from 100 sampled points, matched the empirically best K in all 15 synthetic settings (best K ranged from 1 to 30).
- The scaling model, fitted on K = 1 to 5 only, predicted accuracy up to K = 100 with mean squared error between 1e-6 and 1e-4 on synthetic data. On AVeriTeC the fit used 2 to 100 calls, and the paper reports only a "high correlation", with no number.

## Limitations admitted by the authors
- Only two designs (Vote, Filter-Vote) are studied, so other compound systems are not covered.
- Only objective tasks with few possible answers are tested. Subjective tasks such as poems or essays, where majority vote has no meaning, are left open.
- Query difficulty is known only by querying the LM many times. Predicting it without such queries is an open problem.
- Cost and latency of extra calls are not weighed against accuracy.

## Limitations found by others

## What it leaves untried
- Real-data optimal-K prediction is not shown: the exact-match result is on synthetic two-level data, and real tasks get only a visual fit. Whether fitted-from-few-samples K picks the true best on real benchmarks is unreported.
- Only GPT-3.5 is used with temperature 0.1. Whether stronger models, which push most queries to easy, remove the non-monotonicity is not tested (unsupported either way).
- Heterogeneous generators (different models, as in debate or ensembles) are named as covered by the formalism but not studied.

## Topics
[[Topic - reasoning prompting]] · [[Topic - social choice]]

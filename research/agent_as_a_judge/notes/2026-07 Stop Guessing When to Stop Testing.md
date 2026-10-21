---
title: "Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough Data"
authors: Ofir Arviv et al.
date: 2026-07
arxiv: 2607.08522
url: https://arxiv.org/abs/2607.08522
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/stopping rules/Stop Guessing When to Stop Testing - Efficient Model Evaluation with Just Enough Data (Arviv 2026).pdf
folder: ["agent as a judge", "stopping rules"]
topics: ["stopping rules"]
---
# Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough Data

## One line
Replaces fixed-size benchmark runs with group sequential testing, so an evaluation feeds examples in batches and stops as soon as a user-chosen statistical goal (a CI width, a significant gap, a threshold crossed) is met, with error rates still valid despite the repeated looks.

## Method
The problem: a fixed benchmark size suits no single goal. A rough debugging score needs few examples, while separating two close models needs many. Practitioners cut costs by subsampling by hand (e.g. 1K examples) with no guarantee, and stopping when midway results look good ("peeking") inflates false positives.

The idea, borrowed from clinical trials, is group sequential testing. Examples come in batches; after each batch a test statistic (score gap over its pooled standard error) is recomputed on all data so far. The Pocock spending function sets one constant, stricter critical value for every interim look, chosen so the overall Type I error across all looks equals alpha. CIs are widened the same way. Looking often is paid for up front with a higher bar per look, a "modest power reduction" the paper does not quantify.

On top of this sit stopping rules matched to evaluation goals: efficacy (gap significant), equivalence margin (gap confidently inside, e.g., +/-2 points, so the models count as tied), precision (CI narrower than a minimum detectable effect), threshold crossing (a model is confidently below or above a bar), futility (a meaningful gap is unlikely), and diminishing returns (CI shrinkage per batch falls below a set amount). Rules combine. Why savings are large: precision grows as n^-1/2, so most of it comes early, and in a mean-of-means benchmark the small, high-variance datasets cap the achievable CI anyway. Assumptions: independent examples, an approximately normal statistic, and a number of looks fixed in advance.

## Evaluated on
- A rough single-model score is cheap: a +/-3 CI needs about 15% of the samples, +/-2 about 30%, +/-1.5 about half. Going from 55% to 100% of the data narrows the CI only from 2.9 to 2.7 points. A 1K-example heuristic leaves CIs above +/-5.5.
- Pairwise comparison beats a fixed guess: with a fixed 1.2K samples, 55% of 1K model pairs are separated at 95% confidence, vs 76% sequentially. The fixed-size failures are also silent. Pairs more than 2 points apart usually save at least 60% of the cost; pairs under 1.2 points apart usually use the full benchmark.
- Ranking five close top models (gap at most 5 points) with a +/-2 margin uses 60% of the examples, though 2.4 of 20 comparisons per run stay inseparable.
- A one-sided "new model at least 2 points better" deployment check uses 63% of the examples of a fixed run.
- Screening checkpoints (drop below 60 points, else stop at a +/-2 CI) uses 30% of the budget vs 50% without the cutoff; 86 models are dropped early.

## Limitations admitted by the authors
- Assumes i.i.d. examples. Benchmark items are often clustered by dataset or topic, and methods that relax this cost sample efficiency, so the savings could shrink.
- Stopping points depend on observed results, so two runs can stop at different places, which hurts reproducibility unless randomness is controlled.
- The user must choose margins and acceptable gaps, which takes statistical or domain expertise. A badly chosen margin makes the "equivalent" verdict meaningless.
- Multiple-comparison correction for ranking many models was "simplified" away, so the error rates in the ranking results are not controlled family-wide.
- Batch size, initial size and beta were picked as defaults and never tuned or varied; sensitivity of the savings to them is untested.

## Limitations found by others

## What it leaves untried
- The judge's own noise is ignored: scores come from a Llama 3.1 8B LLM judge, and the CI treats those scores as ground truth. A judge that errs systematically would make the method stop early, and confidently, on a biased number.
- Only Pocock is run; O'Brien-Fleming, SPRT and always-valid confidence sequences (which drop the fixed-number-of-looks assumption) are named but not compared, so it is unknown whether the choice of boundary matters for the savings.
- No adaptive choice of which examples to draw next (e.g. oversampling the high-variance small datasets that the paper shows dominate the CI) is combined with the stopping rules.

## Topics
[[Topic - stopping rules]]

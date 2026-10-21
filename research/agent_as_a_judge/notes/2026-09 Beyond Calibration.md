---
title: "Beyond Calibration: Do a Typed-Decision Model's Probabilities Obey the Probability Axioms?"
authors: Keyi Li et al.
date: 2026-09
arxiv: 2609.33209
url: https://arxiv.org/abs/2609.33209
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Beyond Calibration - Do a Typed-Decision Models Probabilities Obey the Probability Axioms (Li 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "calibration"]
---
# Beyond Calibration: Do a Typed-Decision Model's Probabilities Obey the Probability Axioms?

## One line
A label-free battery of logically linked questions shows that Jev's native probabilities follow the probability axioms more closely than an open LLM's, but still break them in specific question forms, mainly by over-endorsing single-label statements.

## Method
The problem: evaluations of typed-decision models such as Jev report accuracy and calibration, but both are averages over many cases. Neither checks whether the probabilities given to logically related questions about the same case fit together. A pipeline that acts on them can still get P("supported") = 0.7 and P("not supported") = 0.6, and its action then depends on how the question was worded.

The idea: fix a state and an explicit partition into three mutually exclusive, exhaustive labels. For each label ask "is it X", "is it not X", "is it one of the other two", and once, "which label applies". Probability theory fixes how these ten answers must relate: negation and disjunctive complements sum to one, the single-label answers sum to one, the two wordings of the complement are equal, monotonicity holds, and yes/no and choice formats agree. No check needs a gold label, and each violation is set against a measured repeat-noise floor, so noise is not counted as incoherence. Because a coherent system must average 1/3 on single-label questions and 2/3 on complement questions whatever the gold label is, the departures by question form show where a system's bias sits, again without labels. The comparison LLM (Qwen3.8-27B) is read out two ways, by first-token probability and by verbalized JSON probability.

## Evaluated on
- Jev violates negation complementarity least: mean |s+n-1| of 0.064, against 0.293 for Qwen's first-token readout (4.6x) and 0.122 for its verbalized readout.
- The gap is not a confidence artifact: on confidence-matched pairs, Jev is at 0.028 and Qwen at 0.257, the same -0.229 gap. With the double-negation labels removed it widens to 0.057 vs 0.385.
- Jev is still incoherent: its violation is about five times its noise floor of 0.013. Its three single-label probabilities sum to 1.14 on average, above one on 159 of 160 items, because it gives a statement that is true one time in three an average of 0.380.
- Mixing formats is unsafe: yes/no and choice probabilities for the same label differ by 0.09 for Jev, and by 0.096 even after rescaling, so the two formats carry different information.
- The failure modes differ: Qwen's first-token readout answers "no" to both a statement and its negation in 196 of 480 pairs, and its violations do not shrink with confidence. Jev's violations fall from 0.142 on uncertain pairs to 0.018 on confident ones.

## Limitations admitted by the authors
- The study is small: 160 items, two English domains, three-label partitions only.
- There is no paraphrase control. The two wordings of the complement differ by 0.060 for Jev, about as much as its negation violation, so part of what is measured may be sensitivity to wording rather than to logic.
- There is one comparison LLM, run with thinking disabled. GPT-5's near-perfect binary complementarity suggests larger or reasoning models may close the gap, so the ordering applies to this model only.
- Only one Jev version was tested, through one gateway. The closed service can change.
- The datasets are public, so memorization cannot be ruled out, although the 19 Jevals-suite items behaved like the rest (-0.218 vs -0.241).
- Coherence is necessary but not sufficient. A system answering 1/3 and 2/3 to every question passes every check and says nothing about the item. Only the 63.8% top-label accuracy shows Jev was informative.

## Limitations found by others

## What it leaves untried
- Repairing the incoherence, not only measuring it. For example, project the yes/no answers onto the nearest coherent distribution, or use the choice question only, then test whether downstream threshold decisions improve. The paper advises against mixing formats but never measures what mixing costs.
- Partitions with more than three labels, and judge-style tasks. The single-label excess grows with each label (0.14 over three), so judging with many rubric levels is where the overcount would matter most, and it is untested.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]]

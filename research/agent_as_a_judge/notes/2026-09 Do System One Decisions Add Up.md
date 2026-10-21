---
title: "Do System One Decisions Add Up? A Study of Probabilistic Coherence"
authors: Saman Sarker Joy
date: 2026-09
arxiv: 2609.33971
url: https://arxiv.org/abs/2609.33971
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Do System One Decisions Add Up - A Study of Probabilistic Coherence (Joy 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "calibration"]
---
# Do System One Decisions Add Up? A Study of Probabilistic Coherence

## One line
Tests whether the probabilities that decision models (Jev and Laya) give for a broad category, a fine label, and a fine label within an assumed category are consistent with each other, and finds they are not: splitting a decision into stages moves accuracy by about 20 points, up for one model and down for the other.

## Method
The problem: a decision interface returns a choice and a probability for every option, and applications combine those numbers (route a case, escalate, multiply stage confidences). Each distribution sums to one, but nothing guarantees that separately asked questions agree with each other. A model can be accurate and calibrated on each question alone and still be incoherent across them.

The idea is to apply two identities from probability theory to a two-level label hierarchy. (1) A parent's probability should equal the sum of its children's direct probabilities (u = a). (2) A child's direct probability should equal parent probability times conditional child probability (p = q). To check these, the paper asks three kinds of question per input: pick the broad category, pick among all fine labels, and, for **every** parent, pick a fine label assuming that parent. Asking every branch, not just the predicted one, rebuilds a full unconditional distribution q over all fine labels, so it can be compared to the direct one.

This gives three decision rules: flat (argmax of p), hard routing (best parent, then best child, so a wrong parent locks out the right answer), and full marginalization (argmax of q, keeping every branch). Disagreement is measured as parent-level total variation (TV, 0 = agreement, 1 = maximal) and flat-vs-reconstructed Jensen-Shannon divergence. Parent TV is a lower bound on fine-label TV, so a parent mismatch proves at least that much fine-level disagreement. The paper is careful that this measures compatibility of outputs under different question wordings, not the model's "beliefs": assuming a parent changes the instructions and the candidate set at the same time.

## Evaluated on
- Both models are substantially incoherent: mean parent TV is 0.219 to 0.349 for Jev and 0.424 to 0.689 for Laya, on TREC, CLINC150 and MASSIVE. Even at Jev's 91.0% flat accuracy on CLINC150, parent TV is 0.349.
- Decomposition helps one model and hurts the other, every time: marginalization lowers Jev's accuracy by 11.8 to 22.9 points (91.0% to 68.1% on CLINC150) and raises Laya's by 5.6 to 21.3 points (23.1% to 44.4% on CLINC150). All six intervals exclude zero.
- Marginalization beats hard routing in all six model-dataset pairs, but by anywhere from 10.5 points (Laya, CLINC150) down to 0.1 (Laya, MASSIVE). Hard routing fails mostly at the parent step: Jev on CLINC150 makes 317 wrong-parent errors against 37 wrong-child errors, though it is 94.6% accurate within a correct parent.
- Accuracy and calibration can move apart: on MASSIVE, Laya gains 9.2 accuracy points while ECE rises from 0.046 to 0.124.
- Option order matters a lot for Laya: reordering the same choices flips its flat label in 61.7% to 76.7% of comparisons, against 5.8% to 20.0% for Jev.

## Limitations admitted by the authors
- Instructions, candidate set size, order and Laya's option-count calibration all change together between question types, so the paper cannot say whether hierarchy itself causes the incoherence. For example, Laya's temperature switches from about 1.0 to a clamped 0.5 at 11 or more choices, which alone could reshape flat versus conditional distributions.
- Only two systems, and they differ in architecture, scale, precision and training data, so the opposite directions cannot be attributed to any one factor. Laya also ran with an enlarged token budget (1,088/960 vs default 512/192) and outside its model card's comfort zone for many choices.
- Label wording is a confound: TREC fine labels keep cryptic suffixes such as "Entity: cremat", and Laya confuses DESC:def with DESC:desc 94 times under marginalization. No wording ablation was run to test whether clearer labels would fix this.
- The robustness audits are small: order effects come from 30 distinct examples per dataset reused across 4 permutations, and repeated-request stability is tested only for Jev.
- Scope narrowed after pilot and partial results, and intervals are not adjusted for multiple comparisons, so the findings are descriptive.

## Limitations found by others

## What it leaves untried
- A factorial ablation that changes parent wording, option order and calibration one at a time. The authors name it as future work. Without it, a practitioner cannot tell which knob to turn to make a staged judge coherent.
- Forcing coherence by building parent probabilities from summed flat probabilities, then comparing that against independently asked parents. This would show whether incoherence costs accuracy or just reflects a different but valid reading.
- Latency and cost were not measured, even though marginalization needs K+2 calls per input against 1 for flat. That trade-off decides whether the accuracy gain for weak models like Laya is worth paying for.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - calibration]]

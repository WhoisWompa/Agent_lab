---
title: "Type-Safe Is Not Error-Free: Typed Decision Models Follow the Option Name, Not the Definition Bound to It"
authors: Yu Sun et al.
date: 2026-09
arxiv: 2609.26758
url: https://arxiv.org/abs/2609.26758
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Type-Safe Is Not Error-Free - TDMs Follow the Option Name, Not the Definition (Sun 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "presentation sensitivity"]
---
# Type-Safe Is Not Error-Free: Typed Decision Models Follow the Option Name, Not the Definition Bound to It

## One line
Shows that typed decision models (Jev and two open-weight copies, Laya and Open-Jev) choose options by the conventional meaning of their names, such as yes/no, rather than by the explicit definitions bound to them, while still reporting a 0% type-error rate.

## Method
The problem: typed decision models return a softmax over a declared option set, so they can never answer outside it. Jev's makers present the resulting 0% type-error rate as a reliability guarantee. The authors argue it only follows from how the output is built. It limits where probability can go, not how it is split among options, and it holds just as well when the decision is inverted.

Each option is a name plus a definition (e.g. "no" = "No human attention is warranted"). Normally the two agree, so accuracy cannot show which one the model follows. The idea is a **reassignment test**: keep everything fixed and only swap which definition each name is bound to, stated explicitly in the input. A model that reads definitions keeps its choice of definition and returns the other name. A model that reads names keeps the name and so inverts its decision. The measure is the **flip rate** at the level of the chosen definition. It needs no gold labels and is reported against neutral names (0/1, A/B), where the swap only reorders definitions, isolating the names' effect from the operation itself. Random five-character strings test whether any name content matters or only polarity does. AUC separates a lost ranking from a shifted threshold.

One offered explanation for model differences: Laya scores a marker token at the short name, while Open-Jev averages over all tokens, diluting the name with the longer definition.

## Evaluated on
- **Polar names override definitions:** on Laya, yes/no reassignment flips 76.9% of decisions against 6.5% for 0/1 (+70.4 pp, CI [67.6, 73.1]). Every polar pair is at least +39.3 pp above the control. Balanced accuracy falls from 87.2% to 28.4%.
- **The ranking is reversed, not just blurred:** yes/no AUC falls from 93.8% to 23.2%, below chance, so no threshold adjustment can fix it.
- **Polarity is the cause, not the words as such:** polarity adds +41.0 pp in flip rate over neutral names, and names seen in training add another +16.0 pp. Random strings flip within 3.2 pp of neutral names on all three models, at accuracy within 3.3 pp.
- **Holds beyond Laya:** on Jev, yes/no flips 32.5% (+30.4 pp over 0/1), 24 times its test-retest floor of 1.33%, and AUC falls from 81.5% to 58.1%. On Open-Jev the gap is +15.9 pp.
- **Holds beyond binary choices:** with 3 to 16 options, even renaming options to neutral letters changes 52.4% of Laya's decisions. Shifting the original names one step changes 79.7% and drops accuracy from 56.4% to 15.5%.

## Limitations admitted by the authors
- Only two open-weight architectures, English only. So the scoring-geometry explanation for why Laya is 4.1 times as sensitive as Open-Jev is untested.
- Open-Jev is weak before any swap (balanced accuracy 59.8% to 63.9%, against 79.4% to 89.6% for Laya). Its lower flip rate may just reflect a fixed preference for one definition, not robustness.
- Jev is a closed API seen at one point in time and is not deterministic. The served model may change.
- Name pairs differ in how well they keep their meaning: per-task flip rates for the middle pairs range from 12.3% to 92.0%. Without human annotation of meaning preservation, the ranking between polar pairs is loose.
- With multiple options, baseline accuracy is only 56.4%, so that result is directional only.
- Both proposed mitigations (neutral names, training with randomized names) are suggested but not evaluated.

## Limitations found by others

## What it leaves untried
- Training with randomized option names and measuring whether the flip rate drops to the neutral-name floor. The authors call it cheap for a model of Laya's size, and it is the direct fix for the failure they show.
- Combining name reassignment with option-order shuffling, which an outside harness says also flips 43.3% of Laya's decisions, to see whether the two biases add up in a judge pipeline.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - presentation sensitivity]]

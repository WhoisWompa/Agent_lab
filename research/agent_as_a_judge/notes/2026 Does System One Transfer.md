---
title: "Does System One Transfer? Calibrated Typed-Decision Models, Label Budgets, and Translation for Indonesian Regional Languages"
authors: Romi Fadli et al.
date: 2026
arxiv: none
url: https://github.com/tnromy/evaluating-system-one-models-for-indonesian-regional-languages
venue: unknown (preprint; no venue stated)
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/decision models/open models/papers/Does System One Transfer - Calibrated Typed-Decision Models, Label Budgets, Indonesian Languages (Fadli 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "calibration", "confidence-gated escalation", "judge and decision-model audits"]
---
# Does System One Transfer? Calibrated Typed-Decision Models, Label Budgets, and Translation for Indonesian Regional Languages

## One line
A pre-registered test of whether the typed-decision model Jev (label plus probability in one forward pass) stays accurate and calibrated on Indonesian regional languages, how many labels a local classifier needs to match it, and whether routing its least confident decisions to a fallback pays off.

## Method
The problem: "System One" decision models are pitched as the cheap, always-well-formed first layer of a classification pipeline, provided their probability can be trusted, but nearly all evaluation is English and the vendor itself says the model is English-tuned. When a team should instead label data and train a small model was unmeasured.

The idea is to use parallel test sets, where every sentence exists in a regional language and in Indonesian, so the same content can be compared across languages. This allows: (1) a sentence-level resource gradient, testing whether the chance of a correct answer rises with the lexical overlap between a sentence and its Indonesian version; (2) a "perfect translation" upper bound, by giving Jev the human Indonesian sentence instead; (3) separating calibration (do stated probabilities match accuracy on average) from discrimination (does confidence rank errors below correct answers, measured by area under the risk-coverage curve). On top of that sit paired learning curves of retrained classifiers, giving the label budget at which a local model matches zero-shot Jev, and a confidence-gated cascade: Jev answers everything, and its least confident share r, fixed on validation data, is re-answered by a local IndoBERT or an LLM. The cascade should help because the two models err on different items.

## Evaluated on
- Zero-shot Jev matches fine-tuned encoders on NusaX sentiment: macro-F1 0.782 vs 0.783-0.792, and DeepSeek 0.786, at USD 0.015-0.019 per 1,000 decisions.
- Accuracy follows closeness to Indonesian: log-odds of a correct answer rise 0.14-0.42 per standard deviation of overlap, all intervals above zero; the human Indonesian sentence adds up to 37.2 points (Buginese), most in distant languages.
- Calibration holds but error ranking does not: ECE is lower on regional languages than on Indonesian (-0.036 NusaX, -0.020 NT-senti), contrary to the authors' prediction, while AURC is worse in all three datasets (+0.039 to +0.090).
- A logistic-regression baseline with 500 labels per language still falls short of Jev in 9 of 10 NusaX regional languages.
- Cascades: 8 of 9 match or beat the better component; routing 30% of emotion decisions to IndoBERT lifts macro-F1 from 0.629/0.647 to 0.676; routing to DeepSeek matches DeepSeek at 24-77% lower API cost.
- Frontier LLMs are 4.2-13.6 accuracy points better (Opus 5.5: 0.890 vs 0.783 on NusaX), but Sonnet and Opus cost 347-618 times as much per decision.

## Limitations admitted by the authors
- Regional sentences are translations of Indonesian originals, so they may sit closer to Indonesian than natural regional writing; the overlap and transfer results may be optimistic for real text.
- NusaX has been public since 2022 and may be in closed models' training data; Jev cannot be probed for memorisation because it generates no text.
- The label-budget hypothesis (budget smaller where Jev is weaker) went unconfirmed (Spearman 0.52, p = 0.061) because nine of ten budgets tie at "more than 500", so the test has little power.
- Cascade test curves peak at larger shares (30-45%) than those picked on validation; one cascade (NT-senti to fine-tuned Laya) lost 2.1 points because the validation pilot chose too small a share.
- The cascade calls Jev on every item, so it buys accuracy, not savings, for a team that already has a local model.

## Limitations found by others

## What it leaves untried
- Per-language recalibration of the confidence threshold with a few labels: calibration holds but AURC degrades, so a threshold tuned on Indonesian removes fewer errors on regional text, and the paper names this fix without testing it.
- A cascade from Jev to a frontier LLM: the frontier models are 4-14 points better and their verbalised confidence ranks errors well (AURC 0.021-0.033 vs 0.066), yet only the DeepSeek cascade was run.

## Topics
[[Topic - decision models]] · [[Topic - calibration]] · [[Topic - confidence-gated escalation]] · [[Topic - judge and decision-model audits]]

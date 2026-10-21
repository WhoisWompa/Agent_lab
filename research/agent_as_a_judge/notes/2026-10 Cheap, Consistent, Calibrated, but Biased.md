---
title: "Cheap, Consistent, Calibrated, but Biased? Typed Decision Models as Judges"
authors: Fabian Lukassen et al.
date: 2026-10
arxiv: 2610.18122
url: https://arxiv.org/abs/2610.18122
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/evaluations/Cheap, Consistent, Calibrated, but Biased - Typed Decision Models as Judges (Lukassen 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "presentation sensitivity"]
---
# Cheap, Consistent, Calibrated, but Biased? Typed Decision Models as Judges

## One line
Audits eight typed decision models (TDMs) against the CALM catalogue of LLM-judge biases, finding each biased in 3 to 8 of 12 tests, though they are 37 times cheaper and more consistent than 2026 LLM judges.

## Method
TDMs (Jev, Perplexity Decider, Clef and others) are LLMs whose text output is replaced by a decision head: given a question with fixed options, they return one probability per option in a single pass. They are pitched as cheap, calibrated judges, but as fine-tuned LLMs they may inherit LLM-judge biases.

Pairwise prompts with a known better answer each get one irrelevant cue (swapped order, fake citation, "90% of people prefer B", a famous model name, an emotional tone, padding, an identity note). Two choices carry the argument:
- **Excess over self-noise.** Bias = flips caused by the cue minus flips caused by simply resending the prompt. A noisy judge does not look biased, and a deterministic one does not look robust just because it never flips by chance. A judge counts as biased only if it wrongly flips at least 5 of 100 prompts beyond chance (lower end of the 95% interval).
- **Cues on either answer.** A judge that punishes a cue looks robust, even more accurate, when the cue sits on the worse answer, as it mostly does in CALM. Cues are also placed on the better answer.

Because TDMs output probabilities, the paper can also see shifts that do not flip the verdict and whether confidence predicts flips.

## Evaluated on
- **Every TDM is biased, and the test matters more than the model.** The test explains 25% of variance in probability shift, the model 1.4%.
- **Tone is the worst cue.** An emotional tone on the better answer drops median TDM accuracy from 0.99 to 0.42; a fake citation there, from 0.66 to 0.41.
- **TDMs are more biased than 2026 LLM judges.** All eight show position bias (excess 8 to 24 per 100) where no 2026 LLM judge exceeds 6. Bandwagon biases five TDMs, none of the 2026 LLM judges. Perplexity Decider and Clef flip 26 and 27 per 100 under bandwagon against 6 for Qwen3.8-27B, their base LLM, so decision fine-tuning itself adds bias.
- **Both kinds fail on the same prompts.** Per-prompt flip effects correlate at 0.95.
- **Confidence flags most flips, not all.** 30% of verdicts below 0.6 confidence flip versus 3% above 0.9. But tone and citation cues on the better answer flip about half and 14% of verdicts above 0.9.
- **The practical case.** Six TDMs repeat over 99.7% of verdicts (2026 LLM judges: 91 to 98%), at 1/37 the cost and six times the speed.

## Limitations admitted by the authors
- Only pairwise comparisons with a reference answer. Reference-free judgments (e.g. helpfulness to a lay reader) may lean more on tone, so results may not carry over.
- Rewrites come from GPT-4-Turbo, unverified by humans. An emotional rewrite also changes clarity, the very thing separating better from worse answers, so part of the sentiment bias may be a real quality change; under sentiment the prompt explains 90% of LLM-judge flip variation.
- Citations are fake, some implausible, so punishing them may be sound judgment; real citations were not tested.
- The design shows verdicts change, not why: it cannot say whether fine-tuning, the typed request or the missing explanation restores position bias, and with no public training data, model differences cannot be attributed.
- Calibration (ECE 0.07 to 0.25) does not go with less bias, and a 0.8 means different things across TDMs, so thresholds do not transfer.

## Limitations found by others

## What it leaves untried
- Rerunning the full bias battery with the both-orders fix. It removes position bias by construction but was only checked on accuracy (−0.2 to +3.8 points).
- Human-verified, clarity-controlled rewrites and real citations, to tell whether the two cues that beat confidence are biases or data artefacts.
- Controlled base-LLM versus TDM fine-tuning runs, since the bandwagon jump from 6 to 26 points at decision training as the cause.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - presentation sensitivity]]

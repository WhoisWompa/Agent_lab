---
title: Constitutional AI: Harmlessness from AI Feedback
authors: Yuntao Bai et al.
date: 2022-12
arxiv: 2212.08073
url: https://arxiv.org/abs/2212.08073
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2212.08073.pdf
folder: ["multiagent_llm_systems"]
topics: ["judges as reward signals", "LLM and agent judges", "trained judges and reward models"]
---
# Constitutional AI: Harmlessness from AI Feedback

## One line
Trains a harmless but non-evasive assistant with no human harmlessness labels, using a short list of written principles that a model applies to critique its own answers and to judge answer pairs, then distilling those judgments into a reward for RL.

## Method
The problem: human-feedback training for harmlessness needs tens of thousands of labels, the labels are opaque, and crowdworkers reward evasion ("I can't answer that"), so helpfulness and harmlessness trade off. The idea is to replace the human harmlessness labels with a constitution of about 16 natural-language principles, plus a few few-shot examples, and let a model do the supervising.

Stage 1 (supervised): a helpful-only RLHF model answers red-team prompts, usually harmfully. It is asked to critique its answer against a randomly drawn principle, then to rewrite it. This can repeat (up to four rounds). A pretrained model is finetuned on the final revisions, mixed with helpfulness samples. The purpose is to move the policy onto a less harmful distribution before RL, which cuts the exploration RL needs.

Stage 2 (RL from AI feedback): the stage-1 model produces two answers per prompt. A feedback model reads them as a multiple-choice question under a sampled principle, and its normalised log-probabilities for (A) and (B) become soft preference labels. These AI harmlessness labels are mixed with human helpfulness labels to train one preference model, which is the RL reward. Why it should work: models' multiple-choice probabilities are reasonably calibrated, and a principle sampled per label (ensembling) makes the preference model more robust. With chain-of-thought feedback the model commits to one answer, so labels sit near 0 or 1; clamping them to 40-60 percent fixed this, since unclamped, the policy learned to produce more extreme responses.

## Evaluated on
- Models can judge harm: on 438 helpful, honest, harmless comparisons, chain-of-thought plus larger scale approaches preference models trained on human labels; the trend suggests models above 52B will match them (Figure 4, no exact figure given in the text).
- RL-CAI is more harmless than helpful RLHF, HH RLHF and SL-CAI at 52B, by crowdworker Elo, and sits on a better helpfulness/harmlessness frontier than human-feedback HH models (Figure 2). Crowdworkers were told to prefer non-evasive answers when two were equally harmless, which narrows the gap between the human-feedback models.
- Non-evasive: RL-CAI is "virtually never evasive" and explains its objections. This is shown by samples, not by a measured rate.
- Revisions help: harmlessness PM score rises with each revision, while pure helpfulness score falls (Figure 5).
- Critiques matter little at scale: critiqued and direct revisions score about the same for large models; critiques only clearly help small ones (Figure 7).
- Soft labels beat hard 0/1 labels for non-CoT RL-CAI. Absolute harmfulness scores fall during training for HH RLHF and RL-CAI and rise for helpful RLHF (Figure 10).

## Limitations admitted by the authors
- Over-training causes Goodharting: RL-CAI becomes overly harsh or adds boilerplate such as "you are valid, valued, and cared for" to most red-team answers. Principle rewording and ensembling only qualitatively reduced this.
- The generated critiques are often inaccurate or overstated at 52B; the benefit comes from revision, so the transparency the critique is meant to give is partly illusory.
- Preference-model scores become less calibrated at high values, so the monotone gains over revisions "should be taken with a grain of salt". The 0-4 absolute harmfulness scores may be miscalibrated across workers too.
- The 16 principles were chosen ad hoc for research. More principles did not raise PM scores (Figure 6); the claimed diversity benefit for RL exploration was not measured.
- Human supervision remains for helpfulness labels, and the helpfulness-only starting model is itself RLHF-trained.
- Harmlessness Elo is sensitive to the crowdworker instruction change (non-evasive preferred) and to a switch of vendor, which the authors say explains the smaller gap to earlier work, so comparison with prior numbers is loose.
- Dual use: the method lowers the cost of training models to any intended behaviour, and fewer human reviews could let under-tested models ship.

## Limitations found by others

## What it leaves untried
- Getting helpfulness without human labels, starting from a pretrained model with prompting; the paper only removes harmlessness labels.
- Iterated online training, refreshing the preference model with new AI labels as the policy drifts; the preference model here is trained once.
- Principles from a wider set of stakeholders, and testing robustness to attack with automated red teaming; both are named as future work with no evidence yet.

## Topics
[[Topic - judges as reward signals]] · [[Topic - LLM and agent judges]] · [[Topic - trained judges and reward models]]

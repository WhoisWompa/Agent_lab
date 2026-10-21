---
title: Automatically Correcting Large Language Models: Surveying the landscape of diverse self-correction strategies
authors: Liangming Pan et al.
date: 2023-08
arxiv: 2308.03188
url: https://arxiv.org/abs/2308.03188
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2308.03188.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "judges as reward signals"]
---
# Automatically Correcting Large Language Models: Surveying the landscape of diverse self-correction strategies

## One line
A survey that sorts methods for fixing LLM output with automated feedback into a three-party framework (model, critic, refiner) and into training-time, generation-time and post-hoc correction.

## Method
This is a literature review, so the contribution is the taxonomy, not a new system. The problem: LLMs hallucinate, reason unfaithfully, emit toxic content and write flawed code. Human feedback (RLHF) fixes these but is costly and cannot be given in real time. The survey covers the alternative, feedback produced automatically.

The framework borrows a medical analogy. A language model (patient) produces output. A critic model (doctor) turns input and output into feedback, either a scalar or natural language. A refine model (treatment) repairs the output, or the model itself through fine-tuning or RL. Every surveyed work is placed along five axes: what is corrected (hallucination, unfaithful reasoning, toxic content, flawed code), the feedback source (the model itself, or external trained models, tools, knowledge, metrics), the feedback format (scalar or language), when it is used, and how the model is corrected.

The "when" axis is the main organiser:
- **Training-time**: feedback changes weights. Human feedback is used directly or through a reward model (RLHF). Automated variants are external-metric optimisation and self-training, where the model's own filtered or self-critiqued outputs become training data (STaR, RLAIF, ReST).
- **Generation-time**: feedback steers decoding with no weight change. Generate-then-rank samples many candidates and a critic picks one. Feedback-guided decoding scores each reasoning step and searches (beam search, tree search, MCTS).
- **Post-hoc**: feedback arrives after the full output. Variants are self-correction (the same LLM critiques and revises, as in Self-Refine and Reflexion), external feedback from code interpreters, symbolic solvers, retrieval or trained critics, and multi-agent debate.

The survey says generation-time scoring needs accurate intermediate feedback, which holistic tasks like summarisation lack. That is why it argues post-hoc correction fits those tasks and gives richer natural-language feedback.

## Evaluated on
No experiments of its own. The claims it carries from the literature:
- Self-correction needs a strong model. Self-Refine's authors report that smaller open models struggle to refine even with correct feedback.
- Self-repair of code is bottlenecked by the feedback stage. Olausson et al. found real gains only when feedback came from expert humans or GPT-4.
- Debate beats plain self-correction on reasoning: Du et al. report better results than self-correction, but the survey gives no figure.
- Arithmetic reasoning is the most studied area, because intermediate steps are easy to verify. Inductive and abductive reasoning are barely covered.

## Limitations admitted by the authors
- No theory explains why self-correction works. The survey links it to calibration and metacognition (pre-trained models are well calibrated on self-evaluation questions; RLHF-tuned ones need temperature adjustment) but offers nothing firmer.
- No unified metric or benchmark compares strategies on effectiveness, cost or upper bound. Existing evidence is empirical and application by application.
- Training-time correction is unusable for closed-source or huge models, and needs feedback that can be optimised (a number).
- Scalar feedback is "less informative" for correction than language feedback.
- Optimising an external metric can exploit that metric's weaknesses, as cited for BLEURT.
- Almost all work is text-only. Multimodal self-correction is "yet to be broadly adopted".
- Stability under continual self-improvement is unknown, including whether fixing one behaviour undoes an earlier fix (catastrophic forgetting). Model editing is proposed as a route but currently generalises poorly and has side effects.

## Limitations found by others

## What it leaves untried
- A head-to-head comparison of the strategies under one setup. The survey says it is missing and offers only a table of features.
- Analysis of when a loop hurts. It stresses feedback quality as the bottleneck but gives no failure rates or stopping criteria for iterative revision.
- Scope is stated as automated feedback only. Human-feedback methods are touched "for completeness", so the cost trade-off between the two is not quantified.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - judges as reward signals]]

---
title: Can Large Language Models Really Improve by Self-critiquing Their Own Plans?
authors: Karthik Valmeekam et al.
date: 2023-10
arxiv: 2310.08118
url: https://arxiv.org/abs/2310.08118
venue: arXiv (preprint, under review)
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2310.08118.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "judge and decision-model audits"]
---
# Can Large Language Models Really Improve by Self-critiquing Their Own Plans?

## One line
Tests whether GPT-4 can verify its own plans in a generate-and-critique loop on Blocksworld planning, and finds its verifier accepts most invalid plans, so the loop gains little over a sound external checker.

## Method
The problem: papers such as Reflexion and Self-Refine claim that an LLM can critique its own candidate solutions and improve by iterating. The authors doubt this for reasoning tasks. Their argument is that verification being easier than generation is a classical-complexity idea, and it should not carry over to LLMs that do approximate retrieval.

The test is a controlled swap of the verifier. An LLM+LLM system has one GPT-4 generating a plan and another GPT-4 call judging it and writing free-form feedback. The loop stops when the verifier approves or after 15 iterations. This is compared with the same backprompting loop where the verifier is VAL, a sound external plan validator, and with a single-shot generator. VAL also gives ground truth for every plan, so the LLM verifier's accuracy can be measured directly. A second experiment varies feedback detail (none, binary, first error, all unmet preconditions) with VAL as the verifier, to separate "the verdict is wrong" from "the feedback is uninformative".

## Evaluated on
Blocksworld, 100 random instances, GPT-4 at temperature 0.
- Self-critique helps a little, far less than a sound verifier: 55% for LLM+LLM, 40% for single-shot, 88% for LLM+VAL.
- Part of the 15-point gain over single-shot may come from simply getting more attempts (3.48 iterations on average) and not from the verifier's judgment. The paper does not separate the two.
- The verifier is accurate on only 61 of 100 final plans. It approves nearly every valid plan (54/55) but also approves 38 of 45 invalid ones, a false-positive rate of 84.45%. It has almost no discriminating power, and the loop stops early on wrong plans.
- Feedback detail is claimed to matter little. With VAL, binary-only feedback reaches 74% (37/50), and first-error or all-errors feedback reaches 86% (43/50) each. The authors conclude the bottleneck is the binary verdict and not the feedback's richness.

## Limitations admitted by the authors
- One domain (Blocksworld, described as simple), one model (GPT-4) and 100 instances. The conclusion about LLM self-critique in planning rests on this narrow base, and the authors call the evidence "preliminary".
- No chain-of-thought or other prompting variants were tried for the verifier, so the poor verification may reflect the zero-shot prompt and not a limit of the model. The authors list this as future work.

## Limitations found by others

## What it leaves untried
- Other verifier set-ups: a different model as critic, or a debate or cross-examination setup, which the related work names but the paper does not test. Whether the false-positive problem comes from sharing one model for both roles is therefore unknown.
- Separating the retry effect from the critique effect, for example with a matched number of unfiltered resamples. Without it, the 55% vs 40% gap cannot be credited to the LLM verifier.
- Reconciling the feedback claim with its own numbers. Binary-only (74%) is 12 points below detailed feedback (86%) on 50 instances, and no significance test backs the "minimal impact" statement. The feedback experiment also used VAL as verifier, so it says nothing about LLM-written feedback.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - judge and decision-model audits]]

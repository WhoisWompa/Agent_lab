---
title: GPT-4 Doesn't Know It's Wrong: An Analysis of Iterative Prompting for Reasoning Problems
authors: Kaya Stechly et al.
date: 2023-10
arxiv: 2310.12397
url: https://arxiv.org/abs/2310.12397
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2310.12397.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "judge and decision-model audits"]
---
# GPT-4 Doesn't Know It's Wrong: An Analysis of Iterative Prompting for Reasoning Problems

## One line
On graph coloring, GPT-4 self-critique loops do worse than a single answer, and the gains seen with an external verifier come from extra tries, not from the content of the feedback.

## Method
The paper attacks a common belief: that an LLM can critique and refine its own answer. That belief rests on the assumption that verifying is easier than generating. The authors argue this should not hold for an LLM that is doing approximate retrieval.

They test it on graph coloring, an NP-complete problem whose answers a program can check exactly. A generator and a verifier are placed in a loop, with up to 15 back-prompts. Five feedback regimes are compared:
- No feedback (the single-answer baseline).
- Pass/fail only ("try again").
- The first violated edge.
- All violated edges.
- GPT-4's own critique, passed back whether or not it is correct.

The verifier is either GPT-4 itself or a sound program.

Two controls separate what the feedback says from the number of attempts:
- **Sampling control.** Sample several independent answers with no feedback and let the sound verifier pick any correct one. If this matches the loop, the loop's feedback adds nothing.
- **"Evil" feedback.** Claim that a randomly chosen correct edge is wrong, to see whether the model checks the criticism or just obeys it.

A separate verification test gives GPT-4 five kinds of colorings, some correct and some not, and asks it to find the errors.

## Evaluated on
- **Self-critique is worse than not iterating.** The baseline solves 16% of 100 instances. With GPT-4 as its own verifier, 1 of 100 is correct.
- **The self-verifier cannot recognise success.** In 40 instances the generator produced an optimal coloring at some point in the chain. The verifier never accepted it. In 39 of those it invented a violated edge. Only 4 of 100 chains were stopped by the LLM verifier, and none of the 4 was correct.
- **Verification is weak even on static inputs.** Of 118 correct colorings, GPT-4 marked 30 of the 500 colorings correct, and only 5 of those 30 were actually right. It accepted 2 of 100 optimal colorings. Most "incorrect" verdicts cite edges that do not exist. When it names a real error, it usually names a single edge.
- **A sound verifier helps modestly, but the feedback content does not matter.** Accuracy rises from about 16% to nearly 40%. Pass/fail, first-error and all-errors feedback are statistically insignificant differences.
- **Extra tries explain the gain.** Fifteen independent samples at temperature 1, checked by the sound verifier, also reach about 40%. Five samples come close. The authors' phrase is that blindfolded guessing does as well as careful feedback.
- **The model obeys feedback without judging it.** Pointed-out edges get fixed 94% (first error) to 98% (full list, any edge) of the time. False "evil" claims are also fixed 94% of the time, so local fixes are applied whether or not they help the whole coloring.

## Limitations admitted by the authors
- Everything is one domain (graph coloring), one model (GPT-4) and 100 small instances (10 to 17 nodes, about 24 edges). The paper's wider claims about iterative prompting therefore rest on this one case. The authors chose the size range because performance there was volatile.
- It is unclear why self-critique collapses to 1 of 100. Bad feedback may be damaging good answers, or correct answers may simply come early in the chain and be overwritten. The authors call their results "conflicting" on this point.
- Unsupported in the paper: the explanation that LLMs are doing "approximate retrieval" is a stated suspicion, not something the experiments test directly.

## Limitations found by others

## What it leaves untried
- Other reasoning domains, and other models. This matters because the authors cite prior positive self-critique results (Reflexion, Self-Refine) that were not re-run on their original tasks.
- Feedback in a domain where a partial fix can be judged locally. Graph coloring errors are edge-level and interact, so the finding that feedback content is irrelevant may not carry over.
- A cost comparison between the loop and equal-budget sampling. The paper shows they tie on accuracy but does not compare tokens spent.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - judge and decision-model audits]]

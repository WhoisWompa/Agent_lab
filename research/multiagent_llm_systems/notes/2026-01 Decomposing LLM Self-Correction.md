---
title: Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis
authors: Yin Li et al.
date: 2026-01
arxiv: 2601.00828
url: https://arxiv.org/abs/2601.00828
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2601.00828.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis

## One line
Splits a model's self-correction into detecting, locating and fixing its own errors, and reports on grade-school math that the strongest of three models fixes the smallest share of its own mistakes.

## Method
The problem: "self-correction" bundles several abilities, so a loop that fails (as Huang et al. found for intrinsic correction without an oracle) gives no hint of which part broke. The paper measures three separately, on solutions the model itself got wrong:
- Detection: shown its own wrong solution, does it call it incorrect?
- Localization: can it name the first faulty step?
- Correction: can it reach the gold answer, either unprompted ("verify and correct") or given its own localization as a hint? A third condition runs up to three rounds of verify-and-re-solve.

Two ideas come out of the numbers. The Accuracy-Correction Paradox: the more accurate model corrects fewer of its errors. The Error Depth Hypothesis explains it: a strong model errs rarely but on "deep" errors (misreading the problem, flawed logic) that re-reading does not fix, while a weak model's errors are mostly shallow arithmetic slips that a second look repairs. No intervention is proposed; the practical advice is to profile a model's error mix before putting a self-refinement loop around it.

## Evaluated on
Evaluated on 500 harder GSM8K test problems per model, with DeepSeek-Chat, GPT-3.5-Turbo and Claude-3-Haiku.
- Paradox: DeepSeek (94.0% accuracy) corrects 16.7% of its errors unprompted, against 26.8% for GPT-3.5 (66.4%) and 29.1% for Claude (70.4%). Only 30 DeepSeek errors exist, so its interval is wide (6 to 35%) and overlaps GPT-3.5's (20 to 34%).
- Detection does not predict correction: GPT-3.5 flags 81.5% of its errors yet fixes 26.8%; Claude flags 10.1% yet fixes 29.1%.
- Error depth: 62% of GPT-3.5's errors are calculation slips versus 22% of DeepSeek's; setup plus logic errors are 77% of DeepSeek's.
- Iteration helps weak models, not the strong one: three rounds reach 67.9% (GPT-3.5) and 60.8% (Claude), but DeepSeek stalls at 20.0% after round one.
- Hints: the authors say hints from the model's own localization hurt all models (GPT-3.5 26.8 to 15.5%, Claude 29.1 to 12.8%).

## Limitations admitted by the authors
- DeepSeek has only 30 errors, so the central "strongest model is worst" claim rests on a small sample. The paper does not report a test of the gap.
- Only three models, all mid-to-small tier; GPT-4-class, Claude-Sonnet and Llama-3 are untested, so the paradox may not generalize.
- The hints are the model's own localizations, not ground truth, so the harm may only reflect bad localization or anchoring on the faulty path; the paper does not separate the two.
- Math has a checkable answer; open-ended tasks may behave differently.
- Error types are labelled by the model itself, which may misjudge its own errors. The Error Depth Hypothesis rests on this labelling and has not been checked against human annotation.

## Limitations found by others

## What it leaves untried
- Tests of the Error Depth Hypothesis itself: injecting known shallow versus deep errors, or human-labelled error types, would show whether depth really drives correction. At present it is an explanation fitted to three error-type percentages.
- Tool-augmented correction (a calculator for shallow slips), listed as future work, and external feedback for deep errors, which the paper says need "external guidance" but never tests.
- Controls for the iterative result. The iterative rate is defined as the maximum across rounds, and the text does not say how rounds are scored without the gold answer. Comparing it with the single-pass 16.7 to 29.1% is therefore not shown to be fair. A re-sampling-only baseline would show whether reflection or plain retrying gives the gain.

## Notes on reading
The text contradicts itself in places. The abstract says hints hurt all models, but Table 1 shows DeepSeek improving from 16.7% to 26.7% with a hint. GPT-3.5's baseline accuracy is 68% in one place and 66.4% in another.

## Topics
[[Topic - self-refinement and critique loops]]

---
title: "Self-Refine: Iterative Refinement with Self-Feedback"
authors: Madaan et al.
date: 2023-03
arxiv: 2303.17651
url: https://arxiv.org/abs/2303.17651
venue: arXiv (preprint, under review)
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2303.17651.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# Self-Refine: Iterative Refinement with Self-Feedback

## One line
One LLM drafts an answer, critiques it in natural language, and rewrites it from its own critique, repeatedly, with no training, and this beats single-pass generation on 6 of 7 tasks.

## Method
The problem: a first LLM output often misses multi-part requirements (dialogue quality, code readability, 20-30 keyword constraints). Earlier refinement needed a trained refiner per domain, or human or reward-model feedback, which is costly.

The idea: the same model M plays three roles through three few-shot prompts. It generates y0, then writes feedback on y0, then produces y1 from the input, the draft and the feedback. Feedback is asked to be actionable (contains a concrete fix) and specific (names the phrase or construct to change), and for multi-aspect tasks it also gives numeric scores per aspect. The loop stops at a fixed cap (4 iterations in the experiments) or when the feedback contains a stop indicator the model was prompted to emit. The full history of earlier drafts and feedback is appended to each refine prompt so the model does not repeat mistakes. Because scores come per aspect, the final output can be the best-scoring draft rather than the last, which matters when one aspect improves while another degrades.

Why it should work: critiquing a given text is easier than producing it right the first time, and a specific critique tells the refiner what to change. Nothing is enforced by the harness beyond the loop and the stop check; all judgment is prompted.

## Evaluated on
- Beats the same model without the loop on all 7 tasks with GPT-3.5, ChatGPT and GPT-4, about 20% absolute on average (abstract). Largest: GPT-4 dialogue preference 25.4 to 74.6, sentiment reversal 3.8 to 36.2, constrained generation 15.0 to 45.0. Code optimization gains are small (GPT-4 27.3 to 36.0).
- Math reasoning barely moves (GPT-4 92.9 to 93.1, GPT-3.5 64.1 to 64.1). Reason: the model cannot find its own error; ChatGPT feedback said "everything looks good" for 94% of instances. With an external signal saying the answer is wrong, gains exceed 5% (appendix).
- Feedback quality is the active ingredient. Specific feedback vs generic vs none: sentiment reversal 43.2 / 31.2 / 0; code optimization 27.5 / 26.0 / 24.8; acronyms 56.4 / 54.0 / 48.0.
- Iterations help with diminishing returns: constrained generation 29.0 to 49.7 over three iterations, code optimization 22.0 to 28.8, with most of the gain in the first step.
- Not just more samples: outputs were still preferred by humans over each of 4 independent ChatGPT samples.
- Failure analysis of 35 failed cases (code, math): 33% wrong error location, 61% wrong suggested fix, only 6% a refiner that botched good feedback. So failure lies in the critic, not the rewriter.

## Limitations admitted by the authors
- The base model must follow few-shot or instruction prompts well. Vicuna-13B could not produce feedback in the required format and, even with oracle feedback, repeated its output or hallucinated a conversation.
- All strong results use closed, paid models (GPT-3.5, ChatGPT, GPT-4, Codex) whose training data and size are undisclosed, which limits reproduction and explanation.
- English only; benefit in other languages is untested.
- No guard against steering the loop toward toxic or harmful text.
- Quality is not monotone in iterations on multi-aspect tasks such as acronyms; this is patched by score-based output selection, not solved.

## Limitations found by others

## What it leaves untried
- Using an external verifier (tests, a checker) for the feedback step on math. Its own appendix shows more than 5% gain when error detection is outside the model, and self-critique is the weak point (94% "looks good").
- Mixing models: a small model drafts and a large one critiques. Only one preliminary result is given (Vicuna-13B 24.18 to 40.5 on math with ChatGPT feedback), with no systematic study.
- Choosing the stop point per input by a calibrated confidence rather than a fixed cap or prompted flag; the paper gives no evidence the stop indicator is reliable.

## Topics
[[Topic - self-refinement and critique loops]]

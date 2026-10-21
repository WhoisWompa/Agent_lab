---
title: Small Language Models Need Strong Verifiers to Self-Correct Reasoning
authors: Yunxiang Zhang et al.
date: 2024-04
arxiv: 2404.17140
url: https://arxiv.org/abs/2404.17140
venue: arXiv (cs.CL)
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2404.17140.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "trained judges and reward models"]
---
# Small Language Models Need Strong Verifiers to Self-Correct Reasoning

## One line
SCORE has a 7B to 13B model write its own critique-correction training data and fine-tune on it, and the paper finds the gain depends on a strong verifier (GPT-4 or oracle labels), not on the refiner.

## Method
The problem: small open models cannot self-correct reasoning by prompting, and earlier fixes distil critiques from a stronger model. SCORE removes that dependence in two stages.

- **Critiques with a hint.** Sample 10 step-by-step solutions per training question and label them by final answer. For each incorrect solution, show the same model a correct solution to the same question as a hint, and ask for step-by-step feedback. The authors' argument (Appendix B, Bayes' rule) is that conditioning on the correct solution yields the critique that best leads from the wrong solution to the right one, because the model only compares steps and justifies the right ones.
- **Filtering.** Rule filters keep critiques with matching step and feedback counts, steps copied exactly, and the correct answer in the last feedback. A prompt filter then keeps only critiques after which the base model, without the hint, revises to the correct answer. Only 25.5% (LLaMA-2-13B) and 8.8% (Gemma-7B) of raw critiques survive on GSM8K.
- **Fine-tuning.** The same model is fine-tuned to produce a critique of the first wrong step plus a corrected solution, with no hint at inference.

Self-correction is split into a separate verify step and a refine step, run for one round only. The verifier is either a same-size model fine-tuned on final-answer correctness, GPT-4 few-shot prompted, or oracle labels. The refiner runs only when the verifier flags an answer as wrong. Splitting the two lets the authors vary verifier strength with the refiner held fixed.

## Evaluated on
- **The refiner learns something.** With oracle labels, the fine-tuned refiner gains +8.8 (LLaMA) and +11.1 (Gemma) on GSM8K. The prompted refiner gains +1.4 for Gemma and +2.5 for LLaMA. On CommonsenseQA the refiner beats a random re-pick baseline.
- **GPT-4 as verifier helps.** Gemma-7B gains +8.3 on average over five datasets. LLaMA-13B's GSM8K gain is +4.2. Across datasets the average gain over the initial answer is 14.6% (stated in the introduction).
- **A self-trained verifier is the bottleneck.** GSM8K verifier F1 is 51.1 for LLaMA's self-verifier against 88.4 for GPT-4. The self-verifier gains about +0.3, while the prompted verifier plus prompted refiner often loses accuracy (-7.5 on CommonsenseQA for LLaMA).
- **Why GPT-4 helps.** In a confusion matrix, On GSM8K with LLaMA, the weak self-verifier passes 599 wrong answers as correct, so they never reach the refiner. GPT-4 passes only 68.
- **The refiner transfers, the verifier does not.** The GSM8K-trained Gemma refiner gains +12.1 on a MATH subset with GPT-4 verification.
- **Costs.** Inference is 1.3x (LLaMA) and 1.4x (Gemma) the base latency, against 4.5x for sampling 10 solutions. Combined with 10-sample reranking, SCORE adds +1.7 on GSM8K with only the weak verifier.

## Limitations admitted by the authors
- Without a strong verifier, intrinsic self-correction does not work: the self-verifier gives about +0.3 and the paper concludes self-verification is the obstacle. Fine-tuning data scaling plateaus near 10k examples under a weak verifier (Figure 4).
- The headline gains rely on GPT-4 or oracle verification, so the "no stronger model" claim covers only the refiner's training data, not the full pipeline.
- Generating the data takes heavy GPU compute. The paper does not compare its cost with distilling from an API model.
- Verifying and refining add inference latency (1.3x to 1.4x).

## Limitations found by others

## What it leaves untried
- Better small-model verifiers (step-level, or built on model internals). The paper names this as the key gap but tests only outcome-label verifiers.
- More than one correction round. Everything is one iteration, so repeated critique-revise loops are unexamined.
- Ablation of the hint idea against critiques from the stronger model, which would show how much quality is lost by avoiding distillation (unsupported in the paper).

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - trained judges and reward models]]

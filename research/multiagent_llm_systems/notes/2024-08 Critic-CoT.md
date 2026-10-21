---
title: "Critic-CoT: Boosting the Reasoning Abilities of Large Language Model via Chain-of-Thought Critic"
authors: Xin Zheng et al.
date: 2024-08
arxiv: 2408.16326
url: https://arxiv.org/abs/2408.16326
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2408.16326.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "trained judges and reward models"]
---
# Critic-CoT: Boosting the Reasoning Abilities of Large Language Model via Chain-of-Thought Critic

## One line
Fine-tunes one LLM to critique its own solutions step by step in chain-of-thought and to repair them from the first wrong step, using training data labelled only by whether the final answer is right.

## Method
The problem: self-critique with a plain prompt is "System-1", a quick verdict with no analysis, and off-the-shelf models do not self-correct reliably without external feedback. Critique is also rarely trained for, and nobody had studied how critique skill relates to solving skill.

Critic-CoT makes the critique itself a reasoning task. The critic writes an analysis of every step and labels each one correct or incorrect. Refinement then restarts from the first flagged step instead of from scratch.

Training data needs no human labels. A generator samples solutions, and a critic (GPT-4-Turbo) critiques and refines them. A critique is kept only when it agrees with the gold final answer:
- A wrong solution is kept only if the critique flags an error and the refinement then reaches the gold answer.
- A right solution is kept only if the critique flags nothing.

All other critiques are resampled, up to k times. The assumption is that a critique which leads to the right answer is probably a valid critique. This is weak supervision.

Training has two stages:
- Stage 1 fine-tunes Llama-3-70B-Instruct on the GPT-4-Turbo critique and refinement data.
- Stage 2 lets the stage-1 model critique and refine its own samples, falling back to GPT-4-Turbo when it fails, and retrains the base model on stage 1 plus stage 2.

At inference there are two uses:
- Iterative refine: critique, refine from the first error, and repeat until the critic finds no error. This is capped at depth 8, with up to 8 restarts.
- Critic as filter: drop sampled solutions the critic flags, then take a majority vote over the rest.

## Evaluated on
- Training alone helps solving, with no critique at test time: top-1 goes from 89.6 to 91.7 on GSM8K and from 50.4 to 57.6 on MATH500. The authors read this as critique and solving reinforcing each other.
- Iterative refine adds more: 93.3 on GSM8K and 57.8 on MATH500. On MATH500 the gain over the 57.6 trained model is only 0.2.
- Filtering improves on a plain vote:
  - GSM8K: 95.4 vs 94.8 (Maj1@96).
  - MATH500: 68.4 vs 65.4 (Maj1@512).
  - This beats the process-reward-model baselines listed in the paper's comparison.
- Step-wise CoT is what drives critic accuracy. Without it, accuracy falls from 92.3 to 89.5 (step labels only) and 88.0 (whole-solution label) on GSM8K. On MATH500 it falls from 72.2 to 63.8 and 63.0.
- Training on refinement data alone backfires. Iterative refine drops accuracy from 92.0 to 88.2 on GSM8K and from 55.4 to 49.8 on MATH500, because the critic stays weak.
- The gain is not plain distillation. Fine-tuning on GPT-4-Turbo's correct solutions gives 90.7 and 48.0, against 93.3 and 57.8 for Critic-CoT with refine.
- Out of domain the gains are small and uneven.
  - Refine on AGIEval with a MATH-trained critic: 59.8 to 63.7.
  - HumanEval refine with a GSM8K-trained critic: 76.2 to 78.1, but 84.8 with a MATH-trained one.
  - Filtering with a GSM8K-trained critic on AGIEval slightly lowers accuracy: 60.7 to 60.3.

## Limitations admitted by the authors
- The data recipe needs tasks where the final answer is checkable. It cannot say whether a critique is valid on open-ended tasks, so how to filter critiques and train critics there is left open.

## Limitations found by others

## What it leaves untried
- Tasks with no verifiable final answer. The recipe depends entirely on answer matching to accept a critique, and the paper offers no replacement for it.
- Critic quality is still modest. On GSM8K, critic precision is 53.3 and recall 58.2 (F1 55.7), and the paper does not examine the false alarms. A false alarm can pull a correct solution away from a right answer, and the paper does not measure how often that happens.
- Only one base model, Llama-3-70B-Instruct, is trained, and only with GPT-4-Turbo as the teacher. The mutual-reinforcement claim (critique training raises solving) is not tested at other scales or teachers.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - trained judges and reward models]]

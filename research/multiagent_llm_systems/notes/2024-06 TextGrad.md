---
title: "TextGrad: Automatic Differentiation via Text"
authors: Yuksekgonul et al.
date: 2024-06
arxiv: 2406.07496
url: https://arxiv.org/abs/2406.07496
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2406.07496.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "self-refinement and critique loops"]
---
# TextGrad: Automatic Differentiation via Text

## One line
Treats a compound LLM system as a computation graph and improves any text variable in it (prompt, code, solution, molecule string) by passing LLM-written criticism backward along the graph like gradients.

## Method
Problem: compound AI systems (several LLM calls plus tools and simulators) are hand-tuned by experts, and numeric backpropagation does not work through black-box API calls.

Idea: copy the structure of PyTorch autodiff, with text in place of tensors. Each variable is a node; each function (an LLM call, a code interpreter, a docking simulator) is an edge. A loss is an evaluation, written as a natural-language instruction to an LLM, or computed by a tool such as unit tests or a simulator. The "gradient" of a variable is a natural-language critique of how it should change to improve the loss. It is produced by an LLM that sees the variable, the downstream output and the critique already collected for that output. Critiques from every successor of a variable are collected, mirroring the chain rule. An optimizer, Textual Gradient Descent, is one LLM call that takes the variable plus its critiques and writes a revised variable. Each iteration costs at most one extra LLM call per graph edge.

Two uses share the same code. Instance optimization rewrites one answer at test time, with no ground truth needed when the loss is self-critique. Prompt optimization rewrites a system prompt over minibatches. Optimizer ideas are borrowed by analogy: minibatches (losses are summed, critiques concatenated), momentum (the optimizer sees earlier versions of the variable) and constraints written in words. The gradient and update prompts are fixed across all applications. The assumption is that a strong LLM can reason about each component well enough to criticise it usefully.

## Evaluated on
- Beats the prior best on LeetCode Hard code repair with no demonstrations: completion rate 0.36 vs 0.31 for Reflexion (one demonstration) and 0.26 zero-shot, averaged over 5 seeds, gpt-4o, 5 iterations. The prose says 23% for zero-shot while the table says 0.26; the paper does not reconcile the two.
- Test-time refinement of gpt-4o answers raises Google-proof QA accuracy from 51.0 (chain of thought) to 55.0, above the best reported 53.6. It also raises MMLU Machine Learning from 85.7 to 88.4 and College Physics from 91.2 to 95.1. This uses 3 refinement steps plus majority vote, so part of the gain may come from the voting; the paper gives no ablation.
- Prompt optimization for gpt-3.5 with gpt-4o supplying the critiques: Object Counting rises from 77.8 (zero-shot chain of thought) to 91.9, ahead of DSPy's 84.9. On Word Sorting (79.8) and GSM8k (81.1) it only ties DSPy. Adding DSPy's demonstrations to the TextGrad prompt gives 82.1 on GSM8k, so the two methods are complementary.
- Molecule design: on 58 protein targets, ten iterations from a small fragment give molecules whose binding score (Vina) is similar to approved drugs and whose druglikeness (QED) is higher, on the 29 targets that have approved drugs. Evidence is in silico only.
- Radiotherapy planning: TextGrad tunes the organ weights for a numerical planner. On five prostate patients its plans match the prescribed target dose (D95) and give lower dose to bladder and rectum than the clinical plans. Five patients is a very small sample.

## Limitations admitted by the authors
- Molecule and treatment-plan results are proof of concept, validated only in silico. Real value would need experimental and clinical testing, which the paper does not do.
- The framework covers few component types so far. Tool use and retrieval-augmented systems are future work.
- Optimization stability is not addressed. The authors list variance reduction, adaptive gradients and LLM self-verification as open directions.
- Many simultaneous natural-language constraints reduce how reliably the LLM follows them. This limits the constrained-optimization analogy.

## Limitations found by others

## What it leaves untried
- No test of whether the critiques are correct. Gains over DSPy appear on one of three reasoning tasks, and no analysis says when the LLM-written gradient misleads or when the loop gets worse. Without that, a user cannot tell when to trust the loop.
- No cost comparison. Each step makes up to one call per edge, and prompt optimization uses a stronger critic (gpt-4o) than the model it tunes. The paper never reports total spend against the accuracy gain.
- Self-referential use, with TextGrad tuning its own gradient and update prompts, is named as future work but not tried. The fixed prompts therefore stay unvalidated as a general default.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - self-refinement and critique loops]]

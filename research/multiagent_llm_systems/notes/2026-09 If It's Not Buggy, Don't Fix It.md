---
title: If It's Not Buggy, Don't Fix It: On the Dynamics of Iterative Bug-fixing with LLMs
authors: Xietao Wang-Lin et al.
date: 2026-09
arxiv: 2609.10123
url: https://arxiv.org/abs/2609.10123
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2609.10123.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "agent system failure analysis"]
---
# If It's Not Buggy, Don't Fix It: On the Dynamics of Iterative Bug-fixing with LLMs

## One line
Treats a blind "find a bug, patch it, repeat" LLM loop as a dynamical system and shows it damages correct code at least as often as it repairs broken code, ends in edit-and-undo cycles, and is driven by a linear "buggy code" direction in the model.

## Method
The problem: autonomous bug-fixing agents, and multi-agent setups where one output becomes the next input, loop until the model finds no more bugs. With no objective test and no history in the prompt, nobody knows what this does to code that is already correct.

The paper models the loop as a map from one code file to the next, C(n+1) = f(C(n)), which is Markovian because the prompt carries only the current file. Two edit styles are compared: rewriting the whole file, and one search/replace block (SRB) per turn, applied programmatically (an invalid block is a no-op). Two quantities are tracked: repair rate alpha = P(next is correct | current is incorrect) and damage rate beta = P(next is incorrect | current is correct). Under greedy decoding the loop must end in an attractor: a fixed point (the model says "None", emits an identity edit, cites a search text not in the file, or degenerates into repeated comments) or a cycle of length two or more.

The second half is mechanistic. A steering vector is the difference of mean last-token activations between files the model confidently calls buggy (P(Y) > 0.9) and confidently bug-free (P(N) > 0.9), in Qwen2.5-7B-Instruct. Adding gamma times this vector to layer 22 activations shifts the model's propensity to edit. The claim is that the model has an internal "buggy code" representation, and pseudo-bug-fixing is that representation firing falsely on correct code.

## Evaluated on
Competitive-programming C++ submissions (CodeContests+), with Gemini 2.5 Flash-Lite and Qwen2.5-7B-Instruct, up to 100 turns.
- Damage beats repair with SRBs. Gemini at temperature 0, starting from correct code: beta 0.293 vs alpha 0.062. Qwen: beta 0.424 vs alpha 0.041.
- Whole-file edits are gentler but still no better than break-even. Gemini at temperature 0: beta 0.165 vs alpha 0.040. At temperature 0.7 both are near zero (beta 0.015, alpha 0.003).
- SRBs give more cycles, longer cycles and longer runs to convergence than whole-file edits. Some cycles alternate between a correct and an incorrect state forever. The paper's example is a model flipping `l - k + 1` to `l - k` and back. A control that adds the same reasoning trace to whole-file edits (appendix) is reported to show the edit format, not the reasoning, causes the cycling.
- The steering direction is real but not a readout of the answer token. Cross-validated AUC is 0.7 to 0.8 in early and middle layers and near 1.0 around layer 19. Its cosine with the Y-minus-N unembedding direction stays at random level in layers 19 to 22, and it shifts issue counts on an unseen issue-counting task.
- Steering controls the loop. Gamma = -0.5 stops the loop entirely: all correct files are kept, but no incorrect file is fixed. Gamma = +0.5 produces more edits; the paper says more rounds come from hallucinated search blocks that cannot be found.

## Limitations admitted by the authors
- Only two models are tested (Gemini 2.5 Flash-Lite and Qwen2.5-7B-Instruct). The paper names larger models as untested, so the damage rates may not hold for stronger ones.
- The setting is blind and goal-free: the prompt has no task statement, tests or history. Results may not transfer to agents given exact goals.
- Single-file programs only. Multi-file repositories are listed as future work.

## Limitations found by others

## What it leaves untried
- Giving the loop a stopping signal, such as a test oracle, a history of past states or a cycle detector. The paper only observes the loop, yet states stopping conditions under ambiguous goals as motivation.
- Using the bug direction as a deployed control. The paper suggests it could tune agent sensitivity, but only shows that gamma = -0.5 saves correct code at the cost of fixing nothing, so no setting that keeps repairs while cutting damage is shown.
- Real multi-agent or agentic harnesses. The loop is a single model re-reading its own output, so the link to delegation setups is asserted in the introduction, not measured.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - agent system failure analysis]]

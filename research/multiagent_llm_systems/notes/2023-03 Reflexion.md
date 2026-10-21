---
title: Reflexion: Language Agents with Verbal Reinforcement Learning
authors: Noah Shinn et al.
date: 2023-03
arxiv: 2303.11366
url: https://arxiv.org/abs/2303.11366
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2303.11366.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# Reflexion: Language Agents with Verbal Reinforcement Learning

## One line
An LLM agent retries a task, turns each failure signal into a written self-reflection kept in memory, and does better on the next trial without any weight update.

## Method
The problem: language agents need to learn from trial and error, but gradient-based RL needs many samples and fine-tuning of a large model. A scalar or binary reward also says little about which step went wrong (the credit assignment problem).

Reflexion splits the loop into three LLM roles. The Actor (Chain of Thought or ReAct) produces a trajectory. The Evaluator scores it. The Self-Reflection model reads the trajectory, the score and the memory, and writes a short first-person lesson, for example "action a_i led to the later errors; I should have done a_i' instead". The lesson is appended to a long-term memory and the Actor sees it in its next trial. The trajectory is short-term memory. The loop ends when the Evaluator passes the result or a trial cap is hit.

The paper treats the policy as the pair (Actor LLM weights, memory text), so the written reflection plays the role of a "semantic gradient". The reason it should work is that text can point at a specific action, which a number cannot.

The Evaluator varies by task. It is exact match on HotPotQA, a hand-written heuristic on ALFWorld (same action and response repeated more than 3 cycles, or more than 30 actions), or an LLM. For code it is a set of at most 6 self-generated unit tests, which keeps the pass@1 number valid because hidden tests are never used. Memory is a sliding window of 1 to 3 reflections to fit the context.

## Evaluated on
- Decision-making improves with trials. On ALFWorld, ReAct plus Reflexion solves 130 of 134 tasks, an absolute gain of 22% over 12 trials. ReAct alone stalls between trials 6 and 7 and stays at a 22% hallucination rate (the agent believes it holds an item it does not hold).
- Reasoning improves. On HotPotQA, Reflexion beats every baseline. Baselines never solve a task they failed on the first trial, even at temperature 0.7, so resampling alone does not help. Reflexion lifts the CoT with ground-truth context agent by 14%.
- The written reflection is what helps, not the retry. An ablation that gives the agent only its last trajectory as memory gains 8% less than full self-reflection.
- Code results are state of the art on most benchmarks. HumanEval Python pass@1 is 91.0 against 80.1 for GPT-4. HumanEval Rust is 68.0 against 60.0, and MBPP Rust is 75.4 against 70.9. LeetcodeHard (a new 40-question set) is 15.0 against 7.5.
- Both parts of the code loop are needed. On the 50 hardest HumanEval Rust problems, removing test generation drops accuracy to 52% against a 60% baseline, and removing the written reflection stays at 60%. The full method reaches 68%.

## Limitations admitted by the authors
- The method depends on the quality of self-evaluation and has no formal guarantee. Reflexion is natural-language policy optimisation and can get stuck in a local optimum.
- Weak self-generated tests cause false positives. On MBPP Python, 16.3% of solutions that pass all generated tests are wrong, against 1.4% on HumanEval. Reflexion scores 77.1 there, below the GPT-4 baseline of 80.1, so it is the one code benchmark where it loses.
- Test-driven checking fails for some code. Examples are non-deterministic functions, functions that call APIs, and hardware-dependent or concurrent code, where input-output tests are hard to specify.
- Memory is only a sliding window of 1 to 3 reflections. Longer histories are not handled; the authors suggest vector or SQL stores.
- The ability to write useful self-corrections needs a strong model. With starchat-beta on HumanEval Python, Reflexion gives 0.26, the same as the baseline.
- Generated code is run without validation, so the experiments need isolated execution environments.

## Limitations found by others

## What it leaves untried
- Evaluator error is only partly measured. Test false-positive rates are reported for code, but nothing is reported for the LLM evaluator on ALFWorld or for how much its error limits learning.
- Long-term memory beyond a 1 to 3 item window, and RL ideas such as value learning in language or off-policy exploration, are named as future work and not tried.
- The claim that the stored reflections make agents more interpretable and monitorable is made in the broader-impact section with no experiment behind it.

## Topics
[[Topic - self-refinement and critique loops]]

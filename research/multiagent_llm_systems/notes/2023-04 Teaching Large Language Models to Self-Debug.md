---
title: Teaching Large Language Models to Self-Debug
authors: Xinyun Chen et al.
date: 2023-04
arxiv: 2304.05128
url: https://arxiv.org/abs/2304.05128
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2304.05128.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# Teaching Large Language Models to Self-Debug

## One line
A pretrained LLM, prompted with a few examples and no fine-tuning, runs its own code, explains it in words, judges it, and rewrites it until it passes or the turn limit is hit.

## Method
The problem: a model rarely gets complex code right in one shot, and the usual fix is to sample tens of programs and rerank them, which is expensive. Training a separate repair model needs extra data. Earlier work also said LLMs could not correct code without external feedback such as unit tests or human instructions.

The idea is a loop of three steps per turn: generate a program, explain it, produce a feedback message saying whether it is correct. The loop stops when the feedback says "correct" or after a maximum of 10 turns. In practice successful runs mostly end within 3 turns. Only prompts teach the behaviour.

Feedback comes in four forms:
- Simple: only "correct" or "wrong".
- Unit-test feedback: failed assertions and actual outputs, when tests exist.
- Code explanation, "rubber duck" style: the model describes the code clause by clause and compares it with the question. For SQL it also compares the number of returned columns with what the question asks for. The model is not asked to name the bug.
- Execution trace: the model writes the line-by-line execution itself. This is model text, not real intermediate states.

Where tests exist, execution decides correctness. Where none exist (text-to-SQL), the model must judge itself from its explanation and the first two rows of the query result. When several initial samples exist, the program with the most common execution result is chosen first and then debugged. The reason it should work is that explaining code surfaces mismatches with the question that a bare "wrong" cannot.

## Evaluated on
- Beats trained and prompting-only rerankers on Spider text-to-SQL: Codex with explanation reaches 84.1, against 81.9 for the trained LEVER verifier and 75.2 for MBR-Exec.
- Without unit tests, explanation is what helps. On Spider, simple feedback leaves Codex at 81.3 (no change from baseline), while explanation gives 84.1. The model "struggles to distinguish between correct and wrong SQL queries without explanation".
- Gains are largest on hard problems: +9 points on extra-hard Spider queries (63.9 to 72.9). Initial queries are usually nearly right, missing a WHERE condition or a column, and the explanation exposes the gap.
- With unit tests, gains reach 12 points: GPT-4 on TransCoder goes from 77.3 to 90.4 with tests plus explanation. On MBPP, Codex goes from 61.4 to 69.8.
- Better sample efficiency: on Spider, debugging a greedy prediction matches 16 samples without debugging, and debugging from 8 samples beats 32 samples. The abstract claims it matches or beats baselines that sample more than 10 times as many programs.
- Execution matters: with unit-test execution removed, gains shrink to about 5 points with Codex, and under 4 points on MBPP and about 1 point on other benchmarks with GPT-4. Simple feedback on MBPP with Codex falls from 61.4 to 57.6.

## Limitations admitted by the authors
- Self-judgment is weak without execution: GPT-3.5 and GPT-4 "tend to be overconfident in their own initial predictions". GPT-3.5 gains 0 on TransCoder when execution is removed (89.1 stays 89.1).
- Explanation helps less on MBPP, for three stated reasons. Unit tests already reveal the failures. Context length forces fewer examples (3 instead of 6). When the first program is far from correct, the model writes a new one and ignores the old.
- Results depend on the model and on few-shot examples. GPT-4 is worse than Codex on Spider (73.2 vs 81.3), a gap the authors attribute to GPT-4 being tuned for zero-shot prompts. This is a hypothesis; they do not test it.
- Execution traces are not reliably useful. They lower Codex on TransCoder (91.6 with tests alone, 87.9 with trace).
- Gains after the first turn are tiny on Spider: one turn is usually enough, and later turns add under 0.1%.
- Model-written messages describing semantic errors gave no gain over line-by-line explanation (preliminary results, not shown).

## Limitations found by others

## What it leaves untried
- Better self-judgment without execution. Explanation gets 2 to 3 points on Spider, and the authors point to richer explanations and bug descriptions as future work but do not test them.
- Whether extra debugging turns pay for themselves. Cost is reported only through the sample-count comparison, and the added calls for explanation and feedback are not priced.

## Topics
[[Topic - self-refinement and critique loops]]

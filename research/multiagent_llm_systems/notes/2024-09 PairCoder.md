---
title: A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement
authors: Huan Zhang et al.
date: 2024-09
arxiv: 2409.05001
url: https://arxiv.org/abs/2409.05001
venue: ASE 2024
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2409.05001.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops"]
---
# A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement

## One line
PairCoder splits code generation between a Navigator agent that proposes and switches solution plans and a Driver agent that writes and repairs code against public tests, beating single-plan prompting and repair baselines.

## Method
The problem: prompting and repair methods follow one solution plan. If the first plan is wrong, repair is misled by it and cannot find the root cause. The paper's motivating example shows repeated repairs stuck on a flawed Plan A while a different Plan B solves the problem at once.

The idea is to copy pair programming with two roles on the same LLM:
- **Navigator** (planner). It first writes a reflection on the problem (edge cases, public-test explanation). It then samples 15 plans at temperature 0.8, embeds them, and clusters them with k-means++ into k=3. The plan nearest each centroid is kept, so the candidates differ in kind (brute force, greedy and so on). It picks one plan by LLM judgement, preferring a correct but slow plan over a fast but risky one. After each failed test it chooses between two moves: repair the current code, or drop the plan and pick another.
- **Driver** (implementer). It writes code from the chosen plan, runs it on the public tests (Pass, Runtime Error, Wrong Answer, Time Limit Exceeded), and repairs code following a strategy the Navigator writes from the error type.

The switch rule is a heuristic, not a learned judgement. If the new code or its execution feedback already appears in the memory kept for the current plan, the plan counts as stuck and is discarded. Memory is cleared at every switch. The loop ends on passing all public tests or after r=10 rounds. Hidden private tests are used only for scoring.

The authors' reasoning for why it works: execution feedback is the external signal that LLMs need to self-correct, and switching plans takes the search out of the local optimum that repair alone cannot leave.

## Evaluated on
- Beats direct prompting on five code benchmarks with GPT-3.5-Turbo: HumanEval 87.80 vs 67.68 pass@1, CodeContest-test 15.15 vs 6.06. Relative gains are 16.97% to 162.43% on GPT-3.5 and 12.00% to 128.76% on DeepSeek-Coder 33B.
- Beats the strongest repair baselines under the same 10 rounds and the same public tests: HumanEval 87.80 vs 78.05 (Self-debugging) and 77.44 (INTERVENOR). With GPT-4 it scores 93.90 on HumanEval vs 91.0 (Reflexion) and 90.2 (Self-collaboration), the latter two quoted from their papers.
- The gain is not just extra samples. Direct prompting resampled up to 10 times with public-test checking reaches 75.61 on HumanEval, below 87.80.
- Both parts are needed. Always repairing (no plan switching) drops HumanEval to 81.10. Always switching plans (no repair) drops it to 74.39. On CodeContest-test, removing either costs 38.86% and 56.35% relative accuracy.
- Repair baselines plateau (e.g. after 5 rounds on CodeContest-test) while PairCoder keeps rising with more rounds. Its plan switches fall near where they plateau (average 3.8 and 6.7 rounds on HumanEval).
- Cost is higher than most baselines: 5.28 API calls per HumanEval problem vs 2.43 for direct prompting. On CodeContest-test it uses 17.56 calls and 24.06k tokens, below Self-debugging's 38.40k tokens.

## Limitations admitted by the authors
- Everything hinges on the public tests. On CodeContest-test only 21.21% of solutions pass them, and the refinement has little signal to work with. Passing public tests does not guarantee passing private ones (71.43% of those that pass do so on CodeContest-test).
- Absolute accuracy on competition problems stays low (15.15% on CodeContest-test with GPT-3.5). Wrong Answer causes 60.00% of failures there, so the planning is not enough for hard problems.
- Possible benchmark leakage: DeepSeek-Coder direct prompting beats GPT-3.5 on three benchmarks, which the authors attribute to leakage but do not test. They argue it hits all baselines equally.
- Zero-shot prompts only. Few-shot demonstrations might help and were not tried.
- Only two open and closed models plus a GPT-4 run, all Python. Generalisation to other LLMs and languages is future work.
- Gains cost extra calls and tokens, and larger k or r would cost more still. The authors say k=3 and r=10 are a cost trade-off, not a tuned optimum.

## Limitations found by others

## What it leaves untried
- No test-case generation to fix the weak public-test signal, although the authors name it as promising. Without it, the framework cannot improve where its feedback is thinnest.
- The plan-switch rule (repeated code or feedback) is never compared with other triggers or with Navigator judgement. It is unknown whether it switches too late.
- The two-agent split is not tested against one model doing both roles in one context, so the benefit of separation as such is unsupported. The ablations only remove behaviours.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]]

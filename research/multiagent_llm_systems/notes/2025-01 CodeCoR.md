---
title: CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation
authors: Ruwei Pan et al.
date: 2025-01
arxiv: 2501.07811
url: https://arxiv.org/abs/2501.07811
venue: Internetware '26 (arXiv v2)
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2501.07811.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops"]
---
# CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation

## One line
A four-agent code pipeline (prompt, test, code, repair) in which every agent produces several candidates and a pruning check discards weak ones before the next agent sees them, so one agent's misreading does not spread downstream.

## Method
The problem: in sequential multi-agent code workflows (CodeCoT, MapCoder), a mistake at an early stage is amplified later. The paper's example is a prompt agent that drops the "preserve first-occurrence order" requirement. The coder then uses `set()`, the test agent writes tests that never check order, and the wrong code passes its own tests.

The fix is to check each stage's output before it is passed on. A Prompt Agent writes several chain-of-thought plans. A Test Agent writes test cases. A Coding Agent writes candidate programs. A Repair Agent writes repair advice for failing code. Each stage has its own pruning rule:
- Prompts and repair advice are scored by the same LLM that wrote them on four binary criteria (clarity, relevance, conciseness, context). A candidate is kept only if all four are 1.
- Test cases are dropped if the LLM flags them as empty, malformed or invalid.
- Code is dropped if it does not compile.

If pruning would remove every candidate at a stage, the highest-scored one is kept, so the pipeline never stalls. Surviving code runs against the generated tests. Failures go to the Repair Agent for up to 3 rounds, and the candidate that passes the most generated tests is returned. Repair advice that fails pruning is replaced by the raw failing tests.

The "self-reflection" is therefore mostly an LLM self-grading step plus execution against LLM-written tests. The paper says the LLM grader is only a heuristic filter and not the correctness oracle. Final scores come from the official benchmark tests.

## Evaluated on
- Beats the strongest multi-agent baseline on function-level code. Average Pass@1 over HumanEval, HumanEval-ET, MBPP and MBPP-ET is 77.13 against 72.8 for MapCoder and 68.9 for CodeCoT, all with GPT-3.5-turbo. The gain is concentrated on MBPP-ET (65.2 against 58.1 for CodeCoT). On MBPP it is only 79.2 against 78.9 for MapCoder.
- Every component matters in the ablation. Removing the Test Agent drops HumanEval from 86.6 to 45.1, which is below plain GPT-3.5-turbo at 57.3. Removing the pruning step costs 9.2 points on HumanEval, 1.3 on HumanEval-ET, 11.5 on MBPP and 7.1 on MBPP-ET.
- The advantage holds with other backbones but narrows. With GPT-4, HumanEval is 94.5 against 93.9 for MapCoder. With CodeLlama-34B it is 43.9 against 42.7.
- Cost is moderate. HumanEval costs $0.0064 per problem against $0.0083 for MapCoder and $0.0071 for CodeCoT, though more than single-prompt methods such as CoT at $0.0047.
- Repository-level results are small in absolute terms. DevEval Pass@1 is 8.88 against 5.70 for CodeCoT, and RAL-Bench functional pass rate is 20.05 against 18.85. The authors call this "preliminary evidence".
- More candidates do not always help. Raising the budget from 3 to 5 candidates per stage (the paper's cfg3 to cfg4) drops HumanEval Pass@1 from 89.63 to 80.49 at roughly twice the cost. The authors blame noisier intermediate output that makes pruning harder.

## Limitations admitted by the authors
- The ablation tests pruning only as a whole workflow switch. The authors say it "does not fully prove that every individual pruning decision is correct". They do not claim retained candidates beat pruned ones, and a retained-versus-pruned analysis is deferred.
- The search is seed-sensitive. The kept prompts have Jaccard overlap 0.0 across three runs and the kept code only 0.142, though final pass/fail agreement stays at 0.935. Intermediate behaviour is not reproducible even when outcomes mostly are.
- Results are stochastic. They average 10 runs, but LLM generation and LLM-based pruning still vary.
- Benchmarks do not measure developer productivity, trust or usability. A user study and SWE-bench are left to future work.

## Limitations found by others

## What it leaves untried
- It never measures whether the LLM pruner agrees with ground truth, for example how often it discards a correct prompt or keeps a wrong one. The all-1s rule is justified only by assertion, so the mechanism claimed as the contribution is untested at the level of single decisions.
- Pruning of tests and repair advice uses the same model that wrote them, and ranking uses the generated tests. Nothing checks whether wrong tests (as in the `set()` example) are caught beyond the compile and format checks.
- The 89.63 for the default budget in the hyperparameter table does not match the 86.6 main-table HumanEval figure, and the text does not explain the gap. A matched comparison of pruning against plain best-of-N selection at equal cost would show what pruning adds over extra sampling.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]]

---
title: Beyond Task Completion: Revealing Corrupt Success in LLM Agents through Procedure-Aware Evaluation
authors: Hongliu Cao et al.
date: 2026-03
arxiv: 2603.03116
url: https://arxiv.org/abs/2603.03116
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2603.03116.pdf
folder: ["multiagent_llm_systems"]
topics: ["agent evaluation benchmarks", "LLM and agent judges", "agent system failure analysis"]
---
# Beyond Task Completion: Revealing Corrupt Success in LLM Agents through Procedure-Aware Evaluation

## One line
Scores agents on how they reach an outcome (policy, grounding, honesty of statements) and disqualifies "corrupt successes", finding that 27-78% of tau-bench successes hide violations.

## Method
The problem: benchmarks score the final state, so an agent that fabricates a price, breaks a policy or claims an action it never ran scores the same as a clean one. Procedure-Aware Evaluation (PAE) logs a "procedure-complete trace" instead of a plain tool log. Every step is split into read, write and communicate actions, and the trace keeps the policy text, tool outputs and dialogue. That makes four consistency checks possible: what was said against what tools returned (data faithfulness), what was said about policy against the policy text (policy faithfulness), what was done against policy (policy compliance), and what was claimed against what was executed (execution consistency).

Scoring has four axes: Utility (the benchmark's own success), Efficiency (turns, time, tokens, redundant calls), Interaction Quality (user burden, verbosity, intent adherence, question fulfilment) and Procedural Integrity (the four checks, each 0/1).

The new piece is gating. Gated utility is task success multiplied by six binary checks (the four integrity checks plus intent adherence and question fulfilment). One violation turns a success into a failure, so a strong axis cannot compensate for a weak one. Semantic checks are done by a GPT-5 judge that reads the policy, the ground truth and the full transcript and attributes each failure to a turn.

## Evaluated on
- Applied to tau-bench Airline and Retail with GPT-5, Kimi-K2-Thinking and Mistral-Large-3, four trials each.
- The axes are not redundant. GPT-5 is 4-5x slower than the others yet has the best judged efficiency (0.94-0.98). Mistral is fastest but has the worst integrity, with data faithfulness down to 0.45 in Airline.
- Corrupt success is common. Mistral has 76% (Retail) and 78% (Airline) of its successes gated out, and GPT-5 about 27%. Retail success for Mistral falls from 0.68 to 0.16.
- Reliability collapses. Retail Pass^4 drops from 0.58 to 0.24 for GPT-5, from 0.31 to 0.04 for Kimi and from 0.46 to 0.03 for Mistral. No model exceeds 24% fully compliant reliable success.
- Rankings flip. Mistral beats Kimi in Retail at 0.68 vs 0.61 ungated, but loses at 0.16 vs 0.27 gated.
- Models fail differently, from manual review of all 131 Airline corrupt successes. Kimi puts 78% of its violations in policy faithfulness and compliance. Mistral puts 55% in data and policy faithfulness (invented flights, arithmetic errors). GPT-5 spreads violations across categories and often confirms an action without calling the tool.
- The benchmark has flaws. Task definitions omit legitimate paths. A coarse database-match reward contradicts finer assertions. The user simulator sometimes puts its stop token in the same message as a confirmation, so the action never runs and the episode "succeeds" by accident.
- Judge reliability: 89.3% on a 150-item human spot-check, about 90% on action-set proxies, and 93.8-95.2% precision on the 131 corrupt cases.

## Limitations admitted by the authors
- The policy checks need an explicit written policy. Without one, gating drops to four checks, and tacit expert norms are not covered.
- It audits behaviour only. Flawed reasoning that happens to produce correct output is invisible, because reasoning traces are not logged.
- The gate is binary and treats a small tone slip and a wrong $209 charge as equally disqualifying. Graded, risk-weighted gating is left as an extension.
- The judge is wrong 5-11% of the time by the authors' own checks. False positives come from semantic equivalence mismatches and simulator termination artifacts, so gated rates carry that error.

## Limitations found by others

## What it leaves untried
- Only three models, two domains and one benchmark are tested. Whether 27-78% corruption holds in other benchmarks or on other agents is unsupported.
- The judge is GPT-5, which is also one of the agents being scored. The paper does not test for self-preference.
- The paper calls for model-specific safeguards based on each failure profile but does not test whether such safeguards cut corrupt successes.

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - LLM and agent judges]] · [[Topic - agent system failure analysis]]

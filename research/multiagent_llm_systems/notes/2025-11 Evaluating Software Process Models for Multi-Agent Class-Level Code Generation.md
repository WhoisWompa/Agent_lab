---
title: Evaluating Software Process Models for Multi-Agent Class-Level Code Generation
authors: Wasique Islam Shafin et al.
date: 2025-11
arxiv: 2511.09794
url: https://arxiv.org/abs/2511.09794
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2511.09794.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "agent system failure analysis"]
---
# Evaluating Software Process Models for Multi-Agent Class-Level Code Generation

## One line
Runs a four-role Waterfall team of LLM agents on class-level Python tasks and ablates each stage, finding that the process cleans up code but usually lowers functional correctness.

## Method
The question: do role-specialised agents following a software process help on class-level code (several interdependent methods, shared state), which earlier multi-agent work (ChatDev, MetaGPT, SOEN-101) tested only at function level?

The team is a fixed Waterfall chain of four agents: Requirement Engineer, Architect, Developer, Tester. Each runs the same prompt template with a role-specific instruction. Each receives only the previous stage's document: the requirements document goes to the Architect, the design document to the Developer, and the Tester derives tests from the user requirement and runs them against the code. Every document is self-refined once with feedback from the other roles. After testing, the Developer may do up to three bug-fix cycles from the test report, and then the run ends. Nothing in the harness checks that a later stage obeys the original specification; the hand-off is documents only.

The study's idea is the ablation. Remove Requirement, Design or Testing one at a time (Implementation always stays) and compare each variant with the full chain and with a plain single-prompt baseline. This shows which stage changes what. Correctness is Pass@1 on tests; quality comes from SonarQube issue density; failures are hand-labelled in a taxonomy.

## Evaluated on
100 ClassEval Python class tasks, three small models (GPT-4o-mini, DeepSeek-Chat, Claude-3.5-Haiku), temperature 0.8.
- The process does not reliably help correctness. Class-level Pass@1 falls 37.8% for GPT-4o-mini and 39.8% for DeepSeek-Chat. Only Claude-3.5-Haiku gains (+9.5%), so the effect depends on the model. The paper only guesses at why.
- Failures change character. Missing Code drops sharply, for example 50 to 1-2 cases for Claude. Semantic Failure rises from 35-49 to 50-55 cases, and Input Validation errors from 2 to as many as 18. Total runtime errors rise 10-53%, mostly ValueError, AssertionError and TypeError.
- The extra errors are often defensive code the specification did not ask for. Most Input Validation errors are "overrestrictive" checks, which fail strict benchmark tests. This is the authors' explanation, not a tested one.
- Code quality improves in places. Consistency issues fall 32-43% for GPT-4o-mini. Adaptability issues rise a lot: +200-390% for GPT-4o-mini, +13-95% for DeepSeek-Chat. Reliability issues rise for all three models.
- Testing is the stage that matters. Dropping it gives the highest error totals (up to +53%) and, for DeepSeek-Chat, the worst Pass@1 (0.19 against 0.32 for the full chain). Dropping Requirement or Design moves error totals within about 5% of each other, so those stages do little.

## Limitations admitted by the authors
- The root-cause labelling was done by hand and is subjective, so the exact cause of an error may be missed. This affects the RQ3 findings.
- Pass@1 is volatile because it scores only the first sample. The authors keep it because it is common in the field.
- The Waterfall chain only approximates a human process, and other variants or stage combinations might behave differently.
- The Tester agent is an LLM writing its own unit tests. The authors suggest search-based or hybrid test generation might cover more faults.
- The dataset is the largest single source of failure (47-62 cases for the Waterfall variants on GPT-4o-mini and DeepSeek-Chat, 24 to 59 for Claude). Faulty specs and faulty tests in ClassEval inflate errors in every condition.

## Limitations found by others

## What it leaves untried
- Adaptive pipelines that switch stages on or off per task or model. The results show stages help some models and hurt others, but the paper only suggests this.
- A reconciliation step that stops design and test stages from overriding the original specification, which the error analysis blames for the extra validation failures. It is proposed but not built or measured.
- Other process models (Agile, TDD) and other benchmarks. Only Waterfall on one 100-task Python benchmark was tried, so the "process changes failure profile" claim rests on one setup.

## Topics
[[Topic - role-based agent teams]] · [[Topic - agent system failure analysis]]

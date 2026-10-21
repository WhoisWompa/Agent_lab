---
title: TaskWeaver: A Code-First Agent Framework
authors: Bo Qiao et al.
date: 2023-11
arxiv: 2311.17541
url: https://arxiv.org/abs/2311.17541
venue: arXiv
category: framework-production
pdf: research/multiagent_llm_systems/pdfs/2311.17541.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "role-based agent teams"]
---
# TaskWeaver: A Code-First Agent Framework

## One line
A Planner LLM breaks a request into sub-tasks and hands each to a Code Interpreter that writes and runs Python, so plugins, DataFrames and ad-hoc code all live in one stateful execution.

## Method
The problem: existing agent frameworks (LangChain, AutoGen, JARVIS and others) pass complex data such as DataFrames by writing it to disk or encoding it as strings or JSON in the prompt, which the authors say raises error rates on large data. They also offer no systematic way to inject domain knowledge, and a plugin per ad-hoc query is impractical.

The idea is to make code the common currency. Every request becomes Python, and user plugins are plain functions the generated code may call. This lets native objects (DataFrames) pass between plugins and chat rounds without serialisation, and lets the model write custom code where no plugin exists.

Two roles do the work. The Planner is the only role that talks to the user. It drafts a plan, then reviews it and merges sub-tasks that depend on each other only sequentially, since they need no human or LLM intervention between them and fewer steps means fewer LLM calls. It then follows a ReAct pattern: after each result it may revise the plan or ask the user. The Code Interpreter has a generator and an executor. The generator sees plugin schemas (name, arguments, returns) but not plugin implementations. The executor is a per-session Jupyter kernel, optionally inside Docker, so variables persist across rounds.

The harness enforces what prompts only request. Generated code is parsed to an AST and checked against configurable rules (forbidden packages, unsafe calls) before running. The prompt alone is not trusted, because the authors note models ignore such instructions. A violation triggers regeneration, and after repeated failures the Planner is told. Execution errors go back to the generator, up to three retries. A plugin-only mode denies all non-plugin code.

Other parts: planner and generator examples (YAML conversation histories) carry domain knowledge. Only plugins relevant to the request are put in the prompt. An "experience pool" of tips distilled from past chats is retrieved for similar requests and for user preferences. Each role can run on a different model, for example a cheaper one for simple tasks. The authors also describe wrapping TaskWeaver agents as plugins or roles in a multi-agent setting, but present no evidence for it.

For evaluation they propose an Examiner (gives the task, may not hint) and a Judge (checks the final solution against ground truth), so agents that ask clarifying questions are not scored wrong.

## Evaluated on
- GPT-4 beats GPT-3.5 throughout: 0.87 vs 0.42 on the authors' 23 design test cases, 0.60 vs 0.40 on DS-1000 (816 cases), 0.88 vs 0.70 on InfiAgent-DABench, 0.72 vs 0.36 on DSEval.
- Plan merging saves calls: in one demo, LLM calls dropped from 6 to 3.
- Auto-correction recovered a failed pandas_datareader call by switching to yfinance in the stock-forecast case study. Anomaly detection found 11 anomalies in 720 rows.
- Safety demos: requests to delete a system file or read a secret key were declined, and plugin-only mode refused arbitrary code. These are single demonstrations.
- No comparison against another framework appears anywhere in the text.

## Limitations admitted by the authors
- LLM endpoint performance fluctuates over time and across host machines, so even the design test cases are not reliably passed.
- DS-1000 and DSEval scores are depressed by rigid output comparison. Pandas DataFrame mismatches in index or dtype are counted as failures although easy to fix. DSEval's strict pass rate rises from 42.50 to 60.00 on Leetcode (GPT-3.5) once presentation errors are excluded, so the benchmark scores understate real utility.
- Weaker models struggle: GPT-3.5 averages 0.42 on the design cases, and in two cases (stock forecasting, listing files) it beat GPT-4, which declined the file-listing task claiming no file-system access.
- Questions from StackOverflow are ambiguous, and the authors say this makes scoring them hard.

## Limitations found by others

## What it leaves untried
- No ablation of the claimed mechanisms (two-phase planning, AST check, examples, experience memory, dynamic plugin selection). Only the plan-merge demo has a number (6 to 3 calls), so which parts earn the gains is unsupported.
- The Examiner/Judge evaluation is proposed but never used for the reported scores. All results use fixed scoring or execution matching, the rigid method the authors criticise.
- The multi-agent expansion and the security claim (Docker isolation, AST rules) get no adversarial test or measurement.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - role-based agent teams]]

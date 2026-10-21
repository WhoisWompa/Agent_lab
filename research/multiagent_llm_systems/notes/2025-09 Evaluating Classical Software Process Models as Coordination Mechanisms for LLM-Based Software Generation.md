---
title: Evaluating Classical Software Process Models as Coordination Mechanisms for LLM-Based Software Generation
authors: Duc Minh Ha et al.
date: 2025-09
arxiv: 2509.13942
url: https://arxiv.org/abs/2509.13942
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2509.13942.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams"]
---
# Evaluating Classical Software Process Models as Coordination Mechanisms for LLM-Based Software Generation

## One line
Implements Waterfall, V-Model and Agile as three coordination scaffolds inside MetaGPT and compares the size, cost and quality of the software its agent teams produce.

## Method
The problem: multi-agent software teams (MetaGPT, ChatDev, AutoGen) show that agents can build a product together, but nobody had compared which coordination structure works better. AgileCoder tried only Agile, and ChatDev showed feasibility only. The authors argue that human software processes already solve this coordination problem. They supply defined roles, fixed phase order and intermediate artifacts (requirements, design docs, test plans) that act as a memory-friendly channel between agents with limited context.

They rebuild three processes on MetaGPT's role-and-SOP machinery. All three are centralised: the Developer agent orchestrates and a CodeManager holds the files.
- **Waterfall:** a strict forward pipeline of Project Manager, Designer, Developer, Tester and Deployer. There is no backward feedback, so it is stable but cannot react to errors.
- **V-Model:** each build phase is paired with a test phase (requirements with acceptance, design with integration, code with unit), with separate test agents. Tests map to specifications, but there is little room for iteration.
- **Agile:** iterative sprints with an added Sprint Manager that tracks sprint context, caching and versions. Feedback loops exist inside sprints, at the price of more orchestration overhead.

The claim is that process structure, not model choice, shapes outcomes. The design holds prompts, SOPs and role definitions constant, so only the process varies.

## Evaluated on
11 small projects (games, utilities in JavaScript or Python), each run under 3 processes and 4 LLMs (GPT-4o-mini, GPT-4.1-nano, DeepSeek-Chat, DeepSeek-Reasoner), 132 runs.
- Process choice changes size and cost significantly. Median files are Agile 37, V-Model 19, Waterfall 13 (F=239.7). Median LOC are V-Model 934, Agile 578, Waterfall 475.
- Waterfall is cheapest. Median time is 118 s against 226 s for V-Model and 450 s for Agile. Agile's maximum was 7,865 s. Waterfall tokens were about 13.7k at the median in the table, against about 30k for the other two.
- Agile has the best measured quality. Human-run test failure medians are 40% for Agile, 90% for V-Model and 100% for Waterfall. AI-generated tests flagged bugs at 35.6% for Agile, 18.5% for Waterfall and 8.3% for V-Model.
- V-Model's validation-first design did not buy reliability. Its AI-test bug detection (8.3%) was the lowest of the three. The authors suggest static plans produce superficial test cases.
- Model choice mostly moves efficiency, not correctness. GPT-4.1-nano ran in about 90 s and DeepSeek models took over 660 s. LLM effect on human-found test failures was not significant (p=0.073).

## Limitations admitted by the authors
- The quality claim is weak. The process effect on human-detected failures is only p=0.041, and the discussion says Agile's edge "is not robustly supported". The abstract and conclusion still state Agile has the highest quality.
- Tasks are 11 small games and utilities. Results may not hold for industrial, multi-team or safety-critical systems, where evolving requirements and compliance matter.
- Everything runs on MetaGPT. Its built-in CodeManager may favour sequential hand-offs such as Waterfall's, so the ranking may be framework-specific. CAMEL and AutoGen are not tried.
- LOC and file counts measure size, not productivity, and code smells (SonarQube) only loosely track maintainability. Outputs are non-deterministic and assignment is not randomised, so carry-over effects remain.

## Limitations found by others

## What it leaves untried
- Other coordination styles (debate, marketplace negotiation, peer-to-peer). The authors list these as future work, and all three tested processes share one centralised Developer-orchestrated topology, so the process effect is not separated from that structure.
- Larger multi-module systems with long-running development. This is where coordination should matter most, and it is untested.
- Human-in-the-loop checkpoints. The paper argues process artifacts enable them but never runs one.

## Topics
[[Topic - role-based agent teams]]

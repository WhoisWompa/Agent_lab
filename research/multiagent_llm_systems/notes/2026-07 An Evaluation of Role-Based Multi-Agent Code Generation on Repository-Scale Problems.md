---
title: An Evaluation of Role-Based Multi-Agent Code Generation on Repository-Scale Problems
authors: Benedetta Donato et al.
date: 2026-07
arxiv: 2607.04212
url: https://arxiv.org/abs/2607.04212
venue: IEEE Software (accepted)
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2607.04212.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "orchestration and delegation", "self-refinement and critique loops"]
---
# An Evaluation of Role-Based Multi-Agent Code Generation on Repository-Scale Problems

## One line
Compares GPT-5 alone with a planner-plus-coder agent team (with and without a review-and-repair loop) at generating whole Java repositories from a requirements document, and finds the team closer to developer code but still far from a working system.

## Method
Existing role-based code-generation frameworks (MetaGPT, AgileCoder, RTADev) were only tested on function-level benchmarks or apps under 10 files. The question here is when, and by how much, an agent team beats a single LLM at repository scale.

The pipeline has four phases. A planning agent reads the requirements document (SRS), breaks it into ordered tasks, and defines the coding agents dynamically, each with an identifier, a role, role-specific instructions and an assigned LLM. Roles are not fixed in advance because the needed tasks are not known beforehand. In the coding phase each agent writes code for its task, then writes a summary that is passed to the next agent, so later agents know the existing code. An assessment agent then compares the code with the SRS in a static, text-only reading and lists missing or partial requirements. A setup step generates the Maven build file.

Two variants are compared. Sequential skips assessment. Reflexive loops assessment and replanning until no issues are found, up to ten times (built on ChatDev 2.0). The baseline is a single GPT-5 call with the same prompt but no plan. All variants use GPT-5.

## Evaluated on
Twelve recent Java repositories (three each of trivial, simple, moderate, complex), with requirements documents generated from README and Javadoc. Similarity to the original code and a requirement-coverage score stand in for tests, which cannot run on differently structured code.

- The reflexive team is closest to developer code: overall JPlag similarity 0.43 vs 0.33 sequential vs 0.21 single LLM; CrystalBleu 0.19 vs 0.13 vs 0.10.
- The review loop is what helps: the sequential team (no assessment) has the lowest requirement coverage on complex projects (34% vs 61% for the single LLM and 72% for reflexive). Overall coverage is 78% reflexive, 55% sequential, 61% single LLM. The gap over the others widens with project size.
- Output is still a skeleton: generated code is 25% down to 1% of the original size as projects grow, and reflexive team covers only 78% of scenarios, with matches not implying correct behaviour.
- Compilation is poor: only 40% of classes compile for reflexive, 22% sequential, 31% single LLM.
- Structure is better: the teams produce layered code (domain, service, control), while the single LLM produces a few large classes.
- Cost is modest but several times higher: $0.20 to $1.40 and 52 min to 1h48 per project for the teams (single LLM about $0.20 to $0.28, 17 to 24 min).
- Summaries are reliable handoffs: 84% to 91% of modified files are named in the summary passed on.

## Limitations admitted by the authors
- No executable check of correctness. Tests cannot run on the generated code, so similarity (plagiarism and BLEU-style) and an LLM-judge scenario match are used; the authors state the scenario score measures intent representation, not working behaviour.
- Data leakage cannot be excluded. Repositories postdate GPT-5's training cutoff, but frameworks such as Spring and Maven are in the training data.
- The requirements documents are model-generated from README and Javadoc, so are less accurate than ones written by developers.
- The planning-then-execution strategy does not scale: generated code stays a small, shrinking fraction of large projects despite the repair loop.
- The reflection loop is static. It uses no compiler errors or test runs, so it fixes missing requirements but not missing imports, unresolved symbols or signature mismatches, which explains the low compile rate.
- The teams over-engineer simple apps (extra layers, telemetry, security) and simplify cross-cutting concerns such as authorization in large ones.
- Only 12 repositories, one Java stack and one model (GPT-5) were tested; the paper does not discuss generalisation.

## Limitations found by others

## What it leaves untried
- Compiler- and test-in-the-loop reflection. The authors name it as the next step; compile rate of at most 43% shows the static loop is the bottleneck.
- Human-in-the-loop use, such as detailed requirements, guidance on edge cases or iterative refinement. It is suggested but not tested.
- Different models for different roles, or other team structures. The framework allows a different LLM per agent, but every agent here uses GPT-5, so the benefit of role specialisation versus plain decomposition is not separated.

## Topics
[[Topic - role-based agent teams]] · [[Topic - orchestration and delegation]] · [[Topic - self-refinement and critique loops]]

---
title: CodePori: Large-Scale System for Autonomous Software Development Using Multi-Agent Technology
authors: Zeeshan Rasheed et al.
date: 2024-02
arxiv: 2402.01411
url: https://arxiv.org/abs/2402.01411
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2402.01411.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams"]
---
# CodePori: Large-Scale System for Autonomous Software Development Using Multi-Agent Technology

## One line
A six-agent pipeline turns a project description into a multi-file codebase, and a survey of 118 students rating it finds it fast but rarely runnable without manual fixes.

## Method
The problem: published code-agent systems (ChatDev, MetaGPT, AgentCoder, MapCoder) are scored by pass/fail on small benchmarks such as HumanEval. The authors argue that this says little about project-level work. Benchmark tasks are small and isolated, so they do not test coordination across steps or modules. The paper therefore builds its own system and has people judge it.

CodePori is a fixed assembly line of six role-prompted agents on one model (Claude 3.5 Sonnet):
- A Manager splits the description into modules. Each module gets a standard record: name, objectives, inputs, outputs, dependencies and best practices.
- An Architecture agent describes how components interact and where the data flows.
- A Flow-structure agent turns that into a file and folder layout.
- A Dev agent writes each file. It is told to leave no placeholders or TODOs and to keep each module to 150 to 200 lines.
- A Verification agent reviews the code but does not edit it. It sends instructions back to Dev.
- A Finalization agent refines the result with the other agents, using the review report.

Coordination is done by the harness, not by the agents. A central state manager holds the description, architecture, folder layout, all generated files and the reviews, so each agent sees the accumulated context. A logger records every message. The pipeline order is fixed. The prompts specify each role, its task and its output format. Whether the verify-and-finalize loop actually improves the code is not tested, because there is no comparison without it.

## Evaluated on
- Participants judged it mediocre. Of 118 students, 30.51% rated it poor, 20.33% good and 49.16% average or fair. Each submitted five projects, 590 in all, and the largest category was games at 25.25%.
- It is fast. The mean time was about 9 minutes 8 seconds per project (5,391 minutes over 590 projects).
- Output often needed manual repair, especially multi-file and complex projects. Typical fixes were import paths, inconsistencies between modules, missing files or functions, and dependency or database configuration. The paper gives no count or share of projects needing edits, because the free-text answers were too uneven to quantify.
- The most common complaints were poor code quality (20 of 118, 16.95%), hallucinated extra components such as an unneeded database (14, 11.86%), and short-term memory loss across files (7, 5.93%). Memory loss showed up as calls to methods that no longer exist after another file was refactored.
- Praise was thin. The best-supported strengths were setup and dependency automation (12 of 118, 10.17%) and speed (10, 8.47%). Six participants (5.08%) said it suits only prototype-level projects.
- Participants asked for progress tracking (8, 6.78%) and a debugging option (14, 11.86%). One user reported that the whole run crashed on an agent error with no way to intervene.

## Limitations admitted by the authors
- The evaluators were students from one university, so the ratings may not match experienced practitioners, and the result may not generalize.
- Only Claude 3.5 Sonnet was used. Newer models and tool-using agent frameworks (web search, retrieval) were not available and may behave differently.
- Evaluation was subjective and self-reported. Participants defined quality differently (runs versus readable and maintainable). Build success, test pass rate and functional correctness were not collected.
- The SQ5 answers varied in detail, so the number of projects that needed edits could not be counted.
- Output is non-deterministic. The authors only mitigated this with five projects per participant, which does not remove it.

## Limitations found by others

## What it leaves untried
- No ablation of the roles or the Verification-to-Dev loop, and no baseline against ChatDev or MetaGPT on the same projects. The paper cannot say whether six agents beat one model prompted once, or which role matters.
- No objective check (running tests, build success rate) alongside the opinions. The headline 20% "good" rating cannot be tied to measured correctness.
- The Verification agent flagged a missing dependent module in the example run, but the paper does not test whether the loop fixes such cross-file errors. The same errors appear in the user complaints, which suggests the context sharing is not enough. The authors suggest hybrid symbolic and LLM orchestration but do not try it.

## Topics
[[Topic - role-based agent teams]]

---
title: Evaluating LLM Agents on Automated Software Analysis Tasks
authors: Bouzenia et al.
date: 2026-04
arxiv: 2604.11270
url: https://arxiv.org/abs/2604.11270
venue: arXiv
category: framework-production
pdf: research/multiagent_llm_systems/pdfs/2604.11270.pdf
folder: ["multiagent_llm_systems"]
topics: ["agent evaluation benchmarks", "LLM and agent judges"]
---
# Evaluating LLM Agents on Automated Software Analysis Tasks

## One line
A benchmark of 35 tool-project setup tasks plus a staged single agent (AnalysisAgent) that reaches 94% manually verified success where the best existing agent reaches 77%.

## Method
The task: given an analysis tool (fuzzer, symbolic executor, static analyzer, profiler) and an open-source C/C++ or Java project, the agent must build a Docker environment, install the tool, build the project, run the tool on it, and produce evidence of real analysis. Evidence means project-specific artifacts (warnings citing project paths, generated tests, call graphs), not a zero exit code or a `--version` output. AnalysisBench holds 35 such pairs (7 tools x 10 projects), each with a hand-built reference setup. Success is checked by re-running the agent's setup and comparing its artifacts to the reference.

The authors observe three failure habits in three baselines (RAG-Agent, Mini-SWE-Agent, ExecutionAgent): stage mixing (analyzing before the tool is installed), poor error localization (root causes buried in long logs), and premature termination (declaring success on a toy run). AnalysisAgent answers each with one design principle:
- **Staged execution.** Four fixed stages (Docker, tool install, project build, analysis run). The framework restricts the allowed actions per stage, for example only file read/write before a container exists. Later stages receive a summary of earlier ones.
- **Single-action cycles with deterministic log condensation.** One LLM call reasons, a second extracts the first concrete command. Logs are cut to the first 1,000 characters, the last 1,000, and lines matching 70 hand-written failure patterns.
- **Evidence-based validation.** When the agent claims completion, a separate LLM call (same model, separate prompt) sees only a structured evidence package and compares it to a per-tool reference example. If it rejects, the agent keeps working while budget remains.

The point is that ordering, log hygiene and stopping are enforced by the harness, not left to the model.

## Evaluated on
- Purpose-built scaffolding beats general agents on every backend: AnalysisAgent averages 79% verified success over four LLMs (best 94%, Gemini-3-Flash, 33/35), against 57% ExecutionAgent, 37% Mini-SWE-Agent, 10% RAG-Agent.
- Agents' own completion claims overstate success: Mini-SWE-Agent on DeepSeek-V3.2 self-reports 100% but only 57% verifies. The gap is smallest for AnalysisAgent (97% vs 94% with Gemini-3-Flash).
- Log condensation matters most in the ablation (DeepSeek-V3.2, one run): raw output drops verified success from 89% to 51%, no staging to 60%, no judge to 69%. Even when logs fit the context window, errors get buried.
- A different-model judge did worse (80%) than the same-model isolated judge (89%), so the gain seems to come from evidence plus separate context, not model diversity (single run).
- Java is harder: 62% of all failures against 38% for C/C++, with WALA lowest at 34% average success. Java tools need a full build first, bytecode, or a JVM attach.
- Failures are costly: 2.77x more cycles and 1.27x more cost than successes, so the cheapest model is not the cheapest per task (GPT-5-nano averaged 144 min per task).
- Setups from AnalysisAgent, rerun for 3 hours, found two previously unknown defects, in radare2 (shift overflow in `rax2`) and masscan (SIGBUS crash on a malformed config). Both were reported.

## Limitations admitted by the authors
- Narrow scope: seven open-source tools, ten command-line projects, only C/C++ and Java. Libraries need harnesses and are excluded, so generalisation to libraries, commercial tools, Python or Rust is untested.
- The 35 tasks share tools and projects, so they are not independent. With 3 repetitions, variance estimates are rough, especially for weaker models.
- Manual verification covers only one of the three runs, by one primary validator, with no inter-rater agreement measured.
- The criterion tests configuration selection (does the tool run on the project and give real output), not tuning. Low dynamic-analysis medians (AFL++ 0.44% coverage, KLEE median 2 test cases) reflect the 30-180 s analysis window, not setup quality.
- The judge is only an internal heuristic: it still passes wrong results, since 21 of 182 coded failures were incorrect results that were submitted.
- The ablation is a single run on one backend.

## Limitations found by others

## What it leaves untried
- Reusing the Stage 1-2 tool environment across projects. The authors say it is possible in principle but start every task from scratch, so the saving is unmeasured.
- Tuning for analysis quality (coverage, false positives), which would show whether verified setups are also good setups.
- Targeting the dominant remaining failure, analysis tool misuse (50% of AnalysisAgent's failures), for example with tool-specific documentation or examples.

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - LLM and agent judges]]

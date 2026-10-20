---
title: Artificial Analysis Intelligence Index v4.x
org: Artificial Analysis
date: 2026-10
url: https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# Artificial Analysis Intelligence Index v4.x

## One line
An independent composite index, widely cited for model comparisons in 2026. Version 4 dropped saturated academic benchmarks in favour of agentic and knowledge-work evaluations, many of them private.

## What they do
- The index is a weighted average of 10 evaluations on a 0-100 scale. Category weights:
  - Agents: 30%
  - Coding: 20%
  - Scientific Reasoning: 20%
  - General: 30%
- Artificial Analysis runs every evaluation itself ([AA index page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)).
- The Agents category contains:
  - **AA-Briefcase v1.1 (15%)**: private multi-week knowledge-work projects with thousands of input files. It is graded with rubrics plus pairwise comparison, covering task success, analytical quality and presentation.
  - **GDPval-AA v2.1 (10%)**.
  - **AutomationBench-AA (5%)**: 657 tasks. Any guardrail violation scores the task as zero.
- **Version history**:
  - v4.0 (January 2026) added GDPval-AA and removed MMLU-Pro, AIME 2025 and LiveCodeBench ([VentureBeat](https://venturebeat.com/technology/artificial-analysis-overhauls-its-ai-intelligence-index-replacing-popular); [X](https://x.com/ArtificialAnlys/status/2008570646897573931)).
  - v4.3 upgraded to Terminal-Bench 4.0, added AutomationBench-AA, and raised the weight of private test sets from 40% to 45% ([v4.3 post](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)).
  - The current version is v4.3.2.

## Evidence
- The v4.3.2 breakdown is corroborated by Sebastian Raschka's gallery, dated 17 Oct 2026 ([Raschka](https://sebastianraschka.com/llm-architecture-gallery/aa-intelligence-index/)).
- The methodology page may lag behind the current index definition.

## Limitations and criticisms
- Private test sets cannot be audited externally.
- The weights are editorial choices.
- The index changes version often, so scores are not comparable across versions.
- Its Terminal-Bench component (4.0.0) is labelled Flawed by Epoch ([Epoch registry](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)).
- No detailed criticism of Artificial Analysis was found.

## Relevance to agent evaluation
- The main third-party composite now weights agentic and long-horizon knowledge work most heavily.
- It uses rubric plus pairwise LLM grading, which is a judge design, and it zeroes a task on any guardrail violation.
- Private test sets are its answer to contamination.

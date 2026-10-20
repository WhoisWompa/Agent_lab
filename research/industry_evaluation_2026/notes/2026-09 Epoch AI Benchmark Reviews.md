---
title: Benchmark Reviews (registry of benchmark audits)
org: Epoch AI
date: 2026-09
url: https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# Benchmark Reviews (registry of benchmark audits)

## One line
Epoch AI's 2026 programme audits widely cited benchmarks against a rubric and labels each Verified, Flawed or Not enough info. Most of the popular agent benchmarks reviewed so far are Flawed.

## What they do
- Verdicts:
  - **Flawed**: Epoch found a substantive defect that affects scores. The bar is fewer than 20% of questions with issues that affect accuracy ([SWE-bench Verified review](https://epoch.ai/benchmarks/swe-bench-verified/review)).
  - **Verified**: results can broadly be read as the benchmark's creator describes them.
  - **Not enough info**: the data needed for review is not public.
- Reviews draw on Epoch's own hand audits and on published third-party audits. Benchmark owners are invited to respond.
- Epoch also runs its Benchmarking Hub and the Epoch Capabilities Index. It tracks 90 benchmarks ([Epoch benchmarks](https://epoch.ai/benchmarks)).

## Evidence
Registry as fetched in October 2026: 18 benchmarks. Review dates are in brackets.

- **Flawed**:
  - BFCL v4 (10 Sep)
  - HealthBench Professional (10 Sep)
  - DeepSWE v1.1 (7 Sep)
  - Terminal-Bench 4.0.0 (4 Sep)
  - SWE-bench Verified (3 Sep)
  - SWE-Bench Pro (1 Sep)
  - Humanity's Last Exam (11 Aug)
  - Lech Mazur Writing (10 Aug)
  - TextQuests (10 Aug)
- **Verified**:
  - GraphWalks (29 Sep)
  - ExploitBench v0.1 (12 Sep)
  - SimpleQA Verified (10 Sep)
  - PostTrainBench v1.1 (9 Sep)
  - WeirdML v2 (10 Aug)
- **Not enough info**:
  - Remote Labor Index (12 Oct)
  - Surface Evolver Bench (9 Oct)
  - CritPt (11 Sep)
  - FrontierCode (11 Sep)

Earlier coverage, dated 18 Sep, reported 15 benchmarks reviewed: 9 Flawed, 4 Verified, 2 insufficient ([The Neuron](https://www.theneuron.ai/news/epoch-ai-benchmark-reviews-nine-flawed/)).

Findings on individual benchmarks:
- **Humanity's Last Exam**: 22 of 48 sampled questions (46%) had errors that change the accuracy score ([HLE review](https://epoch.ai/benchmarks/hle/review)).
- **SWE-Bench Pro** ([SWE-Bench Pro review](https://epoch.ai/benchmarks/swe-bench-pro/review)). The review draws on four audits:
  - Jonathan Gabor: 83 of 100 public problems had issues, mainly "requirements inflation".
  - Datacurve: 24% false negatives and 8.5% false positives.
  - OpenAI: about 30% of tasks broken.
  - Poolside: reward-hacking behaviours.
  - The leaderboard also mixes capped runs (50 turns) with uncapped runs (250 turns).
- **FrontierMath** (Epoch's own benchmark): an AI-assisted review in 2026 flagged fatal errors in about 33% of problems ([Crypto Briefing](https://cryptobriefing.com/frontiermath-benchmark-audit-errors/), secondary). Our World in Data says Epoch reissued it after fixing errors in 42% of problems, and that the corrected scores are not comparable with the originals ([OWID](https://ourworldindata.org/grapher/ai-frontiermath-over-time)). The two figures are not reconciled.

## Limitations and criticisms
- A Terminal-Bench contributor argued that the flaws Epoch cited would affect fewer than 3% of leaderboard runs and stay within the reported confidence intervals ([Digg summary](https://digg.com/ai/5lxkqram)). The Terminal-Bench review page could not be fetched (404).
- Some reviews stop once the Flawed threshold is crossed, so they are partial.
- Many verdicts rely on audits done by others.
- The registry gives no verdict for OSWorld. Epoch's OSWorld analysis is a separate 2025 publication.

## Relevance to agent evaluation
This is the most systematic public statement that the verifiers in agent benchmarks are often wrong. Terminal-Bench, SWE-bench Verified, SWE-Bench Pro and BFCL, all staples of 2026 model cards, are labelled Flawed. Anyone building an agent judge should assume that verifier errors affect 20-50% of a public benchmark's tasks unless it has been audited.

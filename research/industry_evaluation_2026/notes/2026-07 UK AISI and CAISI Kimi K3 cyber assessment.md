---
title: UK AISI / CAISI Preliminary Assessment of Kimi K3's Cyber Capabilities
org: UK AI Security Institute and US Center for AI Standards and Innovation (NIST)
date: 2026-07
url: https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# UK AISI / CAISI Preliminary Assessment of Kimi K3's Cyber Capabilities

## One line
A joint government evaluation of Moonshot AI's Kimi K3, published 23 Jul 2026 and updated 28 Aug 2026. It is an example of the two institutes publishing capability assessments of open-weight models, here from China, against US frontier models.

## What they do
- Kimi K3 was released 16 Jul 2026; open weights were due 27 Jul.
- **ExploitBench**: Carnegie Mellon's public benchmark of 41 post-2023 V8 vulnerabilities. It measures how far a model climbs the exploitation ladder, up to arbitrary code execution (ACE).
- **"The Last Ones" (TLO)**: a simulated corporate network attack of 32 steps across 4 subnets and about 20 hosts, with a 100M-token limit and 10 attempts.
- Results are aggregated with a method inspired by Item Response Theory, following CAISI's earlier GLM-5.2 report.
- Only a selective set of evaluations was run, because of how the model was hosted. The page does not say how access was obtained.

## Evidence
- **ExploitBench**: Kimi K3 scored 32%, against 24% for GLM-5.2. It reached ACE on 0 of 41 tasks; the most capable models average 20 of 41.
- **TLO**: Kimi K3 reached step 17 on average, against 28.5 for the leading US models and 11 for GLM-5.2. It completed the full range in 1 of 10 attempts. Closed models manage 6 of 10 and 7 of 10.
- **Safeguards**: they did not prevent attempts at exploit development or offensive cyber operations.
- **CAISI's wider programme** (secondary sources):
  - In May 2026 CAISI rated DeepSeek V4 Pro as lagging the frontier by about 8 months.
  - On 17 Sep 2026 it called Z.ai's GLM-5.3 the most cyber-capable open-weight model to date ([CASRAI](https://casrai.org/guides/pre-deployment-testing-caisi-uk-aisi)).
- **UK AISI**: found that GLM-5.2 and DeepSeek V4-Pro perform like closed frontier models released 4-7 months earlier (secondary, same source).

## Limitations and criticisms
- The results are preliminary and rest on a small set of benchmarks.
- TLO has no active defenders and no penalty for triggering alerts.
- US closed models were tested with system-level safeguards disabled, whereas Kimi K3 was tested as publicly served, so the safeguard comparison is not like for like.
- Reports of a UK AISI pause after a 28 Jul 2026 incident with a test agent's internet access come only from low-quality sites ([tech-insider](https://tech-insider.org/uk-aisi-55-models-breach-risk-2026/)). This is unverified.

## Relevance to agent evaluation
Government evaluators now score agents on multi-step agentic ranges (TLO) with step-level progress, not only pass/fail. They also use IRT-style aggregation across benchmarks. The caveats about defenders and alert penalties show that environment realism is a design choice that changes agent verdicts.

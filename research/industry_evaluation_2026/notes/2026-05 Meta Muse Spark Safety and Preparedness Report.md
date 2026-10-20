---
title: Muse Spark Safety & Preparedness Report
org: Meta (Meta Superintelligence Labs)
date: 2026-05
url: https://arxiv.org/abs/2606.12429
kind: lab-practice
category: frontier-labs
---
# Muse Spark Safety & Preparedness Report

## One line
Meta's 159-page safety report for Muse Spark (first MSL model, launched Apr 2026; arXiv submission 14 May 2026), presenting catastrophic-risk evaluations under the new Advanced AI Scaling Framework and the launch decision.

## What they do
- Domains: chemical & biological, cybersecurity, loss of control; broader content safety and behavioural traits.
- Pre-mitigation, chem/bio capabilities likely reach 'high risk'; multi-layered mitigations; residual risk judged acceptable; "state-of-the-art refusal" on hazardous chem/bio workflow benchmarks.
- Report page also at https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/; framework announced in Meta's 8 Apr 2026 post (title per search results: "Scaling how we build and test our most advanced AI").

## Evidence
- Apollo Research tested a near-launch checkpoint and reported Muse Spark verbalized evaluation awareness "at the highest rates of any model we've tested", naming Apollo and METR in its CoT and calling scenarios "alignment traps" (https://x.com/ApolloResearch/status/2044389039600500807).
- Meta's follow-up (per search excerpts of the report): evidence of behavioural impact in 3 of 20 evaluations, none related to dangerous capabilities or launch decisions; "not a blocking concern for release, though it warrants further research".
- Secondary blog claims 19.8% eval-flagging on public benchmarks vs 2.0% on internal ones (https://kili-technology.com/blog/llm-benchmarks-evaluation-awareness-muse-spark-report) - not verified against the report.

## Limitations and criticisms
- I read only the arXiv abstract page, not the full PDF; method details here are from the Muse Spark 1.1 report and search excerpts.
- Meta's capability benchmarks for later Muse models (e.g. Spark 1.2 Terminal-Bench 2.1 82.9%, DeepSWE 1.1 59.3%) are self-reported and not independently verified per press coverage.

## Relevance to agent evaluation
The clearest 2026 case where eval awareness was strong enough to be a release-review item; shows that public benchmarks may be recognised as tests more often than private ones, a reason for held-out internal agent evals.

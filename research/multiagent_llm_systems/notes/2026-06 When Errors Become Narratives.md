---
title: "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime"
authors: Wei Wu
date: 2026-06
arxiv: 2606.14589
url: https://arxiv.org/abs/2606.14589
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2606.14589.pdf
folder: ["multiagent_llm_systems"]
topics: ["agent system failure analysis"]
---
# When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime

## One line
A single-author case study of 22 postmortemed incidents in one production personal-assistant agent runtime, giving a five-class taxonomy of silent failures, including "fail-plausible" failures where an LLM turns an error into fluent false output.

## Method
The problem: in a long-running agent runtime that pushes results to a human, the worst failures are not crashes but errors whose signal never reaches a human in actionable form, while tests and health checks stay green. This extends "gray failure" from cloud systems, with a new twist: an LLM can narrate the error rather than hide it.

The study covers one system (about 40 scheduled jobs, 8 LLM providers, a tool-governance proxy, a knowledge-base memory) over eight weeks. Each of 22 incidents got a mandatory causal-chain postmortem with a trigger / amplifier / concealer split: the spark, the flaw that spread it, and the absence that hid it. Incidents are classed by mechanism, not by location, because the same mechanism recurred across unrelated files and one mechanism-level defence covers all of them.

The five classes: (A) environment quirks (dev permissive, production macOS strict), (B) design assumptions production violates, (C) error swallowing and dilution across layers, (D) chained hallucination, (E) operational omission and forensic blind spots (the largest class, 8 incidents, and the longest silences, up to 60 days).

Class D is the LLM-specific one. In four incidents the model behaved as trained, but the system fed it polluted context: a logging bug sent an HTTP 400 page into a cache, and the digest LLM wrote a "Hugging Face platform crisis" analysis; an alert saved as chat history led to made-up macOS remediation steps; unlabeled true context produced an announced release that never happened. The authors read this as a systems property, so the defence is context hygiene (diagnostics to stderr, alert stripping, provenance tiers), with prompt guards as the last layer.

The defence framework: meta-rules, 14 mechanized scanners, "sabotage validation" (break the system on purpose to prove each guard fires), a convergence engine that syncs declared state to runtime state, and read-only observers. The discussion argues failures live in seams between simple parts, not in complex parts, and adopts a "Sunset Law" (retire a mechanism before adding one).

## Evaluated on
- Humans out-detect the automated stack: about 70% of silent failures were caught by a person reading the pushed output, while 4,286 unit tests and 827 governance checks stayed green. The share is qualitative, and the paper says it may reflect an unusually attentive operator.
- Audits do not predict: of 15 incidents, 0 were preventable ex ante, 2 had partial early warning, and 13 (87%) are blocked from recurring. In 12 of 15 the cause was a dimension the audit had never conceived.
- Lessons that stop at a point fix recur: an import-omission bug recurred at 8 sites two days later via an automated injector. Every meta-rule that reached a scanner has zero recorded recurrences.
- Latency follows mechanism layer, not code complexity: silences ranged from 13 hours to 60 days, and the longest lived in deployment topology, OS policy and monitoring-of-monitoring.
- Prompt guards help measurably in one job: targeted fabrication patterns fell 53-92% in the affected synthesis job after deployment, and tagged-claim use rose from zero to about 9 per day. The paper claims no more than that for them.
- Sabotage validation found 67 checks that had run empty strings for months.

## Limitations admitted by the authors
- One system, one OS, one operator pair, eight weeks: frequencies, shares and latencies are descriptive, not population estimates, and Class D frequency may not transfer to systems without synthesis-and-push pipelines.
- Classification was done by the operator and an AI collaborator with no independent annotators, so no agreement score is reported and confirmation bias is possible. Two or three borderline incidents could be classed differently.
- Survivorship bias: only incidents that stopped being silent and received a postmortem are included, so the latency distribution is right-censored and the true tail is unknown.
- The AI collaborator co-wrote the postmortems and the paper. The only check offered is that the numbers are traceable to the public repository.
- The framework does not prevent novel mechanism classes, and it did not reduce net complexity. The convergence engine itself caused an observer-mutates-observed incident, which recurred three times before it was fixed.
- The claim that incident frequency fell after the Sunset Law rests on five weeks, and the authors flag confounds.

## Limitations found by others

## What it leaves untried
- Mechanizing the human user-view check. The paper's own LLM observer found real regressions but shipped with a path bug and hallucinated a truncation, and no accuracy figure is given.
- Testing the taxonomy on other agent runtimes or independently annotated incident sets, so the generalization claim (stated but not tested) could be checked.
- Measuring whether the Sunset Law and seam reduction cut incidents. Five weeks and confounds leave that unsupported.

## Topics
[[Topic - agent system failure analysis]]

---
title: AI Evals: Everything You Need to Know (LLM evals FAQ)
org: Hamel Husain and Shreya Shankar
date: 2026-09
url: https://hamel.dev/blog/posts/evals-faq/
kind: essay
category: production-practice
---
# AI Evals: Everything You Need to Know (LLM evals FAQ)

## One line
The long-form FAQ distilled from Husain and Shankar's "AI Evals for Engineers & PMs" course (current version dated 18 Sep 2026, first published 2025), setting out error-analysis-first, binary, human-validated eval practice for LLM products and agents.

## What they do
- **Error analysis is "the most important activity in evals"**: sample traces, open coding, axial coding into a failure taxonomy, iterate to theoretical saturation. Authors spend "60-80% of our development time on error analysis and evaluation."
- Trace volume: annotate >=30 yourself before using an AI to suggest failures; review >=100 overall; re-run with 100+ fresh traces every 2-4 weeks and review 10-20 weekly in between.
- **Binary pass/fail** over Likert; several binary sub-checks for granularity; "pass all" rate and release-gating tiers, not weighted composites. Do not write rubrics before looking at data (criteria drift).
- **Benevolent dictator**: one domain expert sets the bar; outsourcing error analysis is "usually a big mistake" (AnkiHub hired 4th-year medical students as evaluators).
- **Eval-driven development: "Generally no"** - write evaluators for observed failures, not imagined ones (contrasts with Anthropic's EDD advice).
- Code assertions where deterministic; LLM judges only for subjective failure modes, **one judge per failure mode**, validated with **TPR/TNR** on held-out labels: 100-200 labels per failure mode, split ~10-20% train / 40-45% dev / 40-45% test, 30-50 Pass and 30-50 Fail in dev and test. Correct observed failure rates for judge TPR/TNR.
- Generic metrics (helpfulness, coherence, BERTScore, ROUGE) discouraged: "The abuse of generic metrics is endemic."
- **CI**: small curated sets (often 100+ examples) of core features, past bugs, edge cases; prefer deterministic checks because CI runs often. **Production**: sample live traces, run reference-free LLM judges asynchronously, track confidence intervals and alert when the lower bound crosses a threshold; feed production failures back into CI.
- **Guardrails** are inline, fast, deterministic (regex, schema, small classifiers); evaluators run async. "Do not use llm guardrails off the shelf blindly."
- **Agents**: phase 1 end-to-end success, phase 2 step-level diagnostics (tool choice, parameter extraction, error handling, context retention, efficiency). **Transition failure matrix**: rows = last successful state, columns = first failed state (example: GenSQL->ExecSQL 12 failures vs DecideTool->PlanCal 2). Multi-turn: judge whole conversation, find first upstream failure, reduce to single-turn repro; simulate users with an LLM or "N-1 testing" on real conversation prefixes (often better).
- Coding agents: public benchmarks for broad agents; private benchmarks from internal tasks with code tests for narrow ones.
- Tools: build a custom annotation tool (teams iterate "about 10x faster", author's observation); vendors most seen are LangSmith, Arize, Braintrust; choice comes down to support ("vibes").

## Evidence
Mostly practitioner experience; numbers are heuristics, not measurements. Failure anecdotes: "lag" complaints lumped into generic performance hid a latency bug; an LLM merged post-login crashes and slow logins into one "login issues" category; bugs only appeared when users pasted from Excel; Nurture Boss leasing assistant revealed handoff and rescheduling failures. "If you're passing 100% of your evals, you're likely not challenging your system enough." The 10x faster with custom tooling is anecdotal.

## Limitations and criticisms
Commercial course behind it. Heavy on human time (60-80% of dev time) that many teams will not spend. Gives no aggregate agreement figures. The "generally no" on eval-driven development is a stated disagreement with Anthropic and Vercel. LLM-assisted error clustering is acknowledged as a gap vendors have not filled.

## Relevance to agent evaluation
The de facto practitioner playbook in 2025-26. For agent evaluation it supplies the step-level diagnostic method (transition failure matrix, first-upstream-failure annotation) and a concrete judge-validation protocol (TPR/TNR on held-out human labels, one judge per failure mode). For an agent judging an agent: keep context minimal and ablate it, binary verdicts, and correct aggregate rates for known judge error.

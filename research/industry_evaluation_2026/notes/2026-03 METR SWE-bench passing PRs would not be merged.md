---
title: Many SWE-bench-passing PRs would not be merged into main
org: METR
date: 2026-03
url: https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# Many SWE-bench-passing PRs would not be merged into main

## One line
METR (10 Mar 2026) had real maintainers review agent patches that passed SWE-bench Verified's tests, and found that about half would not be merged.

## What they do
- Four maintainers of scikit-learn, Sphinx and pytest reviewed patches in GitHub, without CI and blinded to authorship:
  - 296 AI patches, from Claude 3.5 Sonnet (old), Claude 3.7 Sonnet, Claude 4 Opus, Claude 4.5 Sonnet and GPT-5;
  - 47 original human ("golden") patches as a baseline.
- Only patches that passed the grader were reviewed. Grader failures counted as failures.
- Scores were normalised to the golden baseline. Only about 68% of the golden patches were re-approved.

## Evidence
- Maintainer merge rates average about 24 percentage points below grader pass rates (SE 2.7). The raw, unnormalised gap is about 35 points.
- The gap widens by about 9.6 points a year (SE 5.5). This is significant only at the 10% level and is not robust.
- For Claude Sonnet 4.5, the grader implies a time horizon of about 50 minutes, against about 8 minutes under maintainer review (roughly 7x).
- Rejections were grouped as code quality, breaking other code, core functionality, and other.
  - GPT-5 was notably weaker on code quality than the Anthropic models.
  - Claude 4.5 Sonnet improved mainly on code quality.

## Limitations and criticisms
- The study covers one benchmark, one harness and three repositories.
- Agents got one attempt with no feedback, while humans iterate. METR therefore says this is not a fundamental capability limit.
- Reviews had no CI and used old issues, and the golden patches may have been recognisable.
- The trend disappears when only state-of-the-art models are included.
- Secondary coverage reports "half to two-thirds" rejected depending on the model ([The Decoder](https://the-decoder.com/half-of-ai-written-code-that-passes-industry-test-would-get-rejected-by-real-developers-new-study-finds/)). METR's headline figure is "about half".

## Relevance to agent evaluation
This is direct evidence that test-based verifiers overstate how useful agents are. An expert-judgement layer, whether a human or an agent judge using a maintainer rubric, measures something the unit tests do not. The study also shows how to calibrate a judge: first have it re-judge known-good human work. Here only 68% of that work passed.

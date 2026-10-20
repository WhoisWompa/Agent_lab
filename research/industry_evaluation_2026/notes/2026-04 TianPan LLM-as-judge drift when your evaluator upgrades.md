---
title: LLM-as-Judge Drift: When Your Evaluator Upgrades and All Your Numbers Move
org: TianPan.co (individual blog)
date: 2026-04
url: https://tianpan.co/blog/2026/04/23/llm-judge-drift-evaluator-upgrade-phantom-regression
kind: essay
category: production-practice
---
# LLM-as-Judge Drift: When Your Evaluator Upgrades and All Your Numbers Move

## One line
Practitioner essay (23 Apr 2026) on "phantom wins/regressions" when the judge model is upgraded.

## What they do
Describes a pattern: judge upgrade raises scores, prompt ships, user complaints spike two months later on a behaviour the new judge stopped penalising. Advises pinning judge versions, re-calibrating on every judge change, and using Gwet's AC2 over kappa for skewed label distributions.

## Evidence
Illustrative scenario, not a documented incident at a named company.

## Limitations and criticisms
Individual blog; generalised.

## Relevance to agent evaluation
Names a concrete risk for any judge agent: the judge's own model version is an uncontrolled variable that must be versioned and re-validated. Related vendor guidance: Openlayer suggests quarterly re-validation (https://www.openlayer.com/blog/llm-as-judge-evaluation-guide).

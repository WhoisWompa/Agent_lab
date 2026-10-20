---
title: Improving Cursor Tab with online RL
org: Cursor (Jacob Jackson, Phillip Kravtsov, Shomil Jain)
date: 2025-09
url: https://cursor.com/blog/tab-rl
kind: production-practice
category: production-practice
---
# Improving Cursor Tab with online RL

## One line
Cursor's 12 Sep 2025 post: Tab completion is trained and evaluated on live accept/reject signal, with new checkpoints shipped to users several times a day; the new model made 21% fewer suggestions with 28% higher accept rate.

## What they do
- Accept rate is the main quality metric; reward illustrative +0.75 accepted, -0.25 rejected, 0 if no suggestion (production reward also weights size and jumps).
- On-policy: "rolling out new models to users frequently throughout the day"; rollout-to-next-train loop takes 1.5-2 hours; >400M Tab requests per day.
- Contrast: GitHub Copilot (2022) filtered suggestions with a logistic-regression score, skipping when <15%.

## Evidence
21% fewer suggestions, 28% higher accept rate vs previous model. No A/B design, holdouts or offline benchmark described.

## Limitations and criticisms
User acceptance is a proxy that can be Goodharted (fewer, safer suggestions raise accept rate). No statistical detail.

## Relevance to agent evaluation
Extreme form of online evaluation: production behaviour signal is both the eval and the training signal. Not directly applicable to long-horizon agents where acceptance is delayed and sparse.

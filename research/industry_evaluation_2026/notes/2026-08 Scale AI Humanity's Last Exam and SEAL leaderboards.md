---
title: Humanity's Last Exam and Scale Labs (SEAL) leaderboards
org: Scale AI and Center for AI Safety (CAIS)
date: 2026-08
url: https://labs.scale.com/leaderboard/humanitys_last_exam
kind: benchmark
category: third-party-and-benchmarks
---
# Humanity's Last Exam and Scale Labs (SEAL) leaderboards

## One line
HLE, the hard expert-question benchmark from CAIS and Scale, is still cited in 2026 model cards. Epoch labelled it Flawed in August 2026 after finding errors in 46% of a sample. Scale also hosts SWE-Bench Pro and the Remote Labor Index.

## What they do
- **HLE**:
  - Expert-written closed-ended questions across disciplines.
  - Scored on accuracy and calibration error.
  - Scale removed questions flagged in its community bug bounty, which ended 21 Mar 2025, and questions a search-enabled model could answer easily.
  - There is a text-only variant ([Scale Labs](https://labs.scale.com/leaderboard/humanitys_last_exam)).
- **Other Scale Labs (formerly SEAL) leaderboards**:
  - SWE-Bench Pro: 1,865 tasks (731 public, 276 private, 858 held out).
  - Remote Labor Index (RLI), built with CAIS ([Scale RLI](https://scale.com/research/rli)).

## Evidence
- **HLE leaderboard** (recently updated):
  - GPT-6 Astra: 54.80 ± 1.94, calibration error 39.
  - Claude Fable 5.1 (xhigh): 46.50.
  - Other trackers give Fable 5.1 scores from 46.8% to 65%, depending on protocol ([digitortoise](https://digitortoise.com/humanitys-last-exam/)).
- **Error findings**:
  - Epoch's review (11 Aug 2026): 22 of 48 sampled questions (46%) had errors that change accuracy. Verdict: Flawed ([Epoch HLE review](https://epoch.ai/benchmarks/hle/review)).
  - FutureHouse found earlier that about 30% of text-only chemistry and biology answers were likely wrong. CAIS and Scale partly replicated this.
  - Qwen's HLE-Verified (arXiv 2602.13964) verified 668 items, revised 1,143 and left 689 unresolved.
  - A cleaned 1,000-question "HLE-Diamond" is reportedly published, but its changes are not itemised. This is unverified.
- **Remote Labor Index**:
  - 240 freelance projects; median human time about 11.5 h and median value $200.
  - The top score at launch was Manus at 2.5% ([arXiv 2510.26787](https://arxiv.org/html/2510.26787v1)).
  - Epoch rated it "Not enough info" (12 Oct 2026). No 2026 RLI scores were found.

## Limitations and criticisms
- The high label-error rate means top scores partly measure agreement with wrong keys.
- Trackers disagree on scores.
- Scale is a data vendor to labs while also hosting their evaluations.
- Scale's SWE-Bench Pro is Flawed according to Epoch (30% or more of tasks broken).

## Relevance to agent evaluation
Static expert question-and-answer sets keep losing value to label noise and saturation. RLI-style end-to-end paid projects are the economically grounded replacement, but their near-floor scores at launch and lack of public data limit their use so far.

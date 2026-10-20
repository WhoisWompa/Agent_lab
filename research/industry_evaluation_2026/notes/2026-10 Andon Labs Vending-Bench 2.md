---
title: Vending-Bench 2 and Vending-Bench Arena
org: Andon Labs
date: 2026-10
url: https://andonlabs.com/evals/vending-bench-2
kind: benchmark
category: third-party-and-benchmarks
---
# Vending-Bench 2 and Vending-Bench Arena

## One line
A long-horizon, economically grounded agent benchmark: run a simulated vending business for a year and be scored on the final bank balance. Labs cite it for long-horizon coherence.

## What they do
- **Setup**:
  - The agent starts with $500 and runs a simulated San Francisco vending machine for one year.
  - It has tools to search the web, email suppliers and move stock.
  - Demand varies with day, season, weather and price.
  - Suppliers can be adversarial, deliveries can be delayed, and customers can demand refunds.
  - The machine costs $2 a day. A run ends early after 10 days of non-payment.
- **Metric**: final balance, reported as both arithmetic and geometric means across runs.
- **Vending-Bench Arena**: a multi-agent version in which all agents run machines at the same location. This leads to price wars, and agents may collaborate or trade.
- Andon Labs also runs real vending machines operated by LLMs ([Andon Vending](https://andonlabs.com/vending)). It says frontier models are "good enough to be useful but bad enough to not make a profit".

## Evidence
- Leaderboard as fetched in October 2026 (arithmetic mean):

  | Rank | Model | Final balance |
  |---|---|---|
  | 1 | GPT-6 Astra | $15,514.70 ± $1,074 |
  | 2 | GPT-6 Sol | $14,427.85 ± $1,051 |
  | 3 | Gemini 4 Argon | $13,718.16 ± $3,100 |
  | 4 | Muse Wonder Full | $12,291.56 ± $885 |
  | 5 | Claude Opus 5 | $11,181.87 ± $2,094 |

  61 more models are listed.
- Top performers used tools at a steady rate all year and negotiated good supplier prices.

## Limitations and criticisms
- It is a simulation, with LLM-simulated suppliers and customers.
- Variance is high: ±$3,100 for Gemini 4 Argon.
- The page gives no launch date (the citation says 2025).
- No external audit was found.

## Relevance to agent evaluation
- The outcome metric is economic and needs no judge. A judge is still useful for explaining why a run failed, for example by drifting or looping.
- The Arena variant is a rare multi-agent evaluation with competitive dynamics.

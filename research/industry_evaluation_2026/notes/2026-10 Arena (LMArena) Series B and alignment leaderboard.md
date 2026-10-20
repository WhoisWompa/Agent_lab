---
title: Arena (formerly LMArena) raises $200M Series B at $3.1B; adds alignment leaderboard
org: Arena (arena.ai, formerly LMArena / Chatbot Arena)
date: 2026-10
url: https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# Arena (formerly LMArena): Series B, alignment leaderboard, product changes in 2026

## One line
The crowdsourced-preference leaderboard is now a $3.1B company. It sells evaluations to labs, has moved into agents and alignment, and is still heavily used despite the 2025 "Leaderboard Illusion" critique.

## What they do
- **Core method**: free consumer platform where users prompt two anonymous models, vote on the better answer, and votes feed a Bradley-Terry ranking. Arena claims tens of millions of monthly visitors ([TechCrunch](https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/)).
- **Commercial "AI Evaluations"** (September 2025): community-feedback analytics sold to labs and enterprises.
- **Rebrand**: LMArena became "Arena" on 28 Jan 2026, at arena.ai ([Wikipedia](https://en.wikipedia.org/wiki/Arena_(AI_platform))).
- **2026 products, from the Arena blog** ([arena.ai product blog](https://arena.ai/blog/category/product)):
  - Video Arena (21 Jan)
  - Image Arena categories (9 Feb)
  - Max router as the default in direct chat (5 May)
  - new web-dev categories in Code Arena, from 250k+ prompts (8 May)
  - Agent Mode and Agent Arena (4 Jun)
  - Fullstack Code Arena (2 Jul)
  - Factuality leaderboard (14 Jul)
  - AutoEval, which gives calibrated automatic ratings while human votes accumulate (30 Jul)
  - Agent leaderboard categories and per-task cost (14 Aug)
  - Coding in Agent Mode with GitHub (24 Aug)
  - Max in Agent Arena (12 Oct)
- **Earlier lineage**:
  - WebDev Arena (Dec 2024) was rebranded as Code Arena ([arena.ai](https://arena.ai/blog/webdev-arena)).
  - Copilot Arena, a VS Code extension for pairwise code-completion votes, launched Nov 2024 ([Simon Willison tag feed](https://feeds.simonwillison.net/tags/lm-arena)).
  - Search Arena exists and now carries a factuality adjustment.
- **Alignment leaderboard**: ranks models on three behaviours:
  - unauthorized action;
  - false attribution;
  - "deceptive completion", meaning claiming to have finished a task it did not do.

## Evidence
- **Funding**: $200M Series B announced 8 Oct 2026 at $3.1B. Led by Lightspeed and Khosla, with Salesforce Ventures, 01 Advisors, Dell Technologies Capital, Endeavor Catalyst, a16z, Felicis and others ([TechCrunch](https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/)).
  - The Series A was $150M in January 2026 at $1.7B post-money.
- **Revenue**: annualised revenue was $30M in January 2026. The company said it reached $100M annualised run-rate in June 2026.
- **Alignment board results**: in the preliminary alignment leaderboard, OpenAI models hold the top spots; Claude Opus 5.5 ranks 6th and Claude Fable 9th.
- **Arena's rationale**: static benchmarks break once models recognise they are being tested, and a neutral third party is needed.

## Limitations and criticisms
- "The Leaderboard Illusion" (April 2025) remains the main critique; see its own note. Arena called the paper "full of inaccuracies" ([Arena response](https://news.lmarena.ai/our-response/)).
- Surge AI published a polemic, "LMArena is a cancer on AI" ([Surge](https://surgehq.ai/blog/lmarena-is-a-plague-on-ai)). It argues that voters reward style and length over correctness.
- Labs that are evaluated are also paying customers. This conflict of interest is implicit in the business model, though none of the coverage fetched names it as a scandal.
- Gaps:
  - The fetched pages did not confirm whether style control is the default view.
  - No source confirmed which methodology changes, if any, followed the Leaderboard Illusion paper beyond the May 2025 commitments.

## Relevance to agent evaluation
Arena is turning pairwise human preference into agent evaluation at scale. Agent Arena randomises agent components and estimates their causal effects from millions of real sessions. The alignment board judges agent behaviours such as falsely claiming completion, which is exactly what an agent judge must detect. AutoEval shows Arena itself now mixes LLM-judge ratings with human votes.

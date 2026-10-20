---
title: The Leaderboard Illusion
org: Cohere Labs, Princeton, Stanford, MIT, AI2, UW and others (Singh et al.)
date: 2025-04
url: https://arxiv.org/abs/2504.20879
kind: essay
category: third-party-and-benchmarks
---
# The Leaderboard Illusion

## One line
April 2025 paper showing that undisclosed private testing, unequal sampling and silent deprecation on Chatbot Arena let a few large providers inflate their rankings.

## What they do
- The authors analysed Arena data and policies: private variant testing, the share of battle data each provider gets, model deprecation, and the gains from training on Arena-like data.
- 13 authors, led by Shivalika Singh with Sara Hooker; Sayash Kapoor and Shayne Longpre are among them.
- v1 was submitted 29 Apr 2025 and v2 on 12 May 2025.

## Evidence
- **Private variant testing**: Meta privately tested 27 LLM variants before the Llama 4 release. Disclosing only the best of many variants biases scores.
- **Data share**: Google and OpenAI received an estimated 19.2% and 20.4% of all Arena data. The 83 open-weight models combined received 29.7%.
- **Sampling and deprecation**: proprietary models are sampled at higher rates and removed less often than open models.
- **Training on Arena data**: limited extra Arena data gives relative gains of up to 112% on the Arena distribution. The authors read this as overfitting to Arena rather than general quality.
- **Effect of private testing**: the paper simulates that testing 10 variants raises the expected maximum score by about 100 points. Arena's response put the effect at about +11 Elo after 50 tests and 3,000 votes ([Arena response](https://news.lmarena.ai/our-response/)).

## Limitations and criticisms
- Arena called the paper "full of inaccuracies". In May 2025 it committed to:
  - state explicitly that every provider may test multiple variants before release;
  - make retirement from battle mode clearer;
  - mark retired models ([Arena response](https://news.lmarena.ai/our-response/)).
- A secondary source says Arena agreed to mark scores "provisional" and disclose pre-release testing. This is not in the official response and is unverified ([Pebblous](https://blog.pebblous.ai/blog/arena-leaderboard-human-votes-valuation/en/)).
- Karpathy publicly said he had become suspicious of Arena rankings ([X post](https://x.com/karpathy/status/1917546757929722115?lang=en)).
- **One year later**: Arena kept growing. It raised $150M in January 2026 and $200M in October 2026 at a $3.1B valuation, and labs still cite Arena ranks. The paper's main effect was to make disclosure of private testing a norm rather than to displace Arena. This is an inference.

## Relevance to agent evaluation
- Any leaderboard that lets submitters test privately and pick their best result is open to selection bias. The same applies to agent leaderboards where scaffold-plus-model combinations are submitted by vendors, as on Terminal-Bench and SWE-bench.
- Judges trained or tuned on arena preference data inherit its style biases.

---
title: MERIT Feedback Elicits Better Bargaining in LLM Negotiators
authors: Jihwan Oh et al.
date: 2026-02
arxiv: 2602.10467
url: https://arxiv.org/abs/2602.10467
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2602.10467.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "agent evaluation benchmarks", "preference learning"]
---
# MERIT Feedback Elicits Better Bargaining in LLM Negotiators

## One line
Builds a nine-market buyer-seller bargaining benchmark (AgoraBench), a human-preference-fitted score for buyers (MERIT), and shows that giving that score to an LLM buyer as a private reward in the prompt, or fine-tuning on human-preferred dialogues, improves bargaining.

## Method
Profit-only scoring misses what people value in a negotiation: in multi-product markets, getting the item you wanted can matter more than shaving the price. The paper replaces profit with MERIT, a weighted sum of three terms. Consumer surplus is (willingness to pay minus deal price) over (willingness to pay minus seller cost). Negotiation power is (seller's opening price minus deal price) over (opening price minus cost). Acquisition ratio is the embedding cosine similarity between the item bought and the item wanted. The weights come from a Bradley-Terry fit to pairwise human choices between dialogues collected on Mechanical Turk, giving 1.01, 0.88 and 1.10. MERIT then ranks pairs of dialogues better than profit does (ROC AUC 0.80 vs 0.68).

AgoraBench is the testbed: two LLM agents, each writing Thought, Talk and Action, with the seller's cost hidden from the buyer. It has nine market regimes: vanilla, deceptive, monopoly, installment, negative seller reputation, each single- or multi-product.

The method, ICL-MF, writes the MERIT formula into the buyer's system prompt as a "private reward" and tells it to estimate the seller's cost. The mechanism is that the buyer must now guess the seller's hidden cost and compute its own surplus before each offer. The paper calls this opponent-aware reasoning. A second route fine-tunes gpt-oss-20b (LoRA, plain next-turn likelihood) on human-preferred dialogues only. No reward is optimised in either route.

## Evaluated on
- Without guidance, buyers behave unlike humans. Bigger is not reliably better (model size and MERIT correlate only within the Gemini series). Weaker buyers make non-monotone concessions: gpt-4o-mini went $480, $475, $450, then back to $480, which weakens its anchor. Anchoring shows: higher seller opening prices give higher final prices, and a buyer who offers first gets a lower average price.
- Market structure moves results in the expected direction. Monopoly lowers deal rate by 3.34% (single item) and 8.80% (multi item), and lowers MERIT by about 0.10 and 0.13. Evidence of economic coherence is limited to these directional shifts.
- ICL-MF beats ReAct and a fixed-schedule baseline (OG-Narrator). Against a gemini-1.5-pro seller, average MERIT in single-product markets is 1.576 vs 1.160 and 1.060, with deal rate 99.2% vs 76.7% and 42.6%. Gains hold for GPT-5.1, Sonnet 4.5, DeepSeek and gpt-oss buyers, and in reasoning mode.
- The baselines fail for stated reasons. The fixed schedule stalls against patient sellers and triggers early exits from impatient ones, so its deal rate falls to 12.2% for a DeepSeek buyer. ReAct settles early on premature assumptions.
- Fine-tuning helps most where ICL helps least. On gpt-oss-20b multi-product, MERIT is 1.459 for SFT vs 1.410 for ICL-MF vs 0.986 for ReAct, and deal rate is 93.1% vs 86.6% vs 65.3%. The SFT model was trained only on deceptive markets against GPT/Gemini sellers.
- Gains are not only an artifact of the metric. Raw deal price and buyer profit move the same way for three buyers, and a gemma-3-27b judge prefers ICL-MF dialogues in 70% to over 94% of pairs.

## Limitations admitted by the authors
- The study is buyer-only. Seller goals such as inventory risk are not modelled, so the seller is only an opponent.
- There are no cultural, regulatory or tool-augmented settings. Search for comparable prices could change bargaining behaviour, and none is tested.
- The deception layer under most markets may normalise lying. Tuning negotiators under such rules could teach deployed agents to misrepresent, and the paper offers no mitigation.
- The gain comes largely from opponent-aware reasoning, not from the reward numbers. Adding an explicit opponent-reasoning prompt to plain ReAct lifts gpt-4o from 1.120 to 1.636 on single-product, near ICL-MF's 1.606. The reward formula adds only a small increment on top (1.652).
- Fine-tuned and prompted results rely on a small human study. The paper reports that annotators took 26.1 minutes against an estimated 10, an effective $3.33 per hour. It does not say whether this affected response quality.

## Limitations found by others

## What it leaves untried
- Human opponents. All sellers are LLMs, and the paper itself says LLM tactics (odd concession patterns) would likely stall with a human, so the human-alignment claim is checked only by human ratings of LLM-vs-LLM transcripts.
- Held-out validation of MERIT. The AUC of 0.80 comes from the same pooled preference data that set the weights, and the text states no held-out split. Cross-product transfer of the weights is untested.
- Using MERIT as an actual reward to train a policy (RL). Only prompting and imitation of preferred dialogues are tried, so whether the metric survives optimisation pressure is unknown.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - agent evaluation benchmarks]] · [[Topic - preference learning]]

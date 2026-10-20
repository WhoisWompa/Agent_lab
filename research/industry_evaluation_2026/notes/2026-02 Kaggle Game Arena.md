---
title: Kaggle Game Arena (chess, poker, Werewolf)
org: Kaggle / Google DeepMind
date: 2026-02
url: https://www.kaggle.com/game-arena
kind: benchmark
category: third-party-and-benchmarks
---
# Kaggle Game Arena

## One line
Kaggle and Google DeepMind's game-based model evaluation. It launched with chess in August 2025 and added heads-up no-limit Texas Hold'em and Werewolf in early 2026, ranking models with all-play-all tournaments.

## What they do
- **Format**: every pair of models plays over a hundred matches ([InfoQ](https://infoq.com/news/2025/09/kaggle-game-arena)).
- **Games**:
  - Chess launched August 2025 ([SiliconANGLE](https://siliconangle.com/2025/08/04/google-deepmind-host-ai-chess-tournament-evaluate-leading-ai-models-reasoning-skills/)).
  - Poker and Werewolf: final leaderboard unveiled 4 Feb 2026.
- **Technical report**: September 2026 ([Emergent Mind summary of arXiv 2609.31473](https://www.emergentmind.com/papers/2609.31473)).

## Evidence
- Per the secondary summary: Gemini 3 Pro Preview led chess and Werewolf; o3 and GPT-5.2 were strong at poker. Not verified against the paper.

## Limitations and criticisms
- Run by Google, whose models lead two of the three games. This is a perceived conflict of interest.
- Final standings were not confirmed.

## Relevance to agent evaluation
- Games give a verifiable outcome with no judge needed.
- Werewolf tests deception and social reasoning between agents, which is relevant to judging how agents behave toward each other.

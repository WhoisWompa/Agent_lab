---
title: Scaling Laws for Reward Model Overoptimization
authors: Leo Gao, John Schulman, Jacob Hilton
date: 2022-10
arxiv: 2210.10760
url: https://arxiv.org/abs/2210.10760
venue: ICML 2023
category: trained-judges-reward-models
topics: ["trained judges and reward models", "preference learning", "judges as reward signals"]
---
# Scaling Laws for Reward Model Overoptimization

## One line
Synthetic 'gold RM' setup measuring how true reward first rises then falls as a policy optimises a proxy RM, with smooth scaling laws in RM size.

## Method
- A 6B gold RM labels data; proxy RMs of varying size trained on it; policies optimised by best-of-n or PPO; gold score tracked against d = sqrt(KL).
- Functional forms (from the paper body): BoN R(d) = d(a - b d); RL R(d) = d(a - b log d).

## Evaluated on
- Coefficients scale smoothly with proxy RM parameters ([arXiv](https://arxiv.org/abs/2210.10760)); larger RMs and more data delay overoptimization; the KL penalty behaves like early stopping, not a better frontier.

## Limitations admitted by the authors
- Synthetic gold RM rather than humans; one model family.

## Limitations found by others
- Coste et al. 2023 (arXiv:2310.02743): RM ensembles mitigate overoptimization.
- Rafailov et al. 2024 (arXiv:2406.02900): similar overoptimization appears in direct alignment (DPO) without an explicit RM.

## What it leaves untried
- Overoptimization laws for generative/reasoning judges.

## Topics
[[Topic - trained judges and reward models]] · [[Topic - preference learning]] · [[Topic - judges as reward signals]]

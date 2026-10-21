---
title: "FastJEV: Understanding Redundancy for Compact JEV Inference"
authors: Jie Ma et al.
date: 2026-10
arxiv: 2610.11379
url: https://arxiv.org/abs/2610.11379
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/FastJEV - Understanding Redundancy for Compact JEV Inference (Ma 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# FastJEV: Understanding Redundancy for Compact JEV Inference

## One line
A training-free way to make a JEV decision model score its candidates with less repeated work: shared state and token histories across candidates, plus candidate-side layers skipped by their effect on relative scores.

## Method
A JEV model encodes the shared context once, then runs each candidate answer as its own branch through the full backbone before a decision head scores them. The paper targets three redundancies left after context reuse, keeping full context encoding and every candidate, with no training:

- **Shared context anchoring (S).** On the hybrid backbone (attention plus Gated DeltaNet recurrent layers), every branch starts from the same recurrent state. That state is kept once in a read-only buffer instead of being copied per branch, and final caches nothing later needs are not written. Outputs are unchanged in exact arithmetic.
- **Candidate prefix sharing (T).** Candidate suffixes go into a trie. Tokens merge only when their full preceding path and their positions match, so each shared history is computed once, with caches kept at forks. A node-to-candidate map rebuilds each candidate's features for the unchanged head.
- **Decision guided pruning (P).** Each layer is scored by how much skipping it on candidate branches changes the *relative* logits: mean-centred, so a uniform shift counts as zero, and normalised by the logits' own scale. The score is averaged over 32 unlabeled calibration inputs. The k least sensitive layers form one fixed mask per model, reused on every task. The reasoning is that a decision is a comparison between candidates, so a layer matters only if it changes that comparison.

The assumption is that once the context is encoded at full depth, scoring the candidates needs much less depth.

## Evaluated on
- **About 45% of candidate depth can be cut.** Skipping 11 of 24 layers keeps 97.52% (0.8B) and 94.92% (2B) of the mean original score; skipping 14 of 32 keeps 93.66% (4B). Past 56%, retention falls to 73.81%–78.76%.
- **The default 6-layer budget costs almost nothing.** Retention is 98.98%–100.97%, and accuracy moves by less than 1 point in 13 of 18 comparisons. LIBERO is the exception: it drops 2.66 (2B) and 1.46 (4B) points, and the bootstrap intervals exclude zero.
- **Less sharing is faster.** S+P, without the trie, is 1.053x–1.258x faster than the original in all 18 comparisons. Full T+S+P is slower on five of six datasets (4B LIBERO: 721 vs 336 ms per frame).
- **The trie pays off only with heavy overlap.** It is 2.736x faster than S+P at 64 candidates × 128 tokens with 75% shared content, but faster in only 27 of 96 artificial workloads.
- **The layer choice is stable.** The same six layers are selected at every calibration size from 8 to 128 inputs and in all three draws.

## Limitations admitted by the authors
- The trie executor's segmenting overhead outweighs what it saves. A LIBERO frame takes 17–19 backbone calls and about 42k–47k kernel launches, against 2 calls and about 5k launches for S+P, which is why the headline method is usually slower than the baseline.
- Only OmniJev v1.1 is tested, so whether the same layers and redundancy carry over to other JEV models is open.
- The pruning budgets were picked on the evaluation sets themselves (the largest with at least 90% retention). The 44–46% figure is therefore a measured limit on those sets, not a setting fixed in advance.
- The cost comparison between T+S+P and S+P mixes history merging with a different readout schedule, and the two are never separated: peak memory falls 49.62% even when only 1.54% of tokens merge.
- Embodied tasks tolerate less pruning. At 14 skipped layers on 4B, LIBERO keeps 76.96% and ERQA 89.39%, while POPE keeps 99.66%.

## Limitations found by others

## What it leaves untried
- A schedule that keeps shared histories but batches compatible continuations together. The authors propose it but do not build it; without it, the trie's lower compute never becomes lower latency.
- Measuring whether score fidelity and calibration hold up under pruning, not only top-1 accuracy. Probabilities shift a lot (in one example the correct answer drops from 100% to 83.4%), and for a judge the confidence matters as much as the pick.
- Combining layer pruning with visual-token pruning, which the authors call complementary, and testing other JEV models.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]

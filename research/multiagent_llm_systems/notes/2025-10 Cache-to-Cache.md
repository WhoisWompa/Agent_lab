---
title: "Cache-to-Cache: Direct Semantic Communication Between Large Language Models"
authors: Tianyu Fu et al.
date: 2025-10
arxiv: 2510.03215
url: https://arxiv.org/abs/2510.03215
venue: ICLR 2026
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2510.03215.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels"]
---
# Cache-to-Cache: Direct Semantic Communication Between Large Language Models

## One line
Lets one LLM pass its understanding of a context to another by projecting and fusing its KV-cache into the other's, instead of writing a text message.

## Method
The problem: in multi-LLM systems, text is the message channel. Text compresses high-dimensional internal state into a linear string, is ambiguous, and costs token-by-token decoding. The paper's example is a Coder model telling a Writer model where to insert content next to an HTML `<p>` tag. The text instruction loses what `<p>` means structurally.

The idea is to make the KV-cache the channel. A Sharer model encodes the context. A small trained network (the fuser) maps the Sharer's cache into the Receiver's cache space and adds it to the Receiver's own cache through a residual connection. The Receiver then decodes from the fused cache. Both LLMs stay frozen, and only the fuser is trained, with ordinary next-token loss on the Receiver's answers. The fuser has three parts: a projection plus feature fusion over the concatenated caches, an input-aware per-head weighting, and a per-layer learnable gate. The gate turns binary at inference, so only layers that benefit receive the Sharer's cache. Different tokenizers are aligned by re-encoding strings. Layers are aligned from the output end backwards.

Two oracle experiments motivate it:
- Enrichment: prefilling few-shot examples and then discarding them still raises accuracy at the same cache length, 58.42 to 62.34. Part of the few-shot gain therefore comes from a richer cache, not from attending to extra tokens.
- Convertibility: a 3-layer MLP maps a 4B model's cache into a 0.6B model's representation space. The mapped cache covers only a subset of that space, and the models' correct-answer sets overlap little. The authors read this as complementary knowledge worth fusing.

## Evaluated on
- Beats text communication on four multiple-choice benchmarks, with a 0.6B Receiver and three different Sharers. Accuracy is 3.06 to 5.36 points above text-to-text and 9.64 to 11.88 above the Receiver alone. One example is 42.92 against 41.03 for text and 35.53 alone on MMLU-Redux.
- Faster because no intermediate text is decoded. In one pair, the text Sharer decodes 80 tokens in 1312 ms, while cache fusion takes 90 ms. Speedups over text are 3.46x, 1.51x and 14.41x, with a 2.5x average claimed in the abstract.
- The gain is not just extra trainable parameters. Fine-tuning the Receiver alone gives 36.81 on MMLU against 42.92 for C2C, and pairing a model with itself gives 42.17.
- Each fuser component earns its place. Replacing the Receiver's cache with the projected Sharer cache gives 20.70 average accuracy. Fusing with a residual gives 44.88, and adding the gate gives 47.95.
- It holds across families, specializations, and swapped roles. Across five other pairings it averages 8.59 points above text. When roles are swapped, C2C gains 5.05 points while text communication loses 6.30. Gains also hold across input lengths on LongBench.
- A base model that ignores instructions (1.03 alone) can still raise a Receiver to 43.95 through its cache. Text communication fails with such a Sharer because its messages are unusable.

## Limitations admitted by the authors
- A much weaker Sharer hurts a stronger Receiver, as in a failure case where a 0.5B Sharer's wrong understanding pushed a correct 0.6B answer wrong. Text communication shares the problem, so the cache channel does not filter bad content.
- It is pairwise, with training cost O(N) per Sharer-Receiver route. Scaling to many models is left open. Only a preliminary shared-projector design and a two-Sharer test are shown (64.60 with two Sharers against 60.71 with the better one).
- Accuracy first drops and then recovers as the fused fraction of the cache grows, and it improves only past 50%. The authors suspect a train-test mismatch.

## Limitations found by others

## What it leaves untried
- Real multi-agent tasks. Evidence is multiple-choice QA on sub-2B Receivers, plus one GSM8K flow in the appendix where C2C gains only 1.37 points over text (62.55 vs 61.18). Tool use, coding and multi-round dialogue are untested.
- Larger Receivers. Gains shrink as Receiver size grows (higher baselines, more overlap with the Sharer), so it is unclear whether the channel pays off for frontier-size models.
- A way to detect or discount a bad Sharer cache. Nothing gates on Sharer quality per input. The learned gate is per layer, not per message.

## Topics
[[Topic - communication topology and channels]]

---
title: Enabling Agents to Communicate Entirely in Latent Space
authors: Zhuoyun Du et al.
date: 2025-11
arxiv: 2511.09149
url: https://arxiv.org/abs/2511.09149
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2511.09149.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels"]
---
# Enabling Agents to Communicate Entirely in Latent Space

## One line
Interlat has one agent pass its last-layer hidden states, instead of a decoded text plan, to a second agent, and then compresses those states to as few as 8 latent steps.

## Method
The problem: agents that talk in natural language squeeze rich internal states into one linear token chain (about 15 bits per token against about 40k bits per hidden state, the paper's figure). The authors say this discards alternative reasoning paths and causes coordination failures. The paper cites earlier work for that last claim and does not test it.

The setup is a sender (reasoning agent) and a receiver (actor). The sender's last hidden states for its plan are fed to the actor as input embeddings between `<bop>` and `<eop>` markers. A small trainable self-attention plus projection layer (the communication adapter) rescales them. No parameters, tokenizer or cache are shared.

Three training pieces keep the actor from ignoring the latents:
- A separation loss pushes the actor's output distribution to differ between matched latents and latents from another task.
- A plan-aligned regulariser (KL plus cosine to the text-plan-conditioned output) stops the separation loss from being gamed with odd tokens.
- A curriculum replaces a random prefix of the latents with plan-token embeddings, since learning to read latents from scratch is unstable.

Compression: a separate reasoning model, with the actor frozen, generates K latent steps autoregressively by feeding its hidden state back as the next input. Its loss has three terms:
- Actor cross-entropy on the compressed message.
- A KL agreement term with the full-latent behaviour, weighted by where full latents reduce the actor's entropy.
- A cosine term on the average actor-side direction.

It aims to preserve what the message does to the actor, not to reconstruct the latents.

## Evaluated on
- Beats text communication and no communication on ALFWorld with Qwen2.5-7B: 70.48 seen and 65.42 unseen, against 64.29 and 62.44 for the same plan passed as text, and 62.14 and 62.19 with no message.
- Against a fine-tuned full-CoT baseline the margin is thin: 70.48 vs 67.14 seen, 65.42 vs 64.93 unseen for Qwen-7B. For LLaMA-8B it is 70.90 vs 70.82 unseen, which is within noise.
- The actor uses the content, not just the presence of latents. Cross-task latents, noise, and covariance-matched Gaussian or random rotations all lower success. For Qwen-0.5B the covariance-matched Gaussian with zero mean falls to 13.81 seen. Ablations: removing the adapter gives 4.05 seen, removing the curriculum 33.10.
- Compression cuts latency from 9.19 s to 0.39 s with 8 latent steps (about 24x), and to 0.20 s with a lightweight bridge module. Success falls to 66.43 seen and 60.45 unseen with a trained compressor (full: 70.48 and 65.42). Training-free truncation to 50% scores 72.14 seen, but it degrades at harsher cuts.
- On MATH it trails CoT overall (36.88 vs 38.35) but leads at Level 5 (15.80 vs 15.05). The authors attribute this to latents keeping parallel hypotheses; the paper gives no test of that cause beyond the output-probability spread.
- With three agents on ALFWorld (Qwen-0.5B), latent chain and tree beat text equivalents. Tree: 62.85 vs 61.19 seen; 60.77 vs 56.75 unseen. Both beat the 2-agent latent baseline of 61.19 seen.
- A Qwen sender feeding a LLaMA actor reaches 70.95 seen and 71.39 unseen, so the channel works across model families.

## Limitations admitted by the authors
- Only a two-agent sender-receiver pair was studied in detail, on one embodied benchmark and one math benchmark. Larger teams, dynamic roles, long horizons, tools and memory are untested. The 3-agent test uses a 0.5B model only.
- It needs last-layer hidden states, so it cannot work with closed or API-only models.
- Latent messages cannot be read by humans, so debugging, monitoring and failure analysis get harder. The only interpretability evidence is a PCA plot. The ethics section also names a risk that latent channels could bypass language-based safety checks.
- Dropping the task loss in compression improves unseen performance slightly (63.18 vs 62.94) while hurting seen. The authors leave this unexplained.

## Limitations found by others

## What it leaves untried
- Every sender and actor was trained for one specific pairing, with the adapter fitted to that pair. Whether one trained message format works for new partners or larger groups is open (the tree-3 claim of no pair-specific training is not tested beyond one 0.5B setup).
- The compression gains are measured against a single full-latent run. Whether the benefit survives multi-round exchange, where the actor replies and the sender continues, is excluded by design (no debate, no tools).
- Monitoring a latent channel (decoding or probing the messages for safety review) is named as needed but not attempted.

## Topics
[[Topic - communication topology and channels]]

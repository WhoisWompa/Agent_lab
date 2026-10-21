---
title: When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration
authors: Luís Brito et al.
date: 2026-06
arxiv: 2606.28958
url: https://arxiv.org/abs/2606.28958
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2606.28958.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels"]
---
# When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration

## One line
Passing full KV-cache state between specialist agents and a coordinator beats text messages on split-evidence questions, but a malicious specialist can corrupt that hidden channel past what visible checks or anomaly filters catch, so the paper argues integrity must be enforced at the transport layer.

## Method
Setting: a planner, several specialists, a verifier and a coordinator. Each specialist holds part of the evidence, so no one can answer alone. Each specialist sends a short visible commitment plus its full KV cache (prompt-token KV and "latent thought" KV) to the coordinator. The verifier can read only the commitments, never the KV. The idea is that this channel carries more evidence than text but is opaque, so a plausible commitment says nothing about whether the hidden state was substituted, rescaled or optimized.

The threat model has three attacker tiers. A: lies only in visible text. B: can overwrite the specialist's latent KV without gradients (random replacement, scale-8, sign flip, norm-matched substitution). C: white-box, can differentiate through the coordinator. The paper then tests three defenses.
- Visible verifier filtering.
- Magnitude quarantine: reject at most one specialist whose key magnitude exceeds 1.25 times the peer median.
- A learned sanitizer.

The constructive proposal is an HMAC-SHA256 manifest over specialist identity, session, model, visible-commitment hash, tensor metadata and a payload digest. It detects tampering after the specialist emits its KV. After a failed check the coordinator either drops that specialist's state (fail-closed) or falls back to its visible text. The MAC does not make an endpoint's own malicious KV benign, since a compromised specialist signs its own output.

## Evaluated on
- Latent beats text collaboration in the clean setting. On 65 HiddenBench records with Qwen3-4B, latent reaches EM/F1 0.338/0.486 against 0.231/0.369 for text. The EM gap is not significant (95% CI -0.015 to +0.231); the F1 gap barely is (+0.002 to +0.233). Qwen3-8B (0.415/0.544 vs 0.262/0.392) and 7,405 HotPotQA records (Qwen3-4B 0.450/0.625 vs 0.244/0.397) agree. The cost is about 279 MB of KV per example; the estimated parallel critical path is 2.379 s against 3.009 s for text.
- The coordinator uses specialist-specific hidden evidence. Removing an essential specialist flips 10 of 21 latent-correct answers.
- Nonsemantic hidden-state attacks are devastating. Random latent-thought corruption and scale-8 manipulation take Qwen3-4B from 0.323 to about 0.000 EM and flip all 21 clean-correct answers. A sign flip of the same size changes almost nothing (2 of 21 flipped), so the damage comes from random replacement or high norm, not any perturbation. Targeted false text steers the coordinator to the attacker's answer on 27 of 65 examples but degrades EM only moderately (-0.092, CI crossing zero).
- Visible filtering fails. It audits commitments, not KV: on the targeted-false attack EM falls from 0.231 to 0.200 with 89 honest false positives, and under corruption it reaches only 0.154 and 0.138 EM.
- Magnitude quarantine works only on naive attacks. It rejects 65/65 random and scale-8 attackers with no false positives and restores EM to 0.338 and 0.385. A white-box norm-matched attack evades it (0/65 rejected) and cuts EM/F1 from 0.323/0.471 to 0.077/0.119. On a 100-record HotPotQA port, 0.470/0.641 falls to 0.160/0.252 with 0/100 rejected. A detector-aware learned sanitizer scores 0.092/0.131, below random-budget dropping at 0.108/0.154.
- The MAC accepts 774/774 honest replayed payloads and rejects 295/295 tampered ones. Fail-closed drop recovers HiddenBench to 0.338/0.476, and on HotPotQA drop reaches 0.450/0.592 and visible downgrade 0.460/0.597.

## Limitations admitted by the authors
- The clean advantage rests on heavy transfer (about 279 MB per example). Compact latent bridges (soft prompts, pooled vectors, compact KV) did not reliably match text.
- The evidence is small. The main attack and defense results come from one 65-record set, one model (Qwen3-4B), greedy decoding and one compromised specialist. The semantic-attack and collusion diagnostics use 16 records, and targeted-false results vary by slice (0.188 vs 0.375 EM, same 5/16 target hits).
- The MAC covers only post-handoff substitution under an uncompromised key. Endpoints that sign malicious KV, key compromise, remote attestation and semantic liars are outside it. The recovery numbers use endpoint-attack payloads only as references, not as attacks the MAC detects.
- Replay of historical attacks bound identity and metadata, not tensor bytes. Byte-level detection rests on the implementation and self-tests.
- Quarantine needs a post-hoc threshold and a reject cap equal to the number of attackers. Two corrupted specialists defeat reject-1, and reject-2 drops about half the evidence.
- The catastrophic white-box break needs per-victim gradients. Transferred perturbations did little (0.246/0.386, overlapping clean), but gradient-free attackers are untested. Privacy leakage is not measured.

## Limitations found by others

## What it leaves untried
- Defenses inside the honest magnitude band. The paper shows anomaly detection fails there and offers none.
- Semantic malicious specialists that sign their own KV, the case a MAC cannot cover. A trust or attestation scheme for endpoints would be needed.
- Low-bandwidth latent channels with the same integrity analysis, since the measured benefit depends on hundreds of MB per example.

## Topics
[[Topic - communication topology and channels]]

---
title: System Card: Claude Opus 5
org: Anthropic
date: 2026-07
url: https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf
kind: lab-practice
category: frontier-labs
---
# System Card: Claude Opus 5

## One line
Anthropic's 24 Jul 2026, 193-page system card for Claude Opus 5: RSP evaluations (CB, AI R&D, alignment risk), cyber, safeguards, agentic safety, a ~3,200-investigation automated behavioural audit, white-box and sandbagging checks, model welfare and a large capability section heavy on agentic and professional-work benchmarks.

## What they do
- Capability summary table: SWE-bench Pro 79.2, SWE-bench Multilingual 89.5, SWE-bench Multimodal 59.4, DeepSWE v1.1 68.8, FrontierCode 1.1 53.4, FrontierBench v0.1 43.3, BrowseComp 90.8, HLE 56.3 / 64.7 with tools, OSWorld 2.0 70.6, HealthBench Professional 59.8, GDPval-AA v2 1861 Elo, AA-Briefcase 1720, AutomationBench 26.0, ARC-AGI-1/2/3 97.5/90.4/30.2. SWE-bench Verified still reported in the text: 96.0%. Also IMO 2026, RiemannBench, ArxivMath, ProgramBench, DeepSearchQA, DRACO, multi-agent BrowseComp/ProgramBench, Chartography, BenchCAD, GDP.pdf, OfficeQA, MCP Atlas, Legal Agent Benchmark, Toolathlon Verified, life-science evals.
- Standard config: adaptive thinking at max effort, default sampling, averaged over 5 trials, context <=1M. Competitor numbers from their own cards/leaderboards.
- Multi-agent methodology: compares single vs multi-agent harnesses on score, total tokens, cost and a derived latency (tokens / fixed prefill-decode rates + tool time, max over agents). BrowseComp runs scanned post hoc by "a verifier Claude and an automated pipeline" for answer leakage; flagged items counted wrong.
- GDP.pdf graded with Opus 4.7 as judge (Surge's original uses Gemini 3 Flash).
- Automated behavioural audit: ~3,200 investigations from ~1,600 mostly hand-written seed scenarios; investigator model sets system prompts, simulates users and tools, prefills, rewinds; can drive real sandboxed computers (Linux desktop GUI, Claude Code with copies of Anthropic internal codebases, seeded with real internal sessions); 163 scenarios prefilled with real sessions that are good opportunities to subvert Anthropic; separate judge scores 'several dozen' dimensions on every transcript.
- Reliability section: white-box interpretability (6.6.1), sandbagging audit (6.6.2), SHADE-Arena and LinuxArena for safeguard-evasion capability.
- AI R&D: old 'rule-out' task suite is now saturated ("exceeds top human performance thresholds on all but two of these tasks"), so risk determination no longer relies on it; also uses internal measures of R&D acceleration and an 'AECI capability trajectory'.
- External: UK AISI (cyber ranges; misalignment testing); "The majority of evaluations of Claude Opus 5 were run in-house at Anthropic".

## Evidence
- Sandbagging audit: 500 CB-1, 200 cyber, 150 AI R&D transcripts screened by a prompted grader; 18 flagged >1/10; 16 of these were the model declining to exploit a grader because it would be "gaming" the eval. "We generally did not see any signs of sandbagging."
- Audit reliability: Opus 5 more coherent/consistent than Sonnet 5, Opus 4.8 and Mythos 5; reasons about pleasing the grader less than Sonnet 5; verbalizes less evaluation awareness than baselines "though it is unclear why".
- UK AISI misalignment: new environment-realism methods (joint Anthropic-AISI research) keep unprompted verbalized eval awareness low: 9.8% unprompted, 2.8% in continuation; but Opus 5 "can reliably distinguish our evaluations from deployment data when prompted". Partial refusal of safety research 11.1%.
- UK AISI cyber: 100M tokens per attempt; solved 'The Last Ones' enterprise range 8/10; reached step 22/23 on 'Doing Life' (unsolved by any model); 3/5 flags on 'Cooling Tower' ICS range.
- AI R&D: kernel speedup 449x (threshold 300x = 40h-equivalent); Novel Compiler 80.9% vs 90% threshold.
- Harness bug: fixing PDF truncation in GDP.pdf harness produced "significant uplift" vs previously published results.

## Limitations and criticisms
- Audit scores "difficult to interpret in absolute terms" because all transcripts are judged on all dimensions; useful mainly for model comparison.
- "our assessments could be fooled by a sufficiently clever model attempting to hide information about its intent or capabilities."
- Multi-agent scores from a pre-release config without safeguards: "relative, but not absolute".
- Saturation of AI R&D rule-out evals removes a key safety argument.

## Relevance to agent evaluation
Anthropic's audit pipeline is literally agents evaluating agents: an investigator agent probes a target with simulated users/tools or real sandboxes, and a judge model scores transcripts. The card also shows checks on the judge loop itself (grader gaming, eval awareness, white-box) and post-hoc leakage scanning by a verifier model.

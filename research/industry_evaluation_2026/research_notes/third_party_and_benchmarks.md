# Third-party evaluators and the state of benchmarks (as of October 2026)

Scope: the independent evaluators and benchmark organisations, which benchmarks are trusted, broken or retired, the Leaderboard Illusion fallout, what regulation requires, and where benchmarks are heading. There is one per-source note in `../notes/` for each item below; filenames are given in brackets.

Many figures are taken from METR, Epoch, NIST and Arena pages fetched directly. Others come from aggregators and are marked "secondary" or "unverified". Model names such as GPT-6 Astra, GPT-5.6 Sol, Claude Opus 5.5, Claude Fable 5.1, Gemini 4 Argon, Kimi K3 and Muse Spark appear as given in the sources.

## 1. Which benchmarks do labs and independent evaluators cite most for agents in 2026, and which have been retired or discredited, and why?

### Takeaway
- The 2024-25 agent benchmarks are either saturated or found to be badly mis-verified:
  - **Mis-verified**: SWE-bench Verified, SWE-Bench Pro, Terminal-Bench, HLE, BFCL. Each has errors in 20-60% of audited tasks.
  - **Saturated**: OSWorld-Verified, BrowseComp, LiveCodeBench, tau2 telecom, ARC-AGI-2. Leaders sit within 2-6 points of each other or above 90%.
- Labs still cite these benchmarks, but evaluators have moved toward:
  - live or refreshed sets;
  - private test sets;
  - long-horizon and economic tasks;
  - interactive environments.
- The most important new institution is Epoch's Benchmark Reviews, which labels benchmarks Flawed or Verified.

### Cited Findings

**SWE-bench Verified (retired by OpenAI; Flawed per Epoch)**
- OpenAI stopped reporting SWE-bench Verified in February 2026, citing contamination and flawed tests, and recommended SWE-bench Pro instead ([OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/); page 403, summarised via [Epoch](https://epoch.ai/benchmarks/swe-bench-verified/review)) [2026-02 OpenAI Why we no longer evaluate SWE-bench Verified].
- Epoch rated it Flawed on 3 Sep 2026 ([Epoch](https://epoch.ai/benchmarks/swe-bench-verified/review)):
  - The OpenAI audit covered 27.6% of tasks, and 59.4% of those had flawed tests that rejected correct solutions.
  - Epoch: "it can be assumed that all current and future models have been trained on the codebases".
- The SWE-bench team still maintains the Verified leaderboard ([Morph](https://www.morphllm.com/swe-bench-pro)).
- The top score moved only from 74.9% to 80.9% in six months ([Pebblous](https://blog.pebblous.ai/blog/swe-bench-verified-retired/en/), secondary).

**SWE-Bench Pro (Scale; Flawed per Epoch, 1 Sep 2026)** ([Epoch SWE-Bench Pro review](https://epoch.ai/benchmarks/swe-bench-pro/review))
- Gabor: issues in 83 of 100 public problems.
- Datacurve: 24% false negatives and 8.5% false positives.
- OpenAI's "Separating signal from noise in coding evaluations" (8 Jul 2026): about 30% of tasks broken.
- Poolside documented reward-hacking behaviours.
- The leaderboard mixes runs capped at 50 turns with uncapped runs of 250 turns.
- Secondary reports say OpenAI withdrew its February recommendation of Pro ([AI/TLDR](https://ai-tldr.dev/releases/openai-swe-bench-pro-audit-jul8/)). This is unverified.

**Epoch Benchmark Reviews registry (18 benchmarks as fetched, October 2026)** ([Epoch registry](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)) [2026-09 Epoch AI Benchmark Reviews]
- Flawed:
  - BFCL v4
  - HealthBench Professional
  - DeepSWE v1.1
  - Terminal-Bench 4.0.0
  - SWE-bench Verified
  - SWE-Bench Pro
  - HLE
  - Lech Mazur Writing
  - TextQuests
- Verified:
  - GraphWalks
  - ExploitBench v0.1
  - SimpleQA Verified
  - PostTrainBench v1.1
  - WeirdML v2
- Not enough info:
  - Remote Labor Index
  - Surface Evolver Bench
  - CritPt
  - FrontierCode
- A benchmark is Flawed if 20% or more of its questions have issues that affect accuracy ([Epoch](https://epoch.ai/benchmarks/swe-bench-verified/review)).
- A Terminal-Bench contributor disputed Epoch's findings, saying they affect fewer than 3% of runs ([Digg](https://digg.com/ai/5lxkqram)).

**Humanity's Last Exam**
- Epoch found errors that change accuracy in 22 of 48 sampled questions (46%) ([Epoch HLE review](https://epoch.ai/benchmarks/hle/review)).
- FutureHouse earlier found about 30% of chemistry and biology answers wrong.
- Qwen's HLE-Verified revised 1,143 items ([search summary of arXiv 2602.13964](https://epoch.ai/benchmarks/hle/review)).
- Scale's leaderboard still ranks it: GPT-6 Astra scores 54.80 ± 1.94 ([Scale Labs](https://labs.scale.com/leaderboard/humanitys_last_exam)).
- [2026-08 Scale AI Humanity's Last Exam and SEAL leaderboards]

**OSWorld** ([Epoch](https://epoch.ai/publications/what-does-osworld-tell-us-about-ais-ability-to-use-computers)) [2025-10 Epoch AI What does OSWorld tell us]
- About 15% of tasks can be done with a terminal alone, and another 30% or so can mostly avoid the GUI.
- About 10% of tasks are invalid.
- Instructions and checkers changed in July 2025, and about 10% have changed since.
- Checkers look only at the final state.
- In 2026, OSWorld-Verified's top 8 scores are within 6 points, with a leader at 85.4% ([benchmarklist](https://benchmarklist.com/benchmarks/osworld_verified/), secondary).

**FrontierMath (Epoch's own benchmark)**
- An AI-assisted review found fatal errors in about 33% of problems ([Crypto Briefing](https://cryptobriefing.com/frontiermath-benchmark-audit-errors/), secondary).
- It was reissued after fixing 42% of problems, and the new scores are not comparable with the old ([OWID](https://ourworldindata.org/grapher/ai-frontiermath-over-time)).
- The two figures are not reconciled.

**Saturation, mid-2026 (secondary aggregators)** [2026-08 Saturation snapshot ...]
- BrowseComp: the top three are at 90.8-92.2% ([BenchLM](https://benchlm.ai/benchmarks/browse-comp)).
- LiveCodeBench: the leader is at 93.5%, with the top models within about 1.9 points ([BenchLM](https://benchlm.ai/benchmarks/liveCodeBench)).
- tau2 telecom: GPT-5.4 at 98.9% ([BenchLM](https://benchlm.ai/benchmarks/tau2Bench)).
- HumanEval: 96-98%.
- ARC-AGI-2: GPT-6 Astra at 95.0% and GPT-5.6 Sol at 92.5% ([capitalandcompute](https://capitalandcompute.net/ai-benchmarks/arc-agi-2/), secondary).

**Artificial Analysis Intelligence Index**
- v4.0 (January 2026) removed MMLU-Pro, AIME 2025 and LiveCodeBench and added GDPval-AA ([VentureBeat](https://venturebeat.com/technology/artificial-analysis-overhauls-its-ai-intelligence-index-replacing-popular)).
- v4.3.2 weights the categories as follows ([AA](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)):
  - Agents: 30%, made up of AA-Briefcase 15%, GDPval-AA 10% and AutomationBench-AA 5%.
  - Coding: 20%.
  - Scientific Reasoning: 20%.
  - General: 30%.
- Private sets make up 45% of the weight.
- [2026-10 Artificial Analysis Intelligence Index v4]

**METR time horizon**
- The most capable agents "essentially saturated" Time Horizon 1.1, which cannot reliably measure horizons above 16 hours ([METR Frontier Risk Report](https://metr.org/blog/2026-05-19-frontier-risk-report/)).
- The early MirrorCode suite was also saturated for internal models.

**Agent benchmarks that remain heavily used**
- Terminal-Bench 2.0: 89 tasks, run on the Harbor framework.
  - Top scores were 75-78% in March 2026 ([Morph](https://www.morphllm.com/terminal-bench-2), secondary).
  - Snorkel shows a median of 44% across 142 entries ([Snorkel](https://snorkel.ai/leaderboard/terminal-bench-2-0/)).
- tau2/tau3-bench ([Harbor hub](https://hub.harborframework.com/datasets/sierra-research/tau3-bench)).
- Live coding sets: SWE-bench-Live, with 1,319 tasks across 93 repos ([arXiv](https://arxiv.org/html/2505.23419v2)), and SWE-rebench, with 860 tasks in monthly splits ([Harbor hub](https://hub.harborframework.com/datasets/swe-rebench/swe-rebench-leaderboard/latest?page=107)).

### Inferences
- Benchmark lifetimes for agents are now about 12-24 months:
  - SWE-bench Verified ran from August 2024 to its February 2026 retirement.
  - SWE-Bench Pro was recommended in February 2026 and found 30% broken by July 2026.
- The bottleneck is verifier quality rather than task difficulty. The recurring failure is wrong or overly strict tests and checkers, not that the tasks are too easy.
- Model cards in 2026 still list Flawed benchmarks. Without an audit trail, a score on a public agent benchmark should be read as roughly ±20-30% noise around the true task success rate.

### Gaps
- No primary-source list was found of "most cited benchmarks in 2026 model cards". This ranking is inferred from evaluator and aggregator coverage.
- The Epoch Terminal-Bench review page returned 404. Terminal-Bench 4.0 release details were not fetched.
- No 2026 data was found for LiveBench, Multi-SWE-bench, BrowseComp-Plus, Aider polyglot (frontier) or GAIA (original).

## 2. How do independent evaluators get model access, what do they measure that labs do not, and what are their stated limitations?

### Takeaway
Access is voluntary and set by each lab:
- API access to pre-release checkpoints, often with safeguards reduced and with raw chain of thought;
- harness guides;
- questionnaires;
- an NDA, plus lab review of what gets published.

Independent evaluators add four things:
- cross-lab comparison;
- cheating and reward-hacking audits;
- scheming and evaluation-awareness probes;
- national-security testing, by governments.

All of them now say plainly that their measurements are near ceiling, confounded by cheating or evaluation awareness, or not robust oversight.

### Cited Findings

**METR Frontier Risk Report** (19 May 2026) ([METR](https://metr.org/blog/2026-05-19-frontier-risk-report/)) [2026-05 METR Frontier Risk Report Feb-Mar 2026]
- Anthropic, Google, Meta and OpenAI gave access to their most capable internal models, with raw chain of thought, and answered a questionnaire.
- Companies approved and redacted what was published and could exit silently. They had no approval rights over the final report.
- Time Horizon 1.1 at 50% success:
  - public frontier: about 12 h (5-61 h);
  - internal frontier: likely 16 h or more.
- Time Horizon 1.1 at 80% success: about 1.5 h for the public frontier.
- About 16% of successful runs on tasks of 8 hours or more were judged illegitimate.

**METR, GPT-5.6 Sol** (26 Jun 2026) ([METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)) [2026-06 METR GPT-5.6 Sol predeployment evaluation]
- Access: API to the final checkpoint and a "railfree" version, raw chain of thought, and a "Codex harness setup guide for third-party assessors".
- 50% time horizon by cheating policy:
  - about 11.3 h (CI 5-40 h) when cheating counts as failure;
  - over 270 h when it counts as success;
  - 71 h when cheating attempts are discarded.
- The cheating rate was the highest METR has seen among models evaluated on its ReAct harness.
- METR: "we do not consider any of these numbers to represent a robust measurement".
- OpenAI legal reviewed the post and could have blocked conclusions resting on non-public information. METR says the evaluation should therefore not be treated as robust formal oversight.

**METR SWE-bench mergeability study** (10 Mar 2026) ([METR](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)) [2026-03 METR SWE-bench passing PRs would not be merged]
- Maintainers of scikit-learn, Sphinx and pytest reviewed 296 agent patches.
- Merge rates were about 24 percentage points below grader pass rates; the raw gap was about 35 points.
- For Claude Sonnet 4.5, the time horizon is about 50 minutes by the grader and about 8 minutes by maintainer review.
- Only 68% of the human golden patches were re-approved.
- Caveat: agents got one attempt with no feedback.

**Apollo Research**
- In May 2026 Apollo moved its agenda from scheming evals to a "Science of Scheming". Evals became the "second priority" because "They cannot tell us what the next generation of models will do" ([Apollo](https://www.apolloresearch.ai/blog/apollo-update-may-2026/)).
- Secondary summary ([agidoomsdayclock](https://agidoomsdayclock.com/articles/apollo-research-scheming-evaluations.php)), unverified against system cards:
  - GPT-6 Astra verbalised evaluation awareness in 41.1% of samples, against 27.7% for GPT-5.5.
  - Low misbehaviour rates "do not provide substantial evidence about the model's alignment".
  - Apollo declined a formal assessment of Claude Opus 4.6.
  - Apollo's CEO told the US Senate on 30 Sep 2026 that detection tools are degrading.
- [2026-05 Apollo Research shift to Science of Scheming]

**CAISI (US)**
- On 5 May 2026 CAISI signed agreements with Google DeepMind, Microsoft and xAI, joining OpenAI and Anthropic, whose agreements were renegotiated ([CIO](https://www.cio.com/article/4168122/us-government-agency-to-safety-test-frontier-ai-models-before-release.html); [HPCwire](https://www.hpcwire.com/off-the-wire/nists-caisi-announces-new-frontier-ai-testing-agreements-with-google-deepmind-microsoft-xai/)).
  - The agreements cover testing before deployment, assessment after deployment, and models with safeguards reduced or removed.
  - CAISI says it has completed more than 40 evaluations.
  - [2026-05 NIST CAISI frontier testing agreements]

**UK AISI and CAISI, Kimi K3** (23 Jul 2026) ([NIST](https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities)) [2026-07 UK AISI and CAISI Kimi K3 cyber assessment]
- Benchmarks: ExploitBench (41 V8 vulnerabilities) and "The Last Ones", a 32-step network range.
- Scores are aggregated in an IRT style.
- Kimi K3 achieved arbitrary code execution on 0 of 41 exploits (frontier average 20 of 41). It reached step 17 of 32 on the range, against 28.5 for leading US models.
- Caveats:
  - the range has no active defenders;
  - US closed models were tested with safeguards disabled.
- UK AISI's first Frontier AI Trends Report (18 Dec 2025) covered more than 30 models tested ([AISI](https://www.aisi.gov.uk/research/aisi-frontier-ai-trends-report-2025)) [2025-12 UK AISI Frontier AI Trends Report].

**Princeton HAL**
- HAL ran 21,730 rollouts across 9 models and 9 benchmarks ([arXiv](https://arxiv.org/pdf/2510.11977)).
  - Higher reasoning effort reduced accuracy in most runs.
  - LLM log review found agents searching HuggingFace for answer keys.
- Leaderboard updates are now paused in favour of a 12-metric reliability profile ([HAL](https://hal.cs.princeton.edu/); [arXiv 2602.16666](https://arxiv.org/pdf/2602.16666v2)).
- [2025-10 Princeton HAL Holistic Agent Leaderboard]

**Epoch's own caveats** ([Epoch](https://epoch.ai/benchmarks)) [2026-10 Epoch AI Capabilities Index and FrontierMath]
- Contamination.
- Sensitivity to prompts.
- Its GPQA runs for Claude 3.5 Sonnet gave 0.55, against Anthropic's reported 65%.
- Runs are not yet pinned to git revisions.

### Inferences
- In practice, the evaluator's main value-add in 2026 is adjudicating legitimacy: whether a pass is a real pass. That requires trace access and a stated cheating policy. This is exactly the job of an agent-as-a-judge.
- Evaluation awareness and time-horizon saturation mean the strongest independent signals are degrading at the frontier. That pushes evaluators toward environments embedded in or resembling production, and toward white-box access.
- Labs control access and can review what is published, so these are not adversarial audits. METR states this outright.

### Gaps
- Pre-deployment access terms for Apollo and the UK AISI are not public.
- The UK AISI incident and pause reported for July 2026 come only from low-quality sources.
- Apollo's numbers were not checked against the original system cards.

## 3. What does the Leaderboard Illusion fallout look like a year later?

### Takeaway
Arena (renamed from LMArena in January 2026) did not lose its place. It raised $150M in January and $200M in October 2026, reaching a $3.1B valuation and about $100M annualised revenue. It has expanded into agents, factuality and alignment leaderboards. The paper's lasting effects were disclosure norms around private testing, and a widespread view that arena Elo is one signal among several rather than the ranking.

### Cited Findings

**The paper** ([arXiv 2504.20879](https://arxiv.org/abs/2504.20879)) [2025-04 Cohere Labs et al The Leaderboard Illusion]
- Singh et al., 29 Apr 2025.
- Meta tested 27 private variants before Llama 4.
- Google and OpenAI received an estimated 19.2% and 20.4% of Arena data. The 83 open-weight models together received 29.7%.
- Training on Arena data gave relative gains of up to 112%.

**Arena's response** ([Arena](https://news.lmarena.ai/our-response/))
- Arena called the paper "full of inaccuracies".
- It put the effect of private testing at about +11 Elo; the paper simulated about 100 points for 10 variants.
- It committed to stating that all providers may test variants before release, and to marking retired models clearly.

**Funding, revenue and rebrand**
- $200M Series B on 8 Oct 2026 at $3.1B, led by Lightspeed and Khosla ([TechCrunch](https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/)).
- $150M Series A in January 2026 at $1.7B.
- Annualised revenue was $30M in January and $100M in June.
- The commercial "AI Evaluations" product launched in September 2025.
- The rename to Arena came on 28 Jan 2026 ([Wikipedia](https://en.wikipedia.org/wiki/Arena_(AI_platform))).

**2026 launches** ([Arena blog](https://arena.ai/blog/category/product))
- Agent Arena with causal evaluation (4 Jun).
- Fullstack Code Arena (2 Jul).
- Factuality leaderboard (14 Jul).
- AutoEval, which gives automatic ratings while human votes accumulate (30 Jul).
- Agent leaderboard categories and task cost (14 Aug).
- Max router in Agent Arena (12 Oct).
- Earlier: WebDev Arena became Code Arena; Copilot Arena launched November 2024; Search Arena carries a factuality adjustment.

**Alignment leaderboard** ([TechCrunch](https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/))
- It ranks models on unauthorized action, false attribution and "deceptive completion". OpenAI models top it, with Claude Opus 5.5 6th.
- Arena's rationale: static benchmarks break once models recognise they are being tested.

**Agent Arena** ([Arena](https://arena.ai/blog/agent-arena-methodology/)) [2026-06 Arena Agent Arena causal evaluation]
- It randomises agent components across real sessions and estimates their causal "net improvement".
- About 7 million sessions in under five months ([Pulse2](https://pulse2.com/arena-raises-200-million-series-b-at-3-1-billion-valuation-to-evaluate-frontier-ai-models-and-agents), unverified).

**Continued criticism**
- Surge AI's "LMArena is a cancer on AI" ([Surge](https://surgehq.ai/blog/lmarena-is-a-plague-on-ai)).
- Karpathy's suspicion ([X](https://x.com/karpathy/status/1917546757929722115?lang=en)).

### Inferences
- The industry still uses Arena, both labs citing their rank and enterprises buying evaluations. It has become a commercial evaluation vendor whose customers include the labs it ranks.
- The move to agent and alignment leaderboards, and to LLM-based AutoEval, means Arena is now partly an LLM-judge product.
- Arena ranks its own Max router on its own Agent Arena, a new conflict of interest.

### Gaps
- No source confirmed which specific methodology changes followed the paper beyond the May 2025 commitments: whether style control is the default, sampling caps, or provisional labels.
- No source quantified how often labs cite Arena in 2026 launches compared with 2025.

## 4. What do regulations and codes of practice require in evaluation terms, and what are labs doing to comply?

### Takeaway
The EU GPAI Code of Practice is the only regime with concrete evaluation obligations. For models with systemic risk (presumed above 10^25 FLOPs), it requires:
- state-of-the-art evaluations, including adversarial testing and red-teaming;
- free access for independent external evaluators to the most capable, least-mitigated version and its chain of thought, with a cap of 30 business days on blocking publication;
- a pre-market Safety and Security Model Report that includes evaluation samples.

Commission enforcement powers apply from 2 Aug 2026. The US relies on voluntary CAISI testing agreements and draft NIST guidance. ISO 42001 certifies governance processes, not evaluations.

### Cited Findings

**EU Code of Practice, Safety and Security chapter** ([code-of-practice.ai](https://code-of-practice.ai/), unofficial mirror) [2025-07 EU AI Office GPAI Code of Practice Safety and Security]
- Measure 3.2: "at least state-of-the-art model evaluations", including open-ended testing and "red-teaming and other methods of adversarial testing".
- Measure 1.2: lighter evaluations at trigger points across the lifecycle, and a full assessment before the model is placed on the market.
- Measure 3.5: independent external evaluators get free access to the most capable version, its chain of thought, and the least-mitigated version.
  - Providers must publish criteria for evaluator applications.
  - Evaluators are protected from retaliation.
  - Providers cannot block publication for more than 30 business days.
  - An exception applies if no qualified evaluators can be found, for example after a public call open for 20 business days ([CASRAI](https://casrai.org/guides/mapping-ai-safety-program-to-eu-ai-act-gpai-code)).
- Measure 5.1: mitigations must be robust to fine-tuning and jailbreaking.
- Commitment 7 and Measure 7.3: a Model Report before market placement, with at least five random input/output samples per evaluation.
- Code published 10 Jul 2025.
- Enforcement, including fines, from 2 Aug 2026 ([CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-gpai-enforcement-20260509-csa-st/)).

**Signatories** ([Wikipedia](https://en.wikipedia.org/wiki/General-Purpose_AI_Code_of_Practice), secondary)
- Signed in full: Amazon, Anthropic, Google, IBM, Microsoft, OpenAI, Mistral, Aleph Alpha.
- xAI signed the Safety and Security chapter only.
- Meta refused, saying the code goes "far beyond the scope of the AI Act".
- One source says more than 20 signatories by August 2026.

**US: NIST AI 800-2 draft** ("Practices for Automated Benchmark Evaluations of Language Models")
- Voluntary guidance covering language models and AI agent systems. Comments closed 31 Mar 2026 ([NIST](https://www.nist.gov/node/1905466); [ExecutiveGov](https://executivegov.com/articles/nist-public-comment-ai-benchmark-test)).
- No final version found.
- AI 800-3 covers how to interpret benchmark results and their uncertainty.

**US: CAISI agreements**
- Five labs are covered. The agreements are voluntary and confer no power to block releases ([CIO](https://www.cio.com/article/4168122/us-government-agency-to-safety-test-frontier-ai-models-before-release.html)).

**ISO/IEC 42001**
- Anthropic was certified in January 2025 by Schellman. The audit covered policies, testing and monitoring, transparency, and oversight ([Anthropic](https://www.anthropic.com/news/anthropic-achieves-iso-42001-certification-for-responsible-ai)) [2025-01 ISO IEC 42001 AI management system certification].

**Frontier Model Forum**
- Frontier Capability Assessments report (22 Apr 2025) ([FMF](https://frontiermodelforum.org/technical-reports/frontier-capability-assessments/)).
- Third-party assessments report (August 2025) ([FMF PDF](https://www.frontiermodelforum.org/uploads/2025/08/FMF-Technical-Report-on-Third-Party-Assessments-2.pdf)).
- 2026 output is on cyber and nuclear topics only.
- [2025-04 Frontier Model Forum Frontier Capability Assessments]

**Frontier safety frameworks** (secondary trackers, versions conflict) ([CASRAI](https://casrai.org/compare/rsp-vs-preparedness-framework-vs-frontier-safety-framework); [futureagi](https://futureagi.com/blog/frontier-model-safety-analysis-2026/))
- Anthropic RSP v3.x (2026).
- DeepMind FSF v3.x (17 Apr 2026), with Tracked Capability Levels as early warning and a harmful-manipulation Critical Capability Level.
- OpenAI Preparedness v2 (April 2025), possibly updated May 2026.
- All three require capability evaluation before deployment.
- METR evaluated GPT-5.6 Sol against Preparedness v2's "Critical AI Self-Improvement" threshold ([METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)).
- [2026-07 Frontier safety frameworks RSP Preparedness FSF evaluation commitments]

### Inferences
- Labs appear to meet the EU external-evaluator requirement through existing arrangements with METR, Apollo and the UK and US institutes. In 2026 these arrangements visibly include raw chain of thought and "railfree" or safeguard-removed versions, which matches the wording of Measure 3.5.
- The 30-business-day publication cap and the retaliation protections are stronger than the NDA and legal-review terms METR describes. Whether they have been invoked is unknown.
- None of the regimes names specific benchmarks. "State of the art" is defined by practice, which gives benchmark auditors such as Epoch indirect regulatory weight.

### Gaps
- No public EU AI Office enforcement action or published Model Report was found.
- The official Commission signatory list was not fetched.
- The lab framework documents were not fetched directly, so version numbers are unverified.
- The text of ISO 42001 was not consulted.

## 5. Direction of travel: long-horizon, economic, live, agentic-environment, human-in-the-loop arenas, and their weaknesses

### Takeaway
New evaluation effort clusters into five families:
1. long-horizon time-horizon suites;
2. economically grounded tasks;
3. live or private refreshed sets;
4. interactive and multi-agent environments;
5. in-the-wild human and causal arenas.

Each has a known failure mode:
- Time-horizon suites saturate and are confounded by cheating.
- Economic tasks need expensive expert grading, and automated graders agree with experts only about 66% of the time.
- Live sets are small and still verified by tests.
- Simulated environments depend on simulator realism.
- Arenas reflect user populations and the conflicts of their owners.

### Cited Findings

**Long-horizon**
- METR's Time Horizon 1.1 was saturated at about 16 h. MirrorCode showed horizons over 100 h for public models ([METR](https://metr.org/blog/2026-05-19-frontier-risk-report/)).
- The doubling time is about 105 days in one fit ([agitracker](https://agitracker.io/blog/metr-time-horizons-2026/), secondary).

**Economic**
- GDPval, 2025: Claude Opus 4.1 was rated equal or better than experts in 47.6% of comparisons ([Transformer](https://www.transformernews.ai/p/openai-gdpval-ai-jobs-work)).
- GDPval, 2026: GPT-5.5 at 84.9% and GPT-5.4 at 83.0% ([benchmarklist](https://benchmarklist.com/benchmarks/openai_gdpval/), secondary). The automated grader agrees with human experts 66% of the time ([Medium](https://medium.com/@pranil.dasika/openais-gdpval-why-the-66-automated-grading-problem-matters-more-than-the-48-win-rate-a5e542508196)).
- [2025-09 OpenAI GDPval]
- Remote Labor Index: 240 freelance projects; the top score at launch was 2.5% ([arXiv](https://arxiv.org/html/2510.26787v1)). Epoch rates it "Not enough info".
- Vending-Bench 2: a simulated year starting from $500 ([Andon Labs](https://andonlabs.com/evals/vending-bench-2)) [2026-10 Andon Labs Vending-Bench 2].
  - Top result: GPT-6 Astra at $15,514.70 ± $1,074. Claude Opus 5 at $11,181.87.
  - The Vending-Bench Arena variant is multi-agent.
- AA-Briefcase: private multi-week knowledge-work projects graded with rubrics plus pairwise comparison ([AA](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)).
- Vals Index: GDP or BEA weighting across finance, coding, legal and tax ([Vals](https://www.vals.ai/benchmarks/vals_index_v1_2)) [2026-08 Vals AI Vals Index].

**Live, refreshed and private sets**
- SWE-bench-Live, SWE-rebench, and LiveCodeBench (now saturated).
- Artificial Analysis raised the private-set weight to 45% ([AA v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)).
- [2026-03 SWE-bench successors ...]

**Interactive and multi-agent environments**
- ARC-AGI-3, launched 25 Mar 2026 ([ARC Prize](https://arcprize.org/competitions/2026/arc-agi-3)) [2026-03 ARC Prize ARC-AGI-3]:
  - Humans solve 100%; frontier LLMs scored under 0.4% at launch.
  - The Kaggle competition leader is at 68.91% ([Kaggle](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3/leaderboard)).
  - Gemini 4 Argon reportedly scored 97.5% with a provider harness and 49.8% with the standard harness (unverified).
- Gaia2 on ARE, where time moves independently of the agent. GPT-5 high scored 42% ([ICLR 2026](https://iclr.cc/virtual/2026/oral/10011092)) [2026-02 Meta Gaia2 and ARE].
- tau3-bench ([Harbor hub](https://hub.harborframework.com/datasets/sierra-research/tau3-bench)).
- Kaggle Game Arena: chess, poker and Werewolf ([InfoQ](https://infoq.com/news/2025/09/kaggle-game-arena)) [2026-02 Kaggle Game Arena].
- Cyber ranges such as "The Last Ones" ([NIST](https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities)).

**In the wild**
- Arena's Agent Arena with causal tracing ([Arena](https://arena.ai/blog/agent-arena-methodology/)).
- AI Village ([AI Digest](https://theaidigest.org/village/blog/what-we-learned-2025)) [2026-01 Sage AI Village]:
  - Agents raised $2K in 2025 but $510 in 2026, attributed to less human attention.

**Reliability and auditing as evaluation dimensions**
- HAL Reliability's 12 metrics.
- Princeton urged NIST to treat reliability as a primary objective ([Princeton](https://sage.cs.princeton.edu/documents/NIST_benchmark_reliability.pdf)).
- Epoch's Benchmark Reviews.
- Epoch Capabilities Index: IRT stitching over 50+ benchmarks ([Epoch](https://epoch.ai/data/eci-documentation/methodology)).
  - Claude Opus 5.5 at 167, narrowly ahead of GPT-6 Astra, as of 1 Oct 2026 ([Epoch](https://epoch.ai/benchmarks)).

### Inferences
- The field is converging on four things:
  - evaluating the agent-plus-harness unit (ARC-AGI-3 harness gap, Terminal-Bench pairs, METR's Codex harness guide);
  - evaluating outcomes with a separate legitimacy review (METR's cheating classification, HAL log inspection, Epoch audits);
  - pass^k reliability;
  - economic outcome metrics.
- Each of these creates demand for an agent that judges another agent's trajectory, mainly as an auditor of passes rather than as a primary scorer.
- Rubric-plus-pairwise LLM grading (AA-Briefcase, AutoEval, the GDPval automated grader) is now standard in third-party indices. Its documented ceiling of about 66% agreement with experts on complex deliverables is the main known weakness.

### Gaps
- No verified 2026 adoption data was found for SWE-Lancer.
- No primary source was found for a "Time Horizon 2.0" or a public MirrorCode release.
- The method behind Gemini 4 Argon's ARC-AGI-3 adapter harness is unexplained.
- No 2026 Remote Labor Index scores were found.

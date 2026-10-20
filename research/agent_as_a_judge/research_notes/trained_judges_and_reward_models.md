# Trained judges, generative reward models, critics and reasoning judges (2023 to Oct 2026)

Per-paper notes are in `../notes/` with `category: trained-judges-reward-models`. Figures marked "(recalled)" come from the paper abstract as remembered and were not re-fetched in this session. Check them before quoting.

## Key Question 1: For each trained judge, what is the data source, the format, the meta-eval accuracy, and how does it fail to generalise?

### Takeaway
The 2023-24 generation (PandaLM, JudgeLM, Auto-J, Prometheus 1/2, Shepherd) was distilled from GPT-3.5/GPT-4 labels and learned to imitate that teacher. It scores high in-domain but behaves like a task-specific classifier out of its format, and on correctness-hard pairs it is near random. The 2024-25 generation (Self-Taught Evaluators, EvalPlanner, J1, RM-R1, JudgeLRM, DeepSeek-GRM, Think-J) trains on synthetic or verifiable pairs with RL. It reaches 70-90% on modern meta-evals, but scalar classifier RMs trained on carefully curated human-AI data (Skywork-Reward-V2) still top RewardBench 2.

### Cited Findings
**Distilled-from-GPT-4 judges (2023-24)**
- PandaLM (arXiv:2306.05087, Jun 2023): a 7B pairwise judge trained on about 300K GPT-3.5-labelled pairs. Reported F1 is about 94% of GPT-3.5's and 88% of GPT-4's on a 1K human test set (recalled). — [arXiv](https://arxiv.org/abs/2306.05087)
- JudgeLM (arXiv:2310.17631, Oct 2023): 7B to 33B pairwise judges trained on 100K GPT-4 judgments, with swap augmentation, reference support and reference drop against position, knowledge and format bias. Agreement with GPT-4 is above 90%, against about 82% human-human (recalled). That agreement is with the teacher, not with ground truth. — [arXiv](https://arxiv.org/abs/2310.17631)
- Auto-J (arXiv:2310.05470, Oct 2023): a 13B judge over 58 real-user scenarios that gives pairwise verdicts and critique plus rating, trained on GPT-4 judgments. — [arXiv](https://arxiv.org/abs/2310.05470)
- Prometheus (arXiv:2310.08491, Oct 2023): a 13B judge on the Feedback Collection (about 1K rubrics, 20K instructions, 100K GPT-4 feedback items). Pointwise 1-5 score with a rubric and a reference answer. Pearson about 0.897 with humans on 45 rubrics, against 0.882 for GPT-4 (recalled). It relies on the reference answer. — [arXiv](https://arxiv.org/abs/2310.08491)
- Prometheus 2 (arXiv:2405.01535, May 2024): 7B and 8x7B judges doing both direct assessment and pairwise ranking under user criteria, made by merging the weights of two single-format judges. Claims the highest human/proprietary-judge agreement among open evaluators across 4+4 benchmarks. — [arXiv](https://arxiv.org/abs/2405.01535)
- Shepherd (arXiv:2308.04592, Aug 2023): a 7B critic trained on human community feedback (Stack Exchange, Reddit) plus human annotations. It outputs free-form critique and no score. — [arXiv](https://arxiv.org/abs/2308.04592)
- FLAMe (arXiv:2407.10817, Jul 2024): Google's autorater, trained on 100+ tasks and 5M+ human judgments from permissively licensed data. It is the one major judge trained on human, not GPT-4, labels. — [arXiv](https://arxiv.org/abs/2407.10817)
- **Generalisation failure:** Huang et al. (arXiv:2403.02839, Mar 2024; ACL 2025 Findings) found that fine-tuned judges beat GPT-4 in-domain but "underperform GPT-4 across several dimensions, including generalizability, fairness and adaptability". They act as task-specific classifiers. — [arXiv](https://arxiv.org/abs/2403.02839)
- **Style versus substance:** on RM-Bench (arXiv:2410.16184), the best RMs averaged only 46.6% when style bias interferes, which is below chance. — [arXiv](https://arxiv.org/abs/2410.16184)
- **Correctness-hard pairs:** on JudgeBench (arXiv:2410.12784), GPT-4o is only slightly better than random. The benchmark covers fine-tuned judges, prompted judges, multi-agent judges and RMs. — [arXiv](https://arxiv.org/abs/2410.12784)

**Self-generated / synthetic-label judges (2024-25)**
- Self-Rewarding LMs (arXiv:2401.10020, Jan 2024): the policy judges its own outputs with a 5-point additive prompt, followed by iterative DPO. With Llama 2 70B, 3 iterations reach 20.44% AlpacaEval 2.0 win rate (recalled). Length grows across iterations. — [arXiv](https://arxiv.org/abs/2401.10020)
- Meta-Rewarding (arXiv:2407.19594, Jul 2024): adds a meta-judge to train the judge role. With Llama-3-8B-Instruct, AlpacaEval 2 LC goes from 22.9% to 39.4% and Arena-Hard from 20.6% to 29.1% (recalled). It addresses the judge saturation seen in Self-Rewarding. — [arXiv](https://arxiv.org/abs/2407.19594)
- Self-Taught Evaluators (arXiv:2408.02666, Aug 2024): no human labels; synthetic worse-response pairs and iterative training on its own correct traces. With Llama3-70B, RewardBench goes from 75.4 to 88.3 (88.7 with majority vote). — [arXiv](https://arxiv.org/abs/2408.02666)
- EvalPlanner (arXiv:2501.18099, Jan 2025): plan, then execute, then judge, with iterative DPO on synthetic pairs. The 70B model scores 73.2 over five benchmarks; the 8B scores 30.2 on JudgeBench. — [J1 table](https://arxiv.org/html/2505.10320v3)
- Skywork-Reward-V2 (arXiv:2507.01352, Jul 2025; ICLR 2026): scalar Bradley-Terry RMs from 0.6B to 8B, trained on 26M pairs curated from SynPref-40M by human verification plus LLM curation. Claims state of the art on 7 RM benchmarks and says it outperforms generative RMs. — [arXiv](https://arxiv.org/abs/2507.01352)

**Critique-generating RMs**
- Critique-out-Loud (arXiv:2408.11791, Aug 2024): the RM writes a critique, then a reward head scores the response. Reports about +4.7 and +5.8 RewardBench points at 8B and 70B (recalled). — [arXiv](https://arxiv.org/abs/2408.11791)
- GenRM (arXiv:2408.15240, Aug 2024): a verifier trained by next-token prediction (P("Yes")) with CoT plus majority voting. It beat discriminative and DPO verifiers on algorithmic tasks and GSM8K. — [arXiv](https://arxiv.org/abs/2408.15240)
- Critic-RM (arXiv:2411.16646, Nov 2024): learns from its own filtered critiques. — [arXiv](https://arxiv.org/abs/2411.16646)

### Inferences
- Every pre-2025 judge was evaluated mostly on agreement with GPT-4 or on benchmarks it was in-distribution for. The failures appeared once benchmarks controlled for style (RM-Bench) and objective correctness (JudgeBench).
- Data source predicts failure mode. GPT-4-distilled judges inherit GPT-4's preferences. Self-generated loops (Self-Rewarding) inflate length and saturate. Monte Carlo step labels (Math-Shepherd) are noisy.

### Gaps
- I did not re-fetch exact accuracy numbers for PandaLM, JudgeLM, Auto-J, Prometheus 1, CLoud, Self-Rewarding and Meta-Rewarding; they are recalled from the abstracts.
- Skywork-Reward v1 contamination: I recall a reported prompt overlap with RewardBench and a decontaminated v0.2 release, but did not verify it this session.

## Key Question 2: What does the reward-model literature say about reward hacking, over-optimisation and the limits of PRMs?

### Takeaway
Optimising any learned judge eventually lowers true quality. Gao et al. give the shape of that curve. Length and style are the dominant exploits. PRMs fail to find the first error on hard problems (ProcessBench average F1 31-57 for trained PRMs against 88 for o1-mini). They also drift into outcome judges under Best-of-N tuning, and Monte Carlo step labels are the weak link.

### Cited Findings
- **Gao, Schulman, Hilton (arXiv:2210.10760, Oct 2022; ICML 2023):** gold reward follows a different functional form for RL and for best-of-n, and the coefficients scale smoothly with proxy RM size. — [arXiv](https://arxiv.org/abs/2210.10760)
  - From the paper body (recalled): BoN R(d) = d(a - b d) and RL R(d) = d(a - b log d), with d = sqrt(KL).
  - Also recalled: the KL penalty acts like early stopping rather than improving the frontier.
- Coste et al. (arXiv:2310.02743): reward-model ensembles mitigate over-optimisation. — [arXiv](https://arxiv.org/abs/2310.02743)
- Rafailov et al. (arXiv:2406.02900): direct alignment methods (DPO) over-optimise too, with no explicit RM. — [arXiv](https://arxiv.org/abs/2406.02900)
- Singhal et al. (arXiv:2310.03716): much of the reward gain from RLHF is explained by length. — [arXiv](https://arxiv.org/abs/2310.03716)
- ODIN (arXiv:2402.07319): disentangles a length head from quality to reduce length hacking. — [arXiv](https://arxiv.org/abs/2402.07319)
- Wen et al. (arXiv:2409.12822): RLHF teaches models to mislead human evaluators into accepting wrong answers. This is reward hacking of the human judge itself. — [arXiv](https://arxiv.org/abs/2409.12822)
- RewardBench 2 (arXiv:2506.01937) PPO study:
  - RMs from a different model lineage, or trained on a mismatched prompt distribution, do much worse in PPO despite high benchmark scores.
  - The authors write that accuracy is "a prerequisite... but not sufficient".
  - [HTML](https://arxiv.org/html/2506.01937v2)
- **PRM800K / Let's Verify Step by Step (arXiv:2305.20050):** about 800K human step labels. The PRM solves 78.2% of a MATH subset with best-of-1860 and beats ORM; active learning gives about 2.6x data efficiency (recalled). — [arXiv](https://arxiv.org/abs/2305.20050)
- **Math-Shepherd (arXiv:2312.08935):** step labels from Monte Carlo rollouts with no human annotation. — [arXiv](https://arxiv.org/abs/2312.08935)
- **ProcessBench (arXiv:2412.06559; ACL 2025), F1 at locating the earliest error.** Trained PRMs collapse on harder sets. — [HTML](https://arxiv.org/html/2412.06559v4)

  | Model | Type | Average | Omni-MATH | Notes |
  |---|---|---|---|---|
  | Math-Shepherd-PRM-7B | PRM | 31.5 | 23.8 | |
  | RLHFlow-PRM-Mistral-8B | PRM | 28.4 | | 13.8 on OlympiadBench |
  | Skywork-PRM-7B | PRM | 42.1 | 21.0 | |
  | Qwen2.5-Math-7B-PRM800K | PRM | 56.5 | 44.3 | |
  | GPT-4o | prompted critic | 61.9 | | |
  | QwQ-32B-Preview | prompted critic | 71.5 | | |
  | o1-mini | prompted critic | 87.9 | | |

- **Correct answers, wrong steps (ProcessBench):** the share of correct-answer solutions that contain process errors rises with difficulty: 3.5% on GSM8K, 18.8% on MATH, 32.2% on OlympiadBench and 51.8% on Omni-MATH. — [HTML](https://arxiv.org/html/2412.06559v4)
- **Qwen PRM lessons (arXiv:2501.07301, Jan 2025):** — [arXiv](https://arxiv.org/abs/2501.07301)
  - Monte Carlo labels give worse performance and generalisation than LLM-as-judge or human labels.
  - BoN evaluation is biased: PRMs tolerate correct answers with flawed reasoning, and many put their minimum score on the final-answer step. In effect they have become outcome judges.
  - Fix proposed: consensus filtering, where Monte Carlo and the LLM judge must agree.
- **ThinkPRM (arXiv:2504.16828; TMLR 2026):** a generative long-CoT PRM trained on about 8K labels. — [summary of paper](https://arxiv.org/html/2504.16828v3)
  - Beats discriminative PRMs trained on about 100x more data, by up to 8 F1 on ProcessBench.
  - Out of domain: +8% on a GPQA-Diamond subset and +4.5% on a LiveCodeBench subset.

### Inferences
- Through 2025 the lesson is that a step verifier must reason. Discriminative PRMs are overtaken by prompted reasoning models (o1-mini) and by generative PRMs. That is the same shift the judge line made from scalar to reasoning judges.
- Over-optimisation laws have been measured for scalar RMs and for DPO. I found no equivalent scaling-law study for RL against reasoning or generative judges.

### Gaps
- No 2026 update to ProcessBench SOTA was found in this session.
- I found no work quantifying hacking of RL-trained reasoning judges (for example, policies that learn to persuade a thinking judge).

## Key Question 3: What do reasoning judges buy over prompted judges, and where do they still fail?

### Takeaway
RL-trained thinking judges at 8B-32B match or beat much larger prompted reasoners on correctness-heavy meta-evals. Examples: J1-Qwen-32B at 80.8 against DeepSeek-R1-671B at 78.4, and TIR-Judge-8B close to Claude-Opus-4 on listwise ranking. The remaining failures:
- verdicts reached for wrong reasons
- position bias and ties
- weak precise instruction following
- cost
- correctness that needs external evidence

Tool-using judges (code execution, search) are the 2025-26 response to that last failure.

### Cited Findings
- **J1 (arXiv:2505.10320, May 2025):** GRPO on 22K synthetic pairs (17K WildChat, 5K MATH), with verifiable rewards plus a position-consistency reward. — [HTML](https://arxiv.org/html/2505.10320v3)

  | Model | Overall | PPE | RewardBench | RM-Bench | JudgeBench | FollowBenchEval |
  |---|---|---|---|---|---|---|
  | J1-Qwen-32B-MultiTask | 80.8 | 71.8 | 93.6 | 90.3 | 71.4 | 77.1 |
  | DeepSeek-R1-671B | 78.4 | | | | 68.9 | |
  | o1-mini | 72.7 | | | | 64.2 | |
  | EvalPlanner-70B | 73.2 | | | | | |

  - On PPE Correctness, J1 scores 76.8 against 59.8 for DeepSeek-GRM-27B.
  - Pointwise judges produce more ties.
  - Pairwise judges remain position-sensitive.
- **RM-R1 (arXiv:2505.02387, May 2025):** — [HTML](https://arxiv.org/html/2505.02387)
  - Training: distillation on about 9K Claude-3.7/o3-corrected traces, then GRPO with a ±1 reward. Chain-of-Rubrics: the model writes rubrics for chat prompts and solves reasoning prompts itself first.
  - Results at 32B: an average of 81.2-81.5 over RewardBench, RM-Bench and RMB, against GPT-4o at 77.7. RM-Bench math 91.8, code 74.1.
  - RL alone was insufficient.
- **JudgeLRM (arXiv:2504.00050, Mar 2025):** — [arXiv](https://arxiv.org/abs/2504.00050)
  - 3B/4B models beat GPT-4; 7B-14B models beat DeepSeek-R1 by more than 2 F1.
  - SFT gains correlate negatively with the share of reasoning-demanding samples. This is the clearest evidence that SFT on judgments does not teach judging that requires reasoning.
- **Think-J (arXiv:2505.14268; AAAI 2026):** curated thinking data, then offline or online RL. — [arXiv](https://arxiv.org/abs/2505.14268)
- **DeepSeek-GRM (arXiv:2504.02495, Apr 2025):** — [HTML](https://arxiv.org/html/2504.02495v3)
  - Method: SPCT; a pointwise generative RM writes principles and then critiques, trained with online RL. It scales at inference with 32 samples and a meta RM.
  - Overall score: greedy 69.9, voting@32 71.0, MetaRM@32 72.8, against GPT-4o at 71.3.
  - Admits "challenges in efficiency and specific tasks".
- **Reward Reasoning Models (arXiv:2505.14674):** long-CoT pairwise RMs with adaptive compute, using knockout and ELO tournaments over candidates. — [arXiv](https://arxiv.org/abs/2505.14674)
- **CriticGPT (arXiv:2407.00215, Jun 2024), the critic line:** — [arXiv](https://arxiv.org/abs/2407.00215), [HTML](https://arxiv.org/html/2407.00215)
  - Training: RLHF on contractor-inserted bugs.
  - Preference: model critiques preferred over human critiques in 63% of cases on natural bugs and over 80% on inserted bugs. It catches more inserted bugs than paid contractors.
  - Hallucination: critics hallucinate bugs. Longer critiques (tuned by the Force Sampling Beam Search length modifier) are more comprehensive but carry more hallucinations and nitpicks. Absolute nitpick and hallucination rates "remain high".
  - Human+critic teams: they catch about as many bugs as the model alone with fewer hallucinations.
  - Scope: short code only, no multi-file context.
- **TIR-Judge (arXiv:2510.23038; ICLR 2026):** — [arXiv](https://arxiv.org/abs/2510.23038)
  - RL-trained judge with a code executor, covering pointwise, pairwise and listwise formats.
  - +6.4% pointwise and +7.7% pairwise over reasoning judges; listwise at 8B is comparable to Claude-Opus-4.
  - The Zero variant (no distillation) matches the distilled one.
- **OpenReward (arXiv:2510.24636):** an RM that plans tool calls to gather evidence and then verifies each response, trained with GRPO on 27K synthetic pairs. — [arXiv](https://arxiv.org/abs/2510.24636)
- **AgentV-RL (arXiv:2604.16004, Apr 2026; ACL 2026):** — [arXiv](https://arxiv.org/abs/2604.16004)
  - A multi-turn tool-augmented verifier with forward and backward checking agents, trained with RL.
  - The 4B model is reported at +25.2% over SOTA outcome RMs; the abstract does not name the benchmark.
  - Motivation: false positives from error propagation and unreliability on knowledge- or computation-intensive tasks.
- **Earlier tool-using RMs:** Agentic Reward Modeling (arXiv:2502.19328) combines an RM with search and code verification agents; its search variant is sometimes worse than the default. Themis (arXiv:2310.01045, ICLR 2024) was an early tool-augmented RM. — [arXiv](https://arxiv.org/abs/2502.19328)
- **Right verdict, wrong reason:** "Outcome Accuracy is Not Enough" (arXiv:2602.04649, Feb 2026). — [arXiv](https://arxiv.org/abs/2602.04649)
  - GenRMs and LLM judges show "deceptive alignment", producing correct judgments for incorrect reasons.
  - Outcome-only RL lowers rationale consistency over training.
  - Their hybrid reward reaches RM-Bench 87.1 and JudgeBench 82.0.
  - A related paper is R-Align (arXiv:2602.06763); only its abstract snippet was seen.
- **Judge choice as a variable:** RaRE (arXiv:2610.21179, Oct 2026). — [arXiv](https://arxiv.org/abs/2610.21179)
  - In rubric-as-reward RL, the choice of judge alone produces large spread in results.
  - A naive average of judges does not beat the best single judge; confidence-weighted ensembling with drop-on-disagreement does.
- **Cascade judges:** JEV-as-a-Judge (arXiv:2609.26550, Sep 2026). — [arXiv](https://arxiv.org/abs/2609.26550)
  - A decision-only judge escalates low-confidence cases to a reasoning judge, giving 0.9 points above a GPT-6 judge at 41% of its fee.
  - The cheap judge falls behind where the verdict must be derived (math, code, logic) and on style-adversarial or reference-free prose.

### Inferences
- What reasoning buys: the judge solves the problem itself, or writes the rubric, before comparing. That is why gains concentrate on math, code and correctness subsets (RM-R1 math 91.8 against a prior best near 73).
- Where reasoning still fails:
  - Subjective or precise-constraint judging (instruction following).
  - Faithfulness of the rationale itself (arXiv:2602.04649).
  - Correctness that needs evidence the model lacks, which is what pushes toward tools.
- The 2026 direction is agentic verification: tools, multi-turn checking, cascades and ensembles. None of the 2026 papers seen reports an over-optimisation study against these judges.

### Gaps
- I did not verify JudgePanel (arXiv:2608.29168, listed as Aug 2026 in search results, a compact judge with panel deliberation). The search tool itself flagged the ID as unusual, and no note was written.
- No full-text limitations sections were read for TIR-Judge, OpenReward or AgentV-RL; only the abstracts were.
- I found no 2025-26 paper that measures critic false-positive (hallucinated bug) rates at repository scale.

## Key Question 4: What is the 2026 state of the art on meta-evaluation benchmarks, and which categories remain hard?

### Takeaway
RewardBench 1 is saturated (above 93% for J1, EvalPlanner and DeepSeek-GRM with MetaRM). On RewardBench 2 the top score is about 84 (Skywork-Reward-V2-8B, a scalar RM). JudgeBench went from about 50% (GPT-4o in 2024) to about 71% (J1-32B, 2025) and about 82% (a rationale-aligned GenRM, Feb 2026), and one Sep 2026 paper reports a GPT-6 judge at 93.1% on a subset. Precise instruction following, math, factuality, and verdicts that must be derived rather than read off remain the hard categories.

### Cited Findings
- **RewardBench 2 (arXiv:2506.01937; v2 Apr 2026; ICLR 2026):** — [HTML](https://arxiv.org/html/2506.01937v2)
  - 1,865 prompts in a best-of-4 format, with six subsets: Factuality 475, Safety 450, Focus 495, Math 183, Precise IF 160, Ties 102.
  - Models score about 20 points below RewardBench 1.
  - Top model: Skywork-Reward-V2-Llama-3.1-8B at 84.1 (Factuality 84.6, IF 66.3, Math 77.6, Safety 96.7, Focus 98.4, Ties 81.2).
  - Precise IF is the lowest subset for nearly every top-20 model, many of them at 35-50. Math and Factuality are also hard.
  - Score correlates with best-of-N downstream at r = 0.87. Classifier Bradley-Terry RMs lead the table over generative judges.
- **JudgeBench (arXiv:2410.12784; ICLR 2025):** GPT-4o is slightly above random. — [arXiv](https://arxiv.org/abs/2410.12784)
  - Later scores: J1-Qwen-32B 71.4, DeepSeek-R1 68.9, o1-mini 64.2, EvalPlanner-8B 30.2 ([J1](https://arxiv.org/html/2505.10320v3)); rationale-consistency GenRM 82.0 ([arXiv](https://arxiv.org/abs/2602.04649)).
  - A GPT-6 judge is reported at 93.1% on a JudgeBench subset and 94.6% on the RM-Bench hard subset ([arXiv:2609.26550](https://arxiv.org/abs/2609.26550)). These are one paper's own runs, not a leaderboard.
- **RM-Bench (arXiv:2410.16184):** the best RMs scored 46.6% in the style-interfered setting in 2024 ([arXiv](https://arxiv.org/abs/2410.16184)). Later overall scores: J1-32B 90.3; RM-R1-32B 83.9 (code 74.1 is the weakest domain); GenRM 87.1 (arXiv:2602.04649).
- **PPE (arXiv:2410.14872):** human-preference and verifiable-correctness subsets ([arXiv](https://arxiv.org/abs/2410.14872)). Best reported: J1-32B at 71.8 overall and 76.8 on Correctness. DeepSeek-GRM-27B scores 67.2 on Preference and 63.2 on Correctness with MetaRM@32.
- **ProcessBench:** the 2024-25 best is o1-mini at 87.9 F1 among the original entries, and ThinkPRM is up to 8 F1 above discriminative PRMs. — [HTML](https://arxiv.org/html/2412.06559v4)

### Inferences
- The ceiling is no longer RewardBench-style chat preference, which is saturated. The open problems are judging that requires constructing the answer, such as math or code correctness and fine-grained instruction constraints, and judging robust to style.
- A high meta-eval score does not guarantee a good RL reward. RewardBench 2's lineage finding and RaRE's judge spread both show this.

### Gaps
- I found no single aggregated 2026 leaderboard snapshot for JudgeBench, RM-Bench or PPE. Numbers come from individual papers with different subsets and protocols, so they are not directly comparable.
- I did not fetch the live RewardBench 2 Hugging Face leaderboard to check whether a 2026 model has passed 84.1.

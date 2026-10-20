# Alternative evaluation paradigms beyond a single LLM judge (2018 to Oct 2026)

Scope: debate and scalable oversight, multi-judge panels and multi-agent debate, arenas and peer review, consistency and reference-free checks, execution and verification, interactive and user-simulation evaluation, uncertainty-aware judging, and meta-evaluation. One note per paper is in `notes/` with `category: alternative-paradigms`. Where a number comes from memory and was not re-checked against the abstract this session, the note says "as recalled". Everything else here was checked against the arXiv abstract page.

## For debate: what do the empirical results show about judge accuracy with and without debate, and what are the known failure cases?

### Takeaway
Debate reliably beats consultancy (one advocate). It beats a no-help judge only when the judge lacks information the debaters have, as in hidden-passage reading comprehension. On math, logic and code with no information gap, the gain over direct QA is mixed. 2025 human studies found no overall advantage over simply deferring to the model, and the theory has moved on to the obfuscated-arguments problem.

### Cited Findings
- Irving, Christiano and Amodei proposed debate as a zero-sum game judged by a human. They argue that optimal play lets a polynomial-time judge decide PSPACE questions. The only experiment is a toy: on MNIST, a sparse classifier that sees 6 pixels rises from 59.4% to 88.9% accuracy with debate (figures as recalled from the abstract). arXiv 1805.00899, 2018-05. — [arXiv](https://arxiv.org/abs/1805.00899)
- Khan et al. (ICML 2024 best paper) used QuALITY with information asymmetry and verified quotes. LLM judges reached 76% with debate vs 48% naive; human judges 88% vs 60%. Optimising debaters for persuasiveness, without labels, raised judge accuracy. arXiv 2402.06782, 2024-02. — [arXiv](https://arxiv.org/abs/2402.06782)
- Kenton et al. (DeepMind, NeurIPS 2024) tested weak LLM judges on extractive QA, math, code, logic and multimodal tasks:
  - Debate beat consultancy on all tasks.
  - Debate beat direct QA only on extractive QA with information asymmetry; elsewhere the result was mixed.
  - When agents picked their own side, judges were less often convinced of the wrong answer in debate than in consultancy.
  - Stronger debaters helped, but less than earlier work suggested.
  - arXiv 2407.04622, 2024-07. — [arXiv](https://arxiv.org/abs/2407.04622)
- Michael et al. used human expert debaters: judges reached 84% with debate vs 74% with consultancy (as recalled). arXiv 2311.08702, 2023-11. — [arXiv](https://arxiv.org/abs/2311.08702)
- Earlier negative results: single-turn and two-turn human debate did not improve time-limited human judges on hard QuALITY questions. arXiv 2204.05212 and 2210.10860, 2022. — [arXiv](https://arxiv.org/abs/2204.05212), [arXiv](https://arxiv.org/abs/2210.10860)
- Arnesen et al. trained debaters with self-play RL. This raised judge accuracy, while training consultants did not (as recalled). arXiv 2409.16636, 2024-09. — [arXiv](https://arxiv.org/abs/2409.16636)
- Recchia et al. ran two human studies:
  - Simple oversight protocols gave no overall advantage.
  - Seeing arguments for both answers helped only when the model was wrong.
  - After researching online, participants grew more confident in the system even when it was wrong.
  - Their reanalysis says optimistic earlier results were likely driven by evaluators' outside knowledge, an advantage that shrinks as models improve.
  - They recommend comparing every protocol against plain deference to the model.
  - arXiv 2507.19486, 2025-05. — [arXiv](https://arxiv.org/abs/2507.19486)
- Engels et al. derived scaling laws for oversight games. Nested scalable oversight at a general Elo gap of 400 succeeds 51.7% of the time for Debate, 13.5% for Mafia, 10.0% for Backdoor Code and 9.4% for Wargames. Success falls as the overseen system gets stronger. arXiv 2504.18530, 2025-04. — [arXiv](https://arxiv.org/abs/2504.18530)
- Obfuscated arguments (theory): Brown-Cohen et al. state that existing recursive debate protocols let a dishonest debater force the honest one to solve an intractable problem. Prover-estimator debate restores honest-debater efficiency under stability assumptions. arXiv 2506.13609, 2025-06, revised 2026-07. — [arXiv](https://arxiv.org/abs/2506.13609)
- The earlier doubly-efficient debate paper gives protocols where the honest debater needs only polynomial simulation and the judge checks a constant number of steps. It is theory only. arXiv 2311.14125, 2023-11. — [arXiv](https://arxiv.org/abs/2311.14125)
- Prover-verifier games: sneaky provers trained against small verifiers learn incorrect solutions that time-limited humans accept more often over training. This is direct evidence of "persuasive but wrong" outputs emerging from optimisation. Optimising for correctness alone reduces legibility. arXiv 2407.13692, 2024-07. — [arXiv](https://arxiv.org/abs/2407.13692)
- Two metric and threshold critiques were seen only at search-snippet level:
  - arXiv 2504.03731 (2025-03) argues judge accuracy is the wrong metric and earlier debate-vs-consultancy baselines were flawed. — [arXiv](https://arxiv.org/abs/2504.03731)
  - arXiv 2603.05293 (2026-03) reports a sharp threshold between effective and ineffective debate depending on knowledge divergence. — [arXiv](https://arxiv.org/abs/2603.05293)
- Goel et al. found that LLM judges favour models similar to themselves and that errors become more correlated as capability grows (as recalled). This undercuts AI-judges-AI oversight. arXiv 2502.04313, 2025-02. — [arXiv](https://arxiv.org/abs/2502.04313)

### Inferences
- The positive debate results come from settings where the judge lacks information but can verify quotes. When the gap is in reasoning ability, the evidence is weak or mixed. Agent evaluation is mostly a reasoning gap plus a very large amount of evidence to read, which is closer to the regime where debate has not been shown to help.
- The known failure modes each have evidence:
  - Persuasive but wrong outputs: sneaky provers, and humans growing confident in wrong answers.
  - Obfuscated arguments: theory, with a proposed fix that has not been tested empirically.
  - Judge laziness or deference: the Recchia studies, and Kenton's open-consultancy result that judges follow a wrong consultant.
- The fair baseline for any debate protocol is "defer to the strongest model". Few papers report it.

### Gaps
- I did not find an empirical test of prover-estimator debate with LLMs (as of this search).
- I did not find a debate study in which the judge itself has tools (code execution, retrieval) or in which the object being debated is an agent trajectory.
- Exact judge-accuracy tables for Kenton et al. per task were not extracted; the abstract reports only qualitative findings.
- The LMArena-style public response to Kenton/Khan replications and AF posts (e.g. the 2020 obfuscated-arguments post) were not fetched.

## Multi-judge panels and multi-agent debate for evaluation: what they buy and where they failed

### Takeaway
Panels of independent judges from different model families (PoLL, Language Model Council) cut cost and single-model bias. Making the judges deliberate (ChatEval-style debate) adds little beyond voting: 2025 analyses show majority voting explains most multi-agent-debate gains. Correlated errors between models limit how much independence a panel really has.

### Cited Findings
- PoLL (Verga et al.): a panel of smaller models from disjoint families beat a single GPT-4 judge across 3 judge settings and 6 datasets. It showed less intra-model bias and cost more than 7x less. arXiv 2404.18796, 2024-04. — [arXiv](https://arxiv.org/abs/2404.18796)
- Language Model Council: 20 LLMs write tests, answer them and judge one another on emotional-intelligence dilemmas. This gave more separable and robust rankings that matched a human study better than any single judge. The full council is costly, so the authors studied sub-councils by Monte Carlo. arXiv 2406.08598, 2024-06. — [arXiv](https://arxiv.org/abs/2406.08598)
- ChatEval: a multi-agent referee team with diverse personas. The authors' ablation shows that giving every agent the same role hurts. arXiv 2308.07201, 2023-08 (ICLR 2024). — [arXiv](https://arxiv.org/abs/2308.07201)
- Debate or Vote (Choi, Zhu, Li, NeurIPS 2025 spotlight): on 7 NLP benchmarks, majority voting accounts for most multi-agent-debate gains. Debate forms a martingale over beliefs, so it does not raise expected correctness, though biasing updates toward correction helps. arXiv 2508.17536, 2025-08. — [arXiv](https://arxiv.org/abs/2508.17536)
- Earlier critiques: multi-agent debate does not reliably beat self-consistency or ensembling at matched cost (Smit et al., arXiv 2311.17371) or chain-of-thought (Zhang et al., arXiv 2502.08788), as recalled. — [arXiv](https://arxiv.org/abs/2311.17371), [arXiv](https://arxiv.org/abs/2502.08788)
- Two 2025-2026 papers were seen at search-snippet level only:
  - arXiv 2511.07784 reports that majority pressure suppresses independent correction in a controlled puzzle. — [arXiv](https://arxiv.org/abs/2511.07784)
  - arXiv 2606.29270 reports that an LLM judge reading debate logs shares the debaters' blind spots and gave negative net gain. — [arXiv](https://arxiv.org/abs/2606.29270)
- JudgeBench evaluated multi-agent judges among others and found that strong judges, GPT-4o included, did only slightly better than random on hard, objectively labelled pairs. arXiv 2410.12784, 2024-10. — [arXiv](https://arxiv.org/abs/2410.12784)
- Jury Learning (Gordon et al., CHI 2022) is the pre-LLM precedent: it models individual annotators and lets practitioners specify the jury's composition instead of a single majority label. arXiv 2202.02950. — [arXiv](https://arxiv.org/abs/2202.02950)

### Inferences
- The value of a panel comes from independent votes. Deliberation adds cost and herding risk, so a panel should be compared against majority vote at equal compute.

### Gaps
- I did not find a direct "debate vs vote" decomposition for judge panels (ChatEval, Auto-Arena committees) on judging tasks specifically.

## For arenas and crowds: what biases were found and what did "The Leaderboard Illusion" and related critiques show?

### Takeaway
Crowd arenas measure self-selected users' style-sensitive preferences, and their rankings can be gamed:
- Providers can test privately and disclose selectively.
- Data access is unequal across providers.
- Votes can be de-anonymised and rigged.
- Rankings at the top are fragile.

LLM-judged arena substitutes add judge biases on top, to the point that a constant "null" answer can top them.

### Cited Findings
- Chatbot Arena: crowdsourced, anonymous pairwise battles ranked with Bradley-Terry. ICML 2024. arXiv 2403.04132, 2024-03. — [arXiv](https://arxiv.org/abs/2403.04132)
- The Leaderboard Illusion (Singh et al.):
  - Meta tested 27 private variants before Llama-4.
  - Google and OpenAI received an estimated 19.2% and 20.4% of all Arena data; 83 open-weight models combined received 29.7%.
  - Limited extra Arena data gives up to 112% relative gain on the Arena distribution.
  - Proprietary models are deprecated less often.
  - The authors conclude that providers overfit to Arena dynamics.
  - arXiv 2504.20879, 2025-04. — [arXiv](https://arxiv.org/abs/2504.20879)
- Huang et al. showed an attacker can identify which model produced a reply with more than 95% accuracy and then vote for or against a target. They worked with Arena on mitigations. arXiv 2501.07493, 2025-01. — [search result](https://www.researchgate.net/publication/387975867_Exploring_and_Mitigating_Adversarial_Manipulation_of_Voting-Based_Leaderboards)
- Min et al. showed that vote rigging with a few hundred votes can shift rankings. arXiv 2501.17858, 2025-01. — [arXiv](https://arxiv.org/abs/2501.17858)
- Dropping a handful of preferences can change the top LLM rankings. arXiv 2508.11847, 2025-08. — [arXiv](https://arxiv.org/abs/2508.11847)
- MT-Bench / Chatbot Arena paper: the GPT-4 judge agrees with humans more than 80% of the time, but shows position, verbosity and self-enhancement bias. arXiv 2306.05685, 2023-06. — [arXiv](https://arxiv.org/abs/2306.05685)
- Null models (Zheng et al., ICLR 2025): a constant output crafted against the judge template reaches top win rates on AlpacaEval 2.0, Arena-Hard-Auto and MT-Bench (86.5% LC, 83.0, 9.55, as recalled). arXiv 2410.07137, 2024-10. — [arXiv](https://arxiv.org/abs/2410.07137)
- Length control: length-controlled AlpacaEval raised Spearman correlation with Arena from 0.94 to 0.98 (as recalled). arXiv 2404.04475. — [arXiv](https://arxiv.org/abs/2404.04475)
- Arena-Hard-Auto / BenchBuilder distils Arena prompts into a hard static set judged by an LLM; its validation target is agreement with Arena. arXiv 2406.11939, 2024-06. — [arXiv](https://arxiv.org/abs/2406.11939)
- Auto-Arena has an LLM examiner, peer battles and an LLM committee; it reports about 92% Spearman correlation with Arena (as recalled). arXiv 2405.20267, 2024-05. — [arXiv](https://arxiv.org/abs/2405.20267)
- Peer review:
  - PRE qualifies reviewer LLMs with an exam. arXiv 2401.15641. — [arXiv](https://arxiv.org/abs/2401.15641)
  - PiCO learns per-model weights by consistency optimisation. It assumes that stronger models judge more accurately and also answer better. arXiv 2402.01830, 2024-02. — [arXiv](https://arxiv.org/abs/2402.01830)
- Judge Arena (Atla on Hugging Face, Nov 2024) applies arena voting to judges themselves. It is a blog/platform with no paper. — [HF blog](https://huggingface.co/blog/arena-atla)

### Inferences
- PiCO, PRE and Auto-Arena validate themselves by correlation with Chatbot Arena, so they inherit Arena's biases rather than escaping them.
- Peer review assumes reviewer independence, which the similarity findings of Goel et al. (arXiv 2502.04313) undercut.

### Gaps
- LMArena's public rebuttal to The Leaderboard Illusion was not fetched. I found no peer-reviewed critique specific to the validity of style control.
- I did not find an arena for agent trajectories with a published bias audit.

## For consistency/reference-free methods: when do they work and when does a confidently wrong model fool them?

### Takeaway
Consistency checks work when errors are random. This covers confabulations that vary across samples, contradictions a cross-examiner can expose, and logical invariances a superhuman model violates. A model that is wrong in the same way every time passes them all. Consistency is a necessary condition for correctness, not a test of it.

### Cited Findings
- LM vs LM (Cohen et al., EMNLP 2023): an examiner LM cross-examines an examinee about a claim and flags inconsistencies. It beat self-confidence baselines on closed-book factual QA. arXiv 2305.13281, 2023-05. — [arXiv](https://arxiv.org/abs/2305.13281)
- Consistency checks for superhuman models (Fluri, Paleka, Tramer) found logical violations without ground truth: chess engines gave opposite scores to equivalent positions, and GPT-4 forecasts of sports records were non-monotone. arXiv 2306.09983, 2023-06. — [arXiv](https://arxiv.org/abs/2306.09983)
- Round-trip correctness (Allamanis et al., ICML 2024): code to description to code, checked for semantic equivalence. It correlates strongly with HumanEval/MBPP and extends evaluation to domains without labels. arXiv 2402.08699, 2024-02. — [arXiv](https://arxiv.org/abs/2402.08699)
- SelfCheckGPT (arXiv 2303.08896) and semantic entropy (arXiv 2302.09664) score disagreement across samples. By construction, an error repeated in every sample gets low uncertainty (inference from the method). — [arXiv](https://arxiv.org/abs/2303.08896), [arXiv](https://arxiv.org/abs/2302.09664)
- Without external feedback, intrinsic self-correction often fails to improve reasoning and can degrade it. arXiv 2310.01798, 2023-10. — [arXiv](https://arxiv.org/abs/2310.01798)
- CodeT ranks code by agreement with model-generated tests (arXiv 2207.10397). Generated tests can share the code's misconception. — [arXiv](https://arxiv.org/abs/2207.10397)
- "Self-Alignment via consistency": the closest paper found is Self-Alignment for Factuality (Zhang et al., ACL 2024). It uses self-evaluation as the DPO reward, and is bounded by the model's own knowledge. arXiv 2402.09267. — [arXiv](https://arxiv.org/abs/2402.09267)

### Inferences
- Consistency methods are useful as cheap filters that catch confabulations and contradictions. They should be paired with an external signal (execution, retrieval, human) for the systematic-error case.
- Cross-examination is a natural fit for agents, which can be asked why they took an action, but I found no application of it.

### Gaps
- I found no study that measures how often consistency-based evaluators pass confidently wrong outputs across models. The claim rests on the methods' construction and on self-correction results.
- The exact paper the brief calls "Self-Alignment via consistency" was not identified.

## Execution and verification-based evaluation: what it buys and where it failed

### Takeaway
Execution gives ground truth only as good as the tests. Test insufficiency has been shown repeatedly, from HumanEval to SWE-bench Verified. Agents also learn to exploit tests. RLVR inherits the same limitation, and some of its gains appear even with spurious rewards.

### Cited Findings
- EvalPlus (HumanEval+, about 80x more tests) lowered pass@k by up to roughly 19-29% and changed rankings (as recalled). arXiv 2305.01210, 2023-05. — [arXiv](https://arxiv.org/abs/2305.01210)
- UTBoost: 36 under-tested SWE-bench instances; 345 patches wrongly marked passing; 170 erroneous patches in Lite and 92 in Verified. Fixing the result parser changed rankings. arXiv 2506.09289, 2025-06. — [arXiv](https://arxiv.org/abs/2506.09289)
- PatchDiff (ICSE 2026): about 7.8% of "correct" SWE-bench Verified patches fail the full developer test suite, and 29.6% behave differently from the gold patch (28.6% of those are certainly wrong). arXiv 2503.15223. — [arXiv](https://arxiv.org/html/2503.15223v2)
- ImpossibleBench creates spec/test-conflicting variants of LiveCodeBench and SWE-bench, so any pass is cheating. It measures how often agents exploit tests. arXiv 2510.20270, 2025-10. — [arXiv](https://arxiv.org/abs/2510.20270)
- RLVR was named in Tulu 3 (arXiv 2411.15124). DeepSeek-R1 used rule-based rewards to avoid neural reward hacking (arXiv 2501.12948). — [arXiv](https://arxiv.org/abs/2411.15124), [arXiv](https://arxiv.org/abs/2501.12948)
- Critiques of RLVR:
  - Base models reach higher pass@k at large k than RLVR models (arXiv 2504.13837).
  - Random or incorrect rewards still improve Qwen math scores (arXiv 2506.10947).
  - Both recalled, not re-verified. — [arXiv](https://arxiv.org/abs/2504.13837), [arXiv](https://arxiv.org/abs/2506.10947)
- Formal and property-based tests:
  - LLM-written property-based tests are often unsound or weak (arXiv 2307.04346).
  - Clover checks agreement between code, docstring and Dafny annotations (arXiv 2310.17807).
  - [arXiv](https://arxiv.org/abs/2307.04346), [arXiv](https://arxiv.org/abs/2310.17807)
- Agentic Benchmark Checklist (Zhu et al.) audits agent benchmarks for task and outcome-validity flaws. arXiv 2507.02825. — [arXiv](https://arxiv.org/abs/2507.02825)

### Inferences
- Execution-based evaluation fails in a predictable direction: it over-credits. That makes it a natural place to add a second evaluator (an agentic judge that reads the issue and the patch) on passing cases only.

### Gaps
- I found no published head-to-head of an agentic judge vs augmented tests on the same SWE-bench patches. Other notes in this folder (Agent-as-a-Judge, TIR-Judge) are adjacent.

## Interactive and user-simulation evaluation: what it buys and where it failed

### Takeaway
Interaction exposes failures that static tests miss: multi-turn degradation, preference elicitation, social goals. But LLM-simulated users are a new, unvalidated evaluator. They shift scores by several points depending on the simulator, they are miscalibrated against real users, and they misrepresent some dialect groups.

### Cited Findings
- HALIE (Lee et al.): non-interactive metrics did not predict interactive quality across five tasks. arXiv 2212.09746. — [arXiv](https://arxiv.org/abs/2212.09746)
- SOTOPIA: LLM agents pursue social goals, scored by a GPT-4 judge. arXiv 2310.11667. — [arXiv](https://arxiv.org/abs/2310.11667)
- Zhou et al. found that omniscient single-LLM simulation overstates success relative to realistic agent-agent interaction. arXiv 2403.05020. — [arXiv](https://arxiv.org/abs/2403.05020)
- tau-bench uses an LLM-simulated user plus a database-state check and pass^k (arXiv 2406.12045). tau2-bench adds dual control (arXiv 2506.07982). UserBench tests preference elicitation (arXiv 2507.22034). — [arXiv](https://arxiv.org/abs/2406.12045), [arXiv](https://arxiv.org/abs/2506.07982), [arXiv](https://arxiv.org/abs/2507.22034)
- Lost in Simulation (Seshadri et al., 2026-01) ran a human study in the US, India, Kenya and Nigeria on tau-Bench retail:
  - Agent success shifted by up to 9 points depending on the user LLM.
  - Simulators underestimated success on hard tasks and overestimated it on moderate ones.
  - Simulators were the worst proxies for AAVE and Indian English speakers.
  - arXiv 2601.17087. — [arXiv](https://arxiv.org/abs/2601.17087)
- Related notes already in this folder from other researchers: "Mind the Sim2Real Gap in User Simulation" (arXiv 2603.11245; 451 real people vs 31 simulators) and "Simulated Customers Never Walk Away" (arXiv 2606.20708; the tau-bench simulator cannot decline). — [arXiv](https://arxiv.org/abs/2603.11245), [arXiv](https://arxiv.org/abs/2606.20708)
- KIEval (arXiv 2402.15043) and LLM-as-an-Interviewer (arXiv 2412.10424) use an interactor LLM to resist contamination. — [arXiv](https://arxiv.org/abs/2402.15043), [arXiv](https://arxiv.org/abs/2412.10424)
- MINT uses GPT-4 to simulate feedback (arXiv 2309.10691). — [arXiv](https://arxiv.org/abs/2309.10691)
- Lost in Conversation reports an average drop of about 39% from single-turn to multi-turn (as recalled, arXiv 2505.06120). — [arXiv](https://arxiv.org/abs/2505.06120)

### Inferences
- A user simulator is itself a judge-like model and needs the same meta-evaluation (calibration against humans) that judges get. Few benchmarks do this.

### Gaps
- SimulatorArena (Dou et al., EMNLP 2025) was seen only as a citation; its arXiv id was not verified, so no note was written for it.

## For uncertainty-aware judging: how much does abstention or escalation help and at what coverage cost?

### Takeaway
Selective judging turns "the judge is sometimes wrong" into a controlled error rate on the cases it accepts. Trust or Escalate guarantees more than 80% human agreement at almost 80% coverage where GPT-4 alone almost never reaches 80%. SCOPE (2026) holds a 10% risk bound while accepting up to 2.4x more cases than baselines. The price is the cases left to humans, plus an exchangeability assumption. There is also a hard limit: Dorner et al. prove that judge labels cannot cut ground-truth needs by more than half when the judge is no better than the evaluated model.

### Cited Findings
- Trust or Escalate (Jung, Brahman, Choi; ICLR 2025):
  - Confidence comes from Simulated Annotators.
  - The calibrated threshold gives a provable human-agreement level.
  - Cascaded Selective Evaluation escalates from cheaper to stronger judges.
  - On a Chatbot Arena subset where GPT-4 almost never reaches 80% agreement, the method guarantees over 80% agreement with almost 80% test coverage, starting the cascade at Mistral-7B.
  - arXiv 2407.18370, 2024-07. — [arXiv](https://arxiv.org/abs/2407.18370)
- SCOPE (Badshah, Emami, Sajjad; ICML 2026) uses Bidirectional Preference Entropy, querying both response orders. At alpha = 0.10, the empirical false discovery rate is 0.097-0.099, with up to 2.4x more judgments accepted than vanilla baselines. arXiv 2602.13110, 2026-02. — [arXiv](https://arxiv.org/abs/2602.13110)
- Conformal intervals for judge scores: Sheng et al., arXiv 2509.18658, 2025-09. — [arXiv](https://arxiv.org/abs/2509.18658)
- Dorner, Nastl and Hardt (ICLR 2025) prove that if the judge is no more accurate than the evaluated model, no debiasing method can reduce the required ground-truth labels by more than half. Empirical savings are smaller still. arXiv 2410.13341, 2024-10. — [arXiv](https://arxiv.org/abs/2410.13341)
- Statistical combination of a few human labels with many LLM labels: confidence-driven inference (arXiv 2408.15204) and prediction-powered AutoEval (arXiv 2403.07008). — [arXiv](https://arxiv.org/abs/2408.15204), [arXiv](https://arxiv.org/abs/2403.07008)
- A 2026 cascade in this folder from another researcher: JEV-as-a-Judge (arXiv 2609.26550) escalates low-confidence cases to a reasoning judge. Per that note, it scores 0.9 points above a GPT-6 judge at 41% of the cost. — [arXiv](https://arxiv.org/abs/2609.26550)

### Inferences
- Coverage cost: roughly 20% of items going to humans or a stronger tier, at an 80-90% agreement target, is the order of magnitude reported.

### Gaps
- I found no selective-evaluation study on agent trajectories or long-horizon tasks; all of the above are pairwise or score judgments of single outputs.
- Exact coverage-vs-target curves for Trust or Escalate on other datasets were not extracted.

## Meta-evaluation (judge-the-judge)

### Takeaway
Meta-evaluation shows that agreement with human preference is a weak test. On objectively labelled hard pairs, judges are near random (JudgeBench). Percent agreement hides poor kappa. Criteria themselves drift as people grade (EvalGen). Statistical tests such as the alt-test exist for justifying a judge per task.

### Cited Findings
- EvalGen (Shankar et al., UIST 2024): users grade outputs and the system picks LLM or code assertions that agree with them. It documents criteria drift: users need criteria to grade, but grading defines the criteria. arXiv 2404.12272, 2024-04. — [arXiv](https://arxiv.org/abs/2404.12272)
- JudgeBench: on hard knowledge, reasoning, math and coding pairs, strong judges including GPT-4o were only slightly better than random. arXiv 2410.12784. — [arXiv](https://arxiv.org/abs/2410.12784)
- Judging the Judges (Thakur et al.): only the largest models approach human alignment, percent agreement hides differences that Cohen's kappa reveals, and judges are lenient (as recalled). arXiv 2406.12624. — [arXiv](https://arxiv.org/abs/2406.12624)
- Bavaresco et al. (JUDGE-BENCH, 20 tasks): agreement varies widely by task (as recalled). arXiv 2406.18403. — [arXiv](https://arxiv.org/abs/2406.18403)
- Alt-test (Calderon et al.): a statistical justification for replacing annotators with a judge. arXiv 2501.10970. — [arXiv](https://arxiv.org/abs/2501.10970)
- LLMBar: adversarial pairs where the superficially better output fails the instruction (arXiv 2310.07641). — [arXiv](https://arxiv.org/abs/2310.07641)

### Gaps
- The brief's "Humans as judges of judges" title was not matched to a specific paper; Thakur et al. is the closest found.

## Which paradigms have NOT been combined with agentic judges or applied to evaluating agents?

### Takeaway
Most alternative paradigms were built for single outputs and passive text-reading judges. Execution and user simulation are the only ones widely applied to agents. Debate, prover-verifier training, selective or conformal abstention, consistency checks and peer-review ranking have, as far as this search found, not been combined with tool-using agentic judges or applied to agent trajectories.

### Cited Findings
- Every debate study above uses a transcript-reading judge on a QA-style question (QuALITY, math, code answers, GSM). None gives the judge tools or debates an agent trajectory. — [Khan](https://arxiv.org/abs/2402.06782), [Kenton](https://arxiv.org/abs/2407.04622), [Kirchner](https://arxiv.org/abs/2407.13692)
- Selective evaluation papers (Trust or Escalate, SCOPE) are pairwise judgments of single outputs. — [arXiv](https://arxiv.org/abs/2407.18370), [arXiv](https://arxiv.org/abs/2602.13110)
- Agent-as-a-Judge (arXiv 2410.10934, note in this folder) is a single agentic judge exploring a workspace. It is not a panel, it is not a debate and it does not abstain. — [arXiv](https://arxiv.org/abs/2410.10934)
- User-simulation evaluation is applied to agents but rarely calibrated against humans; Lost in Simulation is the exception. — [arXiv](https://arxiv.org/abs/2601.17087)

### Inferences
Untried combinations, with the paper each would extend:
1. Debate between two agentic judges, one arguing an agent succeeded and one arguing it failed, each with tool access to the environment and trajectory, judged by a weaker model (extends Khan/Kenton).
2. Selective or cascaded evaluation of agent runs: a cheap LLM judge first, escalating to an agentic judge and then to a human, with a Trust-or-Escalate-style guarantee (extends 2407.18370).
3. A panel of heterogeneous agentic judges with majority vote, against a single agentic judge (extends PoLL, and Debate or Vote as the control).
4. Cross-examining the evaluated agent about its own trajectory (extends LM vs LM).
5. Consistency or metamorphic checks over environment states (extends Fluri et al.).
6. Arena or peer review over trajectories, with a Leaderboard-Illusion-style audit of submission selection on agent leaderboards.
7. Prover-verifier training where the "sneaky prover" is an agent that fakes success (relates to ImpossibleBench's test exploitation).

### Gaps
- Absence claims are limited to what this search covered. Other researchers' agent-as-judge slices may contain counterexamples (e.g. notes in this folder on "Counsel", "TIR-Judge", "AgentV-RL"); the report writer should cross-check.

# Agent evaluation: outcome benchmarks, trajectory judges, process rewards, simulated users (2023 to Oct 2026)

Scope note: the per-paper notes are in `../notes/` (category `agent-evaluation-benchmarks`). Figures marked "(secondary)" come from a secondary write-up and were not checked against the primary source. Benchmark baselines (SWE-bench 1.96%, WebArena 14.41% vs 78.24% human, OSWorld 12.24% vs 72.36%, GAIA 15% vs 92%, BrowseComp Deep Research 51.5%, MLE-bench 16.9% bronze, WebVoyager auto-eval ~85.3%, TICK 46.4%->52.2%) come from memory of the abstracts. They were not re-fetched in this session.

## Landscape: the outcome benchmarks and their verifiers

| Benchmark | arXiv / date | Verifier | Sees trajectory? |
|---|---|---|---|
| SWE-bench | 2310.06770, 2023-10 | Tests from the gold PR (FAIL_TO_PASS / PASS_TO_PASS) | No |
| SWE-bench Verified | OpenAI blog, 2024-08 | Same tests, 500 human-screened tasks | No |
| WebArena | 2307.13854, 2023-07 | String match and programmatic state checks | No |
| OSWorld | 2404.07972, 2024-04 | Per-task script on final VM state | No |
| tau-bench / tau2-bench | 2406.12045 (2024-06) / 2506.07982 (2025-06) | Final DB state vs goal state, pass^k; LLM-simulated user | No (the user is simulated) |
| AgentBench | 2308.03688, 2023-08 | Per-environment metrics, 8 environments | No |
| GAIA | 2311.12983, 2023-11 | Quasi-exact match on short answer | No |
| BrowseComp | 2504.12516, 2025-04 | Model grader vs short reference answer | No |
| Terminal-Bench 2.0 | 2601.11868, 2026-01 | Container tests, human reference solution | No |
| MLE-bench | 2410.07095, 2024-10 | Kaggle metric vs leaderboard medals | No |
| AgentDojo | 2406.13352, 2024-06 | State checks for both user task and attacker goal | No |

Every major outcome benchmark judges final state or final answer only. Trajectory judging appears only in meta-evaluations (AgentRewardBench, Counsel, OSReward, MobileJudgeBench, TRAIL) and in HAL's log inspection.

## Q1: How well do LLM judges agree with humans on agent trajectories, what do they need to see, and how do they fail?

### Takeaway
On success/failure of web and GUI trajectories, the best LLM judges reach roughly 70-93% agreement with humans, depending on setup. Precision is the weak side: no judge passes 70% precision on AgentRewardBench, and judges lean lenient. Agentic judges that inspect the artifacts (Agent-as-a-Judge) beat judges that read the transcript. The documented failure modes are believing the agent's self-report, missing unfinished steps, grounding mismatches and missed side effects. Locating the error inside a trace is much harder than labelling success: 11% on TRAIL, 14.2% step-level on Who&When.

### Cited Findings
- AgentRewardBench: 1,302 expert-labelled trajectories (5 web benchmarks, 4 agent LLMs), 12 judges. Labels cover success, side effects and repetition. Best judge (GPT-4o, accessibility tree): P 69.8 / R 83.1. No judge above 70% precision. The official rule-based checks score P 83.8 / R 55.9, so they under-report success. — [arXiv 2504.08942](https://arxiv.org/abs/2504.08942), [HTML](https://arxiv.org/html/2504.08942)
- Inputs, from the same paper's GPT-4o-mini ablation: screenshot only P 64.5 / R 78.3; accessibility tree only P 61.5 / R 86.1; both P 62.1 / R 81.7 (more input distracted the judge); neither P 60.7 / R 73.9. Screenshots buy precision; the accessibility tree buys recall. — [HTML](https://arxiv.org/html/2504.08942)
- Judge failure modes named in AgentRewardBench:
  - Grounding mismatch: the agent's reasoning misdescribes the page and a judge without screenshots believes it.
  - Being misled by the agent's claim of success, e.g. a filter that was never applied.
  - Missed instruction details: the right product is found but never purchased.
  - Missing that the agent wrongly declared a task infeasible.
  - Human inter-annotator agreement on success was 89.3%.
  - [HTML](https://arxiv.org/html/2504.08942)
- Agent-as-a-Judge (DevAI: 55 tasks, 365 requirements). The judge explores the workspace with graph, locate, read, retrieve and ask modules.
  - Gray-box (with trajectory): 92.07 / 86.61 / 90.16% alignment with human consensus on MetaGPT / GPT-Pilot / OpenHands, vs LLM-as-a-Judge 68.86 / 71.85 / 70.76%.
  - Black-box (workspace only): 88.52 / 83.88 / 90.44% vs 84.15 / 65.30 / 60.38%.
  - Cost $30.58 vs ~$1,297.50 for human judges, about 97.6% cost and 97.7% time saved.
  - Memory and planning modules hurt or were unstable.
  - [HTML](https://arxiv.org/html/2410.10934v2)
- Online-Mind2Web: 300 live tasks on 136 sites. The WebJudge LLM judge reaches about 85% agreement with humans, and earlier web-agent results look over-optimistic. — [arXiv 2504.01382](https://arxiv.org/abs/2504.01382)
- Pan et al.'s domain-general evaluators reach 74.4-92.9% agreement with oracle metrics. Used as a reward, they improve WebArena by 29% relative and device control by ~75%. — [arXiv 2404.06474](https://arxiv.org/abs/2404.06474)
- OSReward (2026-07): the best VLM judges disagree with the benchmarks' own verifiers on about a quarter of desktop verdicts, and judges show a leniency bias that labels failed runs as successes. OS-Shepherd 9B/35B judges are trained on 100K reasoning-annotated judgments. — [arXiv 2607.28609](https://arxiv.org/abs/2607.28609)
- MobileJudgeBench (2026-08): 931 trajectories, 68 apps. A simple sampled-screenshot baseline matches or beats purpose-built judge pipelines, and the backbone LLM drives quality. Backbones split into conservative and permissive failure profiles. Judge-benchmark scores predict a judge's usefulness as an RL reward. — [arXiv 2608.11434](https://arxiv.org/abs/2608.11434)
- Counsel (2026-06): human labels on process-level critiques of tau-bench and DA-Code trajectories (α=0.78). The best open-weight judge gets ~88% of error locations right but only ~65% of the reasoning. Stronger judges and more reasoning effort help. — [arXiv 2606.21627](https://arxiv.org/abs/2606.21627)
- TRAIL: 148 annotated traces with an error taxonomy. The best model, Gemini-2.5-pro, scores 11% at locating and categorising errors. — [arXiv 2505.08638](https://arxiv.org/abs/2505.08638)
- HAL: 21,730 rollouts cost ~$40k. LLM-aided log reading found agents searching HuggingFace for the benchmark and misusing credit cards in flight booking. Outcome scores did not show either behaviour. — [arXiv 2510.11977](https://arxiv.org/abs/2510.11977)

### Inferences
- Over-trust in the agent's self-report and leniency are the same failure seen from two sides. Each judge paper that reports it (AgentRewardBench, OSReward, MobileJudgeBench's permissive backbone) gives the judge the transcript. The Agent-as-a-Judge results point to the fix: give the judge access to state (workspace, DB, files) so it verifies rather than reads.
- Adding more inputs does not reliably help: both modalities together did worse than screenshots alone, and simple pipelines matched complex ones. Judge quality seems to be bounded by the backbone, not by the information given.
- Side effects are labelled in AgentRewardBench, but no paper found here reports a judge's accuracy on side effects as a headline number.

### Gaps
- No judge-vs-human study found for long-horizon coding trajectories beyond DevAI's 55 tasks, nor for tau-bench-style policy violations with closed frontier judges.
- MAST's LLM-annotator agreement figure was not retrieved.

## Q2: Documented failures of outcome verifiers; how often is the benchmark wrong?

### Takeaway
Very often, and the error runs in both directions. Weak tests and leakage inflate scores; strict string matching deflates them. On SWE-bench, independent audits put verifier error at roughly 6-30% of passes, depending on the method. OpenAI's own 2026 audit found 59.4% of 138 hard Verified tasks flawed. Maintainers would reject about half of passing PRs. ABC reports up to 100% relative mis-estimation across agent benchmarks.

### Cited Findings
- ABC checklist (2025-07): flaws in task setup or reward design shift measured performance by up to 100% relative. SWE-bench Verified has insufficient tests; tau-bench counts empty responses as success. Applying ABC to CVE-Bench cut overestimation by 33%. — [arXiv 2507.02825](https://arxiv.org/abs/2507.02825)
- SWE-Bench+: 32.67% of passing patches had leaked solutions and 31.08% passed on weak tests. SWE-Agent+GPT-4 falls from 12.47% to 3.97%. — [arXiv 2410.06992](https://arxiv.org/abs/2410.06992)
- Wang/Pradel/Liu: 7.8% of passing patches fail the full developer suite, and 29.6% of plausible patches diverge from gold. Scores are inflated by 6.2 pp. — [arXiv 2503.15223](https://arxiv.org/abs/2503.15223)
- UTBoost: 345 wrongly passing patches. 40.9% of Lite and 24.4% of Verified leaderboard entries are affected, with 18 and 11 ranking changes. — [arXiv 2506.09289](https://arxiv.org/abs/2506.09289)
- SWE-Bench Illusion: models identify the buggy file from the issue alone with up to 76% accuracy, vs ~53% on unseen repos. 5-gram verbatim reproduction reaches 35% on Verified, vs 18% elsewhere. — [arXiv 2506.12286](https://arxiv.org/abs/2506.12286)
- OpenAI, 2026-02-23: 59.4% of 138 audited hard Verified tasks had material test or description issues. GPT-5.2, Claude Opus 4.5 and Gemini 3 Flash reproduce gold fixes from memory. OpenAI stopped reporting Verified and recommended SWE-bench Pro. — [OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) (page returned 403 to the fetcher; facts via [search summary](https://aiweekly.co/alerts/openai-drops-swe-bench-verified-backs-pro-after-flaw-audit))
- (secondary) On 2026-07-08 OpenAI audited 731 SWE-bench Pro tasks: 27.4% were flagged by an automated pipeline and 34.1% by engineers, and OpenAI withdrew the Pro recommendation. PAIChecker (2607.28587) reports 13.6% PR-issue misalignment in Verified. — [codex.danielvaughan.com](https://codex.danielvaughan.com/2026/07/31/swe-bench-reliability-crisis-paichecker-change2task-codex-cli-evaluation-benchmark-vacuum/)
- METR (2026-03-10): 296 passing agent PRs were reviewed by 4 maintainers. About half would not be merged, a ~24 pp gap that is statistically significant. — [METR](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)
- OSWorld: OSWorld-Verified (Jul 2025) fixed 300+ issues. — [xlang blog](https://xlang.ai/blog/osworld-verified). Epoch AI (Oct 2025) then found ~10% of tasks with serious errors (wrong keys, checkers too strict or too lax, fatal ambiguity), ~10% depending on live web data and ~15% solvable with a terminal only. — [Epoch](https://epoch.ai/blog/osworld)
- WebArena-style rule checks: 83.8% precision but only 55.9% recall against expert labels, so they systematically under-report. — [AgentRewardBench](https://arxiv.org/html/2504.08942)

### Inferences
- Test-based verifiers fail mainly by false positives (weak tests, leakage, memorisation). String- and state-match verifiers fail mainly by false negatives (strictness). Any judge-based replacement should be checked against both error types separately, not against accuracy alone.
- Each "verified" subset has eventually been re-audited and found faulty (Verified, then Pro, and OSWorld-Verified per Epoch). One-off human screening does not fix the problem.

### Gaps
- No pooled estimate across benchmarks exists. The rates above use different definitions (tasks flawed vs passes wrong vs leaderboard entries affected).
- tau-bench and GAIA verifier error rates beyond the ABC examples were not found.

## Q3: Step-level or process reward for agents (not math): does it work?

### Takeaway
Yes, with modest, mostly verifier-at-inference gains on web tasks. Agent PRMs score progress and checklist subgoals rather than step "correctness". Meta-evaluation of PRMs on long agent traces is thin, and error localisation by LLMs is still poor.

### Cited Findings
- Web-Shepherd (NeurIPS 2025): checklist-conditioned PRM trained on 40K step-level preference pairs. It is ~30 points more accurate than GPT-4o on WebRewardBench and adds +10.9 on WebArena-lite as a verifier for a GPT-4o-mini policy. — [arXiv 2505.15277](https://arxiv.org/abs/2505.15277)
- AgentPRM (2025-11): steps are scored by "promise and progress", with labels from TD estimation plus GAE. It is >8x more compute-efficient than baselines, scales with test-time compute and is used for RL in web shopping and navigation. — [arXiv 2511.08325](https://arxiv.org/abs/2511.08325)
- Pan et al.: trajectory-level evaluators used as reward give +29% on WebArena. — [arXiv 2404.06474](https://arxiv.org/abs/2404.06474)
- Agent-as-a-Judge names building a process-supervised reward from its intermediate requirement checks as future work. It does not build one. — [HTML](https://arxiv.org/html/2410.10934v2)
- MobileJudgeBench finds that judge-benchmark quality predicts downstream on-policy RL gains. — [arXiv 2608.11434](https://arxiv.org/abs/2608.11434)
- Step-level localisation stays hard: Who&When reaches 14.2% step-level accuracy and TRAIL 11%. — [2505.00212](https://arxiv.org/abs/2505.00212), [2505.08638](https://arxiv.org/abs/2505.08638)

### Inferences
- Rubric and checklist decomposition is the common thread: TICK, then Rubrics as Rewards for QA, then Web-Shepherd checklists for web steps, then Agent-as-a-Judge's requirement tree. Checklists appear to be the practical form of step reward for agents.

### Gaps
- No agent PRM found that was evaluated on coding-agent or OS trajectories against human step labels.
- RubricEval was not located with a confirmed arXiv id, so it is omitted.

## Q4: Evaluating agents with other agents (simulated users, adversarial probers)

### Takeaway
Simulated users are now shown to be unreliable proxies. They are over-cooperative, never walk away and leak information early, which inflates success. Changing only the user model moves scores by 9-15 points. Adversarial evaluation exists mostly as fixed injection suites (AgentDojo) rather than adaptive red-team agents.

### Cited Findings
- Sim2Real gap: 451 humans vs 31 simulators on tau-bench (165 tasks). Simulators are "excessively cooperative" and give an "easy mode" with inflated success, and more capable LLMs are not more faithful simulators. — [arXiv 2603.11245](https://arxiv.org/abs/2603.11245)
- Lost in Simulation: success shifts by up to 9 pp depending on the user LLM. Simulators miscalibrate by difficulty (underestimating on hard tasks, overestimating on moderate ones) and are the worst proxies for AAVE and Indian English speakers. — [arXiv 2601.17087](https://arxiv.org/abs/2601.17087)
- UserProxyBench: swapping the user proxy moves reward by 15.2 points. 24.4% of successful episodes violate the user spec, mostly through premature disclosure. — [arXiv 2609.38043](https://arxiv.org/abs/2609.38043)
- The tau-bench simulator always pursues the goal and cannot decline. — [arXiv 2606.20708](https://arxiv.org/pdf/2606.20708) (snippet only)
- tau2-bench gives the user tools too (dual control); performance drops in that mode. — [arXiv 2506.07982](https://arxiv.org/abs/2506.07982)
- (secondary, unverified) Meta's MIMESIS: a GPT-5.5 agent reached 63.6% with real users vs ~82-84% with frontier simulators. — [aiweekly](https://aiweekly.co/alerts/metas-mimesis-user-simulators-lift-agent-scores-nearly-5-points)
- AgentDojo: 97 tasks and 629 injection cases, scored by state checks for both utility and attack success. — [arXiv 2406.13352](https://arxiv.org/abs/2406.13352)

### Gaps
- No paper found that evaluates an adaptive red-team agent as an evaluator, checking whether its findings agree with humans.

## Q5: Multi-agent system evaluation

### Takeaway
Failure taxonomies are reliable for humans (MAST κ=0.88). Automated blame attribution is not usable yet: 53.5% at the agent level and 14.2% at the step level.

### Cited Findings
- MAST: 14 failure modes in 3 categories (system design, inter-agent misalignment, task verification). Built from 150 traces, with 1,600+ traces across 7 frameworks and an LLM annotator. — [arXiv 2503.13657](https://arxiv.org/abs/2503.13657)
- Who&When: 127 multi-agent systems. Best methods reach 53.5% agent-level and 14.2% step-level, some methods do worse than random, and o1/R1 are not usable. — [arXiv 2505.00212](https://arxiv.org/abs/2505.00212)

## Q6: What the papers leave untried

- Judges that verify state (query the DB or VM after the run) combined with trajectory reading, validated against side-effect labels. AgentRewardBench labels side effects but judges read transcripts only.
- Agent-as-a-Judge's intermediate checks as a process reward, and judge-agent self-play. Both are named as future work and not done.
- Maintainer-review-style judges calibrated on METR's labels. No one has turned the 296 reviewed PRs into a judge benchmark.
- Simulated users with the ability to walk away or refuse, calibrated to human data, plus a fidelity gate (UFS/USI) applied before benchmarks report numbers.
- Automated ABC auditing: the checklist is applied by hand.
- Adaptive adversarial-prober evaluators measured against humans.

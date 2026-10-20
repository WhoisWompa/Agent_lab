# Evaluation tooling and platform landscape for LLM apps and agents (as of 20 Oct 2026)

Scope: observability+eval platforms, the clouds' built-in evals, open-source frameworks, agent-specific, simulation and red-team tools, and tracing standards. Per-source notes are in `industry_evaluation_2026/notes/`. GitHub star counts come from the GitHub API on 2026-10-20.

## 1. What is the standard feature set in 2026, and who goes beyond it?

### Takeaway
Tracing, datasets, LLM-as-judge plus code evaluators, annotation queues, online evaluation on sampled production traffic, experiments with CI gating, and prompt playgrounds are now commodity. All the major independents and all three hyperscalers ship them, and deterministic trajectory-match evaluators come standard too. Vendors now compete on four things: agents that write evaluators or optimise prompts (Loop, Alyx, the Foundry and Google optimizers, the Opik optimizer), simulated users, judge calibration and alignment, and cheap distilled judges. Underneath, the market consolidated hard in 2025-26.

### Cited Findings
**The commodity baseline**
- Arize's vendor-written comparison of 7 platforms (AX, Phoenix, LangSmith, Braintrust, Langfuse, Weave, Opik), dated 13 Aug 2026, finds all of them have OTel/OTLP ingestion, datasets, and offline and online evals. On trajectory evals, AX, Phoenix, LangSmith and Braintrust are rated "yes"; Langfuse, Weave and Opik are rated "partial". — [Arize](https://arize.com/resources/llm-and-agent-evaluation-platforms/)
- Langfuse's 2026 releases:
  - categorical and boolean judge scores (Mar–Apr)
  - code evaluators GA (28 May)
  - GitHub Actions experiments that fail on regressions and post to PRs
  - multimodal evaluators (Aug)
  - evaluators and annotation queues exposed through its MCP server (10 Jun)
  — [Langfuse May update](https://langfuse.com/blog/2026-05-31-langfuse-may-update), [Aug update](https://langfuse.com/blog/2026-08-31-langfuse-august-update), [MCP evaluators](https://langfuse.com/changelog/2026-06-10-evaluators-via-mcp)
- LangSmith made threads (multi-turn sessions) first-class on 23 Oct 2025. It added online multi-turn evaluators for semantic intent, outcome and trajectory, plus an Insights Agent that clusters production traces. — [LangChain blog](https://blog.langchain.com/insights-agent-multiturn-evals-langsmith)

**Hyperscalers**
- Microsoft Foundry:
  - Tracing and evaluations GA "this spring". The M365 message describes evaluations that run "adhoc, continuous on production traffic and scheduled to detect drift". — [Build 2026 post, 3 Jun 2026](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/); [AZ525985](https://mc.merill.net/message/AZ525985)
  - In public preview: user simulation, multi-turn evaluation, a rubric evaluator, intelligent trace sampling, traces-to-dataset, and tracing/evals for any framework via OTel. The Agent Optimizer is in private preview. — [Build 2026 post](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/)
- AWS AgentCore Evaluations:
  - Previewed Dec 2025, GA by 31 Mar 2026.
  - Online mode samples a percentage of production traces (up to 10 evaluators per config). An on-demand API serves CI. Code evaluators are Lambdas that receive OTel spans. — [AWS blog](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations); [What's New Dec 2025](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-agentcore-policy-evaluations-preview)
- Google:
  - The evaluation service recommends "adaptive rubrics" (pass/fail rubrics generated per prompt). It also offers static rubrics, computation metrics and custom Python. Any model is supported through LiteLLM. Docs updated 2026-10-19, now branded "Gemini Enterprise Agent Platform". — [Google docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview)
  - At Next '26 (22 Apr 2026) Google added an "Optimize" pillar: Simulation, Evaluation, Observability and an Optimizer that clusters failures and suggests prompt revisions. This comes from secondary coverage only. — [pillitteri.it](https://pasqualepillitteri.it/en/news/1311/gemini-enterprise-agent-platform-google-next-2026); [TWIML](https://twimlai.com/articles/google-cloud-next-26-recap)

**Going beyond the baseline**
- *Agents that write evaluators:*
  - Braintrust Loop "can create and update prompts, scorers, facets, preprocessors, datasets, views, and automations, but has no tool to delete them". Its docs warn that auto-accept can create online scoring rules in production. — [Braintrust docs](https://www.braintrust.dev/docs/loop/index)
  - Arize's Alyx finds failing examples and builds, refines and tests evaluators. — [Arize](https://arize.com/resources/llm-and-agent-evaluation-platforms/)
- *Optimizers:* Opik's Agent Optimizer offers evolutionary, few-shot, meta-prompt and GEPA strategies. — [Comet docs](https://www.comet.com/docs/opik/agent_optimization/opik_optimizer/concepts)
- *Simulation:*
  - Hyperscalers: Foundry user simulation ([Microsoft](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/)) and Google Simulation (secondary coverage, above).
  - Voice and chat agents: Coval raised a $28M Series A in June 2026 ([TNW](https://thenextweb.com/news/coval-28m-series-a-voice-ai-testing)). Others are Cekura (formerly Vocera, renamed Mar 2025; [YC](https://www.ycombinator.com/launches/M57-cekura-formerly-vocera-testing-monitoring-for-ai-voice-agents)) and Hamming ([Hamming](https://hamming.ai/product/automated-testing/ai-voice-agents)).
  - Persona simulators: Maxim ([Lyzr roundup](https://www.lyzr.ai/?p=140045)), plus the DeepEval and MLflow ConversationSimulators.
  - Benchmark-grade simulated users: Sierra's τ-bench repo now hosts τ³-bench, with 375 tasks, a banking domain and full-duplex voice. — [GitHub](https://github.com/sierra-research/tau2-bench); [Harbor listing](https://hub.harborframework.com/datasets/sierra-research/tau3-bench/latest)
- *Cost-aware judges:*
  - Galileo's Luna-2 small models are listed at $0.02/M tokens, 0.95 F1 and 152 ms, against GPT-4o at $2.50, 0.94 F1 and 3,200 ms. These are vendor figures, and the product page instead says $0.12/M. — [Galileo docs](https://docs.galileo.ai/concepts/luna/luna); [arXiv 2602.18583](https://www.arxiv.org/pdf/2602.18583)
  - Foundry's composite evaluators batch 5–6 judges into one call "to reduce cost and latency". — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators)

**Consolidation, 2025–26**

| Date | Deal | Source |
|---|---|---|
| May 2025 | W&B → CoreWeave | [CoreWeave](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Completes-Acquisition-of-Weights--Biases/default.aspx) |
| Mar 2025 | Velvet → Arize | [SiliconANGLE](https://siliconangle.com/2025/03/13/arize-ai-acquires-velvet-expand-support-ai-observability-llm-evaluation/) |
| Aug–Sep 2025 | Humanloop team → Anthropic; platform shut 8 Sep 2025 | [TechCrunch](https://techcrunch.com/2025/08/13/anthropic-nabs-humanloop-team-as-competition-for-enterprise-ai-talent-heats-up/) |
| Jan 2026 | Langfuse → ClickHouse | [ClickHouse](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability) |
| Mar 2026 | Promptfoo → OpenAI | [OpenAI](https://openai.com/index/openai-to-acquire-promptfoo/) |
| Mar 2026 | Helicone → Mintlify (maintenance mode) | [Helicone](https://www.helicone.ai/blog/joining-mintlify) |
| Mar–May 2026 | Traceloop → ServiceNow | [Traceloop](https://traceloop.com/blog/traceloop-is-joining-servicenow) |
| May 2026 | Galileo → Cisco/Splunk | [Cisco](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo) |

Both trackers covering these deals are themselves secondary. — [DevelopersDigest, 18 Oct 2026](https://www.developersdigest.tech/blog/llm-observability-acquisitions-2026); [ai-evals.tools](https://ai-evals.tools/editorial/llm-evals-observability-company-acquisitions)

Braintrust raised $80M at an $800M valuation (ICONIQ, Feb 2026). — [TechLeap/SiliconANGLE](https://finder.techleap.nl/news/feed/braintrust-raises-80m-to-monitor-ai-models-and-agents-in-production)

**Open-source adoption (GitHub stars, 2026-10-20)**

| Repo | Stars | Licence / status |
|---|---|---|
| Langfuse | 36.1k | MIT core |
| MLflow | 28.5k | |
| Promptfoo | 26.2k | MIT |
| Opik | 22.8k | |
| OpenAI evals | 19.6k | last push Apr 2026 |
| DeepEval | 19.0k | |
| Ragas | 16.1k | moved to vibrantlabsai; last push Feb 2026 |
| lm-evaluation-harness | 14.3k | |
| Phoenix | 11.9k | ELv2 |
| garak | 9.6k | |
| OpenCompass | 7.5k | |
| OpenLLMetry | 7.5k | |
| Giskard-oss | 5.9k | |
| simple-evals | 4.7k | |
| PyRIT | 4.7k | |
| TruLens | 3.6k | |
| Laminar | 3.4k | |
| inspect_ai | 3.0k | |
| HELM | 3.0k | |
| lighteval | 2.6k | |
| tau2-bench | 2.3k | |
| openevals | 1.2k | |
| Weave | 1.1k | |
| hal-harness | 0.3k | archived |

— GitHub API

### Inferences
- The baseline now works like a checklist, so platform choice comes down to price model, licence, deployment model and lock-in risk, not features.
- "Agent that builds and edits your evals" is the 2026 differentiator. It feeds judge scores back into prompt changes automatically, which raises the stakes of judge bias (Goodhart).
- Five of the roughly 18 named independents lost independence or shut down within 18 months: Humanloop, W&B, Langfuse, Promptfoo and Galileo. Helicone and Traceloop went the same way among adjacent tools.

### Gaps
- No primary-source detail was obtained for Freeplay, HoneyHive, Vellum or Scale's enterprise eval product. Only aggregator pages were found. Vellum's reported 2026 repositioning is unverified.
- The details of Google's Next '26 Simulation and Optimizer come from secondary press, not Google docs.

## 2. How do products implement LLM-as-a-judge, and what do they say about judge reliability?

### Takeaway
Every product ships prebuilt judges (helpfulness, groundedness, task adherence and so on) plus custom rubric judges, and increasingly per-item generated rubrics (Google adaptive rubrics, Foundry's rubric evaluator). The products split on calibration:
- **Measure agreement:** most of them, including LangSmith Align Evaluator, Arize "Human vs AI", Google's autorater-quality workflow and the Langfuse calibration skill.
- **Automatically optimise the judge against human labels:** only a few, chiefly MLflow/Databricks via DSPy SIMBA, and Google's "tune the autorater".

Vendor docs warn about reliability but publish almost no judge-agreement numbers.

### Cited Findings
**Prebuilt and rubric judges**
- *Foundry* judges are prebuilt and output pass/fail, or a 1-5 score thresholded to pass/fail. The recommended judge is the GPT-5.6 family, with gpt-5.6-luna as the low-cost option. — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators)
- *Foundry's rubric evaluator* (preview) generates context-aware criteria weighted across task success, tone, safety, cost and latency. — [Build 2026](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/)
- *AWS* built-in judges use "fixed prompts, models, and scoring criteria" to keep results consistent, and reason before scoring. The judge model is not named. — [AWS](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations)
- *Google adaptive rubrics* first generate rubrics per data point, which you can review and customise, then autorate against them. — [Google blog, Jun 2025](https://cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage); [docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview)
- *DeepEval* offers four judge styles:
  - G-Eval: criteria, then generated steps, then a score.
  - DAG: decision-tree judges that can be deterministic.
  - JevEval: a "System One model" with calibrated probabilities.
  - The docs warn: "We CANNOT guarantee that evaluations will work as expected when using a custom model". — [DeepEval docs](https://deepeval.com/docs/metrics-introduction)

**Calibration and alignment**
- *LangSmith Align Evaluator:* experts label runs in an annotation queue, the judge prompt is tested against those labels and revised, for offline or online evaluators. — [LangChain docs](https://docs.langchain.com/langsmith/improve-judge-evaluator-feedback). Potato's docs call this 100–200 gold-label loop the standard approach and compute Cohen's κ. — [Potato](https://potatoannotator.readthedocs.io/en/latest/agent-evaluation/judge_alignment/)
- *Arize* builds a labelled dataset from traces and runs a "Human vs AI" evaluator to measure judge accuracy, iterating to close the gap. — [Arize docs](https://arize.com/docs/ax/cookbooks/evaluate/align-llm-evals-with-human-judgment)
- *MLflow/Databricks* `make_judge` alignment:
  - Experts correct judge outputs, then the SIMBA optimiser (DSPy) rewrites the judge's instructions.
  - It needs at least ~10 traces, with 50–100 better.
  - Databricks claims a 30–50% agreement improvement (vendor claim).
  - It does not support multi-turn judges. — [Databricks docs](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges)
- *Google* frames autorater quality as something you check against "a benchmark dataset of human-rated examples". You improve it by refining criteria and CoT, or "bring and tune the autorater with your own reference data". — [Google blog](https://cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage)
- *Langfuse* has an LLM-as-a-Judge calibration skill (with Codex) that reports accuracy, F1, precision, recall and cost against human labels. — [Langfuse May 2026](https://langfuse.com/blog/2026-05-31-langfuse-may-update)

**What vendors and reviewers say about reliability**
- *OpenAI graders doc:*
  - Warns of "grader hacking": high model-grader scores with poor expert evaluations. Observability for it is "planned" but doesn't yet exist.
  - Recommends meta-evaluating graders against expert ground truth and checking rank order, plus few-shot strong/fair/weak examples.
  - Non-numeric outputs default to 0. — [OpenAI graders](https://developers.openai.com/api/docs/guides/graders)
- *AWS* says LLM judges are unreliable for exact-match checks (use code instead). For inconsistent custom judges it advises specific instructions, distinct score levels and lower temperature, and calibrating with SMEs. — [AWS](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations)
- *Patronus TRAIL* contains 148 traces with 841 annotated errors. The best model, Gemini 2.5 Pro, scored "a mere 11%" at localising errors in agent traces. — [arXiv 2505.08638](https://arxiv.org/html/2505.08638v2)
- *Independent price comparison:* none of Braintrust, Langfuse, Opik or Promptfoo "measures whether the LLM judge agrees with human reviewers" out of the box. It cites arXiv 2604.22891 on self-preference bias. — [beri.net, Aug 2026](https://www.beri.net/article/braintrust-vs-langfuse-vs-promptfoo-llm-eval-regression-gate-2026). (This conflicts partly with Langfuse's calibration skill, which shipped in May 2026.)
- *DeepEval/Confident AI* judge metrics "go unchecked against human labels". — [shurco.ai guide](https://shurco.ai/guides/best-ai-agent-evaluation-tools/)

### Inferences
- Calibration has become a recognised workflow: label a few hundred items, compute agreement, revise. It is still mostly manual, though, and only MLflow automates prompt optimisation of the judge.
- No vendor publishes per-evaluator human-agreement statistics for its prebuilt agent judges, so "prebuilt judge" quality is unverified marketing.
- The AWS guidance is "fixed judge for consistency", while Galileo, Foundry and MLflow let the judge change. That is a real tension: a fixed judge resists drift, and a tuned judge fits the domain better.

### Gaps
- No quantitative judge-vs-human agreement figures were found for any hyperscaler built-in agent evaluator (Foundry, AgentCore, Vertex).
- I found no independent replication of MLflow's 30–50% claim or of Luna-2's F1.

## 3. What agent-specific evaluators exist, and how are they validated?

### Takeaway
The converged agent-eval vocabulary has four parts:
- **Outcome:** task or goal completion.
- **Policy:** task or instruction adherence.
- **Process:** tool selection, argument/input accuracy, tool-output utilisation, tool-call success, plan quality and adherence, step efficiency.
- **Deterministic trajectory match against a reference:** exact, in-order or any-order, with precision and recall. Microsoft, Google and AWS all ship these same three modes.

Validation is weak. Products offer ground-truth matchers and SME calibration advice, but publish no evaluator accuracy. Research (TRAIL, HAL) shows LLM judges miss many trace errors and shortcuts.

### Cited Findings
- *Microsoft Foundry:*
  - System-level: Task Completion, Customer Satisfaction (1-5 over six dimensions), Task Adherence, Intent Resolution, and Task Navigation Efficiency (deterministic: exact_match, in_order_match or any_order_match, plus precision, recall and F1).
  - Process-level: Tool Call Accuracy, Tool Selection, Tool Input Accuracy (six strict criteria), Tool Output Utilization, Tool Call Success.
  - Composites: Output Quality and Tool Use Quality.
  - These evaluators do not work on Foundry's own Bing, Code Interpreter, Azure AI Search or Web Search tools. Many are still in preview.
  — [Microsoft Learn, updated 2026-10-08](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators)
- *AWS AgentCore:*
  - Session: Goal Success Rate, using natural-language `assertions`.
  - Tool: Tool Selection Accuracy and Tool Parameter Accuracy.
  - Trajectory Exact, In-Order and Any-Order Match, using `expected_trajectory`.
  - Eleven trace-level quality and safety judges.
  — [AWS](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations)
- *Google:* trajectory_exact_match, trajectory_in_order_match, trajectory_any_order_match, trajectory_precision, trajectory_recall and trajectory_single_tool_use, plus latency and failure. The docs label this Pre-GA. — [Google docs, updated 2026-10-19](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-agents)
- *DeepEval:* trajectory-level Task Completion, Step Efficiency, Plan Adherence and Plan Quality; component-level Tool Correctness and Argument Correctness. — [DeepEval](https://deepeval.com/docs/metrics-introduction)
- *OpenAI* trace grading scores a whole trace: right tool, correct handoff, policy violations. — [OpenAI](https://developers.openai.com/api/docs/guides/agent-evals)
- *LangSmith* has thread-level trajectory evaluators ([LangChain](https://blog.langchain.com/insights-agent-multiturn-evals-langsmith)). The OSS agentevals library provides trajectory match and judge evaluators (752 stars, MIT, [GitHub](https://github.com/langchain-ai/agentevals)).
- *Side effects and state checks:*
  - τ-bench grades the final database state after a conversation with a simulated user ([Sierra](https://github.com/sierra-research/tau2-bench)).
  - Anthropic recommends grading outcomes (environment state), not paths, and reading transcripts to validate graders ([Anthropic](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)).
  - AWS code evaluators receive OTel spans for deterministic business-rule checks ([AWS](https://aws.amazon.com/blogs/machine-learning/build-custom-code-based-evaluators-in-amazon-bedrock-agentcore/)).
- *Agentic judges:*
  - Patronus Percival is framed as an agent that tracks every event in a trajectory rather than an LLM-as-judge. It claims 20+ failure modes and cut analysis from ~1 hour to 1–1.5 min (vendor claim). — [VentureBeat](https://venturebeat.com/ai/patronus-ai-debuts-percival-to-help-enterprises-monitor-failing-ai-agents-at-scale)
  - Anthropic Managed Agents "Outcomes" runs a separate-context rubric grader that feeds failures back for retry (public beta, May 2026). — [Claude docs](https://platform.claude.com/docs/en/managed-agents/define-outcomes)
- *Validation evidence:*
  - TRAIL: best model 11% at localising trace errors. — [arXiv](https://arxiv.org/html/2505.08638v2)
  - HAL (ICLR 2026): 21,730 rollouts cost ~$40k. LLM-assisted log inspection found agents searching HuggingFace for answer keys and misusing credit cards. Higher reasoning effort lowered accuracy in most runs. — [ICLR](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a0928f924a344aaebbb7f6cd8d56e34c-Abstract-Conference.html)
  - The hal-harness repo was archived in Jul 2026 (GitHub API).

### Inferences
- The trajectory-match metrics are identical across the three clouds, which suggests a de facto standard. But they all need a reference trajectory, which most production teams do not have. They also conflict with Anthropic's "grade outcomes, not paths" advice.
- Process judges (tool input accuracy, output utilisation) are single LLM calls over a trace. Given TRAIL's 11%, they are likely to be weakest on long traces. Agentic judges (Percival, Outcomes graders, Inspect Scout-style transcript scanners) are the vendors' response.

### Gaps
- No vendor publishes validation (agreement with human labels) for its agent evaluators.
- I found no side-effect evaluator (one that checks real external state changes) as a named built-in in any platform. Side effects are handled by custom code evaluators or by benchmark environments.

## 4. What do practitioners and reviewers criticise?

### Takeaway
The recurring complaints:
- vendor lock-in and platform death (Humanloop, OpenAI Evals, Helicone)
- per-score and per-trace pricing that makes judge-heavy suites expensive
- judge token cost
- generic prebuilt metrics giving false confidence
- unvalidated judges
- unstable tracing standards
- agent features still in preview or not working with hosted tools

### Cited Findings
- *Lock-in and platform risk:*
  - OpenAI notified users on 3 Jun 2026 that Evals is deprecated: read-only from 31 Oct 2026, dashboard and API shut down 30 Nov 2026. Graders are "part of this transition", and the migration target is Promptfoo, which OpenAI now owns. — [OpenAI deprecations](https://developers.openai.com/api/docs/deprecations); [cookbook](https://developers.openai.com/cookbook/examples/evaluation/moving-from-openai-evals-to-promptfoo)
  - Humanloop users got about 6 weeks: billing stopped 30 Jul 2025 and the platform shut 8 Sep 2025. — [DevelopersDigest](https://www.developersdigest.tech/blog/llm-observability-acquisitions-2026)
  - Portability advice: instrument with OTel, keep your own trace copy, keep evals in the repo, prefer MIT/Apache licences. Phoenix's ELv2 licence is flagged as different. — [same](https://www.developersdigest.tech/blog/llm-observability-acquisitions-2026)
- *Cost:*
  - For a 600k-score/month workload: Braintrust Pro ≈ $1,074, Langfuse Cloud Core ≈ $115, Opik Cloud ≈ $44, Promptfoo $0. Judge-model token costs "often exceed the platform fee".
  - "Braintrust meters the thing it wants you to do more of": adding a fourth scorer raises the bill about 28%.
  — [beri.net](https://www.beri.net/article/braintrust-vs-langfuse-vs-promptfoo-llm-eval-regression-gate-2026)
  - LangSmith's seat pricing hurts teams with many occasional reviewers. One guide reports $5 per 1k traces for 14-day retention (unverified). — [shurco.ai](https://shurco.ai/guides/best-ai-agent-evaluation-tools/)
- *CI gating is weaker than marketed:* Braintrust's eval-action comments on the PR but does not block; Langfuse only fails if your script raises; Promptfoo exits with code 100 on any failure. — [beri.net](https://www.beri.net/article/braintrust-vs-langfuse-vs-promptfoo-llm-eval-regression-gate-2026)
- *Generic metrics:* Hamel Husain answers "No" to whether teams should use ready-to-use metrics. He says they waste time and create false confidence, and recommends error analysis, binary failure modes and judges validated on ~100 labels. — [hamel.dev](https://hamel.dev/blog/posts/evals-faq/should-i-use-ready-to-use-evaluation-metrics.html); [talk deck](https://hamel.dev/blog/posts/revenge/images/The_Revenge_of_the_Data_Scientist.pdf)
- *Judge reliability:*
  - HN commenters: "your judge llm can [hallucinate] too… you need to validate your judges", and same-family models self-prefer. — [HN 44715163](https://news.ycombinator.com/item?id=44715163)
  - A 2026 article citing Browserbase/Microsoft Research reports WebVoyager's judge with ≥45% false positives. This is a secondary source. — [DEV](https://dev.to/max_quimby/your-verifier-is-a-confident-liar-26pc)
- *Agent support gaps:*
  - Foundry tool evaluators have limited support for Bing, Code Interpreter, Azure AI Search and Web Search, and many agent evaluators are still in preview. — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators)
  - Google agent evaluation is Pre-GA. — [Google](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-agents)
  - MLflow judge alignment does not support multi-turn judges. — [Databricks](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges)
  - Arize rates Langfuse, Weave and Opik trajectory support as "partial". — [Arize](https://arize.com/resources/llm-and-agent-evaluation-platforms/)
- *Standards instability:* OTel GenAI conventions are still "Development". They moved to their own repo in Jun 2026 (deprecated in semconv v1.42.0), and agent spans changed in v1.41. — [Greptime](https://www.greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions); [Dash0](https://www.dash0.com/knowledge/opentelemetry-genai-semantic-conventions-explained). A lone contrary claim of stabilisation is unconfirmed.
- *Self-hosting burden:* Langfuse needs Postgres, ClickHouse, Redis, S3 and two containers, and RBAC and audit sit behind an enterprise key. — [beri.net](https://www.beri.net/article/braintrust-vs-langfuse-vs-promptfoo-llm-eval-regression-gate-2026)
- *Comparison content is mostly vendor SEO:* Arize, Maxim, Latitude, Confident AI, Future AGI, Giskard and Coval each rank themselves highly. — e.g. [Maxim](https://www.getmaxim.ai/articles/top-5-platforms-for-ai-agent-evaluation-in-2026/), [Coval](https://www.coval.ai/blog/hamming-vs-cekura)

### Inferences
- "Eval drift" shows up in two forms: judges change when vendors swap models (Foundry's recommended judge moved to the GPT-5.6 family), and conventions churn. Pinning the judge model version is a practical necessity.
- Lack of ground truth is the root problem. The trajectory-match evaluators need references, and the judges need human labels; both cost labour that tools do not remove.

### Gaps
- Reddit threads weren't surfaced by search, so practitioner sentiment comes from HN, blogs and independent comparisons. Systematic data on "flaky evals" (variance across repeated judge runs) was not found.

## 5. What have OpenAI, Google, Microsoft and AWS shipped in 2025-26, and what does it do to independents?

### Takeaway
Microsoft, AWS and Google now each ship a full agent-eval stack: built-in agent judges, trajectory matchers, online evaluation on production traces, simulation and optimizers, all framework-agnostic through OTel. OpenAI went the other way. It is shutting its hosted Evals platform (30 Nov 2026) after buying Promptfoo and pointing users at that open-source CLI. Anthropic offers only a light Console eval tool and an in-runtime rubric grader.

The independents are squeezed. Several were acquired or absorbed into observability, security and data vendors (ClickHouse, Cisco/Splunk, ServiceNow, CoreWeave). The survivors (Braintrust, LangSmith, Arize) differentiate on cross-cloud neutrality, eval UX, agents that write evals, and funding.

### Cited Findings
- *OpenAI:*
  - Trace grading and datasets/eval runs for agents. — [OpenAI](https://developers.openai.com/api/docs/guides/agent-evals)
  - Graders: string_check, text_similarity, score_model, python, multi. — [OpenAI](https://developers.openai.com/api/docs/guides/graders)
  - Promptfoo acquisition announced 9 Mar 2026, to be integrated into OpenAI Frontier; OpenAI says it will stay open source. — [OpenAI](https://openai.com/index/openai-to-acquire-promptfoo/); [TechInformed](https://techinformed.com/openai-moves-to-bring-promptfoo-into-frontier/)
  - Evals and Agent Builder shut down 30 Nov 2026. — [deprecations](https://developers.openai.com/api/docs/deprecations)
- *Microsoft:* see Q1 and Q3 above. Foundry evaluations and tracing are GA (spring 2026), and the AI Red Teaming Agent is GA. — [Tech Community](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/-/4467885)
- *AWS:* AgentCore Evaluations, preview Dec 2025 and GA Mar 2026. It also offers the DeepEval and AutoEval third-party evaluator libraries inside AgentCore. — [AWS docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/third-party-evaluators.html)
- *Google:*
  - Gen AI evaluation service: batch evaluation, autorater validation and tuning, rubric metrics, agent trajectory eval (Jun 2025). — [Google](https://cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage)
  - Vertex rebranded to Gemini Enterprise Agent Platform with Simulation, Evaluation, Observability and Optimizer (Apr 2026, secondary coverage). — [TWIML](https://twimlai.com/articles/google-cloud-next-26-recap)
- *Anthropic:*
  - Console Evaluate tab: test-case generation, side-by-side comparison, 5-point SME grading (since Jul 2024). — [Anthropic](https://www.anthropic.com/news/evaluate-prompts)
  - Managed Agents Outcomes rubric grader (2026). — [Claude docs](https://platform.claude.com/docs/en/managed-agents/define-outcomes)
  - Absorbed the Humanloop team (Aug 2025). — [TechCrunch](https://techcrunch.com/2025/08/13/anthropic-nabs-humanloop-team-as-competition-for-enterprise-ai-talent-heats-up/)
- *Independents' response:*
  - Funding: Braintrust $80M Series B. — [TechLeap](https://finder.techleap.nl/news/feed/braintrust-raises-80m-to-monitor-ai-models-and-agents-in-production)
  - Arize's Alyx is on Google Cloud Marketplace. — [Arize](https://arize.com/resources/llm-and-agent-evaluation-platforms/)
  - Exits: Langfuse to ClickHouse, Galileo to Cisco/Splunk, Traceloop to ServiceNow. — [DevelopersDigest](https://www.developersdigest.tech/blog/llm-observability-acquisitions-2026)
  - Status of others: Patronus's homepage refocused on RL research; Helicone is in maintenance mode; Datadog and PostHog relabelled their products as agent/AI observability. — [same](https://www.developersdigest.tech/blog/llm-observability-acquisitions-2026)

### Inferences
- Hyperscaler evals are good enough for single-cloud shops and are bundled with tracing they already pay for. That pushes independents toward multi-cloud and multi-model neutrality, which OpenAI's ownership of Promptfoo complicates.
- OpenAI's exit from hosted evals, despite owning the model, suggests eval definitions are moving into code repos and CI (Promptfoo, Inspect, pytest-style DeepEval), with platforms as viewers. Separately, voice agents, security red-teaming and judge distillation remain niches where specialists (Coval, Galileo-style SLM judges, Lakera/HiddenLayer) keep their value.

### Gaps
- I did not verify whether Anthropic has a hosted eval or observability product beyond the Console tool and Outcomes. Search found none, which is not proof of absence.
- Market share and revenue figures for independents weren't found. Deal prices are mostly unverified blog estimates.

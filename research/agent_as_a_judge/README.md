# Agent-as-a-judge literature survey

Research run of 2026-10-20. Six Opus researchers each covered one slice of the
evaluation literature (2018 to October 2026); a seventh wrote the report.

| Path | What it is |
|---|---|
| `discussion_summary.md` | Design points from the session discussion after the research. |
| `report.md` | The synthesis: what has been tried, where each method breaks, what is untried. Start here. |
| `research_notes/` | One summary per slice, with inline arXiv ids. Each is the researcher's own write-up of its slice. |
| `notes/` | One note per paper, ~300 files, named `<YYYY-MM> <short title>.md`. Frontmatter has `arxiv` and `category`. `_TEMPLATE.md` is the shape. |

Categories in `notes/`:

| `category` | Slice |
|---|---|
| `agent-as-judge` | Agent-as-a-Judge (Zhuge et al. 2024) and its descendants |
| `llm-judge-foundations` | LLM-as-a-judge basics, biases, attacks, mitigations, meta-evaluation benchmarks |
| `trained-judges-reward-models` | Fine-tuned judges, reward models, critics, process reward models, reasoning judges |
| `agent-evaluation-benchmarks` | Agent benchmarks, verifier failures, trajectory and step-level judging, simulated users |
| `alternative-paradigms` | Debate, arenas, consistency checks, execution, abstention, judge-the-judge |
| `self-evolving-tests` | Generated and adversarial test sets, self-improving judges, evaluator loops |

Numbers marked "recalled" or "unverified" in a note came from the researcher's
memory or a search snippet, not from the paper fetched in session. Check before quoting.

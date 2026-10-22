# Verification-first harnesses, October 2026

Research run of 2026-10-21. Six researchers each covered one slice of the
2025-2026 shift from "how many agents" to "what does the harness verify and
what can each agent observe"; a seventh wrote the report. Extends the
conclusion of `../multiagent_llm_systems/report.md`.

| Path | What it is |
|---|---|
| `report.md` | The synthesis: what has been found per slice, then the open questions in two layers (what the papers admit, what is visible only by comparing them). Start here. |
| `research_notes/` | One note per slice, with URLs inline. |

Slices in `research_notes/`:

| File | Slice |
|---|---|
| `stop_rules.md` | Statistical and adaptive stop rules replacing fixed rounds and agent-declared done |
| `aggregation_and_selection.md` | Externally grounded aggregation, selection over independent draws, wrong-consensus detection |
| `message_verification.md` | Checking or grounding a claim before other agents act on it; schemas, provenance labels, latent-channel integrity |
| `false_completion_and_gates.md` | Measured false-success rates and the execution or state gates proposed against them |
| `information_structure.md` | Experiments varying what each agent sees or is told: hidden tests, rubrics, abort options, blind judges |
| `industry_adoption.md` | What production frameworks and frontier labs shipped, Jan 2025 to Oct 2026 |

Papers are preprints unless a venue is named. Figures marked "unverified" or
"secondary" in a note were not confirmed against the primary page in session.

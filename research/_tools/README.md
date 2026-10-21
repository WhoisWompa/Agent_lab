# research/_tools

The pipeline that turns a folder of PDFs into notes, topic links and the graphify graph. The main session runs it through the `paper-ingest` skill; the reader is `.claude/agents/paper-reader.md`. The topic registry is `research/topics.md`.

| File | What it does |
|---|---|
| `extract_pdf_text.py` | `uv run --with pypdf python -I extract_pdf_text.py <pdf folder> <out folder>`. One `.txt` per PDF (same relative path) plus `index.json` with pages and token estimates. Readers read the `.txt`, never the PDF. |
| `paper_note_brief.md` | How a note is written: the idea and the limitations with the number or reason beside every claim, no experimental procedure, 400 to 700 words, topics from the registry. The paper-reader agent reads it before every note. |
| `topic_assignment_brief.md` | For bulk reclassification only: an Opus agent reads thirty notes against the registry and writes a JSON of assignments and proposals. Used on 2026-10-21 to classify all 384 notes when the registry was created. |
| `apply_assignments.py` | `python -I -X utf8 research/_tools/apply_assignments.py <out.json> ...` from the repo root. Writes each JSON assignment into the note's `topics:` field, drops names not in the registry, prints proposals for the main session to rule on. |
| `build_topics.py` | `python -I -X utf8 research/_tools/build_topics.py` from the repo root. Reads the registry and every note's `topics:`; rewrites each note's `## Topics` section, writes one `Topic - <name>.md` per registry topic and the `Topics.md` overview, removes topic notes no longer in the registry. Idempotent. Run after any note changes. |

Graph: `graphify update . --force` then `graphify cluster-only . --no-label` from the repo root (markdown quick-scan, no LLM, about a minute). Output in `graphify-out/` (gitignored). Query with `graphify query "<question>"`, `graphify explain "<node>"`, `graphify path "<A>" "<B>" --undirected`.

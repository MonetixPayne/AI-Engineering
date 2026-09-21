## 2026-09-21: AI Engineering Development Plan — 1 Hour a Day (ai-engineering-hub spine)

#learning/ai-engineering #plan/24-week #proof-of-work #personal

Source repo: https://github.com/patchy631/ai-engineering-hub (115 project folders: 22 beginner, 48 intermediate, 23 advanced, plus `ai-engineering-roadmap`, `courses/anthropic-academy-courses`).
Scope: personal development, outside DeepL. Complements (does not replace) [[2026-06-16-applied-ai-12-week-path]] — that plan is the evals sprint; this one is the full engineering spine with the repo as the exercise book.

---

## Assumptions (stated, not verified — correct me if wrong)

1. You already write and read Python at agent-assisted level. You do **not** need CS50p or Khan Academy math. **Skip roadmap steps 1-3 and 5.** They are for career-changers, not for someone who ships agent systems.
2. Your gap is not "what is an LLM". Your gap is **production engineering rigor**: retrieval quality, evaluation, cost, latency, failure handling, deployment.
3. Your moat is GTM. The market does not need another AI engineer. It needs very few people who can say "I built the revenue system *and* I can prove it works." So every module below ends in a **number**, not a demo.
4. Budget: 1 hour/day, 5 days a week, 6th day flex. 24 weeks -> ~120 hours. That is enough for 6 real artifacts, not 115 tutorials.

---

## The daily 1-hour loop (non-negotiable shape)

| Minutes | Block | Rule |
|---|---|---|
| 0-10 | READ | One doc, one repo README, or one paper section. No videos over 10 min. |
| 10-50 | BUILD | Type code. Never copy-paste a whole folder. Clone the hub project, then **rebuild the core file from scratch** in your own repo. |
| 50-60 | LOG | `git commit` + one line: what you measured, what broke. This line is the portfolio. |

One public repo: `ai-engineering-proof`. One folder per phase. Each phase ends with a README containing **a table of numbers** (accuracy, latency p50/p95, cost per 1k calls) and a 300-word writeup.

Self-check, forever: **no eval, no ship. No number, no claim.**

---

## Master plan — 6 phases, 24 weeks

| # | Weeks | Module | Hub projects to work through | What you prove (artifact) | Market outcome | GTM implication | Your example project |
|---|---|---|---|---|---|---|---|
| 0 | 1-2 | **Engineering hygiene + the raw API loop.** `uv`, typed config, structured outputs, streaming, retries, token/cost accounting. No frameworks yet. | `streaming-ai-chatbot`, `local-chatgpt`, `gemma3-ocr` (run one local model once, then move on) | A small library: `llm.py` with typed calls, retry, cost logging. Cost printed per run. | You stop being a prompt user and become someone who owns the call path. Baseline for every interview. | You can price any GTM automation before building it. "This play costs €0.004 per lead" is a sentence almost no GTM lead can say. | **Lead-enrichment CLI**: company URL in, typed JSON firmographics out, cost + latency logged per call. |
| 1 | 3-6 | **Retrieval that actually retrieves.** Chunking, embeddings, hybrid search, rerank, document parsing, citations. The single highest-value skill in applied AI. | `simple-rag-workflow` -> `modernbert-rag` -> `rag-with-dockling` -> `colbert-rag` -> `trustworthy-rag`, `fastest-rag-milvus-groq` (latency), `github-rag` | Retrieval benchmark: 50 Q/A pairs over **your own** corpus, recall@k and MRR for 3 configs (naive / hybrid / +rerank). | Retrieval quality is the top real-world failure in enterprise AI. Showing a measured retrieval sweep puts you above most "RAG demo" candidates. | Every GTM knowledge problem is a retrieval problem: battlecards, pricing rules, call notes, past deals. You can now say why an AI answer was wrong and fix it structurally. | **Deal-memory RAG**: chunk 200 anonymised call notes + a pricing doc; answer "what objections lose us mid-market deals" with citations. |
| 2 | 7-9 | **Evals and observability.** Golden sets, LLM-as-judge with rubric, regression gates in CI, tracing, drift. Do this *before* agents — on purpose. | `eval-and-observability` (Opik), `trustworthy-rag`, `guidelines-vs-traditional-prompt`, one model bake-off e.g. `gpt-oss-vs-qwen3` (as an *eval exercise*, not content) | Eval harness with CI gate: PR fails if judged quality drops. Public dashboard screenshot + the judge rubric. | **This is your differentiator.** Anthropic/OpenAI forward-deployed and Applied AI roles screen hard for it. Most candidates have none. | Turns AI GTM claims into defensible numbers for a CRO: "reply-rate uplift with a 92%-accurate qualifier, measured weekly, regression-gated." Kills pilot-purgatory arguments. | **SDR message qualifier eval**: 80 labelled outreach drafts, rubric judge, weekly score trend, gate at 0.85. |
| 3 | 10-14 | **Agents and workflows.** Anthropic's composable patterns first, then one framework. Tool use, routing, planning, human-in-the-loop, failure recovery. | Read Anthropic "Building Effective Agents", then `agentic_rag`, `rag-sql-router`, `corrective-rag`/`firecrawl-agent`, `autogen-stock-analyst` **or** `hotel-booking-crew` (pick one framework, not three), `web-browsing-agent` | Agent with a written **failure taxonomy** and recovery paths, scored on the Phase-2 harness. Show where you chose a workflow over an agent and why. | Hiring signal has moved from "can you call an agent framework" to "do you know when *not* to use an agent". Cost/latency discipline reads as seniority. | Multi-step revenue plays: research -> qualify -> route -> draft -> log to CRM. You can scope which steps should be deterministic, which agentic — the exact judgement GTM leaders lack. | **Account-research crew**: news + site + CRM history -> a 5-bullet pre-call brief with a confidence score and an escalate-to-human rule. |
| 4 | 15-18 | **MCP, memory, and context engineering.** Build a server (not just consume), tool design, permissions, persistent memory, knowledge graphs. | `llamaindex-mcp`, `cursor_linkup_mcp`, `mcp-agentic-rag`, `ultimate-ai-assitant-using-mcp`, `zep-memory-assistant` / `graphiti-mcp`, `context-engineering-workflow` | Your own published MCP server (npm/PyPI or repo) with tool docs, auth notes, and an eval of tool-selection accuracy. | Currently scarce and highly visible. A working, documented MCP server is the strongest single portfolio object in late 2026. | You can expose CRM/enrichment/pricing as safe tools for any agent. This is the real "AI-native GTM stack" job — plumbing revenue data into assistants, with permissions. | **`gtm-mcp`**: tools for `search_accounts`, `get_deal_history`, `draft_followup`, read-only by default, write actions gated. |
| 5 | 19-21 | **Production: serve, deploy, guard, cost.** APIs, containers, concurrency, caching, rate limits, PII, prompt-injection, on-call reality. | `deploy-agentic-rag` (LitServe), `groundX-doc-pipeline`, `openclaw-secure-deployment`, `parlant-conversational-agent` (compliance/guardrails) | A deployed endpoint with a load test: p50/p95 latency, cost per 1k requests, cache hit rate, and one documented incident + fix. | Separates "notebook people" from engineers. Unlocks staff/lead-level and forward-deployed titles rather than analyst-adjacent ones. | You can promise an SLA and a unit cost to a revenue org, and survive the security review. That is the blocker most GTM AI projects die on. | **Qualifier-as-a-service**: the Phase-2 qualifier behind an authenticated API, rate-limited, cached, with a status page. |
| 6 | 22-24 | **Model-level depth + capstone.** Enough fine-tuning and reasoning to have real opinions: when to tune vs prompt vs retrieve; distillation for cost. | `DeepSeek-finetuning` (Unsloth), `knowledge distillation`, `grpo-finetuning-qwen3` (read, tune only if GPU budget), `Build-reasoning-model` (conceptual) | One fine-tuned small model beating a prompted frontier model on **your** narrow task at 10x lower cost — with the eval to prove it. | Very few applied people can defend the tune-vs-prompt decision with their own data. It reads as senior judgement, not hype. | Cost is the reason GTM AI stalls at scale. Showing 10x cost reduction on a repetitive scoring task is a board-level argument. | **Lead-scoring SLM**: distil your qualifier into a 4B model; report accuracy delta and cost delta vs the frontier baseline. |

---

## What to skip in that repo (deliberately)

- **All the "X vs Y" model bake-offs** (`sonnet4-vs-o4`, `qwen3_vs_deepseek-r1`, `o3-vs-claude-code`, `minimaxm2-vs-...`). These are newsletter content with a 3-month shelf life. Use **one** of them, once, as an evals exercise in Phase 2.
- **The thinking-UI clones** (`deepseek-thinking-ui`, `qwen3-thinking-ui`, `gpt-oss-thinking-ui`) — same app three times.
- **OCR variants** — do one (`gemma3-ocr`), skip the other three.
- **Toy crews** (`flight-booking-crew`, `book-writer-flow`, `ai-podcast-generation`) unless you want a fun Friday.
- **`siamese-network`, `train-yolo26-object-detection`, `attention-is-all-you-need-impl`** — classical CV / from-scratch transformers. Interesting, not on your path. Karpathy's series is optional enrichment, not a requirement for applied roles.

Rough count: the plan uses ~30 of 115 folders. That is the point.

---

## Ordering logic (why this sequence and not the repo's)

1. **Retrieval before agents.** A bad agent on good retrieval is fixable. A great agent on bad retrieval is unfixable and undebuggable.
2. **Evals before agents, not after.** If you learn agents first you will build three of them and be unable to say whether any works. Phase 2 is the spine that every later phase reports into.
3. **MCP after agents.** You cannot design good tools until you have watched an agent misuse bad ones.
4. **Deployment before fine-tuning.** Serving skills get used in every job; fine-tuning gets used in few. Fine-tuning last, and only as a cost argument.
5. **Fundamentals (math, from-scratch transformers) never.** They are a research path. You are on an applied path with a GTM moat. Depth there is a detour.

---

## Checkpoints — how you know it worked

| Week | Gate | Pass condition |
|---|---|---|
| 6 | Retrieval | A table comparing 3 retrieval configs on your own corpus, with recall@k. |
| 9 | Evals | CI that blocks a merge on a quality regression. Screenshot the failing run. |
| 14 | Agents | A written failure taxonomy with recovery paths, plus one "I used a workflow instead, because..." note. |
| 18 | MCP | A published MCP server someone else can install from your README alone. |
| 21 | Production | Live endpoint + load-test numbers + one incident writeup. |
| 24 | Capstone | Cost/accuracy table: tuned small model vs prompted frontier model. |

**Publish cadence:** one short writeup at each gate (6 posts in 24 weeks). Title them from the number, not the tech: "Reranking moved recall@5 from 0.61 to 0.88 on 200 sales call notes." That headline style is what makes the GTM+engineering combination legible to hiring managers.

---

## The positioning this buys you

After 24 weeks you are not "a GTM person who learned AI". You are:

> *Someone who builds revenue systems with agents, and proves they work with evals, cost, and latency numbers.*

Roles that opens: Applied AI Engineer / Forward-Deployed Engineer (Anthropic, OpenAI, Sierra, Decagon, LangChain-type vendors), AI GTM Engineer / Head of GTM Engineering (Clay, Unify, 11x-type vendors), and AI Solutions Architect on the revenue side at any enterprise vendor. The scarce combination in all three is exactly yours: domain fluency in revenue **plus** production rigor.

Risk to manage: 1 hour/day only works if the artifact, not the streak, is the scorecard. Miss days. Do not miss gates.

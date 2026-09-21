# Phase 0 — Foundations (weeks 1-2, 10 sessions of 1 hour)

**Artifact:** a CLI that turns a company URL into validated JSON, and reports what each call cost
and how long it took. **Gate:** a results table over 20 real URLs with p50/p95 latency, cost per
1,000 calls, schema-valid rate, and error rate.

Everything later in this repo imports `enrich/llm.py`. Build it properly once.

## Rules for this phase

1. Type the code. Do not paste a finished file from anywhere, including from an assistant.
2. One commit per session, message says what you measured or what broke.
3. Personal API key only, in `.env`, never a work key. `.env` is gitignored.
4. Use a cheap model. The whole phase should cost under 3 dollars.

## The ten sessions

| Day | Build | Verify before you commit |
|---|---|---|
| D1 | `uv sync`. `config.py` with pydantic-settings. In `llm.py`, one raw API call that returns text. | `uv run python -c "from enrich.llm import complete; print(complete('say hi'))"` prints a reply. |
| D2 | `schemas.py` with the `Company` model. Switch the call to structured output and validate the response into it. | Feed the model deliberately thin input. It must fail validation loudly, not return a half-filled object. |
| D3 | `cost.py` with a price table and `cost_usd()`. Write `tests/test_cost.py` first. | `uv run pytest tests/test_cost.py` green. Unknown model raises instead of returning 0.0. |
| D4 | `calllog.py`. Every call appends one JSONL line: tokens, cost, latency_ms, ok, error. | Run three calls, then `wc -l calls.jsonl` shows 3 and the costs are non-zero. |
| D5 | Timeout, retry with exponential backoff and jitter, typed errors. `tests/test_retry.py` with respx. | `uv run pytest` green, including "three 500s raises and logs a failure line". |
| D6 | `fetch.py`: one page, 10s timeout, strip nav and script, cap at 6k chars. | Run it over the 5 URLs in `urls.csv`. Note which fail and why. Bot protection and JS-only pages are the normal case, not an edge case. |
| D7 | Wire it end to end: URL -> page text -> prompt -> validated `Company`. | One URL produces correct JSON. Read the output against the real homepage and check every field yourself. |
| D8 | `cli.py` with typer: `enrich one` and `enrich batch --concurrency 5`. Batch must survive a failing URL. | `uv run enrich batch urls.csv` finishes with one URL deliberately broken. |
| D9 | Extend `urls.csv` to 20 companies you actually know. Run the batch. Compute p50/p95 latency, total cost, cost per 1,000, schema-valid rate, error rate from `calls.jsonl`. | The results table is in this README with real numbers. |
| D10 | Read the 20 outputs. Count how many you would trust in a CRM. Write the 300-word writeup and tag `v0.1-foundations`. | `git tag v0.1-foundations && git push --tags`. |

## Design decisions already made for you (so D1 is not spent choosing)

- **`uv`** for the environment. Fast, lockfile, no virtualenv ceremony.
- **Pydantic** for the output contract, because a CRM cannot consume prose.
- **JSONL, not a database,** for the call log. Twelve lines of code, greppable, enough for D9.
- **A cheap small model.** This phase tests your plumbing, not model quality.
- **`respx`** so tests never hit the network. Tests that call a paid API are not tests.

## Two things that will trip you

**Structured output is not a guarantee.** The model can return valid JSON that is confidently
wrong. That is why `confidence` is a field and why D10 is a manual read of all 20 outputs. The
number that matters on D9 is not "20/20 parsed", it is "how many would you put in front of a rep".

**Cost per call is uninteresting. Cost per 1,000 is the number you will quote.** Compute it from
the log, not from the pricing page, because retries and failed calls cost money too and only the
log knows about them.

## Results

_(D9 fills this in.)_

| Metric | Value |
|---|---|
| URLs attempted | |
| Fetch success rate | |
| Schema-valid rate | |
| Trusted-by-you rate (D10 manual read) | |
| p50 latency | |
| p95 latency | |
| Total cost | |
| Cost per 1,000 URLs | |
| Retries triggered | |

## Log

_(One line per session: what I measured, what broke.)_

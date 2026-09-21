"""One JSONL line per model call. Day 4.

Fields: ts, model, op, input_tokens, output_tokens, cost_usd, latency_ms, ok, error.
Append-only. This file becomes the evidence for the Day 9 results table.
"""
# TODO D4: def log_call(**fields) -> None  (append JSON line to settings.log_path)
# TODO D4: def read_log(path) -> list[dict]

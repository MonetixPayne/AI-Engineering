"""The call path. Days 1-5. The core of this phase.

One function that every later phase reuses:

    complete(prompt: str, schema: type[BaseModel]) -> tuple[BaseModel, CallStats]

Responsibilities, in the order you will add them:
  D1 raw call, text back
  D2 structured output, validated into `schema`
  D3 usage -> cost
  D4 latency + log line
  D5 timeout, retry with exponential backoff and jitter, typed errors
"""
# TODO D5: class CallStats: model, input_tokens, output_tokens, cost_usd, latency_ms, attempts
# TODO D5: retry only on 429/500/502/503/504 and timeouts. Never retry a schema violation
#          without changing something: that is a bug, not a transient fault.

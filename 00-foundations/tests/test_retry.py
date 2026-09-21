"""Day 5. Use respx to fake the HTTP layer. No real API calls in tests."""
# TODO D5: 429 then 200 -> one retry, result returned, attempts == 2.
# TODO D5: three 500s -> raises, attempts == 3, and a failure line is written to the log.
# TODO D5: schema violation -> no retry.

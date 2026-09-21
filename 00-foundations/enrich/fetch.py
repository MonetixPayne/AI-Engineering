"""Get the text of a homepage. Day 6.

Not a crawler. One page, 10s timeout, strip nav/script/style, cap at ~6k characters.
Real inputs are messy: redirects, JS-only pages, 403 from bot protection, 40 languages.
Handle them explicitly and record which ones failed and why.
"""
# TODO D6: def page_text(url: str) -> str

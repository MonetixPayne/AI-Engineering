"""The output contract. Day 2.

This file is the reason the tool is useful. A free-text summary cannot be joined
to a CRM. A validated object can.
"""
# TODO D2: pydantic model Company:
#   name: str
#   industry: str
#   employee_range: Literal["1-10","11-50","51-200","201-1000","1000+"]
#   hq_country: str | None
#   tech_signals: list[str]
#   one_line: str = Field(max_length=140)
#   confidence: float = Field(ge=0, le=1)
# Every field must be answerable from a homepage, or the model will invent it.

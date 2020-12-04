from collections import namedtuple
from typing import Any

RegistrantRule = namedtuple("RegistrantRule", ["min", "max", "registrant_length"])
RULES: Any

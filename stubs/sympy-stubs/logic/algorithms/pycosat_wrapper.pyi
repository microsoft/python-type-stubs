from collections.abc import Generator
from typing import Any, Literal

def pycosat_satisfiable(
    expr, all_models=...
) -> Generator[bool, None, None] | dict[Any, Any] | Generator[dict[Any, Any] | Literal[False], Any, None] | Literal[False]: ...

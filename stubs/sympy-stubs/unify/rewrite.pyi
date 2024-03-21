from typing import Any, Callable, Generator
from sympy import Basic

def rewriterule(source, target, variables=..., condition=..., assume=...) -> Callable[..., Generator[Any | Basic, Any, None]]:
    ...


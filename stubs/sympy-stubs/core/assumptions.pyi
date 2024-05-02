from typing import Any, Self

from sympy.core.facts import FactKB

_assume_rules = ...
_assume_defined = ...
_assume_defined = ...
def assumptions(expr, _check=...) -> dict[Any, Any]:
    ...

def common_assumptions(exprs, check=...) -> dict[Any, Any]:
    ...

def failing_assumptions(expr, **assumptions) -> dict[Any, Any]:
    ...

def check_assumptions(expr, against=..., **assume) -> bool | None:
    ...

class StdFactKB(FactKB):
    def __init__(self, facts=...) -> None:
        ...
    
    def copy(self) -> Self:
        ...
    
    @property
    def generator(self) -> dict[Any, Any]:
        ...
    


def as_property(fact):
    ...

def make_property(fact) -> property:
    ...

class ManagedProperties(type):
    def __init__(cls, *args, **kwargs) -> None:
        ...
    



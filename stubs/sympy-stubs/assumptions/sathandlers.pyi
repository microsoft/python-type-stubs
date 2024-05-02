from typing import Any, Callable
from sympy.core import Add, Mul, Number, NumberSymbol, Pow
from sympy.core.logic import And, Or
from sympy.core.numbers import ImaginaryUnit
from sympy.functions.elementary.complexes import Abs
from sympy.logic.boolalg import Implies
from sympy.matrices.expressions import MatMul

def allargs(symbol, fact, expr) -> And:
    ...

def anyarg(symbol, fact, expr) -> Or:
    ...

def exactlyonearg(symbol, fact, expr) -> Or:
    ...

class ClassFactRegistry:
    def __init__(self) -> None:
        ...
    
    def register(self, cls) -> Callable[..., Any]:
        ...
    
    def multiregister(self, *classes) -> Callable[..., Any]:
        ...
    
    def __getitem__(self, key) -> tuple[frozenset[Any], frozenset[Any]]:
        ...
    
    def __call__(self, expr) -> set[Any]:
        ...
    


class_fact_registry = ...
x = ...
@class_fact_registry.multiregister(Abs)
def _(expr) -> list[Any]:
    ...

@class_fact_registry.multiregister(Add)
def _(expr) -> list[Any]:
    ...

@class_fact_registry.register(Add)
def _(expr) -> Implies:
    ...

@class_fact_registry.multiregister(Mul)
def _(expr) -> list[Any]:
    ...

@class_fact_registry.register(Mul)
def _(expr) -> Implies:
    ...

@class_fact_registry.register(Mul)
def _(expr) -> Implies:
    ...

@class_fact_registry.register(Mul)
def _(expr) -> Implies:
    ...

@class_fact_registry.register(Mul)
def _(expr) -> Implies:
    ...

@class_fact_registry.register(MatMul)
def _(expr) -> Implies:
    ...

@class_fact_registry.multiregister(Pow)
def _(expr) -> list[Any]:
    ...

_old_assump_getters = ...
@class_fact_registry.multiregister(Number, NumberSymbol, ImaginaryUnit)
def _(expr) -> list[Any]:
    ...


from typing import Any, Literal
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.function import UndefinedFunction
from sympy.utilities.misc import debug_decorator as debug

timeit = ...
def compare(a, b, x) -> Literal['<', '>', '=']:
    ...

class SubsSet(dict):
    def __init__(self) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __getitem__(self, key):
        ...
    
    def do_subs(self, e):
        ...
    
    def meets(self, s2) -> bool:
        ...
    
    def union(self, s2, exps=...) -> tuple[SubsSet, Any | None]:
        ...
    
    def copy(self) -> SubsSet:
        ...
    


@debug
def mrv(e, x) -> tuple[SubsSet, Basic] | tuple[SubsSet, Any] | tuple[Any, Basic] | tuple[Any, Any] | tuple[SubsSet, Any | Literal[1]] | tuple[Any, type[UndefinedFunction] | Any]:
    ...

def mrv_max3(f, expsf, g, expsg, union, expsboth, x) -> tuple[SubsSet, Any] | tuple[Any, Any]:
    ...

def mrv_max1(f, g, exps, x) -> tuple[SubsSet, Any] | tuple[Any, Any]:
    ...

@debug
@cacheit
@timeit
def sign(e, x) -> type[UndefinedFunction] | Literal[1, -1, 0]:
    ...

@debug
@timeit
@cacheit
def limitinf(e, x):
    ...

def moveup2(s, x) -> SubsSet:
    ...

def moveup(l, x) -> list[Any]:
    ...

@debug
@timeit
def calculate_series(e, x, logx=...) -> bool | Basic:
    ...

@debug
@timeit
@cacheit
def mrv_leadterm(e, x) -> tuple[Any, Any] | tuple[Basic | Any | type[UndefinedFunction] | Literal[1], Any]:
    ...

def build_expression_tree(Omega, rewrites) -> dict[Any, Any]:
    class Node:
        ...
    
    

@debug
@timeit
def rewrite(e, Omega, x, wsym) -> tuple[Any, Any]:
    ...

def gruntz(e, z, z0, dir=...):
    ...


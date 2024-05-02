from array import array
from typing import Any, Generator, Literal
from sympy import Function
from sympy.core.function import UndefinedFunction
from sympy.utilities.decorator import deprecated

class Sieve:
    def __init__(self) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def extend(self, n) -> None:
        ...
    
    def extend_to_no(self, i) -> None:
        ...
    
    def primerange(self, a, b=...) -> Generator[Any, Any, None]:
        ...
    
    def totientrange(self, a, b) -> Generator[int, Any, None]:
        ...
    
    def mobiusrange(self, a, b) -> Generator[int, Any, None]:
        ...
    
    def search(self, n) -> tuple[int, int]:
        ...
    
    def __contains__(self, n) -> bool:
        ...
    
    def __iter__(self) -> Generator[array[int] | int, Any, None]:
        ...
    
    def __getitem__(self, n) -> array[int] | int:
        ...
    


sieve = ...
def prime(nth) -> array[int] | int:
    ...

class primepi(Function):
    @classmethod
    def eval(cls, n) -> None:
        ...
    


def nextprime(n, ith=...) -> int | array[int] | None:
    ...

def prevprime(n) -> int | array[int] | None:
    ...

def primerange(a, b=...) -> Generator[Any | int | array[int] | None, Any, None]:
    ...

def randprime(a, b) -> int | array[int] | None:
    ...

def primorial(n, nth=...) -> array[int] | int:
    ...

def cycle_length(f, x0, nmax=..., values=...) -> Generator[Any | tuple[int, None] | tuple[int, int], Any, None]:
    ...

def composite(nth) -> int:
    ...

def compositepi(n) -> Literal[0]:
    ...


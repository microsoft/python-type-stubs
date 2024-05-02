from typing import Self
from sympy.core.add import Add
from sympy.core.expr import Expr
from sympy.vector.vector import VectorAdd, VectorZero

class Gradient(Expr):
    def __new__(cls, expr) -> Self:
        ...
    
    def doit(self, **hints) -> VectorZero | VectorAdd | Gradient:
        ...
    


class Divergence(Expr):
    def __new__(cls, expr) -> Self:
        ...
    
    def doit(self, **hints) -> Divergence | Add:
        ...
    


class Curl(Expr):
    def __new__(cls, expr) -> Self:
        ...
    
    def doit(self, **hints) -> VectorZero | VectorAdd | Curl:
        ...
    


def curl(vect, doit=...) -> VectorZero | VectorAdd | Curl:
    ...

def divergence(vect, doit=...) -> Divergence | Add:
    ...

def gradient(scalar_field, doit=...) -> VectorZero | VectorAdd | Gradient:
    ...

class Laplacian(Expr):
    def __new__(cls, expr) -> Self:
        ...
    
    def doit(self, **hints) -> Divergence | Add:
        ...
    



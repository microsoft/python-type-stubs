from sympy.core.expr import Expr
from sympy.core.function import DefinedFunction, Function

class RoundFunction(DefinedFunction):
    @property
    def args(self) -> tuple[Expr]: ...
    def __new__(cls, *args, **options) -> Expr: ...
    @classmethod
    def eval(cls, arg) -> Expr | None: ...

class floor(RoundFunction):
    _dir: int

class ceiling(RoundFunction):
    _dir: int

class frac(Function):
    def __new__(cls, *args, **options) -> Expr: ...
    @classmethod
    def eval(cls, arg) -> Expr | None: ...

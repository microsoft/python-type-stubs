from typing import TYPE_CHECKING, Any, Literal, Self
from sympy.core.decorators import _sympifyit, call_highest_priority
from sympy.core import Add, Mul
from sympy.core.expr import Expr
from sympy.series.order import Order
from sympy.vector.vector import BaseVector

if TYPE_CHECKING:
    ...
class BasisDependent(Expr):
    zero: BasisDependentZero
    @call_highest_priority('__radd__')
    def __add__(self, other):
        ...
    
    @call_highest_priority('__add__')
    def __radd__(self, other):
        ...
    
    @call_highest_priority('__rsub__')
    def __sub__(self, other):
        ...
    
    @call_highest_priority('__sub__')
    def __rsub__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rmul__')
    def __mul__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__mul__')
    def __rmul__(self, other):
        ...
    
    def __neg__(self):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rtruediv__')
    def __truediv__(self, other):
        ...
    
    @call_highest_priority('__truediv__')
    def __rtruediv__(self, other) -> TypeError:
        ...
    
    def evalf(self, n=..., subs=..., maxn=..., chop=..., strict=..., quad=..., verbose=...) -> BasisDependentZero:
        ...
    
    n = ...
    def simplify(self, **kwargs):
        ...
    
    def trigsimp(self, **opts):
        ...
    
    def as_numer_denom(self) -> tuple[Self, Any]:
        ...
    
    def factor(self, *args, **kwargs):
        ...
    
    def as_coeff_Mul(self, rational=...) -> tuple[Any, Self]:
        ...
    
    def as_coeff_add(self, *deps) -> tuple[Literal[0], tuple[Any, ...]]:
        ...
    
    def diff(self, *args, **kwargs):
        ...
    
    def doit(self, **hints):
        ...
    


class BasisDependentAdd(BasisDependent, Add):
    def __new__(cls, *args, **options) -> BasisDependentZero | Order:
        ...
    


class BasisDependentMul(BasisDependent, Mul):
    def __new__(cls, *args, **options) -> Order | BasisDependentZero:
        ...
    


class BasisDependentZero(BasisDependent):
    components: dict[BaseVector, Expr] = ...
    _latex_form: str
    def __new__(cls) -> Self:
        ...
    
    def __hash__(self) -> int:
        ...
    
    @call_highest_priority('__req__')
    def __eq__(self, other) -> bool:
        ...
    
    __req__ = ...
    @call_highest_priority('__radd__')
    def __add__(self, other):
        ...
    
    @call_highest_priority('__add__')
    def __radd__(self, other):
        ...
    
    @call_highest_priority('__rsub__')
    def __sub__(self, other):
        ...
    
    @call_highest_priority('__sub__')
    def __rsub__(self, other):
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def normalize(self) -> Self:
        ...
    



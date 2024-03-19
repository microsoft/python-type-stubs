from inspect import Signature
from types import NotImplementedType
from typing import Any, Callable, Dict, Literal, Self
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.decorators import _sympifyit
from sympy.core.expr import AtomicExpr, Expr
from sympy.core.kind import Kind
from sympy.core.logic import FuzzyBool
from sympy.core.numbers import Float
from sympy.printing.str import StrPrinter
from sympy.sets.sets import FiniteSet
from sympy.tensor.array.array_derivatives import ArrayDerivative

class PoleError(Exception):
    ...


class ArgumentIndexError(ValueError):
    def __str__(self) -> str:
        ...
    


class BadSignatureError(TypeError):
    ...


class BadArgumentsError(TypeError):
    ...


def arity(cls) -> int | tuple[int, ...] | None:
    ...

class FunctionClass(type):
    _new = ...
    def __init__(cls, *args, **kwargs) -> None:
        ...
    
    @property
    def __signature__(self) -> Signature | None:
        ...
    
    @property
    def free_symbols(self) -> set[Any]:
        ...
    
    @property
    def xreplace(self) -> Callable[..., Any]:
        ...
    
    @property
    def nargs(self) -> FiniteSet:
        ...
    
    def __repr__(cls) -> str:
        ...
    


class Application(Basic, metaclass=FunctionClass):
    is_Function = ...
    @cacheit
    def __new__(cls, *args, **options) -> Self:
        ...
    
    @classmethod
    def eval(cls, *args) -> None:
        ...
    
    @property
    def func(self) -> type[Self]:
        ...
    


class Function(Application, Expr):
    @cacheit
    def __new__(cls, *args, **options) -> type[UndefinedFunction]:
        ...
    
    @classmethod
    def class_key(cls) -> tuple[Literal[4], int, str]:
        ...
    
    _singularities: FuzzyBool | tuple[Expr, ...] = ...
    @classmethod
    def is_singular(cls, a) -> FuzzyBool:
        ...
    
    def as_base_exp(self) -> tuple[Self, Any]:
        ...
    
    def fdiff(self, argindex=...) -> ArrayDerivative | Derivative | Subs:
        ...
    


class AppliedUndef(Function):
    is_number = ...
    def __new__(cls, *args, **options) -> type[UndefinedFunction]:
        ...
    


class UndefSageHelper:
    def __get__(self, ins, typ) -> Callable[[], Any]:
        ...
    


_undef_sage_helper = ...
class UndefinedFunction(FunctionClass):
    def __new__(cls, name, bases=..., __dict__=..., **kwargs) -> Self: # type: ignore
        ...
    
    def __instancecheck__(cls, instance) -> bool:
        ...
    
    _kwargs: dict[str, bool | None] = ...
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


class WildFunction(Function, AtomicExpr):
    include: set[Any] = ...
    def __init__(self, name, **assumptions) -> None:
        ...
    
    def matches(self, expr, repl_dict=..., old=...) -> dict[Any, Any] | None:
        ...
    


class Derivative(Expr):
    is_Derivative = ...
    def __new__(cls, expr, *variables, **kwargs):
        ...
    
    @property
    def canonical(cls) -> Self:
        ...
    
    def doit(self, **hints) -> Self:
        ...
    
    @_sympifyit('z0', NotImplementedError)
    def doit_numerically(self, z0) -> Float:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def variables(self) -> tuple[Any, ...]:
        ...
    
    @property
    def variable_count(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def derivative_count(self) -> int:
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    
    @property
    def kind(self) -> Kind:
        ...
    
    def as_finite_difference(self, points=..., x0=..., wrt=...) -> Literal[0]:
        ...
    


class Lambda(Expr):
    is_Function = ...
    def __new__(cls, signature, expr) -> Self:
        ...
    
    @property
    def signature(self) -> Basic:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def variables(self) -> tuple[Any, ...]:
        ...
    
    @property
    def nargs(self) -> FiniteSet:
        ...
    
    bound_symbols = ...
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    
    def __call__(self, *args) -> Basic:
        ...
    
    @property
    def is_identity(self) -> NotImplementedType | bool:
        ...
    


class Subs(Expr):
    def __new__(cls, expr, variables, point, **assumptions) -> Self:
        class CustomStrPrinter(StrPrinter):
            ...
        
        
    
    def doit(self, **hints) -> Basic:
        ...
    
    def evalf(self, prec=..., **options):
        ...
    
    n = ...
    @property
    def variables(self) -> Basic:
        ...
    
    bound_symbols = ...
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def point(self) -> Basic:
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    
    @property
    def expr_free_symbols(self) -> set[Any]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


def diff(f, *symbols, **kwargs) -> ArrayDerivative | Derivative:
    ...

def expand(e, deep=..., modulus=..., power_base=..., power_exp=..., mul=..., log=..., multinomial=..., basic=..., **hints):
    ...

def expand_mul(expr, deep=...):
    ...

def expand_multinomial(expr, deep=...):
    ...

def expand_log(expr, deep=..., force=..., factor=...):
    ...

def expand_func(expr, deep=...):
    ...

def expand_trig(expr, deep=...):
    ...

def expand_complex(expr, deep=...):
    ...

def expand_power_base(expr, deep=..., force=...):
    ...

def expand_power_exp(expr, deep=...):
    ...

def count_ops(expr, visual=...):
    ...

def nfloat(expr, n=..., exponent=..., dkeys=...) -> dict[Any, Any] | Dict | Basic | Any | Float:
    ...


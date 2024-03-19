from typing import Any, Self
from sympy.core import cacheit
from sympy.core.basic import Basic
from sympy.core.function import Function, UndefinedFunction
from sympy.core.logic import FuzzyBool
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.functions.elementary.exponential import log
from sympy.series.order import Order

class HyperbolicFunction(Function):
    unbranched = ...


class sinh(HyperbolicFunction):
    def fdiff(self, argindex=...) -> type[UndefinedFunction]:
        ...
    
    def inverse(self, argindex=...) -> type[asinh]:
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any | Order | Self, Any] | tuple[Self, Any] | tuple[Any, Any]:
        ...
    


class cosh(HyperbolicFunction):
    def fdiff(self, argindex=...) -> type[UndefinedFunction]:
        ...
    
    @classmethod
    def eval(cls, arg) -> Self | type[UndefinedFunction] | Pow | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any | Order | Self, Any] | tuple[Self, Any] | tuple[Any, Any]:
        ...
    


class tanh(HyperbolicFunction):
    def fdiff(self, argindex=...):
        ...
    
    def inverse(self, argindex=...) -> type[atanh]:
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | type[UndefinedFunction] | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any | Order | Self, Any] | tuple[Self, Any] | tuple[Any, Any]:
        ...
    


class coth(HyperbolicFunction):
    def fdiff(self, argindex=...):
        ...
    
    def inverse(self, argindex=...) -> type[acoth]:
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | type[UndefinedFunction] | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any | Order | Self, Any] | tuple[Self, Any] | tuple[Any, Any]:
        ...
    


class ReciprocalHyperbolicFunction(HyperbolicFunction):
    _reciprocal_of = ...
    _is_even: FuzzyBool = ...
    _is_odd: FuzzyBool = ...
    @classmethod
    def eval(cls, arg) -> Self | Mul:
        ...
    
    def as_real_imag(self, deep=..., **hints):
        ...
    


class csch(ReciprocalHyperbolicFunction):
    _reciprocal_of = sinh
    _is_odd = ...
    def fdiff(self, argindex=...):
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    


class sech(ReciprocalHyperbolicFunction):
    _reciprocal_of = cosh
    _is_even = ...
    def fdiff(self, argindex=...):
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    


class InverseHyperbolicFunction(Function):
    ...


class asinh(InverseHyperbolicFunction):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> log | Mul | Basic | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[sinh]:
        ...
    


class acosh(InverseHyperbolicFunction):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg):
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[cosh]:
        ...
    


class atanh(InverseHyperbolicFunction):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | Basic | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[tanh]:
        ...
    


class acoth(InverseHyperbolicFunction):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[coth]:
        ...
    


class asech(InverseHyperbolicFunction):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms) -> type[UndefinedFunction]:
        ...
    
    def inverse(self, argindex=...) -> type[sech]:
        ...
    
    _eval_rewrite_as_tractable = ...


class acsch(InverseHyperbolicFunction):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> log | Mul | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms) -> type[UndefinedFunction]:
        ...
    
    def inverse(self, argindex=...) -> type[csch]:
        ...
    
    _eval_rewrite_as_tractable = ...



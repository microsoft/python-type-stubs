from typing import Any
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.function import Function, UndefinedFunction
from sympy.core.mul import Mul
from sympy.functions.elementary.hyperbolic import cosh, sinh
from sympy.functions.elementary.trigonometric import cos, sin

def real_to_real_as_real_imag(self, deep=..., **hints) -> tuple[Any, Any]:
    ...

class erf(Function):
    unbranched = ...
    def fdiff(self, argindex=...):
        ...
    
    def inverse(self, argindex=...) -> type[erfinv]:
        ...
    
    @classmethod
    def eval(cls, arg) -> Basic | erf2inv | Mul | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    as_real_imag = ...


class erfc(Function):
    unbranched = ...
    def fdiff(self, argindex=...):
        ...
    
    def inverse(self, argindex=...) -> type[erfcinv]:
        ...
    
    @classmethod
    def eval(cls, arg) -> Basic | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    as_real_imag = ...


class erfi(Function):
    unbranched = ...
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, z) -> Mul | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    as_real_imag = ...


class erf2(Function):
    def fdiff(self, argindex):
        ...
    
    @classmethod
    def eval(cls, x, y) -> Basic | Mul | None:
        ...
    


class erfinv(Function):
    def fdiff(self, argindex=...):
        ...
    
    def inverse(self, argindex=...) -> type[erf]:
        ...
    
    @classmethod
    def eval(cls, z) -> Basic | None:
        ...
    


class erfcinv(Function):
    def fdiff(self, argindex=...):
        ...
    
    def inverse(self, argindex=...) -> type[erfc]:
        ...
    
    @classmethod
    def eval(cls, z) -> None:
        ...
    


class erf2inv(Function):
    def fdiff(self, argindex) -> type[UndefinedFunction]:
        ...
    
    @classmethod
    def eval(cls, x, y) -> type[UndefinedFunction] | None:
        ...
    


class Ei(Function):
    @classmethod
    def eval(cls, z) -> None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    
    _eval_rewrite_as_Ci = ...
    _eval_rewrite_as_Chi = ...
    _eval_rewrite_as_Shi = ...


class expint(Function):
    @classmethod
    def eval(cls, nu, z) -> type[UndefinedFunction] | bool | Basic | None:
        ...
    
    def fdiff(self, argindex) -> Mul:
        ...
    
    _eval_rewrite_as_Ci = ...
    _eval_rewrite_as_Chi = ...
    _eval_rewrite_as_Shi = ...


def E1(z) -> type[UndefinedFunction]:
    ...

class li(Function):
    @classmethod
    def eval(cls, z) -> None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    
    _eval_rewrite_as_Ci = ...
    _eval_rewrite_as_Chi = ...


class Li(Function):
    @classmethod
    def eval(cls, z) -> None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    


class TrigonometricIntegral(Function):
    @classmethod
    def eval(cls, z) -> None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    


class Si(TrigonometricIntegral):
    _trigfunc = sin
    _atzero = ...


class Ci(TrigonometricIntegral):
    _trigfunc = cos
    _atzero = ...


class Shi(TrigonometricIntegral):
    _trigfunc = sinh
    _atzero = ...


class Chi(TrigonometricIntegral):
    _trigfunc = cosh
    _atzero = ...


class FresnelIntegral(Function):
    unbranched = ...
    @classmethod
    def eval(cls, z) -> None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    
    _eval_is_finite = ...
    as_real_imag = ...


class fresnels(FresnelIntegral):
    _trigfunc = sin
    _sign = ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    


class fresnelc(FresnelIntegral):
    _trigfunc = cos
    _sign = ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    


class _erfs(Function):
    @classmethod
    def eval(cls, arg) -> None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    


class _eis(Function):
    def fdiff(self, argindex=...):
        ...
    



from typing import Any
from typing_extensions import Self

from sympy.calculus.accumulationbounds import AccumBounds
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import Function, UndefinedFunction
from sympy.core.logic import FuzzyBool
from sympy.core.mul import Mul
from sympy.functions.elementary.piecewise import Piecewise

class TrigonometricFunction(Function):
    unbranched = ...
    _singularities = ...

class sin(TrigonometricFunction):
    def period(self, symbol=...): ...
    def fdiff(self, argindex=...) -> type[UndefinedFunction]: ...
    @classmethod
    def eval(cls, arg): ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any]: ...

class cos(TrigonometricFunction):
    def period(self, symbol=...): ...
    def fdiff(self, argindex=...): ...
    @classmethod
    def eval(cls, arg): ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any]: ...

class tan(TrigonometricFunction):
    def period(self, symbol=...): ...
    def fdiff(self, argindex=...): ...
    def inverse(self, argindex=...) -> type[atan]: ...
    @classmethod
    def eval(cls, arg): ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any] | tuple[Self, Any]: ...

class cot(TrigonometricFunction):
    def period(self, symbol=...): ...
    def fdiff(self, argindex=...): ...
    def inverse(self, argindex=...) -> type[acot]: ...
    @classmethod
    def eval(cls, arg): ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any] | tuple[Self, Any]: ...

class ReciprocalTrigonometricFunction(TrigonometricFunction):
    _reciprocal_of = ...
    _singularities = ...
    _is_even: FuzzyBool = ...
    _is_odd: FuzzyBool = ...
    @classmethod
    def eval(cls, arg) -> Self | Mul: ...
    def fdiff(self, argindex=...) -> Any: ...
    def as_real_imag(self, deep=..., **hints): ...

class sec(ReciprocalTrigonometricFunction):
    _reciprocal_of = cos
    _is_even = ...
    def period(self, symbol=...): ...
    def fdiff(self, argindex=...): ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...

class csc(ReciprocalTrigonometricFunction):
    _reciprocal_of = sin
    _is_odd = ...
    def period(self, symbol=...): ...
    def fdiff(self, argindex=...): ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...

class sinc(Function):
    _singularities = ...
    def fdiff(self, argindex=...): ...
    @classmethod
    def eval(cls, arg) -> Self | None: ...

    _eval_is_finite = ...

class InverseTrigonometricFunction(Function):
    _singularities: tuple[Expr, ...] = ...

class asin(InverseTrigonometricFunction):
    def fdiff(self, argindex=...): ...
    @classmethod
    def eval(cls, arg) -> Mul | None: ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...

    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[sin]: ...

class acos(InverseTrigonometricFunction):
    def fdiff(self, argindex=...): ...
    @classmethod
    def eval(cls, arg) -> None: ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...

    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[cos]: ...

class atan(InverseTrigonometricFunction):
    args: tuple[Expr]
    _singularities = ...
    def fdiff(self, argindex=...): ...
    @classmethod
    def eval(cls, arg) -> AccumBounds | Mul | None: ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...

    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[tan]: ...

class acot(InverseTrigonometricFunction):
    _singularities = ...
    def fdiff(self, argindex=...): ...
    @classmethod
    def eval(cls, arg) -> Mul | None: ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...

    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[cot]: ...

class asec(InverseTrigonometricFunction):
    @classmethod
    def eval(cls, arg) -> None: ...
    def fdiff(self, argindex=...): ...
    def inverse(self, argindex=...) -> type[sec]: ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...

    _eval_rewrite_as_tractable = ...

class acsc(InverseTrigonometricFunction):
    @classmethod
    def eval(cls, arg) -> Mul | None: ...
    def fdiff(self, argindex=...): ...
    def inverse(self, argindex=...) -> type[csc]: ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...

    _eval_rewrite_as_tractable = ...

class atan2(InverseTrigonometricFunction):
    @classmethod
    def eval(cls, y, x) -> atan | Piecewise | None: ...
    def fdiff(self, argindex): ...

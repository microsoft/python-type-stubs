from typing import Self
from sympy.core.basic import Basic
from sympy.core.function import Derivative, Function, UndefinedFunction
from sympy.core.containers import Tuple
from sympy.core.logic import Or

class TupleArg(Tuple):
    def limit(self, x, xlim, dir=...) -> TupleArg:
        ...
    


class TupleParametersBase(Function):
    is_commutative = ...


class hyper(TupleParametersBase):
    def __new__(cls, ap, bq, z, **kwargs) -> type[UndefinedFunction]:
        ...
    
    @classmethod
    def eval(cls, ap, bq, z) -> type[UndefinedFunction] | None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    
    @property
    def argument(self) -> Basic:
        ...
    
    @property
    def ap(self) -> Tuple:
        ...
    
    @property
    def bq(self) -> Tuple:
        ...
    
    @property
    def eta(self):
        ...
    
    @property
    def radius_of_convergence(self):
        ...
    
    @property
    def convergence_statement(self) -> Or | bool:
        ...
    


class meijerg(TupleParametersBase):
    def __new__(cls, *args, **kwargs) -> type[UndefinedFunction]:
        ...
    
    def fdiff(self, argindex=...):
        ...
    
    def get_period(self):
        ...
    
    def integrand(self, s):
        ...
    
    @property
    def argument(self) -> Basic:
        ...
    
    @property
    def an(self) -> Tuple:
        ...
    
    @property
    def ap(self) -> Tuple:
        ...
    
    @property
    def aother(self) -> Tuple:
        ...
    
    @property
    def bm(self) -> Tuple:
        ...
    
    @property
    def bq(self) -> Tuple:
        ...
    
    @property
    def bother(self) -> Tuple:
        ...
    
    @property
    def nu(self):
        ...
    
    @property
    def delta(self):
        ...
    
    @property
    def is_number(self) -> bool:
        ...
    


class HyperRep(Function):
    @classmethod
    def eval(cls, *args) -> Self | None:
        ...
    


class HyperRep_power1(HyperRep):
    ...


class HyperRep_power2(HyperRep):
    ...


class HyperRep_log1(HyperRep):
    ...


class HyperRep_atanh(HyperRep):
    ...


class HyperRep_asin1(HyperRep):
    ...


class HyperRep_asin2(HyperRep):
    ...


class HyperRep_sqrts1(HyperRep):
    ...


class HyperRep_sqrts2(HyperRep):
    ...


class HyperRep_log2(HyperRep):
    ...


class HyperRep_cosasin(HyperRep):
    ...


class HyperRep_sinasin(HyperRep):
    ...


class appellf1(Function):
    @classmethod
    def eval(cls, a, b1, b2, c, x, y) -> Self | None:
        ...
    
    def fdiff(self, argindex=...) -> Derivative:
        ...
    



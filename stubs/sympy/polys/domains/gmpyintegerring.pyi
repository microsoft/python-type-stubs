from typing import Any
from sympy.core.numbers import Integer
from sympy.polys.domains.groundtypes import _GMPYInteger, GMPYInteger
from sympy.polys.domains.integerring import IntegerRing
from sympy.utilities import public

class GMPYIntegerRing(IntegerRing):
    dtype = GMPYInteger
    zero = dtype(0)
    one = dtype(1)
    tp = type(one)
    alias = ...
    def __init__(self) -> None:
        ...
    
    def to_sympy(self, a) -> Integer:
        ...
    
    def from_sympy(self, a) -> _GMPYInteger:
        ...
    
    def from_FF_python(K1, a, K0) -> _GMPYInteger:
        ...
    
    def from_ZZ_python(K1, a, K0) -> _GMPYInteger:
        ...
    
    def from_QQ(K1, a, K0) -> _GMPYInteger | None:
        ...
    
    def from_QQ_python(K1, a, K0) -> _GMPYInteger | None:
        ...
    
    def from_FF_gmpy(K1, a, K0):
        ...
    
    def from_ZZ_gmpy(K1, a, K0):
        ...
    
    def from_QQ_gmpy(K1, a, K0) -> None:
        ...
    
    def from_RealField(K1, a, K0) -> _GMPYInteger | None:
        ...
    
    def from_GaussianIntegerRing(K1, a, K0) -> None:
        ...
    
    def gcdex(self, a, b) -> tuple[Any, Any, Any]:
        ...
    
    def gcd(self, a, b):
        ...
    
    def lcm(self, a, b):
        ...
    
    def sqrt(self, a) -> int:
        ...
    
    def factorial(self, a) -> int:
        ...
    



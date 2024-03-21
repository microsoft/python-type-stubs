from typing import Literal, Self
from sympy.core.basic import Basic
from sympy.matrices.expressions.matexpr import MatrixExpr

class ZeroMatrix(MatrixExpr):
    is_ZeroMatrix = ...
    def __new__(cls, m, n) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, Basic]:
        ...
    


class GenericZeroMatrix(ZeroMatrix):
    def __new__(cls) -> Self:
        ...
    
    @property
    def rows(self):
        ...
    
    @property
    def cols(self):
        ...
    
    @property
    def shape(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class Identity(MatrixExpr):
    is_Identity = ...
    def __new__(cls, n) -> Self:
        ...
    
    @property
    def rows(self) -> Basic:
        ...
    
    @property
    def cols(self) -> Basic:
        ...
    
    @property
    def shape(self) -> tuple[Basic, Basic]:
        ...
    
    @property
    def is_square(self) -> Literal[True]:
        ...
    


class GenericIdentity(Identity):
    def __new__(cls) -> Self:
        ...
    
    @property
    def rows(self):
        ...
    
    @property
    def cols(self):
        ...
    
    @property
    def shape(self):
        ...
    
    @property
    def is_square(self) -> Literal[True]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class OneMatrix(MatrixExpr):
    def __new__(cls, m, n, evaluate=...) -> Identity | Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def is_Identity(self):
        ...
    
    def as_explicit(self):
        ...
    
    def doit(self, **hints) -> Self:
        ...
    



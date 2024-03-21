from typing import Any, Self
from sympy.matrices.expressions.sets import MatrixSet
from sympy.stats.rv import Distribution, MatrixDomain, NamedArgsMixin, PSpace, RandomMatrixSymbol

class MatrixPSpace(PSpace):
    def __new__(cls, sym, distribution, dim_n, dim_m) -> Self:
        ...
    
    distribution = ...
    symbol = ...
    @property
    def domain(self) -> MatrixDomain:
        ...
    
    @property
    def value(self) -> RandomMatrixSymbol:
        ...
    
    @property
    def values(self) -> set[RandomMatrixSymbol]:
        ...
    
    def compute_density(self, expr, *args) -> Any:
        ...
    
    def sample(self, size=..., library=..., seed=...) -> dict[RandomMatrixSymbol, Any]:
        ...
    


def rv(symbol, cls, args) -> RandomMatrixSymbol:
    ...

class SampleMatrixScipy:
    def __new__(cls, dist, size, seed=...) -> None:
        ...
    


class SampleMatrixNumpy:
    def __new__(cls, dist, size, seed=...) -> None:
        ...
    


class SampleMatrixPymc:
    def __new__(cls, dist, size, seed=...) -> None:
        ...
    


_get_sample_class_matrixrv = ...
class MatrixDistribution(Distribution, NamedArgsMixin):
    def __new__(cls, *args) -> Self:
        ...
    
    @staticmethod
    def check(*args) -> None:
        ...
    
    def __call__(self, expr):
        ...
    
    def sample(self, size=..., library=..., seed=...):
        ...
    


class MatrixGammaDistribution(MatrixDistribution):
    _argnames = ...
    @staticmethod
    def check(alpha, beta, scale_matrix) -> None:
        ...
    
    @property
    def set(self) -> MatrixSet:
        ...
    
    @property
    def dimension(self):
        ...
    
    def pdf(self, x):
        ...
    


def MatrixGamma(symbol, alpha, beta, scale_matrix) -> RandomMatrixSymbol:
    ...

class WishartDistribution(MatrixDistribution):
    _argnames = ...
    @staticmethod
    def check(n, scale_matrix) -> None:
        ...
    
    @property
    def set(self) -> MatrixSet:
        ...
    
    @property
    def dimension(self):
        ...
    
    def pdf(self, x):
        ...
    


def Wishart(symbol, n, scale_matrix) -> RandomMatrixSymbol:
    ...

class MatrixNormalDistribution(MatrixDistribution):
    _argnames = ...
    @staticmethod
    def check(location_matrix, scale_matrix_1, scale_matrix_2) -> None:
        ...
    
    @property
    def set(self) -> MatrixSet:
        ...
    
    @property
    def dimension(self):
        ...
    
    def pdf(self, x):
        ...
    


def MatrixNormal(symbol, location_matrix, scale_matrix_1, scale_matrix_2) -> RandomMatrixSymbol:
    ...

class MatrixStudentTDistribution(MatrixDistribution):
    _argnames = ...
    @staticmethod
    def check(nu, location_matrix, scale_matrix_1, scale_matrix_2) -> None:
        ...
    
    @property
    def set(self) -> MatrixSet:
        ...
    
    @property
    def dimension(self):
        ...
    
    def pdf(self, x):
        ...
    


def MatrixStudentT(symbol, nu, location_matrix, scale_matrix_1, scale_matrix_2) -> RandomMatrixSymbol:
    ...


from typing import Any, Literal, Self
from sympy import Equality, Integral, Ne
from sympy.core.basic import Basic
from sympy.core.function import Lambda
from sympy.core.relational import Relational
from sympy.stats.joint_rv_types import JointDistributionHandmade
from sympy.stats.rv import Density, RandomMatrixSymbol, is_random

__all__ = ['CircularEnsemble', 'CircularUnitaryEnsemble', 'CircularOrthogonalEnsemble', 'CircularSymplecticEnsemble', 'GaussianEnsemble', 'GaussianUnitaryEnsemble', 'GaussianOrthogonalEnsemble', 'GaussianSymplecticEnsemble', 'joint_eigen_distribution', 'JointEigenDistribution', 'level_spacing_distribution']
@is_random.register(RandomMatrixSymbol)
def _(x) -> Literal[True]:
    ...

class RandomMatrixEnsembleModel(Basic):
    def __new__(cls, sym, dim=...) -> Self:
        ...
    
    symbol = ...
    dimension = ...
    def density(self, expr) -> Density:
        ...
    
    def __call__(self, expr) -> Density:
        ...
    


class GaussianEnsembleModel(RandomMatrixEnsembleModel):
    ...


class GaussianUnitaryEnsembleModel(GaussianEnsembleModel):
    @property
    def normalization_constant(self):
        ...
    
    def density(self, expr) -> Basic:
        ...
    
    def joint_eigen_distribution(self) -> Lambda:
        ...
    
    def level_spacing_distribution(self) -> Lambda:
        ...
    


class GaussianOrthogonalEnsembleModel(GaussianEnsembleModel):
    @property
    def normalization_constant(self) -> Equality | Relational | Ne | Integral:
        ...
    
    def density(self, expr) -> Basic:
        ...
    
    def joint_eigen_distribution(self) -> Lambda:
        ...
    
    def level_spacing_distribution(self) -> Lambda:
        ...
    


class GaussianSymplecticEnsembleModel(GaussianEnsembleModel):
    @property
    def normalization_constant(self) -> Equality | Relational | Ne | Integral:
        ...
    
    def density(self, expr) -> Basic:
        ...
    
    def joint_eigen_distribution(self) -> Lambda:
        ...
    
    def level_spacing_distribution(self) -> Lambda:
        ...
    


def GaussianEnsemble(sym, dim) -> RandomMatrixSymbol:
    ...

def GaussianUnitaryEnsemble(sym, dim) -> RandomMatrixSymbol:
    ...

def GaussianOrthogonalEnsemble(sym, dim) -> RandomMatrixSymbol:
    ...

def GaussianSymplecticEnsemble(sym, dim) -> RandomMatrixSymbol:
    ...

class CircularEnsembleModel(RandomMatrixEnsembleModel):
    def density(self, expr):
        ...
    


class CircularUnitaryEnsembleModel(CircularEnsembleModel):
    def joint_eigen_distribution(self) -> Lambda:
        ...
    


class CircularOrthogonalEnsembleModel(CircularEnsembleModel):
    def joint_eigen_distribution(self) -> Lambda:
        ...
    


class CircularSymplecticEnsembleModel(CircularEnsembleModel):
    def joint_eigen_distribution(self) -> Lambda:
        ...
    


def CircularEnsemble(sym, dim) -> RandomMatrixSymbol:
    ...

def CircularUnitaryEnsemble(sym, dim) -> RandomMatrixSymbol:
    ...

def CircularOrthogonalEnsemble(sym, dim) -> RandomMatrixSymbol:
    ...

def CircularSymplecticEnsemble(sym, dim) -> RandomMatrixSymbol:
    ...

def joint_eigen_distribution(mat) -> Any:
    ...

def JointEigenDistribution(mat) -> JointDistributionHandmade:
    ...

def level_spacing_distribution(mat):
    ...


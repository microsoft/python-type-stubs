from typing import List, Self
from sympy import Indexed
from sympy.core.basic import Basic
from sympy.matrices import Matrix
from sympy.tensor.array.mutable_ndim_array import MutableNDimArray
from sympy.tensor.array.ndim_array import ArrayKind, ImmutableNDimArray, NDimArray

class DenseNDimArray(NDimArray):
    _array: List[Basic]
    def __new__(self, *args, **kwargs) -> ImmutableDenseNDimArray:
        ...
    
    @property
    def kind(self) -> ArrayKind:
        ...
    
    def __getitem__(self, index) -> Indexed | Self | Basic:
        ...
    
    @classmethod
    def zeros(cls, *shape):
        ...
    
    def tomatrix(self) -> Matrix:
        ...
    
    def reshape(self, *newshape) -> Self:
        ...
    


class ImmutableDenseNDimArray(DenseNDimArray, ImmutableNDimArray):
    def __new__(cls, iterable, shape=..., **kwargs) -> Self:
        ...
    
    def __setitem__(self, index, value):
        ...
    
    def as_mutable(self) -> MutableDenseNDimArray:
        ...
    


class MutableDenseNDimArray(DenseNDimArray, MutableNDimArray):
    def __new__(cls, iterable=..., shape=..., **kwargs) -> Self:
        ...
    
    def __setitem__(self, index, value) -> None:
        ...
    
    def as_immutable(self) -> ImmutableDenseNDimArray:
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    



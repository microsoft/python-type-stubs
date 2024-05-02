from ctypes import Array
import typing
from typing import Any, Generator, List, Optional, Self, Tuple as tTuple
from sympy import ImmutableSparseNDimArray, NDimArray
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.expr import Expr
from sympy.tensor.array.dense_ndim_array import ImmutableDenseNDimArray

class _ArrayExpr(Expr):
    shape: tTuple[Expr, ...]
    def __getitem__(self, item) -> ArrayElement:
        ...
    


class ArraySymbol(_ArrayExpr):
    def __new__(cls, symbol, shape: typing.Iterable) -> ArraySymbol:
        ...
    
    @property
    def name(self) -> Basic:
        ...
    
    @property
    def shape(self) -> Basic:
        ...
    
    def as_explicit(self) -> ImmutableDenseNDimArray:
        ...
    


class ArrayElement(Expr):
    _diff_wrt = ...
    is_symbol = ...
    is_commutative = ...
    def __new__(cls, name, indices) -> Self:
        ...
    
    @property
    def name(self) -> Basic:
        ...
    
    @property
    def indices(self) -> Basic:
        ...
    


class ZeroArray(_ArrayExpr):
    def __new__(cls, *shape) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, ...]:
        ...
    
    def as_explicit(self):
        ...
    


class OneArray(_ArrayExpr):
    def __new__(cls, *shape) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, ...]:
        ...
    
    def as_explicit(self) -> ImmutableDenseNDimArray:
        ...
    


class _CodegenArrayAbstract(Basic):
    @property
    def subranks(self):
        ...
    
    def subrank(self) -> int:
        ...
    
    @property
    def shape(self):
        ...
    
    def doit(self, **hints):
        ...
    


class ArrayTensorProduct(_CodegenArrayAbstract):
    def __new__(cls, *args, **kwargs) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | Self:
        ...
    
    def as_explicit(self) -> NDimArray | ImmutableDenseNDimArray | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ImmutableSparseNDimArray:
        ...
    


class ArrayAdd(_CodegenArrayAbstract):
    def __new__(cls, *args, **kwargs) -> ZeroArray | Self:
        ...
    
    def as_explicit(self) -> Any:
        ...
    


class PermuteDims(_CodegenArrayAbstract):
    def __new__(cls, expr, permutation=..., index_order_old=..., index_order_new=..., **kwargs) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | Self:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def permutation(self) -> Basic:
        ...
    
    def nest_permutation(self) -> Self | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ArrayAdd:
        ...
    
    def as_explicit(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ImmutableSparseNDimArray | ImmutableDenseNDimArray:
        ...
    


class ArrayDiagonal(_CodegenArrayAbstract):
    def __new__(cls, expr, *diagonal_indices, **kwargs) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | Self:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def diagonal_indices(self) -> tuple[Basic, ...]:
        ...
    
    def as_explicit(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ArrayDiagonal | ImmutableDenseNDimArray | Any:
        ...
    


class ArrayElementwiseApplyFunc(_CodegenArrayAbstract):
    def __new__(cls, function, element) -> Self:
        ...
    
    @property
    def function(self) -> Basic:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    
    def as_explicit(self):
        ...
    


class ArrayContraction(_CodegenArrayAbstract):
    def __new__(cls, expr, *contraction_indices, **kwargs) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | Self:
        ...
    
    def __mul__(self, other) -> Self:
        ...
    
    def __rmul__(self, other) -> Self:
        ...
    
    def split_multiple_contractions(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims:
        ...
    
    def flatten_contraction_of_diagonal(self) -> Self | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims:
        ...
    
    @property
    def free_indices(self):
        ...
    
    @property
    def free_indices_to_position(self) -> dict[Any, Any]:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def contraction_indices(self) -> tuple[Basic, ...]:
        ...
    
    def sort_args_by_name(self) -> Self | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims:
        ...
    
    def as_explicit(self) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | ImmutableDenseNDimArray | Any:
        ...
    


class Reshape(_CodegenArrayAbstract):
    def __new__(cls, expr, shape) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    @property
    def expr(self):
        ...
    
    def doit(self, *args, **kwargs) -> Reshape:
        ...
    
    def as_explicit(self) -> Self | Array:
        ...
    


class _ArgE:
    indices: List[Optional[int]]
    def __init__(self, element, indices: Optional[List[Optional[int]]] = ...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...


class _IndPos:
    def __init__(self, arg: int, rel: int) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __iter__(self) -> Generator[int, Any, None]:
        ...
    


class _EditArrayContraction:
    def __init__(self, base_array: typing.Union[ArrayContraction, ArrayDiagonal, ArrayTensorProduct]) -> None:
        ...
    
    def insert_after(self, arg: _ArgE, new_arg: _ArgE) -> None:
        ...
    
    def get_new_contraction_index(self) -> int:
        ...
    
    def refresh_indices(self) -> None:
        ...
    
    def merge_scalars(self) -> None:
        ...
    
    def to_array_contraction(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims:
        ...
    
    def get_contraction_indices(self) -> List[List[int]]:
        ...
    
    def get_mapping_for_index(self, ind) -> List[_IndPos]:
        ...
    
    def get_contraction_indices_to_ind_rel_pos(self) -> List[List[_IndPos]]:
        ...
    
    def count_args_with_index(self, index: int) -> int:
        ...
    
    def get_args_with_index(self, index: int) -> List[_ArgE]:
        ...
    
    @property
    def number_of_diagonal_indices(self) -> int:
        ...
    
    def track_permutation_start(self) -> None:
        ...
    
    def track_permutation_merge(self, destination: _ArgE, from_element: _ArgE) -> None:
        ...
    
    def get_absolute_free_range(self, arg: _ArgE) -> typing.Tuple[int, int]:
        ...
    
    def get_absolute_range(self, arg: _ArgE) -> typing.Tuple[int, int]:
        ...
    


def get_rank(expr) -> int:
    ...

def get_shape(expr) -> tuple[()]:
    ...

def nest_permutation(expr) -> PermuteDims | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | ArrayAdd:
    ...


from types import NotImplementedType
from typing import Any, Callable, Generator, Literal, LiteralString, Self
from abc import ABC, abstractmethod
from sympy import ImmutableDenseNDimArray, ImmutableSparseNDimArray, Indexed, MutableDenseNDimArray
from sympy.combinatorics.permutations import Perm
from sympy.core import Basic, Expr
from sympy.core.containers import Tuple
from sympy.core.sympify import CantSympify
from sympy.core.operations import AssocOp
from sympy.matrices import Matrix
from sympy.tensor.array.expressions.array_expressions import ArrayContraction, ArrayElement, ArrayTensorProduct, PermuteDims, ZeroArray
from sympy.utilities.decorator import deprecated, memoize_property

def deprecate_data() -> None:
    ...

def deprecate_fun_eval() -> None:
    ...

def deprecate_call() -> None:
    ...

class _IndexStructure(CantSympify):
    def __init__(self, free, dum, index_types, indices, canon_bp=...) -> None:
        ...
    
    @staticmethod
    def from_indices(*indices) -> _IndexStructure:
        ...
    
    @staticmethod
    def from_components_free_dum(components, free, dum) -> _IndexStructure:
        ...
    
    def get_indices(self):
        ...
    
    @staticmethod
    def generate_indices_from_free_dum_index_types(free, dum, index_types) -> list[Any]:
        ...
    
    def get_free_indices(self) -> list[TensorIndex]:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    def perm2tensor(self, g, is_canon_bp=...) -> _IndexStructure:
        ...
    
    def indices_canon_args(self) -> tuple[Perm, list[Any], list[Any]]:
        ...
    


def components_canon_args(components) -> list[Any]:
    ...

class _TensorDataLazyEvaluator(CantSympify):
    _substitutions_dict: dict[Any, Any] = ...
    _substitutions_dict_tensmul: dict[Any, Any] = ...
    def __getitem__(self, key) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @staticmethod
    def data_contract_dum(ndarray_list, dum, ext_rank) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | ImmutableDenseNDimArray | Any:
        ...
    
    def data_tensorhead_from_tensmul(self, data, tensmul, tensorhead) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | ImmutableDenseNDimArray | Any | None:
        ...
    
    def data_from_tensor(self, tensor) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | ImmutableDenseNDimArray | Any | None:
        ...
    
    def __setitem__(self, key, value) -> None:
        ...
    
    def __delitem__(self, key) -> None:
        ...
    
    def __contains__(self, key) -> bool:
        ...
    
    def add_metric_data(self, metric, data) -> None:
        ...
    
    @staticmethod
    def inverse_matrix(ndarray) -> MutableDenseNDimArray:
        ...
    
    @staticmethod
    def inverse_transpose_matrix(ndarray) -> MutableDenseNDimArray:
        ...
    
    @staticmethod
    def add_rearrange_tensmul_parts(new_tensmul, old_tensmul) -> None:
        ...
    
    @staticmethod
    def parse_data(data) -> MutableDenseNDimArray:
        ...
    


_tensor_data_substitution_dict = ...
class _TensorManager:
    def __init__(self) -> None:
        ...
    
    @property
    def comm(self) -> list[dict[Any, Any]]:
        ...
    
    def comm_symbols2i(self, i) -> int:
        ...
    
    def comm_i2symbol(self, i) -> int:
        ...
    
    def set_comm(self, i, j, c) -> None:
        ...
    
    def set_comms(self, *args) -> None:
        ...
    
    def get_comm(self, i, j):
        ...
    
    def clear(self) -> None:
        ...
    


TensorManager = ...
class TensorIndexType(Basic):
    def __new__(cls, name, dummy_name=..., dim=..., eps_dim=..., metric_symmetry=..., metric_name=..., **kwargs) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def dummy_name(self):
        ...
    
    @property
    def dim(self) -> Basic:
        ...
    
    @property
    def eps_dim(self) -> Basic:
        ...
    
    @memoize_property
    def metric(self) -> TensorHead | None:
        ...
    
    @memoize_property
    def delta(self) -> TensorHead:
        ...
    
    @memoize_property
    def epsilon(self) -> TensorHead | None:
        ...
    
    def set_metric(self, tensor) -> None:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data) -> None:
        ...
    
    @data.deleter
    def data(self) -> None:
        ...
    
    def get_kronecker_delta(self) -> TensorHead:
        ...
    
    def get_epsilon(self) -> TensorHead | None:
        ...
    


class TensorIndex(Basic):
    def __new__(cls, name, tensor_index_type, is_up=...) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def tensor_index_type(self) -> Basic:
        ...
    
    @property
    def is_up(self) -> Basic:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __neg__(self) -> TensorIndex:
        ...
    


def tensor_indices(s, typ) -> TensorIndex | list[TensorIndex]:
    ...

class TensorSymmetry(Basic):
    def __new__(cls, *args, **kw_args) -> Self:
        ...
    
    @property
    def base(self) -> Basic:
        ...
    
    @property
    def generators(self) -> Basic:
        ...
    
    @property
    def rank(self):
        ...
    
    @classmethod
    def fully_symmetric(cls, rank) -> TensorSymmetry:
        ...
    
    @classmethod
    def direct_product(cls, *args) -> TensorSymmetry:
        ...
    
    @classmethod
    def riemann(cls) -> TensorSymmetry:
        ...
    
    @classmethod
    def no_symmetry(cls, rank) -> TensorSymmetry:
        ...
    


def tensorsymmetry(*args) -> TensorSymmetry:
    ...

@deprecated("TensorType is deprecated. Use tensor_heads() instead.", deprecated_since_version="1.5", active_deprecations_target="deprecated-tensortype")
class TensorType(Basic):
    is_commutative = ...
    def __new__(cls, index_types, symmetry, **kw_args) -> Self:
        ...
    
    @property
    def index_types(self) -> Basic:
        ...
    
    @property
    def symmetry(self) -> Basic:
        ...
    
    @property
    def types(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __call__(self, s, comm=...) -> TensorHead | list[TensorHead]:
        ...
    


def tensorhead(name, typ, sym=..., comm=...) -> TensorHead:
    ...

class TensorHead(Basic):
    is_commutative = ...
    def __new__(cls, name, index_types, symmetry=..., comm=...) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def index_types(self) -> list[Any]:
        ...
    
    @property
    def symmetry(self) -> Basic:
        ...
    
    @property
    def rank(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def commutes_with(self, other):
        ...
    
    def __call__(self, *indices, **kw_args) -> TensExpr:
        ...
    
    def __pow__(self, other):
        ...
    
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data) -> None:
        ...
    
    @data.deleter
    def data(self) -> None:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None] | Any:
        ...
    


def tensor_heads(s, index_types, symmetry=..., comm=...) -> TensorHead | list[TensorHead]:
    ...

class TensExpr(Expr, ABC):
    _op_priority = ...
    is_commutative = ...
    def __neg__(self):
        ...
    
    def __abs__(self):
        ...
    
    def __add__(self, other) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def __radd__(self, other) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def __sub__(self, other) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def __rsub__(self, other) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def __mul__(self, other) -> TensExpr | TensMul:
        ...
    
    def __rmul__(self, other) -> TensExpr | TensMul:
        ...
    
    def __truediv__(self, other) -> TensExpr | TensMul:
        ...
    
    def __rtruediv__(self, other):
        ...
    
    def __pow__(self, other):
        ...
    
    def __rpow__(self, other):
        ...
    
    @property
    @abstractmethod
    def nocoeff(self):
        ...
    
    @property
    @abstractmethod
    def coeff(self):
        ...
    
    @abstractmethod
    def get_indices(self):
        ...
    
    @abstractmethod
    def get_free_indices(self) -> list[TensorIndex]:
        ...
    
    def fun_eval(self, *index_tuples):
        ...
    
    def get_matrix(self) -> Matrix:
        ...
    
    def expand(self, **hints) -> Self:
        ...
    
    def replace_with_arrays(self, replacement_dict, indices=...) -> ArrayElement | Indexed | ImmutableSparseNDimArray | ImmutableDenseNDimArray | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims:
        ...
    


class TensAdd(TensExpr, AssocOp):
    def __new__(cls, *args, **kw_args) -> Self:
        ...
    
    @property
    def coeff(self):
        ...
    
    @property
    def nocoeff(self) -> Self:
        ...
    
    def get_free_indices(self) -> list[TensorIndex]:
        ...
    
    @memoize_property
    def rank(self) -> Literal[0]:
        ...
    
    @memoize_property
    def free_args(self) -> list[Any]:
        ...
    
    @memoize_property
    def free_indices(self) -> list[TensorIndex] | set[Any]:
        ...
    
    def doit(self, **hints) -> Basic | TensExpr | TensMul | Expr | Self:
        ...
    
    def get_indices(self) -> list[Any]:
        ...
    
    def __call__(self, *indices) -> Self | Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def canon_bp(self) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def equals(self, other) -> bool | NotImplementedType:
        ...
    
    def __getitem__(self, item) -> Any | ArrayElement | Indexed | ImmutableDenseNDimArray | Basic:
        ...
    
    def contract_delta(self, delta) -> TensMul | TensExpr | Basic | Expr | TensAdd:
        ...
    
    def contract_metric(self, g) -> TensMul | TensExpr | Basic | Expr | TensAdd:
        ...
    
    def substitute_indices(self, *index_tuples) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data) -> None:
        ...
    
    @data.deleter
    def data(self) -> None:
        ...
    
    def __iter__(self) -> Any:
        ...
    


class Tensor(TensExpr):
    is_commutative = ...
    _index_structure: _IndexStructure = ...
    args: tuple[TensorHead, Tuple]
    def __new__(cls, tensor_head, indices, *, is_canon_bp=..., **kw_args) -> Self:
        ...
    
    @property
    def free(self):
        ...
    
    @property
    def dum(self):
        ...
    
    @property
    def ext_rank(self):
        ...
    
    @property
    def coeff(self):
        ...
    
    @property
    def nocoeff(self):
        ...
    
    @property
    def component(self):
        ...
    
    @property
    def components(self):
        ...
    
    @property
    def head(self) -> TensorHead:
        ...
    
    @property
    def indices(self) -> Tuple:
        ...
    
    @property
    def free_indices(self) -> set[TensorIndex]:
        ...
    
    @property
    def index_types(self) -> list[Any]:
        ...
    
    @property
    def rank(self) -> int:
        ...
    
    def doit(self, **hints) -> TensExpr:
        ...
    
    @property
    def free_in_args(self) -> list[tuple[Any, Any, Literal[0]]]:
        ...
    
    @property
    def dum_in_args(self) -> list[tuple[Any, Any, Literal[0], Literal[0]]]:
        ...
    
    @property
    def free_args(self) -> list[Any]:
        ...
    
    def commutes_with(self, other) -> type[NotImplementedError] | Literal[0]:
        ...
    
    def perm2tensor(self, g, is_canon_bp=...) -> TensExpr:
        ...
    
    def canon_bp(self) -> Self | TensExpr:
        ...
    
    def split(self) -> list[Self]:
        ...
    
    def sorted_components(self) -> Self:
        ...
    
    def get_indices(self) -> list[TensorIndex]:
        ...
    
    def get_free_indices(self) -> list[TensorIndex]:
        ...
    
    def as_base_exp(self) -> tuple[Self, Any]:
        ...
    
    def substitute_indices(self, *index_tuples) -> TensExpr:
        ...
    
    def __call__(self, *indices) -> Self | TensExpr:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None] | Any:
        ...
    
    def __getitem__(self, item) -> Any | ArrayElement | Indexed | ImmutableDenseNDimArray | Basic:
        ...
    
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data) -> None:
        ...
    
    @data.deleter
    def data(self) -> None:
        ...
    
    def equals(self, other) -> bool:
        ...
    
    def contract_metric(self, g) -> Self:
        ...
    
    def contract_delta(self, metric) -> Self:
        ...
    


class TensMul(TensExpr, AssocOp):
    identity = ...
    _index_structure: _IndexStructure = ...
    def __new__(cls, *args, **kw_args) -> Self:
        ...
    
    index_types = ...
    free = ...
    dum = ...
    free_indices = ...
    rank = ...
    ext_rank = ...
    def doit(self, **hints) -> TensExpr | Self:
        ...
    
    @staticmethod
    def from_data(coeff, components, free, dum, **kw_args) -> TensExpr | TensMul:
        ...
    
    @property
    def free_args(self) -> list[Any]:
        ...
    
    @property
    def components(self) -> list[Any]:
        ...
    
    @property
    def free_in_args(self) -> list[tuple[Any, Any, Any]]:
        ...
    
    @property
    def coeff(self):
        ...
    
    @property
    def nocoeff(self) -> TensExpr | Self:
        ...
    
    @property
    def dum_in_args(self) -> list[tuple[Any, Any, Any, Any]]:
        ...
    
    def equals(self, other):
        ...
    
    def get_indices(self):
        ...
    
    def get_free_indices(self) -> list[TensorIndex]:
        ...
    
    def split(self) -> list[Self] | list[Any]:
        ...
    
    def __neg__(self) -> TensExpr | TensMul:
        ...
    
    def __getitem__(self, item) -> Any | ArrayElement | Indexed | ImmutableDenseNDimArray | Basic:
        ...
    
    def sorted_components(self) -> TensExpr | TensMul:
        ...
    
    def perm2tensor(self, g, is_canon_bp=...) -> TensExpr | TensMul:
        ...
    
    def canon_bp(self) -> Self | TensMul | TensExpr:
        ...
    
    def contract_delta(self, delta):
        ...
    
    def contract_metric(self, g):
        ...
    
    def substitute_indices(self, *index_tuples) -> TensExpr | TensMul:
        ...
    
    def __call__(self, *indices) -> Self | TensExpr | TensMul:
        ...
    
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data):
        ...
    
    @data.deleter
    def data(self):
        ...
    
    def __iter__(self) -> Generator[Any, Any, None] | Any:
        ...
    


class TensorElement(TensExpr):
    def __new__(cls, expr, index_map) -> TensExpr | Tensor | Self:
        ...
    
    @property
    def free(self) -> list[tuple[Any, int]]:
        ...
    
    @property
    def dum(self) -> list[Any]:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def index_map(self) -> Basic:
        ...
    
    @property
    def coeff(self):
        ...
    
    @property
    def nocoeff(self) -> Self:
        ...
    
    def get_free_indices(self):
        ...
    
    def get_indices(self):
        ...
    


class WildTensorHead(TensorHead):
    def __new__(cls, name, index_types=..., symmetry=..., comm=..., unordered_indices=...) -> Self:
        ...
    
    def __call__(self, *indices, **kwargs) -> TensExpr:
        ...
    


class WildTensor(Tensor):
    def __new__(cls, tensor_head, indices, **kw_args) -> Tensor | Self:
        ...
    
    def matches(self, expr, repl_dict=..., old=...) -> dict[Any, Any] | None:
        ...
    


class WildTensorIndex(TensorIndex):
    def __new__(cls, name, tensor_index_type, is_up=..., ignore_updown=...) -> Self:
        ...
    
    @property
    def ignore_updown(self) -> Basic:
        ...
    
    def __neg__(self) -> WildTensorIndex:
        ...
    
    def matches(self, expr, repl_dict=..., old=...) -> dict[Any, Any] | None:
        ...
    


class _WildTensExpr(Basic):
    def __init__(self, expr) -> None:
        ...
    
    def __call__(self, *indices) -> TensExpr:
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def __abs__(self):
        ...
    
    def __add__(self, other) -> Self:
        ...
    
    def __radd__(self, other) -> Self:
        ...
    
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    def __mul__(self, other):
        ...
    
    def __rmul__(self, other):
        ...
    
    def __truediv__(self, other):
        ...
    
    def __rtruediv__(self, other):
        ...
    
    def __pow__(self, other):
        ...
    
    def __rpow__(self, other):
        ...
    


def canon_bp(p):
    ...

def tensor_mul(*a) -> TensExpr | TensMul:
    ...

def riemann_cyclic_replace(t_r):
    ...

def riemann_cyclic(t2) -> TensMul | TensExpr | Basic | Expr | TensAdd:
    ...

def get_lines(ex, index_type) -> tuple[list[Any], list[Any], list[int]]:
    ...

def get_free_indices(t) -> tuple[()] | list[TensorIndex]:
    ...

def get_indices(t) -> tuple[()]:
    ...

def get_dummy_indices(t) -> tuple[()] | list[Any]:
    ...

def get_index_structure(t) -> _IndexStructure:
    ...

def get_coeff(t):
    ...

def contract_metric(t, g):
    ...

def perm2tensor(t, g, is_canon_bp=...) -> TensExpr | TensMul:
    ...

def substitute_indices(t, *index_tuples):
    ...


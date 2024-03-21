from typing import Any, Literal, Self
from sympy.core import Basic, Expr
from sympy.core.function import Lambda
from sympy.core.symbol import Symbol
from sympy.matrices.immutable import ImmutableDenseMatrix
from sympy.series.order import Order
from sympy.tensor.array.dense_ndim_array import ImmutableDenseNDimArray

class Manifold(Basic):
    def __new__(cls, name, dim, **kwargs) -> Self:
        ...
    
    @property
    def name(self) -> Basic:
        ...
    
    @property
    def dim(self) -> Basic:
        ...
    


class Patch(Basic):
    def __new__(cls, name, manifold, **kwargs) -> Self:
        ...
    
    @property
    def name(self) -> Basic:
        ...
    
    @property
    def manifold(self) -> Basic:
        ...
    
    @property
    def dim(self):
        ...
    


class CoordSystem(Basic):
    def __new__(cls, name, patch, symbols=..., relations=..., **kwargs) -> Self:
        ...
    
    @property
    def name(self) -> Basic:
        ...
    
    @property
    def patch(self) -> Basic:
        ...
    
    @property
    def manifold(self):
        ...
    
    @property
    def symbols(self) -> tuple[CoordinateSymbol, ...]:
        ...
    
    @property
    def relations(self) -> Basic:
        ...
    
    @property
    def dim(self):
        ...
    
    def transformation(self, sys) -> Lambda:
        ...
    
    def connect_to(self, to_sys, from_coords, to_exprs, inverse=..., fill_in_gaps=...) -> None:
        ...
    
    def transform(self, sys, coordinates=...) -> Basic | ImmutableDenseMatrix:
        ...
    
    def coord_tuple_transform_to(self, to_sys, coords) -> ImmutableDenseMatrix:
        ...
    
    def jacobian(self, sys, coordinates=...):
        ...
    
    jacobian_matrix = ...
    def jacobian_determinant(self, sys, coordinates=...):
        ...
    
    def point(self, coords) -> Point:
        ...
    
    def point_to_coords(self, point):
        ...
    
    def base_scalar(self, coord_index) -> BaseScalarField:
        ...
    
    coord_function = ...
    def base_scalars(self) -> list[BaseScalarField]:
        ...
    
    coord_functions = ...
    def base_vector(self, coord_index) -> BaseVectorField:
        ...
    
    def base_vectors(self) -> list[BaseVectorField]:
        ...
    
    def base_oneform(self, coord_index) -> Differential:
        ...
    
    def base_oneforms(self) -> list[Any | Differential]:
        ...
    


class CoordinateSymbol(Symbol):
    def __new__(cls, coord_sys, index, **assumptions):
        ...
    
    def __getnewargs__(self) -> tuple[Any, Any]:
        ...
    


class Point(Basic):
    def __new__(cls, coord_sys, coords, **kwargs) -> Self:
        ...
    
    @property
    def patch(self):
        ...
    
    @property
    def manifold(self):
        ...
    
    @property
    def dim(self):
        ...
    
    def coords(self, sys=...):
        ...
    
    @property
    def free_symbols(self):
        ...
    


class BaseScalarField(Expr):
    is_commutative = ...
    def __new__(cls, coord_sys, index, **kwargs) -> Self:
        ...
    
    @property
    def coord_sys(self) -> Basic:
        ...
    
    @property
    def index(self) -> Basic:
        ...
    
    @property
    def patch(self):
        ...
    
    @property
    def manifold(self):
        ...
    
    @property
    def dim(self):
        ...
    
    def __call__(self, *args) -> Self:
        ...
    
    free_symbols: set[Any] = ...


class BaseVectorField(Expr):
    is_commutative = ...
    def __new__(cls, coord_sys, index, **kwargs) -> Self:
        ...
    
    @property
    def coord_sys(self) -> Basic:
        ...
    
    @property
    def index(self) -> Basic:
        ...
    
    @property
    def patch(self):
        ...
    
    @property
    def manifold(self):
        ...
    
    @property
    def dim(self):
        ...
    
    def __call__(self, scalar_field) -> Self:
        ...
    


class Commutator(Expr):
    def __new__(cls, v1, v2) -> Self | Literal[0]:
        ...
    
    @property
    def v1(self) -> Basic:
        ...
    
    @property
    def v2(self) -> Basic:
        ...
    
    def __call__(self, scalar_field):
        ...
    


class Differential(Expr):
    is_commutative = ...
    def __new__(cls, form_field) -> Self:
        ...
    
    @property
    def form_field(self) -> Basic:
        ...
    
    def __call__(self, *vector_fields) -> Self | Literal[0]:
        ...
    


class TensorProduct(Expr):
    def __new__(cls, *args) -> Order:
        ...
    
    def __call__(self, *fields) -> Order:
        ...
    


class WedgeProduct(TensorProduct):
    def __call__(self, *fields):
        ...
    


class LieDerivative(Expr):
    def __new__(cls, v_field, expr) -> Self | Commutator | Literal[0]:
        ...
    
    @property
    def v_field(self) -> Basic:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    def __call__(self, *args):
        ...
    


class BaseCovarDerivativeOp(Expr):
    def __new__(cls, coord_sys, index, christoffel) -> Self:
        ...
    
    @property
    def coord_sys(self) -> Basic:
        ...
    
    @property
    def index(self) -> Basic:
        ...
    
    @property
    def christoffel(self) -> Basic:
        ...
    
    def __call__(self, field):
        ...
    


class CovarDerivativeOp(Expr):
    def __new__(cls, wrt, christoffel) -> Self:
        ...
    
    @property
    def wrt(self) -> Basic:
        ...
    
    @property
    def christoffel(self) -> Basic:
        ...
    
    def __call__(self, field):
        ...
    


def intcurve_series(vector_field, param, start_point, n=..., coord_sys=..., coeffs=...) -> list[ImmutableDenseMatrix] | ImmutableDenseMatrix:
    ...

def intcurve_diffequ(vector_field, param, start_point, coord_sys=...) -> tuple[list[Any], list[Any]]:
    ...

def dummyfy(args, exprs) -> tuple[ImmutableDenseMatrix, ImmutableDenseMatrix]:
    ...

def contravariant_order(expr, _strict=...) -> int:
    ...

def covariant_order(expr, _strict=...) -> int:
    ...

def vectors_in_basis(expr, to_sys):
    ...

def twoform_to_matrix(expr) -> ImmutableDenseMatrix:
    ...

def metric_to_Christoffel_1st(expr) -> ImmutableDenseNDimArray:
    ...

def metric_to_Christoffel_2nd(expr) -> ImmutableDenseNDimArray:
    ...

def metric_to_Riemann_components(expr) -> ImmutableDenseNDimArray:
    ...

def metric_to_Ricci_components(expr) -> ImmutableDenseNDimArray:
    ...

class _deprecated_container:
    def __init__(self, message, data) -> None:
        ...
    
    def warn(self) -> None:
        ...
    
    def __iter__(self):
        ...
    
    def __getitem__(self, key):
        ...
    
    def __contains__(self, key):
        ...
    


class _deprecated_list(_deprecated_container, list):
    ...


class _deprecated_dict(_deprecated_container, dict):
    ...



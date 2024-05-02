from types import NotImplementedType
from typing import Any, Literal, Self
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.core.power import Pow
from sympy.matrices.dense import MutableDenseMatrix

class Quaternion(Expr):
    _op_priority = ...
    is_commutative = ...
    def __new__(cls, a=..., b=..., c=..., d=..., real_field=..., norm=...) -> Self:
        ...
    
    def set_norm(self, norm) -> None:
        ...
    
    @property
    def a(self):
        ...
    
    @property
    def b(self):
        ...
    
    @property
    def c(self):
        ...
    
    @property
    def d(self):
        ...
    
    @property
    def real_field(self):
        ...
    
    @property
    def product_matrix_left(self) -> MutableDenseMatrix:
        ...
    
    @property
    def product_matrix_right(self) -> MutableDenseMatrix:
        ...
    
    def to_Matrix(self, vector_only=...) -> MutableDenseMatrix:
        ...
    
    @classmethod
    def from_Matrix(cls, elements) -> Quaternion:
        ...
    
    @classmethod
    def from_euler(cls, angles, seq) -> Any:
        ...
    
    def to_euler(self, seq, angle_addition=..., avoid_square_root=...) -> tuple[int, ...]:
        ...
    
    @classmethod
    def from_axis_angle(cls, vector, angle) -> Self:
        ...
    
    @classmethod
    def from_rotation_matrix(cls, M) -> Quaternion:
        ...
    
    def __add__(self, other) -> Quaternion:
        ...
    
    def __radd__(self, other) -> Quaternion:
        ...
    
    def __sub__(self, other) -> Quaternion:
        ...
    
    def __mul__(self, other) -> Quaternion:
        ...
    
    def __rmul__(self, other) -> Quaternion:
        ...
    
    def __pow__(self, p) -> NotImplementedType | Quaternion | Literal[1]:
        ...
    
    def __neg__(self) -> Quaternion:
        ...
    
    def __truediv__(self, other):
        ...
    
    def __rtruediv__(self, other):
        ...
    
    def diff(self, *symbols, **kwargs) -> Self:
        ...
    
    def add(self, other) -> Quaternion:
        ...
    
    def mul(self, other) -> Quaternion:
        ...
    
    def norm(self) -> Pow:
        ...
    
    def normalize(self):
        ...
    
    def inverse(self):
        ...
    
    def pow(self, p) -> NotImplementedType | Quaternion | Literal[1]:
        ...
    
    def exp(self) -> Quaternion:
        ...
    
    def pow_cos_sin(self, p):
        ...
    
    def integrate(self, *args) -> Quaternion:
        ...
    
    @staticmethod
    def rotate_point(pin, r) -> tuple[Any, Any, Any]:
        ...
    
    def to_axis_angle(self) -> tuple[tuple[Any, Any, Any], Any]:
        ...
    
    def to_rotation_matrix(self, v=..., homogeneous=...) -> MutableDenseMatrix:
        ...
    
    def scalar_part(self):
        ...
    
    def vector_part(self) -> Quaternion:
        ...
    
    def axis(self) -> Quaternion:
        ...
    
    def is_pure(self):
        ...
    
    def is_zero_quaternion(self) -> bool | None:
        ...
    
    def angle(self) -> type[UndefinedFunction]:
        ...
    
    def arc_coplanar(self, other) -> bool | None:
        ...
    
    @classmethod
    def vector_coplanar(cls, q1, q2, q3) -> Any | bool | None:
        ...
    
    def parallel(self, other):
        ...
    
    def orthogonal(self, other):
        ...
    
    def index_vector(self) -> Quaternion:
        ...
    
    def mensor(self) -> type[UndefinedFunction]:
        ...
    



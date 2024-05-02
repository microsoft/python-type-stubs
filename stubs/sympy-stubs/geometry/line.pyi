from types import NotImplementedType
from typing import Any, Self
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.core.power import Pow
from sympy.geometry.entity import GeometrySet
from sympy.geometry.point import Point, Point2D, Point3D
from sympy.sets.sets import Complement, FiniteSet, Intersection, Union

class LinearEntity(GeometrySet):
    def __new__(cls, p1, p2=..., **kwargs) -> Self:
        ...
    
    def __contains__(self, other):
        ...
    
    @property
    def ambient_dimension(self) -> int:
        ...
    
    def angle_between(self, l2) -> type[UndefinedFunction]:
        ...
    
    def smallest_angle_between(self, l2) -> type[UndefinedFunction]:
        ...
    
    def arbitrary_point(self, parameter=...):
        ...
    
    @staticmethod
    def are_concurrent(*lines) -> bool:
        ...
    
    def contains(self, other):
        ...
    
    @property
    def direction(self):
        ...
    
    def intersection(self, other):
        ...
    
    def is_parallel(self, l2):
        ...
    
    def is_perpendicular(self, l2):
        ...
    
    def is_similar(self, other) -> bool:
        ...
    
    @property
    def length(self):
        ...
    
    @property
    def p1(self) -> Basic:
        ...
    
    @property
    def p2(self) -> Basic:
        ...
    
    def parallel_line(self, p) -> Line | Line2D | Line3D | None:
        ...
    
    def perpendicular_line(self, p) -> Line | Line2D | Line3D | None:
        ...
    
    def perpendicular_segment(self, p) -> Point | Point2D | Point3D | Segment2D | Segment3D | Segment:
        ...
    
    @property
    def points(self) -> tuple[Basic, Basic]:
        ...
    
    def projection(self, other) -> FiniteSet | Intersection | Union | Complement | Basic:
        ...
    
    def random_point(self, seed=...):
        ...
    
    def bisectors(self, other) -> list[Self] | list[Line | Line2D | Line3D | None]:
        ...
    


class Line(LinearEntity):
    def __new__(cls, *args, **kwargs) -> Line | Line2D | Line3D | Self | None:
        ...
    
    def contains(self, other) -> bool:
        ...
    
    def distance(self, other) -> Pow | Any:
        ...
    
    def equals(self, other) -> bool:
        ...
    
    def plot_interval(self, parameter=...) -> list[Any]:
        ...
    


class Ray(LinearEntity):
    def __new__(cls, p1, p2=..., **kwargs) -> Ray2D | Ray3D | Self:
        ...
    
    def contains(self, other) -> bool:
        ...
    
    def distance(self, other):
        ...
    
    def equals(self, other) -> bool | NotImplementedType:
        ...
    
    def plot_interval(self, parameter=...) -> list[Any]:
        ...
    
    @property
    def source(self) -> Basic:
        ...
    


class Segment(LinearEntity):
    def __new__(cls, p1, p2, **kwargs) -> Point | Point2D | Point3D | Segment2D | Segment3D | Self:
        ...
    
    def contains(self, other) -> bool:
        ...
    
    def equals(self, other) -> bool:
        ...
    
    def distance(self, other) -> Pow | Any:
        ...
    
    @property
    def length(self) -> Pow | Any:
        ...
    
    @property
    def midpoint(self) -> Point | Point2D | Point3D:
        ...
    
    def perpendicular_bisector(self, p=...) -> Point | Point2D | Point3D | Segment2D | Segment3D | Segment | Line | Line2D | Line3D | None:
        ...
    
    def plot_interval(self, parameter=...) -> list[Any]:
        ...
    


class LinearEntity2D(LinearEntity):
    @property
    def bounds(self) -> tuple[Any, Any, Any, Any]:
        ...
    
    def perpendicular_line(self, p) -> Line | Line2D | Line3D | None:
        ...
    
    @property
    def slope(self):
        ...
    


class Line2D(LinearEntity2D, Line):
    def __new__(cls, p1, pt=..., slope=..., **kwargs) -> Self:
        ...
    
    @property
    def coefficients(self) -> tuple[Any, Any, Any] | tuple[Any, ...]:
        ...
    
    def equation(self, x=..., y=...):
        ...
    


class Ray2D(LinearEntity2D, Ray):
    def __new__(cls, p1, pt=..., angle=..., **kwargs) -> Self:
        ...
    
    @property
    def xdirection(self):
        ...
    
    @property
    def ydirection(self):
        ...
    
    def closing_angle(self, r2):
        ...
    


class Segment2D(LinearEntity2D, Segment):
    def __new__(cls, p1, p2, **kwargs) -> Point | Point2D | Point3D | Self:
        ...
    


class LinearEntity3D(LinearEntity):
    def __new__(cls, p1, p2, **kwargs) -> Self:
        ...
    
    ambient_dimension = ...
    @property
    def direction_ratio(self):
        ...
    
    @property
    def direction_cosine(self):
        ...
    


class Line3D(LinearEntity3D, Line):
    def __new__(cls, p1, pt=..., direction_ratio=..., **kwargs) -> Self:
        ...
    
    def equation(self, x=..., y=..., z=...) -> Tuple:
        ...
    


class Ray3D(LinearEntity3D, Ray):
    def __new__(cls, p1, pt=..., direction_ratio=..., **kwargs) -> Self:
        ...
    
    @property
    def xdirection(self):
        ...
    
    @property
    def ydirection(self):
        ...
    
    @property
    def zdirection(self):
        ...
    


class Segment3D(LinearEntity3D, Segment):
    def __new__(cls, p1, p2, **kwargs) -> Point | Point2D | Point3D | Self:
        ...
    



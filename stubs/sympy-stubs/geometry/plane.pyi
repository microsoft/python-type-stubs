from typing import Any, Literal, Self
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.geometry.entity import GeometryEntity
from sympy.geometry.line import Line3D, Ray3D, Segment3D
from sympy.geometry.point import Point, Point2D, Point3D

class Plane(GeometryEntity):
    def __new__(cls, p1, a=..., b=..., **kwargs) -> Self:
        ...
    
    def __contains__(self, o) -> Literal[False]:
        ...
    
    def angle_between(self, o) -> type[UndefinedFunction] | None:
        ...
    
    def arbitrary_point(self, u=..., v=...) -> Point3D:
        ...
    
    @staticmethod
    def are_concurrent(*planes) -> bool:
        ...
    
    def distance(self, o) -> Expr:
        ...
    
    def equals(self, o) -> Any | Literal[False]:
        ...
    
    def equation(self, x=..., y=..., z=...) -> int:
        ...
    
    def intersection(self, o) -> list[Point | Point2D | Point3D] | list[Any] | list[Point | Point2D | Point3D | Segment3D | Ray3D | Line3D] | list[Any | Point3D | Basic] | list[Self] | list[Line3D] | None:
        ...
    
    def is_coplanar(self, o) -> bool | None:
        ...
    
    def is_parallel(self, l) -> bool | None:
        ...
    
    def is_perpendicular(self, l) -> bool:
        ...
    
    @property
    def normal_vector(self) -> Basic:
        ...
    
    @property
    def p1(self) -> Basic:
        ...
    
    def parallel_plane(self, pt) -> Plane:
        ...
    
    def perpendicular_line(self, pt) -> Line3D:
        ...
    
    def perpendicular_plane(self, *pts) -> Plane:
        ...
    
    def projection_line(self, line) -> Point | Point2D | Point3D | Segment3D | Ray3D | Line3D | Basic | Self | None:
        ...
    
    def projection(self, pt) -> Point | Point2D | Point3D | Segment3D | Ray3D | Line3D | Basic | Self:
        ...
    
    def random_point(self, seed=...) -> Point3D | Basic:
        ...
    
    def parameter_value(self, other, u, v=...) -> Point | Point2D | Point3D:
        ...
    
    @property
    def ambient_dimension(self):
        ...
    



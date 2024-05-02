from typing import Any, Literal, Self
from sympy.core.basic import Basic
from sympy.geometry.entity import GeometrySet
from sympy.geometry.point import Point, Point2D, Point3D

class Parabola(GeometrySet):
    def __new__(cls, focus=..., directrix=..., **kwargs) -> Self:
        ...
    
    @property
    def ambient_dimension(self) -> Literal[2]:
        ...
    
    @property
    def axis_of_symmetry(self):
        ...
    
    @property
    def directrix(self) -> Basic:
        ...
    
    @property
    def eccentricity(self):
        ...
    
    def equation(self, x=..., y=...):
        ...
    
    @property
    def focal_length(self):
        ...
    
    @property
    def focus(self) -> Basic:
        ...
    
    def intersection(self, o) -> list[Parabola] | list[Any] | list[Point2D]:
        ...
    
    @property
    def p_parameter(self):
        ...
    
    @property
    def vertex(self) -> Point | Point2D | Point3D:
        ...
    



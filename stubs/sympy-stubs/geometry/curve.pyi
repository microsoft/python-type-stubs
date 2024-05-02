from typing import Any, Self
from sympy.core.basic import Basic
from sympy.core.relational import Equality, Ne, Relational
from sympy.core.symbol import Symbol
from sympy.geometry.entity import GeometrySet
from sympy.geometry.point import Point, Point2D, Point3D

class Curve(GeometrySet):
    def __new__(cls, function, limits) -> Self:
        ...
    
    def __call__(self, f) -> Self | Basic:
        ...
    
    def arbitrary_point(self, parameter=...) -> Point | Point2D | Point3D:
        ...
    
    @property
    def free_symbols(self) -> set[Any]:
        ...
    
    @property
    def ambient_dimension(self) -> int:
        ...
    
    @property
    def functions(self) -> Basic:
        ...
    
    @property
    def limits(self) -> Basic:
        ...
    
    @property
    def parameter(self):
        ...
    
    @property
    def length(self) -> Equality | Relational | Ne:
        ...
    
    def plot_interval(self, parameter=...) -> list[Any | Symbol]:
        ...
    
    def rotate(self, angle=..., pt=...) -> Self:
        ...
    
    def scale(self, x=..., y=..., pt=...) -> Self:
        ...
    
    def translate(self, x=..., y=...) -> Self:
        ...
    



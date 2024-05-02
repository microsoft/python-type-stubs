from types import NotImplementedType
from typing import Any, Literal, Self
from sympy.core.basic import Basic
from sympy.core.power import Pow
from sympy.geometry.entity import GeometrySet
from sympy.geometry.line import Line, Line2D, Line3D, Segment, Segment2D, Segment3D
from sympy.geometry.point import Point, Point2D, Point3D

class Ellipse(GeometrySet):
    def __contains__(self, o) -> bool | NotImplementedType:
        ...
    
    def __eq__(self, o) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __new__(cls, center=..., hradius=..., vradius=..., eccentricity=..., **kwargs) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | Self | None:
        ...
    
    @property
    def ambient_dimension(self) -> Literal[2]:
        ...
    
    @property
    def apoapsis(self):
        ...
    
    def arbitrary_point(self, parameter=...) -> Point | Point2D | Point3D:
        ...
    
    @property
    def area(self):
        ...
    
    @property
    def bounds(self) -> tuple[Any, Any, Any, Any]:
        ...
    
    @property
    def center(self) -> Basic:
        ...
    
    @property
    def circumference(self):
        ...
    
    @property
    def eccentricity(self):
        ...
    
    def encloses_point(self, p) -> bool | None:
        ...
    
    def equation(self, x=..., y=..., _slope=...):
        ...
    
    def evolute(self, x=..., y=...):
        ...
    
    @property
    def foci(self) -> tuple[Basic, Basic] | tuple[Any, Any] | None:
        ...
    
    @property
    def focus_distance(self) -> Pow | Any:
        ...
    
    @property
    def hradius(self) -> Basic:
        ...
    
    def intersection(self, o) -> list[Point] | list[Any] | Self:
        ...
    
    def is_tangent(self, o) -> bool:
        ...
    
    @property
    def major(self) -> Basic:
        ...
    
    @property
    def minor(self) -> Basic:
        ...
    
    def normal_lines(self, p, prec=...) -> list[Any] | list[Line | Line2D | Line3D | None]:
        ...
    
    @property
    def periapsis(self):
        ...
    
    @property
    def semilatus_rectum(self):
        ...
    
    def auxiliary_circle(self) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    def director_circle(self) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    def plot_interval(self, parameter=...) -> list[Any]:
        ...
    
    def random_point(self, seed=...) -> Point | Point2D | Point3D:
        ...
    
    def reflect(self, line) -> Self:
        ...
    
    def rotate(self, angle=..., pt=...) -> Self:
        ...
    
    def scale(self, x=..., y=..., pt=...) -> Self:
        ...
    
    def tangent_lines(self, p) -> list[Any] | list[Line | Line2D | Line3D | None]:
        ...
    
    @property
    def vradius(self) -> Basic:
        ...
    
    def second_moment_of_area(self, point=...) -> tuple[Any, Any, Literal[0]] | tuple[Any, Any, Any]:
        ...
    
    def polar_second_moment_of_area(self):
        ...
    
    def section_modulus(self, point=...) -> tuple[Any, Any]:
        ...
    


class Circle(Ellipse):
    def __new__(cls, *args, **kwargs) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | Self | None:
        ...
    
    @property
    def circumference(self):
        ...
    
    def equation(self, x=..., y=...):
        ...
    
    def intersection(self, o) -> list[Point] | list[Any] | Ellipse:
        ...
    
    @property
    def radius(self) -> Basic:
        ...
    
    def reflect(self, line) -> Self:
        ...
    
    def scale(self, x=..., y=..., pt=...) -> Self | Ellipse:
        ...
    
    @property
    def vradius(self):
        ...
    



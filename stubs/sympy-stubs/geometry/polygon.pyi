from types import NotImplementedType
from typing import Any, LiteralString, Self
from sympy.core.basic import Basic
from sympy.core.power import Pow
from sympy.functions.elementary.piecewise import Piecewise
from sympy.geometry.ellipse import Circle
from sympy.geometry.entity import GeometryEntity, GeometrySet
from sympy.geometry.line import Line, Line2D, Line3D, Segment, Segment2D, Segment3D
from sympy.geometry.point import Point, Point2D, Point3D

class Polygon(GeometrySet):
    __slots__ = ...
    def __new__(cls, *args, n=..., **kwargs) -> RegularPolygon | Self | Triangle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    @property
    def area(self):
        ...
    
    @property
    def angles(self) -> dict[Any, Any]:
        ...
    
    @property
    def ambient_dimension(self):
        ...
    
    @property
    def perimeter(self):
        ...
    
    @property
    def vertices(self) -> list[Basic]:
        ...
    
    @property
    def centroid(self) -> Point | Point2D | Point3D:
        ...
    
    def second_moment_of_area(self, point=...) -> tuple[Any, Any, Any]:
        ...
    
    def first_moment_of_area(self, point=...) -> tuple[Any, Any]:
        ...
    
    def polar_second_moment_of_area(self):
        ...
    
    def section_modulus(self, point=...) -> tuple[Any, Any]:
        ...
    
    @property
    def sides(self) -> list[Any]:
        ...
    
    @property
    def bounds(self) -> tuple[Any, Any, Any, Any]:
        ...
    
    def is_convex(self) -> bool:
        ...
    
    def encloses_point(self, p) -> bool | None:
        ...
    
    def arbitrary_point(self, parameter=...) -> Piecewise:
        ...
    
    def parameter_value(self, other, t) -> dict[Any, Any]:
        ...
    
    def plot_interval(self, parameter=...) -> list[Any]:
        ...
    
    def intersection(self, o) -> list[Any]:
        ...
    
    def cut_section(self, line) -> tuple[RegularPolygon | Polygon | Triangle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None, RegularPolygon | Polygon | Triangle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None]:
        ...
    
    def distance(self, o):
        ...
    
    def __contains__(self, o) -> NotImplementedType | bool:
        ...
    
    def bisectors(self, prec=...) -> dict[Any, Any]:
        ...
    


class RegularPolygon(Polygon):
    __slots__ = ...
    def __new__(cls, c, r, n, rot=..., **kwargs) -> Self:
        ...
    
    @property
    def args(self) -> tuple[Any, Any, Any, Any]:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    @property
    def area(self):
        ...
    
    @property
    def length(self):
        ...
    
    @property
    def center(self):
        ...
    
    centroid = ...
    @property
    def circumcenter(self):
        ...
    
    @property
    def radius(self):
        ...
    
    @property
    def circumradius(self):
        ...
    
    @property
    def rotation(self):
        ...
    
    @property
    def apothem(self):
        ...
    
    @property
    def inradius(self):
        ...
    
    @property
    def interior_angle(self):
        ...
    
    @property
    def exterior_angle(self):
        ...
    
    @property
    def circumcircle(self) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    @property
    def incircle(self) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    @property
    def angles(self) -> dict[Any, Any]:
        ...
    
    def encloses_point(self, p) -> bool | None:
        ...
    
    def spin(self, angle) -> None:
        ...
    
    def rotate(self, angle, pt=...) -> GeometryEntity:
        ...
    
    def scale(self, x=..., y=..., pt=...) -> Point3D | Polygon | Triangle | Point | Segment2D | Segment3D | Segment | Self:
        ...
    
    def reflect(self, line) -> Self:
        ...
    
    @property
    def vertices(self) -> list[Point | Point2D | Point3D]:
        ...
    
    def __eq__(self, o) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class Triangle(Polygon):
    def __new__(cls, *args, **kwargs) -> Triangle | Self | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    @property
    def vertices(self) -> tuple[Basic, ...]:
        ...
    
    def is_similar(self, t2) -> bool:
        ...
    
    def is_equilateral(self) -> bool:
        ...
    
    def is_isosceles(self) -> bool:
        ...
    
    def is_scalene(self) -> bool:
        ...
    
    def is_right(self):
        ...
    
    @property
    def altitudes(self) -> dict[Basic, Any]:
        ...
    
    @property
    def orthocenter(self):
        ...
    
    @property
    def circumcenter(self):
        ...
    
    @property
    def circumradius(self) -> Pow | Any:
        ...
    
    @property
    def circumcircle(self) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    def bisectors(self) -> dict[Basic, Point | Point2D | Point3D | Segment2D | Segment3D | Segment]:
        ...
    
    @property
    def incenter(self) -> Point | Point2D | Point3D:
        ...
    
    @property
    def inradius(self):
        ...
    
    @property
    def incircle(self) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    @property
    def exradii(self) -> dict[Any, Any]:
        ...
    
    @property
    def excenters(self) -> dict[Any, Point | Point2D | Point3D]:
        ...
    
    @property
    def medians(self) -> dict[Basic, Point | Point2D | Point3D | Segment2D | Segment3D | Segment]:
        ...
    
    @property
    def medial(self) -> Triangle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    @property
    def nine_point_circle(self) -> Circle | Point | Point2D | Point3D | Segment2D | Segment3D | Segment | None:
        ...
    
    @property
    def eulerline(self) -> Line | Line2D | Line3D | None:
        ...
    


def rad(d):
    ...

def deg(r):
    ...


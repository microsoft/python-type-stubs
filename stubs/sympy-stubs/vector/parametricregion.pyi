from functools import singledispatch
from typing import Any, Self

from sympy.core import Basic
from sympy.geometry import Curve, Ellipse, Point, Polygon, Segment
from sympy.vector import ImplicitRegion

class ParametricRegion(Basic):
    def __new__(cls, definition, *bounds) -> Self:
        ...
    
    @property
    def definition(self) -> Basic:
        ...
    
    @property
    def limits(self):
        ...
    
    @property
    def parameters(self):
        ...
    
    @property
    def dimensions(self) -> int:
        ...
    


@singledispatch
def parametric_region_list(reg):
    ...

@parametric_region_list.register(Point)
def _(obj) -> list[ParametricRegion]:
    ...

@parametric_region_list.register(Curve)
def _(obj) -> list[ParametricRegion]:
    ...

@parametric_region_list.register(Ellipse)
def _(obj, parameter=...) -> list[ParametricRegion]:
    ...

@parametric_region_list.register(Segment)
def _(obj, parameter=...) -> list[ParametricRegion]:
    ...

@parametric_region_list.register(Polygon)
def _(obj, parameter=...) -> list[Any]:
    ...

@parametric_region_list.register(ImplicitRegion)
def _(obj, parameters=...) -> list[ParametricRegion]:
    ...


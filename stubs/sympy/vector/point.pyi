from typing import Any, Self
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.vector.vector import VectorZero

class Point(Basic):
    def __new__(cls, name, position=..., parent_point=...) -> Self:
        ...
    
    @cacheit
    def position_wrt(self, other) -> VectorZero:
        ...
    
    def locate_new(self, name, position) -> Point:
        ...
    
    def express_coordinates(self, coordinate_system) -> tuple[Any, ...]:
        ...
    



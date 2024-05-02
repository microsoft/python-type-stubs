from typing import Any, Callable
from sympy.core.basic import Basic
from sympy.core.cache import cacheit

class CoordSys3D(Basic):
    def __new__(cls, name, transformation=..., parent=..., location=..., rotation_matrix=..., vector_names=..., variable_names=...):
        ...
    
    def __iter__(self):
        ...
    
    @property
    def origin(self):
        ...
    
    def base_vectors(self):
        ...
    
    def base_scalars(self):
        ...
    
    def lame_coefficients(self):
        ...
    
    def transformation_to_parent(self):
        ...
    
    def transformation_from_parent(self) -> tuple[Any, ...]:
        ...
    
    def transformation_from_parent_function(self) -> Callable[..., tuple[Any, ...]]:
        ...
    
    def rotation_matrix(self, other):
        ...
    
    @cacheit
    def position_wrt(self, other):
        ...
    
    def scalar_map(self, other) -> dict[Any, Any]:
        ...
    
    def locate_new(self, name, position, vector_names=..., variable_names=...) -> CoordSys3D:
        ...
    
    def orient_new(self, name, orienters, location=..., vector_names=..., variable_names=...) -> CoordSys3D:
        ...
    
    def orient_new_axis(self, name, angle, axis, location=..., vector_names=..., variable_names=...) -> CoordSys3D:
        ...
    
    def orient_new_body(self, name, angle1, angle2, angle3, rotation_order, location=..., vector_names=..., variable_names=...) -> CoordSys3D:
        ...
    
    def orient_new_space(self, name, angle1, angle2, angle3, rotation_order, location=..., vector_names=..., variable_names=...) -> CoordSys3D:
        ...
    
    def orient_new_quaternion(self, name, q0, q1, q2, q3, location=..., vector_names=..., variable_names=...) -> CoordSys3D:
        ...
    
    def create_new(self, name, transformation, variable_names=..., vector_names=...) -> CoordSys3D:
        ...
    
    def __init__(self, name, location=..., rotation_matrix=..., parent=..., vector_names=..., variable_names=..., latex_vects=..., pretty_vects=..., latex_scalars=..., pretty_scalars=..., transformation=...) -> None:
        ...
    



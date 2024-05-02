from typing import Self

from sympy.core.basic import Basic
from sympy.core.cache import cacheit

class Orienter(Basic):
    def rotation_matrix(self):
        ...
    


class AxisOrienter(Orienter):
    def __new__(cls, angle, axis) -> Self:
        ...
    
    def __init__(self, angle, axis) -> None:
        ...
    
    @cacheit
    def rotation_matrix(self, system):
        ...
    
    @property
    def angle(self):
        ...
    
    @property
    def axis(self):
        ...
    


class ThreeAngleOrienter(Orienter):
    def __new__(cls, angle1, angle2, angle3, rot_order) -> Self:
        ...
    
    @property
    def angle1(self):
        ...
    
    @property
    def angle2(self):
        ...
    
    @property
    def angle3(self):
        ...
    
    @property
    def rot_order(self):
        ...
    


class BodyOrienter(ThreeAngleOrienter):
    _in_order = ...
    def __new__(cls, angle1, angle2, angle3, rot_order) -> Self:
        ...
    
    def __init__(self, angle1, angle2, angle3, rot_order) -> None:
        ...
    


class SpaceOrienter(ThreeAngleOrienter):
    _in_order = ...
    def __new__(cls, angle1, angle2, angle3, rot_order) -> Self:
        ...
    
    def __init__(self, angle1, angle2, angle3, rot_order) -> None:
        ...
    


class QuaternionOrienter(Orienter):
    def __new__(cls, q0, q1, q2, q3) -> Self:
        ...
    
    def __init__(self, angle1, angle2, angle3, rot_order) -> None:
        ...
    
    @property
    def q0(self):
        ...
    
    @property
    def q1(self):
        ...
    
    @property
    def q2(self):
        ...
    
    @property
    def q3(self):
        ...
    



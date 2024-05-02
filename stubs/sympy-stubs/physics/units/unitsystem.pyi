from typing import Dict as tDict, Set as tSet

from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.physics.units.dimensions import Dimension, _QuantityMapper
from sympy.physics.units.quantities import Quantity
from sympy.series.order import Order

class UnitSystem(_QuantityMapper):
    _unit_systems: tDict[str, UnitSystem] = ...
    def __init__(self, base_units, units=..., name=..., descr=..., dimension_system=..., derived_units: tDict[Dimension, Quantity] = ...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def extend(self, base, units=..., name=..., description=..., dimension_system=..., derived_units: tDict[Dimension, Quantity] = ...) -> UnitSystem:
        ...
    
    def get_dimension_system(self) -> None:
        ...
    
    def get_quantity_dimension(self, unit) -> Expr | Dimension:
        ...
    
    def get_quantity_scale_factor(self, unit):
        ...
    
    @staticmethod
    def get_unit_system(unit_system) -> UnitSystem:
        ...
    
    @staticmethod
    def get_default_unit_system() -> UnitSystem:
        ...
    
    @property
    def dim(self) -> int:
        ...
    
    @property
    def is_consistent(self):
        ...
    
    @property
    def derived_units(self) -> tDict[Dimension, Quantity]:
        ...
    
    def get_dimensional_expr(self, expr) -> Order | type[UndefinedFunction]:
        ...
    
    def get_units_non_prefixed(self) -> tSet[Quantity]:
        ...
    



from sympy.core.add import Add
from sympy.physics.units.quantities import Quantity

def convert_to(expr, target_units, unit_system=...) -> Add | Quantity:
    ...

def quantity_simplify(expr, across_dimensions: bool = ..., unit_system=...) -> Add | Quantity:
    ...

def check_dimensions(expr, unit_system=...):
    ...


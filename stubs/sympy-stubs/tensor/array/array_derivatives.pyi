from sympy.core.function import Derivative

class ArrayDerivative(Derivative):
    is_scalar = ...
    def __new__(cls, expr, *variables, **kwargs) -> ArrayDerivative:
        ...
    
    @property
    def shape(self):
        ...
    



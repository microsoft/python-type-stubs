from typing import Any, Self

rgen = ...
class Point:
    def __init__(self, x_cord, z_cord, a_24, mod) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def add(self, Q, diff) -> Point:
        ...
    
    def double(self) -> Point:
        ...
    
    def mont_ladder(self, k) -> Self | Point:
        ...
    


def ecm(n, B1=..., B2=..., max_curve=..., seed=...) -> set[Any]:
    ...


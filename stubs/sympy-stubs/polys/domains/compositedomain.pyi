from typing import Self
from sympy.polys.domains.domain import Domain

class CompositeDomain(Domain):
    is_Composite = ...
    def inject(self, *symbols) -> Self:
        ...
    
    def drop(self, *symbols) -> Self:
        ...
    



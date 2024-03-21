from typing import Self
from sympy.polys.domains.domain import Domain

class SimpleDomain(Domain):
    is_Simple = True
    def inject(self, *gens) -> Self:
        ...


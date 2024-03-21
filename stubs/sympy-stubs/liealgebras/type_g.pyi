from typing import Literal, Self
from sympy.liealgebras.cartan_type import Standard_Cartan
from sympy.matrices import Matrix

class TypeG(Standard_Cartan):
    def __new__(cls, n) -> Self:
        ...
    
    def dimension(self) -> Literal[3]:
        ...
    
    def simple_root(self, i) -> list[int]:
        ...
    
    def positive_roots(self) -> dict[int, list[int]]:
        ...
    
    def roots(self) -> Literal[12]:
        ...
    
    def cartan_matrix(self) -> Matrix:
        ...
    
    def basis(self) -> Literal[14]:
        ...
    
    def dynkin_diagram(self) -> Literal['0≡<≡0\n1   2']:
        ...
    



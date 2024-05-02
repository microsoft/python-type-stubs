from typing import Any, Literal, Self
from sympy.liealgebras.cartan_type import Standard_Cartan

class TypeE(Standard_Cartan):
    def __new__(cls, n) -> Self:
        ...
    
    def dimension(self) -> Literal[8]:
        ...
    
    def basic_root(self, i, j) -> list[int]:
        ...
    
    def simple_root(self, i) -> list[float] | list[int]:
        ...
    
    def positive_roots(self) -> dict[Any, Any] | None:
        ...
    
    def roots(self) -> Literal[72, 126, 240] | None:
        ...
    
    def cartan_matrix(self):
        ...
    
    def basis(self) -> Literal[78, 133, 248] | None:
        ...
    
    def dynkin_diagram(self) -> str:
        ...
    



from types import NotImplementedType
from typing import Any, Self
class MutablePolyDenseMatrix:
    def __new__(cls, *args, ring=...) -> Self:
        ...
    
    @classmethod
    def from_list(cls, rows, cols, items, gens, ring) -> Self:
        ...
    
    @classmethod
    def from_dm(cls, dm) -> Self:
        ...
    
    def to_Matrix(self):
        ...
    
    @classmethod
    def from_Matrix(cls, other, *gens, ring=...) -> Self:
        ...
    
    def set_gens(self, gens) -> Self:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @property
    def shape(self):
        ...
    
    @property
    def rows(self):
        ...
    
    @property
    def cols(self):
        ...
    
    def __len__(self):
        ...
    
    def __getitem__(self, key) -> list[Any] | Any | Self:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __add__(self, other) -> Self | NotImplementedType:
        ...
    
    def __sub__(self, other) -> Self | NotImplementedType:
        ...
    
    def __mul__(self, other) -> Self | NotImplementedType:
        ...
    
    def __rmul__(self, other) -> Self | NotImplementedType:
        ...
    
    def __truediv__(self, other) -> NotImplementedType | Self:
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def transpose(self) -> Self:
        ...
    
    def row_join(self, other) -> Self:
        ...
    
    def col_join(self, other) -> Self:
        ...
    
    def applyfunc(self, func) -> Self:
        ...
    
    @classmethod
    def eye(cls, n, gens) -> Self:
        ...
    
    @classmethod
    def zeros(cls, m, n, gens) -> Self:
        ...
    
    def rref(self, simplify=..., normalize_last=...) -> tuple[Self, Any]:
        ...
    
    def nullspace(self) -> list[Self]:
        ...
    
    def rank(self):
        ...
    


PolyMatrix = MutablePolyMatrix = MutablePolyDenseMatrix

from typing import Any, Iterator, Literal

class intervalMembership:
    def __init__(self, a, b) -> None:
        ...
    
    def __getitem__(self, i) -> Any:
        ...
    
    def __len__(self) -> Literal[2]:
        ...
    
    def __iter__(self) -> Iterator[Any]:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __and__(self, other) -> intervalMembership:
        ...
    
    def __or__(self, other) -> intervalMembership:
        ...
    
    def __invert__(self) -> intervalMembership:
        ...
    
    def __xor__(self, other) -> intervalMembership:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    



from typing import Any, Generator, Self
from sympy.core.basic import Basic
def iterargs(expr) -> Generator[Any, Any, None]:
    ...

def iterfreeargs(expr, _first=...) -> Generator[Any, Any, None]:
    ...

class preorder_traversal:
    def __init__(self, node, keys=...) -> None:
        ...
    
    def skip(self) -> None:
        ...
    
    def __next__(self):
        ...
    
    def __iter__(self) -> Self:
        ...
    


def use(expr, func, level=..., args=..., kwargs=...):
    ...

def walk(e, *target) -> Generator[Any, Any, None]:
    ...

def bottom_up(rv, F, atoms=..., nonbasic=...):
    ...

def postorder_traversal(node, keys=...) -> Generator[Any | Basic, Any, None]:
    ...


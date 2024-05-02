from typing import Literal

from sympy.core.core import Registry

class SingletonRegistry(Registry):
    __slots__ = ...
    __call__ = ...
    def __init__(self) -> None:
        ...
    
    def register(self, cls) -> None:
        ...
    
    def __getattr__(self, name):
        ...
    
    def __repr__(self) -> Literal['S']:
        ...
    


S = ...
class Singleton(type):
    def __init__(cls, *args, **kwargs) -> None:
        ...
    



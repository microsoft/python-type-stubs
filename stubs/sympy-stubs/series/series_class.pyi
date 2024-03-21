from typing import Any, Generator
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.cache import cacheit

class SeriesBase(Expr):
    @property
    def interval(self):
        ...
    
    @property
    def start(self):
        ...
    
    @property
    def stop(self):
        ...
    
    @property
    def length(self):
        ...
    
    @property
    def variables(self) -> tuple[()]:
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    
    @cacheit
    def term(self, pt):
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def __getitem__(self, index) -> list[Any] | None:
        ...
    



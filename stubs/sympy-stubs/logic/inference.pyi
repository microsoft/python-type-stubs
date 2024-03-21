from typing import Any, Generator, Literal, NoReturn

def literal_symbol(literal) -> bool:
    ...

def satisfiable(expr, algorithm=..., all_models=..., minimal=...) -> dict[Any, Any] | Generator[bool, None, None] | Generator[Any | Literal[False], Any, None] | Generator[dict[Any, Any] | Literal[False], Any, None] | Generator[dict[Any, Any] | Literal[False], Any, NoReturn] | Literal[False]:
    ...

def valid(expr) -> bool:
    ...

def pl_true(expr, model=..., deep=...) -> bool | None:
    ...

def entails(expr, formula_set=...) -> bool:
    ...

class KB:
    def __init__(self, sentence=...) -> None:
        ...
    
    def tell(self, sentence):
        ...
    
    def ask(self, query):
        ...
    
    def retract(self, sentence):
        ...
    
    @property
    def clauses(self) -> list[Any]:
        ...
    


class PropKB(KB):
    def tell(self, sentence) -> None:
        ...
    
    def ask(self, query) -> bool:
        ...
    
    def retract(self, sentence) -> None:
        ...
    



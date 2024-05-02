from typing import Any

class RewritingSystem:
    def __init__(self, group) -> None:
        ...
    
    def set_max(self, n) -> None:
        ...
    
    @property
    def is_confluent(self) -> bool:
        ...
    
    def add_rule(self, w1, w2, check=...) -> set[Any]:
        ...
    
    def make_confluent(self, check=...) -> bool | None:
        ...
    
    def reduce(self, word, exclude=...):
        ...
    
    def construct_automaton(self) -> None:
        ...
    
    def reduce_using_automaton(self, word):
        ...
    



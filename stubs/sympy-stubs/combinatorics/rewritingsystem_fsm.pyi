from typing import LiteralString
class State:
    def __init__(self, name, state_machine, state_type=..., rh_rule=...) -> None:
        ...
    
    def add_transition(self, letter, state) -> None:
        ...
    


class StateMachine:
    def __init__(self, name, automaton_alphabet) -> None:
        ...
    
    def add_state(self, state_name, state_type=..., rh_rule=...) -> None:
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    



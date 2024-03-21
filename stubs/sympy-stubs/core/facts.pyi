from collections import defaultdict
from typing import Any, Iterator

def transitive_closure(implications) -> set[Any]:
    ...

def deduce_alpha_implications(implications) -> defaultdict[Any, set[Any]]:
    ...

def apply_beta_to_alpha_route(alpha_implications, beta_rules) -> dict[Any, Any]:
    ...

def rules_2prereq(rules) -> defaultdict[Any, set[Any]]:
    ...

class TautologyDetected(Exception):
    ...


class Prover:
    def __init__(self) -> None:
        ...
    
    def split_alpha_beta(self) -> tuple[list[Any], list[Any]]:
        ...
    
    @property
    def rules_alpha(self) -> list[Any]:
        ...
    
    @property
    def rules_beta(self) -> list[Any]:
        ...
    
    def process_rule(self, a, b) -> None:
        ...
    


class FactRules:
    def __init__(self, rules) -> None:
        ...
    
    def print_rules(self) -> Iterator[str]:
        ...
    


class InconsistentAssumptions(ValueError):
    def __str__(self) -> str:
        ...
    


class FactKB(dict):
    def __str__(self) -> str:
        ...
    
    def __init__(self, rules) -> None:
        ...
    
    def deduce_all_facts(self, facts) -> None:
        ...
    



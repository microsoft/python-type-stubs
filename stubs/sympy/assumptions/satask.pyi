from typing import Any
from sympy.assumptions.cnf import CNF, EncodedCNF

def satask(proposition, assumptions=..., context=..., use_known_facts=..., iterations=...) -> bool | None:
    ...

def check_satisfiability(prop, _prop, factbase) -> bool | None:
    ...

def extract_predargs(proposition, assumptions=..., context=...) -> set[Any]:
    ...

def find_symbols(pred) -> set[Any]:
    ...

def get_relevant_clsfacts(exprs, relevant_facts=...) -> tuple[Any, CNF | Any]:
    ...

def get_all_relevant_facts(proposition, assumptions, context, use_known_facts=..., iterations=...) -> EncodedCNF:
    ...


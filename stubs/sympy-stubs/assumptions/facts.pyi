from typing import Any
from sympy.core.cache import cacheit
from sympy.core.logic import And

@cacheit
def get_composite_predicates() -> dict[Any, Any]:
    ...

@cacheit
def get_known_facts(x=...) -> And:
    ...

def generate_known_facts_dict(keys, fact) -> dict[Any, Any]:
    ...

@cacheit
def get_known_facts_keys() -> list[Any]:
    ...

def single_fact_lookup(known_facts_keys, known_facts_cnf) -> dict[Any, Any]:
    ...

def ask_full_inference(proposition, assumptions, known_facts_cnf) -> bool | None:
    ...


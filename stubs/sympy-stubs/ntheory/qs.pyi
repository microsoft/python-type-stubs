from typing import Any, Literal
rgen = ...
class SievePolynomial:
    def __init__(self, modified_coeff=..., a=..., b=...) -> None:
        ...
    
    def eval(self, x) -> Literal[0]:
        ...
    


class FactorBaseElem:
    def __init__(self, prime, tmem_p, log_p) -> None:
        ...
    


def qs(N, prime_bound, M, ERROR_TERM=..., seed=...) -> set[Any]:
    ...


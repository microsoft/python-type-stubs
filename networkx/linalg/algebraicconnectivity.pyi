from functools import partial

from ..classes.graph import Graph
from ..utils import (
    not_implemented_for,
    np_random_state,
    reverse_cuthill_mckee_ordering,
)

__all__ = ["algebraic_connectivity", "fiedler_vector", "spectral_ordering"]

class _PCGSolver:
    def __init__(self, A, M): ...
    def solve(self, B, tol): ...
    def _solve(self, b, tol): ...

class _LUSolver:
    def __init__(self, A): ...
    def solve(self, B, tol=None): ...

@np_random_state(5)
def algebraic_connectivity(
    G: Graph,
    weight="weight",
    normalized=False,
    tol=1e-8,
    method="tracemin_pcg",
    seed=None,
) -> float: ...
@np_random_state(5)
def fiedler_vector(
    G: Graph,
    weight="weight",
    normalized=False,
    tol=1e-8,
    method="tracemin_pcg",
    seed=None,
): ...
@np_random_state(5)
def spectral_ordering(
    G: Graph,
    weight="weight",
    normalized=False,
    tol=1e-8,
    method="tracemin_pcg",
    seed=None,
): ...

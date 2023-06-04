from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = [
    "powerlaw_sequence",
    "zipf_rv",
    "cumulative_distribution",
    "discrete_sequence",
    "random_weighted_sample",
    "weighted_choice",
]

# The same helpers for choosing random sequences from distributions
# uses Python's random module
# https://docs.python.org/3/library/random.html

@py_random_state(2)
def powerlaw_sequence(n, exponent=2.0, seed=None): ...
@py_random_state(2)
def zipf_rv(alpha: float, xmin: int = 1, seed=None) -> int: ...
def cumulative_distribution(distribution): ...
@py_random_state(3)
def discrete_sequence(n, distribution=None, cdistribution=None, seed=None): ...
@py_random_state(2)
def random_weighted_sample(mapping, k, seed=None): ...
@py_random_state(1)
def weighted_choice(mapping, seed=None): ...

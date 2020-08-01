from random import Random
from typing import Any, Generator, Iterator, Optional, Sequence, TypeVar

_T = TypeVar("_T")

def random_sample(random: Optional[Random] = ...) -> float: ...
def cumsum(it: Iterator[float]) -> Generator: ...
def choices_distribution_unique(
    a: Sequence[_T],
    p: Sequence[float],
    random: Optional[Random] = ...,
    length: int = ...,
) -> Sequence[_T]: ...
def choices_distribution(
    a: Sequence[_T],
    p: Sequence[float],
    random: Optional[Random] = ...,
    length: int = ...,
) -> Sequence[_T]: ...

from typing import Callable, TypeVar

from tensorflow.data import Dataset

AUTOTUNE: int
INFINITE_CARDINALITY: int
SHARD_HINT: int
UNKNOWN_CARDINALITY: int

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

def parallel_interleave(
    map_func: Callable[[_T1], Dataset[_T2]],
    cycle_length: int,
    block_length: int = 1,
    sloppy: bool | None = False,
    buffer_output_elements: int | None = None,
    prefetch_input_elements: int | None = None,
) -> Callable[[Dataset[_T1]], Dataset[_T2]]: ...

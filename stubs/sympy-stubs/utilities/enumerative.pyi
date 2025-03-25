from collections.abc import Generator
from typing import Any

class PartComponent:
    __slots__ = ...
    def __init__(self) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

def multiset_partitions_taocp(multiplicities) -> Generator[list[Any], Any, None]: ...
def factoring_visitor(state, primes) -> list[Any]: ...
def list_visitor(state, components) -> list[Any]: ...

class MultisetPartitionTraverser:
    def __init__(self) -> None: ...
    def db_trace(self, msg) -> None: ...
    def decrement_part(self, part) -> bool: ...
    def decrement_part_small(self, part, ub) -> bool: ...
    def decrement_part_large(self, part, amt, lb) -> bool | None: ...
    def decrement_part_range(self, part, lb, ub) -> bool | None: ...
    def spread_part_multiplicity(self) -> bool: ...
    def top_part(self) -> list[PartComponent]: ...
    def enum_all(self, multiplicities) -> Generator[list[Any], Any, None]: ...
    def enum_small(self, multiplicities, ub) -> Generator[list[Any], Any, None]: ...
    def enum_large(self, multiplicities, lb) -> Generator[list[Any], Any, None]: ...
    def enum_range(self, multiplicities, lb, ub) -> Generator[list[Any], Any, None]: ...
    def count_partitions_slow(self, multiplicities) -> int: ...
    def count_partitions(self, multiplicities) -> int: ...

def part_key(part) -> tuple[Any, ...]: ...

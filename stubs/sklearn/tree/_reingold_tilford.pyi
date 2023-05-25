from numpy import ndarray, longlong

# Authors: William Mill (bill@billmill.org)
# License: BSD 3 clause

import numpy as np


class DrawTree:
    def __init__(
        self,
        tree: Tree,
        parent: DrawTree | None = None,
        depth: int = 0,
        number: int = 1,
    ) -> None:
        ...

    def left(self) -> DrawTree | int:
        ...

    def right(self) -> DrawTree | int:
        ...

    def lbrother(self) -> DrawTree | None:
        ...

    def get_lmost_sibling(self) -> DrawTree | None:
        ...

    lmost_sibling = ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def max_extents(self) -> ndarray:
        ...


def buchheim(tree: Tree) -> DrawTree:
    ...


def third_walk(tree: DrawTree, n: float) -> None:
    ...


def first_walk(v: DrawTree, distance: float = 1.0) -> DrawTree:
    ...


def apportion(v: DrawTree, default_ancestor: DrawTree, distance: float) -> DrawTree:
    ...


def move_subtree(wl: DrawTree, wr: DrawTree, shift: float) -> None:
    ...


def execute_shifts(v: DrawTree) -> None:
    ...


def ancestor(vil: DrawTree, v: DrawTree, default_ancestor: DrawTree) -> DrawTree:
    ...


def second_walk(
    v: DrawTree, m: float | int = 0, depth: int = 0, min: float | None = None
) -> float:
    ...


class Tree:
    def __init__(
        self, label: str = "", node_id: longlong | int = ..., *children
    ) -> None:
        ...

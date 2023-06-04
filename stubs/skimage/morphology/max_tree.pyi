from numpy.typing import NDArray

import numpy as np

from ._util import _validate_connectivity, _offsets_to_raveled_neighbors

unsigned_int_types: list = ...
signed_int_types: list = ...
signed_float_types: list = ...

# building the max tree.
def max_tree(image: NDArray, connectivity=1): ...
def area_opening(
    image: NDArray, area_threshold=64, connectivity=1, parent=None, tree_traverser=None
) -> NDArray: ...
def diameter_opening(
    image: NDArray,
    diameter_threshold=8,
    connectivity=1,
    parent=None,
    tree_traverser=None,
) -> NDArray: ...
def area_closing(
    image: NDArray, area_threshold=64, connectivity=1, parent=None, tree_traverser=None
) -> NDArray: ...
def diameter_closing(
    image: NDArray,
    diameter_threshold=8,
    connectivity=1,
    parent=None,
    tree_traverser=None,
) -> NDArray: ...
def max_tree_local_maxima(
    image: NDArray, connectivity=1, parent=None, tree_traverser=None
): ...
